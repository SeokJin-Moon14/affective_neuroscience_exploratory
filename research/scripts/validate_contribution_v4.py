#!/usr/bin/env python3
"""v4 출처 보존·실제 검토 연결·입력 조건·현재 문서 링크를 검사한다.

이 검사는 가설의 신규성·효과·검정력을 승인하지 않는다.
"""
from pathlib import Path
from urllib.parse import unquote
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
CHECKS = []


def check(name, ok, detail=''):
    CHECKS.append({'name': name, 'passed': bool(ok), 'detail': detail})


def read(path):
    return json.loads((ROOT / path).read_text())


def walk(value):
    if isinstance(value, dict):
        yield value
        for v in value.values():
            yield from walk(v)
    elif isinstance(value, list):
        for v in value:
            yield from walk(v)


def source_paths(value):
    entries = value if isinstance(value, list) else value.split(';')
    return [e.strip().split(': ', 1)[0] for e in entries]


def main():
    catalog = read('revision_v4/catalog.json')
    curation = read('revision_v4/curation.json')
    required = '''candidate_id question why_needed primary_data secondary_data data_binding decisive_comparison
        competing_accounts decisive_result conclusion_if_supported conclusion_if_alternative noncontribution_result
        field_impact contribution_type analysis_plan ai_enables existing_data_only new_observations_needed nearest_prior
        strongest_objection response_to_objection claim_limit minimum_pilot abandon_if uncertainty excluded_scope_check
        revision_decision response_log'''.split()
    ids = [c['candidate_id'] for c in catalog]
    check('후보 ID 고유성', len(ids) == len(set(ids)))
    for f in ['INITIAL_SOURCES.json', 'PERCEPTION_SOURCES.json', 'ADDITIONAL_SOURCES.json', 'FINAL_AUTHOR_SOURCES.json']:
        for item in read('revision_v4/' + f):
            p = ROOT / item['path']
            actual = hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None
            check('원문 해시 ' + item['path'], actual == item['sha256'])

    reviews = {}
    review_files = set(ROOT.glob('agents/*/revision_v4_peer_review*.json'))
    review_files.update(ROOT.glob('agents/*/revision_v4_review_D*.json'))
    review_files.update([ROOT / 'agents/01_dataset/revision_v4_data_review.json',
                         ROOT / 'agents/01_dataset/revision_v4_additional_data_reviews.json'])
    for path in sorted(review_files):
        for r in walk(json.loads(path.read_text())):
            if 'review_id' in r and ('candidate_id' in r or 'candidate_ids' in r):
                targets = r.get('candidate_ids', [r.get('candidate_id')])
                reviews.setdefault(r['review_id'], set()).update(targets)
    for c in catalog:
        cid = c['candidate_id']
        check(cid + ' 필수 원고 필드', all(k in c and c[k] is not None for k in required))
        check(cid + ' 기존 관측', c['existing_data_only'] is True and c['new_observations_needed'] == [])
        check(cid + ' 데이터 심사', cid in reviews.get('DATA-V4-' + cid, set()))
        response_ids = {r['review_id'] for r in c['response_log']}
        check(cid + ' 실제 과학 비판에 대한 응답', any(cid in reviews.get(r, set()) for r in response_ids if not r.startswith('DATA-')))
        check(cid + ' 데이터 심사 응답', 'DATA-V4-' + cid in response_ids)
        for b in c['data_binding']:
            for path in source_paths(b['source_path']):
                check(cid + ' 근거 ' + path, (ROOT / path).is_file())
    classified = [cid for g in curation['directions'] + curation['held'] for cid in g.get('candidate_ids', [])]
    check('원안 전체 선정 또는 보류 기록', set(classified) == set(ids))
    check('중복 집계 없음', len(classified) == len(set(classified)))
    by_id = {c['candidate_id']: c for c in catalog}
    for g in curation['directions']:
        check(g['direction_id'] + ' 새 관측 불필요', all(by_id[c]['existing_data_only'] and not by_id[c]['new_observations_needed'] for c in g['candidate_ids']))
        check(g['direction_id'] + ' 네 기여 항목', all(g[k].strip() for k in ['why_short', 'result_short', 'conclusion_short', 'impact_short']))
    metadata = read('pilots/v4/metadata_check.json')
    check('공개 메타데이터 실제 검산', all(metadata['checks'].values()))
    check('뇌 분석 미실행 표기', read('revision_v4/version.json')['experiments_run'] is False)
    plans = read('pilots/plans.json')
    check('선정 방향별 파일럿 계획', {p['direction_id'] for p in plans['pilots']} == {g['direction_id'] for g in curation['directions']})

    docs = set(ROOT.glob('proposals/D*.md')) | set(ROOT.glob('revision_v4/*.md')) | set(ROOT.glob('pilots/v4/*.md'))
    docs |= set(ROOT.glob('discussions/revision_v4/*.md'))
    docs |= {ROOT / s for s in ['START_HERE.md', 'RESEARCH_STATUS.md', 'CHATGPT_PROJECT_BRIEF.md',
                              'proposals/README.md', 'pilots/README.md', 'research_questions/README.md',
                              'research_questions/LANDSCAPE.md', 'research_questions/RANKINGS.md',
                              'synthesis/FINAL_REPORT.md', 'synthesis/FINAL_AUDIT.md',
                              'synthesis/DIVERSITY_AUDIT.md', 'synthesis/OPPORTUNITY_MAP.md']}
    links = 0
    for doc in sorted(docs):
        check('현재 문서 존재 ' + str(doc.relative_to(ROOT)), doc.exists())
        if not doc.exists():
            continue
        for link in re.findall(r'\]\(([^)]+)\)', doc.read_text()):
            if re.match(r'(https?://|mailto:|#)', link):
                continue
            target = unquote(link.split('#', 1)[0].split(' "', 1)[0].strip('<>'))
            path = doc.parent / target
            links += 1
            check('문서 링크 ' + str(doc.relative_to(ROOT)) + ' → ' + target, path.exists())
    report = {'scope': '출처·필드·실제 검토 연결·현재 문서 링크와 공개 메타데이터 검산. 과학적 효과·신규성 승인이 아님.',
              'candidate_count': len(catalog), 'direction_count': len(curation['directions']),
              'check_count': len(CHECKS), 'local_links_checked': links,
              'failed': [c for c in CHECKS if not c['passed']], 'checks': CHECKS}
    (ROOT / 'synthesis/validation_report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: v for k, v in report.items() if k != 'checks'}, ensure_ascii=False))
    if report['failed']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
