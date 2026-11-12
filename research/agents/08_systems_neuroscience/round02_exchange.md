# Agent08 Round2 — 네트워크·시스템신경 정보교환

작성일: 2026-11-12. 새 가설 E3. 원자료 분석·모델 실행·새 문헌 검색은 수행하지 않았다. 기존 근거의 본문/공식 코드 범위를 아래 출처표에서 구별한다.

Agent04와 Agent09의 실제 Round1 보고서를 읽어 두 원리를 수입했다. 데이터 5종의 보유는 사용자 진술로 인정하며 스키마 미확인은 분석조건이다. 자세한 기계 판독 산출물은 [round02_exchange.json](round02_exchange.json)이다.

## 실제 수입한 계산 원리

- **04_brain_foundation**: 자극조건부 대 신경조건부 예측의 분해, 관측시간격자와 잠재상태의 분리. 원래 문제: 범용 표현의 보존·소실과 조건부 예측가능성. 새 질문: 영역 결합·시간 상태·문맥 gradient의 이득이 자극 공통입력 및 HRF로 충분히 설명되는가. 근거: P027, P028, P029.
- **09_generative_ai**: 타당성 제약 아래 경쟁 가설을 구별하는 자극 선택. 원래 문제: 효율적인 편집·순차 정보 이득 최대화. 새 질문: 지역/가산/결합 또는 내용/경로 모형이 다른 예측을 만드는 관측을 독립 실험에서 구별할 수 있는가. 근거: P070, P077, P078.

## C08-01 — 지역 정보의 합으로 충분한가: 정서관련 분산 정보와 영역 간 결합의 분리

**질문:** 동일한 감각·의미 정보와 유효 복잡도에서 영역 간 결합항은 지역 정보의 가산 결합보다 독립 자극의 측정된 정서 주석을 더 잘 설명하는가?

**관측대상:** 사전 정의 ROI/parcel의 시행별 다변량 반응; 지역 L, 분산 가산 D, 영역 간 저차원 결합 N / Axis: AS16, AS08, AS21

1. **모델 적용:** 자극 특징+각 ROI 내 비선형 특징을 갖는 L/D와 같은 유효 복잡도의 bilinear N을 교차검증한다. 먼저 자연 자극에서 D/N 예측 불일치가 큰 검증 집합을 분리하고, 생성 설계는 후속 단계로 둔다.
2. **과학적 질문:** whole-brain 이득이 단순 정보 분산인지 조건부 영역 간 통계적 결합인지 구분한다.
3. **가정 도전:** 분산 디코딩의 성공이 네트워크 상호작용을 뜻한다는 가정을 시험한다. D가 충분해도 분산 표상 설명은 유지되고 결합의 필요성은 축소된다.

**외부 원리:** Agent04의 자극조건부/신경조건부 정보 분해와 Agent09의 가설 판별 중심 설계. 원 문헌은 신호 예측·정보 이득 최적화이며, 새 질문은 정서관련 뇌정보를 기술하는 데 결합항이 필요한가이다.

**주가설:** N은 영역 내 비선형·자극 공통 입력·평균활성·신뢰도를 맞춘 D보다 독립 정서 주석의 held-out 설명력을 높인다.
**경쟁 설명:** ROI 수, 유연성, 자극 의미 또는 공통 HRF가 N의 이득을 모두 만든다.

**측정 대비:** 주지표는 미리 고정한 주석 예측 손실의 D−N 차이이며 stimulus/run holdout과 참가자별 추정치를 보고한다. 전체 신경반응 예측 향상은 보조지표로 분리한다. 주석을 쓰지 않는 stationary 공통입력 모형에서도 동일 이득이 생기는지 검사한다.

**반증:** 동등성 문턱과 검정력을 사전 설정한 뒤 N의 개선이 그 범위 안이거나 평균·주변분포·자기상관 보존 null에서 재현되면 결합 필요성을 반박한다. 신뢰도가 낮으면 기각 대신 식별 불가이다.

**Baseline:** 최선 단일 ROI L; 복잡도 일치 가산 D 및 영역 내 비선형 D; 자극 특징만 사용한 예측; 평균활성+공통입력 모형; train fold에서만 구성한 graph shuffle

**데이터 계획:** primary: Horikawa 보유본의 시행 반응·정서 주석 생성단위·자극 ID를 먼저 확인하여 정적 L/D/N 비교; extension: Emo-FilM 연속 BOLD가 확인될 때 시간 결합으로 확장; other_owned: NSD는 자극·공간 통제와 정서 주석이 존재할 경우에만 대비; Spacetop 및 Mind Captioning은 스키마 확인 후 별도 외적 검증

**실행조건:** 독립 자극 수와 반복 신뢰도; 주석이 자극 집계인지 개인별인지; 공간 범위·ROI 신호 품질; checkpoint가 필요하지 않은 ridge/bilinear fallback 가능; pretrained 활용 시 입력 및 학습중복 확인

**차별점:** 일반 network-state 추정이나 graph encoding의 성능 경쟁을 정서 주석 관련 정보에 대한 L/D/N 설명 필요성 검정으로 바꾼다.
**신규성 위험:** 분산 정서 디코딩 및 비선형 결합 연구와 중복 가능성이 높다. 강한 D·독립 주석·가설 판별 자극을 함께 쓴 선행연구 역검색이 필요하다.
**출처:** P027, P028, P067, P077; 가장 가까운 기존 문헌: P067, P028.

**여덟 탐색 질문:**

1. 분산 정보와 결합을 동일한 복잡도·신뢰도에서 비교하기 어려웠다. 미시도 여부는 미확인이다.
2. 자극 조건부 encoding과 검증 가능한 graph·상태 모형을 같은 평가에 놓을 도구가 있다.
3. 넓은 공간의 정보 곧 영역 상호작용이라는 가정이다.
4. AI는 복합 감각·의미 공통입력을 더 풍부하게 모형화할 가능성이 있다. 우월성은 아직 가설이다.
5. 공통입력 모형 밖의 반복 가능한 결합 정보가 후보이며 잔차 자체는 정서가 아니다.
6. Bayesian design의 목적을 ROI 활성 최대화에서 D/N 판별로 바꾼다.
7. Horikawa를 범주 분류에서 설명 구조 경쟁 자료로 재사용한다.
8. D로 충분하면 결합의 필수성을 줄이고 N이 남으면 가산 설명의 한계를 규정한다. 기능연결은 뇌 인과가 아니다.

## C08-02 — 감각–transmodal gradient의 긴 문맥 이득은 신경 통합인가 관측시간 효과인가

**질문:** 정서 주석 관련 신경분산에 대한 긴 과거 문맥의 추가 설명력은 HRF·자극 시간스펙트럼을 맞춘 뒤에도 cortical gradient 위치와 체계적으로 달라지는가?

**관측대상:** 피질 parcel별 독립 정서 주석 관련 encoding 이득 지도와 개인별 gradient; 피질하에는 동일 좌표를 강제로 부여하지 않음 / Axis: AS17, AS09, AS08

1. **모델 적용:** 동일 feature extractor의 짧은/긴 과거 문맥을 native TR에서 비교한다. 고정 SSM·선택적 SSM과 FIR/HRF family를 동등한 자료·용량으로 대조한다.
2. **과학적 질문:** 느린 BOLD 변화와 신경적 맥락 통합의 관측상 필요성을 분리한다.
3. **가정 도전:** 긴 문맥 모델의 우위나 느린 transmodal 신호를 긴 신경적 기억으로 해석하는 가정이다.

**외부 원리:** Agent04의 과거전용 selective state와 관측격자 분리. 원래 문제는 효율적인 시계열 표현이며 새 문제는 관측과정 이상의 정서관련 맥락 통합이 필요한 공간 위치이다.

**주가설:** 긴 문맥 이득 중 독립 정서 주석으로 한정한 대비가 자극 자기상관·유연한 HRF 보정 후에도 gradient 위치를 따라 증가한다.
**경쟁 설명:** HRF 지연, 사건 길이, 의미 feature 평활도, SNR 또는 모델 입력의 미래 정보가 지도 전체를 설명한다.

**측정 대비:** 같은 held-out 영화/run에서 문맥 길이별 encoding 손실 차이를 구하고 정서 주석 추가/제거의 nested 대비와 gradient 상호작용을 사전 지정한다. 전체 예측지도와 정서 관련 조건부 대비지도를 나란히 보고한다. 의미 통제가 공유 정서정보를 제거할 수 있으므로 고유분산을 순수정서라 부르지 않는다.

**반증:** 유연한 HRF/FIR·자극 스펙트럼 대조에서 gradient 효과가 소멸하거나 과거전용 모델이 양방향 복원에서만 보인 이득을 잃으면 장기 신경 통합 해석을 철회한다.

**Baseline:** 짧은 문맥+FIR; native TR와 보간 입력의 민감도 비교; 동일 스펙트럼의 자극 feature surrogate; 고정 SSM; gradient 대신 해부학적 거리·SNR·평활도

**데이터 계획:** primary: Emo-FilM 보유본에서 연속 BOLD·자극 onset·시간 주석을 확인할 때 우선; horikawa: 연속 신호 및 주석 시간격자가 확인되는 범위에만 적용; 시행 beta 순서를 연속 시간으로 만들지 않음; other_owned: Spacetop의 clip 평정을 연속 궤적으로 간주하지 않음; NSD/Mind Captioning은 연속성 미확인으로 시간 질문 적용 보류

**실행조건:** 원 TR·HRF 추정 범위·run 경계; 시간 정서 주석의 실제 척도와 해상도; 개인 gradient의 독립 추정 자료 또는 고정 외부 atlas; Brain-Mamba 공식 코드 가용성 미확인: 원리 검정은 작은 고정/선택적 SSM 또는 문맥 ridge로 대체

**차별점:** 일반 사건 통합시간 지도를 전체 성능이 아닌 독립 정서 주석 관련 문맥 이득의 공간적 경쟁 설명으로 좁힌다.
**신규성 위험:** temporal receptive window 및 자연주의 정서 encoding과 중복 가능. gradient 상관만 남으면 기존 연구의 반복이다.
**출처:** P028, P061, P063, P066, P068; 가장 가까운 기존 문헌: P066, P068, P028.

**여덟 탐색 질문:**

1. 입력 문맥·HRF·공간조직을 같은 자극에서 분리해야 해서 식별이 어렵다.
2. 고정/선택적 상태와 과거전용 마스킹을 비교할 공개 원리가 있다.
3. 느린 신호는 긴 신경 통합이라는 가정이다.
4. 시퀀스 AI는 사건의 과거 맥락을 명시적 조건변수로 만들 수 있다.
5. feature가 놓친 반복 가능한 문맥 민감성이 후보이나 HRF 차이를 먼저 제외한다.
6. 시스템 식별의 관측모형 경쟁을 gradient 해석에 적용한다.
7. 연속 정서 자료를 주석 예측에서 신경적 문맥 필요시간 검사로 재사용한다.
8. HRF로 충분하면 통합시간 주장을 축소하며, 잔여 효과가 있으면 공간적 통합 가설에 제약을 준다.

## C08-03 — 정서관련 모델–뇌 지도의 공간 조직은 비정상적 신뢰도가 만든 모양인가

**질문:** 정서관련 정보 이득의 cortical gradient 정렬은 영역별 신뢰도·평활도·공간변환이 다른 귀무 관측에서도 재현되는가, 아니면 이 조건들을 넘는 해부학적 조직인가?

**관측대상:** 정서 주석의 조건부 encoding 이득 지도와 반복 신뢰도 지도; parcel과 dense 표현의 대응 / Axis: AS18, AS07, AS17

1. **모델 적용:** dense→parcel 변환과 지역별 측정잡음·공간 평활도를 반영한 nuisance-only 생성모형을 사용하여 전체 encoding→map→gradient 통계 절차를 재실행한다. BrainSMASH의 적용 가정을 자료에서 진단하고 대체 null도 비교한다.
2. **과학적 질문:** 정서관련 신경정보의 위치 주장이 생물학적 조직과 측정 신뢰도 중 무엇에 의존하는지 검사한다.
3. **가정 도전:** 공간 null 한 종류의 유의성이 실제 공간 조직을 보증하고 모든 위치에서 오류율이 같다는 가정이다.

**외부 원리:** Agent04의 공간집계 자체가 정보 병목이라는 질문을 Agent08의 비정상적 spatial null에 수입한다. 원래 목적은 범용 표현 평가·공간 오류 제어이며 새 질문은 정서관련 공간 조직의 관측 가능성이다.

**주가설:** 자료형에 맞게 보정한 비정상적 null에서도 정서관련 이득 지도와 gradient의 관계가 별도 자극/반복에서 유지된다.
**경쟁 설명:** transmodal 부위의 낮은 SNR·영역별 평활도·집단 변환·parcel 크기 차이가 위치 효과를 만든다.

**측정 대비:** 주검정은 지역별 잡음/평활도 생성계에서의 명목 제1종 오류·검정력과 실자료 효과의 위치이다. 정서 연관이 없는 null에서도 관측된 상관이 흔한지 본다. 별도 반복에서 효과의 방향 및 크기를 검증한다.

**반증:** 현실적인 nuisance-only 모형이 관측된 지도를 설명하거나 spatial representation을 맞춘 뒤 효과가 소멸하면 신경 공간조직 주장을 기각한다. null 적합 실패시 결론 보류.

**Baseline:** 독립 parcel permutation은 실패 기준용 비교만 사용; 피질에 적합한 spin; 거리 기반 spatial surrogate; 지역별 신뢰도·평활도 보정 surrogate; 동일 자료의 dense/parcel 지도

**데이터 계획:** primary: Horikawa의 반복 및 공간 반응이 확인되면 정서관련 지도부터 평가; extension: NSD 반복자료가 보유본에 실제 있을 때 공간방법의 잡음 calibration; 독립 정서 주석 없이 정서 효과를 주장하지 않음; other_owned: Emo-FilM의 시간지도는 시간 의존성까지 결합한 별도 검정; Mind Captioning·Spacetop은 공간 표면·반복 스키마 확인 후 조건부

**실행조건:** surface/native 정렬·parcel 면적·mask; 반복으로 추정 가능한 위치별 신뢰도; null의 variogram·분포 적합성; 피질하 분석은 별도 거리기하 사용; cortical spin 적용 금지

**차별점:** 공간 null 방법 자체의 개발을 최초라고 주장하지 않는다. 정서관련 지도에서 정보 집계와 비정상적 측정이 만드는 가짜 조직을 명시적으로 식별하는 응용 질문이다.
**신규성 위험:** 방법론적 감사에 머물 위험이 크다. 특정 신경 공간조직의 상반 예측을 구별하지 못하면 독립 생물학 RQ 대신 모든 지도 후보의 필수 측정 게이트로 유지한다.
**출처:** P026, P062, P063, P064; 가장 가까운 기존 문헌: P063, P064, P062.

**여덟 탐색 질문:**

1. 위치별 ground truth가 없어 공간 오류율을 실자료만으로 식별하기 어렵다.
2. 공개 공간변환·surrogate·다중 입력 표현 도구로 분석 전체의 모의 검증이 가능하다.
3. 한 spatial null이면 모든 공간 지도가 타당하다는 가정이다.
4. AI는 복잡한 신호의 예측지도를 만들지만 오류율 개선을 보장하지 않는다.
5. 공간평균이 지운 희소 정보가 후보이며 반복 신뢰도로 존재부터 확인한다.
6. 생성모형 검증을 실제 뇌지도 해석의 음성대조로 가져온다.
7. 보유 반복 뇌자료를 새 라벨 없이 측정 오차 calibration에 사용한다.
8. 어떤 정서 위치 주장이 식별 가능한지 경계를 바꾼다. 방법적 보정만 나오면 독립 기제 발견이라고 하지 않는다.

## C08-04 — 정서 변화와 동행하는 network-state는 자극 동기화 구조를 넘어서는가

**질문:** 정서 주석 변화와 동행하는 잔여 network-state는 자극 조건부 평균·HRF·사건 경계를 제거한 뒤 다른 run/자극에서도 독립적인 예측 정보를 주는가?

**관측대상:** 연속 BOLD의 cross-fitted 잔차에 대한 평균 상태·공분산 상태·그 결합 및 전이 시점 / Axis: AS16, AS08, AS18

1. **모델 적용:** train fold에서만 자극 encoding을 학습하고 독립 잔차로 mean-only/shared-covariance, covariance-only, both HMM을 비교한다. 상태 학습에 정서 라벨을 쓰지 않고 held-out 주석 변화와의 관계를 별도 평가한다.
2. **과학적 질문:** 지역 평균의 사건 전환과 공분산 구조의 상태 전환이 같은 현상인지 구별한다.
3. **가정 도전:** 추정된 network-state가 곧 자극과 독립적인 내재 신경 상태이며 정서 상태라는 가정이다.

**외부 원리:** Agent04의 stimulus→brain 대 brain-block→brain 조건부 불일치를 수입한다. 원 목적은 예측가능 정보의 분해이며 새 질문은 정서 주석과 연결된 시간적 상태가 어떤 조건에서 필요한지이다.

**주가설:** 공통 입력과 사건 경계를 조건화해도 covariance-state가 평균 상태보다 독립 주석 변화에 대한 예측을 개선하며 학습 외 자극에서 재현된다.
**경쟁 설명:** 불완전한 자극 특징·평균 전환·HRF·motion 또는 짧은 window의 covariance 추정 오차가 상태처럼 보인다.

**측정 대비:** 주석 변화에 대한 held-out log score의 공분산 상태 추가 이득과 상태모형의 held-out BOLD likelihood를 각각 보고한다. 반복 자극이 있으면 자극 동기화 성분과 반복별 잔여 성분을 분리하되 후자를 내재 상태로 확정하지 않는다.

**반증:** stationary 공분산+자극 동기화 평균 null이 같은 상태 이득을 내거나 상태 구조가 별도 run에 전이되지 않으면 동적 결합 설명을 반박한다. 뇌 likelihood만 개선되고 정서 대비가 없으면 일반 동역학 후보로 축소한다.

**Baseline:** 자극 encoding+FIR; mean-only HMM; stationary regularized covariance; 독립 사건 경계 예측; 같은 시간스펙트럼·평균반응을 보존한 시뮬레이션

**데이터 계획:** primary: Emo-FilM의 원 연속 신호·시간 주석·run 경계가 확인될 때; extension: Horikawa/Spacetop은 연속 자료가 실제 있을 때만 적용; other_owned: NSD 시행 beta와 Mind Captioning 이름만으로 연속 상태 입력을 만들지 않음

**실행조건:** 충분한 연속 신호 길이와 독립 run; motion·생리/측정 nuisance 가용성; 상태 수·covariance 차원·regularization을 정할 내부 validation; annotation 빈도·HRF 지연·사건 경계의 독립 출처

**차별점:** HMM 상태의 존재를 보이는 것을 넘어 자극조건부 잔차와 독립 정서 대비에 상태의 추가 필요성을 동시에 요구한다.
**신규성 위험:** 자연주의 dynamic connectivity 및 잔차 네트워크 연구와 겹칠 수 있다. residualization만으로 신규성 또는 내재성은 확보되지 않는다.
**출처:** P027, P029, P066, P067; 가장 가까운 기존 문헌: P067, P066.

**여덟 탐색 질문:**

1. 자극 모형의 오지정과 잠재 상태를 같은 관측으로 구별하기 어렵다.
2. 풍부한 자극 encoding과 neural prediction을 cross-fit해 공통입력 설명을 강화할 수 있다.
3. 상태 추정은 생물학적 실재 또는 내재성의 증거라는 가정이다.
4. AI는 자극 사건과 평균반응을 더 유연하게 설명할 가능성이 있다.
5. 자극 모형이 놓친 반복 가능한 covariance 변화가 후보이나 누락 feature와 구별해야 한다.
6. 잠재상태 시스템 식별의 관측모형 경쟁을 정서 변화 분석에 적용한다.
7. 연속 자료에서 정서 경계·자극 경계·공분산 경계를 서로 다른 관측으로 시험한다.
8. 어떤 종류의 상태 설명이 필요한지 제한한다. 잔차의 존재만으로 자극 독립성 또는 뇌 인과를 주장하지 않는다.

## C08-05 — 내용이 같은 모델에서 계산 경로의 제약이 정서관련 신경정보를 가르는가

**질문:** 자극 내용의 표현력과 출력 성능을 맞춘 모델에서 해부·기능·gradient 기반 경로 제약 중 어떤 것이 독립 정서관련 신경 대비를 더 잘 보존하는가?

**관측대상:** 여러 피질계와 별도 피질하 ROI의 정서 주석 관련 encoding 대비; 모델 내부 경로와 실제 구조적 연결을 동일시하지 않음 / Axis: AS16, AS07, AS21

1. **모델 적용:** 같은 feature·자료·용량으로 해부 거리 순서, 기능 유사도 순서, gradient 순서, 무작위 순서의 작은 graph/SSM 모형을 비교한다. 학습fold 외부의 테스트 신호로 순서를 만들지 않는다. 각 모형의 일반 자극 성능을 맞춘 뒤 정서관련 뇌 대비의 불일치를 평가한다.
2. **과학적 질문:** 자극 내용의 공통 표현으로 충분한지 아니면 관계 제약이 독립 신경정보를 예측하는 데 필요한지 판별한다.
3. **가정 도전:** 같은 내용·비슷한 task 성능을 가진 모델은 신경적으로 동등하며 기능 유사성 기반 경로가 곧 뇌의 실제 전달 경로라는 두 가정을 분리한다.

**외부 원리:** Agent04의 graph ordering과 gradient positioning이라는 경쟁 prior, Agent09의 최대활성 대신 경쟁 모형 판별 자극 선택. 원래 문제는 효율적 입력배열·표현학습이며 새 질문은 내용 충분성 대 경로 제약의 필요성이다.

**주가설:** 일부 관계 제약은 일반 자극 예측 성능·복잡도·SNR을 맞춘 상태에서도 정서관련 신경 대비의 held-out 설명력을 보존한다.
**경쟁 설명:** 경로 효과는 정규화 강도·순서에 따른 접근 가능한 문맥·입력차원 또는 데이터 누수일 뿐이다.

**측정 대비:** 고정 encoding head에서 정서 주석 추가/제거 대비의 경로×정보 상호작용을 검정한다. 내용 retrieval/일반 encoding 점수를 함께 맞춘다. 자연 자극 내 모형 불일치 집합을 개발자료에서 고르고 test 자극에 선택 규칙을 고정한다. 생성 편집은 타당성을 통과하고 새 뇌 반응을 측정할 때만 확장한다.

**반증:** 내용 성능·경로 길이·regularization을 맞추면 차이가 없거나 정서와 무관한 모든 신경 신호가 동일 비율로 좋아지면 정서관련 관계 제약의 기여 주장을 축소한다. 학습 seed 또는 자극에 따라 역전되면 안정된 prior라는 가설을 반박한다.

**Baseline:** 순서 없는 pooled/content-only 모델; 같은 연결수·차수·경로 길이의 무작위 graph; 해부학적 거리만 사용; 영역별 독립 모델; 경로 동일·입력 내용 교환 대조

**데이터 계획:** primary: Horikawa 시행 반응에서 정적 관계 제약 비교; 연속 입력이 없으면 SSM 대신 graph/가산 표현 사용; extension: Emo-FilM 연속 신호가 있을 때 경로와 시간 문맥을 분리한 비교; other_owned: NSD는 일반 내용성능의 대조; Mind Captioning은 텍스트가 해당 뇌반응에서 생성되었는지 출처 확인; Spacetop은 대응 자극·주석 조건 충족 시 검증

**실행조건:** 정확한 ROI 입력 범위와 피질하 지원; 학습 자료로만 추정한 기능 graph/gradient; 내용 성능 및 유효 복잡도 동등화의 사전 기준; Brain-Mamba 코드404 기록이 있으므로 작은 재구현 원리 검정 fallback; 구현을 원모델 성능 재현이라 하지 않음; 새 편집 자극에는 기존 BOLD를 붙이지 않고 실제 추가 측정 필요

**차별점:** graph/gradient prior의 benchmark 순위에서 내용이 동등한 조건의 정서관련 신경 대비와 경쟁 경로의 필요성으로 질문을 바꾼다.
**신규성 위험:** Agent11의 routing 연구와 중복 가능. 본 후보는 AI 경로의 뇌 기제 동일성을 주장하지 않고 기능/해부/gradient prior의 정보적 구별에 제한한다. 강한 내용 대조가 불가능하면 방법 비교로 보류한다.
**출처:** P028, P029, P061, P070, P077; 가장 가까운 기존 문헌: P028, P029.

**여덟 탐색 질문:**

1. 경로를 바꾸면 표현력·문맥·정규화가 동시에 바뀌어 내용 효과와 분리하기 어려웠다.
2. functional ordering과 gradient positioning이라는 서로 다른 공개 원리가 비교 가능한 가설을 제공한다.
3. 내용 성능이 같으면 신경설명도 같다는 가정과 기능연결=전달경로라는 가정을 구분한다.
4. AI는 같은 입력에 대한 대안 계산 경로를 통제된 비교 대상으로 만들 수 있다.
5. 모형 모두가 놓친 관계 의존 신경 대비가 후보이나 측정 신뢰도 검증부터 필요하다.
6. 가설 판별 중심 자극 선택을 관계 prior의 competing prediction에 적용한다.
7. 정서 분류 자료를 경로 prior와 내용 충분성을 대조하는 자료로 재사용한다.
8. 어떤 계산 제약이 관측 설명에 필요한지 제한한다. 모델 경로 절제는 인간 뇌 회로 절제나 뇌 인과 증거가 아니다.

## 검증 범위와 근거 링크

| ID | 문헌 | 기존 검증 범위 |
|---|---|---|
| P026 | [Scaling Vision Transformers for Functional MRI with Flat Maps](https://github.com/MedARC-AI/CortexMAE) | 본문: 아니오; 공식 README/코드만 확인; Discussion: 아니오; 근거: E1(공식 README/코드 범위; 논문 결과 검증과 구분) |
| P027 | [A foundation model of vision, audition, and language for in-silico neuroscience](https://github.com/facebookresearch/tribev2) | 본문: 아니오; 공식 README/코드만 확인; Discussion: 아니오; 근거: E1(공식 README/코드 범위; 논문 결과 검증과 구분) |
| P028 | [Brain-Mamba: Encoding Brain Activity via Selective State Space Models](https://proceedings.mlr.press/v248/behrouz24a.html) | 본문: 예; 출판사 PDF 전체; Discussion: 예; Conclusion p242 및 Appendix E pp249–250; 근거: E1(논문 본문·부록 직접 확인) |
| P029 | [Brain-JEPA: Brain Dynamics Foundation Model with Gradient Positioning and Spatiotemporal Masking](https://github.com/Eric-LRL/Brain-JEPA) | 본문: 아니오; 공식 README/코드만 확인; Discussion: 아니오; 근거: E1(공식 README/코드 범위; 논문 결과 검증과 구분) |
| P061 | [BrainSpace: a toolbox for the analysis of macroscale gradients in neuroimaging and connectomics datasets](https://github.com/MICA-MNI/BrainSpace) | 본문: 아니오; 공식 문서/코드만 확인; Discussion: 아니오; 근거: E1-공식 코드/문서; 논문 본문·Discussion 미확인 |
| P062 | [neuromaps: structural and functional interpretation of brain maps](https://github.com/netneurolab/neuromaps/blob/main/markello2022natmethods.pdf) | 본문: 예; 공식 저장소 postprint의 Abstract/Results 일부/Discussion 직접 읽음; Discussion: 예; Discussion 전체 해당 문단; 근거: E1-논문 본문 및 Discussion 직접 확인 |
| P063 | [Comparing spatial null models for brain maps](https://github.com/netneurolab/markello_spatialnulls/blob/master/manuscript/main.tex) | 본문: 예; Abstract 및 Discussion 직접 읽음; 전체 방법 절을 정독했다고 주장하지 않음; Discussion: 예; Discussion 및 권고사항; 근거: E1-논문 본문 및 Discussion 직접 확인 |
| P064 | [Generative modeling of brain maps with spatial autocorrelation](https://github.com/murraylab/brainsmash) | 본문: 아니오; 공식 문서/코드만 확인; Discussion: 아니오; 근거: E1-공식 코드/문서; 논문 본문·Discussion 미확인 |
| P066 | [Discovering event structure in continuous narrative perception and memory](https://github.com/brainiak/brainiak/blob/master/src/brainiak/eventseg/event.py) | 본문: 아니오; 공식 문서/코드만 확인; Discussion: 아니오; 근거: E1-공식 코드 및 tutorial; 논문 본문·Discussion 미확인 |
| P067 | [Brain network dynamics are hierarchically organized in time](https://github.com/OHBA-analysis/HMM-MAR) | 본문: 아니오; 공식 문서/코드만 확인; Discussion: 아니오; 근거: E1-공식 코드/문서 범위; 논문 본문·Discussion 미확인 |
| P068 | [Neurophysiological signatures of cortical micro-architecture](https://github.com/netneurolab/shafiei_megdynamics) | 본문: 아니오; 공식 문서/코드만 확인; Discussion: 아니오; 근거: E1-공식 코드/문서; 논문 본문·Discussion 미확인 |
| P070 | [Prompt-to-Prompt Image Editing with Cross-Attention Control](https://raw.githubusercontent.com/prompt-to-prompt/prompt-to-prompt.github.io/main/ptp_files/Prompt-to-Prompt_preprint.pdf) | 본문: 예: 공식 PDF 확보·§1/§3/§4/§5 관련 부분 직접 열람; 전체 정독 아님; Discussion: 예: §5 Limitations p.9; §4 평가 논의 p.9; 근거: E1 |
| P077 | [Deep Adaptive Design: Amortizing Sequential Bayesian Experimental Design](https://proceedings.mlr.press/v139/foster21a.html) | 본문: 예: 공식 PDF 확보; §2–4/§7 직접 열람; Discussion: 예: §7 Discussion 및 Limitations and Future Work p.9; 근거: E1 |

## 한계와 다음 단계

- 모든 새로운 신경 질문과 예상 결과는 E3 가설이다. 기존 catalog의 E1은 본문·코드 범위를 구별하여 계승하며 이번 Round2의 새 원문 검증은 아니다.
- 사용자는 Horikawa·Emo-FilM·Mind Captioning·NSD·Spacetop 보유를 밝혔다. 보유 사실과 경로·버전·스키마 검증은 다르며 스키마는 후보 실행조건으로 둔다.
- 기능연결·covariance·모델 경로 효과는 BOLD 수준의 조건부 통계 설명이며 신경 인과·전달 방향·같은 알고리즘의 증거가 아니다.
- 같은 자극·반복·run은 분할을 넘지 않는다. feature 선택·정규화·graph·gradient·상태 수·공간 null 적합·잔차화는 학습fold에서 수행하고 참가자/자극 계층 및 다중비교를 반영한다.
- 새로운 외부 신규성 역검색은 이번 Round2에서 수행하지 않았다. 가장 가까운 문헌은 보유 catalog 범위이며 세계 최초를 주장하지 않는다.
- C08-03은 특정 공간조직의 경쟁 설명을 가르지 못하면 독립 생물학 RQ로 세지 않고 공통 측정 게이트로 유지한다.
