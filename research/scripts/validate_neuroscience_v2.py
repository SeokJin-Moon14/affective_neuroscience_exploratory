#!/usr/bin/env python3
"""v2 기획의 파일 일치·서지 참조·내부 링크 확인. 과학적 타당성 자동 판정은 아니다."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import re
import urllib.parse

r = Path(__file__).resolve().parents[1]
if (r / 'revision_v3/version.json').exists():
    raise SystemExit('현재 문서는 v3입니다. v2 검증 결과는 archive/v2에 보존되어 있으며 현재 문서를 판정하지 않습니다.')
cards = json.loads((r / 'revision_v2/cards.json').read_text())
pilots = json.loads((r / 'revision_v2/pilots.json').read_text())
papers = {p['canonical_id']: p for p in csv.DictReader((r / 'literature/papers.csv').open())}
errors = []
checks = []


def check(condition, label):
    checks.append(label)
    if not condition:
        errors.append(label)


check([c['proposal_id'] for c in cards] == [f'RP{i:02}' for i in range(1, 11)], '현재 선정한 제안 10개의 ID 중복·누락')
check([c['rq_id'] for c in cards] == [f'NQ{i:02}' for i in range(1, 11)], 'v1과 구별한 새 질문 ID')
check(len({c['title'] for c in cards}) == len(cards), '제목 중복')
by_id = {c['proposal_id']: c for c in cards}
required = {'proposal_id', 'rq_id', 'title', 'summary', 'why', 'hypotheses', 'neural_targets', 'approach',
            'outcomes', 'data', 'limits', 'literature', 'novelty', 'first_step', 'previous_links', 'feasibility'}
banned_openers = ['사전 고정한 내용모형', '사전허용집합', '사전 허용집합', '정서 경계 초과거리',
                  '고정 parcel 평균', '정서 대비 판독 접근성', '정서관련편집']
for c in cards:
    pid = c['proposal_id']
    check(required <= set(c), pid + ' 필수 원고 필드')
    check(c['title'].endswith('?'), pid + ' 질문형 제목')
    check(not any(w in c['title'] + c['summary'] for w in banned_openers), pid + ' 문제로 지적된 표현 제거')
    check(len(c['hypotheses']) >= 2 and len(c['outcomes']) >= 3, pid + ' 경쟁 설명과 여러 결과 해석')
    check(all({'explanation', 'prediction'} <= set(h) for h in c['hypotheses']), pid + ' 설명과 관찰 예측 연결')
    check(all(ref['id'] in papers for ref in c['literature']), pid + ' 실제 문헌 장부 참조')
    check(len(set(ref['id'] for ref in c['literature'])) == len(c['literature']), pid + ' 중복 문헌 없음')
    content = (r / f'proposals/{pid}.md').read_text()
    check(content.startswith('# ' + c['title'] + '\n'), pid + ' 렌더링 제목 일치')
    check(c['summary'] in content and c['why'] in content, pid + ' 원고와 독자 문서 일치')
for p in pilots:
    c = by_id[p['proposal_id']]
    check(c['rq_id'] == p['rq_id'], p['pilot_id'] + ' 질문·제안 대응')
    check('아직' in p['status'] and '수행하지 않음' in p['status'], p['pilot_id'] + ' 미실행 상태 명시')
check(json.loads((r/'proposals/cards.json').read_text()) == cards, '제안 JSON 정본과 복사본 일치')
check(json.loads((r/'pilots/plans.json').read_text()) == pilots, '파일럿 JSON 정본과 복사본 일치')

files = [r / p for p in ['START_HERE.md', 'RESEARCH_STATUS.md', 'CHATGPT_PROJECT_BRIEF.md', 'BUNDLE_CONTENTS.md',
         'research_questions/README.md', 'research_questions/LANDSCAPE.md', 'research_questions/RANKINGS.md',
         'literature/REVISION_V2_SOURCES.md', 'literature/novelty/REVISION_V2_REVIEW.md', 'revision_v2/CHANGELOG.md',
         'archive/v1/README.md', 'synthesis/FINAL_REPORT.md', 'synthesis/FINAL_AUDIT.md',
         'synthesis/OPPORTUNITY_MAP.md', 'synthesis/DIVERSITY_AUDIT.md']]
files += sorted((r / 'proposals').glob('*.md')) + sorted((r / 'pilots').glob('*.md'))
missing = []
link_count = 0
for f in files:
    check(f.is_file(), str(f.relative_to(r)) + ' 존재')
    if not f.is_file():
        continue
    for raw in re.findall(r'\]\(([^)]+)\)', f.read_text()):
        if raw.startswith(('http:', 'https:', 'mailto:', '#')):
            continue
        target = urllib.parse.unquote(raw.split('#')[0].strip('<>'))
        if not target:
            continue
        link_count += 1
        if not (f.parent / target).resolve().exists():
            missing.append({'file': str(f.relative_to(r)), 'target': target})
check(not missing, '현재 독자 문서의 내부 링크')
source = json.loads((r / 'skills/humanizer/SOURCE.json').read_text())
check(hashlib.sha256((r / 'skills/humanizer/SKILL.md').read_bytes()).hexdigest() == source['sha256'], 'humanizer 출처 파일 해시')
archive = json.loads((r / 'archive/v1/manifest.json').read_text())
check(all((r / 'archive/v1' / f['path']).exists() for f in archive['files']), '이전 산출물 보존')
check(archive['source_commit'] == 'bee5c041fca8ff8a6dcf99c9c8906252c2cbe2a6', '이전 원격 커밋 식별')
scope = '현재 원고·렌더링의 일치, 문헌 ID와 내부 파일 링크. 한국어 자연스러움·과학적 타당성·신규성은 자동 검증 범위가 아님. 외부 링크 응답이나 실험 실행을 검사하지 않음.'
report = {'version': 2, 'checked_at': datetime.now(timezone.utc).isoformat(), 'checks': len(checks),
          'proposals': len(cards), 'pilot_plans': len(pilots), 'files_checked': len(files),
          'internal_links_checked': link_count, 'errors': errors, 'missing_links': missing, 'scope': scope}
(r / 'synthesis/validation_report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
(r / 'synthesis/link_check.json').write_text(json.dumps({'version': 2, 'files_checked': len(files), 'links_checked': link_count, 'missing': missing}, ensure_ascii=False, indent=2) + '\n')
manifest = {'version': 2, 'scope': '현재 독자 문서', 'files': [
    {'path': str(f.relative_to(r)), 'sha256': hashlib.sha256(f.read_bytes()).hexdigest()} for f in files if f.is_file()]}
(r / 'synthesis/deliverables_manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(report, ensure_ascii=False))
if errors:
    raise SystemExit(1)
