#!/usr/bin/env python3

# V2_LEGACY_GUARD: preserve historical scripts without overwriting the new agenda.
from pathlib import Path as _VersionPath
if (_VersionPath(__file__).resolve().parents[1] / "revision_v2/version.json").exists():
    raise SystemExit("이 스크립트는 v1 전용입니다. 현재 기획에는 render_neuroscience_v2.py와 validate_neuroscience_v2.py를 사용하세요.")

import json,csv
from pathlib import Path
r=Path(__file__).resolve().parents[1];qs={q['rq_id']:q for q in json.loads((r/'research_questions/landscape.json').read_text())}
def readcsv(p):return list(csv.DictReader((r/p).open()))
def writecsv(p,rows):
 with (r/p).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
rows=readcsv('research_questions/clusters.csv');rows=[x for x in rows if x['rq_id'] in qs]
for x in rows:x['title']=qs[x['rq_id']]['title']
writecsv('research_questions/clusters.csv',rows)
p=r/'synthesis/DIVERSITY_AUDIT.md';s=p.read_text().replace('32개 RQ',f'{len(qs)}개 RQ').replace('32개의 독립적',f'{len(qs)}개의 독립적').replace('| 모델 계산·좌표·학습 제약 | 5 | RQ22, RQ25, RQ30, RQ31, RQ32 |','| 모델 계산·좌표·학습 제약 | 3 | RQ25, RQ31, RQ32 |')
if 'RQ30→RQ25' not in s:s+='\n최종 독립 감사는 RQ30→RQ25 계산좌표 분기 통합과 RQ22 방법후보 전환을 요구했고 Coordinator가 수용했다. 방향40개에는 방법·중복분기10개가 포함되며 이를 독립 과학 질문 수에 더하지 않는다. RQ07은 동일 probe의 이력 효과, RQ29는 현재/최근성 일치 후 순서 효과, RQ20은 미래 예측 학습목표의 대비로 범위를 구별했다.\n'
p.write_text(s)
trace=readcsv('research_questions/candidate_crosswalk.csv');d2q={x['direction_id']:x['rq_id'] for x in trace if x['rq_id']}
rows=readcsv('combinations/random_to_questions.csv')
for x in rows:x['rq_ids']=';'.join(dict.fromkeys(d2q[d] for d in x['direction_ids'].split(';') if d in d2q))
writecsv('combinations/random_to_questions.csv',rows)
rows=readcsv('research_questions/rankings.csv');titles={'scientific_potential':'과학적 잠재력','originality':'독창성','short_term_feasibility':'단기 실현성','overall_priority':'종합 우선순위'}
lines=['# 네 가지 우선순위','',
'점수는 문헌과 조건부 설계에 대한 각 역할의 Round4 1–5점 판단이다. 관측된 실험효과·메타분석 점수·역할 간 교정된 척도가 아니다. 세 기준순위는 명시한 항목을 차례로 비교하는 설명용 사전순 정렬이며, 동점의 RQ 번호 순서에 과학적 차이가 있다는 뜻은 없다. 종합 Top10은 Coordinator가 반증 대비·질문 다양성·자료 조건을 함께 판단했으며 자동 가중합 순위가 아니다. 최종 감사에서 제외·병합한 질문은 별도 순위로 세지 않는다.','']
for kind,title in titles.items():
 sub=[x for x in rows if x['ranking']==kind];lines += [f'## {title}','',f"비교 기준: {sub[0]['criterion_order']}",'','| 순서 | 질문 | 근거/점수 |','|---:|---|---|']
 for x in sub[:10]:lines.append(f"| {x['rank']} | [{x['rq_id']} {x['title']}](LANDSCAPE.md#{x['rq_id'].lower()}) | {x['meaning'] if kind=='overall_priority' else x['scores']} |")
 lines+=['']
lines+=['각 질문의 항목별 이유·근거·불확실성은 LANDSCAPE.md, 전체 순위는 rankings.csv에 있다. 우선5는 종합 검토 순서이며 다섯 개 모두 현재 자료로 즉시 실행할 수 있다는 뜻은 아니다. 최종 조건·실제 착수 판정은 Round5 종합과 상세 카드가 우선한다. 특히 RP05는 반복/전처리 독립성 미확인으로 신경 확증 착수를 보류했다.','']
(r/'research_questions/RANKINGS.md').write_text('\n'.join(lines))
print(json.dumps({'active_questions':len(qs),'cluster_rows':len(readcsv('research_questions/clusters.csv')),'random_mappings':30}))
