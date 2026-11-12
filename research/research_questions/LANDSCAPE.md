# Research Question Landscape

**60개 원 후보 → 40개 중복 통합 연구 방향 → 30개 구별되는 수정 RQ**. 방법·공통 검증·보류·중복 분기10개는 방향 지도에 보존하고 독립 RQ 수에서 제외했다. 출력 모달리티·적응 단계·생성기 교체만 다른 분기는 기존 질문에 합쳤다. 최종 감사에서 RQ30은 RQ25에 병합하고 RQ22는 방법후보로 옮겼다. 추적을 위해 번호를 재사용하지 않았다. 숫자 자체가 신규성이나 실현성의 검증을 뜻하지 않는다. 모든 질문은 E3이며 실제 신경 분석 결과는 없다.

각 질문은 Round2 원안, 서로 다른 두 역할의 Round3 비판, Round4 응답을 추적할 수 있다. [원본 대응표](candidate_crosswalk.csv), [방향40개](directions.csv), [신규성 역대조](../literature/novelty/README.md).

| RQ | 질문 | 원 방향 | 출발 후보 |
|---|---|---|---|
| [RQ01](#rq01) | 미래 종료를 모르는 사건 진행 상태는 고정 시간창을 넘는가 | D02 | C01-02, C05-04 |
| [RQ02](#rq02) | 평균을 넘는 외부 평정분포는 독립 신경 대비와 연관되는가 | D03 | C01-03 |
| [RQ03](#rq03) | 비정서 anchor 선택으로 정서 의미 대응을 결정할 수 있는가 | D04 | C01-04, C07-04 |
| [RQ04](#rq04) | 개인별 정서 관련 tuning은 공통정보의 가역 좌표 차이로 충분한가? | D05 | C01-05, C04-04, C12-05 |
| [RQ05](#rq05) | 내용 거리와 주석 불확실성을 맞춘 정서 경계의 초과 신경 거리 | D06 | C02-01 |
| [RQ06](#rq06) | 새 정서 대비와 환경에 재사용되는 공동 압축공간의 충분성 | D08 | C02-03, C07-02 |
| [RQ07](#rq07) | 이력 상태는 복수 후속 사건의 정서 신경반응 변화를 예측하는가 | D09 | C02-04, C12-03 |
| [RQ08](#rq08) | 내용조건부 정서 판독 이득은 실제 뇌 패턴을 필요로 하는가? | D10 | C02-05 |
| [RQ09](#rq09) | 시각 정렬 목표가 정서 대비의 판독 접근성을 바꾸는 조건 | D11 | C03-01 |
| [RQ10](#rq10) | 독립 관측이 배제하는 정서 상반 witness 쌍 | D12 | C03-02, C09-02, C09-01, C10-04 |
| [RQ11](#rq11) | 고정 ROI 분할에서 정서 대비의 비가산 판독이 필요한가 | D13 | C03-03, C08-01 |
| [RQ12](#rq12) | 관계 의미의 설명력과 비가산 신경 예측의 중복을 고정 타깃에서 구별 | D15 | C03-05, C10-02 |
| [RQ13](#rq13) | 독립 반복의 신경 문맥이 자극모형 밖 정서 대비 예측을 회수하는가? | D17 | C04-02, C07-05 |
| [RQ14](#rq14) | parcel 평균이 지운 내부 공간 대비는 정서 관련 예측에 필요한가? | D18 | C04-03 |
| [RQ15](#rq15) | 관측격자를 넘어 필요한 이력 함수는 비선형 관측인가 선택적 상태 전이인가? | D19 | C04-05 |
| [RQ16](#rq16) | 공유 병목의 용량을 넘어 남는 모달리티 정보의 예측 충분성 | D20 | C05-01 |
| [RQ17](#rq17) | 인코더와 관측 필터를 구분한 모달리티별 유효 예측창 | D21 | C05-02 |
| [RQ18](#rq18) | 경계 단서와 과거 소거를 분리한 상태 갱신의 필요성 | D22 | C05-03 |
| [RQ19](#rq19) | 감각 불일치 조건의 비가산성: 공통 단위 paired risk 검정 | D23 | C05-05 |
| [RQ20](#rq20) | 과거 제한 상태의 신경 충분성과 미래 지향 학습목표의 추가 역할 | D24 | C06-01 |
| [RQ21](#rq21) | 촬영·사건 metadata 억제에 따른 정서 대비의 선택적 손실 곡선 | D25 | C06-02, C12-02, C06-04 |
| [RQ23](#rq23) | 훈련에서 식별한 공유 관계 연산은 보지 않은 내용–정서 조합으로 전이되는가 | D28 | C06-05, C01-01, C10-05, C12-01 |
| [RQ24](#rq24) | HRF 가정하 정서 문맥 대비의 피질 분포와 시간모형의 식별 경계 | D31 | C08-02 |
| [RQ25](#rq25) | 같은 내용 입력에서 gate·오차 계산 좌표는 정서 대비의 판독 효율을 바꾸는가 | D33 | C08-05, C11-02, C11-01 |
| [RQ26](#rq26) | 정서 예측에 필요한 평균·분산·상관·시간전이의 최소 관측모형 | D34 | C08-04 |
| [RQ27](#rq27) | 사전 허용집합 안에서 검증하는 정서 관련 편집 신경 대비 | D36 | C09-03, C09-05 |
| [RQ28](#rq28) | 언어 병목에서 정서 신경 대비의 예측 접근성이 선택적으로 낮아지는가 | D39 | C10-01 |
| [RQ29](#rq29) | 최근성 가산 설명을 넘어선 사건 순서 관련 신경 예측 | D40 | C10-03 |
| [RQ31](#rq31) | 유한 함수 동등성을 인정한 공유제약의 정서 대비 일반화 효율 | D42 | C11-03 |
| [RQ32](#rq32) | 실제 신경 guide는 의미로 예측한 신경 guide를 넘는 모델 제약인가 | D44 | C11-05 |

<a id="rq01"></a>
## RQ01. 미래 종료를 모르는 사건 진행 상태는 고정 시간창을 넘는가

과거 입력만으로 추정한 사건 진행 상태가 경과초·예상길이·일반 사건 내용을 넘어 정서 관련 신경 대비를 설명하는가?

- **Axis·유형:** B × C × D × F × H × K × M × N × Q × S × T × V × X; Construct / Stimulus; Inference / Measurement; Model / Method; Neural; Structure / Dynamics
- **모델 적용 → 과학 질문 → 가정 도전:** M0 elapsed time/FIR, M1 train 영화에서 예측한 expected-duration 위치, M2 prefix-only semantic landmarks/state, M3 실제 전체 duration을 아는 offline oracle를 만든다. 의미 상태도 이벤트 전체를 인코딩한 교사에 test 미래를 입력하지 않는다. → 사후 시간 정렬의 유용성과 관찰 시점에 계산 가능한 사건 상태의 추가 신경 설명을 구분한다. → 실제 종료로 나눈 0–1 진행률을 온라인 신경 계산의 입력으로 간주한 원안을 철회한다. 사후 oracle만 좋아지면 방법적 정렬 이득으로 낮춘다.
- **경쟁 설명:** M2가 새로운 영화×duration 구간의 독립 정서 대비에서 M0/M1과 일반 사건 상태 기준을 개선하며, actual-end oracle의 이득과 구별된다. / 정규화 위치·경계·HRF·일반 의미 기억이 전부 설명하거나 미래 종료를 아는 M3에서만 효과가 나타난다.
- **관측 대비:** native scanner 시간에서 각 상태 특징을 생성한 뒤 동일 HRF/FIR 관측모형을 적용한다. prefix 상태 대 elapsed/expected-duration/일반 사건 baseline의 정서 대비 오차 차이와 offline oracle 이득을 별도 추정한다.
- **반증:** M3만 개선하면 온라인 사건상태 가설의 증거가 없다. M2가 일반 사건·의미기억 기준을 넘지 못하면 정서 관련 추가 상태 해석을 축소한다. event boundary·주석 lag 선택은 train 내부로 제한한다.
- **기준모형:** elapsed time/FIR / train 예상 duration 위치 / prefix-only 비신경 semantic progress / 일반 사건경계/과거 의미기억 / actual-duration offline oracle / 자기상관·길이·경계 수 보존 null
- **자료·착수 조건:** primary: Emo-FilM: 공식 1Hz consensus와 fMRI는 별도 코호트임을 유지하며 film-relative time과 실제 onset을 연결한다.; secondary: Horikawa는 clip 평균 대비의 외부 기준선; 연속 사건 분석을 자동 가정하지 않는다. Spacetop은 실제 연속 주석/타이밍 확인 때만 추가.; split: leave-film-out 및 duration 층 보류. run별 시작/끝·평정 lag·사건 경계 선택은 train에서만 고정. Spacetop clip 평정을 연속 주석으로 확장하지 않는다.; fallback: 사건 길이 다양성이나 연속 신경신호가 없으면 시간창 관측 민감도 연구로 축소하고 단계 코드 RQ는 보류.; 원시 연속 주석·BOLD·영상 timebase / 독립적으로 정의할 사건 경계와 사건 길이 변이 / 충분한 영화 수와 HRF 불확실성 평가 / prefix 시점에 접근한 frame/token의 감사 / 예상 종료시점 예측의 독립 검증 / 일반 사건 상태와 정서 대비를 분리할 공통 지지
- **근접 연구와 차이:** P042 / P066; Round2의 사후 시간 재매개화를 폐기하지 않고 offline 대조로 분리하며, 입력 시점의 정보 제한을 충족하는 온라인 상태의 충분성으로 질문을 좁혔다. C05-04와 병합한다.
- **중복·신규성 위험:** 사건분절/시간창·TCC와 밀접하다. 사건좌표 하나의 공동 RQ로만 계산하며 단순 시간정렬이면 방법후보다.
- **병합 시 보존한 판정:** 각 원안의 역할 판정은 병합 후에도 보존한다. C01-02: 과학RQ후보; C05-04: 보류
- **원본:** [agents/01_dataset/round04_revision.json](../agents/01_dataset/round04_revision.json); 후보 C01-02, C05-04
- **근거:** [P002 Emo-FilM: A multimodal dataset for affective neuroscience using naturalistic stimuli](https://doi.org/10.1038/s41597-025-04803-5); [P042 Temporal Cycle-Consistency Learning](https://arxiv.org/abs/1904.07846); [P066 Discovering event structure in continuous narrative perception and memory](https://doi.org/10.1016/j.neuron.2017.06.041); [P089 Deep Predictive Coding Networks for Video Prediction and Unsupervised Learning](https://arxiv.org/abs/1605.08104); [P100 Statistical inference on representational geometries](https://doi.org/10.7554/eLife.82566); [P041 Audio-Visual Event Localization in Unconstrained Videos](https://arxiv.org/abs/1803.08842); [P054 Nonlinear ICA Using Auxiliary Variables and Generalized Contrastive Learning](https://proceedings.mlr.press/v89/hyvarinen19a.html); [P053 Challenging Common Assumptions in the Unsupervised Learning of Disentangled Representations](https://proceedings.mlr.press/v97/locatello19a.html)

| 평가 | 점수 | 이유 | 불확실성 |
|---|---|---|---|
| novelty | 3 | 온라인/사후 구분은 중요하지만 사건분절 선행과 중복 가능하다. | 외부 신규성 검색 접근 실패 시 중복 검토 미완료; 기존 문헌 범위의 잠정 점수 |
| neuro_importance | 4 | 정서 관련 시간상태의 계산 가능 정보 범위를 검정한다. | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| ai_necessity | 3 | 의미 진행 모델은 유용하나 고정시간 기준이 핵심이다. | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| data_feasibility | 3 | Emo-FilM의 개념 적합성은 있으나 prefix/주석/실제 타임베이스 미확인이다. | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| rigor | 4 | 미래종료 oracle와 train-only lag를 분리했다. | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| falsifiability | 4 | oracle만 성공하는 반증 결과가 명확하다. | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| interpretability | 4 | 온라인 상태와 사후 좌표의 성공을 혼동하지 않는다. | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| generalization | 4 | 영화×duration 보류가 명시되어 있다. | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| technical_feasibility | 3 | prefix-only 영상표현 추출과 시간정렬 구현 확인이 필요하다. | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| exploration_value | 4 | 사건단계라는 자연스러운 설명의 정보 누수를 드러낸다. | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |

여덟 탐색 질문의 개별 답과 비판 수용/미해결 이력은 위 구조화 원본에 보존했다.

<a id="rq02"></a>
## RQ02. 평균을 넘는 외부 평정분포는 독립 신경 대비와 연관되는가

평정자 척도·지연·표본수를 모형화한 뒤에도 평균으로 소실되는 외부 주석분포 특징이 보류 영화의 신경 대비와 연관되는가?

- **Axis·유형:** A × C × D × F × H × K × O × Q × R × S × T × X; Construct / Stimulus; Inference / Measurement; Model / Method; Neural; Structure / Dynamics
- **모델 적용 → 과학 질문 → 가정 도전:** 개별 평정 identity·ordinal 또는 유계 척도·시점별 유효 N·lag/결측을 계층 관측모형으로 적합한다. 이 모형의 예측 분포와 실제 rater-split 분포가 신경 대비에 주는 증분을 독립 영화에서 비교한다. → 합의 평균이라는 자극 기술이 정서 관련 신경 연관을 설명하기에 충분한지, 측정 혼합을 넘는 분포 특징이 추가되는지 판별한다. → 평균 충분성을 시험하되 외부 사람 사이의 분포를 개인 뇌 내부의 혼합·불확실성·동시 상태로 해석하지 않는다.
- **경쟁 설명:** 척도/lag/유효표본수만의 분포 null과 평균을 넘는 재현 가능한 외부 분포 특징이 독립 신경 대비를 예측한다. / 유계 척도의 평균–분산 결합, 평정자별 지연, 사건 전환·의미 복잡성·결측만으로 분포와 신경 연관이 생긴다.
- **관측 대비:** 평균+측정모형 예측분포 대 평균+측정모형+독립 재현 분포특징의 held-out neural contrast 증분. 평균·분산 일치 고차분포는 표본지지 게이트를 통과한 별도 탐색이다.
- **반증:** 분포가 rater split에서 불안정하면 측정 한계다. 분포는 안정하지만 사전 최소효과보다 신경 증분 CI가 작으면 해당 범위의 평균 충분성을 지지한다. 두 조건이 확인되지 않으면 분포 코드 부재라고 하지 않는다.
- **기준모형:** 평균 정서 벡터 / 평정자 ordinal/scale+lag+결측 모형의 예측분포 / 동일 평균·유효 N·척도·lag 모의 null / motion·사건경계·의미복잡성 / 평균/분산 일치 고차분포 확장
- **자료·착수 조건:** primary: Emo-FilM: 44명 평정과 30명 fMRI가 별도 집단이라는 기존 공식 감사 사실을 유지. 원평정이 현재 보유본에 있는지 확인 후 수행.; secondary: Horikawa 원평정 가용성이 확인되면 같은 측정 질문을 외부 검증. 합의 값만 있으면 사용하지 않는다.; split: 평정자와 영화/자극을 다른 일반화 축으로 둔다. rater별 지연·척도는 개발자료에서만 추정; 시간점과 RDM쌍을 독립 표본으로 세지 않는다.; fallback: 원평정 부재 시 독립 추가 평정 설계만 남기며 분석 가능이라 표시하지 않는다.; 개별 평정 원자료와 문항/척도 정의 / 같은 시점 또는 같은 clip에 충분한 독립 평정자 / 평균이 유사한데 분포가 다른 자극의 공통 지지 / 시점별 실제 유효 평정자 수와 missingness / 평정자별 시간 지연/척도 식별 / 같은 평정자의 동시 다범주 응답은 별도 자료이며 존재를 가정하지 않음
- **근접 연구와 차이:** P002 / P100; 평정분포의 추가 신경 연관은 유지하되 다중해석 코드라는 인과·표현 명명을 철회했다. 원평정 관측모형을 경쟁 설명으로 명시했다.
- **중복·신규성 위험:** 분포적 annotation·측정오차 연구와 가까우며 신경 증분이 없으면 방법후보다. iVAE 식별 정리가 이 평정모형을 보증하지 않는다.
- **병합 시 보존한 판정:** 각 원안의 역할 판정은 병합 후에도 보존한다. C01-03: 과학RQ후보
- **원본:** [agents/01_dataset/round04_revision.json](../agents/01_dataset/round04_revision.json); 후보 C01-03
- **근거:** [P002 Emo-FilM: A multimodal dataset for affective neuroscience using naturalistic stimuli](https://doi.org/10.1038/s41597-025-04803-5); [P051 Similarity of Neural Network Representations Revisited](https://proceedings.mlr.press/v97/kornblith19a.html); [P055 Variational Autoencoders and Nonlinear ICA: A Unifying Framework](https://proceedings.mlr.press/v108/khemakhem20a.html); [P100 Statistical inference on representational geometries](https://doi.org/10.7554/eLife.82566)

| 평가 | 점수 | 이유 | 불확실성 |
|---|---|---|---|
| novelty | 3 | 평균의 불충분성 원리는 알려져 있으나 독립 신경 증분 질문은 남는다. | 외부 신규성 검색 접근 실패 시 중복 검토 미완료; 기존 문헌 범위의 잠정 점수 |
| neuro_importance | 3 | 신경 표현기전보다 주석관련 신경 설명의 범위를 바꾼다. | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| ai_necessity | 2 | 계층 측정모형·단순 encoding으로 검정 가능해 최신 AI가 필수는 아니다. | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| data_feasibility | 2 | 개별 평정·시점별 N·lag를 사용할 수 있는지 미확인이다. | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| rigor | 4 | 측정혼합 null과 영화/평정자 이중 검증을 둔다. | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| falsifiability | 4 | 분포 비신뢰성과 신경 증분 부재를 분리한다. | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| interpretability | 3 | 외부 분포의 신경 연관 이상은 해석할 수 없다. | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| generalization | 3 | 보류 영화 전이는 가능하지만 척도 차이에 취약하다. | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| technical_feasibility | 3 | 원평정이 있으면 통계모형은 작으나 고차분포 support가 제한될 수 있다. | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| exploration_value | 4 | 평균 집계가 잃는 정보를 독립 신경목표에 질문한다. | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |

여덟 탐색 질문의 개별 답과 비판 수용/미해결 이력은 위 구조화 원본에 보존했다.

<a id="rq03"></a>
## RQ03. 비정서 anchor 선택으로 정서 의미 대응을 결정할 수 있는가

고정된 정렬 예산에서 시각·의미 anchor만으로 미사용 정서 신경대비의 대응을 결정할 수 있는가, 아니면 정서 감독을 추가해야 하는가?

- **Axis·유형:** A × C × D × F × K × L × M × O × P × Q × S × T × V × X; Construct / Stimulus; Inference / Measurement; Model / Method; Neural; Structure / Dynamics
- **모델 적용 → 과학 질문 → 가정 도전:** 같은 목적함수의 ε-cost 수송해를 고정 평가함수의 예측동치류로 묶는다. 개발자료에서만 random·coverage·disagreement 기반 비정서 anchor 선택정책을 정하고 별도 참가자/자극의 보류 정서 대비를 평가한다. 정서 anchor는 수·신뢰도·support를 맞춘 별도 감독 대조다. → 공유 감각/의미 관계가 정서 관련 신경대응까지 결정하는 충분한 제약인지 검증한다. → 낮은 정렬비용이나 cycle consistency가 유일한 의미 대응을 보장한다는 가정
- **경쟁 설명:** 잘 선택한 비정서 anchor만으로 개발에 쓰지 않은 정서 대비의 예측범위와 오차가 줄어 정서 anchor 추가이득이 사전 허용폭 이내가 되는 조건이 존재한다. / 정서 anchor만 개선한다 / 모든 anchor효과가 coverage·신뢰도 차이다 / 차이는 최적화 실패다.
- **관측 대비:** 동일 예산의 비정서 random/coverage/적응선택 대 정서감독 대조에서, 정렬에 쓰지 않은 정서 대비의 예측위험과 예측동치류 사이의 범위를 비교한다. ε-cost는 train-only noise calibration과 고정 목적함수로 정한다.
- **반증:** 비정서 anchor가 충분히 support를 덮고 수치수렴이 확인돼도 미사용 정서 대비를 결정하지 못하면 해당 관측범위의 비정서 제약 충분성을 반박한다. 이것만으로 별도 정서코드 존재를 증명하지 않는다. 정책 개선이 coverage 대조로 설명되면 적응설계의 필요성은 기각한다.
- **기준모형:** random non-affective anchors / coverage-matched non-affective anchors / same-budget affective anchors evaluated on other affective contrasts / 예측동등 permutation 대조와 알려진 대칭/비대칭 기하 / 같은 objective 다중 초기값·Procrustes
- **자료·착수 조건:** 보유 Horikawa–Emo-FilM–Spacetop의 관계기하를 각 자료 내부 관측단위에 맞춰 비교. 독립 공통 anchor가 없으면 Horikawa 내부 내용그룹/참가자 분할에서 먼저 실행하고 자료간 의미주장은 제한. NSD는 시각 정합 보정. Mind Captioning은 identifier·ontology 확인 후 노드 추가.; 독립 공통 정서/의미 anchor와 척도 대응 / 최적화 수렴·다중해 탐색은 전체 해집합 포괄이 아님 / 수송 결합 entropy와 해에 대한 불확실성은 다른 양 / test geometry를 사용하는 transductive 평가와 새 자극 일반화 분리 / 선택정책 development와 평가 anchor 완전 분리 / 적응 Bayesian 방법을 쓸 경우 likelihood/prior/조건독립 가정 명시; 충족하지 않으면 fixed disagreement heuristic 사용
- **근접 연구와 차이:** P057 / P052; 단순 anchor수 증가의 감독이득에서 어떤 비정서 측정의 선택이 미사용 정서 대비를 식별하는지로 질문을 바꿨다. 순차 설계 원리를 도입하되 DAD 신경망 구현 자체가 필수라는 주장은 하지 않는다.
- **중복·신규성 위험:** active alignment·experimental design 선행과 중복 가능. 정서 anchor 학습적합도는 기여가 아니며 보류 정서 대비의 독립 전이가 필요하다.
- **병합 시 보존한 판정:** 각 원안의 역할 판정은 병합 후에도 보존한다. C01-04: 방법후보; C07-04: 과학RQ후보
- **원본:** [agents/07_geometry_information/round04_revision.json](../agents/07_geometry_information/round04_revision.json); 후보 C01-04, C07-04
- **근거:** [P001 The neural representation of visually evoked emotion is high-dimensional, categorical, and distributed across transmodal brain regions](https://doi.org/10.1016/j.isci.2020.101060); [P002 Emo-FilM: A multimodal dataset for affective neuroscience using naturalistic stimuli](https://doi.org/10.1038/s41597-025-04803-5); [P057 Gromov-Wasserstein Averaging of Kernel and Distance Matrices](https://proceedings.mlr.press/v48/peyre16.html); [P077 Deep Adaptive Design: Amortizing Sequential Bayesian Experimental Design](https://arxiv.org/abs/2103.02438); [P100 Statistical inference on representational geometries](https://doi.org/10.7554/eLife.82566); [P052 Position: The Platonic Representation Hypothesis](https://proceedings.mlr.press/v235/huh24a.html); [P042 Temporal Cycle-Consistency Learning](https://arxiv.org/abs/1904.07846); [P055 Variational Autoencoders and Nonlinear ICA: A Unifying Framework](https://proceedings.mlr.press/v108/khemakhem20a.html)

| 평가 | 점수 | 이유 | 불확실성 |
|---|---|---|---|
| novelty | 3 | 비정서 anchor 선택의 정서전이는 흥미롭지만 active alignment 선행 역검색이 남는다. | anchor 질·학습/평가 분리·비용 calibration과 전체 해집합 coverage 미확인. |
| neuro_importance | 4 | 공통기하와 정서 의미대응 사이에 필요한 외부제약을 밝힌다. | anchor 질·학습/평가 분리·비용 calibration과 전체 해집합 coverage 미확인. |
| ai_necessity | 3 | 대형 표현과 수송이 유용하나 적응신경망은 작은 정책으로 대체 가능하다. | anchor 질·학습/평가 분리·비용 calibration과 전체 해집합 coverage 미확인. |
| data_feasibility | 3 | 자료내 같은자극 참가자 경로가 가능하나 anchor의 척도·support 확인이 필요하다. | anchor 질·학습/평가 분리·비용 calibration과 전체 해집합 coverage 미확인. |
| rigor | 4 | 예측동치류·고정목적 ε-cost·독립평가를 분리했다. | anchor 질·학습/평가 분리·비용 calibration과 전체 해집합 coverage 미확인. |
| falsifiability | 4 | 비정서 제약 충분성과 선택정책 필요성을 별도로 반박할 수 있다. | anchor 질·학습/평가 분리·비용 calibration과 전체 해집합 coverage 미확인. |
| interpretability | 3 | 유한해 탐색이라 전역 식별집합은 보장하지 못한다. | anchor 질·학습/평가 분리·비용 calibration과 전체 해집합 coverage 미확인. |
| generalization | 4 | 보류자극·대비·참가자 전이를 직접 겨냥한다. | anchor 질·학습/평가 분리·비용 calibration과 전체 해집합 coverage 미확인. |
| technical_feasibility | 2 | 다중수송해와 순차선택 calibration에 계산·자료 부담이 있다. | anchor 질·학습/평가 분리·비용 calibration과 전체 해집합 coverage 미확인. |
| exploration_value | 5 | 정렬 성공의 의미를 뒤집는 측정선택 질문을 제공한다. | anchor 질·학습/평가 분리·비용 calibration과 전체 해집합 coverage 미확인. |

여덟 탐색 질문의 개별 답과 비판 수용/미해결 이력은 위 구조화 원본에 보존했다.

**실제 Round5 반영 조건:** 정서 감독 미사용의 범위를 alignment/selection으로 제한하고 anchor-only/ID/Procrustes 대조를 포함한다. anchor 수와 유효정보 예산을 구별하며 inductive extension과 transductive targetgeometry 접근을 공개한다.

**철회한 강한 해석:** 유한 다중시작의 좁은 예측범위=전역 의미 유일성

평가 점수는 Round4의 역할 판단이다. Round5 조건으로 실제 착수 가능성이 좁아진 경우 현재 점수 자체를 실현성 증명으로 읽지 않는다.

<a id="rq04"></a>
## RQ04. 개인별 정서 관련 tuning은 공통정보의 가역 좌표 차이로 충분한가?

공유 latent의 개인별 가역 관측 map을 허용해도, 새 자극·새 세션의 A 관련 neural tuning 예측에 추가 개인 성분이 필요한가?

- **Axis·유형:** A × D × F × G × K × M × O × Q × S × T × X; Construct / Stimulus; Inference / Measurement; Model / Method; Neural; Structure / Dynamics
- **모델 적용 → 과학 질문 → 가정 도전:** 같은 q차원 공통 latent z에 개인 intercept/gain, 직교 회전, 조건수 제한 invertible affine map을 순차 적용한 모델과 z+개인 성분 모델을 비교한다. 가역군 비교는 같은 q차원 분석공간에서 정의하고 voxel로의 공통/개인 관측 head는 별도 명시한다. TRIBE 평균 피질 출력은 공통 특징 후보이며 새로운 개인 head가 제공된다고 가정하지 않는다. → 개인 적응의 이득이 같은 정보의 관측 좌표 보정인지, 지정한 공통표현과 좌표군에 없는 추가 재현 예측인지 판별한다. → 공유공간 밖의 반복 성분은 모두 새로운 개인 계산이라는 가정과 반대로 모두 잡음이라는 가정을 동시에 제한한다.
- **경쟁 설명:** 허용한 invertible coordinate group과 동일 학습량/유효 rank를 가진 common+private 모델이 A 관련 neural slope를 새 자극·세션에서 추가 예측한다. / 공통 z+개인 affine map이 충분하거나, 효과가 안정된 nuisance·스케일·감각 tuning 또는 shared capacity 부족으로 설명된다.
- **관측 대비:** 정렬 regularization×평균화 유무를 교차하고 같은 adaptation 표본수에서 common+개인 map 대 common+private를 비교한다. 주 결과는 고정 집계 A에 대한 개인별 neural contrast/slope의 외부 세션 예측손실이며 개인 A 상태로 해석하지 않는다. coordinate-only 합성자료 y_s=B_s z와 별도 private 신호 주입자료에서 분석의 거짓 private 판정/검출력을 먼저 평가한다. 전체 함수족에 대한 가역 등가가 아닌 명시된 gain/rotation/affine 군의 충분성만 시험한다.
- **반증:** common+개인 map이 private 모델과 사전 동등성 범위 안이면 해당 좌표군 밖 개인 추가성분 필요성은 반박된다. 추가 성분이 새 자극/세션에서 전이하지 않으면 재현 가설이 약화된다. affine 실패는 임의 비선형 가역 좌표군 실패나 새로운 개인 뇌 계산을 증명하지 않는다.
- **기준모형:** 공유 ridge / 공유+개인 intercept/scale / 공유+개인 residual ridge / 해부·motion·site 공변량 모형 / subject-label permutation과 신뢰도 일치 대조 / 공통 latent+개인 orthogonal map / 공통 latent+조건수 제한 invertible affine map / common+private와 common-only 확장의 파라미터/rank 대조 / coordinate-only/known-private synthetic recovery
- **자료·착수 조건:** ownership: Horikawa, Emo-FilM, Mind Captioning, NSD, Spacetop 보유는 최신 사용자 진술로 확인. 실제 로컬 경로·버전·스키마를 확인한 것은 아니다.; primary: Horikawa 우선. 독립 정서 주석 A, 자극 ID, 신경 Y, 런/반복 구조를 확보한 분석 단위에서 시작한다.; fallback: 자극 단위 beta만 있으면 정적 대비만 수행하고 연속 BOLD 입력을 요구하는 모형에는 넣지 않는다. 주석이나 신뢰도 추정이 없으면 방법 검증으로 범위를 축소한다.; additional: Emo-FilM은 연속 시계열·시간 정렬 확인 뒤 동적 전이; NSD는 정서 주석 확인 전 의미/공간 방법 대조만; Spacetop은 과제별 실제 주석 확인 뒤 일반화; Mind Captioning은 정확한 식별자·버전·주석 사전 확인 전 특정 실험에 배정하지 않는다.; 동일 개인의 독립 세션/반복 / 공통 자극 및 참가자 연결 정보 / 개인 정서 주석의 존재 여부: 없으면 개인 상태 해석 금지 / 정렬 매핑의 training-only 구현 / 새 개인 adaptation에 사용할 학습량 고정
- **근접 연구와 차이:** P027 / P052 / P053; 개인화 성능에서 관측 좌표군의 충분성 검정으로 주질문을 바꿨다. C12-05의 신뢰도 모듈과 통합 가능하지만 본 후보의 고유 하위 조작은 gain/rotation/affine 군 대 추가 성분이다.
- **중복·신규성 위험:** 개인화/공유 반응모형 선행과 가깝고 C12-05와 상위 RQ 중복이다. 좌표군의 범위를 명시한 경쟁 비교가 없으면 별도 RQ로 세지 않는다.
- **병합 시 보존한 판정:** 각 원안의 역할 판정은 병합 후에도 보존한다. C01-05: 과학RQ후보; C04-04: 과학RQ후보; C12-05: 과학RQ후보
- **원본:** [agents/04_brain_foundation/round04_revision.json](../agents/04_brain_foundation/round04_revision.json); 후보 C01-05, C04-04, C12-05
- **근거:** [P001 The neural representation of visually evoked emotion is high-dimensional, categorical, and distributed across transmodal brain regions](https://doi.org/10.1016/j.isci.2020.101060); [P015 MindEye2: Shared-Subject Models Enable fMRI-To-Image With 1 Hour of Data](https://arxiv.org/abs/2403.11207); [P051 Similarity of Neural Network Representations Revisited](https://proceedings.mlr.press/v97/kornblith19a.html); [P060 A Python Toolbox for Representational Similarity Analysis](https://doi.org/10.1101/2025.05.22.655542); [P100 Statistical inference on representational geometries](https://doi.org/10.7554/eLife.82566); [P101 Representational models: A common framework for understanding encoding, pattern-component, and representational-similarity analysis](https://doi.org/10.1371/journal.pcbi.1005508); [P027 A foundation model of vision, audition, and language for in-silico neuroscience](https://arxiv.org/abs/2605.04326); [P052 Position: The Platonic Representation Hypothesis](https://proceedings.mlr.press/v235/huh24a.html); [P053 Challenging Common Assumptions in the Unsupervised Learning of Disentangled Representations](https://proceedings.mlr.press/v97/locatello19a.html); [P086 Scaling laws for language encoding models in fMRI](https://arxiv.org/abs/2305.11863); [P055 Variational Autoencoders and Nonlinear ICA: A Unifying Framework](https://proceedings.mlr.press/v108/khemakhem20a.html); [P096 Predictive Coding Approximates Backprop along Arbitrary Computation Graphs](https://arxiv.org/abs/2006.04182); [P009 Common and stimulus-type-specific brain representations of negative affect](https://doi.org/10.1038/s41593-022-01082-w); [P007 Generalizable representations of pain, cognitive control, and negative emotion in medial frontal cortex](https://doi.org/10.1038/s41593-017-0051-7)

| 평가 | 점수 | 이유 | 불확실성 |
|---|---|---|---|
| novelty | 3 | 개인화 및 C12-05와 중복하나 좌표군 대조로 특화됨 | 외부 영어 역검색 요청은 proxy 403으로 결과 미접근; 최신 선행 배제 불가. |
| neuro_importance | 4 | 개인 적응의 이득이 관측 혼합인지 추가 성분인지 가름 | 독립 A/신경 대비가 실제 검출 가능해야 과학적 중요성이 실현됨. |
| ai_necessity | 2 | 선형/affine 모형만으로 첫 검정 가능함 | 강한 작은 모형이 충분하면 foundation model 필요성 점수를 추가로 낮춰야 함. |
| data_feasibility | 2 | 개인 내 반복·새 세션·공통 자극이 모두 필요함 | 다섯 자료 보유는 확인되었으나 로컬 버전·스키마·반복·주석은 미검증. |
| rigor | 4 | 정렬/평균 분리와 known-coordinate 음성대조를 포함함 | 제안한 통제는 아직 실행하지 않았고 표본수에 따른 검정력은 미확인. |
| falsifiability | 4 | 공통+map 동등성과 private 전이 실패를 구별함 | 동등성 문턱과 신뢰도는 실자료의 개발 표본에서 결과 확인 전 고정해야 함. |
| interpretability | 3 | 허용 가역군 밖의 비선형 설명은 계속 남음 | 관찰 예측 결과는 인간 뇌 인과나 고유 정보량을 확정하지 못함. |
| generalization | 4 | 새 자극·세션·개인별 adaptation 예산을 분리함 | 실제 독립 자극/참가자/세션 수와 사전학습 중복이 미확인. |
| technical_feasibility | 3 | 작은 관측 map 비교는 가능하나 공유 latent 설계 검증 필요 | checkpoint load·GPU/시간·정확한 입력 지원은 아직 실행 검증하지 않음. |
| exploration_value | 4 | 개인 신경 tuning의 해석 범위를 새롭게 제한함 | 새 연결의 유용성은 대조 모형이 관측 후 구별되는지에 달림. |

여덟 탐색 질문의 개별 답과 비판 수용/미해결 이력은 위 구조화 원본에 보존했다.

<a id="rq05"></a>
## RQ05. 내용 거리와 주석 불확실성을 맞춘 정서 경계의 초과 신경 거리

독립 주석으로 정의한 정서 범주 경계를 가로지르는 자극쌍은 같은 내용거리·강도·밀도의 경계 내 쌍 및 pseudo-boundary 쌍보다 더 큰 신경 거리를 갖는가?

- **Axis·유형:** A × B × C × F × K × L × P × Q × S × T × V; Construct / Stimulus; Inference / Measurement; Model / Method; Neural; Structure / Dynamics
- **모델 적용 → 과학 질문 → 가정 도전:** 독립 내용 metric들을 개발 자료에서 고정한 후 matched pair와 nonlinear smooth baseline을 구성하고, 주석자 split으로 정한 경계의 초과거리를 사건 가족 보류로 평가한다. → 범주를 판독할 수 있는 신경표상에서 범주 경계의 추가 분화가 연속 내용거리보다 필요한가? → 분류 가능성, 거리 증가, 곡률을 동일시하지 않는다. 경계 추가효과의 부재는 해당 범위의 연속 설명 충분성을 뜻하며 범주 존재를 반박하지 않는다.
- **경쟁 설명:** 독립 반응 반복이 확보된 설계에서 내용·주석 불확실성을 맞춘 경계쌍의 초과 crossvalidated distance가 비정서 경계와 pseudo-boundary를 넘어 재현된다. 해당 반복이 없는 관측은 이 확증가설을 직접 검정하지 않는다. / 내용 metric의 누락·경로 선택·motion·길이·밀도·주석자의 경계 불확실성이 초과거리를 만든다.
- **관측 대비:** 훈련 fold에서 fit한 smooth content distance가 예측한 신경거리 대비 잔여거리의 평균을 경계쌍과 matched pseudo-boundary쌍 사이에서 차분한다. 비교쌍 매칭과 경계 정의는 test 신경값을 보지 않고 고정하며 공유 자극쌍 의존성은 family 단위 재표집으로 처리한다.
- **반증:** 원뇌의 정서 대비는 신뢰 가능하지만 경계 초과량이 사전정의 최소효과와 동등한 0 범위이면 해당 경계의 추가 분화를 지지하지 않는다. metric·주석 split·내용군에 따라 소실되면 조건 의존 결과로 보고하고 범주 고유기하를 기각한다.
- **기준모형:** valence–arousal 및 category 선형 모형 / 시각·의미 smooth kernel/스플라인 / 주석 경계 무작위화와 동일 밀도 매칭 / 원본/무편집 왕복/목표/동강도 비목표 편집 / 다중 독립 내용 metric과 matched pseudo-boundary / 주석자 split/불확실성 재표집 / 비정서 semantic 경계와 길이·motion 매칭
- **자료·착수 조건:** 현재Horikawa: 같은 자극 개인 내 반복 미확인. 독립 경계·내용매칭·자극가족 지지집합과 held-out 모형차이의 탐색은 가능하나 unbiased crossnobis로 부르지 않음.; 확증조건: 실제 반복/독립 condition estimate를 확인하거나 후속 측정. condition mean/다른 사람 공유패턴은 별도 표적이며 바꾼 계약을 공개.; NSD: 반복을 활용한 시각 방법교정만; 새 인간 정서 주석 전 정서 경계 확증 아님.; 자극별 주석 분포·반복 신뢰도 / 경계 부근 충분한 독립 자극 가족 / 편집 비목표 변화의 독립 검사 / 새 편집 자극 BOLD / 주석자 수준 데이터가 없으면 독립 새 경계주석 필요 / 자극쌍 비독립성·metric 선택의 훈련 fold 격리 / 생성 경로의 의미보존은 사전정의 측정차원에 한정
- **근접 연구와 차이:** P001 / P008; 원안의 모호한 국소 굽음 주장을 철회하고 독립 경계 초과거리라는 제한된 표적을 도입했다. 실제 검증 경로 없이 곡률을 산출하지 않는다.
- **중복·신규성 위험:** categorical geometry 선행과 중복 가능성이 높다. 국소 거리초과의 신규성은 미확정이며 곡률 주장은 제거했다.
- **병합 시 보존한 판정:** 각 원안의 역할 판정은 병합 후에도 보존한다. C02-01: 과학RQ후보
- **원본:** [agents/02_affective_neuroscience/round04_revision.json](../agents/02_affective_neuroscience/round04_revision.json); 후보 C02-01
- **근거:** [P001 The neural representation of visually evoked emotion is high-dimensional, categorical, and distributed across transmodal brain regions](https://doi.org/10.1016/j.isci.2020.101060); [P008 Emotion schemas are embedded in the human visual system](https://doi.org/10.1126/sciadv.aaw4358); [P070 Prompt-to-Prompt Image Editing with Cross-Attention Control](https://arxiv.org/abs/2208.01626); [P077 Deep Adaptive Design: Amortizing Sequential Bayesian Experimental Design](https://arxiv.org/abs/2103.02438); [P100 Statistical inference on representational geometries](https://doi.org/10.7554/eLife.82566)

| 평가 | 점수 | 이유 | 불확실성 |
|---|---|---|---|
| novelty | 3 | 범주 판독과 경계 초과거리의 구분은 유익하나 categorical geometry 선행과 겹칠 수 있다. | E3 잠정 평가; 신규성 역검색 403·분석 스키마·checkpoint 미검증. 일차 표적은 관찰적 거리이다. |
| neuro_importance | 4 | 연속 내용 표상만으로 정서 범주 분화를 설명할 수 있는지 검정한다. | E3 잠정 평가; 신규성 역검색 403·분석 스키마·checkpoint 미검증. 일차 표적은 관찰적 거리이다. |
| ai_necessity | 2 | 새 AI는 강한 내용 baseline에 유용하지만 RSA·matching만으로 핵심검정이 가능하다. | E3 잠정 평가; 신규성 역검색 403·분석 스키마·checkpoint 미검증. 일차 표적은 관찰적 거리이다. |
| data_feasibility | 3 | Horikawa 자연쌍으로 시작할 수 있으나 독립 경계주석·반복·밀도가 미확인이다. | E3 잠정 평가; 신규성 역검색 403·분석 스키마·checkpoint 미검증. 일차 표적은 관찰적 거리이다. |
| rigor | 4 | 경계·metric·선택의 독립성과 family 재표집을 지정했다. | E3 잠정 평가; 신규성 역검색 403·분석 스키마·checkpoint 미검증. 일차 표적은 관찰적 거리이다. |
| falsifiability | 4 | 유효 원뇌 대비가 있으나 경계초과가 동등한 0이면 제한된 가설을 반박한다. | E3 잠정 평가; 신규성 역검색 403·분석 스키마·checkpoint 미검증. 일차 표적은 관찰적 거리이다. |
| interpretability | 3 | 거리 초과는 명확하지만 누락 내용과의 분리는 불완전하다. | E3 잠정 평가; 신규성 역검색 403·분석 스키마·checkpoint 미검증. 일차 표적은 관찰적 거리이다. |
| generalization | 4 | 사건 가족·내용 metric 보류로 전이를 요구한다. | E3 잠정 평가; 신규성 역검색 403·분석 스키마·checkpoint 미검증. 일차 표적은 관찰적 거리이다. |
| technical_feasibility | 3 | 소규모 거리분석은 가능하나 독립 신뢰도 추정과 강한 내용모형이 필요하다. | E3 잠정 평가; 신규성 역검색 403·분석 스키마·checkpoint 미검증. 일차 표적은 관찰적 거리이다. |
| exploration_value | 4 | 범주 대 연속 설명의 좁은 판별점이 있다. | E3 잠정 평가; 신규성 역검색 403·분석 스키마·checkpoint 미검증. 일차 표적은 관찰적 거리이다. |

여덟 탐색 질문의 개별 답과 비판 수용/미해결 이력은 위 구조화 원본에 보존했다.

**실제 Round5 반영 조건:** 현재 확인한 Horikawa 이벤트는 개인별 동일 자극의 독립 반복을 보장하지 않는다. crossnobis 확증은 실제 독립 반응 추정치가 확인된 경로에만 한정한다. 조건 평균·다른 참가자 대비는 별도 추정대상이며 자동 fallback이 아니다.

**철회한 강한 해석:** odd/even TR·voxel·별도 평정자·다른 사람을 개인 내 신경 반복으로 치환

평가 점수는 Round4의 역할 판단이다. Round5 조건으로 실제 착수 가능성이 좁아진 경우 현재 점수 자체를 실현성 증명으로 읽지 않는다.

<a id="rq06"></a>
## RQ06. 새 정서 대비와 환경에 재사용되는 공동 압축공간의 충분성

정서 감독 없이 정한 하나의 압축공간이 선택에 쓰지 않은 다수 정서 관련 신경 대비를 새 내용환경에서도 함께 보존하는가?

- **Axis·유형:** A × B × C × D × F × G × H × J × K × L × M × O × Q × R × S × T × X; Construct / Stimulus; Inference / Measurement; Model / Method; Neural; Structure / Dynamics
- **모델 적용 → 과학 질문 → 가정 도전:** 입력 X와 훈련자극만으로 PCA/고정 random projection/자기지도 압축 Z_d를 정한다. rank 선택은 개발 대비군에서만 하며, 미사용 대비의 readout은 별도 훈련자극에서 새로 적합할 수 있으나 Z_d와 d를 다시 바꾸지 않는다. 최종 평가는 새 대비×새 내용환경에서 한다. → 일부 정서 대비를 예측하는 편의적 투영과 다양한 대비가 공유해 재사용하는 표현공간을 구별한다. → 단일표적 감독 후 rank1 가능성 또는 개별 환경 rank로부터 공통 신경차원의 하한을 추론하는 가정
- **경쟁 설명:** 고정 압축공간에서 개발대비의 평균손실뿐 아니라 미사용 대비의 최악손실도 사전 허용폭 내로 유지되는 rank 구간이 새 환경에서 재현된다. / 낮은 rank는 감독한 표적에만 유효하거나 표적공분산·낮은 신뢰도의 산물이며 새 대비에서 재사용되지 않는다.
- **관측 대비:** 고정한 multi-target risk R_d와 각 대비 정규화 excess loss의 최대값을 개발/미사용 대비 및 보류환경에서 비교한다. ε는 테스트 전 고정하고 full-reference 자체의 성능·CI를 먼저 보고한다. d의 최소값은 명시한 압축/판독군 안의 경험적 값이다.
- **반증:** 개발대비는 보존하지만 새 대비/환경의 최악손실이 허용폭을 넘으면 재사용 충분성 가설 반박. full-reference가 신뢰할 만한 신호를 예측하지 못하면 판정불가. 더 작은 rank 모형의 실패로 모든 표현의 불가능성이나 공통rank 하한을 주장하지 않는다.
- **기준모형:** label-independent PCA/random projection / 동일 target 수·공분산·신뢰도의 synthetic label family / 각 대비 supervised rank1 접근성 대조 / 공동 supervised projection은 별도 보조 결과 / 동일 readout 예산·표본수 학습곡선
- **자료·착수 조건:** 보유 Horikawa에서 정서/시각/의미 대비를 동일 자극으로 비교; NSD는 차원과 신뢰도 보정. Emo-FilM은 영화별 보류에서 상태 대비로 확장. Spacetop은 유효 클립후 평정 단위; Mind Captioning은 실제 paired 주석 확인 후 의미 표적 경로.; 독립 다중 신경대비와 출력공분산·신뢰도 / 입력 X·압축·d선택·readout별 감독원 기록 / 미사용 대비 readout 훈련과 압축선택의 분리 / 내용 overlap와 full-reference 예측 신뢰도
- **근접 연구와 차이:** P038 / P059; 단일표적 최소차원에서 다중 대비에 대한 고정 공간의 재사용성으로 질문이 실질 변경됐다. 최소rank의 절대값을 정서 차원의 수로 해석하지 않는다.
- **중복·신규성 위험:** 다중과제 저rank 학습과 근접; 새 대비×내용환경 전이에 대한 정서 신경 대비라는 범위의 선행 역검색 필요.
- **병합 시 보존한 판정:** 각 원안의 역할 판정은 병합 후에도 보존한다. C02-03: 과학RQ후보; C07-02: 과학RQ후보
- **원본:** [agents/07_geometry_information/round04_revision.json](../agents/07_geometry_information/round04_revision.json); 후보 C02-03, C07-02
- **근거:** [P001 The neural representation of visually evoked emotion is high-dimensional, categorical, and distributed across transmodal brain regions](https://doi.org/10.1016/j.isci.2020.101060); [P007 Generalizable representations of pain, cognitive control, and negative emotion in medial frontal cortex](https://doi.org/10.1038/s41593-017-0051-7); [P071 Null-text Inversion for Editing Real Images using Guided Diffusion Models](https://arxiv.org/abs/2211.09794); [P076 Diffusion Posterior Sampling for General Noisy Inverse Problems](https://github.com/DPS2022/diffusion-posterior-sampling); [P053 Challenging Common Assumptions in the Unsupervised Learning of Disentangled Representations](https://proceedings.mlr.press/v97/locatello19a.html); [P055 Variational Autoencoders and Nonlinear ICA: A Unifying Framework](https://proceedings.mlr.press/v108/khemakhem20a.html); [P051 Similarity of Neural Network Representations Revisited](https://proceedings.mlr.press/v97/kornblith19a.html); [P038 Attention Bottlenecks for Multimodal Fusion](https://arxiv.org/abs/2107.00135); [P059 Scikit-Dimension: A Python Package for Intrinsic Dimension Estimation](https://doi.org/10.3390/e23101368); [P060 A Python Toolbox for Representational Similarity Analysis](https://doi.org/10.1101/2025.05.22.655542); [P026 Scaling Vision Transformers for Functional MRI with Flat Maps](https://arxiv.org/abs/2510.13768); [P098 WILDS: A Benchmark of in-the-Wild Distribution Shifts](https://proceedings.mlr.press/v139/koh21a.html); [P100 Statistical inference on representational geometries](https://doi.org/10.7554/eLife.82566)

| 평가 | 점수 | 이유 | 불확실성 |
|---|---|---|---|
| novelty | 3 | 새 대비×환경에서 공동압축 재사용을 묻지만 다중과제 저rank 선행과 근접하다. | 다중 대비의 표적공분산/신뢰도·지원범위와 최신 선행 미확인; 절대 rank 보장 없음. |
| neuro_importance | 4 | 여러 정서 신경대비가 공유하는 접근가능 표현을 제한할 수 있다. | 다중 대비의 표적공분산/신뢰도·지원범위와 최신 선행 미확인; 절대 rank 보장 없음. |
| ai_necessity | 2 | PCA/random projection으로도 핵심질문이 가능하여 새 AI 필수성은 낮다. | 다중 대비의 표적공분산/신뢰도·지원범위와 최신 선행 미확인; 절대 rank 보장 없음. |
| data_feasibility | 3 | 다중 대비·공분산·신뢰도가 충분한지는 보유자료 스키마에서 확인해야 한다. | 다중 대비의 표적공분산/신뢰도·지원범위와 최신 선행 미확인; 절대 rank 보장 없음. |
| rigor | 4 | scalar 자명성과 감독누수를 제거했으나 과제난이도 완전매칭은 불가능하다. | 다중 대비의 표적공분산/신뢰도·지원범위와 최신 선행 미확인; 절대 rank 보장 없음. |
| falsifiability | 4 | 미사용 대비 최악손실의 허용폭 이탈로 재사용 가설을 반박할 수 있다. | 다중 대비의 표적공분산/신뢰도·지원범위와 최신 선행 미확인; 절대 rank 보장 없음. |
| interpretability | 4 | 실험군 내 충분성으로 한정해 절대 뇌차원 주장을 피한다. | 다중 대비의 표적공분산/신뢰도·지원범위와 최신 선행 미확인; 절대 rank 보장 없음. |
| generalization | 4 | 새 대비와 새 내용환경을 직접 보류한다. | 다중 대비의 표적공분산/신뢰도·지원범위와 최신 선행 미확인; 절대 rank 보장 없음. |
| technical_feasibility | 3 | readout 수와 반복 불확실성 추정 비용이 있으나 단순 압축 fallback이 있다. | 다중 대비의 표적공분산/신뢰도·지원범위와 최신 선행 미확인; 절대 rank 보장 없음. |
| exploration_value | 4 | 성공과 실패 모두 재사용 가능한 정서대비 범위를 알려준다. | 다중 대비의 표적공분산/신뢰도·지원범위와 최신 선행 미확인; 절대 rank 보장 없음. |

여덟 탐색 질문의 개별 답과 비판 수용/미해결 이력은 위 구조화 원본에 보존했다.

<a id="rq07"></a>
## RQ07. 이력 상태는 복수 후속 사건의 정서 신경반응 변화를 예측하는가

각 후속 probe를 이력 조건 사이에서 같게 유지했을 때, 이력에서 얻은 하나의 상태는 보지 않은 후속 사건군의 정서 관련 신경반응 차이까지 예측하며 명시적 이력+HRF 잔류 모형과 구별되는가?

- **Axis·유형:** A × B × C × D × H × J × L × M × N × P × Q × T × V × X; Construct / Stimulus; Inference / Measurement; Model / Method; Neural; Structure / Dynamics
- **모델 적용 → 과학 질문 → 가정 도전:** 정해진 표적·자극분포에서 예측위험 차이의 CI가 사전 허용오차 안에 있는 현재내용/상태 모델을 발견자료로 선정한다. 이는 국소적 위험동등성이다. 과거 전체+HRF 계열을 넣고 별도 자극에서 최소 pairwise 예측차이가 큰 대비를 선택한다. → 현재 내용과 선형 관측 잔류로 충분한가, 아니면 과거 순서에 의존하는 상태가 같은 현재 및 여러 후속 사건의 정서 관련 신경 대비를 추가 설명하는가? → 평균 encoding score 동등성을 계산 동등성으로, 다른 과거의 현재 BOLD 차이를 잠재상태의 직접 증거로 보는 두 가정을 거부한다.
- **경쟁 설명:** 이력 h1/h2×후속 사건 q1/q2 이상의 교차 설계에서 이력 차이에 따른 후속 신경반응의 차이가 사건군에 따라 달라지고, 하나의 prefix-only 상태가 보지 않은 후속 사건의 차이 부호/크기를 예측한다. 단일 probe의 순서 차이는 일차 증거가 아니다. / 이력 잔류, 자극 순서 적응, 일반 의미/사건 계산, 시간 관측해상도만으로 설명되며 정서 특이적 추가 예측은 없다.
- **관측 대비:** 필수 주추정량은 같은 후속 probe에 대한 이력 차이를 probe군 사이에서 다시 비교한 상호작용과 미관측 후속 사건의 반응차이 예측손실이다. 예 Δ=[z(h1,q1)-z(h2,q1)]-[z(h1,q2)-z(h2,q2)]. 상태·readout·정서 신경대비는 개발에서 고정하고 q군 보류를 둔다. 전체 자극 이력의 명시적 HRF/FIR, 감각 적응, 허용한 비선형 관측 대조를 같은 정보·예산에서 비교한다. 과거순서/지연 조작은 이 교차 실험의 설계 요인이다. UC12-02에 있던 기존 확장을 주 검정으로 승격했으며 새 측정 조건을 유지한다.
- **반증:** 복수 후속 사건으로의 상호작용/전이가 충분한 정밀도에서 없거나 명시적 이력·HRF/적응 대조가 같은 대비를 설명하면 하나의 예측 상태가 필요하다는 해당 주장을 지지하지 않는다. 단일 probe 순서효과만 남으면 RQ29 관련 관측으로 낮추고 독립 증거로 세지 않는다. 미시적 뇌 알고리즘 또는 HRF 전역 분리의 증명은 아니다.
- **기준모형:** 현재내용+전체 과거 자극 FIR; 여러 HRF family; bag-of-events; 시간순서/에너지 일치; 일반 의미상태; 적응 모형; prefix-only 입력. 미래 양방향은 별도 진단.
- **자료·착수 조건:** 보유 Emo-FilM은 기존 자연 자료에서 두 모델의 동등성과 자연적 이력 대비를 찾는 경로다. 동일 현재내용/다른 이력의 식별 가능한 대비가 없으면 새로운 통제 영상 제시·신경 측정이 필요한 제안으로 보존한다. Spacetop clip 후 평정을 영상 내 연속 궤적으로 사용하지 않는다. Horikawa는 기존 visual schema 기준과 비교하는 정적 가지로 제한한다.; 충분한 연속 시간축·영화 onset·정서주석 관측 단위의 대응 / 동일 내용/다른 이력 대비의 실제 존재; 없으면 새 측정이 필요한 장기 실험 / prefix-only 입력과 모델 사전학습 시간 방향 확인; action/reward를 수동 관람에 가정하지 않음 / 동일 probe의 과거순서×지연 교차; UC12-02는 후속사건군까지 교차하는 새 자극 실측 조건.
- **근접 연구와 차이:** P008 / P013 / P048; 예측 모델 순위 대신 기존 자료에서 동등한 두 계산 설명을 출발점으로 독립 disagreement 자극의 신경 대비를 검정한다. 관측 등가의 범위와 깨지는 대비를 명시한다.
- **중복·신규성 위험:** Agent02의 이력 질문·Agent06 RQ-FAI1과 매우 가까움. 별도 독립 RQ가 아니라 그 후보의 식별 설계로 합칠 가능성을 Round3에서 검토한다.
- **병합 시 보존한 판정:** 각 원안의 역할 판정은 병합 후에도 보존한다. C02-04: 과학RQ후보; C12-03: 과학RQ후보
- **원본:** [agents/12_adversarial_review/round04_revision.json](../agents/12_adversarial_review/round04_revision.json); 후보 C02-04, C12-03
- **근거:** [P008 Emotion schemas are embedded in the human visual system](https://doi.org/10.1126/sciadv.aaw4358); [P089 Deep Predictive Coding Networks for Video Prediction and Unsupervised Learning](https://arxiv.org/abs/1605.08104); [P090 Brain-Like Object Recognition with High-Performing Shallow Recurrent ANNs](https://arxiv.org/abs/1909.06161); [P077 Deep Adaptive Design: Amortizing Sequential Bayesian Experimental Design](https://arxiv.org/abs/2103.02438); [P100 Statistical inference on representational geometries](https://doi.org/10.7554/eLife.82566); [P013 V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning](https://raw.githubusercontent.com/facebookresearch/vjepa2/main/README.md); [P048 Mastering diverse control tasks through world models](https://arxiv.org/abs/2301.04104); [P053 Challenging Common Assumptions in the Unsupervised Learning of Disentangled Representations](https://proceedings.mlr.press/v97/locatello19a.html)

| 평가 | 점수 | 이유 | 불확실성 |
|---|---|---|---|
| novelty | 3 | 이력 효과 자체는 선행 연구와 겹치지만 HRF를 가르는 사전 불일치 대비는 조건부 차별점이다. | 직접 선행 역검색 미실행 |
| neuro_importance | 5 | 현재내용·관측필터·지속 상태의 경쟁 설명을 직접 가른다. | 일반 사건/적응 설명 남음 |
| ai_necessity | 4 | 잠재 예측 모델은 상태 가설의 다중 경로 예측을 구체화하며 단순 encoding 순위로 대체되지 않는다. | 모델 state 충분성 미확인 |
| data_feasibility | 2 | 보유 영화는 발견 경로로 쓰되 교차 probe·이력·지연의 강한 검증은 새 실측이 필요할 수 있다. | 강한 대비는 새 신경측정 조건 |
| rigor | 4 | 독립 선택/검증과 전체 자극이력 HRF 대조를 명시했다. | HRF family 범위 오지정 위험 |
| falsifiability | 5 | 모형이 서로 다른 부호·크기를 예측하는 대비를 사전 고정할 수 있다. | 실제 대비 정밀도 미확인 |
| interpretability | 3 | 상태 설명이 이겨도 구체 알고리즘과 일반 적응을 완전히 식별하지 못한다. | 상태 구현의 유일성 없음 |
| generalization | 4 | 새 자극·사람과 후속사건군에 동일 상태의 전이를 평가한다. | 후속사건 지지집합 제한 |
| technical_feasibility | 2 | 모델 비교는 가능하지만 자극제작·독립 평정·새 뇌측정 비용이 남는다. | GPU·제작·측정 예산 미확인 |
| exploration_value | 5 | 같은 기존 점수를 내는 설명들을 새로운 과학적 측정으로 구별한다. | C02-04/C06-01와 통합 필요 |

여덟 탐색 질문의 개별 답과 비판 수용/미해결 이력은 위 구조화 원본에 보존했다.

**최종 독립 감사의 범위 제한:** UC12-02의 이력×복수 후속 사건군 상호작용을 확장항목에서 필수 주추정량으로 올린다. 각 후속 probe는 이력 조건 사이에서 동일하게 유지하고 하나의 prefix-only 상태가 보지 않은 후속 사건의 반응 차이까지 예측하는지 검정한다. 단일 현재 반응의 순서 효과만으로는 이 독립 RQ를 지지하지 못한다.

<a id="rq08"></a>
## RQ08. 내용조건부 정서 판독 이득은 실제 뇌 패턴을 필요로 하는가?

새 내용군에서 나타나는 조건부 지역 readout의 정서 대비 이득은 내용으로 라벨을 직접 예측하는 경로를 넘어 실제 신경 패턴에 의존하는가?

- **Axis·유형:** A × E × F × H × I × K × N × O × Q × R × S × T × X; Construct / Stimulus; Inference / Measurement; Model / Method; Neural; Structure / Dynamics
- **모델 적용 → 과학 질문 → 가정 도전:** 고정 가산·유연 additive·content-only·조건부 gate 모델을 같은 예산으로 비교한다. 독립 fold에서 내용/SNR 조건부 교환을 검증하고 실제 뇌를 요구하는 증분을 평가한다. gate 파라미터 대신 예측함수와 permutation-invariant 지역기여를 보고한다. → 분산 정서 정보의 내용조건부 접근성이 존재하는가, 내용 라벨 상관과 가짜 brain 경로로 충분한가? → gate 우위나 임의 gate 교환 손실이 신경 routing 증거라는 주장을 철회한다. 고정 중복성과 조건부 판독은 공존할 수 있으며 생물학적 양자택일이 아니다.
- **경쟁 설명:** 공통 내용·SNR 지지집합의 새 자극에서 조건부 readout이 고정/가산과 content-only를 넘고, 그 추가 이득이 실제 뇌 입력에서만 반복 재현된다. / gate가 내용에서 정서 라벨을 직접 읽거나 내용별 SNR·지원범위 외 교환·비식별 파라미터가 이득을 만든다.
- **관측 대비:** 높을수록 좋은 held-out log score S에 대해 Δ=[S(conditional,real)-S(static,real)]-[S(conditional,conditional-shuffle)-S(static,conditional-shuffle)]를 정의한다. content-only 초과 및 real-vs-shuffle 성능도 별도 요구한다. 교환은 결과 라벨 A를 정확히 맞추지 않고 사전정의 내용 C·SNR strata 내에서 구성한다; A를 조건화하면 표적 brain–A 관계를 보존해 음성대조가 무력해질 수 있다.
- **반증:** 교환 뒤에도 같은 조건부 이득이 남거나 content-only가 동등하면 brain-specific 접근성 주장을 기각한다. 교환손실이 support 밖에서만 생기면 모델 외삽 artifact로 분류한다. 조건부 null calibration 실패는 결과 판정을 보류한다.
- **기준모형:** 고정 가산·nonlinear additive readout / 같은 용량 content-only 모델 / 무작위/균등 gate / ROI voxel 수·SNR 매칭과 참가자별 평가 / content-only 및 조건부 brain 교환 / 동일 지지집합 내 matched 교환과 support 밖 교환 분리 / seed별 예측함수 동등성과 expert permutation-invariant 요약
- **자료·착수 조건:** 우선: Horikawa의 실제 자극별 신경반응·정서 주석·독립 내용 분류로 내용군별 전이를 구성한다.; 검증: Emo-FilM은 영화 가족 단위 검증이 가능한 경우 사용하되 서로 다른 평정 척도를 직접 동일시하지 않는다. NSD는 정서 정답 없는 내용 대조로만 쓸 수 있다.; round4_boundary: 기존 신경자료로 관찰적 readout 검정이 가능하나 label overlap·조건부 교환 지지가 필수다. 실제 신경 개입은 계획 범위에 포함하지 않는다.; 각 내용군 내 정서 대비의 충분한 공통 지지 / ROI 선택 독립성과 반복 신뢰도 / train/test 내용군 정의 사전 고정 / gate 신경 해석과 연결성 주장 분리 / gate 입력 provenance와 결과라벨 직접 사용 금지 / 내용/SNR 조건부 교환의 exchangeability·density overlap 검증 / 교환 null은 train/test fold 안에서 같은 절차로 재학습·평가; 정확한 조건부독립 검정이라 가정하지 않음
- **근접 연구와 차이:** P005 / P009; Round2의 무조건 gate 교환을 핵심근거에서 내리고 조건부 검정의 국소 교환 구조를 수입해 gate의 라벨 우회와 실제 뇌 정보의 필요성을 분리한다.
- **중복·신규성 위험:** 조건부 decoder·mixed selectivity와 중복 가능성이 있다. support 내 교환도 비모수 정확검정이나 생물학적 routing을 보증하지 않는다.
- **병합 시 보존한 판정:** 각 원안의 역할 판정은 병합 후에도 보존한다. C02-05: 과학RQ후보
- **원본:** [agents/02_affective_neuroscience/round04_revision.json](../agents/02_affective_neuroscience/round04_revision.json); 후보 C02-05
- **근거:** [P005 A Sensitive and Specific Neural Signature for Picture-Induced Negative Affect](https://doi.org/10.1371/journal.pbio.1002180); [P009 Common and stimulus-type-specific brain representations of negative affect](https://doi.org/10.1038/s41593-022-01082-w); [P093 Scaling Vision with Sparse Mixture of Experts](https://arxiv.org/abs/2106.05974); [P090 Brain-Like Object Recognition with High-Performing Shallow Recurrent ANNs](https://arxiv.org/abs/1909.06161); [P102 Conditional independence testing based on a nearest-neighbor estimator of conditional mutual information](https://proceedings.mlr.press/v84/runge18a.html); [P053 Challenging Common Assumptions in the Unsupervised Learning of Disentangled Representations](https://proceedings.mlr.press/v97/locatello19a.html)

| 평가 | 점수 | 이유 | 불확실성 |
|---|---|---|---|
| novelty | 3 | 조건부 decoder 자체는 기존이나 label 우회를 통제한 분산 접근성 대비가 남는다. | E3 잠정 평가; 신규성 역검색 403·분석 스키마·checkpoint 미검증. 조건부 교환의 정확성은 미입증이다. |
| neuro_importance | 4 | 분산 정보의 조건부 접근에 실제 신경 패턴이 필요한지 검정한다. | E3 잠정 평가; 신규성 역검색 403·분석 스키마·checkpoint 미검증. 조건부 교환의 정확성은 미입증이다. |
| ai_necessity | 3 | 조건부 모델은 중요하나 단순 mixture regression이 복잡한 MoE를 대체할 수 있다. | E3 잠정 평가; 신규성 역검색 403·분석 스키마·checkpoint 미검증. 조건부 교환의 정확성은 미입증이다. |
| data_feasibility | 3 | 기존 자료로 가능하나 내용과 정서의 공통지지가 미확인이다. | E3 잠정 평가; 신규성 역검색 403·분석 스키마·checkpoint 미검증. 조건부 교환의 정확성은 미입증이다. |
| rigor | 4 | support 내 교환과 content-only·static·additive 및 함수동등성을 검토한다. | E3 잠정 평가; 신규성 역검색 403·분석 스키마·checkpoint 미검증. 조건부 교환의 정확성은 미입증이다. |
| falsifiability | 4 | brain 교환 뒤 이득 유지시 신경 접근성 설명을 기각한다. | E3 잠정 평가; 신규성 역검색 403·분석 스키마·checkpoint 미검증. 조건부 교환의 정확성은 미입증이다. |
| interpretability | 3 | 예측 차분은 명확하지만 실제 routing과 동일시할 수 없다. | E3 잠정 평가; 신규성 역검색 403·분석 스키마·checkpoint 미검증. 조건부 교환의 정확성은 미입증이다. |
| generalization | 4 | 새 내용군·참가자 반복에서 brain-specific 증분을 요구한다. | E3 잠정 평가; 신규성 역검색 403·분석 스키마·checkpoint 미검증. 조건부 교환의 정확성은 미입증이다. |
| technical_feasibility | 3 | 고차원 조건부 교환 추정과 calibration이 어려워 단순화가 필요하다. | E3 잠정 평가; 신규성 역검색 403·분석 스키마·checkpoint 미검증. 조건부 교환의 정확성은 미입증이다. |
| exploration_value | 4 | 조건부 모델의 성공이 무엇을 이용했는지 새로운 반론을 만든다. | E3 잠정 평가; 신규성 역검색 403·분석 스키마·checkpoint 미검증. 조건부 교환의 정확성은 미입증이다. |

여덟 탐색 질문의 개별 답과 비판 수용/미해결 이력은 위 구조화 원본에 보존했다.

<a id="rq09"></a>
## RQ09. 시각 정렬 목표가 정서 대비의 판독 접근성을 바꾸는 조건

동일 자료·입력·용량에서 정렬 목표를 바꾸면 내용군을 넘어 일반화하는 정서 대비의 접근성이 probe 함수계열과 학습량에 따라 어떻게 달라지는가?

- **Axis·유형:** A × B × C × F × G × I × J × K × O × P × Q × S × X; Construct / Stimulus; Inference / Measurement; Model / Method; Neural; Structure / Dynamics
- **모델 적용 → 과학 질문 → 가정 도전:** 동일 자료·입력의 masked/contrastive 목표와 원뇌/trunk/head × probe family × 훈련량을 비교한다. 가역 혼합·비가역 절단 대조로 측정 실패를 확인한다. → 독립 정서 대비를 읽는 표현·표본 복잡도가 시각 정렬과 내용환경에 따라 달라지는가? → 검색 성공과 probe 실패만으로 정보 충분성 또는 불가역 삭제를 판정할 수 있다는 가정.
- **경쟁 설명:** 원뇌에서 신뢰 가능한 대비가 있을 때 정렬 목표에 따른 접근성 차이가 사전 정의 probe·학습량 범위와 내용군 보류에서 재현된다. / 가역 재부호화·SNR·훈련량·관계 의미 누락·작은 시각 단서 차이이다.
- **관측 대비:** 동일 외부 정서 타깃의 단계별 보류 로그점수 차이를 probe·학습량별 보고한다. 총 예측과 사건·관계 조건부 증분을 병기하고 정서/내용 대비 난도와 검색 정확도도 따로 기록한다.
- **반증:** 비선형 probe나 자료량 증가로 차이가 회복되면 삭제 해석을 기각한다. 충분한 정밀도의 무차이는 시험 범위의 목표 효과를 낮춘다. 원뇌 신호 미확인은 식별불가이다.
- **기준모형:** 원 뇌의 정규화 선형 readout / 동일 차원의 무작위 projection / ridge→CLIP / 시각·의미만으로 정서 주석 예측 / 동일 architecture의 masked/contrastive 비교 / 가역 혼합/비가역 절단 / 관계·사건 및 난도 일치 내용 대비
- **자료·착수 조건:** possession: Horikawa·Emo-FilM·Mind Captioning·NSD·Spacetop 다섯 보유본을 전제로 진행; primary: Horikawa의 자극 단위 주석과 뇌 반응으로 총/조건부 추정량 정의; validation: Emo-FilM 및 Spacetop은 각 측정 단위별 독립 재검증; 공통 척도를 가정하지 않음; controls: NSD는 시각 정렬/신뢰도 대조; Mind Captioning은 정확한 식별과 제공 주석 확인 뒤 의미 통제 후보; fallback: 학습 checkpoint를 못 쓰면 고정 시각 특징+작은 ridge와 원 뇌 readout으로 보존 경계부터 검증; 원영상 내용군·dupidx와 처리 Label 대응 / 정서 주석 단위와 reliability 추정 가능 자료 / 독립 fold 안 전처리·조건화·차원 선택 / 각 보유본 voxel adapter와 split 정의 / 실행 전 확인: 동일 훈련조건·반복 대응과 신규성 역검색 미완료.
- **근접 연구와 차이:** P001 / P015 / P022; UC03-01은 정보 삭제 질문을 알려진 가역 대조에 비춘 접근성 곡선으로 바꾼다. C10-01과 상위 보존 질문을 공유하고 모달 교체는 신규성으로 세지 않는다.
- **중복·신규성 위험:** 기존 transfer·probe 감사의 재평가일 수 있어 목적함수×내용 대비 효과가 없으면 방법후보로 축소.
- **병합 시 보존한 판정:** 각 원안의 역할 판정은 병합 후에도 보존한다. C03-01: 과학RQ후보
- **원본:** [agents/03_vision_decoding/round04_revision.json](../agents/03_vision_decoding/round04_revision.json); 후보 C03-01
- **근거:** [P001 The neural representation of visually evoked emotion is high-dimensional, categorical, and distributed across transmodal brain regions](https://doi.org/10.1016/j.isci.2020.101060); [P008 Emotion schemas are embedded in the human visual system](https://doi.org/10.1126/sciadv.aaw4358); [P015 MindEye2: Shared-Subject Models Enable fMRI-To-Image With 1 Hour of Data](https://arxiv.org/abs/2403.11207); [P022 Seeing Beyond the Brain: Masked Modeling Conditioned Diffusion Model for Human Vision Decoding](https://github.com/zjc062/mind-vis); [P051 Similarity of Neural Network Representations Revisited](https://proceedings.mlr.press/v97/kornblith19a.html); [P100 Statistical inference on representational geometries](https://doi.org/10.7554/eLife.82566)

| 평가 | 점수 | 이유 | 불확실성 |
|---|---|---|---|
| novelty | 3 | 정렬 목표와 접근성 곡선의 교차가 기여지만 transfer 감사와 가깝다. | 분석 미실행; 동일 훈련조건·반복 대응과 신규성 역검색 미완료. |
| neuro_importance | 3 | 관심 대비 보존 조건을 제한하나 인간 압축 기전은 아니다. | 분석 미실행; 동일 훈련조건·반복 대응과 신규성 역검색 미완료. |
| ai_necessity | 3 | 정렬 표현은 필요하지만 작은 readout으로 시작한다. | 분석 미실행; 동일 훈련조건·반복 대응과 신규성 역검색 미완료. |
| data_feasibility | 3 | 동일 시행 latent·반복·내용군 대응이 실행 조건이다. | 분석 미실행; 동일 훈련조건·반복 대응과 신규성 역검색 미완료. |
| rigor | 4 | 가역 대조와 probe·학습량 교차가 재부호화를 시험한다. | 분석 미실행; 동일 훈련조건·반복 대응과 신규성 역검색 미완료. |
| falsifiability | 4 | probe 강화로 차이가 회복되면 삭제 해석이 실패한다. | 분석 미실행; 동일 훈련조건·반복 대응과 신규성 역검색 미완료. |
| interpretability | 4 | 외부 대비 점수로 한정해 정보론적 과장을 줄인다. | 분석 미실행; 동일 훈련조건·반복 대응과 신규성 역검색 미완료. |
| generalization | 3 | 자극가족·참가자를 보류하되 데이터 간 척도 등가는 없다. | 분석 미실행; 동일 훈련조건·반복 대응과 신규성 역검색 미완료. |
| technical_feasibility | 3 | 작은 모형부터 가능하나 동일 훈련조건 구성에 비용이 든다. | 분석 미실행; 동일 훈련조건·반복 대응과 신규성 역검색 미완료. |
| exploration_value | 4 | 관심 정보 보존 평가의 취약점을 반증 가능한 형태로 바꾼다. | 분석 미실행; 동일 훈련조건·반복 대응과 신규성 역검색 미완료. |

여덟 탐색 질문의 개별 답과 비판 수용/미해결 이력은 위 구조화 원본에 보존했다.

**실제 Round5 반영 조건:** 같은 작은 뇌 encoder·같은 입력/시각표적에서 contrastive와 회귀 손실을 비교할 때만 목표함수 효과를 검정한다. cache/ridge는 접근성 기준이다. 유한 probe 실패를 비가역 정보소실로 해석하지 않는다.

**철회한 강한 해석:** 비가역 정보소실의 증명, 다른 backbone 순위에 의한 목표효과

평가 점수는 Round4의 역할 판단이다. Round5 조건으로 실제 착수 가능성이 좁아진 경우 현재 점수 자체를 실현성 증명으로 읽지 않는다.

<a id="rq10"></a>
## RQ10. 독립 관측이 배제하는 정서 상반 witness 쌍

원 관측 일부와 양립하면서 독립 정서 주석이 다른 두 자극 witness를 찾았을 때 추가 독립 반복은 그 모호성을 얼마나 배제하는가?

- **Axis·유형:** A × B × C × F × G × H × I × K × L × M × O × P × Q × R × S × T × X; Construct / Stimulus; Inference / Measurement; Model / Method; Neural; Structure / Dynamics
- **모델 적용 → 과학 질문 → 가정 도전:** 유한 생성 탐색은 반대 주석의 witness 쌍을 제안하는 도구로만 사용하고, 원 관측 중 보류한 반복과 별도 forward family로 적합도를 검증한다. → 정서에 관한 상반 설명을 배제하는 정보가 기존 신경 관측의 어떤 추가 반복/사전지정 공간에서 제공되는지 묻는다. → 좁은 sampler 범위를 신경 식별성의 증거로 해석하는 가정을 폐기하고 존재 witness와 미발견을 비대칭적으로 취급한다.
- **경쟁 설명:** 일부 모델조건부 witness 쌍은 독립 반복의 정서 contrast 관측이 추가될 때 사전정의 오차 허용범위에서 한쪽이 탈락한다. / witness는 encoder 외삽 취약점이며 어떤 독립 forward에서든 탈락하거나, 관측 증가에도 충분한 신뢰도에서 둘 모두 남는다.
- **관측 대비:** 첫 관측 집합으로 고정한 두 후보가 held-out 반복 및 사전정의 contrast에서 허용오차를 통과하는지 평가한다. 추가 관측 전후 기존 witness 배제율·후보별 예측오차를 보고한다. 생성 후보 정서 차이는 별도 인간 주석으로 측정한다.
- **반증:** 원 관측에서만 통과하고 독립 평가 forward/반복에서는 처음부터 실패하면 모델조건부 모호성의 외적 타당성이 약화된다. 추가 반복이 witness를 배제하지 못하면 그 관측량의 구별 이득은 지지되지 않는다. witness 미발견은 비식별성 부재의 반증이 아니다.
- **기준모형:** 자연 matched witness / 작은 알려진 합성 식별/비식별 문제의 탐색 검출력 / 같은 budget의 다중 초기값 / 감각 contrast가 다른 witness 대 정서주석 차이 witness / 독립 반복 증가 대 단순 동일자료 재사용
- **자료·착수 조건:** Horikawa 등 실제 반복이 있는 보유본에서 원 관측 일부/독립 보류 반복으로 검사한다. 반복 부족이면 추가 반복 측정 조건으로 보존한다. 후보의 실제 뇌반응 동일성은 이 검정으로 말할 수 없으며 두 새 후보를 직접 제시·측정해야 별도 평가할 수 있다.; 독립 반복과 train-only 신뢰도 mask / 별도 forward family 및 contrast별 오차 calibration / 후보 독립 인간 정서·의미 주석 / 사전고정 witness 최소 주석차이·적합오차 / 추가 ROI 관측은 잡음 의존성 반영; ROI 분할만으로 독립이라 부르지 않음
- **근접 연구와 차이:** P076 / P053 / P057; prior 기여율과 별도로 관측이 허용하는 정서 대비 범위 자체를 추정하여 실패한 reconstruction을 측정 설계의 문제로 재정의.
- **중복·신규성 위험:** 기존 inverse problem uncertainty와 중복 가능. 엄밀한 식별 집합의 증명이 아닌 경험적 범위를 이론적 bound로 포장하지 않음.
- **병합 시 보존한 판정:** 각 원안의 역할 판정은 병합 후에도 보존한다. C03-02: 과학RQ후보; C09-02: 과학RQ후보; C09-01: 방법후보; C10-04: 방법후보
- **원본:** [agents/09_generative_ai/round04_revision.json](../agents/09_generative_ai/round04_revision.json); 후보 C03-02, C09-02, C09-01, C10-04
- **근거:** [P015 MindEye2: Shared-Subject Models Enable fMRI-To-Image With 1 Hour of Data](https://arxiv.org/abs/2403.11207); [P019 High-resolution image reconstruction with latent diffusion models from human brain activity](https://doi.org/10.1101/2022.11.18.517004); [P076 Diffusion Posterior Sampling for General Noisy Inverse Problems](https://github.com/DPS2022/diffusion-posterior-sampling); [P008 Emotion schemas are embedded in the human visual system](https://doi.org/10.1126/sciadv.aaw4358); [P097 On over-fitting in model selection and subsequent selection bias in performance evaluation](https://jmlr.org/papers/v11/cawley10a.html); [P100 Statistical inference on representational geometries](https://doi.org/10.7554/eLife.82566); [P053 Challenging Common Assumptions in the Unsupervised Learning of Disentangled Representations](https://proceedings.mlr.press/v97/locatello19a.html); [P055 Variational Autoencoders and Nonlinear ICA: A Unifying Framework](https://proceedings.mlr.press/v108/khemakhem20a.html); [P057 Gromov-Wasserstein Averaging of Kernel and Distance Matrices](https://proceedings.mlr.press/v48/peyre16.html); [P071 Null-text Inversion for Editing Real Images using Guided Diffusion Models](https://arxiv.org/abs/2211.09794); [P021 Brain-Diffuser: Natural scene reconstruction from fMRI signals using generative latent diffusion](https://arxiv.org/abs/2303.05334); [P087 Semantic reconstruction of continuous language from non-invasive brain recordings](https://doi.org/10.1038/s41593-023-01304-9)

| 평가 | 점수 | 이유 | 불확실성 |
|---|---|---|---|
| novelty | 3 | witness 배제 추정량은 기존 inverse uncertainty와 가까워 선행 역검색이 필요하다. | E3 사전 평가. 최신 선행 역검색·실제 schema·checkpoint·효과크기·비용 미확인; 점수 합산으로 선정하지 않음. |
| neuro_importance | 4 | 추가 관측이 정서 관련 상반 설명을 구별하는지 묻는다. | E3 사전 평가. 최신 선행 역검색·실제 schema·checkpoint·효과크기·비용 미확인; 점수 합산으로 선정하지 않음. |
| ai_necessity | 3 | 생성 탐색은 자연 pool에 없는 witness를 제안할 수 있으나 필수성은 미확인이다. | E3 사전 평가. 최신 선행 역검색·실제 schema·checkpoint·효과크기·비용 미확인; 점수 합산으로 선정하지 않음. |
| data_feasibility | 3 | 독립 반복이 있으면 기존 자료로 모델조건부 검증 가능하다. | E3 사전 평가. 최신 선행 역검색·실제 schema·checkpoint·효과크기·비용 미확인; 점수 합산으로 선정하지 않음. |
| rigor | 4 | 유한탐색의 내부근사와 독립 평가를 명시했다. | E3 사전 평가. 최신 선행 역검색·실제 schema·checkpoint·효과크기·비용 미확인; 점수 합산으로 선정하지 않음. |
| falsifiability | 4 | 고정 witness의 생존/탈락은 판정 가능하고 미발견은 불확정으로 남긴다. | E3 사전 평가. 최신 선행 역검색·실제 schema·checkpoint·효과크기·비용 미확인; 점수 합산으로 선정하지 않음. |
| interpretability | 4 | 실제 뇌 동등성 대신 모델조건부 모호성으로 제한했다. | E3 사전 평가. 최신 선행 역검색·실제 schema·checkpoint·효과크기·비용 미확인; 점수 합산으로 선정하지 않음. |
| generalization | 2 | 추가 관측 효과가 다른 encoding family에도 유지될지는 미확인이다. | E3 사전 평가. 최신 선행 역검색·실제 schema·checkpoint·효과크기·비용 미확인; 점수 합산으로 선정하지 않음. |
| technical_feasibility | 2 | differentiable forward·proposal·주석 비용이 크다. | E3 사전 평가. 최신 선행 역검색·실제 schema·checkpoint·효과크기·비용 미확인; 점수 합산으로 선정하지 않음. |
| exploration_value | 4 | 탐색 실패와 신경 식별성을 혼동하는 관행을 바꿀 수 있다. | E3 사전 평가. 최신 선행 역검색·실제 schema·checkpoint·효과크기·비용 미확인; 점수 합산으로 선정하지 않음. |

여덟 탐색 질문의 개별 답과 비판 수용/미해결 이력은 위 구조화 원본에 보존했다.

**실제 Round5 반영 조건:** 유한 자연 후보부터 참조 유지/하나 배제/둘다 배제/참조 배제를 분리한다. 개인 내 반복과 정서 주석을 함께 확보한 경로가 필요해 첫3파일럿에서는 제외하고 Discovery 카드로 유지한다.

**철회한 강한 해석:** witness 미발견=유일성, 생성 후보의 forward 적합=실제 동일 뇌반응

평가 점수는 Round4의 역할 판단이다. Round5 조건으로 실제 착수 가능성이 좁아진 경우 현재 점수 자체를 실현성 증명으로 읽지 않는다.

<a id="rq11"></a>
## RQ11. 고정 ROI 분할에서 정서 대비의 비가산 판독이 필요한가

사전고정 ROI 분할에서 독립 정서 주석의 판독위험은 강한 비선형 가산함수로 충분한가, 비가산 readout이 추가 위험을 줄이는가?

- **Axis·유형:** A × E × F × G × H × I × K × L × P × Q × R × T × V × X; Construct / Stimulus; Inference / Measurement; Model / Method; Neural; Structure / Dynamics
- **모델 적용 → 과학 질문 → 가정 도전:** ROI 내부 nonlinear additive spline/동일용량 head와 비가산 head를 같은 fold에서 비교한다. C03-03의 자연 후보 판별 assay와 direct A readout을 병합 RQ 안에서 따로 평가한다. → 정보가 ROI별로 분산된 것과 그 정보를 읽는 데 비가산 함수가 필요한 것을 구분한다. → 비가산 판독의 이득을 정보이론적 시너지 또는 뇌 영역 간 통신으로 해석하는 가정을 제한한다.
- **경쟁 설명:** 내용 공통지지·ROI 신뢰도·유효용량을 맞춘 상태에서 고정 ROI 분할의 비가산 head가 독립 주석 위험을 줄인다. / 비선형 공통자극·관측잡음 상관·정규화 차이 또는 ROI 좌표 선택이 이득을 만든다.
- **관측 대비:** 전체 사전지정 자극분포에서 ΔR=R(additive)−R(nonadditive)를 주추정량으로 보고한다. 모형 불일치로 선별한 자극집합의 ΔR은 다른 조건부 estimand로 분리한다. 후보 판별 log score는 별도 assay이며 두 점수를 합하지 않는다.
- **반증:** 강한 가산계가 사전 동등성 범위에서 충분하면 지정 ROI·표적·함수계열에서 비가산 판독 필요성이 작다. 통신 없는 공통입력 모의계에서도 같은 이득이 나면 통신 해석은 기각하되 실제 자료의 비가산 판독 관찰은 남는다.
- **기준모형:** nonlinear additive spline / 강한 stimulus-only 모형 / 비선형 공통입력·상호작용 생성계의 양성/음성 회복 / ROI 내부 가역 좌표변환과 블록 간 혼합의 분리 / 같은 객체/다른 A 및 같은 A/다른 객체 자연 후보
- **자료·착수 조건:** primary: Horikawa 보유본의 시행 반응·정서 주석 생성단위·자극 ID를 먼저 확인하여 정적 L/D/N 비교; extension: Emo-FilM 연속 BOLD가 확인될 때 시간 결합으로 확장; other_owned: NSD는 자극·공간 통제와 정서 주석이 존재할 경우에만 대비; Spacetop 및 Mind Captioning은 스키마 확인 후 별도 외적 검증; 독립 자극 수와 반복 신뢰도 / 주석이 자극 집계인지 개인별인지 / 공간 범위·ROI 신호 품질 / checkpoint가 필요하지 않은 ridge/bilinear fallback 가능; pretrained 활용 시 입력 및 학습중복 확인
- **근접 연구와 차이:** P005 / P009 / P017 / P067; C03-03과 동일 상위 RQ의 direct readout assay다. 상위 질문의 두 assay를 독립 신경 발견 두 건으로 세지 않는다.
- **중복·신규성 위험:** 분산 정서 디코딩 및 multi-ROI 결합의 근접 선행이 강하다. C03-03과 병합해 중복 계수를 피하며 실제 역검색은 외부 403으로 미완료.
- **병합 시 보존한 판정:** 각 원안의 역할 판정은 병합 후에도 보존한다. C03-03: 과학RQ후보; C08-01: 과학RQ후보
- **원본:** [agents/08_systems_neuroscience/round04_revision.json](../agents/08_systems_neuroscience/round04_revision.json); 후보 C03-03, C08-01
- **근거:** [P005 A Sensitive and Specific Neural Signature for Picture-Induced Negative Affect](https://doi.org/10.1371/journal.pbio.1002180); [P009 Common and stimulus-type-specific brain representations of negative affect](https://doi.org/10.1038/s41593-022-01082-w); [P017 Brain-IT: Image Reconstruction from fMRI via Brain-Interaction Transformer](https://arxiv.org/abs/2510.25976); [P076 Diffusion Posterior Sampling for General Noisy Inverse Problems](https://github.com/DPS2022/diffusion-posterior-sampling); [P028 Brain-Mamba: Encoding Brain Activity via Selective State Space Models](https://proceedings.mlr.press/v248/behrouz24a.html); [P051 Similarity of Neural Network Representations Revisited](https://proceedings.mlr.press/v97/kornblith19a.html); [P053 Challenging Common Assumptions in the Unsupervised Learning of Disentangled Representations](https://proceedings.mlr.press/v97/locatello19a.html); [P067 Brain network dynamics are hierarchically organized in time](https://github.com/OHBA-analysis/HMM-MAR)

| 평가 | 점수 | 이유 | 불확실성 |
|---|---|---|---|
| novelty | 3 | 분산 코드 선행과 C03-03에 가깝지만 가산의 필요성을 명시적으로 제한한다. | 실험 미실행·보유본 스키마 및 가까운 신규문헌 전수검색 미완료를 반영한 잠정 판단 |
| neuro_importance | 4 | 분산 신경정보에 필요한 판독 함수의 범위를 규정한다. | 실험 미실행·보유본 스키마 및 가까운 신규문헌 전수검색 미완료를 반영한 잠정 판단 |
| ai_necessity | 2 | 작은 spline/bilinear baseline으로 일차 질문을 시험할 수 있다. | 실험 미실행·보유본 스키마 및 가까운 신규문헌 전수검색 미완료를 반영한 잠정 판단 |
| data_feasibility | 3 | Horikawa 시행자료가 후보이나 ROI·내용 공통지지·반복 스키마는 미확인이다. | 실험 미실행·보유본 스키마 및 가까운 신규문헌 전수검색 미완료를 반영한 잠정 판단 |
| rigor | 4 | 내용 그룹·신뢰도·블록변환·공통입력 null을 함께 비교한다. | 실험 미실행·보유본 스키마 및 가까운 신규문헌 전수검색 미완료를 반영한 잠정 판단 |
| falsifiability | 4 | 동등성 검정과 known-truth null에서 가산 필요성을 반박할 수 있다. | 실험 미실행·보유본 스키마 및 가까운 신규문헌 전수검색 미완료를 반영한 잠정 판단 |
| interpretability | 4 | 통신 대신 ROI 분할하 predictive risk로 해석을 제한한다. | 실험 미실행·보유본 스키마 및 가까운 신규문헌 전수검색 미완료를 반영한 잠정 판단 |
| generalization | 3 | 새 내용·참가자 전이는 가능하나 공통지지가 실행조건이다. | 실험 미실행·보유본 스키마 및 가까운 신규문헌 전수검색 미완료를 반영한 잠정 판단 |
| technical_feasibility | 4 | checkpoint 없이 작은 head로 구현할 수 있다. | 실험 미실행·보유본 스키마 및 가까운 신규문헌 전수검색 미완료를 반영한 잠정 판단 |
| exploration_value | 4 | 두 assay 불일치가 표상 또는 측정 편향을 드러낼 수 있다. | 실험 미실행·보유본 스키마 및 가까운 신규문헌 전수검색 미완료를 반영한 잠정 판단 |

여덟 탐색 질문의 개별 답과 비판 수용/미해결 이력은 위 구조화 원본에 보존했다.

<a id="rq12"></a>
## RQ12. 관계 의미의 설명력과 비가산 신경 예측의 중복을 고정 타깃에서 구별

고정된 독립 정서 주석에 대해 관계 설명이 추가될 때 영역 간 비가산 예측 이득의 변화는 일반 의미 설명력 증가와 구별되는가?

- **Axis·유형:** A × B × C × E × F × H × L × P × Q × R × T × V × X; Construct / Stimulus; Inference / Measurement; Model / Method; Neural; Structure / Dynamics
- **모델 적용 → 과학 질문 → 가정 도전:** 독립 중립 관계 설명; 길이·예측력 일치 비관계 설명; 정서결론 포함 민감도 조건; 유연한 영역 내 가산 모형; 공통입력×HRF 합성 null; cross-fitting을 사용해 조건 S마다 동일 원타깃 A에 대해 L(S), L(S+D), L(S+N)을 같은 외부 표본에서 측정한다. g(S)=L(S+D)-L(S+N). 주 비교는 [g(O)-g(O+R)]와 예측력 일치 비관계 대조의 감소 차이이며, 모든 총손실·증분도 병기한다. 관계·정서 불일치의 공통 지지 층을 따로 평가한다. → 고정된 독립 정서 주석에 대해 관계 설명이 추가될 때 영역 간 비가산 예측 이득의 변화는 일반 의미 설명력 증가와 구별되는가? → 고정 타깃·관측 support·독립 주석에서 경쟁 설명을 구별한다. 추정량이 바뀐다는 지적을 수용해 고정 원타깃의 nested predictor 대비로 실질 수정한다.
- **경쟁 설명:** 객체 의미 O에서 관계 의미 R로 확장할 때 N-D 이득이 감소하며, 그 감소는 타깃 예측력을 맞춘 비관계 정보 추가보다 크다. / 어떤 타깃 예측력 높은 설명도 동일 감소를 만들거나 관계 추가 후에도 N-D가 유지된다. 감소는 공유정보 대체이며 가짜 신경 효과의 증거가 아니다.
- **관측 대비:** 조건 S마다 동일 원타깃 A에 대해 L(S), L(S+D), L(S+N)을 같은 외부 표본에서 측정한다. g(S)=L(S+D)-L(S+N). 주 비교는 [g(O)-g(O+R)]와 예측력 일치 비관계 대조의 감소 차이이며, 모든 총손실·증분도 병기한다. 관계·정서 불일치의 공통 지지 층을 따로 평가한다.
- **반증:** 예측력 일치 비관계 설명도 동일 감소를 만들면 관계 특이 가설 약화. 원래 g(O)가 없으면 감소 가설을 식별할 기준점이 없다. 관계 후 g가 남아도 조건부 비가산 필요성만 시사한다.
- **기준모형:** 독립 중립 관계 설명; 길이·예측력 일치 비관계 설명; 정서결론 포함 민감도 조건; 유연한 영역 내 가산 모형; 공통입력×HRF 합성 null; cross-fitting
- **자료·착수 조건:** Horikawa 우선으로 시행 단위 대비를 설계하고 Emo-FilM·Spacetop에서는 실제 주석 단위에 맞춰 확장한다. Mind Captioning에 설명 자료가 있다면 출처·내용을 검수하는 후보이나 정서 주석을 있다고 가정하지 않는다.; 설명 생성의 독립 provenance와 중립성 검수 / 의미 조건 공통 표본·타깃 척도 / 관계와 정서가 불일치하는 지지 / ROI 신뢰도 및 주석 cohort / UC10-1의 별도 주석예산·외부 평가표본
- **근접 연구와 차이:** P083 / P067 / P102; 타깃을 고정한 nested 손실로 의미 추가의 일반 효과와 관계 특이 중복을 구별한다. UC10-1은 다음 관계 주석을 선택하는 별도 측정 설계로 추가되며 원 신경 질문을 대체하지 않는다.
- **중복·신규성 위험:** 사건 의미와 정서가 공선적이면 잔차의 고유성은 식별되지 않는다. N 이득도 BOLD 조건부 통계 상호작용이며 인과적 통신은 아니다.
- **병합 시 보존한 판정:** 각 원안의 역할 판정은 병합 후에도 보존한다. C03-05: 과학RQ후보; C10-02: 과학RQ후보
- **원본:** [agents/10_llm_semantics/round04_revision.json](../agents/10_llm_semantics/round04_revision.json); 후보 C03-05, C10-02
- **근거:** [P008 Emotion schemas are embedded in the human visual system](https://doi.org/10.1126/sciadv.aaw4358); [P001 The neural representation of visually evoked emotion is high-dimensional, categorical, and distributed across transmodal brain regions](https://doi.org/10.1016/j.isci.2020.101060); [P070 Prompt-to-Prompt Image Editing with Cross-Attention Control](https://arxiv.org/abs/2208.01626); [P077 Deep Adaptive Design: Amortizing Sequential Bayesian Experimental Design](https://arxiv.org/abs/2103.02438); [P083 Concept Bottleneck Models](https://raw.githubusercontent.com/mlresearch/v119/gh-pages/koh20a/koh20a.pdf); [P084 Label-free Concept Bottleneck Models](https://arxiv.org/abs/2304.06129); [P066 Discovering event structure in continuous narrative perception and memory](https://doi.org/10.1016/j.neuron.2017.06.041); [P067 Brain network dynamics are hierarchically organized in time](https://github.com/OHBA-analysis/HMM-MAR); [P100 Statistical inference on representational geometries](https://doi.org/10.7554/eLife.82566); [P102 Conditional independence testing based on a nearest-neighbor estimator of conditional mutual information](https://proceedings.mlr.press/v84/runge18a.html)

| 평가 | 점수 | 이유 | 불확실성 |
|---|---|---|---|
| novelty | 3 | 의미 조건×신경 조합은 구별되나 기존 variance partitioning과 가깝다. | 관계 특정 신규성 역검색 필요 |
| neuro_importance | 4 | 정서 관련 비가산성 주장이 누락 의미에 의존하는지 시험한다. | 조건부 예측은 기전 아님 |
| ai_necessity | 3 | 개념 모델이 주석을 구조화하지만 인간 관계 그래프도 충분할 수 있다. | LLM 필요성 미확정 |
| data_feasibility | 4 | 기존 관측에 독립 관계 주석을 추가하는 축소안이 있다. | 실제 overlap·주석예산 미확인 |
| rigor | 4 | 고정 타깃과 nested 손실로 estimand 변경을 피했다. | 공선성과 의미 완전성 제한 |
| falsifiability | 4 | 비관계 대조와 기준 N-D 부재가 명확한 반증·비식별 조건이다. | 표본 수·검출력 필요 |
| interpretability | 4 | 결론을 정보 중복과 모형 내 비가산성에 한정한다. | 공유정보의 이론적 해석 남음 |
| generalization | 3 | 내용군·피험자 외부 평가를 계획한다. | 관계 조합 support 불확실 |
| technical_feasibility | 4 | 소형 readout과 검수 주석으로 첫 비교 가능하다. | ROI·주석 독립성 확인 필요 |
| exploration_value | 4 | 순수 잔차 대신 공유 의미의 역할을 드러내는 질문이다. | 선행 중복 가능 |

여덟 탐색 질문의 개별 답과 비판 수용/미해결 이력은 위 구조화 원본에 보존했다.

**실제 Round5 반영 조건:** 고정 A·같은 proper loss·paired test에서 D=b(S)+Σf_r(X_r,S), N은 교차영역 항을 더한 함수족으로 명시한다. 관계/비관계 설명의 조건부 예측력 matching은 개발자료에서만 한다. δ는 정보분해나 신경영역 결합의 인과량이 아니다. 최종 감사 반영: 감소/부분 대체에는 g(O)의 충분한 기준 이득, r_R=g(O)-g(O+R)의 실제 의미 있는 감소, δ=g(O+B)-g(O+R)의 비교우위를 공동 신뢰하한으로 요구한다. δ만 양수이면 차등 변조이며 감소 증거가 아니다.

**철회한 강한 해석:** 영역 비가산 예측=실제 영역 간 결합, 관계 설명 추가=정서 기전 식별

평가 점수는 Round4의 역할 판단이다. Round5 조건으로 실제 착수 가능성이 좁아진 경우 현재 점수 자체를 실현성 증명으로 읽지 않는다.

<a id="rq13"></a>
## RQ13. 독립 반복의 신경 문맥이 자극모형 밖 정서 대비 예측을 회수하는가?

사전 정의한 자극모형 S에 신경 문맥 N을 추가할 때, 독립 반복 간에 전달되는 A 관련 신경 대비의 예측 이득이 같은 반복 잡음 공유와 구별되는가?

- **Axis·유형:** A × B × C × E × F × H × I × J × K × M × P × Q × R × X; Construct / Stimulus; Inference / Measurement; Model / Method; Neural; Structure / Dynamics
- **모델 적용 → 과학 질문 → 가정 도전:** TRIBE v2의 video/audio/text→평균 fsaverage5 피질 출력을 target 공간에 맞추고 train-only 개인 보정을 적용한다. CortexMAE/Brain-JEPA latent를 사용한 N→Y head는 별도 구현이다. masking을 normalization·smoothing·tokenization보다 앞에 적용하며 pretrained 모델이 그 mask를 처리하는지 단위 실행 검증을 요구한다. 미지원이면 masked raw-context ridge로 축소한다. → 같은 관측의 잡음 공유를 넘어 재현되는 신경 문맥이 현재 자극 표현의 예측 충분성에 추가로 필요한지 검사한다. → 신경문맥 추가 이득이 곧 내부 상태 또는 자극에 없는 정서 정보라는 해석을 검정한다.
- **경쟁 설명:** 동일 자극의 반복 a에서 얻은 N이 반복 b의 target Y에서 A 가중 대비 예측을 개선하며, 다른 자극/동일 run N과 의미 강화 baseline을 넘는 부분이 남는다. / 동일 반복에서만 이득이 있으면 공통 잡음·smoothing, 의미 강화로 줄면 누락 자극 표현, 모든 N에서 같으면 run/global nuisance가 설명한다.
- **관측 대비:** 각 held-out 자극 집합에서 사전 고정한 A 대비 가중치 w(합0, 제곱합1)로 c_A(Y)=Σ_i w_iY_i를 계산한다. w는 독립 주석의 고정 차원/고저 대비로 만들며 test BOLD나 model fit에 맞춰 고르지 않는다. L_A=||c_A(Y)-c_A(Yhat)||²_Q에서 Q는 training-only noise precision이다. Δ_A=L_A(S)-L_A(S+N)을 동일 반복 N, 독립 반복 N, 같은 run 다른 자극 N에서 비교한다. 전체 Y 손실과 A 비관련 일치 대비의 개선을 별도로 보고한다. 의미 보강×mask 폭 전체 곡선을 제시한다.
- **반증:** 독립 반복 N의 Δ_A가 사전 최소효과 이하라는 충분히 좁은 CI를 보이면 반복 전이 이득 가설을 반박한다. 동일 반복에만 남으면 공통 측정변동 설명을 강화한다. 의미 보강으로 사라지면 지정 S의 부족으로 분류한다. 반복·A 신뢰도가 부족하면 미식별이며 모든 자극모형 충분성은 주장하지 않는다.
- **기준모형:** 저수준+사건 의미+FIR ridge / TRIBE 공개 평균 출력에 train-only 개인별 선형 보정 / masked raw-neighbor ridge / 자기상관을 보존한 surrogate / 단순 nonlinear 자극 encoding / S+독립 반복 N / S+다른 자극/동일 run N / target 거리별 사전 masking과 global/run nuisance / 동일 입력을 갖는 raw-context ridge
- **자료·착수 조건:** ownership: Horikawa, Emo-FilM, Mind Captioning, NSD, Spacetop 보유는 최신 사용자 진술로 확인. 실제 로컬 경로·버전·스키마를 확인한 것은 아니다.; primary: Horikawa 우선. 독립 정서 주석 A, 자극 ID, 신경 Y, 런/반복 구조를 확보한 분석 단위에서 시작한다.; fallback: 자극 단위 beta만 있으면 정적 대비만 수행하고 연속 BOLD 입력을 요구하는 모형에는 넣지 않는다. 주석이나 신뢰도 추정이 없으면 방법 검증으로 범위를 축소한다.; additional: Emo-FilM은 연속 시계열·시간 정렬 확인 뒤 동적 전이; NSD는 정서 주석 확인 전 의미/공간 방법 대조만; Spacetop은 과제별 실제 주석 확인 뒤 일반화; Mind Captioning은 정확한 식별자·버전·주석 사전 확인 전 특정 실험에 배정하지 않는다.; 공통 cortical mask와 시간 정렬 / TRIBE checkpoint의 최종 TR/config와 5초 offset 처리 / brain model의 실제 mask token/보류 블록 동작 / 개인 평균 출력과 개인 Y 차이의 통제 / 독립 반복 및 개념 probe용 별도 자극 / 반복 a/b의 동일 자극 대응과 nuisance 독립성 / A 대비 w와 loss Q의 사전 정의 / 전처리 이전 mask가 feature 전파를 차단하는 실제 동작
- **근접 연구와 차이:** P027 / P026 / P083; 원 비교의 A 지도 겹침을 명시적 A contrast 예측손실로 바꾸고 동일/독립 반복 입력의 비대칭을 주조작으로 만든다. residual의 원인 분해를 완수했다는 주장은 철회한다.
- **중복·신규성 위험:** variance partitioning 재적용 위험이 높다. target 누출 방지와 의미 강화에 따른 불일치의 감소/잔존을 일차 판별로 고정한다.
- **병합 시 보존한 판정:** 각 원안의 역할 판정은 병합 후에도 보존한다. C04-02: 과학RQ후보; C07-05: 과학RQ후보
- **원본:** [agents/04_brain_foundation/round04_revision.json](../agents/04_brain_foundation/round04_revision.json); 후보 C04-02, C07-05
- **근거:** [P026 Scaling Vision Transformers for Functional MRI with Flat Maps](https://arxiv.org/abs/2510.13768); [P027 A foundation model of vision, audition, and language for in-silico neuroscience](https://arxiv.org/abs/2605.04326); [P029 Brain-JEPA: Brain Dynamics Foundation Model with Gradient Positioning and Spatiotemporal Masking](https://arxiv.org/abs/2409.19407); [P053 Challenging Common Assumptions in the Unsupervised Learning of Disentangled Representations](https://proceedings.mlr.press/v97/locatello19a.html); [P080 BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation](https://raw.githubusercontent.com/mlresearch/v162/gh-pages/li22n/li22n.pdf); [P083 Concept Bottleneck Models](https://raw.githubusercontent.com/mlresearch/v119/gh-pages/koh20a/koh20a.pdf); [P037 Factorized Contrastive Learning: Going Beyond Multi-view Redundancy](https://arxiv.org/abs/2306.05268); [P038 Attention Bottlenecks for Multimodal Fusion](https://arxiv.org/abs/2107.00135); [P058 Quantifying & Modeling Multimodal Interactions: An Information Decomposition Framework](https://arxiv.org/abs/2302.12247); [P102 Conditional independence testing based on a nearest-neighbor estimator of conditional mutual information](https://proceedings.mlr.press/v84/runge18a.html); [P100 Statistical inference on representational geometries](https://doi.org/10.7554/eLife.82566)

| 평가 | 점수 | 이유 | 불확실성 |
|---|---|---|---|
| novelty | 3 | 독립 반복×마스크×의미 강화가 잔차 비교를 구체화함 | 외부 영어 역검색 요청은 proxy 403으로 결과 미접근; 최신 선행 배제 불가. |
| neuro_importance | 4 | 자극모형의 관측 예측 충분성을 실제 반복으로 제한함 | 독립 A/신경 대비가 실제 검출 가능해야 과학적 중요성이 실현됨. |
| ai_necessity | 2 | raw-context ridge로도 첫 판별이 가능함 | 강한 작은 모형이 충분하면 foundation model 필요성 점수를 추가로 낮춰야 함. |
| data_feasibility | 2 | 독립 반복과 같은 자극의 N/Y 대응이 필수이나 미확인 | 다섯 자료 보유는 확인되었으나 로컬 버전·스키마·반복·주석은 미검증. |
| rigor | 4 | A contrast loss와 전처리 이전 masking을 명시함 | 제안한 통제는 아직 실행하지 않았고 표본수에 따른 검정력은 미확인. |
| falsifiability | 4 | 같은 반복/독립 반복의 대안별 예측이 다름 | 동등성 문턱과 신뢰도는 실자료의 개발 표본에서 결과 확인 전 고정해야 함. |
| interpretability | 3 | 미모형화 자극과 내부 상태는 여전히 분리 불가 | 관찰 예측 결과는 인간 뇌 인과나 고유 정보량을 확정하지 못함. |
| generalization | 3 | 새 자극·세션 전이가 가능하지만 반복 조건 제약이 큼 | 실제 독립 자극/참가자/세션 수와 사전학습 중복이 미확인. |
| technical_feasibility | 2 | TRIBE config·개인 보정·mask 지원과 공통 공간 확인 필요 | checkpoint load·GPU/시간·정확한 입력 지원은 아직 실행 검증하지 않음. |
| exploration_value | 4 | 뇌조건부 추가 이득의 기원을 과장하지 않는 시험임 | 새 연결의 유용성은 대조 모형이 관측 후 구별되는지에 달림. |

여덟 탐색 질문의 개별 답과 비판 수용/미해결 이력은 위 구조화 원본에 보존했다.

**실제 Round5 반영 조건:** 같은 사람·같은 자극의 실제 독립 반복과 target-free 전처리가 필요하다. Horikawa 내용 중복은 반복이 아니다. A 동시 공간완성과 B 과거→미래는 관측 계약이 다르다.

**철회한 강한 해석:** 반복 없는 Horikawa에서 즉시 독립 신경 문맥 회수 확증

평가 점수는 Round4의 역할 판단이다. Round5 조건으로 실제 착수 가능성이 좁아진 경우 현재 점수 자체를 실현성 증명으로 읽지 않는다.

<a id="rq14"></a>
## RQ14. parcel 평균이 지운 내부 공간 대비는 정서 관련 예측에 필요한가?

동일 피질 관측에서 parcel 평균에 의해 제거되는 zero-mean 성분이 독립 정서 대비 예측을 회수하며, 그 효과는 특정 atlas 경계에 의존하는가?

- **Axis·유형:** A × E × F × H × I × J × K × O × Q × X; Construct / Stimulus; Inference / Measurement; Model / Method; Neural; Structure / Dynamics
- **모델 적용 → 과학 질문 → 가정 도전:** 서로 겹치지 않는 parcel 평균 행렬 G에 대해 P=Gᵀ(GGᵀ)⁻¹G를 고정하고 m=Py,r=(I-P)y로 나누면 Gr=0이다. 이는 명시한 선형 집계의 대수적 성질이다. train-only PCA로 r의 k차원 좌표를 정하고 m/m+r_k/m+noise를 같은 readout으로 비교한다. CortexMAE variant는 이후 표현의 추가 변형을 검사하는 도구이며 이 직접 대조에 필수 가중치가 아니다. → 지역 평균만으로 A 관련 신경 대비를 읽기에 충분한지, 평균이 상쇄한 재현 가능한 공간 대비가 필요한지 검정한다. → atlas 평균이 신호잡음만 개선하는 중립적 축약이라는 가정. 일반 평균화와 특정 atlas 경계의 효과를 나눈다.
- **경쟁 설명:** H1: m+r_k가 m보다 보류 자극 A 예측을 재현 가능하게 개선한다. H2: 공간 주파수·rank·신뢰도 지표를 명시해 맞춘 뒤 실제 atlas와 random-contiguous parcel의 H1 효과가 다르다. A 선택성은 matched 비정서 대비와의 별도 상호작용이다. / H1 이득이 없으면 평균 충분성 또는 낮은 검정력, H1은 있으나 H2가 없으면 일반 평균 상쇄, 비정서 대비와 같으면 표적 비특이 미세 공간정보다.
- **관측 대비:** 주 추정량은 외부 자극에서 A 예측손실 L(m)-L(m+r_k)이며 V,S를 포함/미포함한 총·조건부 버전을 분리한다. 잔차는 다른 반복에서 신뢰도를 확인하고 m+rank-matched noise 및 m+spatial-spectrum-matched control과 비교한다. 실제/무작위 연속 parcel은 같은 원 y에서 생성한다. 신뢰도 보정 전 총 효과와 train-only 신뢰도/공간대역 보정 효과를 병행하며 보정 후 결과만 선택하지 않는다.
- **반증:** H1은 반복 신뢰도가 충분한 r_k를 더해도 A 접근성 개선의 CI가 동등성 범위 안이면 반박한다. H2는 실제/random atlas 효과 차이가 동등하면 반박한다. random parcel에서도 H1이 유지되는 것은 H1의 반증이 아니다. 비정서 대비도 동일하면 정서 선택성만 반박한다. rank 일치를 정보량 일치라고 부르지 않는다.
- **기준모형:** m-only ridge / m+within-parcel zero-mean k차원 / m+rank-matched noise / spatial-spectrum-matched random aggregation / 실제 atlas 대 random contiguous atlas / 독립 비정서 대비의 분산/신뢰도/공간 주파수 대조
- **자료·착수 조건:** ownership: Horikawa, Emo-FilM, Mind Captioning, NSD, Spacetop 보유는 최신 사용자 진술로 확인. 실제 로컬 경로·버전·스키마를 확인한 것은 아니다.; primary: Horikawa 우선. 독립 정서 주석 A, 자극 ID, 신경 Y, 런/반복 구조를 확보한 분석 단위에서 시작한다.; fallback: 자극 단위 beta만 있으면 정적 대비만 수행하고 연속 BOLD 입력을 요구하는 모형에는 넣지 않는다. 주석이나 신뢰도 추정이 없으면 방법 검증으로 범위를 축소한다.; additional: Emo-FilM은 연속 시계열·시간 정렬 확인 뒤 동적 전이; NSD는 정서 주석 확인 전 의미/공간 방법 대조만; Spacetop은 과제별 실제 주석 확인 뒤 일반화; Mind Captioning은 정확한 식별자·버전·주석 사전 확인 전 특정 실험에 배정하지 않는다.; 동일 참가자의 dense와 parcel 변환 가능성 / 정확한 cortical vertex/voxel 대응 / 반복 신뢰도 / 표면 재등록 및 smoothing 정보 / CortexMAE variant별 학습 차이
- **근접 연구와 차이:** P026 / P081 / P051; 단순 P/F/V 성능 비교에서 집계 연산의 영공간에 실제 예측 가능한 대비가 존재하는지 묻는 witness 검사로 변경했다. 일반 평균 상쇄·경계 특이성·정서 선택성에 서로 다른 반증을 부여한다.
- **중복·신규성 위험:** 기존 multivoxel 대 ROI-average 비교와 가까우므로 신규성은 중간 이하로 둔다. 독립 반복의 null-space witness와 세 가설의 분리가 없으면 방법 QC로 낮춘다.
- **병합 시 보존한 판정:** 각 원안의 역할 판정은 병합 후에도 보존한다. C04-03: 과학RQ후보
- **원본:** [agents/04_brain_foundation/round04_revision.json](../agents/04_brain_foundation/round04_revision.json); 후보 C04-03
- **근거:** [P026 Scaling Vision Transformers for Functional MRI with Flat Maps](https://arxiv.org/abs/2510.13768); [P051 Similarity of Neural Network Representations Revisited](https://proceedings.mlr.press/v97/kornblith19a.html); [P060 A Python Toolbox for Representational Similarity Analysis](https://doi.org/10.1101/2025.05.22.655542); [P081 BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models](https://raw.githubusercontent.com/mlresearch/v202/gh-pages/li23q/li23q.pdf); [P076 Diffusion Posterior Sampling for General Noisy Inverse Problems](https://github.com/DPS2022/diffusion-posterior-sampling)

| 평가 | 점수 | 이유 | 불확실성 |
|---|---|---|---|
| novelty | 3 | ROI 평균 대 패턴은 기존이며 null-space witness와 세 반증이 차별점 | 외부 영어 역검색 요청은 proxy 403으로 결과 미접근; 최신 선행 배제 불가. |
| neuro_importance | 4 | 지역 평균의 정서 대비 충분성을 직접 검정함 | 독립 A/신경 대비가 실제 검출 가능해야 과학적 중요성이 실현됨. |
| ai_necessity | 2 | 선형 집계와 ridge가 충분한 첫 실험이므로 대형 AI 필수성 낮음 | 강한 작은 모형이 충분하면 foundation model 필요성 점수를 추가로 낮춰야 함. |
| data_feasibility | 3 | dense 피질·반복·A가 필요하나 정적 자료로도 가능 | 다섯 자료 보유는 확인되었으나 로컬 버전·스키마·반복·주석은 미검증. |
| rigor | 4 | 동일 관측의 정확한 평균/영공간 분해로 혼동을 줄임 | 제안한 통제는 아직 실행하지 않았고 표본수에 따른 검정력은 미확인. |
| falsifiability | 5 | 일반 상쇄·atlas 특이성·A 선택성의 반증이 구별됨 | 동등성 문턱과 신뢰도는 실자료의 개발 표본에서 결과 확인 전 고정해야 함. |
| interpretability | 4 | 관측 표현의 충분성으로 제한해 해석이 명확함 | 관찰 예측 결과는 인간 뇌 인과나 고유 정보량을 확정하지 못함. |
| generalization | 4 | 새 자극·반복·atlas로 일반화 구조가 구체적임 | 실제 독립 자극/참가자/세션 수와 사전학습 중복이 미확인. |
| technical_feasibility | 4 | checkpoint 없이 선형 대조부터 가능하나 자료 경로 미확인 | checkpoint load·GPU/시간·정확한 입력 지원은 아직 실행 검증하지 않음. |
| exploration_value | 4 | 병목 단계의 정보 손실을 직접 witness로 바꿈 | 새 연결의 유용성은 대조 모형이 관측 후 구별되는지에 달림. |

여덟 탐색 질문의 개별 답과 비판 수용/미해결 이력은 위 구조화 원본에 보존했다.

**실제 Round5 반영 조건:** 면적가중 G/P를 명세하고 평균-only 강한 nonlinear 대조, train-only k곡선과 H1일반상쇄/H2atlas/H3정서선택성 각각을 검정한다. 반복 미확보 시 신뢰도 상한을 만들지 않는다.

**철회한 강한 해석:** r_k의 음성결과=전체 영공간 정보부재

평가 점수는 Round4의 역할 판단이다. Round5 조건으로 실제 착수 가능성이 좁아진 경우 현재 점수 자체를 실현성 증명으로 읽지 않는다.

<a id="rq15"></a>
## RQ15. 관측격자를 넘어 필요한 이력 함수는 비선형 관측인가 선택적 상태 전이인가?

입력·출력 비선형성과 시간 예산을 통제할 때, 고정 상태 전이에 입력 gate를 더하는 것으로 충분한가 아니면 입력 의존 전이가 A 관련 신경 대비의 외부 예측에 추가로 필요한가?

- **Axis·유형:** C × D × F × H × I × K × N × Q × T × V × X; Construct / Stimulus; Inference / Measurement; Model / Method; Neural; Structure / Dynamics
- **모델 적용 → 과학 질문 → 가정 도전:** 신규 소규모 상태모델 3개를 공통 nonlinear input/output map으로 구현한다: F0 고정 A 전이, F1 고정 A+입력 의존 injection gate, F2 입력 의존 A(x) 전이. nonlinear AR 및 정적 gate를 추가한다. Brain-Mamba 공식 코드가 미확보이므로 이 구현을 그 모델 재현 또는 pretrained 활용이라 부르지 않는다. → 신경 관측의 이력 의존 예측에 필요한 함수 복잡도가 단순 입력/출력 비선형성인지 상태 유지의 입력 의존성인지 제한한다. → selective SSM 우월성은 곧 뇌의 선택 gate라는 가정을 시험하고, model-step을 신경 시간상수로 읽지 않는다.
- **경쟁 설명:** 실시간 이력·대역폭·상태차원·목표·readout을 맞춰도 F2의 독립 A contrast 예측이 F0/F1/nonlinear AR보다 개선되며 관측격자 변경에 견고하다. / 추가 이득은 일반 nonlinear capacity·최적화·입력 gating·HRF/보간·같은 창 안의 내용량으로 설명된다.
- **관측 대비:** native/사전 정한 재표본 격자×F0/F1/F2를 비교하되 같은 초 단위 과거, anti-alias 처리, nonlinear input/output와 train-only normalization을 사용한다. 독립 A의 측정 시간단위로 집계한 neural contrast 손실과 전체 Y 손실을 분리한다. 동일 용량/수렴 곡선, gate 정적화/교환, 동일 내용 순서 대조를 함께 평가한다. multivariate surrogate는 채널마다 같은 주파수 위상을 더해 cross-spectrum를 보존하는 구성부터 사용하며 고차 의존성은 보존하지 않는다고 명시한다.
- **반증:** F1 또는 nonlinear AR이 F2와 효과 동등하면 선택 전이의 추가 필요성을 반박한다. 격자/미래차단 후 효과가 소실되면 관측 처리 설명을 강화한다. gate test-time 교환에만 취약하면 OOD 가능성이 남으므로 해당 제어로 재학습한 결과와 함께 판단한다. 어떤 결과도 생물학적 gate를 확정하지 않는다.
- **기준모형:** native-TR AR/FIR ridge / 동일 상태차원 fixed SSM / 같은 문맥 길이 temporal convolution / 자기상관/스펙트럼 보존 surrogate / 과거 사건 bag와 순서 보존 표현 / F0 고정 전이+공통 nonlinear input/output / F1 고정 전이+입력 injection gate / nonlinear AR / 재학습한 static gate 대 test-time gate exchange / multivariate cross-spectrum 보존 surrogate
- **자료·착수 조건:** ownership: Horikawa, Emo-FilM, Mind Captioning, NSD, Spacetop 보유는 최신 사용자 진술로 확인. 실제 로컬 경로·버전·스키마를 확인한 것은 아니다.; primary: Horikawa에서 연속 원시/전처리 시계열 지원을 먼저 확인한다. 없다면 이 동적 후보의 첫 검증은 연속 BOLD·주석을 확인한 Emo-FilM에 배정한다.; fallback: 시점별 A가 없으면 동적 정서 가설은 보류하고 관측격자 방법 검증만 한다. 자극 단위 beta는 이 후보 입력으로 만들지 않는다.; additional: Emo-FilM은 연속 시계열·시간 정렬 확인 뒤 동적 전이; NSD는 정서 주석 확인 전 의미/공간 방법 대조만; Spacetop은 과제별 실제 주석 확인 뒤 일반화; Mind Captioning은 정확한 식별자·버전·주석 사전 확인 전 특정 실험에 배정하지 않는다.; 연속 BOLD와 정확한 TR/시간원점 / 이벤트·정서 주석의 측정 시간 해상도 / 보간의 과거 전용 구현 / 모형 코드 독립 재구현 검증 / 상태차원·학습량·문맥 실시간 길이 통제
- **근접 연구와 차이:** P028 / P034 / P086; 고정 대 선택 SSM의 이분법을 입력/관측 비선형, injection gate, 전이 gate의 위치별 함수족 경쟁으로 바꿨다. 상태 계산과 일반 용량을 구별할 수 있는 수준까지만 주장을 유지한다.
- **중복·신규성 위험:** 일반 temporal benchmark로 환원될 수 있다. 관측격자에 견고한 독립 A 관련 대비가 없으면 정서 연구 후보에서 내린다.
- **병합 시 보존한 판정:** 각 원안의 역할 판정은 병합 후에도 보존한다. C04-05: 과학RQ후보
- **원본:** [agents/04_brain_foundation/round04_revision.json](../agents/04_brain_foundation/round04_revision.json); 후보 C04-05
- **근거:** [P026 Scaling Vision Transformers for Functional MRI with Flat Maps](https://arxiv.org/abs/2510.13768); [P028 Brain-Mamba: Encoding Brain Activity via Selective State Space Models](https://proceedings.mlr.press/v248/behrouz24a.html); [P034 Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://arxiv.org/abs/2312.00752); [P056 Topological Autoencoders](https://proceedings.mlr.press/v119/moor20a.html); [P085 The neural architecture of language: Integrative modeling converges on predictive processing](https://github.com/mschrimpf/neural-nlp); [P086 Scaling laws for language encoding models in fMRI](https://arxiv.org/abs/2305.11863); [P090 Brain-Like Object Recognition with High-Performing Shallow Recurrent ANNs](https://arxiv.org/abs/1909.06161); [P096 Predictive Coding Approximates Backprop along Arbitrary Computation Graphs](https://arxiv.org/abs/2006.04182)

| 평가 | 점수 | 이유 | 불확실성 |
|---|---|---|---|
| novelty | 3 | SSM 비교 선행은 있으나 비선형 위치×격자 대비가 구체적임 | 외부 영어 역검색 요청은 proxy 403으로 결과 미접근; 최신 선행 배제 불가. |
| neuro_importance | 4 | 이력 의존 관측에 필요한 함수족을 좁힘 | 독립 A/신경 대비가 실제 검출 가능해야 과학적 중요성이 실현됨. |
| ai_necessity | 3 | 함수족 구현이 필요하지만 대형 pretrained SSM은 불필요함 | 강한 작은 모형이 충분하면 foundation model 필요성 점수를 추가로 낮춰야 함. |
| data_feasibility | 2 | 연속 BOLD와 A 시간단위/지연 정보가 필수이며 미확인 | 다섯 자료 보유는 확인되었으나 로컬 버전·스키마·반복·주석은 미검증. |
| rigor | 4 | input/transition gate 및 관측필터를 분리함 | 제안한 통제는 아직 실행하지 않았고 표본수에 따른 검정력은 미확인. |
| falsifiability | 4 | F1/AR 충분성과 F2 이득의 구별이 명료함 | 동등성 문턱과 신뢰도는 실자료의 개발 표본에서 결과 확인 전 고정해야 함. |
| interpretability | 3 | predictive family 차이를 생물학적 gate로 읽을 수 없음 | 관찰 예측 결과는 인간 뇌 인과나 고유 정보량을 확정하지 못함. |
| generalization | 4 | 격자·새 자극·순서 대조의 일반화가 명시됨 | 실제 독립 자극/참가자/세션 수와 사전학습 중복이 미확인. |
| technical_feasibility | 2 | 공식 Brain-Mamba 미확보로 신규 구현·검증 필요 | checkpoint load·GPU/시간·정확한 입력 지원은 아직 실행 검증하지 않음. |
| exploration_value | 4 | 선택성이라는 이름에 숨은 일반 용량 효과를 드러냄 | 새 연결의 유용성은 대조 모형이 관측 후 구별되는지에 달림. |

여덟 탐색 질문의 개별 답과 비판 수용/미해결 이력은 위 구조화 원본에 보존했다.

<a id="rq16"></a>
## RQ16. 공유 병목의 용량을 넘어 남는 모달리티 정보의 예측 충분성

동일 시청각 정보원과 읽기모형 예산에서 공유 병목을 확대해도 전체 모달리티 정보 또는 분해 잔차가 독립 정서 신경 대비를 추가 설명하는가?

- **Axis·유형:** A × B × C × E × H × I × J × M × N × P × Q × R × S × T × X; Construct / Stimulus; Inference / Measurement; Model / Method; Neural; Structure / Dynamics
- **모델 적용 → 과학 질문 → 가정 도전:** 같은 동결 V,A에서 공유 S_k와 operational residual을 만들고, 사전 소수 bottleneck k×잔차 포함을 비교한다. full V,A의 같은 유효 용량 readout과 shared-only의 유연한 nonlinear readout을 둔다. FactorCL은 감독 사용 확인 뒤 전체 학습을 nested split에 넣거나 학습 없는 cross-fitted 투영으로 대체한다. → 공통 좌표의 제한된 압축이 버린 정보의 회수인지, 충분히 넓은 공유 표현으로도 설명하지 못한 정보원 의존인지 구분한다. → 고유 latent의 추가 효과가 고유 신경경로를 뜻한다는 가정과 공유표현이 자동으로 충분하다는 가정을 함께 제한한다.
- **경쟁 설명:** 병목 용량·읽기모형 유연성·내용 품질을 맞춘 범위에서도 잔차/전체 정보의 정서 대비 paired-risk 이득이 남는다. / 좁은 공유 병목 또는 제한된 readout이 빠뜨린 사건 의미·감각 품질을 추가 경로가 회수할 뿐이다.
- **관측 대비:** D_k=mean_i[loss(z_Ai,pred_Sk,i)−loss(z_Ai,pred_Sk+residual,i)]를 동일 test 표본과 공통 척도에서 구한다. k×정보원 접근의 곡선을 전체 V,A 대조와 비교한다. 총 모델 용량·정규화·유효 자유도 민감도를 보고하고 gate는 고정한다.
- **반증:** 큰 병목 또는 유연한 shared readout에서 D_k의 사전 최소 효과 상한이 작아지면 이 범위의 잔차 필요성은 지지되지 않는다. 잔차 효과가 seed/분해에 불안정하면 특정 private 정보 해석을 보류한다. 전체 모형도 신뢰 가능한 대비를 못 예측하면 식별불가다.
- **기준모형:** 고정 gate shared-only 용량곡선 / 전체 V,A 동일 유효 용량 nonlinear readout / strict nonlinear additive / 같은 정보량의 직교 좌표변환과 readout 재적합 / 독립 사건 의미·감각 품질 probe
- **자료·착수 조건:** primary: Horikawa의 실제 시청각 자극 가용성부터 확인하여 자극 단위 검정. 시각-only 보유본이면 이 데이터에서 멀티모달 검정을 하지 않는다.; validation: Emo-FilM에서 영화 단위 분할 및 정렬 가능한 시간 집계로 재검증. Spacetop은 실제 task의 clip 수준 뇌·평정 대응으로만 재검증한다.; auxiliary: NSD는 시각 경로의 내용·신뢰도 대조만. Mind Captioning은 정확한 자료 식별·모달리티·주석 확인 이후 의미 통제 후보다.; fallback: 공개 분해의 감독 사용/가중치가 미확인이면 고정 V,A의 train-only 공유 투영과 잔차를 operational 대조로 사용한다. private factor의 실재 추론은 하지 않는다.; 각 보유본의 실제 오디오·영상 제공 범위와 재생 조건 / 독립 정서주석·반복 신뢰도 / 분해의 seed/회전 안정성 / Horikawa dupidx와 내용군 매핑 / FactorCL 학습에 사용되는 타깃·출력 경로와 nested feature learning / 독립 대비 정의·평가 분할 및 bottleneck k 범위 / 공유분해 seed/읽기모형 충분성 감사
- **근접 연구와 차이:** P035 / P037 / P053; Round2의 gate/private 혼합 조작을 정보원 접근×공유 병목의 충분성 경계로 재구성했다. 축 이름을 찾는 대신 동일 정보를 보존한 좌표 변화와 정보원 제거를 구분한다.
- **중복·신규성 위험:** shared/private encoding과 정보보존 감사의 엄격한 재평가일 수 있다. 특정 분해의 잔차를 생물학적 고유 경로로 해석하지 않으며 신규성은 미확정이다.
- **병합 시 보존한 판정:** 각 원안의 역할 판정은 병합 후에도 보존한다. C05-01: 과학RQ후보
- **원본:** [agents/05_multimodal_dynamics/round04_revision.json](../agents/05_multimodal_dynamics/round04_revision.json); 후보 C05-01
- **근거:** [P035 ImageBind: One Embedding Space To Bind Them All](https://arxiv.org/abs/2305.05665); [P037 Factorized Contrastive Learning: Going Beyond Multi-view Redundancy](https://arxiv.org/abs/2306.05268); [P053 Challenging Common Assumptions in the Unsupervised Learning of Disentangled Representations](https://proceedings.mlr.press/v97/locatello19a.html); [P051 Similarity of Neural Network Representations Revisited](https://proceedings.mlr.press/v97/kornblith19a.html); [P083 Concept Bottleneck Models](https://raw.githubusercontent.com/mlresearch/v119/gh-pages/koh20a/koh20a.pdf); [P100 Statistical inference on representational geometries](https://doi.org/10.7554/eLife.82566)

| 평가 | 점수 | 이유 | 불확실성 |
|---|---|---|---|
| novelty | 3 | 정보원 접근×공유 용량은 명료하지만 shared/private encoding 선행과의 차이는 역검색이 남았다. | 외부 Crossref 역검색 403으로 최신 중복·최초성 미확인. |
| neuro_importance | 4 | 공통 표현의 충분성과 압축손실 회수를 구분해 정서 관련 코드 해석을 제한한다. | 관측 신뢰도·대립모형 적합·실제 데이터 효과를 아직 평가하지 않은 E3 판단. |
| ai_necessity | 3 | 고차원 감각 특징은 필요하지만 최신 FactorCL 없이도 operational 비교가 가능하다. | 관측 신뢰도·대립모형 적합·실제 데이터 효과를 아직 평가하지 않은 E3 판단. |
| data_feasibility | 3 | Horikawa 실제 재생 오디오·독립 대비가 미확인이라 시청각 검정이 조건부다. | 실제 경로·버전·주석·체크포인트·연산비는 분석 착수 시 확인. |
| rigor | 4 | nested feature 학습·같은 readout·병목 용량 대조로 주요 혼동을 분리한다. | 관측 신뢰도·대립모형 적합·실제 데이터 효과를 아직 평가하지 않은 E3 판단. |
| falsifiability | 4 | 큰 병목에서 잔차 이득이 사라진다는 명확한 반증이 있다. | 관측 신뢰도·대립모형 적합·실제 데이터 효과를 아직 평가하지 않은 E3 판단. |
| interpretability | 4 | 생물학적 경로가 아닌 검토한 표현의 정보원 충분성으로 해석을 좁혔다. | 관측 신뢰도·대립모형 적합·실제 데이터 효과를 아직 평가하지 않은 E3 판단. |
| generalization | 3 | 내용군·피험자 보류는 가능하나 같은 modality·주석 지원 범위에 제한된다. | 관측 신뢰도·대립모형 적합·실제 데이터 효과를 아직 평가하지 않은 E3 판단. |
| technical_feasibility | 4 | 고정 특징 캐시와 작은 readout이 fallback이며 전체 인코더 재학습이 필수는 아니다. | 실제 경로·버전·주석·체크포인트·연산비는 분석 착수 시 확인. |
| exploration_value | 4 | 공유 좌표에 남은 정보와 버린 정보를 구별하는 적용 범위가 넓다. | 관측 신뢰도·대립모형 적합·실제 데이터 효과를 아직 평가하지 않은 E3 판단. |

여덟 탐색 질문의 개별 답과 비판 수용/미해결 이력은 위 구조화 원본에 보존했다.

**실제 Round5 반영 조건:** 고정한 shared rank/readout/표본량 범위의 접근성만 검정한다. S+residual이 full V,A의 가역 재표현이면 같은 정보입력 대조다. 실제 스캐너 음원 제시를 확인한다.

**철회한 강한 해석:** operational private 잔차=생물학적 고유 경로 또는 PID 고유정보

평가 점수는 Round4의 역할 판단이다. Round5 조건으로 실제 착수 가능성이 좁아진 경우 현재 점수 자체를 실현성 증명으로 읽지 않는다.

<a id="rq17"></a>
## RQ17. 인코더와 관측 필터를 구분한 모달리티별 유효 예측창

입력 가용시간과 encoder 시간필터를 명시한 조건에서 모달리티별 과거 정보량의 차이가 독립 정서 신경 대비를 설명하는 데 필요한가?

- **Axis·유형:** B × C × D × E × H × J × M × Q × V × X; Construct / Stimulus; Inference / Measurement; Model / Method; Neural; Structure / Dynamics
- **모델 적용 → 과학 질문 → 가정 도전:** 동일 endpoint t·실시간 입력 길이로 추출한 고정 시청각 특징에 짧음/김 2×2 창 readout을 둔다. 3×3 전체 grid는 보조 탐색이며 주대비 선정에 test를 사용하지 않는다. 모델별 encoder 유효 필터 차이를 문서화한다. → 모달리티별 과거 가용정보의 예측 충분성을 평가하고 그 차이가 관측 필터만으로 생기는지 구분한다. 실제 신경 시간상수 추정은 이 질문의 기본 산출물이 아니다. → 최적 입력창이 신경 기억 길이라는 가정을 철회한다. 같은 HRF family를 썼다는 사실만으로 encoder×HRF×기억을 식별했다고 하지 않는다.
- **경쟁 설명:** 실제 특징으로 생성한 복구 게이트를 통과한 범위에서 사전 지정 모달리티별 창 대비가 독립 정서 신경 대비의 paired risk를 개선한다. / encoder smoothing·입력 자기상관·모달리티별 관측지연과 readout 자유도 차이가 창 비대칭을 모두 설명한다.
- **관측 대비:** R_ab는 공통 출력단위의 held-out 손실이며 a,b∈{S,L}은 오디오/시각 창이다. 길어진 오디오의 이득 R_SS−R_LS와 시각의 이득 R_SS−R_SL의 차이를 사전 방향 대비로 보고, I=R_SS−R_LS−R_SL+R_LL은 별도의 joint-history 상호작용으로 구분한다. 창 최고점만 보고하지 않는다. 각 모형 HRF/FIR는 같은 family·차수·train 선택 예산으로 적합한다.
- **반증:** encoder 필터를 맞춘 뒤 사전 비대칭 대비의 최소 효과 상한이 작으면 공통 유효창으로 충분한 범위를 제시한다. 공통 기억+상이 encoder 필터와 상이 기억+공통 필터의 복구 혼동이 크면 잠재 신경 시간 해석을 보류하고 방법 후보 결과만 남긴다.
- **기준모형:** 같은 초 단위 입력범위·endpoint 특징 / 짧음/김 공통창 및 2×2 교차창 / 모달리티별 flexible FIR의 동일 적합 예산 / 실제 특징 spectrum/autocorrelation을 보존한 null / 공통기억/상이필터와 상이기억/공통필터의 합성 복구
- **자료·착수 조건:** primary: Emo-FilM의 연속 주석·film onset·BOLD 타임베이스로 조건부 검정. 평정은 스캔 참가자 개인 궤적이 아니라 별도 코호트 관측이다.; horikawa: 우선 보유본에서 원시 시간계열·자극 재생·주석 단위를 확인한다. clip 집계만 있으면 시간창의 clip-level 예측 비교로 줄이고 신경 시간상수 주장을 하지 않는다.; validation: Spacetop은 자극 중 BOLD 시간계열은 사용할 수 있지만 clip 평정으로 연속 정서 궤적을 만들지 않는다. NSD는 본 시간 질문에 쓰지 않는다.; fallback: 새 시간모델 학습 없이 고정 특징의 causal pooling으로 시작. Mind Captioning은 정체·시간 주석 확인 전 핵심 자료로 지정하지 않는다.; TR·run·자극 재생 시각과 음향 동기 / encoder receptive field와 t 이후 입력 차단 감사 / 평정 지연·신뢰도 및 충분한 영화 수 / HRF×창 식별 가능성 시뮬레이션 / 실제 자극 특성·run구조·잡음을 보존한 복구 / encoder별 prefix-only 재추출과 전처리 미래 접근 감사 / 주창 대비의 사전 방향·최소 효과 기준
- **근접 연구와 차이:** P038 / P043 / P002; 일반 HRF 통제에서 나아가 서로 다른 생성기전이 각자 관측 파라미터를 적합한 뒤에도 구분되는지 검사한다. 유효 예측창과 신경 시간상수를 다른 결론으로 분리했다.
- **중복·신규성 위험:** temporal receptive window의 방법론적 정교화일 수 있다. 독립 정서 대비가 없거나 복구 게이트 실패 시 시간관측 방법 후보로 분리한다.
- **병합 시 보존한 판정:** 각 원안의 역할 판정은 병합 후에도 보존한다. C05-02: 과학RQ후보
- **원본:** [agents/05_multimodal_dynamics/round04_revision.json](../agents/05_multimodal_dynamics/round04_revision.json); 후보 C05-02
- **근거:** [P002 Emo-FilM: A multimodal dataset for affective neuroscience using naturalistic stimuli](https://doi.org/10.1038/s41597-025-04803-5); [P038 Attention Bottlenecks for Multimodal Fusion](https://arxiv.org/abs/2107.00135); [P043 VideoMamba: State Space Model for Efficient Video Understanding](https://arxiv.org/abs/2403.06977); [P034 Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://arxiv.org/abs/2312.00752); [P101 Representational models: A common framework for understanding encoding, pattern-component, and representational-similarity analysis](https://doi.org/10.1371/journal.pcbi.1005508); [P100 Statistical inference on representational geometries](https://doi.org/10.7554/eLife.82566)

| 평가 | 점수 | 이유 | 불확실성 |
|---|---|---|---|
| novelty | 3 | 시간창 연구와 가깝고 신경시간 수치보다 관측 충분성에 기여가 있다. | 외부 Crossref 역검색 403으로 최신 중복·최초성 미확인. |
| neuro_importance | 4 | 정서 시간효과를 encoder/HRF 착시와 구별하는 것은 핵심 해석 문제다. | 관측 신뢰도·대립모형 적합·실제 데이터 효과를 아직 평가하지 않은 E3 판단. |
| ai_necessity | 2 | 단순 causal pooling/FIR로 주가설 검정이 가능해 대형 AI의 필수성은 낮다. | 관측 신뢰도·대립모형 적합·실제 데이터 효과를 아직 평가하지 않은 E3 판단. |
| data_feasibility | 3 | 연속 주석·동기화·충분한 영화가 필요하고 보유본 실제 스키마는 조건부다. | 실제 경로·버전·주석·체크포인트·연산비는 분석 착수 시 확인. |
| rigor | 4 | 실제 autocorrelation 복구와 사전 창 대비가 선택·필터 혼동을 줄인다. | 관측 신뢰도·대립모형 적합·실제 데이터 효과를 아직 평가하지 않은 E3 판단. |
| falsifiability | 4 | 효과 복구와 최소효과 마진을 통과한 null을 명확히 구분한다. | 관측 신뢰도·대립모형 적합·실제 데이터 효과를 아직 평가하지 않은 E3 판단. |
| interpretability | 3 | 유효 예측창은 해석 가능하나 잠재 신경시간과의 연결은 제한된다. | 관측 신뢰도·대립모형 적합·실제 데이터 효과를 아직 평가하지 않은 E3 판단. |
| generalization | 3 | 영화 외부 평가가 가능하지만 encoder filter와 modality 변화에 의존한다. | 관측 신뢰도·대립모형 적합·실제 데이터 효과를 아직 평가하지 않은 E3 판단. |
| technical_feasibility | 3 | prefix 재추출 비용·체크포인트 길이 제한 확인이 필요하다. | 실제 경로·버전·주석·체크포인트·연산비는 분석 착수 시 확인. |
| exploration_value | 4 | 기전 차이가 없어도 신경시간 주장의 경계를 정할 수 있다. | 관측 신뢰도·대립모형 적합·실제 데이터 효과를 아직 평가하지 않은 E3 판단. |

여덟 탐색 질문의 개별 답과 비판 수용/미해결 이력은 위 구조화 원본에 보존했다.

<a id="rq18"></a>
## RQ18. 경계 단서와 과거 소거를 분리한 상태 갱신의 필요성

경계 단서를 동일하게 제공하고 초기상태·훈련 노출·관측 필터를 맞춘 뒤에도 사건 위치의 forgetting이 독립 정서 신경 전이를 설명하는 데 필요한가?

- **Axis·유형:** C × D × H × I × J × M × N × Q × V × X; Construct / Stimulus; Inference / Measurement; Model / Method; Neural; Structure / Dynamics
- **모델 적용 → 과학 질문 → 가정 도전:** 동결 영상/비음성 오디오 특징 위 신규 소형 causal state head h_t=F_theta(h_prev,x_≤t)를 둔다. hard zero, train-fit initial state h0, soft forgetting h_tilde=(1−rho_t)h_prev+rho_t h0를 명시한다. theta,h0,rho의 파라미터수와 train 목적을 기록하며 비정서 자극 예측 학습과 BOLD readout 학습을 분리한다. → 경계의 존재를 부호화하는 것과 과거 상태를 줄이는 것 중 어떤 연산이 정서 관련 신경 전이에 추가 설명을 제공하는가? → reset 승리가 뇌의 기억 초기화를 뜻한다는 가정을 배제한다. 초기화 prior·훈련 밖 충격·시간평활화가 같은 결과를 만들 수 있다.
- **경쟁 설명:** 경계 단서가 동일한 조건에서 경계 forgetting이 never·soft generic decay·norm/age/예상오차를 맞춘 random forgetting보다 독립 정서 전이의 예측 위험을 낮춘다. / 경계 indicator만으로 충분하거나 reset-aware 훈련/초기상태 prior/유효 시간필터가 이득을 설명한다.
- **관측 대비:** readout의 boundary indicator 제공(0/1)×state forgetting(0/1)의 2×2를 주분석으로 둔다. 핵심 paired loss는 indicator=1에서 never 대 boundary forgetting 차이이며 같은 연산의 matched-random 위치 대조를 추가한다. 모든 경쟁모형 theta와 HRF/FIR nuisance를 train에서 동일 예산으로 적합하고 독립 영화에서 고정 평가한다. 각 모형의 최선 관측모형을 허용한 뒤의 이득과 공통 고정 관측모형 결과를 나란히 보고한다.
- **반증:** indicator-only 또는 유한창/soft decay가 동등하면 위치특이 소거가 필수라는 가설을 제한한다. reset exposure를 맞추면 이득이 사라지면 훈련 분포이탈 설명이다. 양쪽 생성기전이 관측 후 같은 최소효과 범위의 예측을 내며 복구할 수 없으면 기억 기전을 판정하지 않는다.
- **기준모형:** boundary indicator를 동일 제공한 never-reset / 경계·random 위치에 같은 zero/learned-h0/soft 연산 / reset-aware 훈련 대 test-time-only reset / 같은 입력량의 유한창·generic decay / norm/age/예상오차·컷·음향 onset 맞춤 random 위치
- **자료·착수 조건:** primary: Emo-FilM의 연속 자극과 주석으로 경계 효과 평가. 영화 단위 분할을 먼저 고정한다.; horikawa: 원영상 및 시간계열이 확보되면 clip 내부 사건경계 분석; clip마다 상태를 리셋해야 하는 시행구조 자체와 자연 사건경계를 구분한다.; validation: Spacetop clip 집계 평정은 경계 주변 정서 정답이 아니다. clip-level 요약 관련성만 확인한다. NSD에는 시간 reset 질문을 적용하지 않는다.; fallback: VideoPrism은 frozen clip encoder로만 사용하고 작은 causal state head를 신규 모형으로 명시한다. 관측복구가 실패하면 경계 단서의 예측 충분성만 보고하며 신경 초기화 기전 주장을 하지 않는다.; 독립 사건경계와 컷 구분 / run/clip 경계와 초기 상태 처리 / 연속 정서주석·평정 lag / reset 모델의 분포 이탈 및 창 길이 대조 / theta/h0/rho의 실제 구현·학습예산·reset exposure / 독립 causal 경계검출의 time_available·A 전이 대비 / 복구 가능성 및 관측 파라미터 최적화 동등성
- **근접 연구와 차이:** P089 / P044; 기억 소거의 효과를 경계 단서 전달과 훈련 분포이탈에서 분리하고, 각 모형 관측 파라미터를 재적합한 후에도 필요한 최소 연산인지 검정한다. 기존 BI-RQ08 계열과 공동 설계로 통합한다.
- **중복·신규성 위험:** 사건분절·예측상태 갱신 연구와 중복 가능하며 원래 Agent11 BI-RQ08 계열을 별도 고유 RQ로 이중 집계하지 않는다. 동일 예상 BOLD를 내는 다른 상태 연산은 배제할 수 없다.
- **병합 시 보존한 판정:** 각 원안의 역할 판정은 병합 후에도 보존한다. C05-03: 과학RQ후보
- **원본:** [agents/05_multimodal_dynamics/round04_revision.json](../agents/05_multimodal_dynamics/round04_revision.json); 후보 C05-03
- **근거:** [P089 Deep Predictive Coding Networks for Video Prediction and Unsupervised Learning](https://arxiv.org/abs/1605.08104); [P044 VideoPrism: A Foundational Visual Encoder for Video Understanding](https://arxiv.org/abs/2402.13217); [P034 Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://arxiv.org/abs/2312.00752); [P066 Discovering event structure in continuous narrative perception and memory](https://doi.org/10.1016/j.neuron.2017.06.041); [P002 Emo-FilM: A multimodal dataset for affective neuroscience using naturalistic stimuli](https://doi.org/10.1038/s41597-025-04803-5); [P101 Representational models: A common framework for understanding encoding, pattern-component, and representational-similarity analysis](https://doi.org/10.1371/journal.pcbi.1005508); [P100 Statistical inference on representational geometries](https://doi.org/10.7554/eLife.82566)

| 평가 | 점수 | 이유 | 불확실성 |
|---|---|---|---|
| novelty | 3 | 경계 갱신 선행 및 BI-RQ08과 겹치며 새 요소는 단서×소거 분해다. | 외부 Crossref 역검색 403으로 최신 중복·최초성 미확인. |
| neuro_importance | 4 | 경계 부호화와 과거 상태 감소를 가르는 관찰 대비는 신경 계산 설명에 기여한다. | 관측 신뢰도·대립모형 적합·실제 데이터 효과를 아직 평가하지 않은 E3 판단. |
| ai_necessity | 3 | 상태가 있는 계산 모델은 필요하지만 작은 신규 head로도 검정할 수 있다. | 관측 신뢰도·대립모형 적합·실제 데이터 효과를 아직 평가하지 않은 E3 판단. |
| data_feasibility | 3 | 독립 causal 경계와 연속 정서 대비가 모두 필요한 조건부 설계다. | 실제 경로·버전·주석·체크포인트·연산비는 분석 착수 시 확인. |
| rigor | 4 | reset exposure·초기상태·관측모형을 적합해 주요 대안을 직접 시험한다. | 관측 신뢰도·대립모형 적합·실제 데이터 효과를 아직 평가하지 않은 E3 판단. |
| falsifiability | 4 | indicator-only·유한창·연속모형 우위가 각각 구별되는 부정 결과다. | 관측 신뢰도·대립모형 적합·실제 데이터 효과를 아직 평가하지 않은 E3 판단. |
| interpretability | 3 | 모델 연산 필요성은 해석 가능하지만 뇌 reset 기전으로의 전이는 제한된다. | 관측 신뢰도·대립모형 적합·실제 데이터 효과를 아직 평가하지 않은 E3 판단. |
| generalization | 3 | held-out 영화에 경계 구조와 초기 상태 분포가 달라질 수 있다. | 관측 신뢰도·대립모형 적합·실제 데이터 효과를 아직 평가하지 않은 E3 판단. |
| technical_feasibility | 3 | 작은 causal head 구현은 가능해도 학습 노출·정렬·복구 비용이 남는다. | 실제 경로·버전·주석·체크포인트·연산비는 분석 착수 시 확인. |
| exploration_value | 4 | 연속 누적과 사건별 소거의 최소 계산 설명을 경쟁시킨다. | 관측 신뢰도·대립모형 적합·실제 데이터 효과를 아직 평가하지 않은 E3 판단. |

여덟 탐색 질문의 개별 답과 비판 수용/미해결 이력은 위 구조화 원본에 보존했다.

**실제 Round5 반영 조건:** 모든 주 비교에 같은 경계정보 접근을 주고 강한 연속 boundary×state 대조와 HRF 이후 회복을 요구한다. 미래를 본 경계와 온라인 경계를 구별한다. 명시적 forgetting을 흡수한 exact functional control을 포함하고 관측적으로 같은 모형의 점수 차이는 구현·최적화 차이로 먼저 조사한다.

**철회한 강한 해석:** reset 모델 우세=인간 기억의 실제 소거

평가 점수는 Round4의 역할 판단이다. Round5 조건으로 실제 착수 가능성이 좁아진 경우 현재 점수 자체를 실현성 증명으로 읽지 않는다.

<a id="rq19"></a>
## RQ19. 감각 불일치 조건의 비가산성: 공통 단위 paired risk 검정

동일 frozen 시청각 정보와 공통 출력단위에서 joint readout의 strict additive 대비 이득은 감각 불일치 조건의 독립 정서 신경 대비에서 더 큰가?

- **Axis·유형:** A × B × C × E × H × I × J × M × N × P × Q × R × X; Construct / Stimulus; Inference / Measurement; Model / Method; Neural; Structure / Dynamics
- **모델 적용 → 과학 질문 → 가정 도전:** f_add(A,V,C)=f(A,C)+g(V,C), f_joint=f_add+h(A,V,C)로 함수계열을 명시한다. C는 양쪽에 같은 감각품질·내용 nuisance다. h의 유효 용량 증가에 맞춰 additive의 within-modality 유연성도 늘린 별도 baseline을 둔다. 두 모형은 일치/불일치가 섞인 동일 train 분포에서 적합하고 test에서는 고정한다. → 독립 감각정보 합의 충분성이 일치도 조건에 따라 달라지는지 공통 예측위험 단위에서 비교한다. → 조건별 ΔR²의 차이가 곧 결합규칙 변화라는 가정을 철회한다. nonlinear concatenation은 additive가 아니라 joint이므로 baseline 명칭을 함수에 맞춘다.
- **경쟁 설명:** 내용·감각품질의 공통 지지에서 불일치 조건의 정서 neural paired-loss 이득 D(1)이 일치 조건 D(0)보다 크며 조건별 SNR·표본수 차이만으로 설명되지 않는다. / 조건별 입력난도·희귀성·미측정 관계 의미·noise와 model misspecification이 위험 차이를 만든다. 불일치가 인간 결합규칙을 바꿨다는 인과 설명은 별도다.
- **관측 대비:** train 공통 척도로 정규화한 z_A에 d_i=(z_Ai−f_add_i)^2−(z_Ai−f_joint_i)^2를 계산한다. D(c)=E[d_i|congruence=c, matched support], I=D(1)−D(0)가 주추정량이다. 전체 Y의 같은 손실 차이는 부차 결과다. 조건별 표준화·조건별 R² 분모를 사용하지 않으며 동일 두 모델과 공통 nuisance를 유지한다. 일치도는 독립 관찰자/항목으로 측정한다.
- **반증:** 공통 지지·복잡도·SNR 대조 후 I의 사전 최소 효과 상한이 작으면 조건부 비가산 이득을 지지하지 않는다. I가 전체 BOLD에서만 남고 정서 대비에서는 없으면 정서 RQ 지지 없음. 지지집합이 없으면 영효과가 아닌 식별불가다.
- **기준모형:** f(A,C)+g(V,C)의 strict nonlinear additive / additive 안의 유연성만 늘린 용량 대조 / 동일 features의 명시적 h(A,V,C) joint / 각 감각 단독·품질/의미 baseline / 조건 내 correspondence shuffle은 민감도용이며 새 BOLD 관측이 아님
- **자료·착수 조건:** primary: Horikawa 보유 자극에 실제 동시 시청각 입력과 조건 다양성이 있는지 확인. 없다면 Emo-FilM의 자연 일치/불일치 구간을 대상으로 한다.; annotation: 감각 일치도는 독립 추가 평정이 필요할 수 있다. 정서 평가와 일치도 평가의 주체·시간 단위를 기록하고 AI 일치도 점수를 인간 정답으로 간주하지 않는다.; validation: Spacetop은 실제 clip-level 조건 및 평정 대응만 사용. NSD는 시청각 불일치 연구에 쓰지 않는다. Mind Captioning은 이름만으로 audiovisual 데이터라고 추정하지 않는다.; fallback: 자연 불일치 표본이 충분하지 않으면 추가 자극·실측 fMRI 연구의 제안으로 보류. 오디오를 바꾼 합성 자극에 원래 뇌반응을 붙이지 않는다.; 독립 감각 일치도·정서주석 / 불일치와 저수준/의미 변수의 충분한 겹침 / 각 조건의 효과 식별 가능한 표본수 / Speech Features 제외: 비음성 음악·환경음 구간 선별, 음성 포함 여부는 범위/QC 용도만 사용 / 공통 train 표준화·strict additive 구현 / 일치도와 정서 평가의 독립성 및 matched support / 모형별 유효 자유도·same train/test 고정 검증
- **근접 연구와 차이:** P036 / P038 / P041; Round2의 조건별 R² 차이를 같은 표본의 공통 단위 손실 차이로 재정의하고 정보표현 차이와 결합 함수 차이를 분리했다. 이는 neural fusion 우열이 아니라 조건부 additive 충분성의 검정이다.
- **중복·신규성 위험:** 기존 audiovisual congruence/감각통합과 중복 위험이 크다. 자연 조건의 위험 차이는 입력분포 난도를 완전히 제거하지 못하므로 인간 인과 결합규칙으로 해석하지 않는다.
- **병합 시 보존한 판정:** 각 원안의 역할 판정은 병합 후에도 보존한다. C05-05: 과학RQ후보
- **원본:** [agents/05_multimodal_dynamics/round04_revision.json](../agents/05_multimodal_dynamics/round04_revision.json); 후보 C05-05
- **근거:** [P036 Contrastive Audio-Visual Masked Autoencoder](https://github.com/YuanGongND/cav-mae/tree/master); [P038 Attention Bottlenecks for Multimodal Fusion](https://arxiv.org/abs/2107.00135); [P041 Audio-Visual Event Localization in Unconstrained Videos](https://arxiv.org/abs/1803.08842); [P093 Scaling Vision with Sparse Mixture of Experts](https://arxiv.org/abs/2106.05974); [P100 Statistical inference on representational geometries](https://doi.org/10.7554/eLife.82566); [P101 Representational models: A common framework for understanding encoding, pattern-component, and representational-similarity analysis](https://doi.org/10.1371/journal.pcbi.1005508)

| 평가 | 점수 | 이유 | 불확실성 |
|---|---|---|---|
| novelty | 3 | 시청각 불일치 연구와 가깝고 독립 정서 대비의 additive 충분성에 차별점이 있다. | 외부 Crossref 역검색 403으로 최신 중복·최초성 미확인. |
| neuro_importance | 4 | 언제 가산적 감각정보가 부족한지 조건부로 규정할 수 있다. | 관측 신뢰도·대립모형 적합·실제 데이터 효과를 아직 평가하지 않은 E3 판단. |
| ai_necessity | 2 | 고정 특징과 작은 additive/joint head로 검정 가능해 최신 fusion 모델이 필수는 아니다. | 관측 신뢰도·대립모형 적합·실제 데이터 효과를 아직 평가하지 않은 E3 판단. |
| data_feasibility | 3 | 동시 시청각 입력·독립 일치도 평정·조건 overlap이 확보돼야 한다. | 실제 경로·버전·주석·체크포인트·연산비는 분석 착수 시 확인. |
| rigor | 4 | 공통 train 표준화와 paired loss·strict 함수계열로 분모/용량 혼동을 줄인다. | 관측 신뢰도·대립모형 적합·실제 데이터 효과를 아직 평가하지 않은 E3 판단. |
| falsifiability | 4 | 정서 대비의 조건 상호작용이 최소효과보다 작으면 주가설을 제한한다. | 관측 신뢰도·대립모형 적합·실제 데이터 효과를 아직 평가하지 않은 E3 판단. |
| interpretability | 4 | 예측 위험의 조건 차이는 명료하지만 인간 결합규칙 인과로는 읽지 않는다. | 관측 신뢰도·대립모형 적합·실제 데이터 효과를 아직 평가하지 않은 E3 판단. |
| generalization | 3 | 영화/내용군 보류가 가능하나 희귀 불일치의 지원 범위가 제한될 수 있다. | 관측 신뢰도·대립모형 적합·실제 데이터 효과를 아직 평가하지 않은 E3 판단. |
| technical_feasibility | 4 | 고정 특징 캐시와 소형 readout으로 첫 검증이 가능하다. | 실제 경로·버전·주석·체크포인트·연산비는 분석 착수 시 확인. |
| exploration_value | 4 | 관찰적 통합 주장의 범위를 엄격히 한정하는 음성 결과도 유익하다. | 관측 신뢰도·대립모형 적합·실제 데이터 효과를 아직 평가하지 않은 E3 판단. |

여덟 탐색 질문의 개별 답과 비판 수용/미해결 이력은 위 구조화 원본에 보존했다.

<a id="rq20"></a>
## RQ20. 과거 제한 상태의 신경 충분성과 미래 지향 학습목표의 추가 역할

동일한 현재·과거 입력에서 기억용 압축과 미래 예측용 상태가 독립 정서 대비의 신경반응에 서로 다른 설명력을 제공하는가?

- **Axis·유형:** A × B × C × D × E × H × J × M × Q × V × X; Construct / Stimulus; Inference / Measurement; Model / Method; Neural; Structure / Dynamics
- **모델 적용 → 과학 질문 → 가정 도전:** 같은 prefix·backbone·학습자료·계산예산에서 과거 복원, 순서보존 기억, 실제 미래 예측, target 미래 순열 학습을 비교한다. 공개 JEPA/VideoMAE checkpoint 비교는 후보 선택용이며 목표함수 효과의 본검정은 소형 통제학습이다. → 과거 정보의 이용과 미래 목표에 특수한 정보 보존을 구별한다. prefix-only는 과거 제한성을 뜻하며 미래 예측의 증거가 아니다. → 과거만 본 특징의 우위가 미래 기대라는 가정을 폐기한다. 미래 목표의 이득이 없으면 과거 통합은 유지될 수 있지만 예측 목표 특이성은 지지되지 않는다.
- **경쟁 설명:** 현재·과거 입력과 상태 용량·기억 접근성·학습 선택 예산을 맞춘 조건에서 미래 예측 목표의 상태가 과거 복원/비예측 목표보다 독립 정서 신경 대비를 더 설명한다. 순서 대 bag 차이는 이 목표 비교의 공통 기준이며 별도 일차 가설로 세지 않는다. / 정서 대비는 최근 장면의 가중 평균·사건 순서 기억·장기 의미 압축으로 충분하며 미래 목표는 그 정보를 더 쉽게 읽게 할 뿐이다.
- **관측 대비:** 유일 일차 대비는 동일 prefix 입력·상태/관측모형·선택 예산에서 미래 예측 학습 대 과거 복원/비예측 학습의 독립 정서 신경 대비 예측손실차다. order-aware state 대 recency-weighted bag는 RQ07/RQ29와 공유하는 보조 baseline이다. h_t, 예측 zhat(t+h|t), 입력 도착 후 error e(t+h)의 접근 시점을 구별하며 사후 error를 과거 입력에 넣지 않는다. 같은 자극의 독립 비정서 대비와 미래 target 순열 대조를 함께 평가한다.
- **반증:** 미래 목표의 이득이 기억/순서 기준 또는 미래 target 순열 조건과 실질적 동등 범위면 목표 특이성을 기각한다. oracle만 개선되면 사후 정보 이득으로 제한하며 past-only 우위가 없다고 뇌 예측 자체의 부재를 결론내리지 않는다.
- **기준모형:** 현재-only / 동일 prefix의 recency-weighted bag / 순서보존 causal memory / 동일 backbone의 과거 복원/미래 예측/미래 target 순열 / 미래허용 oracle / 같은 HRF family·입력길이·유효차원
- **자료·착수 조건:** Horikawa 시행평균은 상태 요약 비교로 제한한다. Emo-FilM은 실제 시간정합·별도 평정 코호트와 지연을 명시한 leave-film-out; train/test buffer는 최대 과거창과 HRF 지연 이상으로 설정한다. Spacetop의 clip 평정은 clip 수준 검정이며 연속 정서 궤적으로 취급하지 않는다.; 연속 BOLD와 HRF 모델에 충분한 run 길이 여부 / prefix-only feature 추출 구현 및 미래 token 접근 감사 / 자극 timing·motion·독립 정서 주석 정렬 / 모델 학습데이터·구조가 다른 비교의 식별 한계 / 목표함수 통제 소형 학습의 입력/예산 고정 / 과거 기억과 다음 사건 구별을 독립 probe로 측정할 공통 지지 / raw time에서 HRF 후 두 상태 효과 회복가능성
- **근접 연구와 차이:** P008 / P046 / P066; 영상모델 적용 자체가 아니라 현재 내용·복원·과거 상태를 분리하고 독립 정서 대비에서 필요한 정보를 규정하는 실험적 대립이다.
- **중복·신규성 위험:** Kragel2019의 recurrent feedback 및 기존 시간적 encoding과 중복 가능. 최근 원문 역검색 미실행으로 신규성 미확정.
- **병합 시 보존한 판정:** 각 원안의 역할 판정은 병합 후에도 보존한다. C06-01: 과학RQ후보
- **원본:** [agents/06_frontier_ai/round04_revision.json](../agents/06_frontier_ai/round04_revision.json); 후보 C06-01
- **근거:** [P046 Revisiting Feature Prediction for Learning Visual Representations from Video](https://arxiv.org/abs/2404.08471); [P045 VideoMAE: Masked Autoencoders are Data-Efficient Learners for Self-Supervised Video Pre-Training](https://arxiv.org/abs/2203.12602); [P013 V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning](https://raw.githubusercontent.com/facebookresearch/vjepa2/main/README.md); [P008 Emotion schemas are embedded in the human visual system](https://doi.org/10.1126/sciadv.aaw4358); [P066 Discovering event structure in continuous narrative perception and memory](https://doi.org/10.1016/j.neuron.2017.06.041)

| 평가 | 점수 | 이유 | 불확실성 |
|---|---|---|---|
| novelty | 3 | 기억 대 미래 목표의 동일 입력 대비는 구체적이나 시간적 encoding 선행과 중복 위험이 남는다. | 설계 기반 잠정평가; 신규 외부 역검색 미실행으로 최초성 미확정. |
| neuro_importance | 5 | 현재 내용과 시간 맥락의 기능적 역할을 구별한다. | 설계 기반 잠정평가; 효과·검정력·통제의 실제 성립은 분석 미실행으로 미확인. |
| ai_necessity | 4 | 영상 상태의 목표함수 조절이 필요하나 단순 causal memory가 충분할 가능성도 남긴다. | 설계 기반 잠정평가; 단순 기준이 충분하면 최신 AI 필요성 축소. |
| data_feasibility | 3 | 보유 영상으로 요약 비교가 가능하지만 시간주석·prefix 경로는 미확인이다. | 설계 기반 잠정평가; 사용자 보유 진술과 현재 접근·필드 검증을 구별. |
| rigor | 4 | time_available과 동일 예산 목표 대조를 명시해 핵심 누출을 차단한다. | 설계 기반 잠정평가; 효과·검정력·통제의 실제 성립은 분석 미실행으로 미확인. |
| falsifiability | 4 | 목표 특이성의 실패와 낮은 관측 검출력을 별도 판정한다. | 설계 기반 잠정평가; 효과·검정력·통제의 실제 성립은 분석 미실행으로 미확인. |
| interpretability | 3 | BOLD 대응에서 인간의 실제 예측 계산까지 해석하기는 어렵다. | 설계 기반 잠정평가; 효과·검정력·통제의 실제 성립은 분석 미실행으로 미확인. |
| generalization | 4 | 영화/내용군 유보와 목표 대조로 범위를 확장한다. | 설계 기반 잠정평가; 효과·검정력·통제의 실제 성립은 분석 미실행으로 미확인. |
| technical_feasibility | 3 | 소형 통제학습과 시간 회복 모의실험 비용이 남는다. | 설계 기반 잠정평가; checkpoint·코드·실행경로 미검증. |
| exploration_value | 5 | 미래 기대와 일반 기억을 구별하는 결과는 양성·음성 모두 가치가 크다. | 설계 기반 잠정평가; 효과·검정력·통제의 실제 성립은 분석 미실행으로 미확인. |

여덟 탐색 질문의 개별 답과 비판 수용/미해결 이력은 위 구조화 원본에 보존했다.

**최종 독립 감사의 범위 제한:** 동일 과거 입력·상태용량·선택예산에서 미래 예측 학습목표의 정서 관련 신경 대비 접근성이 복원/비예측 목표와 다른지에 한정. 순서 교환·이력 충분성 자체는 RQ07/RQ29의 공통 대조로 링크하며 별도 기여로 중복 집계하지 않음.

<a id="rq21"></a>
## RQ21. 촬영·사건 metadata 억제에 따른 정서 대비의 선택적 손실 곡선

같은 자극과 피험자에서 촬영 metadata와 사건 metadata의 억제가 독립 정서 대비와 비정서 대비의 예측에 서로 다른 손실 곡선을 만드는가?

- **Axis·유형:** A × B × C × F × H × I × J × K × O × P × Q × R × S × T × X; Construct / Stimulus; Inference / Measurement; Model / Method; Neural; Structure / Dynamics
- **모델 적용 → 과학 질문 → 가정 도전:** 동일 backbone에서 이름이 확인된 촬영·사건 metadata별 보존/억제 강도를 바꾸고 sham 및 복원 손상 기준을 둔다. metadata probe 실패를 정보 부재나 같은 정보량의 증명으로 사용하지 않는다. → 정서 대비 예측에 필요한 내용과 제거 가능한 내용이 관측적으로 구별되는지를 동일 자극의 선택적 손실로 묻는다. → 내용 제거가 순수 정서를 남긴다는 가정과 촬영 정보는 자동으로 무관하다는 가정을 동시에 시험한다.
- **경쟁 설명:** 일반 시각 손상·복원 손실의 공통 구간에서 사건 metadata 억제의 정서 대비 추가 손실이 촬영 metadata 억제보다 크다. 반대·동등 결과도 허용한다. / 차이는 guide의 제거 난도·남은 의미·대비 신뢰도·일반 표현손상으로 설명되며 metadata 유형 자체의 선택성이 없다.
- **관측 대비:** 동일 자극/참가자에서 L(g,s,a)=score(frozen,a)−score(suppression(g,s),a)로 정의한다. 주대비 D(s)=[L(사건,s,정서)−L(사건,s,비정서)]−[L(촬영,s,정서)−L(촬영,s,비정서)]. 대비 score는 동일 metric에서 신뢰도와 난도를 맞추고 원효과/불확실성도 함께 제시한다. 공통 손상 구간 밖은 외삽하지 않는다.
- **반증:** D(s)가 실질적 동등 범위이거나 의미·복원손상·sham 조절로 사라지면 선택성 가설을 기각한다. 모든 metadata 억제가 양쪽 대비를 줄이면 보편 nuisance 선언을 폐기한다.
- **기준모형:** frozen backbone / ERM / 외부환경 유보 IRM / guide label permutation / 동일 rank 무작위 정보 제거 / 의미 특징을 포함/제외한 민감도 분석
- **자료·착수 조건:** 주검정은 Horikawa 등 동일 자극·동일 참가자·동일 신경자료 안의 정서/비정서 대비다. NSD는 외부 방법 재현으로만 사용하며 두 자료의 점수를 직접 빼서 선택성을 주장하지 않는다. metadata와 독립 정서 대비의 overlap가 없는 strata는 적용범위에서 명시적으로 제외한다.; 독립적으로 정의할 촬영 양식·사건 맥락 metadata / 정서 주석과 환경의 충분한 교차 및 공통 지지집합 / FINO checkpoint/guide 경로 확인 / nuisance 명칭이 실제 무관성을 보장하지 않음
- **근접 연구와 차이:** P049 / P050 / P007; 일반화 점수의 최대화 대신 제거 가능한 환경과 유지되어야 하는 맥락의 비대칭 신경 손실을 설명 대상으로 삼는다.
- **중복·신규성 위험:** 기존 domain-general representation 및 context-dependent affect와 중복 가능. 명확한 2×2 신경 대비가 없으면 단순 adaptation benchmark로 격하.
- **병합 시 보존한 판정:** 각 원안의 역할 판정은 병합 후에도 보존한다. C06-02: 과학RQ후보; C12-02: 과학RQ후보; C06-04: 과학RQ후보
- **원본:** [agents/06_frontier_ai/round04_revision.json](../agents/06_frontier_ai/round04_revision.json); 후보 C06-02, C12-02, C06-04
- **근거:** [P049 Invariant Risk Minimization](https://arxiv.org/abs/1907.02893); [P050 Who Needs Labels? Adapting Vision Foundation Models With the Metadata You Already Have](https://arxiv.org/abs/2606.05107); [P001 The neural representation of visually evoked emotion is high-dimensional, categorical, and distributed across transmodal brain regions](https://doi.org/10.1016/j.isci.2020.101060); [P007 Generalizable representations of pain, cognitive control, and negative emotion in medial frontal cortex](https://doi.org/10.1038/s41593-017-0051-7); [P008 Emotion schemas are embedded in the human visual system](https://doi.org/10.1126/sciadv.aaw4358); [P100 Statistical inference on representational geometries](https://doi.org/10.7554/eLife.82566); [P102 Conditional independence testing based on a nearest-neighbor estimator of conditional mutual information](https://proceedings.mlr.press/v84/runge18a.html); [P051 Similarity of Neural Network Representations Revisited](https://proceedings.mlr.press/v97/kornblith19a.html); [P098 WILDS: A Benchmark of in-the-Wild Distribution Shifts](https://proceedings.mlr.press/v139/koh21a.html); [P099 In Search of Lost Domain Generalization](https://arxiv.org/abs/2007.01434)

| 평가 | 점수 | 이유 | 불확실성 |
|---|---|---|---|
| novelty | 3 | C12-02와 직접 겹쳐 통합해야 하며 독립 새 방향으로 중복 세지 않는다. | 설계 기반 잠정평가; 신규 외부 역검색 미실행으로 최초성 미확정. |
| neuro_importance | 4 | 내용 제거와 정서 대비의 관계는 표상 구성 설명에 중요하다. | 설계 기반 잠정평가; 효과·검정력·통제의 실제 성립은 분석 미실행으로 미확인. |
| ai_necessity | 3 | metadata 억제가 대조를 제공하나 더 단순한 feature 제거로도 일부 검정 가능하다. | 설계 기반 잠정평가; 단순 기준이 충분하면 최신 AI 필요성 축소. |
| data_feasibility | 3 | 동일 자료의 두 대비와 metadata 교차가 필요하다. | 설계 기반 잠정평가; 사용자 보유 진술과 현재 접근·필드 검증을 구별. |
| rigor | 4 | 동일 자극 interaction과 total/conditional 구분이 강점이다. | 설계 기반 잠정평가; 효과·검정력·통제의 실제 성립은 분석 미실행으로 미확인. |
| falsifiability | 4 | 선택성의 실질적 영효과와 일반 손상 설명을 판별한다. | 설계 기반 잠정평가; 효과·검정력·통제의 실제 성립은 분석 미실행으로 미확인. |
| interpretability | 3 | 손상량 완전 매칭과 의미 공통분산의 유일 분리가 어렵다. | 설계 기반 잠정평가; 효과·검정력·통제의 실제 성립은 분석 미실행으로 미확인. |
| generalization | 3 | 공통 지지와 검증한 metadata 범위에 제한된다. | 설계 기반 잠정평가; 효과·검정력·통제의 실제 성립은 분석 미실행으로 미확인. |
| technical_feasibility | 3 | 공식 guide 문서는 있지만 현재 checkpoint 호환은 미확인이다. | 설계 기반 잠정평가; checkpoint·코드·실행경로 미검증. |
| exploration_value | 4 | 무엇을 nuisance로 볼지 사전 가정하지 않는 비교가 유용하다. | 설계 기반 잠정평가; 효과·검정력·통제의 실제 성립은 분석 미실행으로 미확인. |

여덟 탐색 질문의 개별 답과 비판 수용/미해결 이력은 위 구조화 원본에 보존했다.

<a id="rq23"></a>
## RQ23. 훈련에서 식별한 공유 관계 연산은 보지 않은 내용–정서 조합으로 전이되는가

훈련 조합들에서 공유 연산이 회복 가능한 조건에서, 알려진 성분의 보지 않은 조합에 대한 신경 대비를 가산 구성보다 공유 bilinear 관계모형이 더 잘 예측하는가?

- **Axis·유형:** A × B × C × E × F × H × J × K × M × O × Q × R × S × T × X; Construct / Stimulus; Inference / Measurement; Model / Method; Neural; Structure / Dynamics
- **모델 적용 → 과학 질문 → 가정 도전:** 각 성분 a의 외부 고정 또는 train-only embedding u(a)와 성분 b의 v(b)를 사용한다. yhat(a,b)=α+f(u(a))+g(v(b))+W[(Uu(a))⊙(Vv(b))]의 U,V,W를 모든 train pair에서 공유하고 test pair별 자유계수는 두지 않는다. 같은 유효복잡도의 성분 내부 비선형과 비교한다. → 새 조합의 신경 대비를 설명하는 데 재사용 가능한 관계 연산이 필요한지, 관측한 성분의 가산/내부 비선형 재사용으로 충분한지 구별한다. → 보지 않은 pair를 임의 interaction으로 예측할 수 있다는 가정을 삭제한다. 구조적 지지가 있는 경우의 실패만 관계 가설의 반증 자료로 쓴다.
- **경쟁 설명:** 동일 설계의 synthetic recovery가 가능한 범위에서 공유 관계모형이 가산·성분 내부 비선형보다 unseen-pair 정서 신경 대비를 더 잘 예측한다. / 강한 가산/내부 비선형으로 충분하거나, 관계모형 이득이 내용관계 OOD·motion·주석 집계·추정조건수 차이에서 생긴다.
- **관측 대비:** 새 pair와 기존 pair의 새로운 자극을 각각 test로 두고 동일 원자 marginal 범위·내용거리·duration·주석 신뢰도로 맞춘다. 주추정은 공동 U,V,W 모형 대 같은 복잡도의 가산/내부 비선형 모형의 unseen-pair ΔR²이며, 같은 자극의 비정서 대비에서 생기는 일반 조합 이득도 보고한다.
- **반증:** 실제 split·noise에서 알려진 shared-bilinear 신호가 회복되고 additive false-positive가 교정된 효과범위에서 ΔR²가 동등 범위면 선택한 관계 연산의 필요성을 낮춘다. recovery 실패나 설계 rank 결손이면 실행 설계를 보류하며 가산 뇌 코드의 증거로 쓰지 않는다.
- **기준모형:** 성분 가산 모형 / 같은 복잡도의 성분 내부 비선형 / dense vision/semantic encoding / 빈도·거리 일치 조합 유보 / 주석 측정오차 모형 / 지역 제한/분산 가산/통계 상호작용의 분리
- **자료·착수 조건:** Horikawa 실제 다범주 주석과 내용 성분으로 support graph를 만들되 ontology는 외부 또는 train 주석으로 고정한다. 독립 평가자 집합이 있으면 test 정서 대비를 따로 구성하며 없으면 집계 주석 기반 조건부 분석으로 제한한다. Mind Captioning의 정체/주석을 추정하지 않는다.; 충분한 조합 수와 성분별 관측 범위 / 주석이 개별 평가인지 집계인지 확인 / 고정 조합 ontology와 독립 train/test split / 관측 fMRI interaction을 신경 인과 coupling으로 읽지 않을 것 / 공유 bilinear design의 rank/conditioning과 recovery 게이트 / 독립 test 주석이 없을 때 결과 범위 제한 / 새 pair 및 기존 pair test의 관계 의미 거리 매칭
- **근접 연구와 차이:** P001 / P008 / P083; 범주 수나 비선형 정확도를 비교하는 대신 성분은 관측했지만 관계는 보지 못한 평가에서 재사용 가능한 신경 연산의 충분성을 판별한다.
- **중복·신규성 위험:** Agent02 U2와 직접 겹치는 문제를 AI 조합 유보/성분 내부 비선형 통제로 구체화한 공동 후보이며 독립 원안으로 이중 집계하지 않는다. compositional emotion 연구 역검색은 남아 있다.
- **병합 시 보존한 판정:** 각 원안의 역할 판정은 병합 후에도 보존한다. C06-05: 과학RQ후보; C01-01: 과학RQ후보; C10-05: 과학RQ후보; C12-01: 과학RQ후보
- **원본:** [agents/06_frontier_ai/round04_revision.json](../agents/06_frontier_ai/round04_revision.json); 후보 C06-05, C01-01, C10-05, C12-01
- **근거:** [P001 The neural representation of visually evoked emotion is high-dimensional, categorical, and distributed across transmodal brain regions](https://doi.org/10.1016/j.isci.2020.101060); [P008 Emotion schemas are embedded in the human visual system](https://doi.org/10.1126/sciadv.aaw4358); [P009 Common and stimulus-type-specific brain representations of negative affect](https://doi.org/10.1038/s41593-022-01082-w); [P083 Concept Bottleneck Models](https://raw.githubusercontent.com/mlresearch/v119/gh-pages/koh20a/koh20a.pdf); [P055 Variational Autoencoders and Nonlinear ICA: A Unifying Framework](https://proceedings.mlr.press/v108/khemakhem20a.html); [P100 Statistical inference on representational geometries](https://doi.org/10.7554/eLife.82566); [P101 Representational models: A common framework for understanding encoding, pattern-component, and representational-similarity analysis](https://doi.org/10.1371/journal.pcbi.1005508); [P015 MindEye2: Shared-Subject Models Enable fMRI-To-Image With 1 Hour of Data](https://arxiv.org/abs/2403.11207); [P051 Similarity of Neural Network Representations Revisited](https://proceedings.mlr.press/v97/kornblith19a.html); [P093 Scaling Vision with Sparse Mixture of Experts](https://arxiv.org/abs/2106.05974); [P098 WILDS: A Benchmark of in-the-Wild Distribution Shifts](https://proceedings.mlr.press/v139/koh21a.html); [P062 neuromaps: structural and functional interpretation of brain maps](https://doi.org/10.1038/s41592-022-01625-w); [P079 Learning Transferable Visual Models From Natural Language Supervision](https://raw.githubusercontent.com/mlresearch/v139/gh-pages/radford21a/radford21a.pdf); [P076 Diffusion Posterior Sampling for General Noisy Inverse Problems](https://github.com/DPS2022/diffusion-posterior-sampling); [P007 Generalizable representations of pain, cognitive control, and negative emotion in medial frontal cortex](https://doi.org/10.1038/s41593-017-0051-7); [P049 Invariant Risk Minimization](https://arxiv.org/abs/1907.02893); [P053 Challenging Common Assumptions in the Unsupervised Learning of Disentangled Representations](https://proceedings.mlr.press/v97/locatello19a.html)

| 평가 | 점수 | 이유 | 불확실성 |
|---|---|---|---|
| novelty | 3 | 구성 일반화와 혼합 정서 선행의 중복 위험이 남으며 새 pair 구조가 차별 후보다. | 설계 기반 잠정평가; 신규 외부 역검색 미실행으로 최초성 미확정. |
| neuro_importance | 5 | 성분 재사용과 관계 계산의 필요성은 정서 코드 설명에 직접 관련된다. | 설계 기반 잠정평가; 효과·검정력·통제의 실제 성립은 분석 미실행으로 미확인. |
| ai_necessity | 3 | 공유 관계모형은 필요하지만 소형 통계 bilinear도 가능해 frontier AI 필수성은 낮다. | 설계 기반 잠정평가; 단순 기준이 충분하면 최신 AI 필요성 축소. |
| data_feasibility | 2 | 실제 조합 support·독립 평정·조건수가 아직 확인되지 않았다. | 설계 기반 잠정평가; 사용자 보유 진술과 현재 접근·필드 검증을 구별. |
| rigor | 4 | 예측식과 회복 gate로 미관측 자유계수 문제를 해소하는 설계를 정의했다. | 설계 기반 잠정평가; 효과·검정력·통제의 실제 성립은 분석 미실행으로 미확인. |
| falsifiability | 4 | 식별 가능한 효과범위에서만 관계 필요성의 영효과를 해석한다. | 설계 기반 잠정평가; 효과·검정력·통제의 실제 성립은 분석 미실행으로 미확인. |
| interpretability | 3 | 저랭크 연산이 뇌의 실제 구조라는 해석은 허용하지 않는다. | 설계 기반 잠정평가; 효과·검정력·통제의 실제 성립은 분석 미실행으로 미확인. |
| generalization | 4 | 알려진 성분의 새 pair라는 명시적 구조 일반화를 평가한다. | 설계 기반 잠정평가; 효과·검정력·통제의 실제 성립은 분석 미실행으로 미확인. |
| technical_feasibility | 3 | 작은 공유 모형은 구현 가능하나 simulation과 support 감사가 선행한다. | 설계 기반 잠정평가; checkpoint·코드·실행경로 미검증. |
| exploration_value | 5 | 지원 가능한 조합이 있다면 신경 구성 원리를 가르는 잠재력이 크다. | 설계 기반 잠정평가; 효과·검정력·통제의 실제 성립은 분석 미실행으로 미확인. |

여덟 탐색 질문의 개별 답과 비판 수용/미해결 이력은 위 구조화 원본에 보존했다.

<a id="rq24"></a>
## RQ24. HRF 가정하 정서 문맥 대비의 피질 분포와 시간모형의 식별 경계

지정 HRF family와 정서 입력이력을 고정했을 때 자극 문맥 길이에 따른 정서 주석 추가예측 대비는 독립 cortical gradient와 어떻게 관계하는가?

- **Axis·유형:** C × D × E × F × H × I × N × Q × V × X; Construct / Stimulus; Inference / Measurement; Model / Method; Neural; Structure / Dynamics
- **모델 적용 → 과학 질문 → 가정 도전:** 동일 현재 자극·과거 문맥 길이 L을 갖는 M_X(L)와 M_X(L)+A_fixed를 비교한다. 일차 A_fixed는 자극시점 현재 주석 A_t이며 모든 모형에서 같은 HRF family로 관측화한다. 고정 길이 H의 과거 A는 독립 이차 분석이며 L과 함께 늘리지 않는다. → 정서 주석과 연관된 문맥 예측정보의 공간분포 및 HRF·neural-history 분해의 식별 한계를 구분한다. → BOLD 합성커널의 예측우위가 HRF와 신경필터 각각의 고유 시간상수를 정한다는 가정을 반박한다.
- **경쟁 설명:** Δ_A(L)=R[M_X(L)]−R[M_X(L)+A_fixed]의 L에 따른 변화는 독립 gradient 위치와 관계하며 지정한 관측모형과 회복 가능한 범위에서 재현된다. 방향은 개발자료 선택 대신 사전 양측 검정으로 고정한다. / 동일 합성커널의 다른 HRF/신경필터 분해, 자극 저주파·주석 의미 공유·지역 SNR이 관측 대비를 설명한다.
- **관측 대비:** 주추정량은 Δ_A(long)−Δ_A(short)와 고정 gradient의 관계이며 Δ_A의 감소도 긴 문맥 X가 A와 공유한 정보를 설명한 결과로 보고한다. 전체 예측 이득과 A의 조건부 이득을 분리하며 순수정서라 명명하지 않는다.
- **반증:** 독립 HRF 제약과 회복 simulation에서 식별력을 확보한 영역에서만 추가 문맥 필요성의 동등성을 평가한다. 동일 BOLD를 내는 convolution 동치쌍을 구별했다면 파이프라인을 기각한다. 유연한 HRF에서 효과 소실만으로 신경 통합 부재를 주장하지 않는다.
- **기준모형:** 짧은 신경필터+넓은 HRF와 긴 필터+좁은 HRF의 동일 합성커널 쌍 / neural history 유무×지역 HRF 차이 유무 2×2 회복 / 현재입력 일치·과거 이력 상이한 held-out 대비 / native TR의 FIR/과거전용 문맥 모형 / gradient 부호 고정·근접 고유값 부분공간 민감도
- **자료·착수 조건:** primary: Emo-FilM 보유본에서 연속 BOLD·자극 onset·시간 주석을 확인할 때 우선; horikawa: 연속 신호 및 주석 시간격자가 확인되는 범위에만 적용; 시행 beta 순서를 연속 시간으로 만들지 않음; other_owned: Spacetop의 clip 평정을 연속 궤적으로 간주하지 않음; NSD/Mind Captioning은 연속성 미확인으로 시간 질문 적용 보류; 원 TR·HRF 추정 범위·run 경계 / 시간 정서 주석의 실제 척도와 해상도 / 개인 gradient의 독립 추정 자료 또는 고정 외부 atlas / Brain-Mamba 공식 코드 가용성 미확인: 원리 검정은 작은 고정/선택적 SSM 또는 문맥 ridge로 대체 / 독립 HRF 제약의 존재와 허용범위; 없으면 생리적 필터 분해 결론 제외 / 정서 이력 H와 자극 문맥 L을 독립 고정한 설계 / 각 HRF/이력 모의조건의 회복력; 모의결과 미실행
- **근접 연구와 차이:** P066 / P068 / P028; 원래 신경 통합시간 지도 주장을 철회하고 명시된 주석 입력범위의 문맥 상호작용과 관측모형 동치류를 평가한다.
- **중복·신규성 위험:** temporal receptive window 및 자연주의 정서 encoding과 중복 가능. gradient 상관만 남으면 기존 연구의 반복이다.
- **병합 시 보존한 판정:** 각 원안의 역할 판정은 병합 후에도 보존한다. C08-02: 과학RQ후보
- **원본:** [agents/08_systems_neuroscience/round04_revision.json](../agents/08_systems_neuroscience/round04_revision.json); 후보 C08-02
- **근거:** [P028 Brain-Mamba: Encoding Brain Activity via Selective State Space Models](https://proceedings.mlr.press/v248/behrouz24a.html); [P051 Similarity of Neural Network Representations Revisited](https://proceedings.mlr.press/v97/kornblith19a.html); [P053 Challenging Common Assumptions in the Unsupervised Learning of Disentangled Representations](https://proceedings.mlr.press/v97/locatello19a.html); [P061 BrainSpace: a toolbox for the analysis of macroscale gradients in neuroimaging and connectomics datasets](https://doi.org/10.1038/s42003-020-0794-7); [P063 Comparing spatial null models for brain maps](https://doi.org/10.1016/j.neuroimage.2021.118052); [P066 Discovering event structure in continuous narrative perception and memory](https://doi.org/10.1016/j.neuron.2017.06.041); [P068 Neurophysiological signatures of cortical micro-architecture](https://doi.org/10.1038/s41467-023-41689-6)

| 평가 | 점수 | 이유 | 불확실성 |
|---|---|---|---|
| novelty | 3 | 시간통합 선행과 가깝고 새 부분은 주석이력 고정 문맥 대비다. | 실험 미실행·보유본 스키마 및 가까운 신규문헌 전수검색 미완료를 반영한 잠정 판단 |
| neuro_importance | 4 | 생리 시간해석의 식별 경계를 제약하는 의미가 크다. | 실험 미실행·보유본 스키마 및 가까운 신규문헌 전수검색 미완료를 반영한 잠정 판단 |
| ai_necessity | 2 | 문맥 ridge와 FIR로 상당 부분 검증 가능하다. | 실험 미실행·보유본 스키마 및 가까운 신규문헌 전수검색 미완료를 반영한 잠정 판단 |
| data_feasibility | 2 | 독립 HRF 정보와 연속 주석·신호가 미확인이다. | 실험 미실행·보유본 스키마 및 가까운 신규문헌 전수검색 미완료를 반영한 잠정 판단 |
| rigor | 4 | 동일 합성커널과 2×2 회복으로 반증 규칙 자체를 검증한다. | 실험 미실행·보유본 스키마 및 가까운 신규문헌 전수검색 미완료를 반영한 잠정 판단 |
| falsifiability | 3 | 관측 대비는 반증 가능하나 생리 필터 분해는 여전히 조건부다. | 실험 미실행·보유본 스키마 및 가까운 신규문헌 전수검색 미완료를 반영한 잠정 판단 |
| interpretability | 3 | estimand는 명확하지만 HRF와 neural-history 동치가 남는다. | 실험 미실행·보유본 스키마 및 가까운 신규문헌 전수검색 미완료를 반영한 잠정 판단 |
| generalization | 3 | held-out 영화가 가능하나 충분한 길이/내용 변이 필요하다. | 실험 미실행·보유본 스키마 및 가까운 신규문헌 전수검색 미완료를 반영한 잠정 판단 |
| technical_feasibility | 3 | 작은 시계열 모형은 가능하나 회복·gradient 불확실성 계산이 필요하다. | 실험 미실행·보유본 스키마 및 가까운 신규문헌 전수검색 미완료를 반영한 잠정 판단 |
| exploration_value | 4 | 효과의 부재와 비식별을 구분하는 새로운 측정설계로 이어질 수 있다. | 실험 미실행·보유본 스키마 및 가까운 신규문헌 전수검색 미완료를 반영한 잠정 판단 |

여덟 탐색 질문의 개별 답과 비판 수용/미해결 이력은 위 구조화 원본에 보존했다.

<a id="rq25"></a>
## RQ25. 같은 내용 입력에서 gate·오차 계산 좌표는 정서 대비의 판독 효율을 바꾸는가

같은 완전한 입력정보에 gate 또는 오차의 결정적 계산 좌표를 부가할 때, 제한된 readout·표본 예산에서 정서 대비의 접근성 변화가 난도를 맞춘 비정서 대비와 어떻게 다르며 가역 재매개변수화에도 유지되는가?

- **Axis·유형:** A × B × C × D × E × F × H × I × J × L × M × N × P × Q × R × T × V × X; Construct / Stimulus; Inference / Measurement; Model / Method; Neural; Structure / Dynamics
- **모델 적용 → 과학 질문 → 가정 도전:** 선택되지 않은 expert 출력까지 가능한 범위에서 계산하고 pre-gate 입력, logits/dispatch, drop token과 load를 기록한다. 내용 해상도를 증가시키며 gate의 조건부 접근성 곡선을 추정한다. → 독립 routing 정보의 존재가 아니라 같은 입력의 어떤 기능적 좌표가 정서 대비 예측에 경제적인가? → 불완전한 내용 요약 대비 gate 이득을 뇌의 routing 정보로 읽지 않는다.
- **경쟁 설명:** 동일 완전입력의 gate 또는 오차 계산좌표가 제한된 함수족·학습량 범위에서 정서 대비의 판독 효율을 바꾸며, 그 선택성은 비정서 대비·가역 재표현 대조 후에도 평가할 수 있다. 정보 추가나 신경 구현의 동일성 주장이 아니다. / 미선택 expert·관계 의미의 누락, gate×출력의 추가 비선형성, load/위치 통계가 이득을 설명한다.
- **관측 대비:** gate_coordinate_branch: 같은 보류 정서 신경 대비에서 내용 해상도×readout 예산별 예측손실 차이를 구한다. pre-gate 입력의 유연한 attention 재가중 baseline을 추가한다. 출력/과제손상 허용범위 내 대체 routing이 실제로 구성되는 경우에만 route invariance를 비교한다.; error_coordinate_branch: 동일 train/test와 각 표본수 n에서 사전 정서 대비의 평균제곱 예측손실 차이를 측정한다. 파라미터/계산예산 고정 곡선과 충분한 함수족의 포화곡선을 분리한다. [E+,E−]와 [E,abs(E)]는 서로 결정되는 재표현 대조로 사용한다.
- **반증:** gate_coordinate_branch: 완전 내용과 유연한 readout에서 이득이 소멸하면 별도 정보 주장을 배제한다. 제한 예산의 효율도 소멸하거나 출력 동등 routing에서 통계가 불안정하면 안정된 route 좌표 해석을 보류한다.; error_coordinate_branch: 충분한 readout에서 차이 소멸은 독립 정보 가설의 반증과 일치하며 예상 가능한 결과다. 제한 예산에서도 선택적 이득이 없거나 일반 시각 대비와 같으면 정서 관련 효율 가설을 축소한다.
- **기준모형:** gate_coordinate_branch: pre-gate 입력의 비선형 readout / all-expert content와 attention 가중합 / 부하/top-k/패치수 고정 / 동일 출력 대체 routing: 존재 확인 후 적용 / 유사 입력의 분포 내 gate 교환·손상량 일치 대조; error_coordinate_branch: A+Ahat+R를 모두 보는 동일 비선형 함수족 / 원 입력에서 고정 오차변환을 계산하는 정확 동등 경로 / 상태·절대오차·방향오차를 동일 입력정보로 비교 / 가역 오차 좌표 재표현 / 명도·색·사건관계 일치 자극 및 신뢰도 일치 비정서 대비
- **자료·착수 조건:** Horikawa의 정서 대비와 자극별 반응을 우선 후보로 둔다. 시청각 확장은 Emo-FilM/Spacetop의 실제 modality 확인 뒤 수행한다. 원 V-MoE는 이미지 routing이며 시간 gate가 이미 구현됐다고 가정하지 않는다.; 자극/신경/정서 주석 연결 / 현재 checkpoint와 논문판 코드 차이 / 공유/고유 분해의 fold 내부 학습과 seed 안정성 / 미선택 expert를 포함한 텐서 추출 비용 / 출력 동등 재routing 존재 여부; 없으면 불가능 상태로 기록 / 독립 자극에서 gate 교환의 분포 적합성
- **근접 연구와 차이:** P093 / P037; 원안의 gate 고유정보를 철회하고 완전 입력 아래 기능적 좌표의 접근성·동등 재routing 안정성으로 수정했다.
- **중복·신규성 위험:** 높음: 조건부 계산 해석과 신경 encoding 조합의 중복 가능. expert-ROI 대응 자체는 신규성 근거로 삼지 않는다.
- **병합 시 보존한 판정:** C08-05: 방법후보; C11-02: 과학RQ후보; C11-01: 과학RQ후보
- **원본:** [agents/11_brain_inspired/round04_revision.json](../agents/11_brain_inspired/round04_revision.json); 후보 C08-05, C11-02, C11-01
- **근거:** [P028 Brain-Mamba: Encoding Brain Activity via Selective State Space Models](https://proceedings.mlr.press/v248/behrouz24a.html); [P029 Brain-JEPA: Brain Dynamics Foundation Model with Gradient Positioning and Spatiotemporal Masking](https://arxiv.org/abs/2409.19407); [P051 Similarity of Neural Network Representations Revisited](https://proceedings.mlr.press/v97/kornblith19a.html); [P053 Challenging Common Assumptions in the Unsupervised Learning of Disentangled Representations](https://proceedings.mlr.press/v97/locatello19a.html); [P061 BrainSpace: a toolbox for the analysis of macroscale gradients in neuroimaging and connectomics datasets](https://doi.org/10.1038/s42003-020-0794-7); [P093 Scaling Vision with Sparse Mixture of Experts](https://arxiv.org/abs/2106.05974); [P037 Factorized Contrastive Learning: Going Beyond Multi-view Redundancy](https://arxiv.org/abs/2306.05268); [P038 Attention Bottlenecks for Multimodal Fusion](https://arxiv.org/abs/2107.00135); [P089 Deep Predictive Coding Networks for Video Prediction and Unsupervised Learning](https://arxiv.org/abs/1605.08104); [P046 Revisiting Feature Prediction for Learning Visual Representations from Video](https://arxiv.org/abs/2404.08471); [P096 Predictive Coding Approximates Backprop along Arbitrary Computation Graphs](https://arxiv.org/abs/2006.04182)

| 평가 | 점수 | 이유 | 불확실성 |
|---|---|---|---|
| novelty | 2 | gate 해석 선행과 근접하여 최초성은 미확정이다. | 잠정 설계 평가; 신규성 역검색은 GitHub 제한 검색이고 원자료·checkpoint·모델 실행은 미검증 |
| neuro_importance | 3 | 내용 대 기능 좌표의 범위를 좁히지만 뇌 routing은 식별하지 않는다. | 잠정 설계 평가; 신규성 역검색은 GitHub 제한 검색이고 원자료·checkpoint·모델 실행은 미검증 |
| ai_necessity | 3 | 명시 gate 추출이 필요하나 강한 내용 재가중으로 대체될 수 있다. | 잠정 설계 평가; 신규성 역검색은 GitHub 제한 검색이고 원자료·checkpoint·모델 실행은 미검증 |
| data_feasibility | 2 | all-expert 추출과 독립 정서 대비의 실제 조건이 미확인이다. | 잠정 설계 평가; 신규성 역검색은 GitHub 제한 검색이고 원자료·checkpoint·모델 실행은 미검증 |
| rigor | 3 | 완전 입력을 넣었지만 대체 routing 존재 및 손상 매칭이 어렵다. | 잠정 설계 평가; 신규성 역검색은 GitHub 제한 검색이고 원자료·checkpoint·모델 실행은 미검증 |
| falsifiability | 3 | 풍부한 내용기준의 충분성과 route 불안정으로 주장을 축소할 수 있다. | 잠정 설계 평가; 신규성 역검색은 GitHub 제한 검색이고 원자료·checkpoint·모델 실행은 미검증 |
| interpretability | 3 | 조건부 좌표로 낮췄으나 재매개화 동등류는 남는다. | 잠정 설계 평가; 신규성 역검색은 GitHub 제한 검색이고 원자료·checkpoint·모델 실행은 미검증 |
| generalization | 3 | seed·내용·routing 변형을 계획했으나 실증 전이다. | 잠정 설계 평가; 신규성 역검색은 GitHub 제한 검색이고 원자료·checkpoint·모델 실행은 미검증 |
| technical_feasibility | 2 | 미선택 expert 계산과 동등 routing 구성 비용이 불명확하다. | 잠정 설계 평가; 신규성 역검색은 GitHub 제한 검색이고 원자료·checkpoint·모델 실행은 미검증 |
| exploration_value | 3 | 전문가 번호를 뇌 경로로 읽는 관행에 강한 통제를 준다. | 잠정 설계 평가; 신규성 역검색은 GitHub 제한 검색이고 원자료·checkpoint·모델 실행은 미검증 |

여덟 탐색 질문의 개별 답과 비판 수용/미해결 이력은 위 구조화 원본에 보존했다.

**최종 독립 감사의 범위 제한:** gate·error 분기를 모두 비교하되 동일 입력의 정보량 증가나 인간 신경 기전 증명으로 해석하지 않는다. 각 원안은 원 출처에 보존한다.

<a id="rq26"></a>
## RQ26. 정서 예측에 필요한 평균·분산·상관·시간전이의 최소 관측모형

자극조건부 잔차에서 독립 정서 주석 예측을 개선하는 것은 평균 변화, 대각 분산, 비대각 상관 또는 시간적 전이 중 무엇인가?

- **Axis·유형:** A × D × E × F × H × I × K × Q × T × X; Construct / Stimulus; Inference / Measurement; Model / Method; Neural; Structure / Dynamics
- **모델 적용 → 과학 질문 → 가정 도전:** 잔차화는 cross-fit한다. 동일 평균구조에서 stationary covariance→가변 diagonal→고정상관+가변분산→full covariance를 비교하고, 각 공간모형에 iid mixture·연속 volatility/covariance·이산 HMM 전이를 대조한다. 상태수·regularization은 내부 BOLD validation에 고정한다. → 동적 network-state라는 단일 해석을 평균/분산/상관의 공간적 관측구조와 이산/연속 시간구조의 최소 필요성으로 분해한다. → covariance HMM의 성공이 영역 간 결합 변화 및 실재하는 이산 신경 상태를 뜻한다는 가정이다.
- **경쟁 설명:** 정서 주석 관련 예측정보의 일부는 가변 분산 및 연속 관측모형을 넘어서는 비대각 시간구조를 요구한다. 이산 상태 자체의 존재는 별도 가설로 확정하지 않는다. / 같은 관측분포의 비정규 mixture·연속 분산변동·공통 자극 잔여가 HMM의 이득을 설명한다.
- **관측 대비:** 주석 변화의 held-out log score에서 비대각 구조 추가이득과 전이 추가이득을 별개 추정한다. BOLD 순차 log score는 보조다. 온라인 평가는 p(z_t|Y_≤t,X_≤t)의 filtered 상태만 쓰고 smoothing은 별도 오프라인 동행 결과로 명명한다.
- **반증:** 고정상관+가변분산이 full covariance와 동등하면 동적 비대각 구조 필요성을 낮춘다. 동일 emissions iid mixture 또는 연속 covariance가 HMM과 동등하면 이산 전이 필요성은 반박한다. 신뢰도·검정력 미달은 판정불가이다.
- **기준모형:** stationary covariance / time-varying diagonal covariance / fixed correlation+time-varying variance / 동일 emissions와 점유분포를 갖는 iid mixture / 같은 주변분포·자기상관을 맞춘 연속 volatility/covariance / 상태label 순열불변 예측 통계
- **자료·착수 조건:** primary: Emo-FilM의 원 연속 신호·시간 주석·run 경계가 확인될 때; extension: Horikawa/Spacetop은 연속 자료가 실제 있을 때만 적용; other_owned: NSD 시행 beta와 Mind Captioning 이름만으로 연속 상태 입력을 만들지 않음; 충분한 연속 신호 길이와 독립 run / motion·생리/측정 nuisance 가용성 / 상태 수·covariance 차원·regularization을 정할 내부 validation / annotation 빈도·HRF 지연·사건 경계의 독립 출처 / 필터링/스무딩 시간정보 정의 / 가변 분산 및 연속 null의 독립 calibration / 정서 상태명 대신 label 순열에 불변인 예측통계
- **근접 연구와 차이:** P067 / P066; 비대각 구조와 진폭을 분리하고 같은 관측 공간기하를 갖는 서로 다른 시간과정으로 상태 존재 해석을 직접 공격한다.
- **중복·신규성 위험:** 자연주의 dynamic connectivity 및 잔차 네트워크 연구와 겹칠 수 있다. residualization만으로 신규성 또는 내재성은 확보되지 않는다.
- **병합 시 보존한 판정:** 각 원안의 역할 판정은 병합 후에도 보존한다. C08-04: 과학RQ후보
- **원본:** [agents/08_systems_neuroscience/round04_revision.json](../agents/08_systems_neuroscience/round04_revision.json); 후보 C08-04
- **근거:** [P027 A foundation model of vision, audition, and language for in-silico neuroscience](https://arxiv.org/abs/2605.04326); [P029 Brain-JEPA: Brain Dynamics Foundation Model with Gradient Positioning and Spatiotemporal Masking](https://arxiv.org/abs/2409.19407); [P051 Similarity of Neural Network Representations Revisited](https://proceedings.mlr.press/v97/kornblith19a.html); [P066 Discovering event structure in continuous narrative perception and memory](https://doi.org/10.1016/j.neuron.2017.06.041); [P067 Brain network dynamics are hierarchically organized in time](https://github.com/OHBA-analysis/HMM-MAR)

| 평가 | 점수 | 이유 | 불확실성 |
|---|---|---|---|
| novelty | 3 | HMM·변동성 선행은 강하지만 독립 정서 대비의 최소 관측모형을 경쟁시킨다. | 실험 미실행·보유본 스키마 및 가까운 신규문헌 전수검색 미완료를 반영한 잠정 판단 |
| neuro_importance | 4 | 평균·진폭·상관·전이 중 어떤 설명이 필요한지 구별한다. | 실험 미실행·보유본 스키마 및 가까운 신규문헌 전수검색 미완료를 반영한 잠정 판단 |
| ai_necessity | 3 | 풍부한 자극 encoder는 도움이 되지만 작은 상태모형도 필수 대조다. | 실험 미실행·보유본 스키마 및 가까운 신규문헌 전수검색 미완료를 반영한 잠정 판단 |
| data_feasibility | 2 | 충분한 연속 run·시간 주석·nuisance 자료가 미확인이다. | 실험 미실행·보유본 스키마 및 가까운 신규문헌 전수검색 미완료를 반영한 잠정 판단 |
| rigor | 4 | 비대각/대각 및 이산/연속 대조를 분리하고 test 라벨 선택을 금지한다. | 실험 미실행·보유본 스키마 및 가까운 신규문헌 전수검색 미완료를 반영한 잠정 판단 |
| falsifiability | 4 | 가변 분산 또는 연속 null의 동등성이 강한 상태 해석을 반박한다. | 실험 미실행·보유본 스키마 및 가까운 신규문헌 전수검색 미완료를 반영한 잠정 판단 |
| interpretability | 4 | 이산 실재 대신 관측예측의 필요성으로 제한한다. | 실험 미실행·보유본 스키마 및 가까운 신규문헌 전수검색 미완료를 반영한 잠정 판단 |
| generalization | 3 | 영화/run 전이를 요구하나 상태 추정의 자료량 제약이 크다. | 실험 미실행·보유본 스키마 및 가까운 신규문헌 전수검색 미완료를 반영한 잠정 판단 |
| technical_feasibility | 3 | HMM 구현은 있으나 full covariance와 연속 null의 안정 추정이 어렵다. | 실험 미실행·보유본 스키마 및 가까운 신규문헌 전수검색 미완료를 반영한 잠정 판단 |
| exploration_value | 4 | 상태 성공의 원인을 공간기하와 시간정보로 나누는 가치가 있다. | 실험 미실행·보유본 스키마 및 가까운 신규문헌 전수검색 미완료를 반영한 잠정 판단 |

여덟 탐색 질문의 개별 답과 비판 수용/미해결 이력은 위 구조화 원본에 보존했다.

<a id="rq27"></a>
## RQ27. 사전 허용집합 안에서 검증하는 정서 관련 편집 신경 대비

개발자료에서 고정한 의미 보존·정서 조작량·감각 변화의 공통 지지 안에서 목표 편집 대 비목표 편집의 실제 신경 대비가 재현되는가?

- **Axis·유형:** A × B × C × F × H × K × L × O × P × Q × R × S × T × X; Construct / Stimulus; Inference / Measurement; Model / Method; Neural; Structure / Dynamics
- **모델 적용 → 과학 질문 → 가정 도전:** 모든 생성시도를 기록하고 독립 개발 주석으로 허용집합을 고정한 뒤 family 내 목표/비목표/무편집을 실제 제시한다. → 정서 주석 변화가 확인된 자극 대비가 지정된 의미·감각 보존 범위에서도 신경 반응 차이를 유지하는가? → 편집 통과군은 원 자극 모집단을 대표하고 pass/fail 차이는 의미 보존의 인과효과라는 가정을 거부한다.
- **경쟁 설명:** 허용집합 내 동일 family의 목표 대 동강도 비목표 대비에서 사전정의 neural contrast가 재현된다. / 선별이 조작 강도·난도·자연성을 바꾸었거나 미측정 의미 변화와 inversion artifact가 대비를 설명한다.
- **관측 대비:** 허용집합 S=1의 family별 목표−비목표 신경대비와 무편집 대비를 평가한다. 보존 연속점수×조작량의 관계는 보조 moderator 분석이다. 통과/실패 직접 차이를 일차 estimand로 쓰지 않는다.
- **반증:** 독립 주석상 충분한 조작·신뢰도·공통 지지가 있으나 목표 대비가 사전 최소 의미 효과를 지지하지 않으면 시험한 허용영역의 신경 가설이 약화된다. overlap 실패는 조작 설계 실패이며 신경 정보 부재가 아니다.
- **기준모형:** 무편집 inversion 왕복 / 동강도 비목표 편집 / 독립 자연 matched 자극 / 원본 family별 paired contrast / 허용조건 완화에 따른 coverage/효과 민감도(개발에서만 선택)
- **자료·착수 조건:** 보유 자극은 원본/자연 대조 pool 후보다. 새 편집물에는 새 인간 주석과 새 뇌 측정이 필수다. 기존 BOLD를 편집물에 붙이지 않는다. 자료 미확인은 제안 진행을 막지 않고 실행 전 확인 조건으로 남긴다.; 전체 생성시도·실패·선별 로그 / 독립 개발/검증 주석과 A 변화량·자연성·감각 변화의 공동 overlap / 사전 허용집합·최소 대비·표본단위 정의 / 새 자극 실제 제시·새 인간 뇌 측정 / 원본 family·참가자 계층 추론과 제시 순서 무작위화
- **근접 연구와 차이:** P070 / P078; 편집 모델 성능이 아닌 조작 타당성 기준을 통과하면서 살아남는 신경 대비를 연구 대상으로 설정.
- **중복·신규성 위험:** 일반 자극 통제 연구와 중복 가능. 의미의 완전 보존은 주장 불가; 명시된 측정 차원에서의 보존으로 제한.
- **병합 시 보존한 판정:** 각 원안의 역할 판정은 병합 후에도 보존한다. C09-03: 과학RQ후보; C09-05: 방법후보
- **원본:** [agents/09_generative_ai/round04_revision.json](../agents/09_generative_ai/round04_revision.json); 후보 C09-03, C09-05
- **근거:** [P070 Prompt-to-Prompt Image Editing with Cross-Attention Control](https://arxiv.org/abs/2208.01626); [P078 FlowEdit: Inversion-Free Text-Based Editing Using Pre-Trained Flow Models](https://arxiv.org/abs/2412.08629); [P051 Similarity of Neural Network Representations Revisited](https://proceedings.mlr.press/v97/kornblith19a.html); [P100 Statistical inference on representational geometries](https://doi.org/10.7554/eLife.82566); [P102 Conditional independence testing based on a nearest-neighbor estimator of conditional mutual information](https://proceedings.mlr.press/v84/runge18a.html); [P098 WILDS: A Benchmark of in-the-Wild Distribution Shifts](https://proceedings.mlr.press/v139/koh21a.html); [P099 In Search of Lost Domain Generalization](https://arxiv.org/abs/2007.01434)

| 평가 | 점수 | 이유 | 불확실성 |
|---|---|---|---|
| novelty | 3 | 선별된 estimand가 분명하지만 통제 자극 신경과학의 연장일 수 있다. | E3 사전 평가. 최신 선행 역검색·실제 schema·checkpoint·효과크기·비용 미확인; 점수 합산으로 선정하지 않음. |
| neuro_importance | 4 | 내용 보존과 독립 정서 대비의 양립 여부를 실제 뇌에서 판별한다. | E3 사전 평가. 최신 선행 역검색·실제 schema·checkpoint·효과크기·비용 미확인; 점수 합산으로 선정하지 않음. |
| ai_necessity | 3 | 생성은 matched 후보 제작에 유용하나 자연 대조로 대체 가능한 범위도 있다. | E3 사전 평가. 최신 선행 역검색·실제 schema·checkpoint·효과크기·비용 미확인; 점수 합산으로 선정하지 않음. |
| data_feasibility | 2 | 새 주석과 새 인간 뇌 측정이 필수다. | E3 사전 평가. 최신 선행 역검색·실제 schema·checkpoint·효과크기·비용 미확인; 점수 합산으로 선정하지 않음. |
| rigor | 4 | 전체 실패 로그·overlap·조건부 모집단을 명시했다. | E3 사전 평가. 최신 선행 역검색·실제 schema·checkpoint·효과크기·비용 미확인; 점수 합산으로 선정하지 않음. |
| falsifiability | 4 | 조작 성공과 신경대비 부재를 분리하는 기준이 있다. | E3 사전 평가. 최신 선행 역검색·실제 schema·checkpoint·효과크기·비용 미확인; 점수 합산으로 선정하지 않음. |
| interpretability | 3 | 정서 단일성분 또는 회로 인과를 주장하지 않는다. | E3 사전 평가. 최신 선행 역검색·실제 schema·checkpoint·효과크기·비용 미확인; 점수 합산으로 선정하지 않음. |
| generalization | 2 | 허용집합 밖으로 일반화하지 못한다. | E3 사전 평가. 최신 선행 역검색·실제 schema·checkpoint·효과크기·비용 미확인; 점수 합산으로 선정하지 않음. |
| technical_feasibility | 2 | 편집 통과율·실측 비용을 아직 계측하지 않았다. | E3 사전 평가. 최신 선행 역검색·실제 schema·checkpoint·효과크기·비용 미확인; 점수 합산으로 선정하지 않음. |
| exploration_value | 4 | 유효한 개입이 가능한 자극 범위 자체를 과학적 제약으로 다룬다. | E3 사전 평가. 최신 선행 역검색·실제 schema·checkpoint·효과크기·비용 미확인; 점수 합산으로 선정하지 않음. |

여덟 탐색 질문의 개별 답과 비판 수용/미해결 이력은 위 구조화 원본에 보존했다.

**실제 Round5 반영 조건:** 새 인간 주석·실제 새 BOLD가 필요하다. 결과전 family 수준 허용집합을 고정하고 생성 실패·독립realization·비목표 의미변화·선택된모집단을 명세한다.

**철회한 강한 해석:** 원본 BOLD 재사용, 허용된 자극묶음의 효과=순수 정서의 신경 인과효과

평가 점수는 Round4의 역할 판단이다. Round5 조건으로 실제 착수 가능성이 좁아진 경우 현재 점수 자체를 실현성 증명으로 읽지 않는다.

<a id="rq28"></a>
## RQ28. 언어 병목에서 정서 신경 대비의 예측 접근성이 선택적으로 낮아지는가

비정서 판별력과 일반 압축 오차를 맞췄을 때 언어 병목에서 독립 정서 신경 대비에 대한 외부 예측손실이 선택적으로 증가하는가?

- **Axis·유형:** A × C × F × G × H × I × J × K × O × Q × R × T × X; Construct / Stimulus; Inference / Measurement; Model / Method; Neural; Structure / Dynamics
- **모델 적용 → 과학 질문 → 가정 도전:** distortion와 비정서 판별력 일치 비언어 병목; 선형/소형 비선형 probe; 가역 재표현 대조; 관계·질감 과제; 다수 seed와 길이 일치 캡션을 사용해 동일 held-out 자극에서 각 신경 대비에 고정한 척도의 예측손실 L을 계산한다. 단계별 L(병목)-L(직접특징)을 정서/비정서 대비와 언어/비언어 병목 사이에서 비교한다. 대비 척도·noise ceiling은 훈련/독립 반복으로 고정하고 분모가 불명확한 잔차비율을 만들지 않는다. 용량×선형/소형 비선형 probe×훈련량 곡선을 함께 보고한다. → 비정서 판별력과 일반 압축 오차를 맞췄을 때 언어 병목에서 독립 정서 신경 대비에 대한 외부 예측손실이 선택적으로 증가하는가? → 고정 타깃·관측 support·독립 주석에서 경쟁 설명을 구별한다. 질문은 유지하되 실제 뇌 정보의 소실에서 특정 표현의 정서 대비 예측 접근성으로 주장을 축소한다.
- **경쟁 설명:** 일반 압축 오차와 비정서 대비의 난이도·신뢰도를 맞춘 뒤에도 언어 병목의 정서 대비 예측손실 증가가 비언어 병목보다 크고 평가한 readout family에서 남는다. / 차이는 일반 압축, 관계 누락, 표현 좌표, 유한 표본 probe 접근성 또는 캡션 입력범위의 차이다.
- **관측 대비:** 동일 held-out 자극에서 각 신경 대비에 고정한 척도의 예측손실 L을 계산한다. 단계별 L(병목)-L(직접특징)을 정서/비정서 대비와 언어/비언어 병목 사이에서 비교한다. 대비 척도·noise ceiling은 훈련/독립 반복으로 고정하고 분모가 불명확한 잔차비율을 만들지 않는다. 용량×선형/소형 비선형 probe×훈련량 곡선을 함께 보고한다.
- **반증:** 비선형 probe에서 회복되면 선형 접근성 차이이며 소실 주장을 철회한다. 비언어 병목 또는 관계·질감 대비에서도 같은 감소가 나면 정서·언어 선택성은 지지되지 않는다. 원 신경 대비 신뢰도 부족은 식별불가다.
- **기준모형:** distortion와 비정서 판별력 일치 비언어 병목; 선형/소형 비선형 probe; 가역 재표현 대조; 관계·질감 과제; 다수 seed와 길이 일치 캡션
- **자료·착수 조건:** Horikawa를 정서 대비의 우선 자료로 설계. NSD는 시각 식별/압축 대조 후보. Mind Captioning은 실제 신경–자극–텍스트 대응이 있는 경우 추가 경로로 연결하며 이름으로 구조를 확정하지 않는다.; 실제 단계/용량별 특징과 checkpoint / 캡션 available time·입력 provenance / 독립 신경 대비·주석 및 신뢰도 / distortion·비정서 난이도의 공통 지지
- **근접 연구와 차이:** P081 / P015 / P051; 고정된 실제 신경 대비의 예측손실에 대한 병목 종류×대비 종류의 상호작용으로 좁혔다. 단계 성능 차이를 인간 뇌의 정보 소실로 해석하지 않는다.
- **중복·신규성 위험:** 정렬 정보보존 연구와 중복될 수 있다. 단순 차원 감소 효과라면 정서 선택성 주장을 철회하고 방법 비교로 축소.
- **병합 시 보존한 판정:** 각 원안의 역할 판정은 병합 후에도 보존한다. C10-01: 과학RQ후보
- **원본:** [agents/10_llm_semantics/round04_revision.json](../agents/10_llm_semantics/round04_revision.json); 후보 C10-01
- **근거:** [P081 BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models](https://raw.githubusercontent.com/mlresearch/v202/gh-pages/li23q/li23q.pdf); [P015 MindEye2: Shared-Subject Models Enable fMRI-To-Image With 1 Hour of Data](https://arxiv.org/abs/2403.11207); [P079 Learning Transferable Visual Models From Natural Language Supervision](https://raw.githubusercontent.com/mlresearch/v139/gh-pages/radford21a/radford21a.pdf); [P051 Similarity of Neural Network Representations Revisited](https://proceedings.mlr.press/v97/kornblith19a.html); [P100 Statistical inference on representational geometries](https://doi.org/10.7554/eLife.82566)

| 평가 | 점수 | 이유 | 불확실성 |
|---|---|---|---|
| novelty | 3 | 병목과 정서 대비의 상호작용은 판별적이나 표현 보존 연구와 가깝다. | 새 외부 검색 미실행 |
| neuro_importance | 4 | 언어적 설명의 신경 충분성 경계를 좁힌다. | 정서 대비의 측정 타당성 미확정 |
| ai_necessity | 3 | 명시적 언어 병목이 유용하지만 소형 비언어 기준이 충분할 수 있다. | 최신 모델 필수성 없음 |
| data_feasibility | 3 | 기존 자극·BOLD로 설계 가능하다. | 반복·주석·활성 접근 미확인 |
| rigor | 4 | 고정 타깃과 distortion·probe 대조를 추가했다. | 완전 의미 일치 불가 |
| falsifiability | 4 | 비선형 회복과 일반 압축이 명시적 반증이다. | 검출력 제한 |
| interpretability | 3 | 접근성으로 제한해 과잉 해석을 줄였다. | 정보 부재 식별 불가 |
| generalization | 3 | 새 자극 family에서 보존 곡선을 검정한다. | 내용 coverage 불확실 |
| technical_feasibility | 3 | 고정 특징과 작은 readout으로 시작할 수 있다. | 용량별 checkpoint 미확인 |
| exploration_value | 4 | 정서 선택적 압축 주장의 해석 범위를 시험한다. | 최초성 미확정 |

여덟 탐색 질문의 개별 답과 비판 수용/미해결 이력은 위 구조화 원본에 보존했다.

<a id="rq29"></a>
## RQ29. 최근성 가산 설명을 넘어선 사건 순서 관련 신경 예측

현재·최근 사건을 고정하고 사건 identity별 lag 기여를 허용해도 순서 관련 관계 표현이 독립 정서 신경 대비의 예측을 추가하는가?

- **Axis·유형:** C × D × E × H × I × J × M × Q × V × X; Construct / Stimulus; Inference / Measurement; Model / Method; Neural; Structure / Dynamics
- **모델 적용 → 과학 질문 → 가정 도전:** 현재+최근 k사건; identity×lag 가산모형; causal unordered 표현; 원순서 paraphrase; 개연성 일치 대체순서; 동일 smoothness/FIR; full-film oracle 분리을 사용해 현재와 마지막 k개 사건을 고정한 원순서/먼 과거 교환/lag 가중 bag/원순서 paraphrase를 동일 외부 영화에서 비교한다. 주 추정량은 고정 신경 대비의 예측손실 차이이며 전체 서사 예측도 별도 보고한다. 사건별 available time과 HRF 연산자를 공유하고 train/test 경계에 지원구간 buffer를 둔다. → 현재·최근 사건을 고정하고 사건 identity별 lag 기여를 허용해도 순서 관련 관계 표현이 독립 정서 신경 대비의 예측을 추가하는가? → 고정 타깃·관측 support·독립 주석에서 경쟁 설명을 구별한다. 원 사건집합 비교만으로 recency와 순서를 가를 수 없다는 실제 비판을 반영한다.
- **경쟁 설명:** past-only 원순서 표현이 최근성·개연성·smoothness·동일 HRF family를 통제한 기준보다 독립 영화의 정서 신경 대비를 더 잘 예측한다. / 이득은 recency-weighted 내용, 잘못된 순서 입력의 OOD, 미래/완결 사건 서술 또는 관측 평활화 때문이다.
- **관측 대비:** 현재와 마지막 k개 사건을 고정한 원순서/먼 과거 교환/lag 가중 bag/원순서 paraphrase를 동일 외부 영화에서 비교한다. 주 추정량은 고정 신경 대비의 예측손실 차이이며 전체 서사 예측도 별도 보고한다. 사건별 available time과 HRF 연산자를 공유하고 train/test 경계에 지원구간 buffer를 둔다.
- **반증:** identity×lag 기준과 동등하면 순서 관계 표현의 추가 필요성은 약화된다. 자연스러움·smoothness 일치 후 사라지면 표현 OOD 설명을 지지한다. full-film에서만 나타나면 온라인 과거 주장 기각.
- **기준모형:** 현재+최근 k사건; identity×lag 가산모형; causal unordered 표현; 원순서 paraphrase; 개연성 일치 대체순서; 동일 smoothness/FIR; full-film oracle 분리
- **자료·착수 조건:** 보유5종을 기반으로 계속 설계한다. Emo-FilM은 실제 연속 주석·평정지연을 사용하는 시간 분석 후보; Spacetop은 확인된 평정 단위에 맞춘 clip 요약 대비로 제한하며 clip 평정을 매 TR 복제하지 않는다. Horikawa는 실제 시행 정보에 맞춘 축소안, NSD는 정적 대조, Mind Captioning은 실제 시점·출처가 있는 경우만 시간 의미 통제로 연결한다.; 사건 onset/completion 및 caption generation time / 실제 prefix·최근 사건 공통 지지 / 독립 영화·주석 cohort·지연 / 개연성·smoothness 대조 / 실제 HRF 지원구간
- **근접 연구와 차이:** P085 / P086 / P066; 같은 사건집합의 원순서 우위를 recency·OOD·시간관측과 경쟁시키도록 좁혔다. 순서 자체와 순서의 의미를 완전히 분리했다는 주장은 하지 않는다.
- **중복·신규성 위험:** 서사 encoding과 중복 위험. 순서를 바꾼 모델 특징의 예측 차이를 실제로 순서를 바꿔 본 뇌의 인과 반응으로 해석할 수 없다.
- **병합 시 보존한 판정:** 각 원안의 역할 판정은 병합 후에도 보존한다. C10-03: 과학RQ후보
- **원본:** [agents/10_llm_semantics/round04_revision.json](../agents/10_llm_semantics/round04_revision.json); 후보 C10-03
- **근거:** [P085 The neural architecture of language: Integrative modeling converges on predictive processing](https://github.com/mschrimpf/neural-nlp); [P086 Scaling laws for language encoding models in fMRI](https://arxiv.org/abs/2305.11863); [P066 Discovering event structure in continuous narrative perception and memory](https://doi.org/10.1016/j.neuron.2017.06.041); [P100 Statistical inference on representational geometries](https://doi.org/10.7554/eLife.82566); [P002 Emo-FilM: A multimodal dataset for affective neuroscience using naturalistic stimuli](https://doi.org/10.1038/s41597-025-04803-5)

| 평가 | 점수 | 이유 | 불확실성 |
|---|---|---|---|
| novelty | 3 | recency를 분리한 정서 문맥 대비가 후보 차별점이다. | 서사 순서 선행 최신 역검색 필요 |
| neuro_importance | 4 | 사건 관계가 필요한 시간적 표현의 범위를 규정한다. | HRF 해상도 제한 |
| ai_necessity | 3 | 문맥 LLM이 유용하지만 lag 가중 단순 기준이 충분할 수 있다. | 단순 기준 우위 가능 |
| data_feasibility | 3 | 연속 자료와 clip 요약의 두 계획이 있다. | 사건 available time·주석 해상도 미확인 |
| rigor | 4 | recency·OOD·미래·buffer 대조를 추가했다. | 순서와 의미 완전 분리 불가 |
| falsifiability | 4 | lag와 oracle 비교가 분명한 반증을 제공한다. | 통계적 동등성 검출력 필요 |
| interpretability | 3 | 관찰적 순서 특징 증분으로 해석을 제한한다. | 모델 개연성과 의미 변화 남음 |
| generalization | 3 | 외부 영화 전이를 계획한다. | 독립 영화 수 불확실 |
| technical_feasibility | 3 | 특징 추출·사건 주석 비용이 요구된다. | 시간별 caption 경로 미확인 |
| exploration_value | 4 | 느린 BOLD를 긴 통합으로 해석하는 가정을 시험한다. | 실제 순서 개입은 별도 측정 |

여덟 탐색 질문의 개별 답과 비판 수용/미해결 이력은 위 구조화 원본에 보존했다.

**최종 독립 감사의 범위 제한:** 현재 사건·최근성·사건 다중집합을 맞추고 사건 순열만 바꾸었을 때 순서 비가산 효과가 남는가에 한정. 일반적 이력 보존/HRF 상태나 미래학습목표 효과로 확장하지 않음. 공통 지지가 없으면 다른 시간 RQ로 중복 승격하지 않음.

<a id="rq31"></a>
## RQ31. 유한 함수 동등성을 인정한 공유제약의 정서 대비 일반화 효율

정확히 펼친 유한 반복망과의 함수 동등성을 확인한 뒤, 가중치 공유라는 학습 제약은 새 사건 길이·조합에서 독립 정서 신경 대비의 예측 효율을 바꾸는가?

- **Axis·유형:** C × D × F × I × J × K × M × N × Q × T × V; Construct / Stimulus; Inference / Measurement; Model / Method; Neural; Structure / Dynamics
- **모델 적용 → 과학 질문 → 가정 도전:** 같은 가중치를 복사한 exact-unroll에서 출력과 대응 중간상태 일치를 확인한다. 그 후 같은 함수에서 시작한 공유/비공유 모델을 데이터량·반복 길이별로 학습한다. → 재귀 구현의 신경 실재가 아니라 공유제약이 제공하는 학습·전이 편향이 정서 대비에서 선택적인가? → 같은 함수의 encoding으로 재귀와 feedforward 구현을 구별한다는 가정을 철회한다.
- **경쟁 설명:** 유한 관측에서는 exact-unroll과 같지만 학습 밖 길이·사건 조합에서 공유제약이 정서 대비 예측의 효율을 높이며 일반 시각 정확도 대조로 완전히 설명되지 않는다. / 파라미터 감소의 일반 규제·위치/순서 정보·깊이·학습량만으로 충분하다.
- **관측 대비:** 학습 자료량×공유 제약×반복수 요인에서 보류 사건 길이/조합의 정서 대비 손실과 일반 시각 대비 손실을 비교한다. 파라미터/FLOPs/정확도 맞춤 결과는 별도 보고하고 내부 step을 신경 시간으로 변환하지 않는다.
- **반증:** exact-unroll 출력 불일치면 구현 점검 단계에서 중단한다. OOD 효율이 비공유·일반 규제·순서무관 대조와 같으면 공유제약의 해당 범위 필요성을 지지하지 않는다.
- **기준모형:** 동일 가중치 exact-unroll / 동일 함수 초기화 비공유 모델 / 일반 parameter regularization / 공유가중치 순서무관 pooling / 학습량/길이 및 인식 성능 맞춤 대조 / 독립 단계·position-only·동일 사건집합 순서교환
- **자료·착수 조건:** Horikawa에서 자극별 계산 비교를 먼저 계획한다. 실제 연속 timing·사건 다양성이 있는 보유 자료에서 단계 비교를 수행하며, 속도 조작 실측이 없으면 속도 불변성의 인과 주장은 하지 않는다.; 사건 경계/단계 주석 또는 비신경 독립 추정 / 연속 자료와 run 경계 / 동일 목표/학습자료의 통제 모델 생성 비용 / 모든 상태갱신·정규화·초기상태를 보존한 정확 펼침 / 길이 OOD와 자극 의미 OOD의 분리 / 외부 사건 단계 및 순서 정의
- **근접 연구와 차이:** P090 / P042; 재귀의 뇌 구현 판별에서 공유제약의 학습/길이 전이 효율로 핵심 주장을 바꿨다. exact-unroll 통제는 결과가 아니라 미실행 검증 절차다.
- **중복·신규성 위험:** 중간~높음: 재귀와 깊이 비교는 기존 주제. 정서 대비와 단계 shortcut의 동시 판별이 차별 후보지만 최초성 미검증.
- **병합 시 보존한 판정:** 각 원안의 역할 판정은 병합 후에도 보존한다. C11-03: 과학RQ후보
- **원본:** [agents/11_brain_inspired/round04_revision.json](../agents/11_brain_inspired/round04_revision.json); 후보 C11-03
- **근거:** [P090 Brain-Like Object Recognition with High-Performing Shallow Recurrent ANNs](https://arxiv.org/abs/1909.06161); [P042 Temporal Cycle-Consistency Learning](https://arxiv.org/abs/1904.07846); [P043 VideoMamba: State Space Model for Efficient Video Understanding](https://arxiv.org/abs/2403.06977); [P096 Predictive Coding Approximates Backprop along Arbitrary Computation Graphs](https://arxiv.org/abs/2006.04182)

| 평가 | 점수 | 이유 | 불확실성 |
|---|---|---|---|
| novelty | 3 | 공유제약과 OOD 효율 자체는 기존이며 정서 대비 연결만 후보이다. | 잠정 설계 평가; 신규성 역검색은 GitHub 제한 검색이고 원자료·checkpoint·모델 실행은 미검증 |
| neuro_importance | 3 | 구현보다 학습 편향의 신경 대비 관련성을 제한적으로 평가한다. | 잠정 설계 평가; 신규성 역검색은 GitHub 제한 검색이고 원자료·checkpoint·모델 실행은 미검증 |
| ai_necessity | 3 | 반복/펼침 통제 모델이 필요하지만 초대형 모델은 필요하지 않다. | 잠정 설계 평가; 신규성 역검색은 GitHub 제한 검색이고 원자료·checkpoint·모델 실행은 미검증 |
| data_feasibility | 2 | 길이·사건 조합과 독립 정서 대비의 충분성이 미확인이다. | 잠정 설계 평가; 신규성 역검색은 GitHub 제한 검색이고 원자료·checkpoint·모델 실행은 미검증 |
| rigor | 4 | exact-unroll과 여러 예산 대조로 핵심 혼동을 명시했다. | 잠정 설계 평가; 신규성 역검색은 GitHub 제한 검색이고 원자료·checkpoint·모델 실행은 미검증 |
| falsifiability | 4 | 등가 검증 실패와 OOD 효율 부재의 중단 조건이 명료하다. | 잠정 설계 평가; 신규성 역검색은 GitHub 제한 검색이고 원자료·checkpoint·모델 실행은 미검증 |
| interpretability | 4 | 재귀 실재 주장을 철회해 조건부 해석 경계가 분명하다. | 잠정 설계 평가; 신규성 역검색은 GitHub 제한 검색이고 원자료·checkpoint·모델 실행은 미검증 |
| generalization | 4 | 새 길이×새 조합 평가를 질문의 중심에 둔다. | 잠정 설계 평가; 신규성 역검색은 GitHub 제한 검색이고 원자료·checkpoint·모델 실행은 미검증 |
| technical_feasibility | 2 | 동일 자료/초기함수의 제어 학습은 구현 비용이 있다. | 잠정 설계 평가; 신규성 역검색은 GitHub 제한 검색이고 원자료·checkpoint·모델 실행은 미검증 |
| exploration_value | 4 | 신경 비교가 구현 식별보다 학습 제약에 주는 정보를 재정의한다. | 잠정 설계 평가; 신규성 역검색은 GitHub 제한 검색이고 원자료·checkpoint·모델 실행은 미검증 |

여덟 탐색 질문의 개별 답과 비판 수용/미해결 이력은 위 구조화 원본에 보존했다.

<a id="rq32"></a>
## RQ32. 실제 신경 guide는 의미로 예측한 신경 guide를 넘는 모델 제약인가

풍부한 자극 의미로 cross-fit 예측한 neural guide와 통계구조를 맞춘 뒤에도 실제 신경 guide는 새 내용×새 피험자에서 모델 상태예측과 독립 정서 신경 대비에 추가 효용을 주는가?

- **Axis·유형:** A × C × F × H × I × J × N × Q × R × S × T × X; Construct / Stimulus; Inference / Measurement; Model / Method; Neural; Structure / Dynamics
- **모델 적용 → 과학 질문 → 가정 도전:** 훈련 fold 내부에서 자극만으로 neural target을 예측하는 teacher를 cross-fit한다. 같은 adapter에 실제 neural target, cross-fit 예측 target, 그 잔차, 풍부한 독립 의미 guide 및 통계구조 일치 sham을 각각 제공한다. → 신경 측정이라는 감독 원천이 지정한 강한 자극 예측 guide를 넘어 유용한 모델 제약을 제공하는가? → 무작위 guide보다 neural guide가 좋으면 뇌 고유 계산을 발견했다는 가정을 철회한다.
- **경쟁 설명:** 실제 neural guide 또는 신뢰 가능한 cross-fit 잔차 guide가 강한 semantic-predicted neural guide보다 새 내용/사람의 이중 지표에서 추가 효용을 보인다. / 구조화된 의미 감독·자극 ID·추가 label 정보량·신뢰도·일반 규제 및 readout 맞춤으로 충분하다.
- **관측 대비:** 동일 adapter의 보류 상태예측 손실과 새 피험자×새 자극의 정서 신경 대비 손실을 각각 사전 고정한다. 두 지표 개선을 공동 요구한다. guide별 rank·공분산·smoothness·반복 신뢰도·손실 scale과 자극 속성 예측력을 보고하되 완전 정보량 일치를 주장하지 않는다.
- **반증:** semantic-predicted neural guide로 충분하면 지정 비교에서 신경 측정의 추가 감독 효용을 지지하지 않는다. 신경 정렬만 좋아지면 계산 사용 주장을 낮춘다. 손상량 일치/분포 내 ablation에서 효용이 사라지면 제거 효과의 해석을 보류한다.
- **기준모형:** cross-fitted stimulus-only predicted neural guide / 외부 검수 객체·관계·사건 의미 guide / 실제 neural guide와 cross-fitted residual guide / 공분산/신뢰도/smoothness 일치 sham / 동일 adapter·손실 scale·학습 예산 / 손상량 일치 및 분포 내 feature 교체
- **자료·착수 조건:** Horikawa 보유 자료에서 독립 정서 대비·반복·자극 분리가 확인되면 소형 adapter 계획을 구체화한다. NSD는 정서 라벨을 가정하지 않는 감각 대조; Mind Captioning은 식별자·주석 미확인 상태로 후속 의미 대조 후보만 유지한다.; 독립 정서 대비의 구성 타당성·신뢰도 / 훈련/검증/외부평가 피험자·자극 분리 / 모델 checkpoint·adapter 지원·비정서 예측 목표 / 신경 guide와 의미 guide의 정보량 매칭 / 훈련-only cross-fitting과 outer 피험자×내용 분리 / 의미 guide는 자극/독립 사람이 만든 설명이며 같은 뇌에서 만든 캡션 제외 / guide의 신뢰도·공분산과 자극속성 예측력 보고 / 완전 의미 제거 불가에 대한 잔여 한계 명시
- **근접 연구와 차이:** P050 / P049; 신경 대 무작위 감독 비교를 실제 측정 대 자극으로 예측한 대체 신경 교사의 추가 효용 질문으로 변경했다. 잔차를 순수 정서나 자극과 독립인 뇌 정보로 명명하지 않는다.
- **중복·신규성 위험:** 높음: neural-guided learning 선행연구를 추가 역검색해야 한다. 세계 최초·뇌 메커니즘 발견은 주장하지 않는다.
- **병합 시 보존한 판정:** 각 원안의 역할 판정은 병합 후에도 보존한다. C11-05: 과학RQ후보
- **원본:** [agents/11_brain_inspired/round04_revision.json](../agents/11_brain_inspired/round04_revision.json); 후보 C11-05
- **근거:** [P027 A foundation model of vision, audition, and language for in-silico neuroscience](https://arxiv.org/abs/2605.04326); [P049 Invariant Risk Minimization](https://arxiv.org/abs/1907.02893); [P050 Who Needs Labels? Adapting Vision Foundation Models With the Metadata You Already Have](https://arxiv.org/abs/2606.05107); [P083 Concept Bottleneck Models](https://raw.githubusercontent.com/mlresearch/v119/gh-pages/koh20a/koh20a.pdf); [P100 Statistical inference on representational geometries](https://doi.org/10.7554/eLife.82566); [DOC-CIRCUIT circuit-tracer 공식 코드](https://github.com/safety-research/circuit-tracer)

| 평가 | 점수 | 이유 | 불확실성 |
|---|---|---|---|
| novelty | 3 | neural-guided learning 선행과 중복 위험이 커 잠정 3점이다. | 잠정 설계 평가; 신규성 역검색은 GitHub 제한 검색이고 원자료·checkpoint·모델 실행은 미검증 |
| neuro_importance | 4 | 신경 측정이 추가 계산 제약을 제공하는지 직접 평가한다. | 잠정 설계 평가; 신규성 역검색은 GitHub 제한 검색이고 원자료·checkpoint·모델 실행은 미검증 |
| ai_necessity | 3 | 자극→신경 teacher와 adapter가 필요하나 단순 baseline도 유지한다. | 잠정 설계 평가; 신규성 역검색은 GitHub 제한 검색이고 원자료·checkpoint·모델 실행은 미검증 |
| data_feasibility | 2 | 새 사람×새 내용 및 교사 신뢰도 확보가 실제로 미확인이다. | 잠정 설계 평가; 신규성 역검색은 GitHub 제한 검색이고 원자료·checkpoint·모델 실행은 미검증 |
| rigor | 4 | cross-fitting·강한 semantic teacher·이중 평가로 순환을 통제한다. | 잠정 설계 평가; 신규성 역검색은 GitHub 제한 검색이고 원자료·checkpoint·모델 실행은 미검증 |
| falsifiability | 4 | 대체 교사의 충분성 또는 한쪽 지표만 개선되면 주장을 낮춘다. | 잠정 설계 평가; 신규성 역검색은 GitHub 제한 검색이고 원자료·checkpoint·모델 실행은 미검증 |
| interpretability | 3 | 잔차의 신경고유성은 주장하지 않아도 정보매칭 한계가 남는다. | 잠정 설계 평가; 신규성 역검색은 GitHub 제한 검색이고 원자료·checkpoint·모델 실행은 미검증 |
| generalization | 4 | 이중 외부 분할과 별도 모델 전이를 핵심 판정으로 둔다. | 잠정 설계 평가; 신규성 역검색은 GitHub 제한 검색이고 원자료·checkpoint·모델 실행은 미검증 |
| technical_feasibility | 2 | checkpoint/adapter/교사학습 비용과 데이터량은 확인 전이다. | 잠정 설계 평가; 신규성 역검색은 GitHub 제한 검색이고 원자료·checkpoint·모델 실행은 미검증 |
| exploration_value | 4 | 신경과학→AI 역방향의 실질적 효용을 반증 가능하게 한다. | 잠정 설계 평가; 신규성 역검색은 GitHub 제한 검색이고 원자료·checkpoint·모델 실행은 미검증 |

여덟 탐색 질문의 개별 답과 비판 수용/미해결 이력은 위 구조화 원본에 보존했다.

<a id="rq30"></a>
## RQ30 — 독립 RQ 집계에서 제외

동일 과학 대비의 계산좌표 분기로 병합; RQ25

원안과 추적 정보는 [보존 기록](retired_questions.json)에 있다.

<a id="rq22"></a>
## RQ22 — 독립 RQ 집계에서 제외

방법후보로 유지; 기저 불변성과 모델 기능/신경 대응의 감사는 유용하지만 현재 명세만으로 독립 정서 신경 가설을 구별하지 못하므로 방법후보로 유지

원안과 추적 정보는 [보존 기록](retired_questions.json)에 있다.
