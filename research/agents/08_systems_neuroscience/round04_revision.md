# Agent08 Round4 — 비판 응답과 후보 재구성

두 비판자 10개 리뷰를 실제 대조했다. 과학 후보 3개 중 C08-01은 C03-03과 병합하며, C08-03·05는 방법후보로 분리한다. 자기 최상위 추천은 병합 C08-01과 C08-04다. 실증 분석은 수행하지 않았다.

## C08-01 — 고정 ROI 분할에서 정서 대비의 비가산 판독이 필요한가

**판정:** 과학RQ후보 / 수정·상위 RQ 병합
**응답한 실제 비판:** R3-03-C08-01, R3-07-C08-01

**수용한 수정:**

- C03-03과 동일한 상위 RQ에 병합하고 두 assay를 별도 추정량으로 남긴다.
- P005/P009를 직접 근접 신경 선행으로 추가한다.
- 주장을 고정 ROI 분할하 비가산 판독의 추가위험 감소로 제한하고 시너지·통신·인과 용어를 제거한다.
- block 내부 좌표변환 안정성, 비선형 공통입력 null, 전체 분포/선별분포 estimand를 분리한다.

**남긴 이견:**

- R3-07의 소수의견을 수용한다: 비가산 판독의 필요성 자체는 신경표상의 관측 제약으로 가치가 있어 무조건 방법후보로 내리지 않는다.
- 두 assay의 일치를 생물학적 통신의 충분조건으로 보지는 않는다.

**수정 질문:** 사전고정 ROI 분할에서 독립 정서 주석의 판독위험은 강한 비선형 가산함수로 충분한가, 비가산 readout이 추가 위험을 줄이는가?

**모델 적용:** ROI 내부 nonlinear additive spline/동일용량 head와 비가산 head를 같은 fold에서 비교한다. C03-03의 자연 후보 판별 assay와 direct A readout을 병합 RQ 안에서 따로 평가한다.

**과학 질문:** 정보가 ROI별로 분산된 것과 그 정보를 읽는 데 비가산 함수가 필요한 것을 구분한다.

**가정 도전:** 비가산 판독의 이득을 정보이론적 시너지 또는 뇌 영역 간 통신으로 해석하는 가정을 제한한다.

**주가설:** 내용 공통지지·ROI 신뢰도·유효용량을 맞춘 상태에서 고정 ROI 분할의 비가산 head가 독립 주석 위험을 줄인다.
**경쟁 설명:** 비선형 공통자극·관측잡음 상관·정규화 차이 또는 ROI 좌표 선택이 이득을 만든다.

**측정 대비:** 전체 사전지정 자극분포에서 ΔR=R(additive)−R(nonadditive)를 주추정량으로 보고한다. 모형 불일치로 선별한 자극집합의 ΔR은 다른 조건부 estimand로 분리한다. 후보 판별 log score는 별도 assay이며 두 점수를 합하지 않는다.

**반증:** 강한 가산계가 사전 동등성 범위에서 충분하면 지정 ROI·표적·함수계열에서 비가산 판독 필요성이 작다. 통신 없는 공통입력 모의계에서도 같은 이득이 나면 통신 해석은 기각하되 실제 자료의 비가산 판독 관찰은 남는다.

**Baseline:** nonlinear additive spline; 강한 stimulus-only 모형; 비선형 공통입력·상호작용 생성계의 양성/음성 회복; ROI 내부 가역 좌표변환과 블록 간 혼합의 분리; 같은 객체/다른 A 및 같은 A/다른 객체 자연 후보

**계수:** C03-03과 하나의 상위 RQ로 병합; C08-01을 추가 독립 RQ로 중복 계수하지 않음
**최상위 추천:** True — C03-03과 병합한 상위 RQ로만 추천; 저비용 직접 assay로 가산 충분성을 검정한다.

**영어 역검색:** `distributed emotion brain representations additive nonlinear readout region interactions confounds`. 공식 Crossref API 응답: 프록시 403; 결과 미확보.

| 평가 | 점수 | 근거 |
|---|---:|---|
| novelty | 3 | 분산 코드 선행과 C03-03에 가깝지만 가산의 필요성을 명시적으로 제한한다. |
| neuro_importance | 4 | 분산 신경정보에 필요한 판독 함수의 범위를 규정한다. |
| ai_necessity | 2 | 작은 spline/bilinear baseline으로 일차 질문을 시험할 수 있다. |
| data_feasibility | 3 | Horikawa 시행자료가 후보이나 ROI·내용 공통지지·반복 스키마는 미확인이다. |
| rigor | 4 | 내용 그룹·신뢰도·블록변환·공통입력 null을 함께 비교한다. |
| falsifiability | 4 | 동등성 검정과 known-truth null에서 가산 필요성을 반박할 수 있다. |
| interpretability | 4 | 통신 대신 ROI 분할하 predictive risk로 해석을 제한한다. |
| generalization | 3 | 새 내용·참가자 전이는 가능하나 공통지지가 실행조건이다. |
| technical_feasibility | 4 | checkpoint 없이 작은 head로 구현할 수 있다. |
| exploration_value | 4 | 두 assay 불일치가 표상 또는 측정 편향을 드러낼 수 있다. |

모든 평가는 스키마·실증·신규성 미확인에 따른 잠정치다. 상세 8질문·데이터 조건·출처·역검색 URL은 JSON에 보존했다.

## C08-02 — HRF 가정하 정서 문맥 대비의 피질 분포와 시간모형의 식별 경계

**판정:** 과학RQ후보 / 수정·좁힌 과학RQ 유지
**응답한 실제 비판:** R3-03-C08-02, R3-07-C08-02

**수용한 수정:**

- 정서 입력 이력 범위를 문맥 길이와 독립적으로 고정한다.
- HRF×neural-history 회복 및 합성커널 동일 쌍을 음성대조로 추가한다.
- 독립 HRF 정보가 없으면 생리적 시간상수 대신 지정 HRF family하 문맥 예측 대비라고 명명한다.
- gradient 부호·근접 고유값의 부분공간 불확실성 및 공간 게이트를 적용한다.

**남긴 이견:**

- 문맥 이득의 피질 분포는 HRF 완전식별 없이도 관측량으로 보고할 수 있다는 소수의견을 유지한다.
- 유연한 HRF에서 효과가 사라진 사실 하나로 신경 통합의 부재를 주장하지 않는다.

**수정 질문:** 지정 HRF family와 정서 입력이력을 고정했을 때 자극 문맥 길이에 따른 정서 주석 추가예측 대비는 독립 cortical gradient와 어떻게 관계하는가?

**모델 적용:** 동일 현재 자극·과거 문맥 길이 L을 갖는 M_X(L)와 M_X(L)+A_fixed를 비교한다. 일차 A_fixed는 자극시점 현재 주석 A_t이며 모든 모형에서 같은 HRF family로 관측화한다. 고정 길이 H의 과거 A는 독립 이차 분석이며 L과 함께 늘리지 않는다.

**과학 질문:** 정서 주석과 연관된 문맥 예측정보의 공간분포 및 HRF·neural-history 분해의 식별 한계를 구분한다.

**가정 도전:** BOLD 합성커널의 예측우위가 HRF와 신경필터 각각의 고유 시간상수를 정한다는 가정을 반박한다.

**주가설:** Δ_A(L)=R[M_X(L)]−R[M_X(L)+A_fixed]의 L에 따른 변화는 독립 gradient 위치와 관계하며 지정한 관측모형과 회복 가능한 범위에서 재현된다. 방향은 개발자료 선택 대신 사전 양측 검정으로 고정한다.
**경쟁 설명:** 동일 합성커널의 다른 HRF/신경필터 분해, 자극 저주파·주석 의미 공유·지역 SNR이 관측 대비를 설명한다.

**측정 대비:** 주추정량은 Δ_A(long)−Δ_A(short)와 고정 gradient의 관계이며 Δ_A의 감소도 긴 문맥 X가 A와 공유한 정보를 설명한 결과로 보고한다. 전체 예측 이득과 A의 조건부 이득을 분리하며 순수정서라 명명하지 않는다.

**반증:** 독립 HRF 제약과 회복 simulation에서 식별력을 확보한 영역에서만 추가 문맥 필요성의 동등성을 평가한다. 동일 BOLD를 내는 convolution 동치쌍을 구별했다면 파이프라인을 기각한다. 유연한 HRF에서 효과 소실만으로 신경 통합 부재를 주장하지 않는다.

**Baseline:** 짧은 신경필터+넓은 HRF와 긴 필터+좁은 HRF의 동일 합성커널 쌍; neural history 유무×지역 HRF 차이 유무 2×2 회복; 현재입력 일치·과거 이력 상이한 held-out 대비; native TR의 FIR/과거전용 문맥 모형; gradient 부호 고정·근접 고유값 부분공간 민감도

**계수:** 신경 시간상수 식별 주장은 보류. 좁힌 관측적 문맥 대비 질문만 과학 후보로 유지한다.
**최상위 추천:** False — 방법후보 또는 식별 전제가 강한 관측 질문이므로 자기 최상위 2개에는 넣지 않는다.

**영어 역검색:** `emotion cortical gradient temporal context hemodynamic convolution neural filter identifiability`. 공식 Crossref API 응답: 프록시 403; 결과 미확보.

| 평가 | 점수 | 근거 |
|---|---:|---|
| novelty | 3 | 시간통합 선행과 가깝고 새 부분은 주석이력 고정 문맥 대비다. |
| neuro_importance | 4 | 생리 시간해석의 식별 경계를 제약하는 의미가 크다. |
| ai_necessity | 2 | 문맥 ridge와 FIR로 상당 부분 검증 가능하다. |
| data_feasibility | 2 | 독립 HRF 정보와 연속 주석·신호가 미확인이다. |
| rigor | 4 | 동일 합성커널과 2×2 회복으로 반증 규칙 자체를 검증한다. |
| falsifiability | 3 | 관측 대비는 반증 가능하나 생리 필터 분해는 여전히 조건부다. |
| interpretability | 3 | estimand는 명확하지만 HRF와 neural-history 동치가 남는다. |
| generalization | 3 | held-out 영화가 가능하나 충분한 길이/내용 변이 필요하다. |
| technical_feasibility | 3 | 작은 시계열 모형은 가능하나 회복·gradient 불확실성 계산이 필요하다. |
| exploration_value | 4 | 효과의 부재와 비식별을 구분하는 새로운 측정설계로 이어질 수 있다. |

모든 평가는 스키마·실증·신규성 미확인에 따른 잠정치다. 상세 8질문·데이터 조건·출처·역검색 URL은 JSON에 보존했다.

## C08-03 — AS18 공통 방법 게이트: 공간 null의 국소 오류와 신호 복원

**판정:** 방법후보 / 방법후보 유지
**응답한 실제 비판:** R3-03-C08-03, R3-07-C08-03

**수용한 수정:**

- 독립 과학RQ 수에서 제외하고 AS18 공통 방법 게이트로 고정한다.
- 독립 반복 차이/훈련 잔차에서 null 모수를 적합한다.
- 효과없음·고정위치·gradient 신호 주입의 지역별 오류율·검정력·복원을 함께 평가한다.
- variogram만으로 공동분포 적합성을 선언하지 않는다.

**남긴 이견:**

- R3-03 보류와 R3-07 유지는 실제로 방법 산출물 유지·독립 과학 계수 제외라는 같은 범위에서 조정 가능하다.
- 방법 게이트의 실용적 우선순위는 낮추지 않되 생물학적 발견 점수와 섞지 않는다.

**수정 질문:** 독립 자료에서 추정한 공간 잡음모형은 정서관련 지도 분석의 국소 오류율과 알려진 주입신호의 복원력을 함께 보장하는가?

**모델 적용:** 독립 반복 차이/훈련 잔차로 nuisance를 적합한 뒤 효과없음·고정위치·gradient 신호를 주입하여 encoding부터 지도검정까지 재실행한다.

**과학 질문:** 현재 산출물은 공간 주장을 허용할 측정 조건 검증이며 독립적인 생물학 질문은 아니다.

**가정 도전:** spatial null 한 종류의 통과 또는 variogram 적합이 모든 위치의 타당성을 보장한다는 가정이다.

**주가설:** 독립 nuisance 추정과 지역별 calibration은 사전 허용범위의 오류율을 유지하면서 알려진 위치와 gradient 효과를 복원한다.
**경쟁 설명:** null이 진짜 신호를 흡수하거나 공동분포·관측설계를 잘못 재현하여 과보정 또는 거짓 양성을 만든다.

**측정 대비:** 국소 제1종 오류, 효과크기 편향, 위치별 power와 신호 복원율을 함께 보고한다. 실제 정서 지도 효과는 이 방법게이트 통과 후 다른 과학 후보에서 평가한다.

**반증:** 명목 오류율을 넘거나 양성 주입신호를 복원하지 못하면 해당 null 설정을 수정한다. null 적합 실패는 신경조직의 양성 증거가 아니며 보정 후 음성도 검정력 없이 해석하지 않는다.

**Baseline:** 효과 없는 nuisance-only 자료; 위치를 아는 양성 주입신호; gradient 양성 주입신호; 같은 관측기하·다른 공간위치의 모의쌍; 지역 covariance·분포·국소 오류율 진단

**계수:** 독립 과학RQ 수에서 제외
**최상위 추천:** False — 방법후보 또는 식별 전제가 강한 관측 질문이므로 자기 최상위 2개에는 넣지 않는다.

**영어 역검색:** `emotion brain maps spatial nonstationarity null models signal injection calibration`. 공식 Crossref API 응답: 프록시 403; 결과 미확보.

| 평가 | 점수 | 근거 |
|---|---:|---|
| novelty | 2 | 공간 null calibration은 P063/P064의 기존 문제다. |
| neuro_importance | 3 | 잘못된 지도 해석을 차단하지만 단독 신경 발견은 아니다. |
| ai_necessity | 1 | 고전 surrogate와 시뮬레이션이 핵심이며 최신 AI가 필수 아니다. |
| data_feasibility | 3 | 반복 잡음·surface 정보가 있으면 가능하나 보유본 스키마 미확인이다. |
| rigor | 5 | 음성/양성 주입과 독립 nuisance 추정으로 오류·power를 함께 본다. |
| falsifiability | 5 | 국소 오류와 복원 실패가 명확한 설정 폐기 기준이다. |
| interpretability | 4 | 공통 방법 게이트로 지위를 제한해 해석 과장을 줄인다. |
| generalization | 4 | 여러 정서 지도 후보에 재사용 가능한 calibration이다. |
| technical_feasibility | 4 | 공개 공간 도구가 있으나 현재 설치·실행은 미확인이다. |
| exploration_value | 3 | 독립 발견보다 전체 연구의 신뢰성을 높인다. |

모든 평가는 스키마·실증·신규성 미확인에 따른 잠정치다. 상세 8질문·데이터 조건·출처·역검색 URL은 JSON에 보존했다.

## C08-04 — 정서 예측에 필요한 평균·분산·상관·시간전이의 최소 관측모형

**판정:** 과학RQ후보 / 수정·과학RQ 유지
**응답한 실제 비판:** R3-03-C08-04, R3-07-C08-04

**수용한 수정:**

- 공분산 이득을 대각 분산과 비대각 상관구조로 분리한다.
- 고정상관+가변분산, 동일 emissions의 iid mixture, 연속 volatility/covariance null을 추가한다.
- 온라인 예측은 t까지 filtering만 사용하고 smoothing은 별도 오프라인 동행 분석으로 제한한다.
- 상태수·regularization을 내부 BOLD fold에서 고정하고 test 정서 주석은 선택에 쓰지 않는다.

**남긴 이견:**

- 이산 상태가 실제 존재하지 않아도 상태추상화는 가능하다는 소수의견을 인정한다.
- 이산 HMM 우위가 생물학적 상태의 고유성 또는 실제 영역 간 통신을 증명한다는 주장에는 동의하지 않는다.

**수정 질문:** 자극조건부 잔차에서 독립 정서 주석 예측을 개선하는 것은 평균 변화, 대각 분산, 비대각 상관 또는 시간적 전이 중 무엇인가?

**모델 적용:** 잔차화는 cross-fit한다. 동일 평균구조에서 stationary covariance→가변 diagonal→고정상관+가변분산→full covariance를 비교하고, 각 공간모형에 iid mixture·연속 volatility/covariance·이산 HMM 전이를 대조한다. 상태수·regularization은 내부 BOLD validation에 고정한다.

**과학 질문:** 동적 network-state라는 단일 해석을 평균/분산/상관의 공간적 관측구조와 이산/연속 시간구조의 최소 필요성으로 분해한다.

**가정 도전:** covariance HMM의 성공이 영역 간 결합 변화 및 실재하는 이산 신경 상태를 뜻한다는 가정이다.

**주가설:** 정서 주석 관련 예측정보의 일부는 가변 분산 및 연속 관측모형을 넘어서는 비대각 시간구조를 요구한다. 이산 상태 자체의 존재는 별도 가설로 확정하지 않는다.
**경쟁 설명:** 같은 관측분포의 비정규 mixture·연속 분산변동·공통 자극 잔여가 HMM의 이득을 설명한다.

**측정 대비:** 주석 변화의 held-out log score에서 비대각 구조 추가이득과 전이 추가이득을 별개 추정한다. BOLD 순차 log score는 보조다. 온라인 평가는 p(z_t|Y_≤t,X_≤t)의 filtered 상태만 쓰고 smoothing은 별도 오프라인 동행 결과로 명명한다.

**반증:** 고정상관+가변분산이 full covariance와 동등하면 동적 비대각 구조 필요성을 낮춘다. 동일 emissions iid mixture 또는 연속 covariance가 HMM과 동등하면 이산 전이 필요성은 반박한다. 신뢰도·검정력 미달은 판정불가이다.

**Baseline:** stationary covariance; time-varying diagonal covariance; fixed correlation+time-varying variance; 동일 emissions와 점유분포를 갖는 iid mixture; 같은 주변분포·자기상관을 맞춘 연속 volatility/covariance; 상태label 순열불변 예측 통계

**계수:** 생물학적 이산 상태의 실재 주장이 아니라 정서 예측에 필요한 최소 관측모형의 비교
**최상위 추천:** True — 평균·분산·상관·전이의 상반 설명이 명시돼 과학적 판별력이 높다.

**영어 역검색:** `emotion dynamic connectivity hidden Markov continuous volatility covariance diagonal variance`. 공식 Crossref API 응답: 프록시 403; 결과 미확보.

| 평가 | 점수 | 근거 |
|---|---:|---|
| novelty | 3 | HMM·변동성 선행은 강하지만 독립 정서 대비의 최소 관측모형을 경쟁시킨다. |
| neuro_importance | 4 | 평균·진폭·상관·전이 중 어떤 설명이 필요한지 구별한다. |
| ai_necessity | 3 | 풍부한 자극 encoder는 도움이 되지만 작은 상태모형도 필수 대조다. |
| data_feasibility | 2 | 충분한 연속 run·시간 주석·nuisance 자료가 미확인이다. |
| rigor | 4 | 비대각/대각 및 이산/연속 대조를 분리하고 test 라벨 선택을 금지한다. |
| falsifiability | 4 | 가변 분산 또는 연속 null의 동등성이 강한 상태 해석을 반박한다. |
| interpretability | 4 | 이산 실재 대신 관측예측의 필요성으로 제한한다. |
| generalization | 3 | 영화/run 전이를 요구하나 상태 추정의 자료량 제약이 크다. |
| technical_feasibility | 3 | HMM 구현은 있으나 full covariance와 연속 null의 안정 추정이 어렵다. |
| exploration_value | 4 | 상태 성공의 원인을 공간기하와 시간정보로 나누는 가치가 있다. |

모든 평가는 스키마·실증·신규성 미확인에 따른 잠정치다. 상세 8질문·데이터 조건·출처·역검색 URL은 JSON에 보존했다.

## C08-05 — 방법후보: 고정 자극 feature에서 ROI 출력계수의 graph regularization

**판정:** 방법후보 / 방법후보로 전환; 경로 기제 주장 보류
**응답한 실제 비판:** R3-03-C08-05, R3-07-C08-05

**수용한 수정:**

- graph 공동 재색인, 고정 node의 edge 변경, SSM 순서 변경을 별개 조작으로 분리한다.
- 일차 방향을 고정 자극 feature→ROI 반응 예측으로 제한하여 test brain 입력을 제거한다.
- 공동 재색인은 equivariance sanity check일 뿐 가설 검정이 아님을 명시한다.
- 원래 경로 질문을 출력계수의 관계 regularization 비교로 좁히고 SSM 경로는 이 후보에서 제외한다.

**남긴 이견:**

- R3-03은 수정 후 과학적 발전 가능성을 인정하나 R3-07은 조작 정의 전 보류했다. 정의는 아래처럼 해결하지만 현재 목표는 정규화 유용성이라 단독 과학RQ로 승격하지 않는다.
- 유효한 edge prior가 발견되어도 최적화/편향 변화와 실제 뇌 전달경로는 구별되지 않는다.

**수정 질문:** 고정 자극 feature→ROI encoding에서 node 정체성을 고정한 graph edge prior는 동등한 용량의 무관계 출력보다 정서 대비를 더 안정적으로 예측하는가?

**모델 적용:** 공통 frozen X와 ROI 출력계수 B에 loss+λ tr(Bᵀ L_G B) 형태의 관계 정규화를 비교하는 작은 원리 실험을 정의한다. 여기서 B는 ROI×feature, L_G는 train-only/외부 graph Laplacian이다. X·ROI ID를 고정하고 L_G의 edge만 바꾼다. 이는 E3 설계이며 P028 원모델을 실행했다는 뜻이 아니다.

**과학 질문:** 현재 단계는 관계 prior의 관측예측 유용성을 평가하는 방법 질문이다. 해부학적 전달경로의 필요성을 묻는 독립 신경 질문으로 세지 않는다.

**가정 도전:** graph 공동 재색인이 실제 edge 개입이며 같은 scalar 내용성능이 같은 표현을 뜻한다는 가정이다.

**주가설:** 정체성이 고정된 ROI의 특정 edge prior는 degree/거리 분포·regularization·최적화를 맞춘 null보다 독립 정서 대비 예측을 개선할 수 있다.
**경쟁 설명:** 모든 차이는 smoothing 정규화·최적화 난도 또는 학습자료의 graph 추정오차로 설명된다.

**측정 대비:** 고정 X와 동일 decoding-free encoding loss에서 edge prior별 A 관련 대비의 held-out 예측차를 평가한다. 공동 node 재색인(Y→PY,B→PB,L→PLPᵀ)은 같은 목적함수의 sanity check이며 효과 검정이 아니다. λ와 null 선정은 개발자료에 고정한다.

**반증:** 공동 재색인에서 수치오차 이상의 차이가 나면 구현을 수정한다. 실제 edge 변경이 matched null보다 나쁘거나 동등하면 해당 관계 prior의 필요성을 낮춘다. SSM 순서 효과는 이 estimand에 포함하지 않는다.

**Baseline:** graph 없는 동일 ridge; ROI 공동 재색인 equivariance sanity check; 고정 node의 degree/거리분포 보존 edge 재배선; 공통 frozen feature와 동일 regularization 예산; 훈련 graph 불확실성·seed·수렴 민감도

**계수:** 독립 과학RQ 수에서 제외; 원래 실제 뇌 경로 기제 주장은 보류
**최상위 추천:** False — 방법후보 또는 식별 전제가 강한 관측 질문이므로 자기 최상위 2개에는 넣지 않는다.

**영어 역검색:** `brain encoding emotion graph topology permutation equivariance fixed features rewiring`. 공식 Crossref API 응답: 프록시 403; 결과 미확보.

| 평가 | 점수 | 근거 |
|---|---:|---|
| novelty | 2 | graph regularization은 새 방법이라고 보기 어렵다. |
| neuro_importance | 2 | 현재는 모델 prior의 유용성이고 독립 신경기제가 아니다. |
| ai_necessity | 1 | 고정 feature의 ridge+Laplacian으로 충분하며 최신 AI가 필요 없다. |
| data_feasibility | 3 | 시행 X→Y로 가능하나 graph·주석·반복 스키마가 미확인이다. |
| rigor | 4 | joint relabeling과 actual edge 변화를 수학적으로 구분한다. |
| falsifiability | 4 | equivariance 실패와 edge prior 동등성이 명확한 부정 기준이다. |
| interpretability | 4 | 경로라는 모호한 해석을 제거하고 regularization으로 한정한다. |
| generalization | 3 | 새 자극·graph 불확실성 전이는 가능하나 생물학 일반화는 없다. |
| technical_feasibility | 4 | 작은 quadratic objective 구현으로 원리 검정이 가능하다. |
| exploration_value | 2 | 독립 발견 가치보다 후속 구조모형을 잘 정의하는 방법 가치가 크다. |

모든 평가는 스키마·실증·신규성 미확인에 따른 잠정치다. 상세 8질문·데이터 조건·출처·역검색 URL은 JSON에 보존했다.

## UC08-01 — 표현학습의 비식별성·불변성 및 시스템 식별

**원래 목표:** P053은 관측만으로 잠재 요인 분해가 유일하지 않은 문제를, P051은 표현 비교에서 허용 변환에 따라 동등성이 달라지는 문제를 다룬다. P028은 상태공간의 예측 표현을 제공한다.

**수입 구조:** 예측이 같은 두 생성설명을 먼저 명시하고 그 동치류를 깨는 독립 측정을 요구한다. 예: 같은 합성커널을 만드는 HRF/신경필터 두 분해, 같은 목적함수를 만드는 graph 공동 재색인.

**새 신경 질문:** 어떤 정서 문맥·관계 효과가 관측 동치류를 넘어 식별되며 어떤 생리적 해석은 추가 정보 없이는 불가능한가?

**Round2와 차이:** Round2는 대체모형의 성능 비교였다. 이번 연결은 정확히 같은 관측을 만드는 모의쌍/공동 재색인을 음성대조로 고정하고 원래 신경시간상수·경로 주장을 축소한다.

**판별 대조:** 동일 BOLD 합성커널 쌍을 분석이 잘못 구별하는지 검사하고, 공동 graph 재색인의 objective/예측 동일성을 검증한다. 이 대조를 통과한 뒤 실제 이력/edge 변경만 평가한다.

**실패 해석:** 동일 관측을 서로 다른 기제로 확신해 구별하면 분석/해석을 기각한다. 구별하지 못하는 것은 실패가 아니라 올바른 비식별 판정이다.

**근거:** P051, P053, P028. 원문 검증 범위는 기존 catalog 계승; 이 신경 전이와 수학적 대조 설계는 새 E3 연결이며 미실행

## UC08-02 — 정적 표현기하 비교와 확률과정의 시간전이 식별

**원래 목표:** P051은 표현간 기하 비교를, P067은 잠재 관측상태의 시간 조직을, P066은 사건분절을 다룬다.

**수입 구조:** 같은 emissions·점유분포 또는 같은 정적 공간기하를 가진 과정도 iid/연속/이산 전이가 다를 수 있다는 구조를 사용한다. 정적 분포를 고정하고 시간정보만 남는 예측을 검사한다.

**새 신경 질문:** 정서 주석 예측에 필요한 것은 비정규 공간분포의 압축인가, 비대각 시간구조 또는 전이가 제공하는 추가 정보인가?

**Round2와 차이:** Round2의 mean/covariance HMM 비교는 진폭·분포·전이를 함께 바꿨다. 새 연결은 같은 공간관측을 만드는 동등 emissions와 시간변화를 분리하고 이산 HMM 실재 주장을 검증 대상으로 낮춘다.

**판별 대조:** 공간 emissions 고정 iid mixture, 연속 covariance, 이산 HMM을 과거 filtering 기반 보류 run의 순차 점수와 독립 정서 대비로 비교한다. 공간 QC에는 같은 기하/다른 위치 신호를 넣어 통계가 무엇에 민감한지 확인한다.

**실패 해석:** 동일 정적분포로 충분하면 전이/이산 상태의 필요성을 줄인다. HMM 우위가 있어도 생물학적 실재나 인과 통신으로 승격하지 않는다.

**근거:** P051, P066, P067. 기존 공식 코드·논문 검증 범위를 계승한 E3 설계; 실제 연속·이산 모의 검정은 미실행

## 한계와 실제 완료 범위

- 실제 두 비판자 10개 review에 응답했다. 반론/소수의견과 원 후보 5개를 모두 보존했고 대상 Agent·공유 파일은 수정하지 않았다.
- Crossref 공식 API에 후보별 영어 쿼리 5개를 실제 전송했으나 모두 Tunnel connection failed: 403 Forbidden이었다. 우회하지 않았고 검색 실패를 candidate별 URL·오류와 함께 보존한다. 외부 신규성을 확인했다고 주장하지 않는다.
- 근거는 기존 canonical catalog의 논문/공식 코드 검증 범위를 계승한다. 새로운 신경 전이는 E3이며 source title만으로 결과를 보증하지 않는다.
- 과학 후보 3개 중 C08-01은 C03-03과 병합 계수한다. C08-03·05는 방법후보이며 독립 과학RQ 수에서 제외한다. C08-02의 생리 시간상수, C08-04의 생물학적 이산상태, C08-05의 실제 뇌 경로는 미해결 주장으로 남긴다.
- 데이터 5종 보유는 사용자 진술로 유지한다. 스키마 미확인은 실제 실행조건이며 이번 문헌·토론·계획 완료를 막지 않는다.
- 모델·모의회복·뇌분석은 실행하지 않았다. 기능연결·covariance·AI edge 편집은 인간 뇌 인과의 증거가 아니다.
