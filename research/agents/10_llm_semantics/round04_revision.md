# Agent10 실제 Round4 비판 응답과 새 연결

독립 관측과 고정 추정량을 중심으로 후보5개를 수정했다. 자기 최상위 제안은 C10-02·C10-05이며 C10-04는 상위 관측–prior 질문의 방법후보다.

## 읽기 기록

- `discussions/ROUND04_PROTOCOL.md`

- `discussions/round_03/collected.json`

- `agents/10_llm_semantics/round02_exchange.json`

- `literature/papers.csv`


## C10-01 응답

실제 비판: R3-05-C10-01, R3-09-C10-01

판정: 수정 — 질문은 유지하되 실제 뇌 정보의 소실에서 특정 표현의 정서 대비 예측 접근성으로 주장을 축소한다.

수용:

- 두 검토자의 지적대로 실제 신경반응의 신뢰도는 고정된 측정 특성으로 두고 압축 단계의 종속변수에서 제거한다.

- 불명확한 보존율 대신 독립 신경 대비에 대한 held-out 예측손실 차이를 정의한다. 선형 접근성 저하와 평가한 비선형 probe에서도 회복되지 않는 차이를 구분한다.

- 객체 외 관계·질감 대비 및 distortion와 비정서 판별력을 맞춘 비언어 병목을 포함한다.

- 캡션의 생성 입력·seed·길이·available time·뇌/정서라벨 비사용을 기록한다. 전체 결말을 본 설명은 온라인 분석과 분리한다.

남은 이견:

- 정보의 완전 부재나 언어에 본질적으로 없는 정서정보를 유한 probe로 입증할 수 없다는 두 검토자의 이견을 수용해 강한 정보소실 주장은 철회한다.

- 비정서 대비로 모든 의미를 같게 만들 수 없으므로 결론은 명시한 비교·readout family에 한정한다.


## C10-02 응답

실제 비판: R3-05-C10-02, R3-09-C10-02

판정: 수정 — 추정량이 바뀐다는 지적을 수용해 고정 원타깃의 nested predictor 대비로 실질 수정한다.

수용:

- 원 정서 주석 A를 모든 의미 조건에서 고정하고 잔차 타깃의 분산 변경을 비교하지 않는다.

- 객체·중립 관계·정서결론 포함 설명을 분리하고 뇌·정서 라벨을 입력하지 않은 설명만 주분석에 사용한다.

- 의미-only, 의미+D, 의미+N의 동일 보류 표본 예측을 비교한다. 감소는 조건부 예측의 통계적 중복으로 해석하며 원 N-D가 허위였다고 하지 않는다.

- 타깃 예측력·길이·내용량을 맞춘 비관계 설명과 공통입력×HRF null을 추가한다. UC10-1로 제한된 추가 관계 주석의 선택 원리를 제안한다.

남은 이견:

- 관계 의미를 지우면 더 순수한 정서가 된다는 해석은 철회한다. 공유정보와 비가산성이 공존할 수 있다는 이견을 보존한다.

- 관계별 감소의 특이성을 확인해도 의미가 인과적으로 신경 상호작용을 매개했다는 주장은 하지 않는다.


## C10-03 응답

실제 비판: R3-05-C10-03, R3-09-C10-03

판정: 수정 — 원 사건집합 비교만으로 recency와 순서를 가를 수 없다는 실제 비판을 반영한다.

수용:

- 마지막 k개 사건·현재 구간을 고정한 먼 과거 순서 교환과 identity×lag 가산 baseline을 추가한다.

- 원순서 paraphrase, 검수된 대체순서, 특징 smoothness·개연성 대조를 별도로 둔다.

- 사건 설명은 시점 t까지 관찰한 부분만 사용하며 completion·generation 시각을 기록한다. full-film oracle은 회고 조건이다.

- Emo-FilM 연속 주석과 Spacetop clip 수준 평정 계획을 분리하고, 원시간 HRF family와 fold buffer를 적용한다.

남은 이견:

- 시간순서와 순서가 만드는 사건 관계 의미를 완전히 분리한다는 주장은 철회한다. 관심대상을 최근성 가산 설명을 넘어선 순서 관련 관계 표현의 증분으로 좁힌다.

- 모델 순서 변형이 인간의 순서 개입을 대신하지 않는다는 이견을 수용한다.


## C10-04 응답

실제 비판: R3-05-C10-04, R3-09-C10-04

판정: 수정 — 교환의 분포 적합성 개선과 관측–prior 가족의 하위 캡션 비교라는 범위 조정을 수용한다.

수용:

- Agent05의 핵심 유지와 Agent09의 교환 OOD 수정 요구를 함께 반영한다.

- 같은 피험자·런·SNR·사건단계·내용 공통지지 안에서 독립 metadata로 교환 후보를 고정한다. 평균/영 조건은 주분석에서 제외한다.

- 원 뇌 readout·생성 전 latent·캡션의 외부 판별을 나누고 latent/출력 성공의 네 경우를 사전 정의한다.

- Agent09 C09-01과 정보출처 서명 중복을 인정해 독립 최상위 RQ 수에 추가하지 않는 방법/하위 비교 후보로 분리한다.

남은 이견:

- Agent05는 유지, Agent09는 수정·상위 가족 병합을 권고했다. 과학적 동기를 버리지 않지만 후보 중복을 줄이기 위해 방법후보로 분류한다.

- latent 실패·출력 성공을 prior 보충으로 단정하지 않는다. latent probe의 접근성 실패도 가능한 소수 설명으로 남긴다.


## C10-05 응답

실제 비판: R3-05-C10-05, R3-09-C10-05

판정: 수정 — 가설을 실제 관측 가능한 cell의 일반화 대비로 제한하고 mapping 불확실성을 새 연구 차원으로 추가한다.

수용:

- zero-shot anatomy-only, 평가 내용과 독립인 calibration k-shot, 피험자 내 기준을 분리하고 예산을 맞춘다.

- 새 ID·새 관계조합·새 성분을 구분하고 실제 참가자×자극 관측 cell만 사용한다. 없는 cell을 예측으로 채워 검정하지 않는다.

- 같은 시험 자극의 자극-only 관계 판별을 추가해 표현·신경 mapping·측정의 세 층을 구분한다.

- UC10-2로 단일 최선 정렬 대신 독립 calibration에서 허용된 복수 mapping에 걸쳐 유지되는 결론을 평가하도록 확장한다.

남은 이견:

- 정렬 뒤 남은 실패를 곧 언어 조합 결손으로 특정한다는 원 표현을 철회한다.

- Agent09는 개념 유지, Agent05는 calibration 명세 수정을 요구했다. 개념은 유지하지만 단일 mapping 귀속을 피하도록 실질 수정한다.

- 측정 불변성이 충분하지 않으면 의미/좌표만으로 원인을 완전히 분해할 수 없다는 이견을 남긴다.


## UC10-1 — 순차 Bayesian 실험설계와 개념 질의

**original_computational_goal**: P077은 설계–관측 history에서 다음 실험을 고르는 정책으로 반복 설계 비용을 줄인다. P083 §8은 인간 질의로 개념을 학습·정제할 가능성을 논의한다.

**imported_structure**: 다음 자극을 생성하는 대신 어떤 독립 중립 관계 주석을 다음에 수집할지 선택한다. 후보 관계 질의의 기대 정보가 관계특이 중복 가설과 일반 타깃설명력 가설을 얼마나 구별하는지 훈련 자료에서 평가한다.

**new_neural_question**: 제한된 추가 의미 주석 예산에서 어떤 관계를 확인해야 정서 관련 N-D 감소의 두 설명을 가장 잘 구분하는가?

**why_not_same_as_round2**: Round2는 미리 정한 객체/관계 특징을 비교했다. 여기서는 미측정 의미 중 다음 관측을 적응적으로 선택하는 측정 정책 자체를 새로 도입한다. 단순 모델·데이터명 교체가 아니다.

**candidate_ids**: C10-02

**source_papers**: P077; P083; P100

**assumptions**: 관계 주석은 뇌·정서라벨을 보지 않는 별도 주석자가 제공; 주석 likelihood와 불확실성을 정의할 수 있어야 정확한 Bayesian 설계 명칭 사용 가능; P077의 연속 설계·조건부 독립·명시적 likelihood 가정이 이산·상관 주석에 자동 성립하지 않음; 불충족 시 이산 enumeration 또는 disagreement 휴리스틱으로 명칭을 낮추고 exact EIG를 주장하지 않음

**discriminating_test**: 동일 주석비용에서 random/내용 coverage/단순 disagreement/가능하면 명시적 정보기준 정책을 훈련 자료에만 적용한다. 고정된 외부 자극·주석에서 두 경쟁 설명의 판별 손실과 잘못된 선택 비율을 비교한다. adaptive 선택의 성능을 선택에 사용한 신경 자료로 평가하지 않는다.

**failure_interpretation**: 단순 coverage와 같으면 적응 설계의 필요성이 없다. 비용 감소만 있고 신경 가설 판별이 나아지지 않으면 주석 효율 방법으로 제한한다.


## UC10-2 — 잡음 역문제의 복수 해와 신경 지도 정렬

**original_computational_goal**: P076은 잡음 관측과 diffusion prior를 결합해 신호를 근사 복원한다. P062는 좌표가 다른 뇌 지도의 변환·비교를 다루며 개인/집단 변환의 한계를 밝힌다.

**imported_structure**: 관측과 양립하는 자극 후보의 복수성이라는 구조를 자극 대신 신경 mapping의 복수성으로 옮긴다. 독립 calibration에서 비슷한 손실을 갖는 mapping family를 사전에 허용하고 이후 의미 일반화 결론이 모든 허용 mapping에서 유지되는지 본다.

**new_neural_question**: 특정 정렬 하나에서 보이는 새 의미조합의 정서 신경 예측 실패는 calibration으로 구별할 수 없는 다른 mapping에서도 유지되는가?

**why_not_same_as_round2**: Round2는 개인/공유 mapping 중 선택한 모형의 요인 비교였다. 여기서는 선택을 하나로 고정하지 않고 허용 mapping 전체에서의 결론 범위를 주타깃으로 바꾸었다. P076의 원신호 생성과도 다른 추정 대상이다.

**candidate_ids**: C10-05

**source_papers**: P076; P062; P100

**assumptions**: 독립 calibration 관측과 noise/reliability 기반 사전 허용오차; 후보 mapping family의 유한 coverage 한계를 명시; 같은 test 성능으로 허용 mapping을 선택하지 않음; 허용집합을 posterior 또는 진짜 신경 등가군으로 해석하지 않음

**discriminating_test**: mapping을 생성한 훈련 자료와 허용여부를 정하는 calibration, 의미일반화를 평가하는 test를 분리한다. calibration 손실이 비슷한 mapping들에서 새 관계조합 대비의 부호·크기 범위를 보고 단일 최선 mapping 결론과 비교한다.

**failure_interpretation**: mapping에 따라 결론이 바뀌면 의미 실패의 귀속이 정렬 선택에 의존한다. 모두 같은 실패라도 공통 누락과 주석차이가 남으므로 뇌의 의미코드 부재를 확정하지 않는다.


## C10-01 수정안 — 언어 병목에서 정서 신경 대비의 예측 접근성이 선택적으로 낮아지는가

연구역할: 과학RQ후보

최상위 추천: False; 이번 자기 후보 최상위2개에는 제안하지 않음; 비교·하위 검증으로 보존

**axis_ids**: ["AS22", "AS05", "AS07", "AS30"]

**research_question**: 비정서 판별력과 일반 압축 오차를 맞췄을 때 언어 병목에서 독립 정서 신경 대비에 대한 외부 예측손실이 선택적으로 증가하는가?

**neural_target**: 반복 또는 독립 자료로 신뢰도를 추정해 고정한 정서·객체·관계·질감 신경 대비; 모델 단계가 실제 신뢰도를 바꾼다고 가정하지 않음

**external_principle**: Agent03의 정렬 정보보존 감사와 생성 전후 이중 평가; BLIP-2의 시각→Q-Former 언어 병목

**model_application**: distortion와 비정서 판별력 일치 비언어 병목; 선형/소형 비선형 probe; 가역 재표현 대조; 관계·질감 과제; 다수 seed와 길이 일치 캡션을 사용해 동일 held-out 자극에서 각 신경 대비에 고정한 척도의 예측손실 L을 계산한다. 단계별 L(병목)-L(직접특징)을 정서/비정서 대비와 언어/비언어 병목 사이에서 비교한다. 대비 척도·noise ceiling은 훈련/독립 반복으로 고정하고 분모가 불명확한 잔차비율을 만들지 않는다. 용량×선형/소형 비선형 probe×훈련량 곡선을 함께 보고한다.

**scientific_question**: 비정서 판별력과 일반 압축 오차를 맞췄을 때 언어 병목에서 독립 정서 신경 대비에 대한 외부 예측손실이 선택적으로 증가하는가?

**assumption_challenge**: 고정 타깃·관측 support·독립 주석에서 경쟁 설명을 구별한다. 질문은 유지하되 실제 뇌 정보의 소실에서 특정 표현의 정서 대비 예측 접근성으로 주장을 축소한다.

**main_hypothesis**: 일반 압축 오차와 비정서 대비의 난이도·신뢰도를 맞춘 뒤에도 언어 병목의 정서 대비 예측손실 증가가 비언어 병목보다 크고 평가한 readout family에서 남는다.

**alternative**: 차이는 일반 압축, 관계 누락, 표현 좌표, 유한 표본 probe 접근성 또는 캡션 입력범위의 차이다.

**measurable_contrast**: 동일 held-out 자극에서 각 신경 대비에 고정한 척도의 예측손실 L을 계산한다. 단계별 L(병목)-L(직접특징)을 정서/비정서 대비와 언어/비언어 병목 사이에서 비교한다. 대비 척도·noise ceiling은 훈련/독립 반복으로 고정하고 분모가 불명확한 잔차비율을 만들지 않는다. 용량×선형/소형 비선형 probe×훈련량 곡선을 함께 보고한다.

**falsification**: 비선형 probe에서 회복되면 선형 접근성 차이이며 소실 주장을 철회한다. 비언어 병목 또는 관계·질감 대비에서도 같은 감소가 나면 정서·언어 선택성은 지지되지 않는다. 원 신경 대비 신뢰도 부족은 식별불가다.

**baseline**: distortion와 비정서 판별력 일치 비언어 병목; 선형/소형 비선형 probe; 가역 재표현 대조; 관계·질감 과제; 다수 seed와 길이 일치 캡션

**dataset_plan**: Horikawa를 정서 대비의 우선 자료로 설계. NSD는 시각 식별/압축 대조 후보. Mind Captioning은 실제 신경–자극–텍스트 대응이 있는 경우 추가 경로로 연결하며 이름으로 구조를 확정하지 않는다.

**missing_conditions**: ["실제 단계/용량별 특징과 checkpoint", "캡션 available time·입력 provenance", "독립 신경 대비·주석 및 신뢰도", "distortion·비정서 난이도의 공통 지지"]

**source_papers**: ["P081", "P015", "P079", "P051", "P100"]

**closest_prior_ids**: ["P081", "P015", "P051"]

**what_is_new**: 고정된 실제 신경 대비의 예측손실에 대한 병목 종류×대비 종류의 상호작용으로 좁혔다. 단계 성능 차이를 인간 뇌의 정보 소실로 해석하지 않는다.

**novelty_risk**: 정렬 정보보존 연구와 중복될 수 있다. 단순 차원 감소 효과라면 정서 선택성 주장을 철회하고 방법 비교로 축소.

**conceptual_signature**: {"관측대상": "고정 신경 대비의 외부 예측손실", "조작": "언어성×병목용량×probe 유연성", "경쟁설명": "선택적 접근성 저하 대 일반 압축·표현 좌표"}

### 여덟 질문

- q1: 최초성은 미확인이다. 정렬 정보보존 연구와 중복될 수 있다. 단순 차원 감소 효과라면 정서 선택성 주장을 철회하고 방법 비교로 축소.

- q2: P081의 명시적 병목과 P015 공식 중간 경로가 동일 입력의 압축 비교를 구체화한다.

- q3: 고정 타깃·관측 support·독립 주석에서 경쟁 설명을 구별한다. 질문은 유지하되 실제 뇌 정보의 소실에서 특정 표현의 정서 대비 예측 접근성으로 주장을 축소한다.

- q4: 언어 관련 시각 정보 선택을 여러 압축 단계에서 관측할 수 있다; 뇌 설명의 우월성은 미검증이다.

- q5: 언어 목적이 버리는 반복 가능한 대비가 후보지만 잡음·미측정 시각 정보를 먼저 배제한다.

- q6: 실제 Round4 신규 연결: Agent03의 정렬 정보보존 감사와 생성 전후 이중 평가; BLIP-2의 시각→Q-Former 언어 병목

- q7: Horikawa를 정서 대비의 우선 자료로 설계. NSD는 시각 식별/압축 대조 후보. Mind Captioning은 실제 신경–자극–텍스트 대응이 있는 경우 추가 경로로 연결하며 이름으로 구조를 확정하지 않는다.

- q8: 비선형 probe에서 회복되면 선형 접근성 차이이며 소실 주장을 철회한다. 비언어 병목 또는 관계·질감 대비에서도 같은 감소가 나면 정서·언어 선택성은 지지되지 않는다. 원 신경 대비 신뢰도 부족은 식별불가다.

### 역대조

영어 query: `language bottleneck selective affective neural prediction loss nonlinear probes semantic controls`

실행 범위: 기존 canonical 제목에 영어 토큰2개 이상 포함 여부로 로컬 역대조; 근접 ID 직접 대조 병행

로컬 hits: P085, P087

외부 검색 미실행. 로컬 검색 결과는 선행연구 부재의 증거가 아니다.

### 평가10항목

| 항목 | 점수 | 이유 | 불확실성 |

|---|---:|---|---|

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

평가 근거: P081, P015, P079, P051, P100


## C10-02 수정안 — 관계 의미의 설명력과 비가산 신경 예측의 중복을 고정 타깃에서 구별

연구역할: 과학RQ후보

최상위 추천: True; 고정 원타깃의 관계×신경조합 대비가 해석 가능한 양성·음성 결과를 제공하며 기존 관측으로 시작할 수 있어 자기 최상위 후보로 제안한다.

**axis_ids**: ["AS24", "AS16", "AS29"]

**research_question**: 고정된 독립 정서 주석에 대해 관계 설명이 추가될 때 영역 간 비가산 예측 이득의 변화는 일반 의미 설명력 증가와 구별되는가?

**neural_target**: 같은 원 정서 주석 A를 예측하는 신경 D/N의 외부 로그손실 또는 사전 고정 손실; 의미 조건에 따라 A를 잔차화해 바꾸지 않음

**external_principle**: Agent08의 지역/분산 가산/상호작용 경쟁과 개념 병목의 불완전 개념 감사

**model_application**: 독립 중립 관계 설명; 길이·예측력 일치 비관계 설명; 정서결론 포함 민감도 조건; 유연한 영역 내 가산 모형; 공통입력×HRF 합성 null; cross-fitting을 사용해 조건 S마다 동일 원타깃 A에 대해 L(S), L(S+D), L(S+N)을 같은 외부 표본에서 측정한다. g(S)=L(S+D)-L(S+N). 주 비교는 [g(O)-g(O+R)]와 예측력 일치 비관계 대조의 감소 차이이며, 모든 총손실·증분도 병기한다. 관계·정서 불일치의 공통 지지 층을 따로 평가한다.

**scientific_question**: 고정된 독립 정서 주석에 대해 관계 설명이 추가될 때 영역 간 비가산 예측 이득의 변화는 일반 의미 설명력 증가와 구별되는가?

**assumption_challenge**: 고정 타깃·관측 support·독립 주석에서 경쟁 설명을 구별한다. 추정량이 바뀐다는 지적을 수용해 고정 원타깃의 nested predictor 대비로 실질 수정한다.

**main_hypothesis**: 객체 의미 O에서 관계 의미 R로 확장할 때 N-D 이득이 감소하며, 그 감소는 타깃 예측력을 맞춘 비관계 정보 추가보다 크다.

**alternative**: 어떤 타깃 예측력 높은 설명도 동일 감소를 만들거나 관계 추가 후에도 N-D가 유지된다. 감소는 공유정보 대체이며 가짜 신경 효과의 증거가 아니다.

**measurable_contrast**: 조건 S마다 동일 원타깃 A에 대해 L(S), L(S+D), L(S+N)을 같은 외부 표본에서 측정한다. g(S)=L(S+D)-L(S+N). 주 비교는 [g(O)-g(O+R)]와 예측력 일치 비관계 대조의 감소 차이이며, 모든 총손실·증분도 병기한다. 관계·정서 불일치의 공통 지지 층을 따로 평가한다.

**falsification**: 예측력 일치 비관계 설명도 동일 감소를 만들면 관계 특이 가설 약화. 원래 g(O)가 없으면 감소 가설을 식별할 기준점이 없다. 관계 후 g가 남아도 조건부 비가산 필요성만 시사한다.

**baseline**: 독립 중립 관계 설명; 길이·예측력 일치 비관계 설명; 정서결론 포함 민감도 조건; 유연한 영역 내 가산 모형; 공통입력×HRF 합성 null; cross-fitting

**dataset_plan**: Horikawa 우선으로 시행 단위 대비를 설계하고 Emo-FilM·Spacetop에서는 실제 주석 단위에 맞춰 확장한다. Mind Captioning에 설명 자료가 있다면 출처·내용을 검수하는 후보이나 정서 주석을 있다고 가정하지 않는다.

**missing_conditions**: ["설명 생성의 독립 provenance와 중립성 검수", "의미 조건 공통 표본·타깃 척도", "관계와 정서가 불일치하는 지지", "ROI 신뢰도 및 주석 cohort", "UC10-1의 별도 주석예산·외부 평가표본"]

**source_papers**: ["P083", "P084", "P066", "P067", "P100", "P102", "P077"]

**closest_prior_ids**: ["P083", "P067", "P102"]

**what_is_new**: 타깃을 고정한 nested 손실로 의미 추가의 일반 효과와 관계 특이 중복을 구별한다. UC10-1은 다음 관계 주석을 선택하는 별도 측정 설계로 추가되며 원 신경 질문을 대체하지 않는다.

**novelty_risk**: 사건 의미와 정서가 공선적이면 잔차의 고유성은 식별되지 않는다. N 이득도 BOLD 조건부 통계 상호작용이며 인과적 통신은 아니다.

**conceptual_signature**: {"관측대상": "고정 A에서 의미 조건별 N-D 손실차", "조작": "중립 관계 정보 대 예측력 일치 비관계 정보", "경쟁설명": "관계 특정 중복 대 일반 타깃 설명력 증가"}

### 여덟 질문

- q1: 최초성은 미확인이다. 사건 의미와 정서가 공선적이면 잔차의 고유성은 식별되지 않는다. N 이득도 BOLD 조건부 통계 상호작용이며 인과적 통신은 아니다.

- q2: P083/P084의 명시적 개념 경로와 P066/P067의 상태·패턴 분석 도구가 비교 틀을 제공한다.

- q3: 고정 타깃·관측 support·독립 주석에서 경쟁 설명을 구별한다. 추정량이 바뀐다는 지적을 수용해 고정 원타깃의 nested predictor 대비로 실질 수정한다.

- q4: 객체 간 관계·사건 역할을 명시적 특징으로 만들 수 있으나 인간 검수가 필요하다.

- q5: 개념 확장 뒤 재현되는 신경 조합 정보가 후보이며 공통 입력·잡음이 경쟁 설명이다.

- q6: 실제 Round4 신규 연결: UC10-1 다음 자극을 생성하는 대신 어떤 독립 중립 관계 주석을 다음에 수집할지 선택한다. 후보 관계 질의의 기대 정보가 관계특이 중복 가설과 일반 타깃설명력 가설을 얼마나 구별하는지 훈련 자료에서 평가한다.

- q7: Horikawa 우선으로 시행 단위 대비를 설계하고 Emo-FilM·Spacetop에서는 실제 주석 단위에 맞춰 확장한다. Mind Captioning에 설명 자료가 있다면 출처·내용을 검수하는 후보이나 정서 주석을 있다고 가정하지 않는다.

- q8: 예측력 일치 비관계 설명도 동일 감소를 만들면 관계 특이 가설 약화. 원래 g(O)가 없으면 감소 가설을 식별할 기준점이 없다. 관계 후 g가 남아도 조건부 비가산 필요성만 시사한다.

### 역대조

영어 query: `relational semantics conditional neural interaction affect prediction additive nonlinear encoding baseline`

실행 범위: 기존 canonical 제목에 영어 토큰2개 이상 포함 여부로 로컬 역대조; 근접 ID 직접 대조 병행

로컬 hits: P005

외부 검색 미실행. 로컬 검색 결과는 선행연구 부재의 증거가 아니다.

### 평가10항목

| 항목 | 점수 | 이유 | 불확실성 |

|---|---:|---|---|

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

평가 근거: P083, P084, P066, P067, P100, P102, P077


## C10-03 수정안 — 최근성 가산 설명을 넘어선 사건 순서 관련 신경 예측

연구역할: 과학RQ후보

최상위 추천: False; 이번 자기 후보 최상위2개에는 제안하지 않음; 비교·하위 검증으로 보존

**axis_ids**: ["AS23", "AS17", "AS32", "AS35"]

**research_question**: 현재·최근 사건을 고정하고 사건 identity별 lag 기여를 허용해도 순서 관련 관계 표현이 독립 정서 신경 대비의 예측을 추가하는가?

**neural_target**: 과거 입력에 대응하는 시간별 voxel/parcel 반응 및 정서 주석 관련 대비; gradient는 독립적으로 정의한 이차 공간 분석

**external_principle**: Agent08의 문맥 길이 대 HRF 관측모형 경쟁; Agent10의 사건 순서 대 의미량 비교

**model_application**: 현재+최근 k사건; identity×lag 가산모형; causal unordered 표현; 원순서 paraphrase; 개연성 일치 대체순서; 동일 smoothness/FIR; full-film oracle 분리을 사용해 현재와 마지막 k개 사건을 고정한 원순서/먼 과거 교환/lag 가중 bag/원순서 paraphrase를 동일 외부 영화에서 비교한다. 주 추정량은 고정 신경 대비의 예측손실 차이이며 전체 서사 예측도 별도 보고한다. 사건별 available time과 HRF 연산자를 공유하고 train/test 경계에 지원구간 buffer를 둔다.

**scientific_question**: 현재·최근 사건을 고정하고 사건 identity별 lag 기여를 허용해도 순서 관련 관계 표현이 독립 정서 신경 대비의 예측을 추가하는가?

**assumption_challenge**: 고정 타깃·관측 support·독립 주석에서 경쟁 설명을 구별한다. 원 사건집합 비교만으로 recency와 순서를 가를 수 없다는 실제 비판을 반영한다.

**main_hypothesis**: past-only 원순서 표현이 최근성·개연성·smoothness·동일 HRF family를 통제한 기준보다 독립 영화의 정서 신경 대비를 더 잘 예측한다.

**alternative**: 이득은 recency-weighted 내용, 잘못된 순서 입력의 OOD, 미래/완결 사건 서술 또는 관측 평활화 때문이다.

**measurable_contrast**: 현재와 마지막 k개 사건을 고정한 원순서/먼 과거 교환/lag 가중 bag/원순서 paraphrase를 동일 외부 영화에서 비교한다. 주 추정량은 고정 신경 대비의 예측손실 차이이며 전체 서사 예측도 별도 보고한다. 사건별 available time과 HRF 연산자를 공유하고 train/test 경계에 지원구간 buffer를 둔다.

**falsification**: identity×lag 기준과 동등하면 순서 관계 표현의 추가 필요성은 약화된다. 자연스러움·smoothness 일치 후 사라지면 표현 OOD 설명을 지지한다. full-film에서만 나타나면 온라인 과거 주장 기각.

**baseline**: 현재+최근 k사건; identity×lag 가산모형; causal unordered 표현; 원순서 paraphrase; 개연성 일치 대체순서; 동일 smoothness/FIR; full-film oracle 분리

**dataset_plan**: 보유5종을 기반으로 계속 설계한다. Emo-FilM은 실제 연속 주석·평정지연을 사용하는 시간 분석 후보; Spacetop은 확인된 평정 단위에 맞춘 clip 요약 대비로 제한하며 clip 평정을 매 TR 복제하지 않는다. Horikawa는 실제 시행 정보에 맞춘 축소안, NSD는 정적 대조, Mind Captioning은 실제 시점·출처가 있는 경우만 시간 의미 통제로 연결한다.

**missing_conditions**: ["사건 onset/completion 및 caption generation time", "실제 prefix·최근 사건 공통 지지", "독립 영화·주석 cohort·지연", "개연성·smoothness 대조", "실제 HRF 지원구간"]

**source_papers**: ["P085", "P086", "P066", "P100", "P002"]

**closest_prior_ids**: ["P085", "P086", "P066"]

**what_is_new**: 같은 사건집합의 원순서 우위를 recency·OOD·시간관측과 경쟁시키도록 좁혔다. 순서 자체와 순서의 의미를 완전히 분리했다는 주장은 하지 않는다.

**novelty_risk**: 서사 encoding과 중복 위험. 순서를 바꾼 모델 특징의 예측 차이를 실제로 순서를 바꿔 본 뇌의 인과 반응으로 해석할 수 없다.

**conceptual_signature**: {"관측대상": "최근성 기준을 넘는 고정 신경 대비 예측", "조작": "현재/최근 사건 고정 후 먼 과거 순서", "경쟁설명": "순서 관련 관계 대 lag가산·OOD·회고정보"}

### 여덟 질문

- q1: 최초성은 미확인이다. 서사 encoding과 중복 위험. 순서를 바꾼 모델 특징의 예측 차이를 실제로 순서를 바꿔 본 뇌의 인과 반응으로 해석할 수 없다.

- q2: 문맥별 특징 추출 코드와 사건 분절·공간 null 구현이 비교를 구체화한다.

- q3: 고정 타깃·관측 support·독립 주석에서 경쟁 설명을 구별한다. 원 사건집합 비교만으로 recency와 순서를 가를 수 없다는 실제 비판을 반영한다.

- q4: 문맥 순서에 조건부인 관계를 표현할 수 있지만 그 신경 필요성은 시험 대상이다.

- q5: 모델이 잘못된 과거 압축을 하는 경우 남는 시간 대비가 후보이나 HRF와 분리해야 한다.

- q6: 실제 Round4 신규 연결: Agent08의 문맥 길이 대 HRF 관측모형 경쟁; Agent10의 사건 순서 대 의미량 비교

- q7: 보유5종을 기반으로 계속 설계한다. Emo-FilM은 실제 연속 주석·평정지연을 사용하는 시간 분석 후보; Spacetop은 확인된 평정 단위에 맞춘 clip 요약 대비로 제한하며 clip 평정을 매 TR 복제하지 않는다. Horikawa는 실제 시행 정보에 맞춘 축소안, NSD는 정적 대조, Mind Captioning은 실제 시점·출처가 있는 경우만 시간 의미 통제로 연결한다.

- q8: identity×lag 기준과 동등하면 순서 관계 표현의 추가 필요성은 약화된다. 자연스러움·smoothness 일치 후 사라지면 표현 OOD 설명을 지지한다. full-film에서만 나타나면 온라인 과거 주장 기각.

### 역대조

영어 query: `narrative order recency weighted event representations affective brain encoding temporal controls`

실행 범위: 기존 canonical 제목에 영어 토큰2개 이상 포함 여부로 로컬 역대조; 근접 ID 직접 대조 병행

로컬 hits: P009, P028, P029, P066

외부 검색 미실행. 로컬 검색 결과는 선행연구 부재의 증거가 아니다.

### 평가10항목

| 항목 | 점수 | 이유 | 불확실성 |

|---|---:|---|---|

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

평가 근거: P085, P086, P066, P100, P002


## C10-04 수정안 — 관측–prior 비교의 하위 검사: 캡션 단계에서 신경 조건을 사용하는가

연구역할: 방법후보

최상위 추천: False; 이번 자기 후보 최상위2개에는 제안하지 않음; 비교·하위 검증으로 보존

**axis_ids**: ["AS04", "AS20", "AS22"]

**research_question**: 동일 관측 support의 신경 조건을 교환할 때 생성 전 판별 가능한 정서 관련 내용이 캡션 출력에 보존되는가?

**neural_target**: 보류 신경 관측에서 외부 자극 참조·독립 주석과 대응하는 정보; 캡션으로 같은 Y를 다시 설명하는 encoding 순환은 금지

**external_principle**: Agent03의 prior-only/조건 교환 및 생성 전후 이중 평가

**model_application**: 생성 없는 latent retrieval; 원 뇌 readout; 같은 사람/런·SNR·관계·사건단계 matched swap; 비정서 hard-negative; 다수 seed; 동일 prior 설정을 사용해 같은 사람/런의 독립 metadata 매칭 support에서 실제/교환 조건×prior 설정을 비교한다. 고정된 외부 정서 대비와 비정서 내용 판별의 손실을 원 뇌·latent·출력에서 따로 측정한다. latent+/출력+는 보존, latent+/출력-는 출력 손실, latent-/출력+는 prior 보충 또는 probe 한계, 양쪽-는 출처 미식별로 보고한다. 원 뇌 기준의 성공 여부도 병기한다.

**scientific_question**: 동일 관측 support의 신경 조건을 교환할 때 생성 전 판별 가능한 정서 관련 내용이 캡션 출력에 보존되는가?

**assumption_challenge**: 고정 타깃·관측 support·독립 주석에서 경쟁 설명을 구별한다. 교환의 분포 적합성 개선과 관측–prior 가족의 하위 캡션 비교라는 범위 조정을 수용한다.

**main_hypothesis**: 신뢰도·내용·사건단계를 맞춘 유효 신경 조건의 외부 판별 이득이 생성 전 latent와 캡션에 함께 나타난다.

**alternative**: 교환 OOD·신호품질·decoder 접근성 또는 언어 prior의 보충이 차이를 만든다.

**measurable_contrast**: 같은 사람/런의 독립 metadata 매칭 support에서 실제/교환 조건×prior 설정을 비교한다. 고정된 외부 정서 대비와 비정서 내용 판별의 손실을 원 뇌·latent·출력에서 따로 측정한다. latent+/출력+는 보존, latent+/출력-는 출력 손실, latent-/출력+는 prior 보충 또는 probe 한계, 양쪽-는 출처 미식별로 보고한다. 원 뇌 기준의 성공 여부도 병기한다.

**falsification**: matched support에서 실제 조건 이득이 없으면 해당 decoder의 신경 조건 사용을 지지하지 못한다. 원 뇌 정보 부재로 확장하지 않는다. 적합한 교환 표본이 없으면 swap 결론을 내리지 않는다.

**baseline**: 생성 없는 latent retrieval; 원 뇌 readout; 같은 사람/런·SNR·관계·사건단계 matched swap; 비정서 hard-negative; 다수 seed; 동일 prior 설정

**dataset_plan**: Mind Captioning의 정확한 식별자·조건 경로·참조가 실제 확인되면 이 하위 검사를 적용한다. 이름만으로 생성 과제·주석·기억 과제를 가정하지 않는다. 적합한 경로 또는 matched support가 없으면 보유 자극의 생성 없는 latent retrieval 방법 검증으로 축소한다.

**missing_conditions**: ["실제 Mind Captioning 태스크·조건 경로·가중치·prompt", "독립 원자극 참조·정서 주석", "같은 참가자·런·SNR의 교환 support", "캡션 prefix/full-clip provenance", "생성 전 probe의 검출력"]

**source_papers**: ["P015", "P021", "P087", "P076", "P100"]

**closest_prior_ids**: ["P015", "P087", "P076"]

**what_is_new**: 독립적인 새 최상위 RQ로 세기보다 관측–prior 식별 가족에서 캡션 출력의 선택적 보존과 실패 위치를 검사하는 하위 방법으로 정리했다.

**novelty_risk**: 기존 decoder ablation 반복일 수 있다. 정서 대비가 없으면 일반 정보출처 분석에 한정하며 Mind Captioning의 특정 논문을 안다고 가정하지 않는다.

**conceptual_signature**: {"관측대상": "latent에서 출력으로 전달되는 외부 판별 정보", "조작": "support 내 조건 교환×prior 설정", "경쟁설명": "출력 사용 실패 대 prior보충·probe한계·OOD"}

### 여덟 질문

- q1: 최초성은 미확인이다. 기존 decoder ablation 반복일 수 있다. 정서 대비가 없으면 일반 정보출처 분석에 한정하며 Mind Captioning의 특정 논문을 안다고 가정하지 않는다.

- q2: P015/P021의 공개 경로와 P087의 신경–언어 연결 코드가 조건 비교를 가능하게 한다.

- q3: 고정 타깃·관측 support·독립 주석에서 경쟁 설명을 구별한다. 교환의 분포 적합성 개선과 관측–prior 가족의 하위 캡션 비교라는 범위 조정을 수용한다.

- q4: 불완전한 신경 조건을 언어로 완성하지만 바로 그 능력이 정보 기원 혼동을 만든다.

- q5: 모델이 표준 문장으로 평탄화하는 미묘한 대비가 후보이며 생성 전 latent와 비교해야 한다.

- q6: 실제 Round4 신규 연결: Agent03의 prior-only/조건 교환 및 생성 전후 이중 평가

- q7: Mind Captioning의 정확한 식별자·조건 경로·참조가 실제 확인되면 이 하위 검사를 적용한다. 이름만으로 생성 과제·주석·기억 과제를 가정하지 않는다. 적합한 경로 또는 matched support가 없으면 보유 자극의 생성 없는 latent retrieval 방법 검증으로 축소한다.

- q8: matched support에서 실제 조건 이득이 없으면 해당 decoder의 신경 조건 사용을 지지하지 못한다. 원 뇌 정보 부재로 확장하지 않는다. 적합한 교환 표본이 없으면 swap 결론을 내리지 않는다.

### 역대조

영어 query: `brain conditioned caption emotion content provenance matched condition swaps distribution shift`

실행 범위: 기존 canonical 제목에 영어 토큰2개 이상 포함 여부로 로컬 역대조; 근접 ID 직접 대조 병행

로컬 hits: P001, P010, P022, P098

외부 검색 미실행. 로컬 검색 결과는 선행연구 부재의 증거가 아니다.

### 평가10항목

| 항목 | 점수 | 이유 | 불확실성 |

|---|---:|---|---|

| novelty | 2 | 관측–prior 분리와 서명이 겹쳐 독립 RQ 수에 추가하지 않는다. | 상위 가족의 최종 병합은 Coordinator 판단 |

| neuro_importance | 3 | 정서 서술의 신경 기원 과장을 막는 검사다. | 해당 경로 미확인 |

| ai_necessity | 3 | 모듈 접근이 필요하지만 생성 없는 검색으로 일부 대체 가능하다. | 생성 모델 필수성 제한 |

| data_feasibility | 2 | 조건·참조·matched support가 있어야 실행된다. | Mind Captioning 스키마 미확인 |

| rigor | 4 | OOD와 단계별 실패를 명시했다. | 완전한 내용·SNR 매칭 불가 |

| falsifiability | 4 | 단계별 외부 판별과 실제 조건 이득으로 검정 가능하다. | 낮은 신뢰도와 정보 부재 미분리 |

| interpretability | 3 | 방법 범위로 낮춰 인과·정보기원 주장을 제한한다. | 출력만 성공하는 경우 원인 미식별 |

| generalization | 3 | 여러 seed·내용군·prior를 계획한다. | decoder 간 비교 가능한 support 불확실 |

| technical_feasibility | 2 | 실제 conditioner와 checkpoint 접근이 필요하다. | 실행 환경·가중치 미검증 |

| exploration_value | 3 | 주장 감사에 유용하지만 상위 질문의 하위 비교다. | 최상위 연구로 중복될 위험 |

평가 근거: P015, P021, P087, P076, P100


## C10-05 수정안 — 의미 조합 일반화의 실패는 허용 가능한 신경 mapping들에 공통적인가

연구역할: 과학RQ후보

최상위 추천: True; 단일 최선 정렬에 따른 설명 귀속을 여러 허용 mapping의 안정성 문제로 바꾸며 음성 결과도 해석 가능해 자기 최상위 후보로 제안한다.

**axis_ids**: ["AS28", "AS31", "AS24", "AS15"]

**research_question**: 독립 calibration에서 허용되는 여러 신경 mapping과 0/k-shot 조건을 고려할 때 새 관계조합의 정서 대비 예측 저하가 자극표현·mapping·측정 중 어느 설명과 양립하는가?

**neural_target**: 독립 내용 그룹·참가자에서 측정되는 정서 주석 관련 신경 예측 또는 고정 대비; 훈련에서 정한 평가방향 유지

**external_principle**: Agent03의 새 피험자+새 자극 이중 보류와 Agent08의 개인/집단 좌표 변환 구분

**model_application**: anatomy-only zero-shot; 독립 예산 일치 k-shot; 참가자 내 ridge; 자극-only 객체/관계 예측; 여러 허용 정렬; 내용 fingerprint 분할; 반복 신뢰도 일치을 사용해 관측된 공통 자극 cell에서 anatomy-only 0-shot/독립 calibration k-shot/피험자 내 mapping을 평가한다. 허용 mapping은 평가 내용과 분리된 calibration 손실의 사전 허용오차로 정의하고 test로 선택하지 않는다. 새 ID/새 관계조합/새 성분별 고정 정서 대비 손실과 자극-only 관계 손실을 병기한다. 허용 mapping별 결과 범위를 보고하며 이를 posterior나 뇌의 참된 등가군으로 부르지 않는다.

**scientific_question**: 독립 calibration에서 허용되는 여러 신경 mapping과 0/k-shot 조건을 고려할 때 새 관계조합의 정서 대비 예측 저하가 자극표현·mapping·측정 중 어느 설명과 양립하는가?

**assumption_challenge**: 고정 타깃·관측 support·독립 주석에서 경쟁 설명을 구별한다. 가설을 실제 관측 가능한 cell의 일반화 대비로 제한하고 mapping 불확실성을 새 연구 차원으로 추가한다.

**main_hypothesis**: 일부 조합 일반화 차이는 독립 calibration에서 허용된 모든 평가 mapping에서 같은 방향으로 남고 자극-only 조합 판별의 실패와 함께 나타난다.

**alternative**: 실패가 calibration 예산·mapping 선택으로 회복되거나 자극-only는 성공하지만 신경 mapping 또는 주석·신뢰도 차이가 설명한다.

**measurable_contrast**: 관측된 공통 자극 cell에서 anatomy-only 0-shot/독립 calibration k-shot/피험자 내 mapping을 평가한다. 허용 mapping은 평가 내용과 분리된 calibration 손실의 사전 허용오차로 정의하고 test로 선택하지 않는다. 새 ID/새 관계조합/새 성분별 고정 정서 대비 손실과 자극-only 관계 손실을 병기한다. 허용 mapping별 결과 범위를 보고하며 이를 posterior나 뇌의 참된 등가군으로 부르지 않는다.

**falsification**: 허용 mapping에 따라 결론 방향이 바뀌면 mapping에 강건한 조합 실패 가설은 약화된다. 자극-only 성공·calibration 회복이면 언어표현 결손 귀속을 철회한다. 충분한 교차 cell이 없으면 참가자 내 의미 대비만 검정한다.

**baseline**: anatomy-only zero-shot; 독립 예산 일치 k-shot; 참가자 내 ridge; 자극-only 객체/관계 예측; 여러 허용 정렬; 내용 fingerprint 분할; 반복 신뢰도 일치

**dataset_plan**: Horikawa에서 관측 cell과 내용 조합을 확인해 참가자 내 비교부터 시작한다. 공통 자극이 있는 보유본에서만 개인/공유 mapping을 교차한다. NSD는 의미·시각 대조 후보이고 정서 주석을 가정하지 않는다. 다섯 자료의 공통 ontology·참가자·자극을 가정해 pooling하지 않으며 Mind Captioning은 실제 대응이 확인되면 설명 출처 비교에만 연결한다.

**missing_conditions**: ["실제 참가자×자극 cell과 calibration 별도 표본", "각 test성분의 train 등장 여부·관계 조합 support", "주석 cohort·개인 신뢰도", "calibration 허용오차와 mapping family 사전정의", "공통 관측 없으면 참가자 내 fallback"]

**source_papers**: ["P015", "P062", "P083", "P079", "P076", "P098", "P100"]

**closest_prior_ids**: ["P015", "P062", "P076", "P100"]

**what_is_new**: Round2의 단일 정렬×의미 실패 비교를 UC10-2의 허용 mapping 집합에 대한 결론 안정성으로 확장했다. 표현·mapping·측정 중 하나를 무리하게 원인으로 확정하지 않고 가설과 양립하는 범위를 줄인다.

**novelty_risk**: 도메인 일반화·alignment 연구와 중복 가능. 미확인 공통 ontology나 공동 자극 없이 직접 pooling하면 설계가 무효화된다.

**conceptual_signature**: {"관측대상": "새 조합 대비의 mapping별 일반화 범위", "조작": "0/k-shot·허용 mapping family·의미 조합", "경쟁설명": "표현 결손 대 mapping 비유일성·측정 차이"}

### 여덟 질문

- q1: 최초성은 미확인이다. 도메인 일반화·alignment 연구와 중복 가능. 미확인 공통 ontology나 공동 자극 없이 직접 pooling하면 설계가 무효화된다.

- q2: 공유 피험자 decoder와 개인/집단 지도 도구 및 명시적 개념 특징이 두 축의 분리를 구체화한다.

- q3: 고정 타깃·관측 support·독립 주석에서 경쟁 설명을 구별한다. 가설을 실제 관측 가능한 cell의 일반화 대비로 제한하고 mapping 불확실성을 새 연구 차원으로 추가한다.

- q4: 객체·관계의 조합을 표현하고 독립 시험군을 설계할 수 있으나 의미 동등성은 검수해야 한다.

- q5: 개인 공간에 남고 공유 좌표에서 지워지는 재현 가능한 대비가 후보다.

- q6: 실제 Round4 신규 연결: UC10-2 관측과 양립하는 자극 후보의 복수성이라는 구조를 자극 대신 신경 mapping의 복수성으로 옮긴다. 독립 calibration에서 비슷한 손실을 갖는 mapping family를 사전에 허용하고 이후 의미 일반화 결론이 모든 허용 mapping에서 유지되는지 본다.

- q7: Horikawa에서 관측 cell과 내용 조합을 확인해 참가자 내 비교부터 시작한다. 공통 자극이 있는 보유본에서만 개인/공유 mapping을 교차한다. NSD는 의미·시각 대조 후보이고 정서 주석을 가정하지 않는다. 다섯 자료의 공통 ontology·참가자·자극을 가정해 pooling하지 않으며 Mind Captioning은 실제 대응이 확인되면 설명 출처 비교에만 연결한다.

- q8: 허용 mapping에 따라 결론 방향이 바뀌면 mapping에 강건한 조합 실패 가설은 약화된다. 자극-only 성공·calibration 회복이면 언어표현 결손 귀속을 철회한다. 충분한 교차 cell이 없으면 참가자 내 의미 대비만 검정한다.

### 역대조

영어 query: `compositional semantic generalization cross subject brain alignment calibration mapping ambiguity affect`

실행 범위: 기존 canonical 제목에 영어 토큰2개 이상 포함 여부로 로컬 역대조; 근접 ID 직접 대조 병행

로컬 hits: P001, P009, P012, P023, P087

외부 검색 미실행. 로컬 검색 결과는 선행연구 부재의 증거가 아니다.

### 평가10항목

| 항목 | 점수 | 이유 | 불확실성 |

|---|---:|---|---|

| novelty | 3 | 허용 mapping별 결론 안정성은 기존 전이 비교를 확장한다. | 부분 식별·정렬 문헌 중복 미확인 |

| neuro_importance | 4 | 신경 일반화 실패의 표현·좌표·측정 설명을 좁힌다. | 완전 인과 분해 불가 |

| ai_necessity | 3 | 복수 mapping과 개념 모델이 유용하지만 단순 정렬도 핵심 기준이다. | 대형 AI 필수 아님 |

| data_feasibility | 3 | 참가자 내 축소안으로 시작할 수 있다. | 교차 cell과 calibration 자료 미확인 |

| rigor | 4 | test와 독립된 mapping 허용집합·고정 평가를 정의했다. | 허용오차와 후보 family 의존 |

| falsifiability | 4 | mapping 간 방향 불일치와 calibration 회복이 반증이다. | 허용집합 coverage 한계 |

| interpretability | 4 | 원인 확정 대신 양립 가능한 설명의 범위를 보고한다. | 측정 불변성 미확인 |

| generalization | 4 | 새 성분·관계조합·참가자를 명시적으로 분리한다. | 보유본의 support가 불완전할 수 있음 |

| technical_feasibility | 3 | 여러 소형 mapping의 비교는 가능하나 계산량이 늘어난다. | 개인 자료형·정렬 도구 접근 미확인 |

| exploration_value | 4 | 일반화 실패의 과잉 신경 해석을 줄이는 새로운 질문이다. | 최초성 미확정 |

평가 근거: P015, P062, P083, P079, P076, P098, P100


## 한계

- 본 산출물은 실제 Agent05·09의 비판10개를 읽고 후보5개에 응답한 Round4다. 두 의견의 차이와 미해결 해석을 보존했다. Round5 완료는 주장하지 않는다.

- 후보5개 필수필드를 보존했고 평가10항목과 영어 역검색어를 추가했다. 새 외부 웹 검색은 수행하지 않았다. 실제 실행한 검색은 로컬 canonical 제목 토큰 매칭과 근접 문헌 역대조이며 세계 최초를 확정하지 않는다.

- UC10-1·UC10-2의 원문 근거는 기존 catalog의 본문/코드 범위를 계승한다. 새 신경 연결과 적응 주석·허용 mapping 설계는 E3이며 실행하지 않았다.

- 최상위 자기 추천은 C10-02·C10-05 두 개다. C10-04는 관측–prior 가족의 방법후보로 분리해 별도 최고위 연구 수를 늘리지 않는다. 점수는 자동 가중합이 아니다.

- 보유5종은 사용자 진술로 반영한다. Mind Captioning의 식별자·주석·입출력·기억/심상 과제는 추정하지 않으며 스키마 확인은 실제 분석 조건으로 남긴다.

- 모델·뇌 분석·신규 주석·생성 실험·새 인간 측정은 수행하지 않았다. 같은 뇌→캡션→같은 뇌의 순환, 동일 주석의 선택/평가 재사용을 금지한다.

- 자기 round04_revision.json/md만 작성했으며 공유/Git/상대 파일은 수정하지 않았다.
