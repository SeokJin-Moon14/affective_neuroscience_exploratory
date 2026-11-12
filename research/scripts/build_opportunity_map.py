#!/usr/bin/env python3
import csv,json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
path=root/'discussions/round_04/collected.json'
cs={c['candidate_id']:c for c in json.loads(path.read_text())}
axes={a['axis_id']:a for a in json.loads((root/'axis_map/integrated_subaxes.json').read_text())}
strategies=[
 ('Technology Transfer','C07-04','最適輸送'.replace('最適輸送','최적수송'),'서로 다른 좌표계의 거리관계를 비교하는 계산을 정서 의미 대응의 비유일성 검정으로 전이'),
 ('Methodological Inversion','C09-02','inverse problems','단일 복원 성공을 같은 관측을 만족하는 여러 후보의 식별범위 문제로 뒤집음'),
 ('Representation Competition','C04-02','조건부 예측과 정보원 비교','자극으로 설명되는 변동과 과거 신경으로 설명되는 변동을 같은 test에서 경쟁'),
 ('Scale Bridging','C08-02','계층 시간범위 비교','영상 문맥의 길이를 감각–transmodal 위치별 정서 대비와 연결하되 HRF·공간null을 경쟁'),
 ('Dynamics & Geometry','C07-03','지연공간 위상과 null','정적 점구름 도식에서 시간 지연의 연결구조가 관측과정을 넘는지로 전환'),
 ('Cross-Dataset Discovery','C01-04','관계쌍·측정 불변성','같은 라벨 이름 대신 독립 anchor·관계쌍을 비교 단위로 사용'),
 ('Counterfactual Modeling','C09-03','생성 편집 타당성','모델 latent 편집과 실제 자극의 감각·사건 보존을 나눈 뒤 선택적 신경 대비를 설계'),
 ('Brain-to-AI Reverse Inspiration','C11-05','신경정보 보존 제약','예측기가 신경자료에 맞는지를 넘어 신경 제약이 모델의 맥락 일반화를 바꾸는지 검정'),
 ('Model Disagreement','C12-03','모형 불일치와 능동 설계','기존 관측에서 동등한 모형의 차이가 가장 큰 안전한 자극 대비를 찾음'),
 ('Hidden Structure Discovery','C06-01','예측상태 추상화','정서 라벨을 쓰지 않은 상태를 만든 뒤 독립 정서–신경 대비로 검증'),
 ('Unresolved Discussion Transfer','C11-03','재귀 계산 비교','P008 Discussion의 recurrent feedback 후속 제안을 유효 문맥·계산량이 같은 재귀/비재귀 비교로 연결'),
 ('Assumption Reversal','C05-01','공유/고유 정보 통로','공통 공간이 충분하다는 전제를 고유 경로가 필요한지의 판별로 뒤집음')]
records=[]
for i,(strategy,cid,field,transfer) in enumerate(strategies,1):
    c=cs[cid];parents=sorted({p for sid in c['axis_ids'] for p in axes[sid]['parent_axes']})
    types=sorted({t for sid in c['axis_ids'] for t in axes[sid]['type_tags']})
    records.append({'combination_id':f'L{i:02}','generation_path':'문헌 기반:'+strategy,'axis_ids':parents,'type_tags':types,
                    'scientific_construct':c['research_question'],'external_field_concept':field+'; '+transfer,
                    'ai_model_or_method':c['model_application'],'neural_target':c['neural_target'],'available_dataset':c['dataset_plan'],
                    'measurable_contrast':c['measurable_contrast'],'falsifiable_prediction':c['falsification'],'baseline':c['baseline'],
                    'source_papers':list(dict.fromkeys(c['source_papers']+(['P008'] if i==11 else []))),
                    'missing_assumptions':c['missing_conditions'],'novelty_risk':c['novelty_risk'],
                    'decision':'수정 필요' if c['research_role']!='과학RQ후보' else '발전','rejection_reason':'',
                    'candidate_ids':[cid],'transfer_claim':'E3 전이; 저자 제안 직접 확인은 L11의 P008 지정 절만 해당'})
def write_csv(path,rows):
    fields=list(dict.fromkeys(k for r in rows for k in r))
    with path.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
        for r in rows:w.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(list,dict)) else v for k,v in r.items()})
write_csv(root/'combinations/literature_based.csv',records)
(root/'combinations/literature_based.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
randoms=json.loads((root/'combinations/random_evaluated.json').read_text())
write_csv(root/'combinations/combination_matrix.csv',records+randoms)
lines=['# 분야 간 기회 지도','', '12개 문헌 생성 전략을 모두 검토했다. 각 행의 신경 전이는 E3이며, 인용 문헌이 이 새 신경 질문에 답했다고 주장하지 않는다. 자세한 대비와 반증은 후보 원본 및 최종 질문 지도에 연결된다.','', '| 연결 | 원 분야 | 새 계산 능력·전이 | 연결 후보 |','|---|---|---|---|']
for r in records:lines.append(f"| {r['combination_id']} {r['generation_path'][6:]} | {r['external_field_concept'].split(';')[0]} | {r['external_field_concept'].split(';',1)[1]} | {r['candidate_ids'][0]} |")
lines+=['', '## 저자의 미래 제안과 새로운 연구자 제안의 구분','',
        'L11의 P008은 실제 확인한 Discussion의 recurrent feedback 제안을 출발점으로 삼았다. 공정한 유효문맥·계산량 비교 및 정서 대비 검정은 이번 연구자의 E3 재구성이다. 나머지 연결은 원논문 저자의 직접 후속 제안이라고 표현하지 않는다.','',
        '[전체 조합42개](../combinations/combination_matrix.csv): 문헌 기반12개와 실제 무작위30개를 구별한다. [후보별 신규성 역대조](../literature/novelty/README.md).','']
(root/'synthesis/OPPORTUNITY_MAP.md').write_text('\n'.join(lines))
problems=[]
for c in cs.values():
    problems.append({'problem_id':'UP-'+c['candidate_id'],'candidate_id':c['candidate_id'],'open_problem':c['research_question'],
                     'challenged_assumption':c['assumption_challenge'],'literature_basis':c['source_papers'],
                     'transfer_opportunity':c['external_principle'],'claim_source':'연구자의 E3 문헌 기반 추론; 저자의 직접 제안과 구별',
                     'status':c['research_role'],'source_file':c['source_file']})
write_csv(root/'literature/unresolved_problems.csv',problems)
write_csv(root/'synthesis/assumption_inventory.csv',[{'candidate_id':c['candidate_id'],'role':c['role_folder'],'assumption':c['assumption_challenge'],'source_papers':c['source_papers'],'new_capability':c['external_principle']} for c in cs.values()])
print(json.dumps({'literature_combinations':12,'all_combinations':42,'unresolved_problems':len(problems)},ensure_ascii=False))
