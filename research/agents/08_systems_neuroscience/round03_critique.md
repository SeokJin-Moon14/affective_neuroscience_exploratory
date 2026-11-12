# Agent08 Round3 — Agent09·Agent01 전체 후보 비판

실제 Round2 원본을 읽고 C09-01~05, C01-01~05 총 10개를 검토했다. 수정 9개, 강한 신경 주장 보류 1개다. 보류는 아이디어 폐기 또는 전체 후속 작업 중단을 뜻하지 않는다. 새 원문 검증·원자료 분석은 수행하지 않았다.

## R3-08-C09-01 — 수정

**가장 강한 반론:** 같은 전체 likelihood는 같은 정서정보 제약을 뜻하지 않으며, 두 평가 encoder가 같은 학습편향을 공유하면 독립 평가도 명목상 독립일 수 있다.

**여덟 체크:**

1. P076의 관측조건 샘플링과 P053의 비식별성은 선행이다. 독립 정서 대비에서 관측 기여를 확인하는 부분이 남지만 brain-decoding prior 감사 전체를 새롭다고 할 수 없다.
2. 단순 guidance ablation이면 방법 점검이다. 원본 정서 회복과 실제 신경 대비 기여를 다른 추정량으로 고정해야 신경 질문이 된다.
3. 전체 likelihood를 맞춰도 해당 정서 neural contrast의 likelihood가 다를 수 있다. 정서 대비가 없는 고차원 잔차가 전체 적합도를 지배할 수 있다.
4. 반복별 BOLD·대비 정의용 독립 주석·관측잡음 covariance·원본 가족 및 participant ID가 필요하다. 5종 보유만으로 충족되지 않는다.
5. 원 자극 의미와 prior의 학습 의미가 공유되므로 prior 간 안정성은 독립 증거가 아니다. 감각·의미·HRF 조건을 보존한 shuffle이 필요하다.
6. 관측 기여의 통계적 attribution에 한정하면 적절하다. 생성된 이미지 내용의 안정성을 뇌 계산 기제로 부르면 안 된다.
7. 복수 독립 encoder, 실제 반복으로 calibration한 신경 대비별 likelihood, nuisance-조건부 관측 교환을 추가한다.
8. 신뢰도가 충분한데 prior-only와 같으면 그 대비를 뇌에서 읽었다는 주장을 제한한다. 낮은 신뢰도에서는 미식별이다.

**필수 수정:**

- 전체 BOLD 적합도와 사전고정 정서 neural contrast 적합도를 분리한 이중 estimand를 명시한다.
- encoder의 학습자료·특징 및 noise model 공유 여부를 기록하고 실제 반복으로 대비별 오차를 calibration한다.
- 원본 자극 family를 독립단위로 두고 여러 생성 seed를 표본수로 세지 않는다.

**더 강한 판별 대조:** 같은 감각·의미 조건 안에서 관측 대비만 다른 실제 반복/자극 쌍을 골라 진짜 관측·조건부 교환·prior-only를 비교한다. 전체 적합도 일치 층과 정서 대비 적합도 일치 층을 따로 평가하여 prior 안정성의 이유를 구별한다.

**음성 결과의 가치:** 관측의 독립 기여가 없으면 정서적으로 그럴듯한 생성물에서 읽을 수 있는 신경정보의 범위를 축소한다.

**남은 불일치:** 완전히 독립적인 likelihood의 충분성은 실제 반복·외적 검증 없이 결정할 수 없다. prior 공통편향의 모든 영향을 제거할 수 있다는 합의는 없다.

**근거:** P076, P053, P100, P067.

## R3-08-C09-02 — 수정

**가장 강한 반론:** 샘플링으로 발견한 최소–최대 범위는 가능한 전체 범위의 내부 근사다. 좁아졌다는 결과는 탐색 실패와 고유 식별을 구별하지 못한다.

**여덟 체크:**

1. 역문제의 비유일성은 P053/P076에 이미 있다. 정서 대비의 관측상 구별 실패에 대한 검증 가능한 witness를 찾는 부분이 남는다.
2. 복수 sampler benchmark가 아니라 같은 실측 관측에 적합한 반대 정서 후보의 존재를 시험하면 구별된다.
3. 전체 관측 적합도가 같은 두 후보도 정서 대비를 예측하는 특정 ROI에서 달라질 수 있어 contrast별 관측오차가 필요하다.
4. 실제 반복 covariance·허용오차 개발자료·후보 독립 주석·encoder 외삽 검증이 필요하다.
5. 극값 탐색은 의미 외삽과 encoder의 adversarial 취약점을 악용할 수 있다. 자연 matched 후보와 범위 제한을 우선한다.
6. 경험적 범위를 엄밀 bound로 부르지 않은 점은 적절하다. 다만 좁은 유한 탐색 범위로 비식별 가설을 반박하는 조건은 논리적으로 너무 강하다.
7. 알려진 관측모형의 합성 식별/비식별 문제에서 탐색 실패율을 측정하고 자연 자극 witness를 추가한다.
8. 서로 다른 valid 해를 찾으면 해당 관측모형의 비유일성을 보인다. 찾지 못한 결과는 탐색 능력의 한계도 포함하므로 식별 성공이 아니다.

**필수 수정:**

- 주추정량을 식별구간 추정에서 사전지정 차이 이상의 valid witness 발견 여부와 경험적 탐색 범위로 바꾼다.
- 반증을 충분한 탐색이라는 미확정 조건에 의존시키지 말고 알려진 합성 문제에서의 탐색 검출력과 실제 관측 추가에 따른 witness 배제율로 구체화한다.
- 새 후보의 실제 BOLD 동등성은 별도 측정 전에는 주장하지 않는다.

**더 강한 판별 대조:** 관측량을 늘릴수록 이미 발견한 반대 정서 witness가 별도 반복 likelihood에서 탈락하는지 평가한다. encoder 적합도만 높고 반복 검증에서는 탈락하면 모형오류 설명이 우세하다. 좁은 범위는 탐색상 음성 결과로 남긴다.

**음성 결과의 가치:** 후보 집합의 폭보다 어떤 추가 관측이 기존 비유일한 해를 배제하는지 배워 측정 설계를 개선한다.

**남은 불일치:** 유한 생성 탐색만으로 전체 식별집합의 외부 경계를 보장하는 방법은 제시되지 않았다. 실제 뇌의 구별능력과 현재 encoder의 구별능력도 별개다.

**근거:** P076, P053, P057, P100.

## R3-08-C09-03 — 수정

**가장 강한 반론:** pass/fail은 편집 후 발생한 선택변수이므로 두 집단이 정서 조작량·복잡도·자연성에서 달라질 수 있다. 보존군 효과 소실이 정서 신경정보의 부재와 같지 않다.

**여덟 체크:**

1. P070/P078의 편집 보존과 일반 자극 통제는 선행이다. 독립 보존 기준을 통과한 실제 신경 대비의 존재가 남은 질문이다.
2. 보존 QC만 하면 방법후보다. 새 측정에서 목표 대 동강도 비목표의 독립 정서 대비가 필요하다.
3. 정서 주석 차이 자체가 보존 성공군과 실패군에서 다르면 BOLD 차이를 선택적 정서 효과로 읽을 수 없다.
4. 독립 사건·감각·정서 평정, 보존 점수 연속값, 새 자극 onset·반복·피험자 수가 필요하다.
5. 보존 여부로 조건화하면 편집 강도·의미 복잡도·정서 변화량이 함께 선택될 수 있다. pass/fail 차이는 단순 artifact 효과가 아니다.
6. 보존 판정의 인과효과가 아니라고 명시한 점은 타당하다. 무작위 자극 제시도 정서만의 선택적 원인을 보증하지 않는다.
7. 개발자료에서 정한 공통 지지 내 편집량 층화, 목표/비목표 무작위 제시, 원본 family별 paired contrast가 더 강하다.
8. 보존 성공군의 충분한 주석 대비에도 BOLD 효과가 없으면 시험한 강도·내용 범위에서 선택적 신경 대비를 축소한다.

**필수 수정:**

- 개발자료에서 보존·조작량 허용영역을 고정하고 해당 영역을 대상으로 estimand를 한정한다.
- 보존 연속점수와 실제 정서 주석 변화량을 함께 보고, 공통 지지가 없는 strata는 비교에서 제외한다고 사전 명시한다.
- 원본 family와 참가자를 계층단위로 삼고 편집 seed는 가족 내 반복으로 처리한다.

**더 강한 판별 대조:** 같은 원본에서 주석 변화량·감각 편집량을 맞춘 목표/비목표 후보를 사전 검증한 뒤 실제 측정 순서를 무작위화한다. pass/fail 상관 비교는 보조 분석으로 두고 독립 주석을 가진 자연 matched 자극과 효과 방향을 비교한다.

**음성 결과의 가치:** 검증된 조작이 없어서 효과가 없는 경우와 충분한 조작에도 신경 대비가 없는 경우를 구별할 수 있다.

**남은 불일치:** 사전정의 의미 차원 밖의 미측정 변화는 남는다. 선택적 정서 조작의 완전성에는 합의할 수 없다.

**근거:** P070, P078, P100, P102.

## R3-08-C09-04 — 수정

**가장 강한 반론:** 정책이 선택한 서로 다른 자극에서 특정 모형을 더 자신 있게 고르는 것이 옳은 모형 판별임을 보장하지 않는다. 공통 오지정이 정보 이득을 과장할 수 있다.

**여덟 체크:**

1. P077의 정보 이득 설계가 이미 핵심 원리다. fMRI 의존성과 편집 실패를 포함한 실제 정책 판별이 남는다.
2. 정책 점수 향상만으로 새로운 신경 기제는 아니다. 경쟁 신경 가설의 어느 상반 예측을 가르는지 고정해야 한다.
3. 일반 BOLD log score와 독립 정서 contrast의 모형 구분 점수를 분리해야 한다. 모형 둘 모두 틀린 경우도 포함해야 한다.
4. 새 시행·새 주석 예산, HRF·순서 영향, likelihood calibration, 정책별 실제 선택확률 및 독립 평가 pool이 필요하다.
5. EIG가 의미 외삽·motion·낮은 SNR을 선호할 수 있으며 정책마다 다른 자극 분포에서 점수를 직접 비교하면 난이도 차이와 섞인다.
6. 실측을 요구한 경계는 적절하다. posterior의 자신감 증가나 큰 Bayes factor를 참 신경 가설 발견으로 해석하면 안 된다.
7. 공통 고정 평가 pool의 proper score, 두 모형 모두 오지정인 synthetic 대조, validity filter-only 정책을 추가한다.
8. 단순 coverage가 동등하면 복잡한 정책의 필요성을 줄일 수 있다. 모든 모형 calibration 실패는 가설군 수정 신호이다.

**필수 수정:**

- 모형 구분 성공과 예측 calibration을 별도 지표로 두고 neither-model 적합성 검사를 추가한다.
- 선택 자극 내 설계 효율과 공통 held-out 평가 pool의 일반화를 분리한다.
- 원본 family·실제 참가자·독립 run을 표본 단위로 하고 비용에 실패한 후보 및 주석 비용을 포함한다.

**더 강한 판별 대조:** 알려진 참 모형·두 모형 모두 틀린 모의 관측에서 policy 실패 양상을 먼저 비교하고, 실제 자료에서는 정책을 개발자료에 고정한 뒤 같은 별도 평가 pool의 정서 대비 log score와 calibration을 평가한다. 정보 이득과 반응 크기를 분리한다.

**음성 결과의 가치:** 유효성 층이 효과가 없으면 단순 설계를 택하고, 모든 정책이 자기 simulator에서만 성공하면 관측모형을 고쳐야 함을 배운다.

**남은 불일치:** 실제 뇌의 참 모형은 알려져 있지 않으므로 진실 발견률을 직접 보고할 수 없다. 정책 비교는 관측 예측·calibration 범위에 제한한다.

**근거:** P077, P100, P098, P067.

## R3-08-C09-05 — 수정

**가장 강한 반론:** 소수의 family와 비공개 학습계보로는 생성기 모집단 일반화를 추정할 수 없으며, 가족 간 대비 차이는 artifact뿐 아니라 실제 조작의 의미 차이일 수 있다.

**여덟 체크:**

1. P098/P099의 domain generalization은 이미 확립된 문제다. generator family가 신경 대비의 일반화 축인지 검증하는 응용이 남는다.
2. 두 생성기 순위만 비교하면 benchmark다. 일차 추정량을 family×정서 대비 상호작용과 사전 동등성 검정으로 정해야 한다.
3. 일반 이미지/BOLD 품질의 차이를 정서 contrast의 불변성과 분리한 점은 적절하다. domain별 대비 신뢰도를 실제로 추정해야 한다.
4. 모델 계보·지원분포·조작 주석·새 반복 BOLD와 충분한 독립 family 수가 필요하다. 두 pipeline만 있으면 모집단 일반화를 제한한다.
5. 같은 prompt는 같은 실제 조작이 아니다. 가족별 감각 흔적과 의미 보존이 같아야 하는 공통 지지가 필요하다.
6. 생성기 간 불변성은 자극 효과의 강건성이지 특정 신경 회로의 인과성은 아니다. 기존 경계는 대체로 적절하다.
7. 자연 matched control과 독립 artifact 특징, family를 고정효과로 처리한 paired contrast, 조작량 동등성 검정이 강하다.
8. 조작 성공·신뢰도가 충분한 family에서만 실패하면 적용범위를 제한한다. 실패의 원인을 보편적인 생성 artifact로 단정하지 않는다.

**필수 수정:**

- 독립 family 정의를 학습목표·backbone·weights 출처로 기록하고 불명확한 항목을 그대로 남긴다.
- 두 family 수준이면 고정된 두 구현 범위의 비교라고 명시한다.
- 정서 주석 변화량과 신경 대비의 동등성 문턱을 개발자료에서 고정하고 seed를 family의 독립 반복으로 세지 않는다.

**더 강한 판별 대조:** 원본 family를 공유하는 두 검증 pipeline과 자연 자극에서 실제 정서 주석 변화량을 맞춘 paired 실험을 수행한다. 신경 대비의 family 상호작용과 단순 SNR 차이를 분리한 뒤 held-out 원본에 전이한다.

**음성 결과의 가치:** 어떤 구현·내용 범위에서 재현되는지 구체화할 수 있고, 소수 family에서의 성공을 보편적 정서 개입으로 확대하지 않는다.

**남은 불일치:** 비공개 학습자료로 생성기 독립성이 완전히 확인되지 않을 수 있다. 현재 후보는 제한된 pipeline 강건성까지가 검증 가능한 범위다.

**근거:** P078, P070, P098, P099, P100.

## R3-08-C01-01 — 수정

**가장 강한 반론:** 내용 보류에서 대비 방향이 바뀌어도 공통 잠재 정서코드를 읽는 감각 gain·관측모형의 변화일 수 있다. 내용×정서 모형 우위만으로 표상 코드 자체의 변형을 식별하기 어렵다.

**여덟 체크:**

1. P001의 분산 정서 표상과 cross-decoding이 선행 범위다. 내용 그룹에 대한 불변 대 상호작용 경쟁의 정확 중복은 미확인이다.
2. ID에서 내용 단위로 바꾼 것만으로 새 신경 질문은 아니다. 불변 축과 관계 변화 모형의 상반 예측을 주검정으로 고정하면 유지 가능하다.
3. 명시한 정서 대비는 적절하다. 그러나 시각/의미 잔차를 순수정서로 부를 수 없고 total/conditional 효과를 함께 보고해야 한다.
4. 영상–BOLD–주석 join, dupidx 적용 범위, 내용별 정서 공통 지지, 반복별 신뢰도가 필요하다.
5. 동영상 motion·길이·HRF와 장면 구성의 상관이 내용 보류 실패를 설명할 수 있다. embedding 하나가 내용 등가성을 보증하지 않는다.
6. 내용 일반화는 표현 대응이지 추상 정서 기제 또는 인과 코드의 증거가 아니다.
7. 독립 내용 주석과 복수 embedding, 내용을 조건화한 공통 잠재코드+gain/측정모형을 추가한다.
8. 공통 지지·신뢰도 충분 조건에서 불변 축이 실패하면 시험한 내용에서의 적용범위를 제한할 수 있다. 전체 뇌의 불변코드 부재는 아니다.

**필수 수정:**

- 불변성을 신경공간의 고정방향인지, 사전 제한한 관측변환 아래 공통 잠재코드인지 정의한다.
- 내용 그룹은 독립 내용 주석으로 검증하고 임계값·embedding 선택은 개발자료에 고정한다.
- 내용 그룹×정서 대비×참가자 계층을 명시하고 자극쌍 수를 독립 N으로 세지 않는다.

**더 강한 판별 대조:** 같은 잠재 정서축에 내용별 gain·공통 선형 관측만 허용한 모형과 내용별 관계변형 모형을 동일 복잡도로 비교한다. 대비 자체의 신뢰도를 독립 반복에서 먼저 측정한 뒤 새로운 내용 그룹의 방향 및 크기를 예측한다.

**음성 결과의 가치:** 불변성의 어떤 정의가 충분한지 정하고, 단순 관측변환으로 설명되면 새 코드 주장을 축소한다.

**남은 불일치:** 뇌 코드와 관측 변환의 분리는 fMRI 관측만으로 완전하지 않을 수 있다. 내용 등가성도 선택한 측정 기준에 한정된다.

**근거:** P001, P015, P051, P100.

## R3-08-C01-02 — 수정

**가장 강한 반론:** 사건의 실제 전체 길이로 현재 진행률을 정의하면 아직 보지 않은 종료시점이 입력에 들어간다. 이 이득은 사건 단계의 온라인 신경표상을 지지하지 않을 수 있다.

**여덟 체크:**

1. 사건 분절·시간척도는 P066/P068이 더 가까운 선행이다. 현재 P056의 topology 근거만으로 직접 신규성을 판단하기 어렵다.
2. 단순 time-warp 성능 비교를 넘어 미래 정보 없는 event-state와 고정 시간창의 경쟁이면 신경 질문이 된다.
3. 전체 BOLD 이득과 독립 정서 대비를 구분한 점은 적절하다. 주석 지연이 단계 정렬과 함께 최적화되면 정서 대비가 과장될 수 있다.
4. 독립 경계·onset/offset·native TR·평정 지연·길이 다양성이 필요하며 마지막 경계가 예측 가능한지도 중요하다.
5. 정규화 진행률=(t−onset)/duration은 종료시점을 사용한다. HRF 보정만으로 그 미래정보 이용을 신경의 온라인 상태 계산과 같게 만들 수 없다.
6. 사후 궤적 정렬의 기술적 대응과 현재시점에 뇌가 계산 가능한 상태를 분리해야 한다.
7. 과거만의 사건 landmark, 훈련자료 기반 예상 duration, actual-end를 쓰는 oracle 단계의 세 대조를 추가한다.
8. oracle 단계에서만 성공하면 사후 사건 정렬의 유용성이지 온라인 사건 단계 계산의 증거가 아니다. 고정시간과 동등하면 단순 설명을 유지한다.

**필수 수정:**

- 주장을 사후 사건좌표의 기술적 충분성 대 온라인 진행상태 계산으로 나누고 후자를 별도 후보로 제한한다.
- native 시간에서 과거전용 landmark/예상길이와 실제 끝점을 아는 oracle를 분리한다.
- P066 사건분절과 P068 다중 시간특징을 직접 가까운 선행으로 추가하고 효과가 일반 사건 대조를 넘는지 확인한다.

**더 강한 판별 대조:** 다른 길이의 held-out 영화에서 fixed-time, prefix-only expected progress, actual-duration oracle를 같은 자유도로 비교한다. 경계/길이/HRF null에서 oracle만 좋아지는지 확인하고 정서 대비의 추가 이득을 별도 검정한다.

**음성 결과의 가치:** 사후 시간 정렬과 신경적 시간 계산의 차이를 직접 드러낸다. 온라인 정보 없이 얻은 성능을 기제 증거에서 제외할 수 있다.

**남은 불일치:** 실제 관객이 종료시점을 예측할 수 있었는지는 현재 메타데이터만으로 알 수 없다. 예상길이 모형의 적합성은 별도 평가가 필요하다.

**근거:** P002, P066, P068, P028.

## R3-08-C01-03 — 수정

**가장 강한 반론:** 같은 평균의 다른 평정 분포는 자극의 다중 의미뿐 아니라 척도 사용과 평정 지연의 혼합일 수 있다. 코호트 평균 신경거리는 그 원인을 식별하지 못한다.

**여덟 체크:**

1. 분포/충분통계 및 측정오차 개념은 선행이다. 외부 평정 분포가 독립 신경거리에 추가하는 정보가 남은 질문이다.
2. 분포 추정 QC만 개선되면 방법후보다. 평균·유효평정자수를 맞춘 독립 신경 대비가 필요하다.
3. 평정 분포의 정보는 정서 주석 관련 자극 설명이다. 외부 평정자의 이질성이 한 fMRI 참가자 뇌에 부호화된다고 읽으면 과장이다.
4. 개별 원평정·척도·평정자 identity·시간 지연·시점별 결측과 샘플수가 필요하다. 44명이라는 전체 규모가 모든 시점 44개 독립값을 뜻하지 않는다.
5. bounded 척도의 평균-분산 결합, 평정자별 scale, 사건 반응 지연이 혼합분포처럼 보일 수 있다.
6. 독립 코호트의 측정 관계를 개인 뇌의 다중 해석 또는 내적 상태로 바꾸지 않는 경계는 필수이다.
7. ordinal 계층 척도·평정자 지연만으로 만든 null, 평균/분산 일치 고차형태 대조, 영화 단위 holdout을 추가한다.
8. 분포 구조가 rater split에서 재현돼도 신경 이득이 없으면 평균의 충분성을 해당 범위에서 지지한다. 재현성이 없으면 측정설계 한계이다.

**필수 수정:**

- 평정 분포를 정서 다중성 코드가 아니라 외부 주석 분포와 연관된 신경 정보로 명명한다.
- 연속 평정에서는 평정자별 지연 및 ordinal/유계 척도 모형을 독립 개발자료에서 추정한다.
- 독립단위를 평정자와 영화/자극으로 구분하고 시간점·RDM쌍을 독립 표본처럼 세지 않는다.

**더 강한 판별 대조:** 동일 평균·유효 표본수·척도·지연 모형으로 생성한 평정 분포와 실제 rater-split 재현 분포를 비교한다. 고차형태를 시험할 때 평균·분산도 일치시키고 held-out 영화의 신경거리 추가예측을 검정한다.

**음성 결과의 가치:** 신경효과의 부재와 주석분포의 비신뢰성을 분리하여 consensus가 언제 충분한지 제한한다.

**남은 불일치:** 분포 이득이 남아도 미측정 사건 모호성·시각 내용이 원인일 수 있다. 이를 특정한 정서 계산으로 확정할 수 없다.

**근거:** P002, P051, P055, P100.

## R3-08-C01-04 — 보류

**가장 강한 반론:** GW 결합만으로 새 자극의 대응을 자동 예측할 수 없다. 신경 anchor와 inductive extension이 없으면 test geometry를 다시 써서 외부검증인 것처럼 되는 위험이 있다.

**여덟 체크:**

1. P057의 관계 정렬·대칭 비유일성은 선행이다. 독립 anchor와 실제 신경 대비의 이중 외적 검증이 남는다.
2. 낮은 GW 비용만이면 정렬 benchmark다. 외부 정서 관계와 신경 대비까지 운반하는 주장은 개념적으로 구별된다.
3. 현재 독립 신경 anchor의 실재가 없으므로 공통 정서 신경코드의 주검정은 아직 실행불가 조건이다. 개념 연구는 계속할 수 있다.
4. 양쪽 데이터의 실제 대응 신경 대비, ontology, 독립 bridge, 신뢰도, out-of-sample map 정의가 필요하다.
5. 감각 공통기하와 거리대칭뿐 아니라 촬영 프로토콜·HRF·정규화가 데이터셋 차이를 지배할 수 있다.
6. 같은 관계 예측은 공통 관측기하이지 같은 신경 알고리즘 또는 인과 기전이 아니다.
7. 고정 training coupling에서 새로운 자극으로 가는 inductive extension과 의미-only anchor 대 brain+meaning anchor를 분리한다.
8. anchor가 없으면 신경 코드 가설의 음성 결과도 판정할 수 없다. 유효 anchor에서 결합별 반전이면 대응 비식별을 보여준다.

**필수 수정:**

- 당장 유지할 산출물을 기하 비유일성의 방법후보로 분리하고 공통 신경코드 주장은 bridge 계획의 조건부 discovery track에 둔다.
- train 관계에서 test 자극으로 가는 입력 feature·거리 계산·mapping 규칙을 명시하고 test 신경기하를 최적화에 재투입하지 않는다.
- 새 공통 평정만 얻었을 때와 양쪽 뇌 측정까지 얻었을 때 가능한 주장을 구분한다.

**더 강한 판별 대조:** 훈련 bridge만으로 mapping을 고정하고 별도 bridge의 의미 관계와 실제 신경 대비를 두 단계로 검증한다. 유사한 GW 비용의 의미 순열 결합이 어느 단계에서 실패하는지 검사한다. bridge 부재 시 성공 주장은 기하 수준으로 제한한다.

**음성 결과의 가치:** 의미 대응 실패와 신경 대응 실패를 나누며 공통 모양이 공통 코드가 되는 충분조건을 구체화한다.

**남은 불일치:** 보류는 데이터 소유 여부 때문이 아니라 핵심 neural estimand를 측정할 anchor와 예측경로가 아직 특정되지 않았기 때문이다. 문헌·설계 발전은 계속 가능하다.

**근거:** P001, P002, P057, P055.

## R3-08-C01-05 — 수정

**가장 강한 반론:** 일반 선형 좌표변환은 Euclidean 거리·각도를 바꾼다. 따라서 참가자별 선형 좌표보정과 관계 자체의 변형은 현재 정의에서는 겹치며 두 설명이 식별되지 않는다.

**여덟 체크:**

1. 개인차·hyperalignment·shared/private는 선행 범위다. P015/P060만으로 이 문제의 새로움을 확정할 수 없다.
2. 개인화 성능 대신 좌표동치와 관계변형을 구분하려는 목표는 유효하지만 허용변환 정의가 먼저 필요하다.
3. 정서 관련 독립 대비를 요구한 점은 적절하다. 전체 RDM 상호작용 신뢰도와 정서 대비 관련 신뢰도를 따로 추정해야 한다.
4. 참가자×자극 공통 coverage·독립 반복·run별 신호·개인 HRF·noise covariance·자극 집계 주석 출처가 필요하다.
5. 이질적 voxel 신뢰도·정렬·gain만으로 Euclidean RDM이 변할 수 있다. 내용별 시각 민감도 역시 정서 대비와 얽힌다.
6. 참가자별 관계 변화는 개인 정서 경험 또는 인과 신경코드의 증거가 아니다. 원 후보 경계는 대체로 적절하다.
7. 직교/등방 gain과 일반 선형변환의 비교군을 분리하고 독립 noise-whitened crossvalidated distance를 추가한다.
8. 지정한 동치군 내에서 개인화가 충분하면 더 복잡한 관계변형의 필요성을 줄인다. 5명 내 반복결론을 모집단 부재로 확대하지 않는다.

**필수 수정:**

- 좌표보정의 허용변환군을 직교회전+공통 scale 등으로 먼저 제한하거나 metric을 변환과 함께 정의한다.
- 일반 선형 gain/whitening은 별도 중간 모형으로 두고 구조적 관계변형과 동일시하지 않는다.
- 개인별 신뢰도와 noise-whitening을 독립 반복에서 추정하고 within-participant 결과와 참가자 모집단 추론을 분리한다.

**더 강한 판별 대조:** 같은 저차원 신호에서 직교+등방gain, 일반 선형 관측변환, 자극의존 비선형 관계변형을 nested 비교한다. 각각 독립 반복의 crossvalidated distance와 새 자극의 정서 대비를 예측하게 하여 어느 단계가 필수인지 검정한다.

**음성 결과의 가치:** 공통 코드의 어떤 동치정의가 유지되는지 배운다. 선형 관측변환이 충분하면 개인별 코드 변형의 강한 해석을 철회한다.

**남은 불일치:** 일반 관측변환과 잠재 코드 변화의 식별은 허용모형에 의존한다. 참가자가 적어 모집단 일반화에는 제한이 남는다.

**근거:** P001, P015, P051, P060, P100.

## 근거와 실행 한계

- 배정된 실제 Round2 보고서 2개 역할의 전체 10후보에 대한 비판이다. 대상 파일을 수정하지 않았다.
- 기존 canonical catalog 범위의 선행 역대조이며 새 외부 검색·원문 재열람·원자료 분석을 실행하지 않았다. 모든 비판·수정안은 E3 방법론 추론이다.
- 보유 5종의 소유 사실과 실행 스키마를 구별한다. 스키마 미확인 때문에 문헌 연구 전체를 중단하지 않는다. C01-04의 강한 신경코드 판정만 측정 anchor 명시 전 보류했다.
- 비유의성을 동등성·부재의 증거로 쓰지 않는다. 사전 최소효과·독립 신뢰도·검정력 없으면 판정불가를 허용한다.
- 생성 경로·기능연결·latent 편집의 결과를 인간 뇌 인과로 해석하지 않는다.

## canonical 근거 링크

- P001: [The neural representation of visually evoked emotion is high-dimensional, categorical, and distributed across transmodal brain regions](https://raw.githubusercontent.com/OpenNeuroDatasets/ds002425/3f94b2bf9a75ddb62637c529d30dc40dd4ab5ba1/dataset_description.json). 본문: 아니오; 프록시 403; Discussion: 아니오; 근거: E2
- P002: [Emo-FilM: A multimodal dataset for affective neuroscience using naturalistic stimuli](https://raw.githubusercontent.com/OpenNeuroDatasets/ds004892/cdf68fe448ad180a476fa2371473a1a6ed063774/dataset_description.json). 본문: 아니오; 프록시 403; Discussion: 아니오; 근거: E2
- P015: [MindEye2: Shared-Subject Models Enable fMRI-To-Image With 1 Hour of Data](https://github.com/MedARC-AI/MindEyeV2). 본문: 아니오; 공식 코드/README만 직접 확인; Discussion: 아니오; 근거: E2
- P028: [Brain-Mamba: Encoding Brain Activity via Selective State Space Models](https://proceedings.mlr.press/v248/behrouz24a.html). 본문: 예; 출판사 PDF 전체; Discussion: 예; Conclusion p242 및 Appendix E pp249–250; 근거: E1(논문 본문·부록 직접 확인)
- P051: [Similarity of Neural Network Representations Revisited](https://proceedings.mlr.press/v97/kornblith19a.html). 본문: 예; 공식 PDF 직접 열람; Discussion: 예; 결론/한계 해당 절 직접 확인; 근거: E1(본문); 정서·뇌 전이는 E3
- P053: [Challenging Common Assumptions in the Unsupervised Learning of Disentangled Representations](https://proceedings.mlr.press/v97/locatello19a.html). 본문: 예; 공식 PDF 직접 열람; Discussion: 예; 결론/한계 해당 절 직접 확인; 근거: E1(본문); 정서·뇌 전이는 E3
- P055: [Variational Autoencoders and Nonlinear ICA: A Unifying Framework](https://proceedings.mlr.press/v108/khemakhem20a.html). 본문: 예; 공식 PDF 직접 열람; Discussion: 예; 결론/한계 해당 절 직접 확인; 근거: E1(본문); 정서·뇌 전이는 E3
- P057: [Gromov-Wasserstein Averaging of Kernel and Distance Matrices](https://proceedings.mlr.press/v48/peyre16.html). 본문: 예; 공식 PDF 직접 열람; Discussion: 예; 결론/한계 해당 절 직접 확인; 근거: E1(본문); 정서·뇌 전이는 E3
- P060: [A Python Toolbox for Representational Similarity Analysis](https://github.com/rsagroup/rsatoolbox). 본문: 아니오; E1은 공식 코드·문서만; Discussion: 아니오; 근거: E1(공식 코드/문서만); E2(서지); E3(전이)
- P066: [Discovering event structure in continuous narrative perception and memory](https://github.com/brainiak/brainiak/blob/master/src/brainiak/eventseg/event.py). 본문: 아니오; 공식 문서/코드만 확인; Discussion: 아니오; 근거: E1-공식 코드 및 tutorial; 논문 본문·Discussion 미확인
- P067: [Brain network dynamics are hierarchically organized in time](https://github.com/OHBA-analysis/HMM-MAR). 본문: 아니오; 공식 문서/코드만 확인; Discussion: 아니오; 근거: E1-공식 코드/문서 범위; 논문 본문·Discussion 미확인
- P068: [Neurophysiological signatures of cortical micro-architecture](https://github.com/netneurolab/shafiei_megdynamics). 본문: 아니오; 공식 문서/코드만 확인; Discussion: 아니오; 근거: E1-공식 코드/문서; 논문 본문·Discussion 미확인
- P070: [Prompt-to-Prompt Image Editing with Cross-Attention Control](https://raw.githubusercontent.com/prompt-to-prompt/prompt-to-prompt.github.io/main/ptp_files/Prompt-to-Prompt_preprint.pdf). 본문: 예: 공식 PDF 확보·§1/§3/§4/§5 관련 부분 직접 열람; 전체 정독 아님; Discussion: 예: §5 Limitations p.9; §4 평가 논의 p.9; 근거: E1
- P076: [Diffusion Posterior Sampling for General Noisy Inverse Problems](https://github.com/DPS2022/diffusion-posterior-sampling). 본문: 아니오: 논문 본문 미열람; Discussion: 아니오; 근거: E1
- P077: [Deep Adaptive Design: Amortizing Sequential Bayesian Experimental Design](https://proceedings.mlr.press/v139/foster21a.html). 본문: 예: 공식 PDF 확보; §2–4/§7 직접 열람; Discussion: 예: §7 Discussion 및 Limitations and Future Work p.9; 근거: E1
- P078: [FlowEdit: Inversion-Free Text-Based Editing Using Pre-Trained Flow Models](https://github.com/fallenshock/FlowEdit). 본문: 아니오: 논문 본문 미열람; Discussion: 아니오; 근거: E1
- P098: [WILDS: A Benchmark of in-the-Wild Distribution Shifts](https://proceedings.mlr.press/v139/koh21a.html). 본문: 예: PDF 저장; 검토 절은 source_location 참조; Discussion: 예: §7 PDF p.9; 근거: E1
- P099: [In Search of Lost Domain Generalization](https://github.com/facebookresearch/DomainBed). 본문: 아니오; Discussion: 아니오; 근거: E1
- P100: [Statistical inference on representational geometries](https://elifesciences.org/articles/82566). 본문: 예: 공식 XML 저장·본문 검토; Discussion: 예: Discussion s3-1–s3-6; 근거: E1
- P102: [Conditional independence testing based on a nearest-neighbor estimator of conditional mutual information](https://proceedings.mlr.press/v84/runge18a.html). 본문: 예: PDF 저장; §1–2 및 §5 검토; Discussion: 예: §5 Conclusion PDF p.8; 근거: E1
