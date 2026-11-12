#!/usr/bin/env python3
"""실제 Round4 수정본을 Coordinator의 내용별 중복·선정 판정과 결합한다."""
import csv,json
from pathlib import Path
root=Path(__file__).resolve().parents[1]; out=root/'research_questions'
cs={c['candidate_id']:c for c in json.loads((root/'discussions/round_04/collected.json').read_text())}
plan=json.loads((out/'curation_plan.json').read_text())
# Round4에서 C12-03이 명시적 이력×probe 신경대비로 바뀌었으므로 D09와 합친다.
next(g for g in plan if g['direction_id']=='D37')['candidate_ids'].remove('C12-03')
next(g for g in plan if g['direction_id']=='D09')['candidate_ids'].append('C12-03')
next(g for g in plan if g['direction_id']=='D09')['merge_reason']+='; C12-03의 명시적 HRF·이력 대조와 새 probe 실험을 같은 과학 질문으로 통합'
axis={a['axis_id']:a for a in json.loads((root/'axis_map/integrated_subaxes.json').read_text())}
papers={p['canonical_id']:p for p in csv.DictReader((root/'literature/papers.csv').open())}
catalog={p['reference_id']:p for p in csv.DictReader((root/'axis_map/reference_catalog.csv').open())}
# Agent12 독립 중복 감사 수용. 기존 ID는 alias 기록에 보존한다.
merges={'D45':'D01','D46':'D25','D01':'D28','D27':'D25','D38':'D36','D35':'D12'}
for old,new in merges.items():
    a=next(g for g in plan if g['direction_id']==old);b=next(g for g in plan if g['direction_id']==new)
    b['candidate_ids']+=a['candidate_ids'];b['merge_reason']+='; 독립 감사와 Coordinator 내용 대조에 따라 '+old+'의 같은 대비/검증 분기를 통합'
plan=[g for g in plan if g['direction_id'] not in merges]
representatives={'D04':'C07-04','D05':'C04-04','D08':'C07-02','D09':'C12-03','D12':'C09-02','D13':'C08-01','D15':'C10-02','D33':'C11-02'}
excluded={
 'D01':'내용·사람 일반화와 좌표/연산 구별은 다른 RQ의 공통 검증 요인으로 통합. 독립적 과학 대비가 더 구체화되기 전 중복 집계하지 않음.',
 'D14':'생성 영상의 시간 해상도 감사는 관측등가·시간 정보 후보의 검증 분기로 통합.',
 'D16':'Round4 제안자의 권고를 반영하여 학습목표별 접근성 비교를 D11의 학습 연산 분기로 통합. 목표/용량/입력 조건만 다른 모델 비교를 별도 RQ로 세지 않음.',
 'D27':'분포 밖 적응의 정보 보존은 D25 선택적 불변성의 학습/적응 단계 대조로 통합.',
 'D29':'측정척도별 기하 순위 변화는 공통 측정 모듈로 유지.',
 'D30':'위상 null 기각만으로 특정 정서 계산 가설을 식별하지 못하므로 방법·탐색 항목으로 유지.',
 'D32':'공간 신뢰도·null 감사를 공통 방법 조건으로 유지.',
 'D35':'출력 모달리티별 prior 기여는 D12 관측 제약과 RP07 평가 분기로 통합.',
 'D38':'생성기 family 전이는 D36 편집 타당성과 D12 관측등가의 일반화 대조로 통합.',
 'D43':'구체 정서 계산의 차이가 없는 생물학적 구현 회복시험은 방법후보로 유지.',
 'D37':'Round4에서 제안자가 유한 pool 실험설계를 방법후보로 분류. C12-03의 실제 이력 신경대비는 D09에 통합.'}
metrics=['novelty','neuro_importance','ai_necessity','data_feasibility','rigor','falsifiability','interpretability','generalization','technical_feasibility','exploration_value']
def txt(x):
    if isinstance(x,str):return x
    if isinstance(x,list):return ' / '.join(txt(v) for v in x)
    if isinstance(x,dict):return '; '.join(f'{k}: {txt(v)}' for k,v in x.items())
    return str(x)
def write_csv(path, rows):
    fields=list(dict.fromkeys(k for r in rows for k in r))
    with path.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
        for r in rows:w.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(list,dict)) else v for k,v in r.items()})
landscape=[];directions=[];trace=[]
for group in plan:
    did=group['direction_id'];cid=representatives.get(did,group['representative_candidate_id']);c=dict(cs[cid])
    if not c['research_role'].startswith('과학RQ후보'):
        excluded.setdefault(did,'실제 Round4 제안자의 판정 '+c['research_role']+'를 존중하여 독립 과학 RQ 수에서 제외')
    refs=list(dict.fromkeys(p for source in group['candidate_ids'] for p in cs[source]['source_papers']))
    subaxes=list(dict.fromkeys(a for source in group['candidate_ids'] for a in cs[source]['axis_ids']))
    source_statuses={source:cs[source]['research_role'] for source in group['candidate_ids']}
    remaining_disagreement='각 원안의 역할 판정은 병합 후에도 보존한다. ' + '; '.join(f'{k}: {v}' for k,v in source_statuses.items())
    directions.append(dict(group,representative_candidate=cid,revised_title=c['title'],source_papers=refs,
                           merged_source_statuses=source_statuses,remaining_disagreement=remaining_disagreement,
                           decision='RQ로 구체화' if did not in excluded else '방법·공통검증·중복분기로 유지',
                           decision_reason=excluded.get(did,'별개의 관측대상·조작·경쟁설명·반증 대비가 남음; 실제 분석 조건부')))
    if did not in excluded:
        assert set(metrics)<=set(c['evaluation']),(cid,list(c['evaluation']))
        for metric in metrics:
            assert 1<=float(c['evaluation'][metric]['score'])<=5,(cid,metric)
        rq=dict(c,rq_id=f'RQ{len(landscape)+1:02}',direction_id=did,merged_candidate_ids=group['candidate_ids'],
                source_papers=refs,axis_ids=subaxes,parent_axes=sorted({x for a in subaxes for x in axis[a]['parent_axes']}),
                type_tags=sorted({x for a in subaxes for x in axis[a]['type_tags']}),
                merge_rationale=group['merge_reason'],merged_source_statuses=source_statuses,
                remaining_disagreement=remaining_disagreement,claim_status='E3 수정된 연구 질문; 신경 결과·세계 최초 미확정')
        landscape.append(rq)
    for source in group['candidate_ids']:
        trace.append({'candidate_id':source,'direction_id':did,'rq_id':landscape[-1]['rq_id'] if did not in excluded else '',
                      'decision_reason':excluded.get(did,group['merge_reason'])})
assert len(directions)==40 and len(landscape)>=30 and len(trace)==60
assert len({t['candidate_id'] for t in trace})==60
(out/'landscape.json').write_text(json.dumps(landscape,ensure_ascii=False,indent=2)+'\n')
write_csv(out/'landscape.csv',landscape);write_csv(out/'directions.csv',directions);write_csv(out/'candidate_crosswalk.csv',trace)
(out/'direction_aliases.json').write_text(json.dumps(merges,ensure_ascii=False,indent=2)+'\n')
def cite(pid):
    p=papers.get(pid) or catalog.get(pid)
    assert p is not None,pid
    return f"[{pid} {p['title']}]({p['official_url']})"
lines=['# Research Question Landscape','',
       f'**60개 원 후보 → 40개 중복 통합 연구 방향 → {len(landscape)}개 구별되는 수정 RQ**. 방법·공통 검증·보류 항목{40-len(landscape)}개는 방향 지도에 보존하고 독립 RQ 수에서 제외했다. 출력 모달리티·적응 단계·생성기 교체만 다른 분기는 기존 질문에 합쳤다. 숫자 자체가 신규성이나 실현성의 검증을 뜻하지 않는다. 모든 질문은 E3이며 실제 신경 분석 결과는 없다.','',
       '각 질문은 Round2 원안, 서로 다른 두 역할의 Round3 비판, Round4 응답을 추적할 수 있다. [원본 대응표](candidate_crosswalk.csv), [방향40개](directions.csv), [신규성 역대조](../literature/novelty/README.md).','',
       '| RQ | 질문 | 원 방향 | 출발 후보 |','|---|---|---|---|']
for q in landscape:lines.append(f"| [{q['rq_id']}](#{q['rq_id'].lower()}) | {q['title']} | {q['direction_id']} | {', '.join(q['merged_candidate_ids'])} |")
for q in landscape:
    lines += ['',f"<a id=\"{q['rq_id'].lower()}\"></a>",f"## {q['rq_id']}. {q['title']}",'',
      q['research_question'],'',f"- **Axis·유형:** {' × '.join(q['parent_axes'])}; {'; '.join(q['type_tags'])}",
      f"- **모델 적용 → 과학 질문 → 가정 도전:** {txt(q['model_application'])} → {txt(q['scientific_question'])} → {txt(q['assumption_challenge'])}",
      f"- **경쟁 설명:** {txt(q['main_hypothesis'])} / {txt(q['alternative'])}",
      f"- **관측 대비:** {txt(q['measurable_contrast'])}",f"- **반증:** {txt(q['falsification'])}",f"- **기준모형:** {txt(q['baseline'])}",
      f"- **자료·착수 조건:** {txt(q['dataset_plan'])}; {txt(q['missing_conditions'])}",
      f"- **근접 연구와 차이:** {txt(q['closest_prior_ids'])}; {txt(q['what_is_new'])}",f"- **중복·신규성 위험:** {txt(q['novelty_risk'])}",
      f"- **병합 시 보존한 판정:** {q['remaining_disagreement']}",
      f"- **원본:** [{q['source_file']}](../{q['source_file']}); 후보 {', '.join(q['merged_candidate_ids'])}",
      '- **근거:** '+'; '.join(cite(x) for x in q['source_papers']),
      '', '| 평가 | 점수 | 이유 | 불확실성 |','|---|---|---|---|']
    for key in metrics:
        e=q['evaluation'][key]
        lines.append(f"| {key} | {e['score']} | {txt(e['reason']).replace('|','/')} | {txt(e['uncertainty']).replace('|','/')} |")
    lines += ['', '여덟 탐색 질문의 개별 답과 비판 수용/미해결 이력은 위 구조화 원본에 보존했다.']
(out/'LANDSCAPE.md').write_text('\n'.join(lines)+'\n')
short_dirs=['D11','D15','D22','D20','D17','D06','D12','D18','D04','D36']
reasons=[
 'Horikawa 우선으로 정렬 후 접근가능성과 비가역 손실을 구별하며 생성기 학습 없이 첫 대비를 구성할 수 있음.',
 '관계 의미 누락과 비가산 신경 예측 이득을 고정 타깃에서 구별하고 Mind Captioning을 조건부로 연결함.',
 '현재 자극·연속 상태·사건경계 reset의 충돌하는 예측을 시간자료에서 검정함.',
 '모달리티 공유 통로의 충분성과 고유 경로 필요성을 강한 가산 기준으로 구별함.',
 '자극조건부와 신경조건부의 불일치를 의미 누락·공통자극과 경쟁시킴.',
 '정서 범주 경계의 신경 구조를 단순 고차원성보다 구체적인 국소 대비로 검정함.',
 '그럴듯한 단일 복원보다 관측이 제한하는 정서 정보의 식별 범위를 질문함.',
 '공간 평균의 null-space에 정서 대비가 남는지 검정하여 뇌 foundation model의 공간 병목을 해부학·신뢰도와 구별함.',
 '서로 다른 자료의 거리구조 일치와 정서 의미 대응을 구별하는 장기 기회를 보존함.',
 '사전 허용집합에서 의미 보존 편집의 실제 신경 대비를 검정하는 장기 경로; 선택한 모집단과 새 측정 조건을 명시함.']
short=[]
for i,(did,reason) in enumerate(zip(short_dirs,reasons),1):
    q=next(q for q in landscape if q['direction_id']==did)
    short.append(dict(q,proposal_id=f'RP{i:02}',coordinator_selection_reason=reason,priority_group='우선5' if i<=5 else '확장5'))
(out/'shortlist.json').write_text(json.dumps(short,ensure_ascii=False,indent=2)+'\n')
write_csv(out/'shortlist.csv',[{'proposal_id':q['proposal_id'],'rq_id':q['rq_id'],'direction_id':q['direction_id'],'title':q['title'],'selection_reason':q['coordinator_selection_reason'],'priority_group':q['priority_group']} for q in short])
# 세 기준순위는 설명용 사전순 비교다. 종합순위 Top10은 위 내용 판단으로 선정한다.
ranking_specs={'scientific_potential':['neuro_importance','exploration_value','falsifiability'],
               'originality':['novelty','ai_necessity','exploration_value'],
               'short_term_feasibility':['data_feasibility','technical_feasibility','rigor']}
rankings=[]
for name,keys in ranking_specs.items():
    ordered=sorted(landscape,key=lambda q:tuple(-float(q['evaluation'][k]['score']) for k in keys)+(q['rq_id'],))
    for rank,q in enumerate(ordered,1):rankings.append({'ranking':name,'rank':rank,'rq_id':q['rq_id'],'title':q['title'],'criterion_order':keys,'scores':[q['evaluation'][k]['score'] for k in keys],'meaning':'설명용 사전순 비교; 자동 종합 선정 아님'})
for rank,q in enumerate(short,1):rankings.append({'ranking':'overall_priority','rank':rank,'rq_id':q['rq_id'],'title':q['title'],'criterion_order':'Coordinator 내용·다양성·반증·착수조건 판단','scores':'가중합 사용 안 함','meaning':q['coordinator_selection_reason']})
write_csv(out/'rankings.csv',rankings)
print(json.dumps({'directions':len(directions),'rqs':len(landscape),'shortlist':len(short),'traced_candidates':len(trace)},ensure_ascii=False))
