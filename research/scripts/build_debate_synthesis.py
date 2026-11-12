#!/usr/bin/env python3
"""실제 세 관점·후속 응답과 Coordinator의 명시적 판정을 합성."""
import json,collections
from pathlib import Path
r=Path(__file__).resolve().parents[1];out=r/'discussions/round_05'
def prose(x):
 if isinstance(x,str):return x
 if isinstance(x,list):return ' / '.join(prose(v) for v in x)
 if isinstance(x,dict):return '; '.join(f'{k}: {prose(v)}' for k,v in x.items())
 return str(x)
positions=json.loads((out/'collected.json').read_text())
qs={q['proposal_id']:q for q in json.loads((r/'research_questions/shortlist.json').read_text())}
responses=[]
for f in sorted((r/'agents').glob('*/round05_rebuttal.json')):
 d=json.loads(f.read_text());responses.extend(dict(x,response_source=f.relative_to(r).as_posix()) for x in d['responses'])
assert len(responses)>=20 and all(sum(x['proposal_id']==pid for x in responses)>=2 for pid in qs)
manual={
'RP01':('수정 후 조건부 파일럿','동일 입력·작은 encoder·시각표적에서 contrastive 대 회귀를 비교한다. cache/ridge는 접근성·검증 기준이며 목표효과와 분리한다.','유한 readout·학습량의 실패로 정보 소실을 증명할 수 없다. 내용 통제도 정서 특수성의 완전 보장은 아니다.'),
'RP02':('수정 후 조건부 제안','고정 A·loss·표본에서 D/N 함수족의 S 접근을 맞추고 δ=g(O+B)-g(O+R)를 검정한다. matching은 개발에서만 한다. 감소 주장에는 g(O) 기준·r_R의 실제 감소·δ 비교우위의 공동 조건을 요구하며 δ만 양수이면 차등 변조다.','관계/비관계의 같은 예측력은 신경과의 오류 중복을 같게 하지 않는다. no-coupling 공통원인 모형이 같은 결과를 낼 수 있고 정확 direct prior도 미확정이다.'),
'RP03':('수정 후 조건부 파일럿','경계를 같은 시점에 받는 연속 상태 대조와 exact functional control, HRF 이후 모형복구를 먼저 둔다.','우세한 forgetting 매개화가 관측상 효율적일 수 있으나 인간 기억 소거나 전체 함수족에서의 필요성은 식별되지 않는다.'),
'RP04':('조건부 제안','고정 shared 용량·readout·학습량에서 operational residual/full입력을 비교하고 실제 오디오 제시를 확인한다.','private의 비유일성과 유한 shared family 밖의 대안이 남는다. 양성도 생물학적 고유 경로 또는 PID 분해의 확증은 아니다.'),
'RP05':('설계 유지·신경 확증 착수 보류','같은 사람/자극의 독립 반복과 target-free 전처리가 확인될 때만 신경 문맥 회수 검정을 시작한다. 동시공간/과거미래 분기를 구별한다.','안정적 미모형화 의미·혈관·해부학·추가 관측량이 신경 문맥 이득을 설명할 수 있다. 보유 사실만으로 반복 조건을 충족하지 않는다.'),
'RP06':('설계·관측 탐색 유지·crossnobis 확증 보류','현 Horikawa는 경계·내용 지지집합과 보류 모형차이 탐색부터 한다. 개별 자극 경계거리 확증에는 실제 독립 추정치를 요구한다.','내용 metric 공통 누락과 주석 불확실성이 남는다. condition 평균·다른 참가자 교차거리는 다른 추정대상이고 개인내 반복 대체가 아니다.'),
'RP07':('Discovery 유지·첫3파일럿 제외','유한 자연 universe의 witness와 참조 유지부터 설계한다. 정서주석+독립반복 경로 또는 명시적인 집단 관측 계약이 확보되어야 한다.','생성 후보의 forward calibration은 자연 관측에서 보장되지 않는다. 단순 SNR 개선·encoder 취약점·선택 후 오배제율이 남으며 미발견은 유일성 증명이 아니다.'),
'RP08':('수정 후 조건부 파일럿','면적가중 평균/영공간 좌표를 분리하고 H1일반상쇄·H2atlas·H3정서선택성을 별도 검정한다. 강한 평균-only 대조와 train-only k곡선을 둔다.','PCA r_k의 실패는 전체 영공간의 실패가 아니다. H1만 양성이면 일반 공간 접근성으로 제한하고 반복 신뢰도·피험자 모집단 결론을 추가하지 않는다.'),
'RP09':('Discovery 유지·자료 내 교정부터','anchor 정의·정보예산·ID 접근·inductive extension을 명세하고 geometry/anchor-only 대조를 둔다. 정서감독 미사용의 단계 범위를 명시한다.','의미 feature 자체의 정서정보는 제거되지 않는다. 유한 다중시작의 범위가 전역 식별집합이나 의미 유일성을 보장하지 않는다.'),
'RP10':('Discovery 유지·새 주석/신경 측정 조건','family 수준 허용집합을 BOLD 이전에 고정하고 독립 realization·모든 실패·새 주석/제시를 포함한다.','양성 효과는 선택된 실제 자극 묶음의 차이다. 미측정 의미·생성 흔적을 배제한 순수 정서 인과량으로 해석할 수 없다.')}
verdicts=[];lines=['# Round5 실제 대립·후속 응답·최종 판정','',
'서로 다른 역할의 제안자·회의적 비판자·데이터통계 검토자가 Top10에 각각 독립 입장을 작성했다. 30개 입장 파일을 수집한 뒤 제안자가 실제 상대 기록을 읽고 후속 응답을 남겼다. 아래 Coordinator 판정은 다수결 합의가 아니며 조건·철회·해결되지 않은 반론을 보존한다.','',
'최종 감사 후 RP02 등의 응답 문서에는 판정식 정정이 반영됐다. 아래는 현재 수정본이며 초기 세 입장과 별도 감사·수정 로그를 함께 보존한다. 과거에 검토자 모두가 최종 재합의했다고 뜻하지 않는다. [감사와 수정 이력](../../synthesis/FINAL_AUDIT.md).','',
'최초 30개 판단: '+str(dict(collections.Counter(x['judgment'] for x in positions)))+f'. 실제 후속 응답 항목: {len(responses)}개. 동일 역할 응답에 여러 비판이 함께 기록될 수 있으므로 응답 항목 수를 독립 과학 주장 수로 해석하지 않는다.','',
'| 제안 | 제안자 / 비판자 / 통계 | Coordinator 판정 |','|---|---|---|']
for pid,q in sorted(qs.items()):
 ps=[x for x in positions if x['proposal_id']==pid];ordered=[next(x for x in ps if x['debate_role']==label) for label in ['제안자','회의적비판자','데이터통계검토자']]
 dec,change,unresolved=manual[pid];rs=[x for x in responses if x['proposal_id']==pid]
 verdicts.append({'proposal_id':pid,'rq_id':q['rq_id'],'coordinator_decision':dec,'accepted_scope':change,'remaining_disagreement':unresolved,'positions':ps,'responses':rs})
 lines.append(f"| [{pid}](../../proposals/{pid}.md) | "+' / '.join(x['reviewer_folder'][:2]+': '+x['judgment'] for x in ordered)+f' | {dec} |')
for v in verdicts:
 lines += ['',f"## {v['proposal_id']}. {qs[v['proposal_id']]['title']}",'',f"**최종 판정:** {v['coordinator_decision']}",'',v['accepted_scope'],'','**남은 대립:** '+v['remaining_disagreement'],'','**실제 제안자의 응답:**','']
 for x in v['responses']:
  lines += [f"- **검토자 {prose(x['critic_role'])} / {prose(x['decision'])}:** {prose(x['critique_summary'])}",'',
            '  **응답:** '+prose(x['response']),'','  **남은 쟁점:** '+prose(x['remaining_disagreement']),'',f"  [작성 원본](../../{x['response_source']})",'']
 lines += ['**최초 입장 원본:**','']
 for x in v['positions']:lines+=['- '+f"[{x['debate_role']} {x['reviewer_folder']}](../../{x['review_source']})",'']
lines+=['## 토론으로 실제 바뀐 결정','',
'RP01의 비가역 손실 표현을 철회했다. RP02의 주추정량을 고정 정서 타깃의 조건부 판독 대비로 명확히 했다. RP03의 reset을 실제 인간 소거 기전으로 해석하지 않기로 했다. RP05/06의 확인되지 않은 Horikawa 독립 반복을 착수조건으로 올렸다. RP07은 제안자도 독립 관측/주석 조건을 인정하여 첫3파일럿에서 제외하고 RP08 공간 대비로 교체했다. RP08은 H1/H2/H3를 분리했다. RP09의 비정서를 감독 미사용의 단계적 정의로 좁혔고 RP10은 새 주석/새 BOLD를 필수로 유지했다.','',
'[Round3 실제120개 비판](../round_03/SYNTHESIS.md) → [Round4 실제60개 수정](../round_04/SYNTHESIS.md) → [최종 RQ 반영조건](../../research_questions/round05_amendments.json).']
(out/'rebuttals_collected.json').write_text(json.dumps(responses,ensure_ascii=False,indent=2)+'\n')
(out/'coordinator_verdicts.json').write_text(json.dumps(verdicts,ensure_ascii=False,indent=2)+'\n')
(out/'SYNTHESIS.md').write_text('\n'.join(lines)+'\n')
print(json.dumps({'positions':len(positions),'rebuttal_responses':len(responses),'coordinator_verdicts':len(verdicts)},ensure_ascii=False))
