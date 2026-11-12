import csv,pathlib,json
p=pathlib.Path(__file__).parent
future=[
('BF04-F1','다른 신경학적 조건으로 평가를 확장','Appendix E, p249, 항목1','ADHD·seizure·task·시각해독 외 임상조건을 추가하겠다는 저자 제안','연구 중심에서는 임상조건 자체를 새 Axis로 확장하지 않음','자료 분포가 달라져도 신호 선택이 유지되는지 방법론적 일반화만 전이'),
('BF04-F2','Pearson 고정 연결망을 학습형 연결망으로 대체','Appendix E, pp249–250, 항목2','연결망을 data-driven/end-to-end 방식으로 학습하겠다는 저자 제안','학습된 연결이 인과적 연결이라는 증거는 아님','E3: 정적 graph와 학습 graph의 차이가 정서 관련 신호 보존을 바꾸는지 동일 시계열로 검증'),
('BF04-F3','피험자별 신호품질을 고려한 강건 학습','Appendix E, p250, 항목3','모든 피험자를 동일하게 취급하는 현재 학습의 제약; attention으로 강건 학습을 검토','향후 방향이며 실제 구현·효과가 검증되지 않음','E3: 신호품질을 nuisance로 측정하고 subject holdout에서 효과를 분리'),
('BF04-F4','다중모달 입력 확장','Appendix E, p250, 항목4','기록 텍스트나 fMRI+sMRI, fMRI+EEG 등의 sequence 기반 통합 제안','각 modality에서 별도 실험한 것과 joint multimodal 모델을 구분','E3: 구조·기능 token 통합(BF06)과 비교하되 측정 단위·정렬이 확인된 자료에서만 검증'),
('BF04-F5','분포이동 강건성 평가','Appendix E, p250, 항목5','OOD에서 기존 모델과 Brain-Mamba가 모두 어려울 수 있고 선택 기제가 도움될 것이라는 저자 가설; 평가를 미래로 남김','합성 corruption 결과를 이 미수행 OOD 실험으로 대체하지 않음','E3: 피험자·자극·site holdout을 각각 분리해 input-dependent selection 가설을 반증'),
]
cols=['direction_id','paper_id','author_direction','source_location','author_claim_scope','limitation','agent_transfer','evidence_level','source','verified_on','confidence','needs_followup','origin_agent']
with (p/'discussion_mining.csv').open('w',newline='',encoding='utf-8-sig') as f:
 w=csv.DictWriter(f,fieldnames=cols);w.writeheader()
 for a,b,c,d,e,g in future:w.writerow(dict(direction_id=a,paper_id='BF04',author_direction=b,source_location=c,author_claim_scope=d,limitation=e,agent_transfer=g,evidence_level='E1(저자 원문); 전이 E3',source='https://raw.githubusercontent.com/mlresearch/v248/main/assets/behrouz24a/behrouz24a.pdf',verified_on='2026-11-12',confidence='높음: Appendix E 직접 열람; 전이는 미검증',needs_followup='독립 자료에서 반증 가능한 실험 필요',origin_agent='04_brain_foundation'))
cols=['axis_id','name','definition','type_tags','representative_papers','models','open_questions','transfer_opportunities','dataset_feasibility','confidence','origin_agent','last_verified']
sub=[['J-X-Q.BF1','사전학습 목표별 정보 보존과 소실','재구성·잠재예측·변환불변 목표에서 신뢰 가능한 신경정보가 보존 또는 제거되는 양상을 비교','Neural; Model/Method; Structure/Dynamics; Inference/Measurement','BF01;BF02;BF05;BF08;BF09','SwiFT; CortexMAE; Brain-JEPA','작은 정서 관련 transient는 어떤 목표에서 소실되는가?','같은 ROI·학습자료·probe 조건에서 목적함수만 비교','네 데이터셋 모두 조건부; 실제 시계열·반복신뢰도·주석 감사 필요','E3; 도구 근거 E1','04_brain_foundation','2026-11-12'],['H-F-X.BF2','자극조건부와 신경조건부 표현의 불일치','자극에서 예측 가능한 신경변동과 다른 신경구간에서 예측 가능한 신경변동의 차이를 검사','Construct/Stimulus; Neural; Model/Method; Inference/Measurement','BF02;BF03;BF05','TRIBE v2; CortexMAE; Brain-JEPA','두 모형이 놓치는 신뢰 가능한 정서 관련 정보는 겹치는가?','cross-fitting 잔차·조건부 추가설명력; 잔차를 정서와 동일시하지 않음','정렬된 자극·연속 신경시계열·독립 평가단위가 필요; 실제 가능성 미확인','E3; 잔차 식별성 낮음, 추가 통제 필요','04_brain_foundation','2026-11-12'],['D-N-Q.BF3','관측시간격자와 잠재상태 선택의 분리','TR·HRF·재표본화가 만드는 시간구조와 입력의존 상태 갱신의 기여를 구별','Structure/Dynamics; Model/Method; Inference/Measurement','BF02;BF03;BF04;BF10','selective SSM; 고정 SSM; CortexMAE; TRIBE v2','긴 문맥 이득은 신경적 통합인가 관측과정의 자기상관인가?','과거전용 예측·HRF 대조·자기상관 보존 surrogate·run holdout','연속 시계열 확인 전 보류; beta-map trial 나열은 대체 입력으로 불가','E3; 코드404로 Brain-Mamba 직접 재사용 보류','04_brain_foundation','2026-11-12']]
with (p/'subaxes.csv').open('w',newline='',encoding='utf-8-sig') as f:
 w=csv.writer(f);w.writerow(cols);w.writerows(sub)
# 읽기 쉬운 한국어 기술 표기로 정리한다.
repls={
'공식코드':'공식 코드','공식저장소':'공식 저장소','공식README':'공식 README','학습자료':'학습 자료','학습목표':'학습 목표','원문확인':'원문 확인','본문접근':'본문 접근','가중치실행':'가중치 실행','본문검증':'본문 검증','논문본문':'논문 본문','본문성능':'본문 성능','본문결과':'본문 결과','가중치링크':'가중치 링크','가중치load':'가중치 load','체크포인트다운로드':'체크포인트 다운로드','다른Agent':'다른 Agent','다른모델':'다른 모델','데이터감사':'데이터 감사','정서관련':'정서 관련','신경정보':'신경정보','신경질문':'신경 질문','원계산원리':'원 계산원리','고정자료':'고정 자료','독립자료':'독립 자료','새질문':'새 질문','검증범위':'검증 범위','공간표현':'공간 표현','공간정보':'공간 정보','시간범위':'시간 범위','시간축':'시간축','시간변환':'시간 변환','정확한':'정확한','전체뇌':'전체 뇌','코드문서':'코드 문서','원자료':'원자료','범용표현':'범용 표현','피질모델':'피질 모델','평균피험자':'평균 피험자','평균subject':'평균 subject','개인별반응':'개인별 반응','표현고유정보':'표현 고유 정보','상태선택':'상태 선택','자료분포':'자료 분포','이환경':'이 환경','신호품질':'신호 품질','실행가용성':'실행 가용성','실측신뢰도':'실측 신뢰도','재현가능한':'재현 가능한','신뢰가능한':'신뢰 가능한','신뢰도높은':'신뢰도 높은','재현가능성':'재현 가능성','모형효과':'모형 효과','전체token':'전체 token','무작위/해부/기능순서':'무작위/해부/기능 순서','입력의존':'입력 의존','제거실험':'제거 실험','새benchmark':'새 benchmark','과학적개입':'과학적 개입','원신호':'원신호','구체분할':'구체 분할','저자E1':'저자 E1','연구팀E3':'연구팀 E3','엄밀한':'엄밀한','현재독립':'현재 독립','시계열길이':'시계열 길이','조건부모형':'조건부 모형','개인별변동':'개인별 변동','평가head':'평가 head','고정probe':'고정 probe','새피험자':'새 피험자','현단계':'현 단계','부정결과':'부정 결과','같은데이터':'같은 데이터','같은신경자료':'같은 신경자료','같은원자료':'같은 원자료','동일입력':'동일 입력','동일자료':'동일 자료','새실측자극반응':'새 실측 자극반응','이단계':'이 단계','전이자체':'전이 자체','표현학습':'표현학습','체크포인트링크':'체크포인트 링크','계산적설명':'계산적 설명','전체학습자료':'전체 학습 자료','논문집계':'논문 집계','서지확인':'서지 확인','직접읽은':'직접 읽은','후속코드식별':'후속 코드 식별','원문1편':'원문 1편','서지10편':'서지 10편','고유10편':'고유 10편','나머지9편':'나머지 9편','10편집계':'10편 집계','10편에추가':'10편에 추가','추가문헌':'추가 문헌','별도실험':'별도 실험','물리공간':'물리 공간','표형성능':'표형 성능','시간예측':'시간 예측','베타':'베타','피질전용':'피질 전용','시간순서교란':'시간순서 교란','피험자내':'피험자 내','모델간':'모델 간','사전학습중복':'사전학습 중복','자료정렬':'자료 정렬','가중치의지원':'가중치의 지원'}
for name in ['round1_report.md','model_cards.md']:
 f=p/name;t=f.read_text()
 for a,b in repls.items():t=t.replace(a,b)
 f.write_text(t)
# 구조 검증: 실제 실행 결과만 기록.
with (p/'papers.csv').open(encoding='utf-8-sig',newline='') as f:
 reader=csv.DictReader(f);r=list(reader);assert len(reader.fieldnames)==32 and len(r)==10
 assert len({x['paper_id'] for x in r})==10
 assert all(all(x[k] for k in reader.fieldnames) for x in r)
 assert sum(x['full_text_access'].startswith('예') for x in r)==1
(p/'validation.json').write_text(json.dumps({'verified_on':'2026-11-12','paper_rows':len(r),'columns':32,'unique_paper_ids':10,'full_text_papers':1,'discussion_papers':1,'author_future_directions':5,'subaxes':3,'model_execution_performed':False,'checkpoint_download_performed':False,'csv_validation':'통과'},ensure_ascii=False,indent=2))
print('CSV 구조검증 통과:10문헌/32열/원문1/저자future5/신규subaxis3')
