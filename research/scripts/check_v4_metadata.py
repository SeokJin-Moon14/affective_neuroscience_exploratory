#!/usr/bin/env python3
"""공개 MC 이벤트와 기존 사람 캡션에서 v4의 ID·분할 조건을 재검산한다.

뇌 배열·정서 평정·모든 참가자의 자료를 검사하는 스크립트가 아니다.
"""
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVENTS = ROOT / 'agents/01_dataset/evidence/revision_v4/mc_sub01_events'
CAPTIONS = ROOT / 'datasets/mind_captioning/evidence/caption_ck20.csv'
EXCLUDED = {1, 4, 5, 6, 7, 8, 11, 859, 866, 1673, 2157, 2187, 2188, 2194, 2195}


def rows(path):
    with path.open(encoding='utf-8-sig') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def positive_ids(records, key):
    return [int(float(r[key])) for r in records if float(r.get(key, 0)) > 0]


def main():
    files = sorted(EVENTS.glob('*.tsv'))
    if not files or not CAPTIONS.exists():
        raise SystemExit('검산에 필요한 보존된 공개 메타데이터가 없습니다.')
    grouped = {}
    for task in ('trainPerception', 'testPerception', 'testImagery'):
        fs = [p for p in files if f'_task-{task}_' in p.name]
        key = 'imageryID' if task == 'testImagery' else 'stimID'
        ids = [v for p in fs for v in positive_ids(rows(p), key)]
        grouped[task] = {'files': fs, 'ids': ids, 'set': set(ids)}
    train, test, imagery = [grouped[x] for x in ('trainPerception', 'testPerception', 'testImagery')]
    held = [p for p in train['files'] if 'ses-trainPerception10_' in p.name
            and any(f'_run-{n:02d}_' in p.name for n in (6, 7))]
    held_ids = [v for p in held for v in positive_ids(rows(p), 'stimID')]
    clean_files = [p for p in train['files'] if p not in held]
    clean_ids = [v for p in clean_files for v in positive_ids(rows(p), 'stimID')]
    with CAPTIONS.open(encoding='utf-8-sig') as f:
        counts = Counter(int(r['video_id']) for r in csv.DictReader(f))
    tests = {
        'test_and_first_imagery_session_same_ids': test['set'] == imagery['set'],
        'last_two_train_runs_are_test_ids': set(held_ids) == test['set'],
        'clean_train_and_test_disjoint': not (set(clean_ids) & test['set']),
        'all_observed_original_ids_have_captions': set(counts).issuperset(train['set'] | test['set'] | imagery['set']),
        'test_perception_five_observed_repetitions': set(Counter(test['ids']).values()) == {5},
    }
    report = {
        'scope': 'sub-01: raw train60런, testPerception10런, testImagery 첫 세션6런',
        'source_hashes': {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                          for p in files + [CAPTIONS]},
        'tasks': {k: {'run_files': len(v['files']), 'blocks': len(v['ids']),
                      'unique_original_ids': len(v['set']),
                      'repetition_histogram': dict(Counter(Counter(v['ids']).values()))}
                  for k, v in grouped.items()},
        'caption_rows': sum(counts.values()), 'caption_original_ids': len(counts),
        'caption_count_histogram': dict(Counter(counts.values())),
        'raw_train_test_overlap': len(train['set'] & test['set']),
        'excluded_train_runs': [p.name for p in held],
        'clean_training_runs': len(clean_files), 'clean_training_ids': len(set(clean_ids)),
        'test_ids_after_horikawa_15_exclusions': sorted(test['set'] - EXCLUDED),
        'eligible_test_id_count_before_further_qc': len(test['set'] - EXCLUDED),
        'checks': tests,
        'not_checked': ['원영상 바이트 일치', '정서 주석 본체와 항목', '특징 행과 원ID',
                        'processed MAT의 심상 집계 구간', '모든 참가자의 유효 반복과 뇌 반응',
                        '실제 정서·내용 관계의 분리 가능성', '효과·검정력·신규성'],
        'brain_experiments_run': False,
    }
    target = ROOT / 'pilots/v4/metadata_check.json'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'checks': tests, 'clean_train': len(set(clean_ids)),
                      'eligible_test_max': len(test['set'] - EXCLUDED),
                      'report': str(target.relative_to(ROOT))}, ensure_ascii=False))
    if not all(tests.values()):
        raise SystemExit(1)


if __name__ == '__main__':
    main()
