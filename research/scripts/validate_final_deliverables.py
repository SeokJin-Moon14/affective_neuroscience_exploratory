#!/usr/bin/env python3
"""실제 산출물의 개수·추적·필수계약을 검사한다. 신경 실험 검증이 아니다."""
import csv,json,collections,hashlib,random,re
from pathlib import Path
from datetime import datetime,timezone
r=Path(__file__).resolve().parents[1]
def read(p):return json.loads((r/p).read_text())
def rows(p):return list(csv.DictReader((r/p).open()))
roles=sorted(p for p in (r/'agents').iterdir() if p.is_dir() and p.name[:2].isdigit())
assert len(roles)==12
r2=read('discussions/round_02/collected.json');r3=read('discussions/round_03/collected.json');r4=read('discussions/round_04/collected.json');r5=read('discussions/round_05/collected.json')
assert len(r2)==len(r4)==60 and len(r3)==120 and len(r5)==30
ids={x['candidate_id'] for x in r2};assert len(ids)==60 and ids=={x['candidate_id'] for x in r4}
assert set(collections.Counter(x['target_candidate_id'] for x in r3).values())=={2}
assert all(len({x['reviewer_folder'] for x in r3 if x['target_candidate_id']==cid})==2 for cid in ids)
assert all(len(x['checks'])==8 for x in r3)
assert all(len(json.loads((p/'round02_exchange.json').read_text())['imports'])>=2 for p in roles)
refids={p['canonical_id'] for p in rows('literature/papers.csv')}|{p['reference_id'] for p in rows('axis_map/reference_catalog.csv')}
axes={x['axis_id'] for x in read('axis_map/integrated_subaxes.json')}
responses=[];connections=[]
for p in roles:
 d=json.loads((p/'round04_revision.json').read_text());assert len(d['responses'])==5 and len(d['new_connections'])>=2
 responses+=d['responses'];connections+=d['new_connections']
assert len(responses)==60 and len(connections)>=24
reviews_by_id={x['review_id']:x for x in r3}
for response in responses:
 assert len(response['critique_ids'])==2
 assert all(reviews_by_id[x]['target_candidate_id']==response['candidate_id'] for x in response['critique_ids'])
for c in r4:
 assert set(c['source_papers'])<=refids and set(c['axis_ids'])<=axes
 assert len(c['eight_questions'])==8 and len(c['evaluation'])==10
 for e in c['evaluation'].values():
  assert 1<=float(e['score'])<=5 and e['reason'] and e['uncertainty'] and e['source_papers']
  assert set(e['source_papers'])<=refids
qs=read('research_questions/landscape.json');dirs=rows('research_questions/directions.csv');trace=rows('research_questions/candidate_crosswalk.csv')
assert len(trace)==60 and {x['candidate_id'] for x in trace}==ids
assert len({d['direction_id'] for d in dirs})==len(dirs)
assert len({q['rq_id'] for q in qs})==len(qs) and all(len(q['type_tags'])>=3 for q in qs)
short=read('research_questions/shortlist.json');assert len(short)==10
assign=read('discussions/round05_assignments.json')
for q in short:
 pid=q['proposal_id'];poss=[x for x in r5 if x['proposal_id']==pid]
 assert len(poss)==3 and {x['debate_role'] for x in poss}=={'제안자','회의적비판자','데이터통계검토자'}
 assert len({x['reviewer_folder'] for x in poss})==3
 for x in poss:
  assert x['rq_id']==q['rq_id'] and x['unresolved_disagreement'] and x['best_evidence']
  expected=next(a for a in assign if a['proposal_id']==pid and a['debate_role']==x['debate_role'])
  assert x['reviewer_folder'].startswith(expected['role'])
rebuttals=[]
for p in (r/'agents').glob('*/round05_rebuttal.json'):rebuttals+=json.loads(p.read_text())['responses']
assert len(rebuttals)>=20 and all(sum(x['proposal_id']==q['proposal_id'] for x in rebuttals)>=2 for q in short)
for q in short:
 expected={x['role'] for x in assign if x['proposal_id']==q['proposal_id'] and x['debate_role']!='제안자'}
 actual={re.match(r'(\d{2})',x['critic_role']).group(1) for x in rebuttals if x['proposal_id']==q['proposal_id']}
 assert expected<=actual,(q['proposal_id'],expected,actual)
draw=read('combinations/random_draws.json');assert draw['seed']==20261112 and len(draw['accepted'])==30
assert hashlib.sha256((r/'axis_map/taxonomy.csv').read_bytes()).hexdigest()==draw['taxonomy_sha256']
rng=random.Random(draw['seed']);types=list(draw['pools']);seen=set();attempts=[];accepted=[]
while len(accepted)<30:
 ts=rng.sample(types,3);as_=[rng.choice(draw['pools'][t]) for t in ts];key=tuple(sorted(set(as_)))
 reason='동일 Axis 중복' if len(key)<3 else '이미 추출한 조합' if key in seen else None
 attempt={'attempt':len(attempts)+1,'sampled_types':ts,'sampled_axes':as_,'redraw_reason':reason};attempts.append(attempt)
 if reason:continue
 seen.add(key);accepted.append({'combination_id':f'R{len(accepted)+1:02}','generation_path':'실제 무작위: 유형3개 균등추출→유형별 Axis 균등추출','axis_ids':list(key),'type_tags':ts,'sampling_attempt':attempt['attempt']})
assert attempts==draw['attempts'] and accepted==draw['accepted']
assert len(rows('combinations/combination_matrix.csv'))==42 and len(read('combinations/random_evaluated.json'))==30
assert {q['rq_id'] for q in qs}<={x['rq_id'] for x in read('literature/novelty/reverse_search_records.json')}
cards=read('proposals/cards.json');pilots=read('pilots/plans.json');assert len(cards)==10 and len(pilots)==3
assert {c['proposal_id'] for c in cards}=={q['proposal_id'] for q in short}
for c in cards:
 assert len({p['paper_id'] for p in c['prior_literature']})>=5
 assert all(p['paper_id'] in refids and p['contribution'] and p['limitation'] and p['access_scope'] for p in c['prior_literature'])
 assert c['debate_response'] and c['falsifiable_outcomes'] and c['limitations_and_risks']
for p in pilots:assert p['readiness'] and p['failure_modes_and_claim_limits'] and p['decision_points']
verified=rows('literature/verified_papers.csv');assert len(verified)>=100
report={'checked_at':datetime.now(timezone.utc).isoformat(),'result':'PASS', 'scope':'산출물 구조·실제 역할 추적·참조ID·수량 검사; 뇌 분석/모델 성능/전역 신규성 검증 아님',
'mission_quantity_targets_met':len(qs)>=30 and len(dirs)>=40,
'counts':{'roles':12,'verified_bibliographies':len(verified),'unique_inventory':len(rows('literature/papers.csv')),'round2_candidates':len(r2),'round3_reviews':len(r3),'round3_checks':sum(len(x['checks']) for x in r3),'round4_responses':len(responses),'round4_connections':len(connections),'round4_evaluations':600,'round5_positions':len(r5),'round5_rebuttal_responses':len(rebuttals),'random_combinations':30,'literature_combinations':12,'directions':len(dirs),'research_questions':len(qs),'proposals':len(cards),'pilots':len(pilots)},
'limits':['검증 보류 서지3편과 별도 보조 출처를 확정100편에 추가 집계하지 않음','원문 Discussion/한계 직접 확인은27편 범위','원 사용자 데이터의 현재 경로/스키마 및 모델 load는 미확인','전역 신규성 검색에는 네트워크 제약이 남음']}
(r/'synthesis/validation_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False))
