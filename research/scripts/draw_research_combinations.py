#!/usr/bin/env python3
"""고정된 Axis v1에서 실제 난수를 사용한 독립 조합 30개. 과학 판정은 별도."""
import csv, hashlib, json, random
from datetime import datetime
from zoneinfo import ZoneInfo
from pathlib import Path

root=Path(__file__).resolve().parents[1]
path=root/'axis_map/taxonomy.csv'
taxonomy=list(csv.DictReader(path.open()))
types=['Construct / Stimulus','Neural','Model / Method','Structure / Dynamics','Inference / Measurement']
pools={t:sorted(r['axis_id'] for r in taxonomy if t in json.loads(r['type_tags'])) for t in types}
rng=random.Random(20261112)
seen=set(); attempts=[]; accepted=[]
while len(accepted)<30:
    sampled_types=rng.sample(types,3)
    sampled_axes=[rng.choice(pools[t]) for t in sampled_types]
    key=tuple(sorted(set(sampled_axes)))
    reason='동일 Axis 중복' if len(key)<3 else '이미 추출한 조합' if key in seen else None
    attempt={'attempt':len(attempts)+1,'sampled_types':sampled_types,'sampled_axes':sampled_axes,'redraw_reason':reason}
    attempts.append(attempt)
    if reason:continue
    seen.add(key)
    accepted.append({'combination_id':f'R{len(accepted)+1:02}','generation_path':'실제 무작위: 유형3개 균등추출→유형별 Axis 균등추출',
                     'axis_ids':list(key),'type_tags':sampled_types,'sampling_attempt':attempt['attempt']})
out=root/'combinations';out.mkdir(exist_ok=True)
record={'seed':20261112,'executed_at':datetime.now(ZoneInfo('Asia/Seoul')).isoformat(),
        'taxonomy_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'algorithm':'Python random.Random; sample(types,3); choice(type_pool)',
        'pools':pools,'redraw_rule':'동일 Axis 중복 또는 동일3축집합만 재추첨. 과학적 부적합·U/W 공백은 재추첨하지 않고 판정으로 보존.',
        'semantically_duplicate_rule':'의미상 중복은 사후 판정하여 RQ 집계에서 병합; 결과를 보고 난수를 다시 뽑지 않음',
        'attempts':attempts,'accepted':accepted}
(out/'random_draws.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'attempts':len(attempts),'accepted':accepted},ensure_ascii=False))
