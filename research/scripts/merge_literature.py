"""역할별 문헌 원본을 보존하며 병합한다. 내용 검증을 자동으로 대체하지 않는다."""
from pathlib import Path
import csv
import json
import re
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
FIELDS = '''paper_id title authors year venue doi_or_arxiv official_url version
source_verified full_text_access discussion_access domain axis_tags original_rq
dataset stimulus brain_measurement model_method training_objective main_findings
scientific_contribution limitations future_directions future_direction_source_location
transfer_idea relevant_datasets novelty_risk evidence_level agent verification_date'''.split()

def normalized_title(s):
    return re.sub(r'[^\w]', '', unicodedata.normalize('NFKC', s).casefold())

def identifiers(row):
    s = row.get('doi_or_arxiv', '')
    ids = set()
    for x in re.findall(r'10\.\d{4,9}/[^\s;,|]+', s, re.I):
        ids.add(x.lower().rstrip('.)'))
    for x in re.findall(r'\b\d{4}\.\d{4,5}(?:v\d+)?\b', s):
        ids.add(re.sub(r'v\d+$', '', x))
    return ids

def main():
    rows, issues = [], []
    source_paths = sorted((ROOT / 'agents').glob('*/papers.csv'))
    supplement = ROOT / 'literature/coordinator_papers.csv'
    if supplement.exists():
        source_paths.append(supplement)
    for path in source_paths:
        with path.open(encoding='utf-8-sig', newline='') as f:
            reader = csv.DictReader(f)
            missing = sorted(set(FIELDS) - set(reader.fieldnames or []))
            if missing:
                issues.append({'file': str(path.relative_to(ROOT)), 'missing_columns': missing})
            for row in reader:
                if None in row:
                    issues.append({'file': str(path.relative_to(ROOT)), 'malformed_csv': row.get('paper_id')})
                    row.pop(None)
                row = {k: v or '' for k, v in row.items()}
                row['source_file'] = str(path.relative_to(ROOT))
                rows.append(row)
    # DOI/arXiv 또는 정규화한 동일 제목으로 병합. 다른 버전의 수동 감사는 별도 필요.
    groups = []
    for row in rows:
        ids, title = identifiers(row), normalized_title(row.get('title', ''))
        hits = [g for g in groups if (ids and ids & g['ids']) or (title and title in g['titles'])]
        if hits:
            group = hits[0]
            for other in hits[1:]:
                group['rows'] += other['rows']
                group['ids'] |= other['ids']
                group['titles'] |= other['titles']
                groups.remove(other)
        else:
            group = {'rows': [], 'ids': set(), 'titles': set()}
            groups.append(group)
        group['rows'].append(row)
        group['ids'] |= ids
        group['titles'].add(title)
    all_fields = FIELDS + sorted(set().union(*(set(r) for r in rows)) - set(FIELDS)) if rows else FIELDS
    with (ROOT / 'literature/papers_all_evidence.csv').open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=all_fields)
        writer.writeheader()
        writer.writerows(rows)
    unique = []
    for n, group in enumerate(groups, 1):
        # 지정 본문 직접 확인과 서지 완전성을 우선한다. 다른 근거는 원본에 보존.
        def rank(r):
            full = r.get('full_text_access', '').strip().lower()
            direct = full.startswith(('예', 'yes', 'true'))
            return (direct, sum(bool(r.get(k)) for k in FIELDS))
        row = max(group['rows'], key=rank).copy()
        row['canonical_id'] = f'P{n:03d}'
        row['origin_ids'] = '; '.join(r.get('paper_id', '') for r in group['rows'])
        row['origin_files'] = '; '.join(sorted({r['source_file'] for r in group['rows']}))
        row['identifier_set'] = '; '.join(sorted(group['ids']))
        row['verification_gate'] = '수동 검토 필요'
        unique.append(row)
    fields = all_fields + ['canonical_id', 'origin_ids', 'origin_files', 'identifier_set', 'verification_gate']
    with (ROOT / 'literature/papers.csv').open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(unique)
    result = {'source_rows': len(rows), 'unique_candidates': len(unique), 'source_files': len({r['source_file'] for r in rows}), 'agent_source_files': len({r['source_file'] for r in rows if r['source_file'].startswith('agents/')}), 'issues': issues, 'note': '고유 후보 수는 검증 완료 문헌 수가 아니다. 수동 검토 후 별도 집계한다.'}
    (ROOT / 'literature/merge_audit.json').write_text(json.dumps(result, ensure_ascii=False, indent=2))
    print(json.dumps(result, ensure_ascii=False))

if __name__ == '__main__':
    main()
