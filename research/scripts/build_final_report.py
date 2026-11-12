#!/usr/bin/env python3
"""검증된 산출물을 최종 보고·재개 안내로 연결한다."""
from pathlib import Path
import csv,json,re
r=Path(__file__).resolve().parents[1]
validation=json.loads((r/'synthesis/validation_report.json').read_text());assert validation['result']=='PASS'
qs=json.loads((r/'research_questions/landscape.json').read_text());cards=json.loads((r/'proposals/cards.json').read_text());pilots=json.loads((r/'pilots/plans.json').read_text())
verdicts=json.loads((r/'discussions/round_05/coordinator_verdicts.json').read_text());counts=validation['counts']
assert len(qs)==counts['research_questions'] and len(cards)==10 and len(pilots)==3
s=(r/'scripts/report_templates/final_synthesis.md').read_text()
s=s.replace('{{RQ_COUNT}}',str(len(qs))).replace('{{DIRECTION_COUNT}}',str(counts['directions'])).replace('{{OTHER_DIRECTION_COUNT}}',str(counts['directions']-len(qs)))
debate=['| 제안 | 최종 범위 | 남은 쟁점 |','|---|---|---|']
for v in verdicts:debate.append(f"| [{v['proposal_id']}](../proposals/{v['proposal_id']}.md) | {v['coordinator_decision']} | {v['remaining_disagreement']} |")
debate += ['',f"실제 후속 응답은 {counts['round5_rebuttal_responses']}항목이다. 제안자가 수용했다고 해서 원 비판자가 최종 재합의했다고 기록하지 않았다. 각 역할의 최초 입장·응답·Coordinator 판정은 원본 링크로 확인할 수 있다."]
reasons={'PILOT01':'정렬 목표의 차이와 좌표/판독 제약을 구별한다. 같은 작은 encoder·시각표적에서 contrastive 대 회귀를 비교하며, frozen cache·ridge는 사전 접근성 기준이다. 실제 주석척도에 맞춘 같은 loss와 정서/비정서 대비를 고정한다.',
'PILOT02':'경계 단서와 상태 갱신의 예측 차이가 HRF 이후에도 구별되는지 먼저 확인한다. 같은 경계 접근의 연속 대조·정확한 함수 동등 대조를 통과하지 못하면 미시적 기전 주장을 중단한다.',
'PILOT03':'checkpoint 없이 선형 공간 집계와 내부 대비의 첫 관측을 구성할 수 있다. 공간 평균의 일반적 손실, atlas 경계 효과, 정서 선택성을 별도 가설로 나누므로 첫 결과가 어디까지 의미 있는지 판정하기 쉽다.'}
pilot_section=[]
for p in sorted(pilots,key=lambda p:p['pilot_id']):pilot_section += [f"**[{p['pilot_id']} — {p['title']}](../pilots/{p['pilot_id']}.md)**",'',reasons[p['pilot_id']],'']
pilot_section += ['세 계획의 순서는 실제 자료 연결·작은 기준모형·식별가능성/회복 점검 → 대조를 포함한 주분석 → 불확실성·확대/수정/중단 판단이다. 현재 데이터 마운트·실제 배열·가중치 load를 검증하지 않았으므로 실행 준비는 조건부다. 계획 수립을 위해 새 주석 수집이나 사람 대상 실험을 실행하지 않았다. [선정 이유와 RP07 제외 결정](../pilots/SELECTION.md).']
s=s.replace('{{DEBATE_SECTION}}','\n'.join(debate)).replace('{{PILOT_SECTION}}','\n'.join(pilot_section))
# 본문에 실제 근거 식별자를 유지하되 확인한 서지의 논문 URL로 연결한다.
papers={p['canonical_id']:p for p in csv.DictReader((r/'literature/papers.csv').open())}
def cite(m):
 pid=m.group(0);p=papers[pid];ident=p['doi_or_arxiv'];doi=re.search(r'10\.\d{4,9}/[^\s;,]+',ident);a=re.search(r'arXiv:(\d{4}\.\d{4,5})',ident,re.I)
 url='https://doi.org/'+doi.group(0) if doi else 'https://arxiv.org/abs/'+a.group(1) if a else p['official_url']
 return f'[{pid}]({url})'
s=re.sub(r'\bP\d{3}\b',cite,s)
(r/'synthesis/FINAL_REPORT.md').write_text(s)
entries=[
('A','Dataset Intelligence Report','datasets/DATASET_INTELLIGENCE_REPORT.md','공식4종 감사와 사용자 보유5종의 실제 확인/미확인 구분'),
('B','Research Axis Encyclopedia','axis_map/AXIS_ENCYCLOPEDIA.md','24축·36원제안·8묶음'),
('C','Verified Literature Database','literature/verified_papers.csv','고유 서지확인100편; 전체103편과보류별도'),
('D','Discussion Mining','literature/discussion_mining.csv','직접지정본문27편·저자후속25편; E3와구별'),
('E','Cross-Disciplinary Opportunity Map','synthesis/OPPORTUNITY_MAP.md','문헌생성12전략·실제Round4새연결27개'),
('F','Actual Agent Discussion Records','discussions/round_05/SYNTHESIS.md','12역할·실제Round1–5·제안자후속응답·소수의견'),
('G','Research Combination Matrix','combinations/combination_matrix.csv','문헌12+실제랜덤30=42'),
('H','Research Question Landscape','research_questions/LANDSCAPE.md',f"방향{counts['directions']}·독립RQ{len(qs)}·방법보류중복{counts['directions']-len(qs)}"),
('I','Top 10 Proposals','proposals/README.md','각16본문항목·관련문헌≥5·실제반론응답'),
('J','Top 3 Pilot Plans','pilots/README.md','각9실행항목·자료/모델조건·실험미실행'),
('K','Coordinator Final Synthesis','synthesis/FINAL_REPORT.md','최종10질문·8탐색질문·우선순위·미해결조건')]
manifest=[]
for code,name,path,scope in entries:
 assert (r/path).is_file(),path
 manifest.append({'deliverable':code,'name':name,'path':path,'status':'문헌·토론·설계 산출물 완료','verified_scope':scope})
(r/'synthesis/deliverables_manifest.json').write_text(json.dumps({'date':'2026-11-12','counts':counts,'deliverables':manifest,'execution_status':'실제 사용자 뇌 분석·모델 실험 미실행; 착수 조건은 개별 계획'},ensure_ascii=False,indent=2)+'\n')
(r/'START_HERE.md').write_text(f'''# 연구 결과 시작점

2026-11-12 기준 요청한 **연구 기획 산출물**을 마무리했다. 문헌100편의 서지·출처, 실제12역할·5라운드 토론, 방향{counts["directions"]}개·RQ{len(qs)}개·상세 제안10개·파일럿 계획3개를 정리했다. 실제 뇌 분석·모델 실험은 실행하지 않았다.

1. [최종 종합 보고서](synthesis/FINAL_REPORT.md)
2. [상세 연구 제안10개](proposals/README.md)
3. [파일럿 실행 계획3개](pilots/README.md)
4. [전체 RQ{len(qs)}개](research_questions/LANDSCAPE.md)와 [네 가지 우선순위](research_questions/RANKINGS.md)
5. [실제 토론·수정·미해결 의견](discussions/round_05/SYNTHESIS.md)
6. [Axis Encyclopedia](axis_map/AXIS_ENCYCLOPEDIA.md)와 [연구 기회 지도](synthesis/OPPORTUNITY_MAP.md)
7. [자료 확인 범위](datasets/DATASET_INTELLIGENCE_REPORT.md)와 [문헌 접근 범위](literature/COVERAGE_AND_GAPS.md)
8. [현재 상태](RESEARCH_STATUS.md), [최종 감사](synthesis/FINAL_AUDIT.md), [ChatGPT 프로젝트 안내](CHATGPT_PROJECT_BRIEF.md)

첨부는 사용자가 지정한 연구 사양으로 적용했고 상위 권한 지침을 대체하지 않았다. 기존 EmoBrain 내용은 접근하지 않았다. 사용자 보유5종의 실제 마운트·스키마는 분석 착수 조건으로 남겼다.100편은 원문 완독 수가 아니며 직접 지정본문/한계 확인은27편이다. 외부 검색 제약으로 전역 신규성은 미확정이다.

단계별 공개 원격 백업의 성공 정본은 저장소 backup/LAST_SUCCESS.json이다. 초기 보고·Round1/Axis v1은 당시 기록이며 현재 결론은 최종 보고서를 따른다.
''')
print(json.dumps({'final_report':True,'manifest_entries':len(manifest),'counts':counts},ensure_ascii=False))
