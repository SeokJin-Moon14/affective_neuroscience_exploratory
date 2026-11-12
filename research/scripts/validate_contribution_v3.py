#!/usr/bin/env python3
"""v3 파일·검토 이력·참조의 일치만 확인한다. 연구 가치와 신규성은 자동 판정하지 않는다."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import re
from urllib.parse import unquote

R = Path(__file__).resolve().parents[1]
errors, checks = [], []

def read(name):
    return json.loads((R / name).read_text())

def check(condition, label):
    checks.append(label)
    if not condition:
        errors.append(label)

catalog = read('revision_v3/catalog.json')
curation = read('revision_v3/curation.json')
assignments = read('revision_v3/PEER_ASSIGNMENTS.json')
peers = [x['review'] for x in read('revision_v3/peer_reviews.json')]
critic = read('agents/12_adversarial_review/revision_v3_contribution_review.json')
followups = read('agents/12_adversarial_review/revision_v3_response_check.json')
critic += [{'review_id': r['original_review_id'] + '-followup', 'candidate_id': r['candidate_id']}
           for r in followups]
critic += read('revision_v3/COORDINATOR_REVIEW.json')
original = read('revision_v3/independent_candidates.json')
papers = {p['canonical_id'] for p in csv.DictReader((R / 'literature/papers.csv').open())}
ids = [c['candidate_id'] for c in catalog]
check(len(ids) == len(set(ids)), '현재 원고 ID 중복 없음')
check(set(c['candidate_id'] for c in original).issubset(ids), '최초 독립 후보의 발전·통합·보류 기록 보존')

required = {'candidate_id', 'question', 'premise', 'why_needed', 'contribution_type',
            'competing_accounts', 'decisive_result', 'conclusion_if_supported',
            'conclusion_if_alternative', 'noncontribution_result', 'field_impact',
            'minimum_design', 'ai_enables', 'nearest_prior', 'data_scope',
            'strongest_objection', 'response_to_objection', 'relation_to_v2',
            'uncertainty', 'revision_decision', 'response_log'}
review_ids = {r['review_id'] for r in peers + critic}
for c in catalog:
    cid = c['candidate_id']
    check(required.issubset(c) and all(c.get(k) for k in required), cid + ': 필수 원고 항목')
    check(all(r['paper_id'] in papers for r in c['nearest_prior']), cid + ': 실제 문헌 ID 참조')
    response_ids = {r['review_id'] for r in c['response_log']}
    expected = {r['review_id'] for r in peers + critic if r['candidate_id'] == cid}
    check(bool(expected) and expected.issubset(response_ids), cid + ': 실제 비판에 대한 저자 응답')
    check(response_ids.issubset(review_ids), cid + ': 존재하는 검토 ID만 응답')
    check(all(all(r.get(k) for k in ['review_id', 'position', 'substantive_change', 'remaining'])
              for r in c['response_log']), cid + ': 수정과 미해결점 보존')
    check((R / 'proposals' / (cid + '.md')).exists(), cid + ': 읽기용 원고 존재')

for s in assignments['original_sources']:
    check(hashlib.sha256((R / s['path']).read_bytes()).hexdigest() == s['sha256'],
          s['path'] + ': 독립 제안 원본 보존')
for s in read('revision_v3/AUTHOR_SOURCES.json'):
    check(hashlib.sha256((R / s['path']).read_bytes()).hexdigest() == s['sha256'],
          s['path'] + ': 실제 저자 수정본과 통합 시점 일치')
for s in read('revision_v3/ADDITIONAL_ASSIGNMENTS.json').get('original_sources', []):
    check(hashlib.sha256((R / s['path']).read_bytes()).hexdigest() == s['sha256'],
          s['path'] + ': 추가 독립 제안 원본 보존')

grouped = [cid for g in curation['groups'] for cid in g['candidate_ids']]
held = [x['candidate_id'] for x in curation.get('not_advanced', [])]
check(len(grouped) == len(set(grouped)), '통합 방향 간 원안 중복 집계 없음')
check(not set(grouped) & set(held), '발전 그룹과 보류 목록 구별')
check(set(grouped + held) == set(ids), '모든 후보의 최종 처리 기록')
check(read('proposals/cards.json') == catalog, '현재 카드와 정본 일치')

paths = ['START_HERE.md', 'RESEARCH_STATUS.md', 'CHATGPT_PROJECT_BRIEF.md',
         'synthesis/FINAL_REPORT.md', 'synthesis/FINAL_AUDIT.md',
         'synthesis/DIVERSITY_AUDIT.md', 'synthesis/OPPORTUNITY_MAP.md',
         'proposals/README.md', 'pilots/README.md', 'research_questions/README.md',
         'research_questions/LANDSCAPE.md', 'research_questions/RANKINGS.md',
         'revision_v3/CONTRIBUTIONS.md', 'revision_v3/DECISIONS.md',
         'discussions/revision_v3/SYNTHESIS.md', 'literature/REVISION_V3_SOURCES.md']
paths += ['proposals/' + cid + '.md' for cid in ids]
for name in paths:
    p = R / name
    check(p.exists(), name + ': 문서 존재')
    if not p.exists():
        continue
    for link in re.findall(r'\]\(([^)]+)\)', p.read_text()):
        if re.match(r'^[a-z][a-z0-9+.-]*:', link, re.I) or link.startswith('#'):
            continue
        target = unquote(link.split('#')[0].split('?')[0].strip('<>'))
        resolved = (p.parent / target).resolve()
        # 이 실행의 마지막에 작성할 검사 보고서 자체의 링크도 허용한다.
        check(resolved.exists() or resolved == R / 'revision_v3/VALIDATION.json',
              name + ': 내부 링크 ' + target)

report = {'checked_at_utc': datetime.now(timezone.utc).isoformat(),
          'scope': '문서 구조·참조·원본 보존·실제 검토 응답. 과학적 타당성·최초성·실험 결과의 검증 아님.',
          'candidate_manuscripts': len(catalog), 'research_directions': len(curation['groups']),
          'checks': len(checks), 'errors': errors,
          'files_sha256': {n: hashlib.sha256((R / n).read_bytes()).hexdigest() for n in paths if (R / n).exists()}}
(R / 'revision_v3/VALIDATION.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({k: v for k, v in report.items() if k != 'files_sha256'}, ensure_ascii=False, indent=2))
raise SystemExit(bool(errors))
