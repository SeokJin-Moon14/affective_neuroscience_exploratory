# Agent04 Round4: 실제 비판 응답과 수정 후보

2026-11-12. 실제 비판 10건에 응답한 후보 5개, 새 연결 3개. 원자료/모델 분석 결과가 아닌 E3 제안이다.

## C04-01 비판 응답

근거 비판: R3-03-C04-01, R3-11-C04-01

**판정:** 수정 후 과학RQ후보 유지. 두 비판은 정보량과 접근성 혼동을 공통 지적했다. 이중 표적·readout 학습곡선으로 해석 범위를 좁히고 중복 집계를 방지한다.

**수용 수정**

- 선택적 정보 소실이라는 제목/일차 주장을 선택적 접근성으로 좁힌다.
- 동일 architecture·입력·augmentation·mask 계열·자료량뿐 아니라 목적별 수렴, rank×probe 용량×학습량 곡선을 비교한다.
- 복원 성능–A 접근성 Pareto 비교와 비정서·저분산 주입 대조를 추가한다.
- C03-01과 동일 상위 RQ로 병합할 것을 권고하고, neural-only 목적과 brain-to-visual 목적을 하위 요인으로 구분한다.

**남는 이견/제한**

- 어떤 유한 probe 계열도 전체 정보 부재를 증명하지 못한다는 비판을 수용한다. 다만 수렴·대조를 통과한 접근성의 선택적 변화는 실용적 신경표현 평가의 과학적 제한으로 유지한다.
- 같은 FLOPs와 같은 수렴을 동시에 완벽히 맞추기 어렵다. 고정 예산 결과와 수렴 수준을 맞춘 결과를 별도 estimand로 보고한다.

## C04-02 비판 응답

근거 비판: R3-03-C04-02, R3-11-C04-02

**판정:** 수정 후 과학RQ후보 유지. 신경 입력의 우월성을 당연한 정보량 차이와 측정 잡음 공유로부터 구별하고 정서 대비를 명시적 손실로 측정하도록 수정한다.

**수용 수정**

- 동시 공간완성과 과거 전용 예측을 분리하며 이번 우선 분석은 공간완성으로 고정한다.
- S+동일 반복 N과 S+독립 반복 N을 구분하고 다른 자극/같은 run의 N을 대조한다.
- target 및 buffer를 공간 변환·tokenization 이전부터 제외하고, 포함 관계에 맞춘 mask 폭과 의미 보강의 전체 민감도곡선을 보고한다.
- 지도 겹침 대신 독립 A 가중 신경 대비의 예측손실 차이를 일차 추정량으로 정의한다.

**남는 이견/제한**

- 독립 반복에서 남는 효과도 내부 상태와 미모형화 자극 정보를 구별하지 못한다. 특정 S와 관측 조건에 상대적인 재현 가능한 N의 추가 예측으로만 해석한다.
- 엄격한 past-only N과 동시 다른 공간 N은 입력 가용성이 다르므로 같은 causal 예측 점수로 비교하지 않는다.

## C04-03 비판 응답

근거 비판: R3-03-C04-03, R3-11-C04-03

**판정:** 수정 후 과학RQ후보 유지. null-space 잔차 복구라는 직접 조작으로 평균의 충분성을 검정하고 기존 반증 논리의 혼동을 제거한다.

**수용 수정**

- 일차 일반 공간평균 상쇄와 이차 atlas 경계 특이성을 분리한다.
- parcel mean과 within-parcel zero-mean 잔차의 독립 A 예측 접근성을 직접 비교한다.
- 정보량 일치라는 표현을 제거하고 rank·복원오차·공간 주파수·신뢰도 중 실제 맞춘 지표를 명시한다.
- SNR 보정이 신호 손실 효과를 제거할 수 있으므로 원 효과와 train-only 보정 효과를 모두 보고한다.

**남는 이견/제한**

- random parcel에서도 손실이 같으면 atlas 특이성만 약화되고 평균화 일반 가설은 남는다는 두 비판을 전부 수용한다.
- 신뢰도 일치 대조는 nuisance 보정 estimand이며 원자료 평균화의 총 효과와 동일하지 않다. 어느 하나만 정답으로 선택하지 않는다.

## C04-04 비판 응답

근거 비판: R3-03-C04-04, R3-11-C04-04

**판정:** 수정 후 과학RQ후보 유지. 개인의 재현 정보와 공통정보의 좌표차이를 구별하도록 경쟁 모형 자체를 바꾼다.

**수용 수정**

- 정렬 regularization과 subject 평균화를 독립 요인으로 분리한다.
- 공통 latent+개인 gain/rotation/affine 관측 map과 공통+개인 추가 latent를 같은 readout·rank 예산에서 비교한다.
- 개인 intercept/scale을 넘는 A 관련 slope의 새 자극·새 세션 안정성을 일차 표적으로 고정한다.
- C12-05와 상위 공유/개인정보 RQ는 통합하고 본 후보는 관측 좌표군의 충분성으로 특화한다.

**남는 이견/제한**

- 반복 가능한 개인 residual 자체를 private 계산이라고 부르지 않는다. 허용한 관측 map 밖의 추가 예측만 말한다.
- 가역 affine map의 실패는 모든 nonlinear 가역 map 실패를 뜻하지 않는다. 허용 좌표군을 사전 고정하고 결과의 범위를 그 군으로 제한한다.

## C04-05 비판 응답

근거 비판: R3-03-C04-05, R3-11-C04-05

**판정:** 수정 후 과학RQ후보 유지. 일반 비선형 용량과 상태 전이 선택성을 분리하여 관측격자에 견고한 결과의 해석을 제한한다.

**수용 수정**

- 고정 전이+동일 비선형 입력/출력, 고정 전이+입력 gate, 입력 의존 전이의 세 모형을 비교한다.
- fixed SSM+nonlinear readout·nonlinear AR·gate 고정/교환 대조를 추가한다.
- 실시간 과거 길이·대역폭·자료량·훈련 목표를 일치시키고 gate별 연산량 및 수렴 차이를 기록한다.
- 같은 위상변화를 모든 채널에 적용하는 multivariate surrogate의 보존 성질과 한계를 명시한다.

**남는 이견/제한**

- 견고한 selective 이득도 인간 신경 gate의 필요성을 증명하지 않는다. 관측상 필요한 이력 함수군의 구별로만 해석한다.
- gate 교환은 OOD를 유발할 수 있으므로 제어 조건에서 재학습한 모델과 test-time 교환을 따로 보고한다.

## UC04-01 — 역문제·관측 영공간 감사

**original_computational_goal:** P076은 잡음 있는 역문제에서 관측 제약과 생성 prior를 결합해 가능한 해를 찾는다. 정확한 posterior 보장이나 fMRI 적용 결과는 확인되지 않았다.

**imported_structure:** 관측 연산이 같은 값을 내는 방향을 직접 구성하고 그 방향이 외부 표적을 바꾸는 witness인지 검사한다. 여기서는 생성기 대신 알려진 parcel 평균 행렬의 null space를 정확히 구성한다.

**new_neural_question:** 동일한 parcel 평균을 유지하면서 바뀌는 재현 공간 대비가 A 관련 예측을 바꾸는가?

**why_not_same_as_round2:** 단순 표현 유사도/병목 전후 성능이 아니라 Gr=0인 소거 성분을 정의해 재추가하는 판별 조작이 새로 생겼다. 일반 평균화와 atlas 특수성을 별도 가설로 분해한다.

**discriminating_test:** m/m+r_k/m+noise를 실제/random atlas에서 비교하고 A·matched 비정서 대비를 외부 자극에서 평가한다.

**failure_interpretation:** r의 추가 예측이 없으면 지정한 관측/추정 조건에서 평균의 충분성을 지지한다. random atlas에서도 효과면 일반 평균 상쇄이고 atlas 특이성은 아니다.

**evidence_scope:** P076 공식 코드/초록 기반 원리 및 P026 공식 구현; null-space 설계와 신경 전이는 E3.

근거: P076, P026, P060. 연결 후보: C04-03.

## UC04-02 — 알고리즘 비교의 관측 동치 통제·가역 좌표군

**original_computational_goal:** P051은 어떤 변환을 허용해야 표현 비교가 구별력을 가지는지, P096은 predictive coding과 backprop 계산을 비교하는 문제를 다룬다. P096의 원문 등가 정리 전체는 미확인이다.

**imported_structure:** 표현의 좌표/관측 map만 다른 모형과 추가 상태가 필요한 모형을 분리하고, 알려진 동치 생성자료를 음성대조로 사용한다.

**new_neural_question:** 안정된 개인 잔차는 공통 latent의 gain/rotation/affine 관측 차이로 설명되는가, 그 지정군을 넘어서는 개인 성분이 필요한가?

**why_not_same_as_round2:** shared/private 잔차의 재현성만 검사했던 질문에 명시적 허용 좌표군과 coordinate-only recovery 대조를 도입해 새 경쟁모형을 만든다.

**discriminating_test:** known B_s z 모의 관측과 known-private 관측을 구별하는지 먼저 검사한 뒤 공통+affine 대 공통+private의 외부 A neural slope 손실을 비교한다.

**failure_interpretation:** affine map으로 충분하면 개인 적응의 이득을 추가 계산보다 관측 좌표 보정으로 해석한다.

**evidence_scope:** 좌표 불변성은 P051 본문 기록, P096은 공식 코드/문서 기록에 한정; 신경 전이는 E3.

근거: P051, P055, P096. 연결 후보: C04-04.

## UC04-03 — 계산 구조의 동치/비동치와 recurrence 대 depth 비교

**original_computational_goal:** P090은 얕은 재귀 시각모형의 계산 성능을, P096은 다른 학습 계산의 대응을, P034는 입력 의존 selective sequence 계산을 다룬다.

**imported_structure:** 최종 예측 성능이 다른 경우 비선형성의 존재와 위치를 별도 요인으로 고정하여 어느 계산 경로가 필요한지 반례를 찾는다.

**new_neural_question:** A 관련 이력 예측의 이득은 nonlinear observation만으로 충분한가, 고정 전이의 gated input 또는 입력 의존 전이가 추가로 필요한가?

**why_not_same_as_round2:** 관측격자×fixed/selective 이분법에 input gate와 transition gate를 분리하는 세 함수족 대조를 추가해 용량 혼동을 직접 겨냥한다.

**discriminating_test:** F0/F1/F2와 nonlinear AR를 같은 격자·대역폭에서 비교하고 A contrast 이득이 전이 선택성에만 남는지 본다.

**failure_interpretation:** F1 또는 nonlinear AR로 충분하면 선택 전이 기전 주장을 버리고 더 단순한 관측 예측 함수군을 채택한다.

**evidence_scope:** P090/P096/P034의 기존 공식 코드 검토 범위이며 논문 전체 등가성 재검증 아님; 신규 함수족 실험은 E3.

근거: P090, P096, P034. 연결 후보: C04-05.

## 수정 C04-01 — 사전학습 목표가 재현 정서 대비의 접근성을 선택적으로 바꾸는가?

연결축: AS07, AS13, AS24. 역할: 과학RQ후보. 최상위 추천: False — C03-01과 상위 RQ로 통합 권고; 독립 최상위 후보로 이중 선정하지 않음.

**research_question:** 동일 신경 입력과 encoder에서 사전학습 목적을 바꿀 때, 전체 신호 복원 수준과 readout 학습곡선을 고려해도 독립 정서 대비의 접근성이 달라지는가?

**neural_target:** 피질 시계열 또는 대응되는 자극 단위 신경 패턴의 반복 재현 성분과 독립 정서 주석 관련 대비

**model_application:** SwiFT/CortexMAE/Brain-JEPA 공개 체크포인트 비교는 탐색 자료다. 주검정은 동일 encoder·공간·입력·decoder/head 예산에서 복원/latent-prediction/contrastive objective를 구현한 소규모 신규 비교다. 목표별 target network 등 필수 구조 차이는 별도 명시한다.

**scientific_question:** 예측가능한 일반 신경 구조와 독립 A 관련 대비가 같은 목적함수의 충분한 표현으로 함께 회수되는지 검정한다.

**assumption_challenge:** 범용 복원 성능이 높은 표현이면 모든 신경 표적을 같은 표본·readout 예산에서 읽을 수 있다는 가정. 무한 함수군의 정보량 동일성은 검정하지 않는다.

**main_hypothesis:** 일치 복원 수준·비정서 대비 신뢰도에서 A 총/조건부 접근성의 목적별 차이가 probe 용량·학습량 곡선의 일부 또는 전반에 유지된다.

**alternative:** 차이는 수렴·rank·입력 증강·mask·readout의 유한 표본 또는 분산 규모 차이이며 지정한 강한 probe로 회수된다.

**measurable_contrast:** 동일 입력의 objective×rank를 교차하고 각 조건에서 probe 용량×학습 표본수 곡선을 얻는다. 예산 고정 결과와 수렴 기준 고정 결과를 분리한다. 훈련 기준으로 정한 복원오차 허용영역 안에서 독립 자극 A 예측의 총 점수 및 V,S를 추가한 조건부 증분을 각각 비교한다. 비정서 대비는 분산·신뢰도·공간 주파수 범위를 명시해 맞춘다. Pareto 지배는 관측된 grid와 오차막대 범위에서만 주장한다.

**falsification:** 강한 probe에서 차이가 회수되면 좌표 접근성 재배치로 분류한다. 수렴/복원 수준 일치 뒤 목적 차이에 대한 CI가 사전 동등성 범위 안이면 선택적 접근성 차이를 반박한다. raw Y의 A 신뢰도가 부족하면 식별불가다. 모든 probe 실패도 정보이론적 부재를 증명하지 않는다.

**what_is_new:** 원래 자기지도 효율·범용 성능 문제를 동일 복원 수준에서 읽을 수 있는 정서 대비의 표본·함수 예산 의존성으로 바꾼다. Round3 이후 단일 probe 손실에서 곡선 전체의 접근성으로 추정량을 수정했다.

**novelty_risk:** C03-01과 상위 질문이 중복한다. 통합 RQ 아래 neural-only 대 시각 정렬 목표의 하위 가설로 유지하며 별도 독립 RQ 수를 늘리지 않는다.

**기준과 실행 조건:** raw ridge; 차원 일치 PCA와 random projection; 미학습 encoder; 동일 encoder의 MAE/latent-prediction/contrastive 목적 비교; 검수 사건 목록을 늘린 의미 기준; 분산 whitening 유무의 별도 estimand; known low-variance 신호를 A와 독립적으로 주입한 synthetic recovery; rank/복원오차/수렴/probe 학습곡선 일치 비교 / 사전학습 corpus 중복; 목표별 동일 입력/예산을 구성할 코드; checkpoint별 실제 config와 load; A와 Y의 독립 신뢰도; 재현 가능한 반복 또는 대체 신뢰도 설계

**영어 역검색:** fMRI pretraining objectives emotion representation accessibility matched reconstruction probe capacity

실제 요청 결과: proxy tunnel 403; 검색 결과 미접근. canonical 근접 선행 대조만 유효.

**평가(자동 합산 없음)**

| 항목 | 점수 | 근거 | 불확실성 |
|---|---:|---|---|
| novelty | 3 | 목적×접근성 곡선은 구별되나 C03-01 및 기존 probing과 가까움 (P025, P026, P033) | 외부 영어 역검색 요청은 proxy 403으로 결과 미접근; 최신 선행 배제 불가. |
| neuro_importance | 4 | 범용 신경표현의 표적 충분성을 제한함 (P025, P026, P033) | 독립 A/신경 대비가 실제 검출 가능해야 과학적 중요성이 실현됨. |
| ai_necessity | 3 | 목표함수 통제에는 학습 모델이 필요하나 대형 foundation 모델은 필수가 아님 (P025, P026, P033) | 강한 작은 모형이 충분하면 foundation model 필요성 점수를 추가로 낮춰야 함. |
| data_feasibility | 3 | A/신경 신뢰도와 독립 split이 확인되면 정적 가지도 가능 (P025, P026, P033) | 다섯 자료 보유는 확인되었으나 로컬 버전·스키마·반복·주석은 미검증. |
| rigor | 4 | 수렴·rank·probe 곡선으로 주요 confound를 드러냄 (P025, P026, P033) | 제안한 통제는 아직 실행하지 않았고 표본수에 따른 검정력은 미확인. |
| falsifiability | 4 | 동등성/회수/미식별 결과를 명시함 (P025, P026, P033) | 동등성 문턱과 신뢰도는 실자료의 개발 표본에서 결과 확인 전 고정해야 함. |
| interpretability | 4 | 정보 부재 대신 유한 접근성으로 제한함 (P025, P026, P033) | 관찰 예측 결과는 인간 뇌 인과나 고유 정보량을 확정하지 못함. |
| generalization | 4 | 새 내용군·피험자에서 같은 곡선 검증 가능 (P025, P026, P033) | 실제 독립 자극/참가자/세션 수와 사전학습 중복이 미확인. |
| technical_feasibility | 2 | 같은 encoder의 여러 objective 구현·학습이 필요함 (P025, P026, P033) | checkpoint load·GPU/시간·정확한 입력 지원은 아직 실행 검증하지 않음. |
| exploration_value | 4 | 성능순위와 표적 보존이 갈리는 조건을 찾음 (P025, P026, P033) | 새 연결의 유용성은 대조 모형이 관측 후 구별되는지에 달림. |

**여덟 질문**

1. 관련 방법 선행이 존재하고 최초 여부는 미확정이다. 영어 역검색은 시도했으나 proxy 403으로 실패했고 기존 canonical 근접 문헌만 대조했다.
2. 공개 fMRI MAE·JEPA·contrastive 구현으로 목적의 통제 비교를 설계할 수 있다.
3. 범용 복원 성능이 높은 표현이면 모든 신경 표적을 같은 표본·readout 예산에서 읽을 수 있다는 가정. 무한 함수군의 정보량 동일성은 검정하지 않는다.
4. 분산 시공간 상관과 예측가능 공통구조를 재사용할 수 있다.
5. 작지만 반복되는 A 관련 대비가 압축될 가능성은 E3이며 먼저 raw 신호의 신뢰도를 확인한다.
6. Agent07의 정보 보존/좌표 불변성 구별 + Agent10의 의미 측정 오차 감사
7. 기존 정서 자료를 분류 성능 대신 학습 목적에 따른 신호 보존 시험에 사용한다.
8. 강한 probe에서 차이가 회수되면 좌표 접근성 재배치로 분류한다. 수렴/복원 수준 일치 뒤 목적 차이에 대한 CI가 사전 동등성 범위 안이면 선택적 접근성 차이를 반박한다. raw Y의 A 신뢰도가 부족하면 식별불가다. 모든 probe 실패도 정보이론적 부재를 증명하지 않는다.

근거: P025, P026, P029, P051, P083, P032, P033. 모델 구현 지원은 기존 확인 범위이며 새 가중치 실행 없음.

## 수정 C04-02 — 독립 반복의 신경 문맥이 자극모형 밖 정서 대비 예측을 회수하는가?

연결축: AS08, AS24, AS29. 역할: 과학RQ후보. 최상위 추천: False — 상대적 조건부 예측 질문은 유효하나 반복/입력 비대칭과 해석 한계로 후순위.

**research_question:** 사전 정의한 자극모형 S에 신경 문맥 N을 추가할 때, 독립 반복 간에 전달되는 A 관련 신경 대비의 예측 이득이 같은 반복 잡음 공유와 구별되는가?

**neural_target:** 공통 피질 mask의 target 공간 블록 Y와 독립 A 가중 신경 대비. 우선 동시 공간완성으로 한정하며 과거 예측은 별도 후속 가지다.

**model_application:** TRIBE v2의 video/audio/text→평균 fsaverage5 피질 출력을 target 공간에 맞추고 train-only 개인 보정을 적용한다. CortexMAE/Brain-JEPA latent를 사용한 N→Y head는 별도 구현이다. masking을 normalization·smoothing·tokenization보다 앞에 적용하며 pretrained 모델이 그 mask를 처리하는지 단위 실행 검증을 요구한다. 미지원이면 masked raw-context ridge로 축소한다.

**scientific_question:** 같은 관측의 잡음 공유를 넘어 재현되는 신경 문맥이 현재 자극 표현의 예측 충분성에 추가로 필요한지 검사한다.

**assumption_challenge:** 신경문맥 추가 이득이 곧 내부 상태 또는 자극에 없는 정서 정보라는 해석을 검정한다.

**main_hypothesis:** 동일 자극의 반복 a에서 얻은 N이 반복 b의 target Y에서 A 가중 대비 예측을 개선하며, 다른 자극/동일 run N과 의미 강화 baseline을 넘는 부분이 남는다.

**alternative:** 동일 반복에서만 이득이 있으면 공통 잡음·smoothing, 의미 강화로 줄면 누락 자극 표현, 모든 N에서 같으면 run/global nuisance가 설명한다.

**measurable_contrast:** 각 held-out 자극 집합에서 사전 고정한 A 대비 가중치 w(합0, 제곱합1)로 c_A(Y)=Σ_i w_iY_i를 계산한다. w는 독립 주석의 고정 차원/고저 대비로 만들며 test BOLD나 model fit에 맞춰 고르지 않는다. L_A=||c_A(Y)-c_A(Yhat)||²_Q에서 Q는 training-only noise precision이다. Δ_A=L_A(S)-L_A(S+N)을 동일 반복 N, 독립 반복 N, 같은 run 다른 자극 N에서 비교한다. 전체 Y 손실과 A 비관련 일치 대비의 개선을 별도로 보고한다. 의미 보강×mask 폭 전체 곡선을 제시한다.

**falsification:** 독립 반복 N의 Δ_A가 사전 최소효과 이하라는 충분히 좁은 CI를 보이면 반복 전이 이득 가설을 반박한다. 동일 반복에만 남으면 공통 측정변동 설명을 강화한다. 의미 보강으로 사라지면 지정 S의 부족으로 분류한다. 반복·A 신뢰도가 부족하면 미식별이며 모든 자극모형 충분성은 주장하지 않는다.

**what_is_new:** 원 비교의 A 지도 겹침을 명시적 A contrast 예측손실로 바꾸고 동일/독립 반복 입력의 비대칭을 주조작으로 만든다. residual의 원인 분해를 완수했다는 주장은 철회한다.

**novelty_risk:** variance partitioning 재적용 위험이 높다. target 누출 방지와 의미 강화에 따른 불일치의 감소/잔존을 일차 판별로 고정한다.

**기준과 실행 조건:** 저수준+사건 의미+FIR ridge; TRIBE 공개 평균 출력에 train-only 개인별 선형 보정; masked raw-neighbor ridge; 자기상관을 보존한 surrogate; 단순 nonlinear 자극 encoding; S+독립 반복 N; S+다른 자극/동일 run N; target 거리별 사전 masking과 global/run nuisance; 동일 입력을 갖는 raw-context ridge / 공통 cortical mask와 시간 정렬; TRIBE checkpoint의 최종 TR/config와 5초 offset 처리; brain model의 실제 mask token/보류 블록 동작; 개인 평균 출력과 개인 Y 차이의 통제; 독립 반복 및 개념 probe용 별도 자극; 반복 a/b의 동일 자극 대응과 nuisance 독립성; A 대비 w와 loss Q의 사전 정의; 전처리 이전 mask가 feature 전파를 차단하는 실제 동작

**영어 역검색:** stimulus encoding neural context independent repetition emotion prediction shared measurement noise

실제 요청 결과: proxy tunnel 403; 검색 결과 미접근. canonical 근접 선행 대조만 유효.

**평가(자동 합산 없음)**

| 항목 | 점수 | 근거 | 불확실성 |
|---|---:|---|---|
| novelty | 3 | 독립 반복×마스크×의미 강화가 잔차 비교를 구체화함 (P026, P027, P083) | 외부 영어 역검색 요청은 proxy 403으로 결과 미접근; 최신 선행 배제 불가. |
| neuro_importance | 4 | 자극모형의 관측 예측 충분성을 실제 반복으로 제한함 (P026, P027, P083) | 독립 A/신경 대비가 실제 검출 가능해야 과학적 중요성이 실현됨. |
| ai_necessity | 2 | raw-context ridge로도 첫 판별이 가능함 (P026, P027, P083) | 강한 작은 모형이 충분하면 foundation model 필요성 점수를 추가로 낮춰야 함. |
| data_feasibility | 2 | 독립 반복과 같은 자극의 N/Y 대응이 필수이나 미확인 (P026, P027, P083) | 다섯 자료 보유는 확인되었으나 로컬 버전·스키마·반복·주석은 미검증. |
| rigor | 4 | A contrast loss와 전처리 이전 masking을 명시함 (P026, P027, P083) | 제안한 통제는 아직 실행하지 않았고 표본수에 따른 검정력은 미확인. |
| falsifiability | 4 | 같은 반복/독립 반복의 대안별 예측이 다름 (P026, P027, P083) | 동등성 문턱과 신뢰도는 실자료의 개발 표본에서 결과 확인 전 고정해야 함. |
| interpretability | 3 | 미모형화 자극과 내부 상태는 여전히 분리 불가 (P026, P027, P083) | 관찰 예측 결과는 인간 뇌 인과나 고유 정보량을 확정하지 못함. |
| generalization | 3 | 새 자극·세션 전이가 가능하지만 반복 조건 제약이 큼 (P026, P027, P083) | 실제 독립 자극/참가자/세션 수와 사전학습 중복이 미확인. |
| technical_feasibility | 2 | TRIBE config·개인 보정·mask 지원과 공통 공간 확인 필요 (P026, P027, P083) | checkpoint load·GPU/시간·정확한 입력 지원은 아직 실행 검증하지 않음. |
| exploration_value | 4 | 뇌조건부 추가 이득의 기원을 과장하지 않는 시험임 (P026, P027, P083) | 새 연결의 유용성은 대조 모형이 관측 후 구별되는지에 달림. |

**여덟 질문**

1. 관련 방법 선행이 존재하고 최초 여부는 미확정이다. 영어 역검색은 시도했으나 proxy 403으로 실패했고 기존 canonical 근접 문헌만 대조했다.
2. 자극→피질 예측과 fMRI→latent 구현이 같은 자료에서 비교 가능한 도구를 제공한다.
3. 신경문맥 추가 이득이 곧 내부 상태 또는 자극에 없는 정서 정보라는 해석을 검정한다.
4. 멀티모달 자극의 비선형 결합과 신경 내 통계구조를 각각 포착할 수 있다.
5. 모형군이 누락한 재현 성분은 후보이나 정서 고유성은 미확인이다.
6. Agent10의 개념 누출 감사·복수 설명 불확실성 + Agent07의 shared/private 비식별성
7. 같은 자연자극 뇌자료를 두 조건부 예측의 적용범위 비교에 사용한다.
8. 독립 반복 N의 Δ_A가 사전 최소효과 이하라는 충분히 좁은 CI를 보이면 반복 전이 이득 가설을 반박한다. 동일 반복에만 남으면 공통 측정변동 설명을 강화한다. 의미 보강으로 사라지면 지정 S의 부족으로 분류한다. 반복·A 신뢰도가 부족하면 미식별이며 모든 자극모형 충분성은 주장하지 않는다.

근거: P026, P027, P029, P053, P080, P083. 모델 구현 지원은 기존 확인 범위이며 새 가중치 실행 없음.

## 수정 C04-03 — parcel 평균이 지운 내부 공간 대비는 정서 관련 예측에 필요한가?

연결축: AS07, AS13, AS16. 역할: 과학RQ후보. 최상위 추천: True — 동일 자료의 정확한 집계 연산과 영공간 복구가 반증을 명료하게 하며 checkpoint 없이 첫 검정 가능. AI 필요성은 낮다는 평가도 보존.

**research_question:** 동일 피질 관측에서 parcel 평균에 의해 제거되는 zero-mean 성분이 독립 정서 대비 예측을 회수하며, 그 효과는 특정 atlas 경계에 의존하는가?

**neural_target:** 같은 dense 피질 y의 parcel 평균 투영 Py와 null-space 잔차 (I-P)y. 하위피질 또는 실제 뇌의 압축 연산으로 일반화하지 않는다.

**model_application:** 서로 겹치지 않는 parcel 평균 행렬 G에 대해 P=Gᵀ(GGᵀ)⁻¹G를 고정하고 m=Py,r=(I-P)y로 나누면 Gr=0이다. 이는 명시한 선형 집계의 대수적 성질이다. train-only PCA로 r의 k차원 좌표를 정하고 m/m+r_k/m+noise를 같은 readout으로 비교한다. CortexMAE variant는 이후 표현의 추가 변형을 검사하는 도구이며 이 직접 대조에 필수 가중치가 아니다.

**scientific_question:** 지역 평균만으로 A 관련 신경 대비를 읽기에 충분한지, 평균이 상쇄한 재현 가능한 공간 대비가 필요한지 검정한다.

**assumption_challenge:** atlas 평균이 신호잡음만 개선하는 중립적 축약이라는 가정. 일반 평균화와 특정 atlas 경계의 효과를 나눈다.

**main_hypothesis:** H1: m+r_k가 m보다 보류 자극 A 예측을 재현 가능하게 개선한다. H2: 공간 주파수·rank·신뢰도 지표를 명시해 맞춘 뒤 실제 atlas와 random-contiguous parcel의 H1 효과가 다르다. A 선택성은 matched 비정서 대비와의 별도 상호작용이다.

**alternative:** H1 이득이 없으면 평균 충분성 또는 낮은 검정력, H1은 있으나 H2가 없으면 일반 평균 상쇄, 비정서 대비와 같으면 표적 비특이 미세 공간정보다.

**measurable_contrast:** 주 추정량은 외부 자극에서 A 예측손실 L(m)-L(m+r_k)이며 V,S를 포함/미포함한 총·조건부 버전을 분리한다. 잔차는 다른 반복에서 신뢰도를 확인하고 m+rank-matched noise 및 m+spatial-spectrum-matched control과 비교한다. 실제/무작위 연속 parcel은 같은 원 y에서 생성한다. 신뢰도 보정 전 총 효과와 train-only 신뢰도/공간대역 보정 효과를 병행하며 보정 후 결과만 선택하지 않는다.

**falsification:** H1은 반복 신뢰도가 충분한 r_k를 더해도 A 접근성 개선의 CI가 동등성 범위 안이면 반박한다. H2는 실제/random atlas 효과 차이가 동등하면 반박한다. random parcel에서도 H1이 유지되는 것은 H1의 반증이 아니다. 비정서 대비도 동일하면 정서 선택성만 반박한다. rank 일치를 정보량 일치라고 부르지 않는다.

**what_is_new:** 단순 P/F/V 성능 비교에서 집계 연산의 영공간에 실제 예측 가능한 대비가 존재하는지 묻는 witness 검사로 변경했다. 일반 평균 상쇄·경계 특이성·정서 선택성에 서로 다른 반증을 부여한다.

**novelty_risk:** 기존 multivoxel 대 ROI-average 비교와 가까우므로 신규성은 중간 이하로 둔다. 독립 반복의 null-space witness와 세 가설의 분리가 없으면 방법 QC로 낮춘다.

**기준과 실행 조건:** m-only ridge; m+within-parcel zero-mean k차원; m+rank-matched noise; spatial-spectrum-matched random aggregation; 실제 atlas 대 random contiguous atlas; 독립 비정서 대비의 분산/신뢰도/공간 주파수 대조 / 동일 참가자의 dense와 parcel 변환 가능성; 정확한 cortical vertex/voxel 대응; 반복 신뢰도; 표면 재등록 및 smoothing 정보; CortexMAE variant별 학습 차이

**영어 역검색:** fMRI parcel averaging within parcel zero mean residual emotion representation

실제 요청 결과: proxy tunnel 403; 검색 결과 미접근. canonical 근접 선행 대조만 유효.

**평가(자동 합산 없음)**

| 항목 | 점수 | 근거 | 불확실성 |
|---|---:|---|---|
| novelty | 3 | ROI 평균 대 패턴은 기존이며 null-space witness와 세 반증이 차별점 (P026, P051, P076) | 외부 영어 역검색 요청은 proxy 403으로 결과 미접근; 최신 선행 배제 불가. |
| neuro_importance | 4 | 지역 평균의 정서 대비 충분성을 직접 검정함 (P026, P051, P076) | 독립 A/신경 대비가 실제 검출 가능해야 과학적 중요성이 실현됨. |
| ai_necessity | 2 | 선형 집계와 ridge가 충분한 첫 실험이므로 대형 AI 필수성 낮음 (P026, P051, P076) | 강한 작은 모형이 충분하면 foundation model 필요성 점수를 추가로 낮춰야 함. |
| data_feasibility | 3 | dense 피질·반복·A가 필요하나 정적 자료로도 가능 (P026, P051, P076) | 다섯 자료 보유는 확인되었으나 로컬 버전·스키마·반복·주석은 미검증. |
| rigor | 4 | 동일 관측의 정확한 평균/영공간 분해로 혼동을 줄임 (P026, P051, P076) | 제안한 통제는 아직 실행하지 않았고 표본수에 따른 검정력은 미확인. |
| falsifiability | 5 | 일반 상쇄·atlas 특이성·A 선택성의 반증이 구별됨 (P026, P051, P076) | 동등성 문턱과 신뢰도는 실자료의 개발 표본에서 결과 확인 전 고정해야 함. |
| interpretability | 4 | 관측 표현의 충분성으로 제한해 해석이 명확함 (P026, P051, P076) | 관찰 예측 결과는 인간 뇌 인과나 고유 정보량을 확정하지 못함. |
| generalization | 4 | 새 자극·반복·atlas로 일반화 구조가 구체적임 (P026, P051, P076) | 실제 독립 자극/참가자/세션 수와 사전학습 중복이 미확인. |
| technical_feasibility | 4 | checkpoint 없이 선형 대조부터 가능하나 자료 경로 미확인 (P026, P051, P076) | checkpoint load·GPU/시간·정확한 입력 지원은 아직 실행 검증하지 않음. |
| exploration_value | 4 | 병목 단계의 정보 손실을 직접 witness로 바꿈 (P026, P051, P076) | 새 연결의 유용성은 대조 모형이 관측 후 구별되는지에 달림. |

**여덟 질문**

1. 관련 방법 선행이 존재하고 최초 여부는 미확정이다. 영어 역검색은 시도했으나 proxy 403으로 실패했고 기존 canonical 근접 문헌만 대조했다.
2. CortexMAE 입력 계열과 병목 분석이 동일 입력의 비교 설계를 돕는다.
3. atlas 평균이 신호잡음만 개선하는 중립적 축약이라는 가정. 일반 평균화와 특정 atlas 경계의 효과를 나눈다.
4. dense 신호의 분산 공간 패턴을 조합할 수 있다.
5. 평균에서 상쇄되는 재현 공간 대비는 측정 가능한 후보다.
6. Round2의 병목 감사에 역문제의 관측 영공간에서 구별되는 해를 찾는 witness 구조를 새로 수입한다(UC04-01).
7. 정적 beta 자료도 공간 병목 검정에는 활용할 수 있다.
8. H1은 반복 신뢰도가 충분한 r_k를 더해도 A 접근성 개선의 CI가 동등성 범위 안이면 반박한다. H2는 실제/random atlas 효과 차이가 동등하면 반박한다. random parcel에서도 H1이 유지되는 것은 H1의 반증이 아니다. 비정서 대비도 동일하면 정서 선택성만 반박한다. rank 일치를 정보량 일치라고 부르지 않는다.

근거: P026, P051, P060, P081, P076. 모델 구현 지원은 기존 확인 범위이며 새 가중치 실행 없음.

## 수정 C04-04 — 개인별 정서 관련 tuning은 공통정보의 가역 좌표 차이로 충분한가?

연결축: AS05, AS15, AS28, AS33. 역할: 과학RQ후보. 최상위 추천: False — C12-05의 공유/개인성 상위 RQ에 좌표군 대조 하위 실험으로 통합 권고.

**research_question:** 공유 latent의 개인별 가역 관측 map을 허용해도, 새 자극·새 세션의 A 관련 neural tuning 예측에 추가 개인 성분이 필요한가?

**neural_target:** 개인별 피질 패턴 중 공유 예측을 뺀 잔차의 독립 반복 신뢰도와 자극 외부 A 관련성

**model_application:** 같은 q차원 공통 latent z에 개인 intercept/gain, 직교 회전, 조건수 제한 invertible affine map을 순차 적용한 모델과 z+개인 성분 모델을 비교한다. 가역군 비교는 같은 q차원 분석공간에서 정의하고 voxel로의 공통/개인 관측 head는 별도 명시한다. TRIBE 평균 피질 출력은 공통 특징 후보이며 새로운 개인 head가 제공된다고 가정하지 않는다.

**scientific_question:** 개인 적응의 이득이 같은 정보의 관측 좌표 보정인지, 지정한 공통표현과 좌표군에 없는 추가 재현 예측인지 판별한다.

**assumption_challenge:** 공유공간 밖의 반복 성분은 모두 새로운 개인 계산이라는 가정과 반대로 모두 잡음이라는 가정을 동시에 제한한다.

**main_hypothesis:** 허용한 invertible coordinate group과 동일 학습량/유효 rank를 가진 common+private 모델이 A 관련 neural slope를 새 자극·세션에서 추가 예측한다.

**alternative:** 공통 z+개인 affine map이 충분하거나, 효과가 안정된 nuisance·스케일·감각 tuning 또는 shared capacity 부족으로 설명된다.

**measurable_contrast:** 정렬 regularization×평균화 유무를 교차하고 같은 adaptation 표본수에서 common+개인 map 대 common+private를 비교한다. 주 결과는 고정 집계 A에 대한 개인별 neural contrast/slope의 외부 세션 예측손실이며 개인 A 상태로 해석하지 않는다. coordinate-only 합성자료 y_s=B_s z와 별도 private 신호 주입자료에서 분석의 거짓 private 판정/검출력을 먼저 평가한다. 전체 함수족에 대한 가역 등가가 아닌 명시된 gain/rotation/affine 군의 충분성만 시험한다.

**falsification:** common+개인 map이 private 모델과 사전 동등성 범위 안이면 해당 좌표군 밖 개인 추가성분 필요성은 반박된다. 추가 성분이 새 자극/세션에서 전이하지 않으면 재현 가설이 약화된다. affine 실패는 임의 비선형 가역 좌표군 실패나 새로운 개인 뇌 계산을 증명하지 않는다.

**what_is_new:** 개인화 성능에서 관측 좌표군의 충분성 검정으로 주질문을 바꿨다. C12-05의 신뢰도 모듈과 통합 가능하지만 본 후보의 고유 하위 조작은 gain/rotation/affine 군 대 추가 성분이다.

**novelty_risk:** 개인화/공유 반응모형 선행과 가깝고 C12-05와 상위 RQ 중복이다. 좌표군의 범위를 명시한 경쟁 비교가 없으면 별도 RQ로 세지 않는다.

**기준과 실행 조건:** 공유 ridge; 공유+개인 intercept/scale; 공유+개인 residual ridge; 해부·motion·site 공변량 모형; subject-label permutation과 신뢰도 일치 대조; 공통 latent+개인 orthogonal map; 공통 latent+조건수 제한 invertible affine map; common+private와 common-only 확장의 파라미터/rank 대조; coordinate-only/known-private synthetic recovery / 동일 개인의 독립 세션/반복; 공통 자극 및 참가자 연결 정보; 개인 정서 주석의 존재 여부: 없으면 개인 상태 해석 금지; 정렬 매핑의 training-only 구현; 새 개인 adaptation에 사용할 학습량 고정

**영어 역검색:** shared neural representation individual affine observation mapping emotion tuning alignment

실제 요청 결과: proxy tunnel 403; 검색 결과 미접근. canonical 근접 선행 대조만 유효.

**평가(자동 합산 없음)**

| 항목 | 점수 | 근거 | 불확실성 |
|---|---:|---|---|
| novelty | 3 | 개인화 및 C12-05와 중복하나 좌표군 대조로 특화됨 (P027, P052, P096) | 외부 영어 역검색 요청은 proxy 403으로 결과 미접근; 최신 선행 배제 불가. |
| neuro_importance | 4 | 개인 적응의 이득이 관측 혼합인지 추가 성분인지 가름 (P027, P052, P096) | 독립 A/신경 대비가 실제 검출 가능해야 과학적 중요성이 실현됨. |
| ai_necessity | 2 | 선형/affine 모형만으로 첫 검정 가능함 (P027, P052, P096) | 강한 작은 모형이 충분하면 foundation model 필요성 점수를 추가로 낮춰야 함. |
| data_feasibility | 2 | 개인 내 반복·새 세션·공통 자극이 모두 필요함 (P027, P052, P096) | 다섯 자료 보유는 확인되었으나 로컬 버전·스키마·반복·주석은 미검증. |
| rigor | 4 | 정렬/평균 분리와 known-coordinate 음성대조를 포함함 (P027, P052, P096) | 제안한 통제는 아직 실행하지 않았고 표본수에 따른 검정력은 미확인. |
| falsifiability | 4 | 공통+map 동등성과 private 전이 실패를 구별함 (P027, P052, P096) | 동등성 문턱과 신뢰도는 실자료의 개발 표본에서 결과 확인 전 고정해야 함. |
| interpretability | 3 | 허용 가역군 밖의 비선형 설명은 계속 남음 (P027, P052, P096) | 관찰 예측 결과는 인간 뇌 인과나 고유 정보량을 확정하지 못함. |
| generalization | 4 | 새 자극·세션·개인별 adaptation 예산을 분리함 (P027, P052, P096) | 실제 독립 자극/참가자/세션 수와 사전학습 중복이 미확인. |
| technical_feasibility | 3 | 작은 관측 map 비교는 가능하나 공유 latent 설계 검증 필요 (P027, P052, P096) | checkpoint load·GPU/시간·정확한 입력 지원은 아직 실행 검증하지 않음. |
| exploration_value | 4 | 개인 신경 tuning의 해석 범위를 새롭게 제한함 (P027, P052, P096) | 새 연결의 유용성은 대조 모형이 관측 후 구별되는지에 달림. |

**여덟 질문**

1. 관련 방법 선행이 존재하고 최초 여부는 미확정이다. 영어 역검색은 시도했으나 proxy 403으로 실패했고 기존 canonical 근접 문헌만 대조했다.
2. 평균 자극 예측과 개인 잔차 모델을 분리하고 정렬 강도를 통제할 수 있다.
3. 공유공간 밖의 반복 성분은 모두 새로운 개인 계산이라는 가정과 반대로 모두 잡음이라는 가정을 동시에 제한한다.
4. 집단에 공통된 자극–신경 변환을 안정적으로 포착할 수 있다.
5. 개인 내 반복되는 신경 tuning은 평균 모형이 놓칠 수 있다.
6. 표현 비교의 변환 불변성과 비식별성에 학습 알고리즘 비교의 관측 동치 통제 구조를 수입해 허용 좌표군 안의 설명을 먼저 소거한다(UC04-02).
7. 반복 측정 자료를 집단 평균 대신 개인 신경 대비의 안정성 검정에 사용한다.
8. common+개인 map이 private 모델과 사전 동등성 범위 안이면 해당 좌표군 밖 개인 추가성분 필요성은 반박된다. 추가 성분이 새 자극/세션에서 전이하지 않으면 재현 가설이 약화된다. affine 실패는 임의 비선형 가역 좌표군 실패나 새로운 개인 뇌 계산을 증명하지 않는다.

근거: P027, P052, P053, P060, P086, P051, P055, P096. 모델 구현 지원은 기존 확인 범위이며 새 가중치 실행 없음.

## 수정 C04-05 — 관측격자를 넘어 필요한 이력 함수는 비선형 관측인가 선택적 상태 전이인가?

연결축: AS09, AS14, AS23, AS32. 역할: 과학RQ후보. 최상위 추천: True — 공간 평균 후보와 다른 시간 계산 가설이며 관측격자·일반 용량을 구별하는 명시적 경쟁을 제공. 연속 자료와 신규 구현 검증을 조건으로 추천.

**research_question:** 입력·출력 비선형성과 시간 예산을 통제할 때, 고정 상태 전이에 입력 gate를 더하는 것으로 충분한가 아니면 입력 의존 전이가 A 관련 신경 대비의 외부 예측에 추가로 필요한가?

**neural_target:** 연속 BOLD의 보류 미래 블록 또는 시점별 A 관련 대비; 충분한 시간 주석이 없으면 일반 시간 예측만 가능

**model_application:** 신규 소규모 상태모델 3개를 공통 nonlinear input/output map으로 구현한다: F0 고정 A 전이, F1 고정 A+입력 의존 injection gate, F2 입력 의존 A(x) 전이. nonlinear AR 및 정적 gate를 추가한다. Brain-Mamba 공식 코드가 미확보이므로 이 구현을 그 모델 재현 또는 pretrained 활용이라 부르지 않는다.

**scientific_question:** 신경 관측의 이력 의존 예측에 필요한 함수 복잡도가 단순 입력/출력 비선형성인지 상태 유지의 입력 의존성인지 제한한다.

**assumption_challenge:** selective SSM 우월성은 곧 뇌의 선택 gate라는 가정을 시험하고, model-step을 신경 시간상수로 읽지 않는다.

**main_hypothesis:** 실시간 이력·대역폭·상태차원·목표·readout을 맞춰도 F2의 독립 A contrast 예측이 F0/F1/nonlinear AR보다 개선되며 관측격자 변경에 견고하다.

**alternative:** 추가 이득은 일반 nonlinear capacity·최적화·입력 gating·HRF/보간·같은 창 안의 내용량으로 설명된다.

**measurable_contrast:** native/사전 정한 재표본 격자×F0/F1/F2를 비교하되 같은 초 단위 과거, anti-alias 처리, nonlinear input/output와 train-only normalization을 사용한다. 독립 A의 측정 시간단위로 집계한 neural contrast 손실과 전체 Y 손실을 분리한다. 동일 용량/수렴 곡선, gate 정적화/교환, 동일 내용 순서 대조를 함께 평가한다. multivariate surrogate는 채널마다 같은 주파수 위상을 더해 cross-spectrum를 보존하는 구성부터 사용하며 고차 의존성은 보존하지 않는다고 명시한다.

**falsification:** F1 또는 nonlinear AR이 F2와 효과 동등하면 선택 전이의 추가 필요성을 반박한다. 격자/미래차단 후 효과가 소실되면 관측 처리 설명을 강화한다. gate test-time 교환에만 취약하면 OOD 가능성이 남으므로 해당 제어로 재학습한 결과와 함께 판단한다. 어떤 결과도 생물학적 gate를 확정하지 않는다.

**what_is_new:** 고정 대 선택 SSM의 이분법을 입력/관측 비선형, injection gate, 전이 gate의 위치별 함수족 경쟁으로 바꿨다. 상태 계산과 일반 용량을 구별할 수 있는 수준까지만 주장을 유지한다.

**novelty_risk:** 일반 temporal benchmark로 환원될 수 있다. 관측격자에 견고한 독립 A 관련 대비가 없으면 정서 연구 후보에서 내린다.

**기준과 실행 조건:** native-TR AR/FIR ridge; 동일 상태차원 fixed SSM; 같은 문맥 길이 temporal convolution; 자기상관/스펙트럼 보존 surrogate; 과거 사건 bag와 순서 보존 표현; F0 고정 전이+공통 nonlinear input/output; F1 고정 전이+입력 injection gate; nonlinear AR; 재학습한 static gate 대 test-time gate exchange; multivariate cross-spectrum 보존 surrogate / 연속 BOLD와 정확한 TR/시간원점; 이벤트·정서 주석의 측정 시간 해상도; 보간의 과거 전용 구현; 모형 코드 독립 재구현 검증; 상태차원·학습량·문맥 실시간 길이 통제

**영어 역검색:** selective state space fMRI emotion nonlinear capacity hemodynamic sampling controls

실제 요청 결과: proxy tunnel 403; 검색 결과 미접근. canonical 근접 선행 대조만 유효.

**평가(자동 합산 없음)**

| 항목 | 점수 | 근거 | 불확실성 |
|---|---:|---|---|
| novelty | 3 | SSM 비교 선행은 있으나 비선형 위치×격자 대비가 구체적임 (P026, P028, P096) | 외부 영어 역검색 요청은 proxy 403으로 결과 미접근; 최신 선행 배제 불가. |
| neuro_importance | 4 | 이력 의존 관측에 필요한 함수족을 좁힘 (P026, P028, P096) | 독립 A/신경 대비가 실제 검출 가능해야 과학적 중요성이 실현됨. |
| ai_necessity | 3 | 함수족 구현이 필요하지만 대형 pretrained SSM은 불필요함 (P026, P028, P096) | 강한 작은 모형이 충분하면 foundation model 필요성 점수를 추가로 낮춰야 함. |
| data_feasibility | 2 | 연속 BOLD와 A 시간단위/지연 정보가 필수이며 미확인 (P026, P028, P096) | 다섯 자료 보유는 확인되었으나 로컬 버전·스키마·반복·주석은 미검증. |
| rigor | 4 | input/transition gate 및 관측필터를 분리함 (P026, P028, P096) | 제안한 통제는 아직 실행하지 않았고 표본수에 따른 검정력은 미확인. |
| falsifiability | 4 | F1/AR 충분성과 F2 이득의 구별이 명료함 (P026, P028, P096) | 동등성 문턱과 신뢰도는 실자료의 개발 표본에서 결과 확인 전 고정해야 함. |
| interpretability | 3 | predictive family 차이를 생물학적 gate로 읽을 수 없음 (P026, P028, P096) | 관찰 예측 결과는 인간 뇌 인과나 고유 정보량을 확정하지 못함. |
| generalization | 4 | 격자·새 자극·순서 대조의 일반화가 명시됨 (P026, P028, P096) | 실제 독립 자극/참가자/세션 수와 사전학습 중복이 미확인. |
| technical_feasibility | 2 | 공식 Brain-Mamba 미확보로 신규 구현·검증 필요 (P026, P028, P096) | checkpoint load·GPU/시간·정확한 입력 지원은 아직 실행 검증하지 않음. |
| exploration_value | 4 | 선택성이라는 이름에 숨은 일반 용량 효과를 드러냄 (P026, P028, P096) | 새 연결의 유용성은 대조 모형이 관측 후 구별되는지에 달림. |

**여덟 질문**

1. 관련 방법 선행이 존재하고 최초 여부는 미확정이다. 영어 역검색은 시도했으나 proxy 403으로 실패했고 기존 canonical 근접 문헌만 대조했다.
2. 선택적 SSM과 공개 fMRI 전처리 코드로 두 요인을 명시적으로 분리할 수 있다.
3. selective SSM 우월성은 곧 뇌의 선택 gate라는 가정을 시험하고, model-step을 신경 시간상수로 읽지 않는다.
4. 입력에 따라 선택적으로 유지되는 예측 상태를 표현할 수 있다.
5. 단일 고정시간상수로 설명되지 않는 신경 이력 의존성은 아직 E3 후보다.
6. Round2 관측척도 검정에 알고리즘 비교의 계산 경로 분리 원리를 수입한다. 비선형성의 위치를 입력/관측과 상태 전이로 나누어 observationally distinguishable function families를 비교한다(UC04-03).
7. 연속 원자료가 있는 보유 자료를 시간격자 민감도 시험에 재사용한다. beta-map 시행순서를 연속신호로 바꾸지 않는다.
8. F1 또는 nonlinear AR이 F2와 효과 동등하면 선택 전이의 추가 필요성을 반박한다. 격자/미래차단 후 효과가 소실되면 관측 처리 설명을 강화한다. gate test-time 교환에만 취약하면 OOD 가능성이 남으므로 해당 제어로 재학습한 결과와 함께 판단한다. 어떤 결과도 생물학적 gate를 확정하지 않는다.

근거: P026, P028, P034, P056, P085, P086, P090, P096. 모델 구현 지원은 기존 확인 범위이며 새 가중치 실행 없음.

## 한계

- 원 후보 5개 및 Agent03/11의 실제 비판 10건에 응답했다. 비판을 대신 만들어 쓰지 않았다.
- 새 연결 3개는 기존 문헌의 계산 구조를 사용한 E3 제안이며 신규 신경 발견이 아니다. P096 등 코드 확인 자료를 원문 정리 검증으로 승격하지 않았다.
- 영어 8–15단어 역검색을 후보별 실제 HTTP 요청으로 시도했으나 5건 모두 proxy tunnel 403으로 실패했다. 차단을 우회하지 않았고 외부 검색 성공 또는 세계 최초를 주장하지 않는다.
- 스키마·경로·A/반복·checkpoint·계산비용 미확인은 분석 착수 조건이다. 문헌/토론 진행을 차단하지 않았으며 이 결과는 실행 계획이다.
- C04-01은 C03-01과, C04-04는 C12-05와 상위 RQ 통합을 권고한다. 별도 모델명으로 RQ 수를 늘리지 않는다.
- 평가 점수는 잠정 설계 판단이며 자동 가중합을 계산하지 않았다. 최상위 자기 후보는 C04-03/C04-05 두 개만 추천한다.
- C04-03의 AI 필요성 2점과 C04-05의 데이터/기술 실현성 2점을 보존했다. 높은 과학적 관심이 기술적 준비를 의미하지 않는다.
- 공유 문서·Git·타 Agent 파일은 수정하지 않고 자기 round04 JSON/MD만 작성했다.
