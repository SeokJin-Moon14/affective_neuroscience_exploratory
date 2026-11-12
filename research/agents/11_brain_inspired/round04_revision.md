# Agent 11 Round 4 비판 응답과 재구성

2026-11-12. Agent06·10이 실제 작성한 비판 10개에 응답했다. 오차/gate의 독립정보 주장, 유한 재귀 구현 식별 주장을 철회했고 C11-04는 방법후보로 분리했다. 새 연결2개와 잠정 shortlist2개를 제시한다.

## 비판 응답

### C11-01 · 수정 후 조건부 발전

실제 비판: R3-06-C11-01, R3-10-C11-01

수용: E=f(A,Ahat)의 결정성을 명시하고 추가 정보 주장을 철회; A,Ahat,R 전체 입력 및 함수족/유효복잡도 일치 대조 추가; 주 추정량을 독립 정서 신경 대비의 보류 손실·표본효율로 고정

남은 의견 차이: 비판 수용. 제한된 readout의 효율도 관측적 계산 제약 후보로는 보존하지만 신경 error unit이나 정보이론적 증분으로 해석하지 않는다. 효율만 보이면 방법 결과로 낮춘다.

두 실제 비판의 결정성·동등성·추정대상 문제를 반영했다. 스키마 미확인은 구현 조건이며 문헌 작업의 차단 조건이 아니다.

### C11-02 · 수정 후 조건부 발전

실제 비판: R3-06-C11-02, R3-10-C11-02

수용: gate의 결정 입력과 미선택 expert 출력까지 내용 기준에 포함; 특정 내용 요약/함수족 대비 gate 좌표 접근성으로 축소; output-matched routing의 존재 여부와 분포 내 교환 조건 명시

남은 의견 차이: 비판 수용. 완전 입력과 충분한 함수족에서 gate의 새 정보는 없지만, 사전 제한한 계산 예산의 유용한 좌표는 시험 가능하다. 대체 routing이 항상 존재한다고 가정하지 않는다.

두 실제 비판의 결정성·동등성·추정대상 문제를 반영했다. 스키마 미확인은 구현 조건이며 문헌 작업의 차단 조건이 아니다.

### C11-03 · 수정 후 조건부 발전

실제 비판: R3-06-C11-03, R3-10-C11-03

수용: 유한 재귀와 동일 가중치 exact-unroll의 출력/중간상태 대응을 선행 점검; 주 질문을 공유제약의 학습·길이/조합 일반화로 변경; 공유효과·일반 규제·내용 순서를 별도 요인으로 분리

남은 의견 차이: 재귀 구현의 식별 불가를 수용한다. 공유제약이 낳는 학습 일반화는 남지만 그 결과를 인간 뇌의 가중치 공유 증거로 부르지 않는다.

두 실제 비판의 결정성·동등성·추정대상 문제를 반영했다. 스키마 미확인은 구현 조건이며 문헌 작업의 차단 조건이 아니다.

### C11-04 · 수정: 방법후보로 분리·직접 신경기전 해석 보류

실제 비판: R3-06-C11-04, R3-10-C11-04

수용: 직접 신경기전 후보를 보류하고 방법후보로 분리; 한 구조쌍·한 목적·한 대비·관측 및 readout family를 사전 고정; 관측 등가 검정에 가역 재매개화·등가통제·신호 주입/거짓양성 보정 포함

남은 의견 차이: 독립 과학질문으로 유지할 수 있다는 원안의 범위를 철회한다. 식별 한계 지도는 유익하나 현재는 방법 모듈이며 구체 정서 경쟁예측이 확보돼야 과학 RQ로 재심사한다.

두 실제 비판의 결정성·동등성·추정대상 문제를 반영했다. 스키마 미확인은 구현 조건이며 문헌 작업의 차단 조건이 아니다.

### C11-05 · 수정 후 조건부 발전

실제 비판: R3-06-C11-05, R3-10-C11-05

수용: cross-fitted semantic-predicted neural guide와 실제 neural guide를 분리; 풍부한 독립 사건/관계 의미 및 공분산·신뢰도·손실 scale 대조 추가; 잔차 guide를 순수 정서/신경고유 정보로 명명하지 않고 새 사람×새 내용에서 평가

남은 의견 차이: 의미 정보 완전 제거는 요구하지 않으며 가능하다고 주장하지 않는다. 비교한 강한 semantic-predicted guide를 넘어선 추가 효용이라는 상대적 주장만 허용한다.

두 실제 비판의 결정성·동등성·추정대상 문제를 반영했다. 스키마 미확인은 구현 조건이며 문헌 작업의 차단 조건이 아니다.

## 새 연결

### UC11-01 · 표현 비교의 불변성·계산 그래프 검증

**original_computational_goal:** P051은 신경망 표현 유사성 비교를, P096은 예측부호화와 역전파 계산 관계를 다룬다. P090의 반복 블록은 유한 계산 그래프로 펼칠 수 있는 구현이다.

**imported_structure:** 같은 정보·함수에 대한 재매개화와 정확한 계산 경로 변환을 검정의 등가 통제로 삼는다.

**new_neural_question:** 표현 좌표의 효율과 인간 신경 계산 구현의 식별을 나눴을 때, 독립 정서 대비가 실제로 제약하는 것은 어느 수준인가?

**why_not_same_as_round2:** Round2의 모델 변수 분해를 넘어, 동일 함수이면 같아야 하는 검정 불변성 조건을 도입하고 그 조건을 통과한 뒤 학습 효율만 비교한다.

**assumptions:** exact-unroll은 모든 상태갱신·정규화·초기상태를 보존해야 함; readout family가 변환을 흡수하는 조건과 제한 예산의 조건을 분리; P096의 근사 정리를 모든 구현의 exact equivalence로 일반화하지 않음

**discriminating_test:** 동등 정보/동일 함수 통제가 신경 평가에서 차이를 만드는지 먼저 확인하고, 차이가 있으면 분석/학습 좌표 효과를 조사한다. 이후 자료량·길이 OOD의 학습제약 효과만 비교한다.

**failure_interpretation:** 등가통제 실패는 미시 신경 발견이 아니라 구현·readout·평가 절차의 문제다.

**evidence_scope:** P051 본문 검증은 기존 catalog 기록; Agent11이 이번에 재열람하지 않음. P090/P096은 직접 읽은 공식 코드 범위. 신경 전이는 E3.

근거: P051, P096, P090

### UC11-02 · 자극 기반 대체 측정과 교사 신호 검증

**original_computational_goal:** P027은 자극에서 집단 피질반응을 예측하고 P050은 metadata로 표현의 보존/억제를 지도한다. P100은 표현 추론의 일반화 단위를 다룬다.

**imported_structure:** 비용이 큰 실제 신경 교사와 자극만으로 예측한 대체 신경 교사를 cross-fit해 동일 adapter에서 비교한다.

**new_neural_question:** 신경 측정이 제공하는 감독의 효용은 풍부한 의미로 예측 가능한 교사 정보로 충분한가, 지정된 대체 교사를 넘는 안정된 추가 효용이 있는가?

**why_not_same_as_round2:** Round2의 neural/semantic/random guide 비교를 대체 신경 교사와 실제 교사의 같은 target 형식 비교로 바꾸고 교사 생성과 평가의 cross-fitting을 명시했다.

**assumptions:** 자극 predictor와 guide는 outer 평가 신경 데이터를 보지 않음; 잔차는 순수 정서 또는 완전한 신경 고유정보가 아님; 교사 신뢰도·공분산·예측되는 자극정보를 보고하되 완전 정보량 매칭을 주장하지 않음

**discriminating_test:** 실제 neural, cross-fit predicted neural, cross-fit residual, 풍부한 의미 교사의 모델 전이 손실과 새 사람×새 자극의 정서 신경 대비 손실을 공동 비교한다.

**failure_interpretation:** 대체 교사로 충분하면 지정 비교에서 신경 측정의 추가 감독 효용을 지지하지 않는다. 인간 신경 계산의 의미 환원을 증명하지는 않는다.

**evidence_scope:** P027/P050 공식 문서 확인 및 P100 본문 확인은 기존 역할/catalog 기록을 계승; 이번 신규 원문 확인 없음. 대체 교사 연결은 E3.

근거: P027, P050, P100

## 수정 후보 전체

### C11-01 · 동일 입력정보에서 오차 좌표는 정서 신경 대비의 제한된 읽기 효율을 높이는가

역할: 과학RQ후보; Axis: AS25, AS35, AS10, AS29

**research_question:** A·Ahat·R의 동일 정보와 허용 함수족 아래, 명시적 오차 좌표가 독립 정서 신경 대비의 표본효율을 일반 시각 대비보다 선택적으로 바꾸는가?

**neural_target:** 사전 정의한 정서 주석 대비에 대한 보류 신경 대비 예측 손실; 전체 BOLD 손실은 보조 지표

**model_application:** 현재 A, 예측 Ahat, 상태 R을 모든 조건에 제공하고 E+=ReLU(Ahat−A), E−=ReLU(A−Ahat)를 고정 계산한다. 동일 정보의 여러 좌표를 같은 유효 readout 예산에서 비교한다.

**scientific_question:** 추가 정보가 아닌 계산 좌표의 접근성 차이가 정서 대비에서 선택적인가?

**assumption_challenge:** E의 조건부 이득을 독립 신경정보 또는 prediction-error unit 증거로 읽는 가정을 철회한다.

**main_hypothesis:** 같은 데이터·입력정보의 제한 readout에서 오차 좌표의 학습곡선 이득이 신뢰도 일치 비정서 대비보다 크다.

**alternative:** 일반 함수근사·조건수·현재 입력 누락·명도/의미 변화로 충분하다.

**measurable_contrast:** 동일 train/test와 각 표본수 n에서 사전 정서 대비의 평균제곱 예측손실 차이를 측정한다. 파라미터/계산예산 고정 곡선과 충분한 함수족의 포화곡선을 분리한다. [E+,E−]와 [E,abs(E)]는 서로 결정되는 재표현 대조로 사용한다.

**falsification:** 충분한 readout에서 차이 소멸은 독립 정보 가설의 반증과 일치하며 예상 가능한 결과다. 제한 예산에서도 선택적 이득이 없거나 일반 시각 대비와 같으면 정서 관련 효율 가설을 축소한다.

**baseline:** A+Ahat+R를 모두 보는 동일 비선형 함수족; 원 입력에서 고정 오차변환을 계산하는 정확 동등 경로; 상태·절대오차·방향오차를 동일 입력정보로 비교; 가역 오차 좌표 재표현; 명도·색·사건관계 일치 자극 및 신뢰도 일치 비정서 대비

**dataset_plan:** 보유 Horikawa 자극과 신경/정서 대비로 자극별 검정을 우선 설계한다. 연속 프레임·주석이 확인되면 Emo-FilM/Spacetop의 시간 비교로 확장; 시간 주석 없으면 궤적 주장은 하지 않는다.

**missing_conditions:** 자극 프레임·제시 timing·독립 정서 주석 단위; checkpoint와 입력 정규화 확인; 오차 부호를 정의할 감각 좌표; JEPA latent 부호는 일반적으로 회전 비식별적; A/Ahat/R의 완전 입력 감사; 함수족/유효 복잡도와 학습예산 일치; 독립 정서·비정서 대비의 신뢰도 매칭

**what_is_new:** 원안의 추가정보 주장을 폐기하고 동일정보 재매개화의 표본효율×정서대비 선택성으로 실질적으로 변경했다. 신경 error unit의 실재 검증은 아니다.

**novelty_risk:** 높음: 정서 예측오차 선행연구와 겹칠 수 있다. 이번 Round2는 신규 외부 검색 없이 기존 문헌 역대조만 수행했다.

**interpretation_boundary:** 모델 좌표/구조/학습의 비교는 지정 입력·관측 연산자·허용 readout에서의 예측 주장이다. 인간 뇌의 미시 회로·spike timing·가중치 공유·학습 규칙을 식별한 것으로 해석하지 않는다.

**여덟 질문:**

1. Q1 최초성 미확인; 파생 좌표의 정보 증가와 readout 효율을 혼동하기 쉬웠다.

2. Q2 공개 A/Ahat/R/E 접근으로 동일정보 좌표를 실제 비교 가능하다.

3. Q3 오차가 원 입력보다 새 정보를 갖는다는 가정을 철회한다.

4. Q4 AI는 원 입력과 파생 좌표·readout 예산을 명시적으로 통제한다.

5. Q5 잔여 신경 대비는 모델/의미 누락 또는 잡음일 수 있어 미시기전으로 명명하지 않는다.

6. Q6 재매개화 불변성 검사를 정서 대비의 좌표 효율 검정에 수입한다.

7. Q7 같은 자극·신경 대비를 표본수/예산별 학습곡선에 재사용한다.

8. Q8 효율이 정서 대비에 선택적일 때만 조건부 계산 좌표 제약으로 남긴다.

**역검색:** signed prediction error neural encoding emotional stimuli nonlinear readout efficiency

https://github.com/search?q=signed+prediction+error+neural+encoding+emotional+stimuli+nonlinear+readout+efficiency&type=repositories

실제 GitHub 검색 HTTP200, 0건. 학술 전수 검색이 아니며 최초성 근거로 사용하지 않는다.

**10항목 잠정 평가:**

| 항목 | 점수 | 근거 |

|---|---:|---|

| novelty | 2 | 파생특징의 효율 비교와 겹쳐 신규성은 제한적이다. |

| neuro_importance | 3 | 정서 대비의 읽기 제약을 좁히지만 error unit을 밝히지는 않는다. |

| ai_necessity | 2 | 단순 고정변환과 강한 readout으로 핵심 대조가 가능하다. |

| data_feasibility | 3 | 자극별 대비부터 가능하나 입력과 반복 schema 확인이 필요하다. |

| rigor | 4 | 정보예산·함수족·학습곡선 대조를 명시했다. |

| falsifiability | 4 | 선택적 효율 부재와 일반 함수근사 설명으로 반증 가능하다. |

| interpretability | 4 | 추가 정보 주장을 철회해 접근성 해석이 명료하다. |

| generalization | 3 | 새 자극/내용 전이는 계획했으나 자료 다양성 미확인이다. |

| technical_feasibility | 3 | PredNet 내부 변수는 코드상 접근 가능하지만 실행 미검증이다. |

| exploration_value | 3 | 익숙한 오차 encoding의 해석 한계를 생산적으로 드러낸다. |

평가 공통 불확실성: 실행·스키마·checkpoint·신규성 미확인. 가중합 선정 없음.

**Shortlist:** False — 결정적 파생특징의 접근성 질문으로 축소했으므로 최상위 우선순위는 낮춘다.

**근거:** [P089](https://github.com/coxlab/prednet), [P046](https://arxiv.org/abs/2404.08471), [P096](https://github.com/BerenMillidge/PredictiveCodingBackprop), [P051](https://proceedings.mlr.press/v97/kornblith19a.html)

### C11-02 · 완전한 내용 입력에서 gate 좌표의 효율과 재매개화 안정성

역할: 과학RQ후보; Axis: AS26, AS34, AS11, AS29

**research_question:** pre-gate 입력과 모든 전문가 내용을 제공한 제한된 읽기 모형에서 gate 좌표의 정서 대비 예측 효율은 내용 해상도·부하 제약·출력 동등 재routing에 얼마나 견고한가?

**neural_target:** 독립 자극·피험자에서 재현되는 정서 관련 분산 BOLD 및 경로-내용 조건부 설명분

**model_application:** 선택되지 않은 expert 출력까지 가능한 범위에서 계산하고 pre-gate 입력, logits/dispatch, drop token과 load를 기록한다. 내용 해상도를 증가시키며 gate의 조건부 접근성 곡선을 추정한다.

**scientific_question:** 독립 routing 정보의 존재가 아니라 같은 입력의 어떤 기능적 좌표가 정서 대비 예측에 경제적인가?

**assumption_challenge:** 불완전한 내용 요약 대비 gate 이득을 뇌의 routing 정보로 읽지 않는다.

**main_hypothesis:** 사전 제한한 readout 예산에서 gate 좌표의 효율이 풍부한 내용 기준과 동등 출력의 대체 routing 통계에서 안정적으로 나타난다.

**alternative:** 미선택 expert·관계 의미의 누락, gate×출력의 추가 비선형성, load/위치 통계가 이득을 설명한다.

**measurable_contrast:** 같은 보류 정서 신경 대비에서 내용 해상도×readout 예산별 예측손실 차이를 구한다. pre-gate 입력의 유연한 attention 재가중 baseline을 추가한다. 출력/과제손상 허용범위 내 대체 routing이 실제로 구성되는 경우에만 route invariance를 비교한다.

**falsification:** 완전 내용과 유연한 readout에서 이득이 소멸하면 별도 정보 주장을 배제한다. 제한 예산의 효율도 소멸하거나 출력 동등 routing에서 통계가 불안정하면 안정된 route 좌표 해석을 보류한다.

**baseline:** pre-gate 입력의 비선형 readout; all-expert content와 attention 가중합; 부하/top-k/패치수 고정; 동일 출력 대체 routing: 존재 확인 후 적용; 유사 입력의 분포 내 gate 교환·손상량 일치 대조

**dataset_plan:** Horikawa의 정서 대비와 자극별 반응을 우선 후보로 둔다. 시청각 확장은 Emo-FilM/Spacetop의 실제 modality 확인 뒤 수행한다. 원 V-MoE는 이미지 routing이며 시간 gate가 이미 구현됐다고 가정하지 않는다.

**missing_conditions:** 자극/신경/정서 주석 연결; 현재 checkpoint와 논문판 코드 차이; 공유/고유 분해의 fold 내부 학습과 seed 안정성; 미선택 expert를 포함한 텐서 추출 비용; 출력 동등 재routing 존재 여부; 없으면 불가능 상태로 기록; 독립 자극에서 gate 교환의 분포 적합성

**what_is_new:** 원안의 gate 고유정보를 철회하고 완전 입력 아래 기능적 좌표의 접근성·동등 재routing 안정성으로 수정했다.

**novelty_risk:** 높음: 조건부 계산 해석과 신경 encoding 조합의 중복 가능. expert-ROI 대응 자체는 신규성 근거로 삼지 않는다.

**interpretation_boundary:** 모델 좌표/구조/학습의 비교는 지정 입력·관측 연산자·허용 readout에서의 예측 주장이다. 인간 뇌의 미시 회로·spike timing·가중치 공유·학습 규칙을 식별한 것으로 해석하지 않는다.

**여덟 질문:**

1. Q1 최초성 미확인; 미선택 expert와 gate 결정입력의 누락이 문제다.

2. Q2 공개 routing으로 pre-gate와 dispatch 기록을 계획할 수 있다.

3. Q3 gate 이득이 독립 경로 정보라는 가정을 철회한다.

4. Q4 AI는 동일 출력의 대체 계산과 내용 해상도 곡선을 구성할 수 있는 후보 도구다.

5. Q5 뇌의 선택적 전달이 존재하더라도 모델 gate 대응만으로 판정하지 못한다.

6. Q6 함수 동등성 및 계산좌표 검사를 조건부 계산에 전이한다.

7. Q7 기존 자극 대비로 내용 요약의 완전성에 따른 gate 효율을 평가한다.

8. Q8 내용 압축으로 충분한지와 제한 예산의 유용한 gate 좌표를 구별한다.

**역검색:** mixture experts routing brain alignment gate content information equivalence

https://github.com/search?q=mixture+experts+routing+brain+alignment+gate+content+information+equivalence&type=repositories

실제 GitHub 검색 HTTP200, 0건. 학술 전수 검색이 아니며 최초성 근거로 사용하지 않는다.

**10항목 잠정 평가:**

| 항목 | 점수 | 근거 |

|---|---:|---|

| novelty | 2 | gate 해석 선행과 근접하여 최초성은 미확정이다. |

| neuro_importance | 3 | 내용 대 기능 좌표의 범위를 좁히지만 뇌 routing은 식별하지 않는다. |

| ai_necessity | 3 | 명시 gate 추출이 필요하나 강한 내용 재가중으로 대체될 수 있다. |

| data_feasibility | 2 | all-expert 추출과 독립 정서 대비의 실제 조건이 미확인이다. |

| rigor | 3 | 완전 입력을 넣었지만 대체 routing 존재 및 손상 매칭이 어렵다. |

| falsifiability | 3 | 풍부한 내용기준의 충분성과 route 불안정으로 주장을 축소할 수 있다. |

| interpretability | 3 | 조건부 좌표로 낮췄으나 재매개화 동등류는 남는다. |

| generalization | 3 | seed·내용·routing 변형을 계획했으나 실증 전이다. |

| technical_feasibility | 2 | 미선택 expert 계산과 동등 routing 구성 비용이 불명확하다. |

| exploration_value | 3 | 전문가 번호를 뇌 경로로 읽는 관행에 강한 통제를 준다. |

평가 공통 불확실성: 실행·스키마·checkpoint·신규성 미확인. 가중합 선정 없음.

**Shortlist:** False — 대체 routing의 비유일성과 추출 부담이 커 먼저 방법 타당성 확인이 필요하다.

**근거:** [P093](https://github.com/google-research/vmoe), [P037](https://github.com/pliang279/FactorCL), [P038](https://github.com/google-research/scenic/tree/main/scenic/projects/mbt), [P051](https://proceedings.mlr.press/v97/kornblith19a.html)

### C11-03 · 유한 함수 동등성을 인정한 공유제약의 정서 대비 일반화 효율

역할: 과학RQ후보; Axis: AS27, AS36, AS23, AS35

**research_question:** 정확히 펼친 유한 반복망과의 함수 동등성을 확인한 뒤, 가중치 공유라는 학습 제약은 새 사건 길이·조합에서 독립 정서 신경 대비의 예측 효율을 바꾸는가?

**neural_target:** 사건 단계별 정서 대비와 연결된 신경 표현의 일반화; 실제 시간 해상도가 허용하는 범위

**model_application:** 같은 가중치를 복사한 exact-unroll에서 출력과 대응 중간상태 일치를 확인한다. 그 후 같은 함수에서 시작한 공유/비공유 모델을 데이터량·반복 길이별로 학습한다.

**scientific_question:** 재귀 구현의 신경 실재가 아니라 공유제약이 제공하는 학습·전이 편향이 정서 대비에서 선택적인가?

**assumption_challenge:** 같은 함수의 encoding으로 재귀와 feedforward 구현을 구별한다는 가정을 철회한다.

**main_hypothesis:** 유한 관측에서는 exact-unroll과 같지만 학습 밖 길이·사건 조합에서 공유제약이 정서 대비 예측의 효율을 높이며 일반 시각 정확도 대조로 완전히 설명되지 않는다.

**alternative:** 파라미터 감소의 일반 규제·위치/순서 정보·깊이·학습량만으로 충분하다.

**measurable_contrast:** 학습 자료량×공유 제약×반복수 요인에서 보류 사건 길이/조합의 정서 대비 손실과 일반 시각 대비 손실을 비교한다. 파라미터/FLOPs/정확도 맞춤 결과는 별도 보고하고 내부 step을 신경 시간으로 변환하지 않는다.

**falsification:** exact-unroll 출력 불일치면 구현 점검 단계에서 중단한다. OOD 효율이 비공유·일반 규제·순서무관 대조와 같으면 공유제약의 해당 범위 필요성을 지지하지 않는다.

**baseline:** 동일 가중치 exact-unroll; 동일 함수 초기화 비공유 모델; 일반 parameter regularization; 공유가중치 순서무관 pooling; 학습량/길이 및 인식 성능 맞춤 대조; 독립 단계·position-only·동일 사건집합 순서교환

**dataset_plan:** Horikawa에서 자극별 계산 비교를 먼저 계획한다. 실제 연속 timing·사건 다양성이 있는 보유 자료에서 단계 비교를 수행하며, 속도 조작 실측이 없으면 속도 불변성의 인과 주장은 하지 않는다.

**missing_conditions:** 사건 경계/단계 주석 또는 비신경 독립 추정; 연속 자료와 run 경계; 동일 목표/학습자료의 통제 모델 생성 비용; 모든 상태갱신·정규화·초기상태를 보존한 정확 펼침; 길이 OOD와 자극 의미 OOD의 분리; 외부 사건 단계 및 순서 정의

**what_is_new:** 재귀의 뇌 구현 판별에서 공유제약의 학습/길이 전이 효율로 핵심 주장을 바꿨다. exact-unroll 통제는 결과가 아니라 미실행 검증 절차다.

**novelty_risk:** 중간~높음: 재귀와 깊이 비교는 기존 주제. 정서 대비와 단계 shortcut의 동시 판별이 차별 후보지만 최초성 미검증.

**interpretation_boundary:** 모델 좌표/구조/학습의 비교는 지정 입력·관측 연산자·허용 readout에서의 예측 주장이다. 인간 뇌의 미시 회로·spike timing·가중치 공유·학습 규칙을 식별한 것으로 해석하지 않는다.

**여덟 질문:**

1. Q1 최초성 미확인; 유한 재귀와 펼친 망의 함수 동등성을 먼저 인정해야 한다.

2. Q2 공개 반복 구조에서 exact-unroll 및 학습량 대조를 설계할 수 있다.

3. Q3 encoding으로 구현상의 재귀를 식별한다는 가정을 철회한다.

4. Q4 AI는 동일 초기 함수에서 공유제약의 학습 효과를 분리한다.

5. Q5 뇌와 모델의 길이 전이 차이가 있어도 가중치 공유의 직접 증거는 아니다.

6. Q6 계산 그래프 동등성 검사를 OOD 구조제약 평가에 수입한다.

7. Q7 사건 길이·내용 조합의 보류 분할로 기존 자료를 재활용한다.

8. Q8 결과는 공유제약의 학습 편향을 정서 대비에 연결하는 상대적 모델 제약이다.

**역검색:** weight tying recurrent neural networks brain encoding sample efficiency generalization

https://github.com/search?q=weight+tying+recurrent+neural+networks+brain+encoding+sample+efficiency+generalization&type=repositories

실제 GitHub 검색 HTTP200, 0건. 학술 전수 검색이 아니며 최초성 근거로 사용하지 않는다.

**10항목 잠정 평가:**

| 항목 | 점수 | 근거 |

|---|---:|---|

| novelty | 3 | 공유제약과 OOD 효율 자체는 기존이며 정서 대비 연결만 후보이다. |

| neuro_importance | 3 | 구현보다 학습 편향의 신경 대비 관련성을 제한적으로 평가한다. |

| ai_necessity | 3 | 반복/펼침 통제 모델이 필요하지만 초대형 모델은 필요하지 않다. |

| data_feasibility | 2 | 길이·사건 조합과 독립 정서 대비의 충분성이 미확인이다. |

| rigor | 4 | exact-unroll과 여러 예산 대조로 핵심 혼동을 명시했다. |

| falsifiability | 4 | 등가 검증 실패와 OOD 효율 부재의 중단 조건이 명료하다. |

| interpretability | 4 | 재귀 실재 주장을 철회해 조건부 해석 경계가 분명하다. |

| generalization | 4 | 새 길이×새 조합 평가를 질문의 중심에 둔다. |

| technical_feasibility | 2 | 동일 자료/초기함수의 제어 학습은 구현 비용이 있다. |

| exploration_value | 4 | 신경 비교가 구현 식별보다 학습 제약에 주는 정보를 재정의한다. |

평가 공통 불확실성: 실행·스키마·checkpoint·신규성 미확인. 가중합 선정 없음.

**Shortlist:** True — exact-unroll을 통과한 공유제약의 OOD 효율을 독립 정서 대비와 연결하는 제한된 질문이 명료하다.

**근거:** [P090](https://github.com/dicarlolab/CORnet), [P042](https://github.com/google-research/google-research/tree/master/tcc), [P043](https://github.com/OpenGVLab/VideoMamba), [P096](https://github.com/BerenMillidge/PredictiveCodingBackprop)

### C11-04 · 고정 관측·readout에서 한 스파이크/율 구조쌍의 대비 회수 감사

역할: 방법후보; Axis: AS27, AS09, AS30, AS14

**research_question:** 같은 입력·다음 상태 예측 목표의 LIF recurrent 모델과 smooth-rate recurrent 모델에서 사전 지정한 이력×정서 대비의 차이는 고정 관측·readout family에서 어느 효과크기까지 회수 가능한가?

**neural_target:** 정서 대비에서 모델 간 관측 등가성 및 검출 가능한 효과의 상한; 실제 spike timing 측정 아님

**model_application:** 같은 연결·입력·목표를 가진 소형 LIF/율 구조쌍 하나를 사용한다. 학습 규칙 비교는 이번 모듈에서 제외한다. 관측 family와 readout rank/용량을 사전에 고정하고 등가 통제와 알려진 신호 주입을 검정한다.

**scientific_question:** 현재는 정서 신경 기전의 직접 질문이 아니라 특정 대비의 검출력·거짓양성·동등성 검정이 유효한지 평가하는 방법 질문이다.

**assumption_challenge:** 차이가 관측 연산 뒤 남으면 실제 뇌 구현을 식별했다는 가정을 배제한다.

**main_hypothesis:** 사전 정의한 표적 대비와 효과크기의 회수 가능 범위를 모형 쌍·관측·readout family별로 보정할 수 있다. 특정 인간 뇌 구조의 우위를 예측하지 않는다.

**alternative:** readout 재매개화·rank·시간대역·활성단위 또는 HRF 선택이 겉보기 구별을 만든다.

**measurable_contrast:** 정서 대비는 독립 주석으로 정의한 동일 현재사건/상이 이력의 조건간 신경 대비로 고정한다. 시뮬레이션에서는 그 설계벡터 방향의 알려진 효과크기를 주입해 회수율/거짓양성률/CI coverage를 산출하도록 계획한다. 결과는 아직 없다. 실제 자료에서는 같은 대비의 held-out 손실 차이와 사전 동등성 범위를 적용한다.

**falsification:** 등가통제의 거짓양성 또는 사전 효과크기의 회수 실패면 신경 비교에 적용하지 않는다. 가정 family에 따라 방향이 바뀌면 기전 해석을 보류한다.

**baseline:** 동일 함수 및 가역 재표현 등가통제; 알려진 대비 신호 주입; 시간대역·공분산·rank·활성규모 일치; 사전 고정 복수 HRF와 readout family

**dataset_plan:** 보유 fMRI는 정서 관련 표상 차이 평가의 후보이며 밀리초 기전 확인 자료로 쓰지 않는다. Horikawa부터 실제 신뢰도·반복 정보를 확인하고, timing 부재 시 자극 집계 수준의 등가성 평가로 제한한다.

**missing_conditions:** 단일 LIF/율 구조쌍의 동일 목표 구현; 독립 대비 설계벡터와 최소 의미효과; TR·신뢰도·시간대역·HRF 범위; 허용 readout family 사전등록; e-prop P091은 별도 학습규칙 후속으로만 남기며 서지 보류 유지

**what_is_new:** 원안의 여러 구조×학습 규칙을 비교하는 포괄 과학후보를 철회하고 단일 구조쌍의 검정 보정 모듈로 좁혔다. 구체 정서 경쟁예측을 확보할 때만 과학 RQ 재심사한다.

**novelty_risk:** 중간: 관측 등가성과 신경 모델 비식별성은 기존 주제. 정서 대비에서 구체적인 차이 회수/동등성 범위를 제시해야 기여가 된다.

**interpretation_boundary:** 모델 좌표/구조/학습의 비교는 지정 입력·관측 연산자·허용 readout에서의 예측 주장이다. 인간 뇌의 미시 회로·spike timing·가중치 공유·학습 규칙을 식별한 것으로 해석하지 않는다.

**여덟 질문:**

1. Q1 기존 식별성 방법의 확장으로 보고 최초성을 주장하지 않는다.

2. Q2 공개 SNN/율 구현에서 단일 구조쌍의 보정을 구체화할 수 있다.

3. Q3 시뮬레이션 차이 검출이 생체 구조 식별이라는 가정을 배제한다.

4. Q4 AI는 알려진 동등·비동등 조건을 만들어 검정 자체를 감사한다.

5. Q5 뇌가 가진 미세 정보가 관측에서 소실될 수 있지만 이번에 측정한 사실은 아니다.

6. Q6 통계적 coverage/거짓양성 보정을 생물학적 모델 비교에 전이한다.

7. Q7 반복 자료는 신뢰도·최소효과 보정에 쓰이며 학습규칙 확인 자료로 간주하지 않는다.

8. Q8 현재 기여는 방법 경계이며 독립 정서 기전 RQ로 집계하지 않는다.

**역검색:** spiking rate neural networks fMRI observational equivalence readout identifiability

https://github.com/search?q=spiking+rate+neural+networks+fMRI+observational+equivalence+readout+identifiability&type=repositories

실제 GitHub 검색 HTTP200, 0건. 학술 전수 검색이 아니며 최초성 근거로 사용하지 않는다.

**10항목 잠정 평가:**

| 항목 | 점수 | 근거 |

|---|---:|---|

| novelty | 2 | 일반 식별/QC 방법 확장이므로 독립 신규성은 낮다. |

| neuro_importance | 2 | 정서 기전 답보다 잘못된 기전 주장을 막는 보조 가치다. |

| ai_necessity | 2 | 소형 모의 모델과 통계 보정으로 상당 부분 가능하다. |

| data_feasibility | 3 | 합성 보정은 가능하나 실제 대비/신뢰도 확인이 남는다. |

| rigor | 4 | 한 구조쌍과 고정 readout의 회수·거짓양성을 평가한다. |

| falsifiability | 4 | 사전 효과의 회수와 CI coverage 실패로 적용을 중단한다. |

| interpretability | 4 | 방법 역할과 인간 뇌 기전의 경계를 명확히 분리했다. |

| generalization | 2 | 단일 구조쌍의 결과를 다른 생물학적 제약으로 일반화하지 않는다. |

| technical_feasibility | 3 | 소형 구현은 계획 가능하지만 LIF/율 정합 검증은 미실행이다. |

| exploration_value | 3 | 다른 후보의 관측 한계를 정량화할 방법 모듈 가치가 있다. |

평가 공통 불확실성: 실행·스키마·checkpoint·신규성 미확인. 가중합 선정 없음.

**Shortlist:** False — 일반 식별/QC 모듈로 분리하여 독립 과학 shortlist에서는 제외한다.

**근거:** [P092](https://github.com/fzenke/spytorch), [P094](https://github.com/ZK-Zhou/spikformer), [P100](https://elifesciences.org/articles/82566), [P096](https://github.com/BerenMillidge/PredictiveCodingBackprop)

### C11-05 · 실제 신경 guide는 의미로 예측한 신경 guide를 넘는 모델 제약인가

역할: 과학RQ후보; Axis: AS08, AS11, AS12, AS27

**research_question:** 풍부한 자극 의미로 cross-fit 예측한 neural guide와 통계구조를 맞춘 뒤에도 실제 신경 guide는 새 내용×새 피험자에서 모델 상태예측과 독립 정서 신경 대비에 추가 효용을 주는가?

**neural_target:** 훈련과 분리된 피험자/자극의 독립 정서 대비; 신경 유도 모델의 보류 맥락 일반화

**model_application:** 훈련 fold 내부에서 자극만으로 neural target을 예측하는 teacher를 cross-fit한다. 같은 adapter에 실제 neural target, cross-fit 예측 target, 그 잔차, 풍부한 독립 의미 guide 및 통계구조 일치 sham을 각각 제공한다.

**scientific_question:** 신경 측정이라는 감독 원천이 지정한 강한 자극 예측 guide를 넘어 유용한 모델 제약을 제공하는가?

**assumption_challenge:** 무작위 guide보다 neural guide가 좋으면 뇌 고유 계산을 발견했다는 가정을 철회한다.

**main_hypothesis:** 실제 neural guide 또는 신뢰 가능한 cross-fit 잔차 guide가 강한 semantic-predicted neural guide보다 새 내용/사람의 이중 지표에서 추가 효용을 보인다.

**alternative:** 구조화된 의미 감독·자극 ID·추가 label 정보량·신뢰도·일반 규제 및 readout 맞춤으로 충분하다.

**measurable_contrast:** 동일 adapter의 보류 상태예측 손실과 새 피험자×새 자극의 정서 신경 대비 손실을 각각 사전 고정한다. 두 지표 개선을 공동 요구한다. guide별 rank·공분산·smoothness·반복 신뢰도·손실 scale과 자극 속성 예측력을 보고하되 완전 정보량 일치를 주장하지 않는다.

**falsification:** semantic-predicted neural guide로 충분하면 지정 비교에서 신경 측정의 추가 감독 효용을 지지하지 않는다. 신경 정렬만 좋아지면 계산 사용 주장을 낮춘다. 손상량 일치/분포 내 ablation에서 효용이 사라지면 제거 효과의 해석을 보류한다.

**baseline:** cross-fitted stimulus-only predicted neural guide; 외부 검수 객체·관계·사건 의미 guide; 실제 neural guide와 cross-fitted residual guide; 공분산/신뢰도/smoothness 일치 sham; 동일 adapter·손실 scale·학습 예산; 손상량 일치 및 분포 내 feature 교체

**dataset_plan:** Horikawa 보유 자료에서 독립 정서 대비·반복·자극 분리가 확인되면 소형 adapter 계획을 구체화한다. NSD는 정서 라벨을 가정하지 않는 감각 대조; Mind Captioning은 식별자·주석 미확인 상태로 후속 의미 대조 후보만 유지한다.

**missing_conditions:** 독립 정서 대비의 구성 타당성·신뢰도; 훈련/검증/외부평가 피험자·자극 분리; 모델 checkpoint·adapter 지원·비정서 예측 목표; 신경 guide와 의미 guide의 정보량 매칭; 훈련-only cross-fitting과 outer 피험자×내용 분리; 의미 guide는 자극/독립 사람이 만든 설명이며 같은 뇌에서 만든 캡션 제외; guide의 신뢰도·공분산과 자극속성 예측력 보고; 완전 의미 제거 불가에 대한 잔여 한계 명시

**what_is_new:** 신경 대 무작위 감독 비교를 실제 측정 대 자극으로 예측한 대체 신경 교사의 추가 효용 질문으로 변경했다. 잔차를 순수 정서나 자극과 독립인 뇌 정보로 명명하지 않는다.

**novelty_risk:** 높음: neural-guided learning 선행연구를 추가 역검색해야 한다. 세계 최초·뇌 메커니즘 발견은 주장하지 않는다.

**interpretation_boundary:** 모델 좌표/구조/학습의 비교는 지정 입력·관측 연산자·허용 readout에서의 예측 주장이다. 인간 뇌의 미시 회로·spike timing·가중치 공유·학습 규칙을 식별한 것으로 해석하지 않는다.

**여덟 질문:**

1. Q1 neural-guided 선행은 미완료; 추가 감독과 신경 원천의 효과를 분리하기 어려웠다.

2. Q2 자극→신경 predictor와 guide adapter로 대체 교사 대조를 구성할 수 있다.

3. Q3 neural 대 random의 이득이 뇌 고유 계산이라는 가정을 철회한다.

4. Q4 AI는 같은 adapter에 실제/예측/잔차 교사를 제공해 일반화 비용을 비교한다.

5. Q5 모델이 못 예측한 neural 잔차는 의미 누락·잡음일 수 있으며 고유 정서라고 부르지 않는다.

6. Q6 대체 측정/교사 검증을 신경정보→모델 제약의 역전이에 사용한다.

7. Q7 훈련 신경 자료를 교사로 쓰되 새 사람×새 내용의 독립 평가를 유지한다.

8. Q8 강한 대체 교사를 넘는 이중 효용이 있어야 지정 비교의 신경 감독 가치가 지지된다.

**역검색:** brain guided learning semantic predicted neural targets cross subject generalization

https://github.com/search?q=brain+guided+learning+semantic+predicted+neural+targets+cross+subject+generalization&type=repositories

실제 GitHub 검색 HTTP200, 0건. 학술 전수 검색이 아니며 최초성 근거로 사용하지 않는다.

**10항목 잠정 평가:**

| 항목 | 점수 | 근거 |

|---|---:|---|

| novelty | 3 | neural-guided learning 선행과 중복 위험이 커 잠정 3점이다. |

| neuro_importance | 4 | 신경 측정이 추가 계산 제약을 제공하는지 직접 평가한다. |

| ai_necessity | 3 | 자극→신경 teacher와 adapter가 필요하나 단순 baseline도 유지한다. |

| data_feasibility | 2 | 새 사람×새 내용 및 교사 신뢰도 확보가 실제로 미확인이다. |

| rigor | 4 | cross-fitting·강한 semantic teacher·이중 평가로 순환을 통제한다. |

| falsifiability | 4 | 대체 교사의 충분성 또는 한쪽 지표만 개선되면 주장을 낮춘다. |

| interpretability | 3 | 잔차의 신경고유성은 주장하지 않아도 정보매칭 한계가 남는다. |

| generalization | 4 | 이중 외부 분할과 별도 모델 전이를 핵심 판정으로 둔다. |

| technical_feasibility | 2 | checkpoint/adapter/교사학습 비용과 데이터량은 확인 전이다. |

| exploration_value | 4 | 신경과학→AI 역방향의 실질적 효용을 반증 가능하게 한다. |

평가 공통 불확실성: 실행·스키마·checkpoint·신규성 미확인. 가중합 선정 없음.

**Shortlist:** True — 강한 semantic-predicted neural guide 대조와 이중 외부 검정으로 신경정보의 추가 감독 효용을 반증 가능하게 한다.

**근거:** [P027](https://github.com/facebookresearch/tribev2), [P049](https://arxiv.org/abs/1907.02893), [P050](https://arxiv.org/abs/2606.05107), [P083](https://raw.githubusercontent.com/mlresearch/v119/gh-pages/koh20a/koh20a.pdf), [P100](https://elifesciences.org/articles/82566), [DOC-CIRCUIT](https://github.com/safety-research/circuit-tracer)

## 한계

- 원자료·모델·체크포인트 실행 및 새 원문/Discussion 열람을 수행하지 않았다.

- 영어 질의5개로 GitHub 저장소 역검색을 실제 실행해 HTTP200·0건을 받았지만 긴 결합질의의 제한 때문에 신규성 증거로 사용하지 않는다. 학술 전수 검색은 미완료다.

- P091 e-prop의 최종 연도·저널 서지 보류 및 EmoPathway E0를 유지한다. C11-04의 현재 방법 비교에서 e-prop 학습 규칙 비교는 제외했다.

- 미시 신경 구현은 현재 관측·허용 readout에서 식별되지 않을 수 있다. 상대적 예측/학습효율을 인간 회로·학습규칙 인과로 확장하지 않는다.

- 보유 자료5종은 전제로 유지하며 미확인 스키마는 실행 조건이다. 개념·문헌 작업의 차단 조건이 아니다.

- C11-04는 방법후보로 분리했고 독립 과학 shortlist에는 포함하지 않는다. shortlist는 C11-03과 C11-05 두 개만 잠정 권고한다.

- 자기 round04_revision.json/md만 작성하며 공유 파일·Git은 수정하지 않았다.
