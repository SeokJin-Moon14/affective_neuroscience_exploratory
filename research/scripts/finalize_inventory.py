"""Coordinator가 검토한 서지 보류 사유와 원문 접근 범위를 집계한다."""
from pathlib import Path
import csv
import json
import re

ROOT = Path(__file__).resolve().parents[1]
PENDING = {
    'A01-SPACETOP2024': '공식 Authors 배열과 HowToAcknowledge 저자 표기 충돌; 정식 서지 대조 필요',
    'G07-P08': '공식 README 본문 저자열과 BibTeX 저자열 충돌; 명단 확정 보류',
    'BI03': '발표연도·최종 출판연도 미확인',
}

def direct(text):
    text = text.strip()
    if text.lower().startswith(('예', 'yes', 'true')):
        return True
    if re.search(r'아니|미열람|미접근|미확인|미검토', text):
        return False
    return '직접' in text and any(x in text for x in ['PDF', '본문', '읽', '검토', '확인'])

def write_csv(path, fields, rows):
    with path.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

def main():
    with (ROOT / 'literature/papers.csv').open(encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fields, rows = reader.fieldnames, list(reader)
    verified, pending = [], []
    for row in rows:
        ids = set(row['origin_ids'].split('; '))
        reasons = [reason for key, reason in PENDING.items() if key in ids]
        row['verification_gate'] = '보류: ' + '; '.join(reasons) if reasons else '서지·출처 확인; 본문 검증 범위는 별도 열 참조'
        (pending if reasons else verified).append(row)
    for name, data in [('papers.csv', rows), ('verified_papers.csv', verified), ('pending_verification.csv', pending)]:
        write_csv(ROOT / 'literature' / name, fields, data)
    full = [r for r in verified if direct(r['full_text_access'])]
    discussion = [r for r in verified if direct(r['discussion_access'])]
    mining = []
    for row in discussion:
        author = row['future_directions']
        # 원 Agent가 한 셀에 함께 쓴 추론을 저자 발언과 분리한다.
        author = author.split('Agent E3:')[0].strip()
        no_explicit = '별도 추출하지 않음' in author or '추가 추출 없음' in author
        mining.append({
            'canonical_id': row['canonical_id'], 'origin_ids': row['origin_ids'],
            'title': row['title'], 'author_future_direction': author,
            'author_future_direction_extracted': '아니오' if no_explicit else '예',
            'source_location': row['future_direction_source_location'],
            'agent_transfer_E3': row['transfer_idea'], 'discussion_access': row['discussion_access'],
            'official_url': row['official_url'], 'origin_files': row['origin_files'],
            'verification_date': '2026-11-12',
        })
    if mining:
        write_csv(ROOT / 'literature/discussion_mining.csv', list(mining[0]), mining)
    merge = json.loads((ROOT / 'literature/merge_audit.json').read_text())
    summary = {
        'date': '2026-11-12', 'role_count': merge.get('agent_source_files', merge['source_files']),
        'source_rows': merge['source_rows'], 'unique_candidates': len(rows),
        'bibliographically_verified': len(verified), 'pending': len(pending),
        'full_text_or_selected_sections_checked': len(full),
        'discussion_limitations_or_conclusion_checked': len(discussion),
        'author_future_direction_records': sum(r['author_future_direction_extracted'] == '예' for r in mining),
        'verification_target': 100, 'strict_pending_reasons': PENDING,
        'notes': f'서지 확인 {len(verified)}편은 원문 {len(verified)}편을 읽었다는 뜻이 아니다. 보류 후보는 목표 수에서 제외했다.',
    }
    (ROOT / 'literature/verification_summary.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2))
    print(json.dumps(summary, ensure_ascii=False))

if __name__ == '__main__':
    main()
