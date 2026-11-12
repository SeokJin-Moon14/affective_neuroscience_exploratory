#!/usr/bin/env python3
"""전문 역할이 쓴 카드·계획의 필수항목/근거를 검사하고 공유 문서로 렌더링."""
import csv,json,re
from pathlib import Path
root=Path(__file__).resolve().parents[1]
papers={r['canonical_id']:r for r in csv.DictReader((root/'literature/papers.csv').open())}
for entry in csv.DictReader((root/'axis_map/reference_catalog.csv').open()):
    papers.setdefault(entry['reference_id'],entry)
short={r['proposal_id']:r for r in json.loads((root/'research_questions/shortlist.json').read_text())}
def render(value,level=0):
    if isinstance(value,str):return value+'\n'
    if isinstance(value,list):
        return '\n'.join('- '+(render(v,level+1).strip().replace('\n','\n  ')) for v in value)+'\n'
    if isinstance(value,dict):
        return '\n'.join(f'**{key.replace("_"," ")}:** '+render(val,level+1).strip()+'\n' for key,val in value.items())+'\n'
    return str(value)+'\n'
def link(pid):
    p=papers[pid];ident=p.get('doi_or_arxiv','');url=p['official_url']
    doi=re.search(r'10\.\d{4,9}/[^\s;,]+',ident)
    arxiv=re.search(r'(?:arXiv:|arxiv.org/abs/)(\d{4}\.\d{4,5}(?:v\d+)?)',ident,re.I)
    if doi:url='https://doi.org/'+doi.group(0)
    elif arxiv:url='https://arxiv.org/abs/'+arxiv.group(1)
    return f"[{pid} {p['title']}]({url})"+(f" · [실제 확인 출처]({p['official_url']})" if url!=p['official_url'] else '')
fields=[('core_question','핵심 질문'),('scientific_motivation','과학적 동기'),('idea_provenance','아이디어 출처'),
        ('prior_literature','관련 문헌과 실제 확인 범위'),('closest_prior_and_novelty','가장 가까운 선행연구와 신규성'),
        ('dataset_and_metadata','데이터와 메타데이터'),('computational_framework','계산 모형'),('neural_target','신경 표적'),
        ('proposed_analyses','분석·검증 계획'),('competing_explanations','경쟁 설명'),('falsifiable_outcomes','긍정·부정·혼합 결과'),
        ('scientific_and_modeling_contribution','신경과학과 모델링 기여'),('limitations_and_risks','한계와 위험'),
        ('smallest_informative_pilot','최소 정보 파일럿'),('priority','우선순위')]
proposal_files=sorted((root/'agents').glob('*/proposal_RP*.json'))
assert len(proposal_files)==10,len(proposal_files)
cards=[]
for file in proposal_files:
    c=json.loads(file.read_text());pid=c['proposal_id'];assert pid in short and c['rq_id']==short[pid]['rq_id']
    assert all(c.get(k) for k,_ in fields)
    assert c.get('debate_response')
    assert len(c['prior_literature'])>=5
    assert len({p['paper_id'] for p in c['prior_literature']})>=5
    lines=[f"# {pid}. {c['title']}",'',f"연결: {c['rq_id']}. 문헌 기반 제안이며 실제 신경 결과가 아니다. 실현성은 명시한 데이터·모델 조건에 따른다.",'',
           '## 1. RQ ID / Working Title','',f"{c['rq_id']} — {c['title']}",'']
    for i,(key,label) in enumerate(fields,2):
        lines += [f'## {i}. {label}','']
        if key=='prior_literature':
            for entry in c[key]:
                assert entry['paper_id'] in papers
                lines += [f"- {link(entry['paper_id'])}: {entry['contribution']} 한계: {entry['limitation']} 확인 범위: {entry['access_scope']}",'']
        else:lines += [render(c[key]),'']
    if c.get('execution_contract'):
        lines += ['## 최종 감사로 확정한 실행 계약','',render(c['execution_contract']),'']
    lines += ['## 실제 토론에 대한 응답','',render(c['debate_response']),'',
              f"작성 원본: [{file.parent.name}](../{file.relative_to(root).as_posix()}). [Round5 기록](../discussions/round_05/SYNTHESIS.md).",'']
    dest=root/'proposals'/f'{pid}.md';dest.write_text('\n'.join(lines))
    c['author_source']=file.relative_to(root).as_posix();cards.append(c)
cards.sort(key=lambda c:c['proposal_id'])
(root/'proposals/cards.json').write_text(json.dumps(cards,ensure_ascii=False,indent=2)+'\n')
lines=['# 상세 연구 제안 10개','', '각 제안은 미션의16개 본문 항목과 실제 Round5 비판 응답을 포함한다. 우선5와 확장5를 구별하며, 순위는 가중합 자동선정이 아니라 경쟁 설명·다양성·착수 조건에 대한 Coordinator 판단이다.','',
       '우선5는 종합 검토 순서이며 즉시 실행 순서가 아니다. 실제 첫 파일럿은 RP01·RP03·RP08이다.','',
       '| 우선 | 제안 | RQ | 최종 추진 범위 | 선정 이유 |','|---|---|---|---|---|']
vp=root/'discussions/round_05/coordinator_verdicts.json'
verdicts={v['proposal_id']:v['coordinator_decision'] for v in json.loads(vp.read_text())} if vp.exists() else {}
for pid,s in sorted(short.items()):lines.append(f"| {s['priority_group']} | [{pid} {s['title']}]({pid}.md) | {s['rq_id']} | {verdicts.get(pid,'명시한 자료 조건부')} | {s['coordinator_selection_reason']} |")
lines+=['','[세 파일럿](../pilots/README.md) / [질문 전체 지도](../research_questions/LANDSCAPE.md) / [네 가지 순위](../research_questions/rankings.csv).','']
(root/'proposals/README.md').write_text('\n'.join(lines))

pilot_files=sorted((root/'agents').glob('*/pilot_PILOT*.json'))
if pilot_files:
    assert len(pilot_files)==3,len(pilot_files)
    pilot_fields=[('hypotheses','핵심·경쟁 가설'),('data_and_access','자료·접근·하위집합'),('model_and_environment','모델·체크포인트·자원'),
                  ('inputs_outputs','입력·출력과 정렬'),('experiment_sequence','실험 순서'),('evaluation','평가·통계'),
                  ('ablations_controls','Ablation·대조'),('decision_points','확대·수정·중단 기준'),('failure_modes_and_claim_limits','실패 가능성과 주장 한계')]
    plans=[]
    for file in pilot_files:
        p=json.loads(file.read_text());assert all(p.get(k) for k,_ in pilot_fields)
        assert p['proposal_id'] in short and p['rq_id']==short[p['proposal_id']]['rq_id']
        lines=[f"# {p['pilot_id']}. {p['title']}",'',f"연결: [{p['proposal_id']}](../proposals/{p['proposal_id']}.md), {p['rq_id']}.",'',
               '**준비 상태:** '+render(p['readiness']),'','이 문서는 파일럿 실행 계획이다. 실험·모델 추론·뇌 분석 결과를 보고하는 문서가 아니다.','']
        for i,(key,label) in enumerate(pilot_fields,1):lines += [f'## {i}. {label}','',render(p[key]),'']
        if p.get('execution_contract'):
            lines += ['## 최종 감사로 확정한 실행 계약','',render(p['execution_contract']),'']
        lines+=['## 근거','']
        for ref in p['references']:
            if ref in papers:lines += ['- '+link(ref)]
            else:lines += ['- '+str(ref)]
        lines+=['',f"작성 원본: [{file.parent.name}](../{file.relative_to(root).as_posix()}). [공통 자원·모델 근거](RESOURCE_AND_MODEL_PLAN.md).",'']
        (root/'pilots'/f"{p['pilot_id']}.md").write_text('\n'.join(lines));p['author_source']=file.relative_to(root).as_posix();plans.append(p)
    plans.sort(key=lambda p:p['pilot_id'])
    (root/'pilots/plans.json').write_text(json.dumps(plans,ensure_ascii=False,indent=2)+'\n')
    lines=['# 세 가지 파일럿 구현 계획','', '서로 다른 과학 대비를 대표하는 계획3개다. 현재 확보한 공식 경로·체크포인트 식별과 실행 성공을 구별한다. 사용자의 데이터 보유를 전제하되 보유본의 실제 필드·정렬·신뢰도 확인은 착수 조건으로 남긴다.','']
    for p in plans:lines+=['- '+f"[{p['pilot_id']} — {p['title']}]({p['pilot_id']}.md): {p['proposal_id']} / {p['rq_id']}"]
    lines+=['','[현재 환경 관측과 자원 산술](RESOURCE_AND_MODEL_PLAN.md). 모든 작업·백업은 클라우드 기준이며 사용자 컴퓨터에 데이터 다운로드를 요구하지 않는다.','']
    (root/'pilots/README.md').write_text('\n'.join(lines))
print(json.dumps({'proposal_cards':len(cards),'pilot_plans':len(pilot_files)},ensure_ascii=False))
