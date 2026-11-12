#!/usr/bin/env python3
"""실제 Round4 수정본을 Coordinator의 내용별 중복·선정 판정과 결합한다."""
import csv,json,re
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
assert len(trace)==60 and len({d['direction_id'] for d in directions})==len(directions)
assert len({t['candidate_id'] for t in trace})==60
amendment_path=out/'round05_amendments.json'
if amendment_path.exists():
    amendments=json.loads(amendment_path.read_text())
    for q in landscape:
        if q['rq_id'] not in amendments:continue
        a=amendments[q['rq_id']]
        q['round05_condition']=a['condition'];q['round05_rejected_claim']=a['rejected_claim']
        q['round4_original_fields']={key:q[key] for key in a['field_overrides']}
        q.update(a['field_overrides'])
curation_path=out/'final_curation.json';retired=[]
if curation_path.exists():
    audit=json.loads(curation_path.read_text());by_rq={q['rq_id']:q for q in landscape}
    for old,new in audit['merge_rqs'].items():
        a,b=by_rq[old],by_rq[new]
        retired.append(dict(a,final_audit_status='동일 과학 대비의 계산좌표 분기로 병합',redirect_rq=new))
        b['merged_candidate_ids']=list(dict.fromkeys(b['merged_candidate_ids']+a['merged_candidate_ids']))
        b['source_papers']=list(dict.fromkeys(b['source_papers']+a['source_papers']))
        b['axis_ids']=list(dict.fromkeys(b['axis_ids']+a['axis_ids']))
        b['parent_axes']=sorted(set(b['parent_axes'])|set(a['parent_axes']))
        b['type_tags']=sorted(set(b['type_tags'])|set(a['type_tags']))
        b['merged_direction_ids']=[b['direction_id'],a['direction_id']]
        b['merged_source_statuses'].update(a['merged_source_statuses'])
        b['merge_rationale']+='; 최종 독립 감사: gate와 error의 결정적 파생좌표는 같은 접근성 질문의 두 분기로 통합'
        b['title']=audit['merged_title'];b['research_question']=audit['merged_question']
        b['main_hypothesis']='동일 완전입력의 gate 또는 오차 계산좌표가 제한된 함수족·학습량 범위에서 정서 대비의 판독 효율을 바꾸며, 그 선택성은 비정서 대비·가역 재표현 대조 후에도 평가할 수 있다. 정보 추가나 신경 구현의 동일성 주장이 아니다.'
        for key in ['measurable_contrast','baseline','falsification']:
            b[key]={'gate_coordinate_branch':b[key],'error_coordinate_branch':a[key]}
        b['score_scope']='병합 전 대표 C11-02의 Round4 평가를 표시; C11-01 원 평가도 원본에 보존하며 평균·별도 RQ 수로 쓰지 않음'
        b['remaining_disagreement']='; '.join(f'{k}: {v}' for k,v in b['merged_source_statuses'].items())
        b['final_audit_condition']='gate·error 분기를 모두 비교하되 동일 입력의 정보량 증가나 인간 신경 기전 증명으로 해석하지 않는다. 각 원안은 원 출처에 보존한다.'
        for t in trace:
            if t['rq_id']==old:t['rq_id']=new;t['decision_reason']='최종 감사에서 같은 입력의 계산좌표 분기로 '+new+'에 통합'
        for d in directions:
            if d['direction_id']==a['direction_id']:d['decision']='다른 RQ의 계산좌표 분기로 통합';d['decision_reason']=new+'와 같은 관측·반증 대비'
    for rid,reason in audit['method_rqs'].items():
        q=by_rq[rid];retired.append(dict(q,final_audit_status='방법후보로 유지',reason=reason))
        for t in trace:
            if t['rq_id']==rid:t['rq_id']='';t['decision_reason']=reason
        for d in directions:
            if d['direction_id']==q['direction_id']:d['decision']='방법·공통검증으로 유지';d['decision_reason']=reason
    landscape=[q for q in landscape if q['rq_id'] not in audit['merge_rqs'] and q['rq_id'] not in audit['method_rqs']]
    for q in landscape:
        if q['rq_id'] in audit['narrowing']:q['final_audit_condition']=audit['narrowing'][q['rq_id']]
        if q['rq_id'] in audit.get('field_overrides',{}):
            overrides=audit['field_overrides'][q['rq_id']]
            q['pre_final_audit_fields']={key:q[key] for key in overrides}
            q.update(overrides)
    (out/'retired_questions.json').write_text(json.dumps(retired,ensure_ascii=False,indent=2)+'\n')
for d in directions:d['status']='Round4·Round5 및 최종 독립 감사 반영'
(out/'landscape.json').write_text(json.dumps(landscape,ensure_ascii=False,indent=2)+'\n')
write_csv(out/'landscape.csv',landscape);write_csv(out/'directions.csv',directions);write_csv(out/'candidate_crosswalk.csv',trace)
(out/'direction_aliases.json').write_text(json.dumps(merges,ensure_ascii=False,indent=2)+'\n')
def cite(pid):
    p=papers.get(pid) or catalog.get(pid)
    assert p is not None,pid
    ident=p.get('doi_or_arxiv','');url=p['official_url']
    doi=re.search(r'10\.\d{4,9}/[^\s;,]+',ident)
    arxiv=re.search(r'(?:arXiv:|arxiv.org/abs/)(\d{4}\.\d{4,5}(?:v\d+)?)',ident,re.I)
    if doi:url='https://doi.org/'+doi.group(0)
    elif arxiv:url='https://arxiv.org/abs/'+arxiv.group(1)
    return f"[{pid} {p['title']}]({url})"
lines=['# Research Question Landscape','',
       f'**60개 원 후보 → {len(directions)}개 중복 통합 연구 방향 → {len(landscape)}개 구별되는 수정 RQ**. 방법·공통 검증·보류·중복 분기{len(directions)-len(landscape)}개는 방향 지도에 보존하고 독립 RQ 수에서 제외했다. 출력 모달리티·적응 단계·생성기 교체만 다른 분기는 기존 질문에 합쳤다. 최종 감사에서 RQ30은 RQ25에 병합하고 RQ22는 방법후보로 옮겼다. 추적을 위해 번호를 재사용하지 않았다. 숫자 자체가 신규성이나 실현성의 검증을 뜻하지 않는다. 모든 질문은 E3이며 실제 신경 분석 결과는 없다.','',
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
    if q.get('round05_condition'):
        lines += ['', '**실제 Round5 반영 조건:** '+q['round05_condition'], '', '**철회한 강한 해석:** '+q['round05_rejected_claim'], '', '평가 점수는 Round4의 역할 판단이다. Round5 조건으로 실제 착수 가능성이 좁아진 경우 현재 점수 자체를 실현성 증명으로 읽지 않는다.']
    if q.get('final_audit_condition'):lines += ['', '**최종 독립 감사의 범위 제한:** '+q['final_audit_condition']]
for q in retired:
    lines += ['',f"<a id=\"{q['rq_id'].lower()}\"></a>",f"## {q['rq_id']} — 독립 RQ 집계에서 제외",'',q['final_audit_status']+'; '+q.get('redirect_rq',q.get('reason','')),'','원안과 추적 정보는 [보존 기록](retired_questions.json)에 있다.']
(out/'LANDSCAPE.md').write_text('\n'.join(lines)+'\n')
short_dirs=['D11','D15','D22','D20','D17','D06','D12','D18','D04','D36']
reasons=[
 'Horikawa 우선으로 같은 입력·시각표적에서 정렬 전후 정서 대비의 판독 접근성을 검정한다. 유한 probe로 비가역 정보 소실을 입증하지 않으며, 작은 학습목표 비교와 cache 기준부터 조건부 착수할 수 있음.',
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
print(json.dumps({'directions':len(directions),'rqs':len(landscape),'shortlist':len(short),'traced_candidates':len(trace),'quantity_targets_met':len(directions)>=40 and len(landscape)>=30},ensure_ascii=False))
