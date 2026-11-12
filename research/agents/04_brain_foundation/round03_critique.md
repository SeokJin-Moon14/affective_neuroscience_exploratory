# Agent04 Round3: 멀티모달·생성 연구 후보 비판

2026-11-12. 대상 Agent05·Agent09의 후보 10개를 실제 검토했다. 수정 8개, 보류 2개. 모든 수정안은 E3이며 실측 결과가 아니다.

## C05-01 — 수정

**가장 강한 반론:** 고유 경로 추가 이득은 공유 경로를 인위적으로 좁힌 결과와 구별되지 않는다. gate×content 실험을 한꺼번에 하면 조작의 원인도 불명확해진다.

**여덟 필수 검사**

1. **선행이 답한 부분과 남은 부분:** P037의 원 문제는 multi-view redundancy를 넘는 표현 학습이다. 어떤 private 경로가 정서 신경 대비에 필요한지는 미해결이지만, 분해의 고유성은 확보되지 않았다.
2. **단순 모델·benchmark 교체 여부:** 같은 입력의 경로 필요성 검정이면 모델 교체를 넘는다. 서로 다른 checkpoint의 S와 Vp/Ap를 단순 비교하면 입력·훈련목적 차이가 된다.
3. **독립 정서 대비 여부:** 전체 ΔR²와 정서 대비를 구별한다고 적었으나 대비의 고정 방법이 없다. 독립 주석 A의 contrast와 held-out neural target을 학습 전에 명시해야 한다.
4. **실제 필요한 자료·지원 조건:** 재생된 실제 음원, 비음성 구간, 자극 내용군·반복·독립 A, FactorCL의 타깃 감독 사용 여부와 정확한 추출 출력을 확인해야 한다.
5. **자극·motion·의미·HRF 대안:** private는 잔여 의미·SNR와 강하게 공변할 수 있다. 차원 일치만으로 공유 표현의 underfitting이나 조건부 비선형 정보를 배제하지 못한다.
6. **추론 수준 혼동:** gate를 뇌 회로로 읽지 않는 제한은 타당하다. 모델 경로 제거의 실패를 생물학적 경로 필요성으로 확대해서는 안 된다.
7. **더 강한 기준과 대조:** 전체 unimodal 특징으로 동일 용량의 충분히 유연한 additive/interaction readout을 적합하고 공유 병목 크기를 연속 변경하는 대조가 필요하다.
8. **부정적 결과의 의미:** private의 증분이 공유 병목 확대로 사라지면 분해 이전에 버린 내용의 회수이며 별도 신경 통로의 필요성은 지지되지 않는다.

**필수 수정**

- 1차 분석은 gate를 고정한 S 대 S+Vp+Ap에 한정하고, shared rank/정규화 강도를 훈련 fold에서 matched effective capacity로 조정한다.
- FactorCL에 A 또는 신경 표적이 쓰이면 전체 feature 학습을 외부 split 안으로 옮긴다. 현재 공개 구현의 타깃 사용이 미확인이므로 unsupervised라고 전제하지 않는다.
- A로 신경 대비를 정의하는 단계와 그 대비를 평가하는 자극·반복을 분리하고 S의 개념 누락을 독립 사건 probe로 검사한다.

**판별력이 더 큰 대조:** 같은 원 시청각 특징에서 shared bottleneck 크기×private 포함을 교차한다. private 이득이 작은 병목에서만 생기면 병목 손실 설명, 큰 병목에서도 재현되고 내용·품질 대조를 넘으면 검토한 공유 표현의 불충분성을 지지한다. gate 비교는 그 이후 별도 2×2 실험으로 둔다.

**부정 결과의 가치:** 공유 표현의 충분한 용량이 모든 증분을 설명하면 저비용 공유 readout을 지지하며 생물학적 고유정보 부재까지 주장하지 않는다.

**모델 지원과 계산 범위:** ImageBind의 1024차원 공통 출력은 FactorCL private 출력이 아니다. temporal gate는 V-MoE의 확인된 기본 기능으로 취급하지 않는다. 고정 특징을 한 번 캐시하고 3개 병목 크기×private 유무의 작은 readout부터 수행; 전체 인코더 재학습은 별도 비용·가중치 가용성 확인 뒤 진행한다.

**자기 후보와 구별:** C04-01의 목표함수 조작과 달리 C05-01은 모달리티 경로의 충분성 조작이다. 단순 정보보존 probe만 남으면 공통 방법 카드를 공유한다.

**남은 이견:** private latent를 무엇과 구별할지 아직 비유일하다. 공유 표현의 충분성이 확보되지 않으면 신경 고유 통로 주장에는 동의할 수 없다.

근거: P035, P037, P093, P053, P083. 기존 canonical 검증 기록의 범위에서 사용.

## C05-02 — 수정

**가장 강한 반론:** La와 Lv는 readout 창만 제어한다. 원 인코더의 숨은 시간창과 HRF가 포함된 전체 유효 필터를 분리하지 않으면 뇌의 모달리티별 기억 길이를 식별하지 못한다.

**여덟 필수 검사**

1. **선행이 답한 부분과 남은 부분:** P038/P043은 멀티모달 융합과 영상 이해를 다루며 신경 통합창의 식별을 보장하지 않는다. 기존 시간창 연구와 차별점은 La×Lv 비대칭 대비다.
2. **단순 모델·benchmark 교체 여부:** 작은 causal readout의 창 조작은 질문 중심 설계다. 서로 다른 encoder별 최적창을 비교하는 것으로 바꾸면 benchmark가 된다.
3. **독립 정서 대비 여부:** 총 BOLD 이득과 A 대비를 분리한 점은 타당하다. 창 선택에 A 대비를 쓰고 같은 자료에서 이를 검정하지 않도록 이중 선택을 분리해야 한다.
4. **실제 필요한 자료·지원 조건:** feature endpoint/stride/receptive field, TR와 실제 음향 동기, A의 별도 코호트·평정 지연·영화 수가 필요하다.
5. **자극·motion·의미·HRF 대안:** HRF 외에 영상/오디오 pretrained receptive field가 이미 서로 다르고 feature autocorrelation이 La/Lv를 결정할 수 있다.
6. **추론 수준 혼동:** 과거 전용 후처리를 해도 양방향 full-clip encoder의 feature 자체에 미래가 들어 있으면 causal 조건이 아니다.
7. **더 강한 기준과 대조:** 동일 실시간 길이로 잘라 각각 endpoint를 t에 둔 feature를 다시 추출하고, 모달리티별 flexible FIR와 matched spectrum 대조를 포함한다.
8. **부정적 결과의 의미:** 이득이 인코더 receptive field를 맞춘 뒤 소실되면 신경 기억 비대칭보다 관측 표현의 시간평활화 차이가 설명한다.

**필수 수정**

- 각 특징의 허용 입력 범위를 초 단위로 기록하고 endpoint t 이후 프레임/오디오가 전처리·인코더·정규화 어디에도 없도록 감사한다.
- 주장 수준을 우선 모달리티별 과거 가용정보의 예측 충분성으로 제한한다. 신경 통합시간 수치 추정은 합성 복구에서 HRF×encoder filter×창을 구별할 때만 시도한다.
- 창 후보·HRF 후보를 소수로 사전 고정하고 영화 외부 평가에서 비대칭 이득을 계산한다.

**판별력이 더 큰 대조:** known unequal encoder filters+equal latent memory와 equal encoder filters+unequal latent memory를 각각 넣은 모의 관측에서 같은 절차가 두 경우를 구별하는지 확인한다. 구별이 안 되면 관측적 창 충분성 대비만 유지하고 신경 시간상수 주장을 삭제한다.

**부정 결과의 가치:** 시각/오디오의 겉보기 시간 비대칭이 관측 필터만으로 생기는 조건을 제시한다. null 결과가 두 모달리티의 실제 뇌 통합시간 동일성을 증명하지는 않는다.

**모델 지원과 계산 범위:** VideoMamba의 bimamba 기본 설정과 MBT의 clip 특징은 원형 그대로 online 상태가 아니다. 시작은 endpoint가 명시된 고정 특징+3×3 창 grid로 제한하고 각 창별 대형 모델 재학습은 하지 않는다. 초 단위 창과 TR당 index를 구별한다.

**자기 후보와 구별:** C04-05와 관측격자 통제는 공유하되 이 후보는 모달리티별 창 비대칭, C04-05는 selective/fixed 상태 계산의 필요성이다.

**남은 이견:** 공통 HRF 후보집합만으로 모달리티별 HRF 차이나 encoder filter 차이를 통제할 수 있다는 부분에는 추가 식별 검증이 필요하다.

근거: P038, P043, P002, P026, P086. 기존 canonical 검증 기록의 범위에서 사용.

## C05-03 — 수정

**가장 강한 반론:** 모델 상태를 영으로 만드는 조작은 훈련 분포 밖 충격이며 경계의 존재를 알려주는 추가 입력이기도 하다. 현재 비교는 기억 소거와 경계 단서 전달을 완전히 분리하지 못한다.

**여덟 필수 검사**

1. **선행이 답한 부분과 남은 부분:** P089의 상태/오차 출력은 reset 조작 도구를 제공하지만 인간 정서 전이의 경계 reset 필요성은 답하지 않는다. 사건 분할 선행의 포괄적 역검색은 남아 있다.
2. **단순 모델·benchmark 교체 여부:** 동일 모형의 reset 위치를 바꾸므로 모델 교체가 아니다. 다만 reset의 OOD 충격과 경계 신호의 단순 제공을 구별해야 한다.
3. **독립 정서 대비 여부:** 경계 전후 패턴 변화 자체는 정서 대비가 아니다. 독립 A transition을 정의하고 감각 경계 변화와 분리해야 한다.
4. **실제 필요한 자료·지원 조건:** 독립 경계·컷·run/clip 경계·연속 A lag와 유효 경계 간격, encoder와 state의 정확한 초기화 동작이 필요하다.
5. **자극·motion·의미·HRF 대안:** 실제 경계는 컷·의미 변화·놀라운 사건과 겹친다. 무작위 reset의 횟수만 맞춰서는 state가 받는 예상오차 크기를 맞추지 못한다.
6. **추론 수준 혼동:** 모델 reset을 뇌 인과개입과 구분한 점은 적절하다. reset 우위는 뇌가 상태를 영으로 초기화한다는 증거가 아니다.
7. **더 강한 기준과 대조:** boundary indicator를 readout에만 제공한 never-reset, soft forget, norm/age/예상오차 맞춤 random-reset을 추가한다.
8. **부정적 결과의 의미:** boundary indicator만으로 충분하면 과거 소거가 아니라 경계 단서 encoding이 설명한다. hard reset 실패도 모든 사건 갱신 기제의 반증은 아니다.

**필수 수정**

- reset/never 조건에 동일 boundary indicator를 제공하고 고정 hard reset, 학습된 initial state, 연속값 forget gate를 별도 명시한다.
- reset-aware 학습과 test-time-only reset을 분리하여 OOD 충격 설명을 검사한다.
- A transition과 경계 위치의 지연 선택은 개발 영화에서만 정하고 boundary×A contrast를 외부 영화에서 평가한다.

**판별력이 더 큰 대조:** 경계 신호 제공 여부×state forgetting 여부의 2×2를 같은 readout·HRF로 비교한다. 경계 신호만으로 설명되는 부분을 뺀 후 사건 위치의 forgetting이 norm/age-matched 임의 위치보다 우월한지 검정한다.

**부정 결과의 가치:** 과거 소거가 불필요하면 사건 경계를 별도 표상하는 단순 모형을 지지한다. 모든 조작에 효과가 없으면 데이터 해상도에서 경계 기반 계산을 구별하지 못한 것으로 제한한다.

**모델 지원과 계산 범위:** PredNet의 R/E 출력과 reset 구현은 별도 확인 대상이고, VideoPrism은 기본적으로 frozen clip encoder이지 reset 가능한 recurrent state가 아니다. 작은 causal state head를 명시적 신규 모형으로 구현; 네 초기화 조건으로 우선 제한한다.

**자기 후보와 구별:** C04-05의 선택적 상태 대비와 연관되지만 boundary location×forgetting의 추가 판별이 있다. Agent11의 같은 reset 후보와는 최종 RQ 병합을 권고한다.

**남은 이견:** 영화 특징의 boundary reset과 뇌의 기억 초기화를 대응시키는 정도가 남은 논점이다. 관측 예측의 최소 필요 연산으로만 합의 가능하다.

근거: P089, P044, P002, P034. 기존 canonical 검증 기록의 범위에서 사용.

## C05-04 — 보류

**가장 강한 반론:** 핵심 조작인 사건 단계 좌표가 정서 신경자료와 독립적으로 유효한지 아직 입증되지 않았다. 자연 사건군 대응이 성립하지 않으면 결과가 나와도 단계 가설을 반증할 수 없다.

**여덟 필수 검사**

1. **선행이 답한 부분과 남은 부분:** P042의 cycle 대응은 같은 행동의 phase correspondence 도구다. 서로 다른 자연 영화의 의미 사건이 같은 latent 진행을 공유한다는 근거는 아직 없다.
2. **단순 모델·benchmark 교체 여부:** 사건 좌표의 외부 예측이면 benchmark를 넘지만 사건군 대응이 없으면 TCC를 새 자료에 적용한 정렬 실험만 남는다.
3. **독립 정서 대비 여부:** 원시간에서 A 관련 neural contrast를 평가하는 점은 적절하다. clip-level A만 있는 자료로 연속 정서 전이를 검증할 수 없다.
4. **실제 필요한 자료·지원 조건:** 서로 다른 duration에서 의미적으로 대응하는 단계, 그 단계의 독립 주석·정확한 시작/끝·연속 A와 BOLD가 필요하다.
5. **자극·motion·의미·HRF 대안:** 내용군 분리만으로 duration과 사건 복잡도·컷 수가 분리되지 않는다. 사건군 안에서도 유효한 단계 대응과 duration overlap을 확인해야 한다.
6. **추론 수준 혼동:** 자연 duration 변이를 속도 조작의 인과효과로 읽지 않는 제한은 타당하다. 학습된 phase를 인간 사건 단계로 자동 명명할 수 없다.
7. **더 강한 기준과 대조:** held-out human event landmarks를 사용한 alignment 정확도와 위치-only null을 먼저 비교한다. event-identity-only와 duration-matched baseline도 필요하다.
8. **부정적 결과의 의미:** TCC가 독립 landmarks를 예측하지 못하면 부정 결과는 신경 phase 가설이 아니라 phase 측정 실패를 뜻한다.

**필수 수정**

- 현재 후보를 discovery track에 유지하되 신경 파일럿 착수는 독립 landmark 일반화 게이트 이후로 둔다. 스키마 미확인 자체가 아니라 측정 구인의 대응 부재가 보류 이유다.
- 단계 추출기를 자극만으로 학습하고, 별도 영상의 인간 landmark를 예측하는지 위치-only/normalized-time/DTW와 비교한다.
- duration×event family의 overlap이 부족하면 관찰 자료의 phase 질문으로는 식별불가라고 명시하고 필요한 새 matched 사건 자료를 설계한다.

**판별력이 더 큰 대조:** 동일 사건군 안에서 지속시간만 다른 쌍과 지속시간은 같지만 단계 구성이 다른 쌍을 독립 주석으로 구성한다. 알려진 HRF를 거친 합성 전이의 복구와 실제 held-out landmark 검증을 모두 통과한 좌표만 neural readout에 사용한다.

**부정 결과의 가치:** 단계 좌표의 검증 실패는 TCC가 해당 자연 사건의 의미 진행을 측정하지 못한다는 방법론적 경계를 알려준다. neural phase 가설의 기각과 분리한다.

**모델 지원과 계산 범위:** TCC 모델과 AVE event localization 출력은 서로 다른 의미의 단계다. AVE의 Bi-LSTM 출력을 과거 전용 진행 상태로 쓰지 않는다. 처음에는 소수 사건군의 고정 특징+DTW/normalized-time으로 게이트를 평가하고 TCC 재학습은 그 이후에만 한다.

**자기 후보와 구별:** C04-05는 동일 물리시간의 관측격자를 바꾼다. C05-04는 별도 사건 좌표를 도입하므로 대응 타당성이라는 추가 식별 조건이 있다.

**남은 이견:** 보류는 아이디어 기각이 아니다. 사건군 대응의 유효성을 영상 자체의 cycle loss로 대신할 수 있는지에 동의하지 않는다.

근거: P042, P041, P002, P051. 기존 canonical 검증 기록의 범위에서 사용.

## C05-05 — 수정

**가장 강한 반론:** joint와 additive의 차이를 다른 사전학습 목적·가중치에서 얻으면 결합 연산과 표현 품질이 혼동된다. congruence 조건의 겹침도 없는 경우 단순 모델 비교로 해결되지 않는다.

**여덟 필수 검사**

1. **선행이 답한 부분과 남은 부분:** P036/P038의 joint representation 이득은 시청각 표현학습 성과이며 신경적 비가산성을 입증하지 않는다. 기존 congruence 연구와 가까워 역검색이 중요하다.
2. **단순 모델·benchmark 교체 여부:** 일치도×joint-additive 상호작용이면 benchmark를 넘는다. 서로 다른 encoder 가중치·목적함수 비교로는 결합 규칙을 분리할 수 없다.
3. **독립 정서 대비 여부:** 정서 대비와 총 BOLD 증분을 병행한 점은 타당하다. 독립 congruence 판정이 A를 사실상 다시 측정하지 않는지 구성 개념을 분리해야 한다.
4. **실제 필요한 자료·지원 조건:** 실제 동시 재생 영상·음악/환경음, 일치/불일치 독립 평정·A·조건별 유효 표본·자극 family overlap이 필요하다.
5. **자극·motion·의미·HRF 대안:** 불일치가 음원 유무·음량·장면 희귀성과 결합되면 조건 상호작용이 추정되지 않는다. nuisance residualization만으로 없는 overlap을 만들 수 없다.
6. **추론 수준 혼동:** PID synergy나 뇌 인과통합을 주장하지 않는 것은 적절하다. joint checkpoint 우위는 여전히 계산 구조의 증명이 아니다.
7. **더 강한 기준과 대조:** 같은 고정 unimodal 특징에 additive nonlinear readout과 interaction readout을 붙여 비교하고, paired correspondence를 보존/파괴한 제어 특징을 병행한다.
8. **부정적 결과의 의미:** 강한 additive가 충분하면 지정한 표현·측정조건에서 cross-modal interaction이 불필요하다는 결론이며 뇌의 모든 통합 부재는 아니다.

**필수 수정**

- 1차 대비를 동일 frozen unimodal feature의 additive 대 interaction readout으로 고정한다. pretrained CAV-MAE/MBT는 외부 검증 또는 secondary 비교로 둔다.
- 일치도를 사건·음원 대응 기준으로 정의하고 정서 주석 평가자/항목과 분리한다. 조건별 low-level·의미 overlap을 사전 확인하고 지원되지 않는 영역에 외삽하지 않는다.
- counterfactual 오디오 교체 특징은 sensitivity 분석이며 원래 BOLD의 관측 조건으로 대체하지 않는다.

**판별력이 더 큰 대조:** 같은 V,A feature에서 f(V)+g(A)와 f(V)+g(A)+h(V,A)를 용량/정규화 일치로 비교한다. held-out 영화에서 정서 neural contrast에 대한 interaction 이득의 congruence 차이를 추정하며 동일 차원의 within-condition paired shuffle을 단순 correspondence 대조로 사용한다.

**부정 결과의 가치:** 학습목적·표현 품질을 고정한 뒤 이득이 없어지면 foundation model 우위와 신경 비가산성을 구별할 근거가 된다.

**모델 지원과 계산 범위:** CAV-MAE의 시각 입력은 frame 기반이며 긴 영화 상태가 아니다. MBT token bottleneck 개수를 신경통합 차원으로 읽지 않는다. 같은 캐시 특징으로 2개 readout을 먼저 비교하고 반복 대형 feature 추출 비용을 피한다.

**자기 후보와 구별:** C04의 정보보존 질문과 달리 핵심 조작은 joint-additive×congruence이다. C05-01과 같은 private/gate ablation만 남으면 둘은 병합해야 한다.

**남은 이견:** 자연 일치도 조건을 충분히 정의할 수 있을지, interaction readout의 유연성 증가와 결합 규칙의 필요성을 어느 정도 구별할지가 남는다.

근거: P036, P038, P041, P093, P053. 기존 canonical 검증 기록의 범위에서 사용.

## C09-01 — 수정

**가장 강한 반론:** 동일 likelihood를 쓴다는 통제는 좋은 출발이지만, 그 likelihood가 개인 fMRI를 충분히 표현하는지와 prior별 guidance가 같은 관측 적합도를 달성하는지가 핵심이다. 공개 평균피질 simulator를 개인 뇌의 likelihood로 바로 사용할 수 없다.

**여덟 필수 검사**

1. **선행이 답한 부분과 남은 부분:** P076은 일반 inverse problem의 근사 posterior sampling이다. fMRI forward likelihood와 정서 대비 calibration은 별도 문제이며 원 논문 기능으로 제공되지 않는다.
2. **단순 모델·benchmark 교체 여부:** 관측 의존성×prior 변화 대비는 단순 생성 성능 비교를 넘는다. guidance 수치만 바꾸면 선택 예산·적합도 차이의 기술 감사에 머무른다.
3. **독립 정서 대비 여부:** 원본 이미지의 A 회복과 신경 contrast 회복을 구별한 점은 타당하다. 생성물의 A-like feature는 사람의 독립 주석 없이는 정서 측정이 아니다.
4. **실제 필요한 자료·지원 조건:** 개인별 반복 BOLD·자극 ID·독립 A·생성 후보 주석·검증 가능한 noise covariance 및 각 prior와 forward model의 정확한 지원 입력이 필요하다.
5. **자극·motion·의미·HRF 대안:** brain shuffle이 자극 의미와 likelihood 적합도를 함께 파괴하므로 양성 차이는 일반 자극 식별만으로도 발생할 수 있다.
6. **추론 수준 혼동:** 기존 관측의 정보 기여 감사로 한정하는 것은 적절하다. generated candidate의 예측 BOLD를 실측처럼 사용할 수 없다.
7. **더 강한 기준과 대조:** 의미/저수준 matched brain swap, 실제 관측 없는 same-stimulus semantic prior, 직접 brain-to-A/feature ridge와 독립 forward 검증을 추가한다.
8. **부정적 결과의 의미:** prior에 민감해도 forward model이 부정확하면 뇌에 A 정보가 없다는 결론은 불가능하다. 반면 calibrated matched swap에서도 동등하면 관측 특이 attribution은 약해진다.

**필수 수정**

- forward mean와 noise covariance를 독립 학습/반복 자료에서 정하고, 생성 최적화에 쓴 forward와 평가용 forward의 model-family/자료를 분리한다.
- 동일 guidance 값 대신 calibration 구간 안의 관측 적합도와 자연성 기준을 맞추어 prior를 비교한다. unconditioned prior와 원 자극 의미로 조건화한 prior를 별도로 명시한다.
- 개인 표적이면 TRIBE 평균 fsaverage5 출력에 개인 보정과 공통 피질 마스크가 필요하며 subcortex나 임의 voxel을 지원한다고 가정하지 않는다.

**판별력이 더 큰 대조:** 관측(실제/의미 matched 타자극/제거)×prior family의 요인 설계에서 같은 후보 수·forward 호출 수·적합도 허용범위를 유지한다. A 관련 neural contrast를 평가하는 데이터와 후보를 골랐던 데이터는 분리한다. 생성기 없이 자연자극 retrieval에서도 관측 의존성이 남는지 비교한다.

**부정 결과의 가치:** 어떤 prior 조건과 forward 정확도에서 정서 attribution이 안정적인지 범위를 제한한다. 직접 ridge와 차이가 없으면 생성기가 과학 질문에 필수인지 재평가한다.

**모델 지원과 계산 범위:** DPS는 pretrained brain decoder가 아니며 필요한 differentiable forward/noise likelihood를 새로 구성해야 한다. 2 prior×3 관측조건에서 같은 N proposal과 forward 호출 budget을 사용하고 실제 peak VRAM/호출시간을 측정한 뒤 N을 정한다. 비용 수치는 아직 미측정이다.

**자기 후보와 구별:** C04-02가 두 입력원의 예측집합을 비교하는 데 비해 C09-01은 관측을 고정하고 prior를 바꾼다. 같은 잔차 probe는 공유 가능하지만 조작은 구별된다.

**남은 이견:** 고정된 부정확 likelihood에 대한 안정성은 측정된 뇌정보의 안정성과 다르다. calibration을 통과한 공통 피질 대비까지 주장하는 데만 동의한다.

근거: P076, P071, P027, P053, P100. 기존 canonical 검증 기록의 범위에서 사용.

## C09-02 — 수정

**가장 강한 반론:** 찾은 후보들의 범위는 탐색된 집합의 범위일 뿐이다. 좁아졌다는 결과로 비식별 가설을 반박하려면 없는 후보가 없다는 보장이 필요한데, 일반 생성 sampler에는 그 보장이 없다.

**여덟 필수 검사**

1. **선행이 답한 부분과 남은 부분:** P053/P055/P057의 비식별성과 P076의 inverse sampling은 근거 원리다. 이들의 정리가 실제 fMRI candidate set의 완전한 식별 구간을 제공하지는 않는다.
2. **단순 모델·benchmark 교체 여부:** 후보 범위를 관측량 증가에 따라 비교하면 점 reconstruction을 넘는다. sampler 출력의 최대/최소만 보고하면 생성 다양성 benchmark가 된다.
3. **독립 정서 대비 여부:** 후보 자극의 정서 범위와 neural A contrast의 범위를 구별해야 한다. 인공 feature 극값은 독립 A의 극값을 보장하지 않는다.
4. **실제 필요한 자료·지원 조건:** 반복별 독립 관측·noise covariance·생성 후보의 인간 A·자연성/의미 판정·검증 forward·허용오차 calibration 자료가 필요하다.
5. **자극·motion·의미·HRF 대안:** 넓은 범위는 실제 관측 비식별성보다 model mismatch 또는 generator가 악용한 forward adversarial direction일 수 있다.
6. **추론 수준 혼동:** 경험적 범위로 제한한 점은 타당하다. 그러나 좁은 탐색 범위를 반증으로 쓰는 것은 탐색 완전성 없이는 비대칭적으로 약하다.
7. **더 강한 기준과 대조:** 넓은 범위를 입증하는 두 실제 후보의 witness pair, 별도 forward family, 반복 수 증가, brute-force 가능한 합성 문제를 병행한다.
8. **부정적 결과의 의미:** 좁은 범위만 찾았다는 결과는 식별 성공의 증거가 약하다. 충분한 독립 관측을 추가해 기존 witness 쌍이 탈락하면 측정 추가의 구별력을 보여준다.

**필수 수정**

- 일차 estimand를 두 calibrated-compatible 후보 사이 독립 A 차이의 존재로 바꾸고 이를 witness evidence로 명명한다. 전체 식별 구간 또는 엄밀 상한은 주장하지 않는다.
- 반증을 탐색 구간 축소가 아니라 추가 독립 반복·vertex/ROI 관측이 사전 확보한 witness pair를 구분하는지로 재정의한다.
- 극값 탐색과 평가 forward를 분리하고 후보를 생성에 쓰지 않은 인간 주석으로 평가한다. 작은 합성 문제에서만 알려진 참 집합과 탐색 coverage를 계산한다.

**판별력이 더 큰 대조:** 기존 관측 절반으로 두 상반된 A 후보를 찾은 뒤 나머지 독립 반복/피질 공간의 held-out likelihood에서 둘의 적합도를 검정한다. 다른 forward family에서도 양립하면 model-conditioned ambiguity의 witness가 되고, 추가 관측에서 갈리면 측정량의 식별 개선을 보여준다.

**부정 결과의 가치:** 후보가 탈락하는 관측 단위를 특정하면 어디에 추가 측정이 유익한지 알려준다. 후보를 못 찾은 것은 비식별성이 없다는 증명으로 집계하지 않는다.

**모델 지원과 계산 범위:** 후보별 모든 ROI의 고차원 likelihood 최적화는 비용이 클 수 있다. train-only reliability mask와 작은 사전정의 contrast로 시작하고, 후보 수/초기값/forward 호출 budget을 sampler마다 동일하게 기록한다. 낮은 정확도의 대체 forward를 과학적 ground truth로 쓰지 않는다.

**자기 후보와 구별:** C09-01과 생성 코드는 공유해도 추정량은 다르다. C09-01은 관측×prior attribution, C09-02는 두 양립 후보의 witness와 새 관측에 따른 탈락이다.

**남은 이견:** 원안의 충분한 탐색 후 좁은 구간을 반증으로 인정하는 기준은 미정이다. witness의 존재와 부재에 서로 다른 증거 강도를 부여해야 한다.

근거: P076, P053, P055, P057, P100. 기존 canonical 검증 기록의 범위에서 사용.

## C09-03 — 수정

**가장 강한 반론:** 의미 보존을 통과한 편집의 효과가 작아지면 내용 훼손 때문인지, 그 필터가 정서 조작 강도까지 줄였기 때문인지 구별되지 않는다. 통과군 조건화는 선택 편향도 만든다.

**여덟 필수 검사**

1. **선행이 답한 부분과 남은 부분:** P070/P078은 편집 구현을 제공한다. 의미 보존한 정서 neural contrast를 입증하지 않으며 inversion 자체의 왜곡이 원문에서 제한으로 제시된다.
2. **단순 모델·benchmark 교체 여부:** 실제 새 자극 반응과 조작 타당성의 연결은 단순 모델 교체가 아니다. 보존 성공률만 평가하면 생성 QC 후보로 남는다.
3. **독립 정서 대비 여부:** 독립 A와 실제 새 BOLD를 요구한 점은 강점이다. 보존 성공/실패 자체는 후처리 선택 변수이므로 두 집단 차이를 목표 조작 효과와 혼동하면 안 된다.
4. **실제 필요한 자료·지원 조건:** 원본 사용권·독립 A/사건 평정·허용 동등성 범위·참가자/원본 family·제시 순서·새 측정·각 편집의 강도·실패 로그가 필요하다.
5. **자극·motion·의미·HRF 대안:** 보존 성공군은 애초 단순하거나 특정 정서 강도의 원본에 치우칠 수 있다. 성공군만 조건화하면 난도와 A가 만드는 선택 편향이 남는다.
6. **추론 수준 혼동:** 실측 자극 조작은 그 자극 대비의 효과를 평가하지만 뇌 회로 기전이나 완전한 정서 단일성분 인과를 입증하지 않는다.
7. **더 강한 기준과 대조:** 원본 family 내 전체 후보의 선택 확률을 보존하고 목표/비목표/무편집을 무작위 제시한다. 성공 여부는 사전 threshold를 가진 moderator로만 평가한다.
8. **부정적 결과의 의미:** 실패군만 효과가 있어도 성공군의 낮은 조작 강도·낮은 신뢰도로 설명될 수 있다. 목표 A 조작 크기의 overlap이 유지될 때 선택적 해석을 반박할 수 있다.

**필수 수정**

- 의미 보존뿐 아니라 목표 A 변화량·자연성·시각 변형량의 공동 overlap을 개발 자료에서 확인한다. 통과군과 실패군의 공통 지지 영역 밖 비교는 하지 않는다.
- 전체 편집 시도와 실패율을 기록하고 원본 family별 목표·비목표·inversion-only 후보를 함께 보존한다. 지침/ROI를 test 효과에 맞추지 않는다.
- 표본별 무작위 제시를 하되 보존 통과 여부 자체를 무작위 처치로 표현하지 않는다. 새 뇌 수집 전 주석 기반 게이트를 통과하도록 한다.

**판별력이 더 큰 대조:** 같은 원본 family에서 A 변화량이 겹치는 보존 통과·실패 후보를 개발 주석으로 고르고 독립 주석 및 신경표본에서 검증한다. 목표 대 비목표 contrast의 보존상태 interaction을 평가하되 inversion-only의 baseline artifact를 차감한다.

**부정 결과의 가치:** 동등한 A 조작에도 보존군 효과가 사라지면 지정한 내용 변수로 설명되는 신경 대비임을 지지한다. overlap 실패는 선택성 주장에 필요한 자극을 아직 만들지 못했다는 결과다.

**모델 지원과 계산 범위:** Prompt-to-Prompt는 실제 이미지에 바로 완전 보존 편집을 보장하지 않으며 inversion 단계가 필요할 수 있다. FlowEdit의 latent 이동량은 matched perceptual edit strength가 아니다. 주석 통과 후보가 확보되기 전에 대규모 신경 실험 예산을 계산하지 말고 generator/seed별 통과율을 먼저 계측한다.

**자기 후보와 구별:** C04는 기존 측정의 표상 충분성이고 이 후보는 새 실측 자극 대비다. 분석 방향은 독립적이며 새 측정 필요성 때문에 단기 기존자료 파일럿과 분리한다.

**남은 이견:** 정서 관련 사건 단서와 보존해야 할 사건 의미의 경계는 이론적으로 완전히 분리되지 않을 수 있다. 보존 차원과 목표 차원을 명시한 제한적 해석만 가능하다.

근거: P070, P071, P078, P051, P100, P102. 기존 canonical 검증 기록의 범위에서 사용.

## C09-04 — 보류

**가장 강한 반론:** 아직 구별할 두 신경 모형과 공통 평가 모집단이 구체화되지 않아 정보 이득의 표적이 불명확하다. DAD를 추가하면 편집·likelihood·정책 세 학습 오차를 동시에 떠안는다.

**여덟 필수 검사**

1. **선행이 답한 부분과 남은 부분:** P077의 DAD는 명시 likelihood와 조건부 독립 관측 등 전제를 갖는다. 불연속 유한 자극 pool·HRF 의존 신경자료에서 그대로 보장되지 않는다.
2. **단순 모델·benchmark 교체 여부:** 정책 성능 자체가 아니라 구체적 경쟁 정서 neural model을 구별할 때 연구 질문이 된다. 현재 감각/의미/정서 기여라는 이름만으로 경쟁 모형이 확정되지 않았다.
3. **독립 정서 대비 여부:** log score 개선은 일반 예측 calibration 향상일 수 있다. 독립 A 관련 두 상반 신경 설명의 판별 목표를 고정해야 한다.
4. **실제 필요한 자료·지원 조건:** 새 BOLD·개인 noise model·경쟁 모형 likelihood·timing/HRF·후보 validity 확률·주석 및 생성 비용·고정 평가 자극이 필요하다.
5. **자극·motion·의미·HRF 대안:** 선택 정책마다 고른 자극 분포가 달라 test log score의 난도도 달라진다. validity-aware 정책이 쉬운 자극만 고르면 이득이 과장될 수 있다.
6. **추론 수준 혼동:** 자기 simulator 점수를 준비 단계로 제한한 것은 타당하다. simulated EIG 향상을 실제 인간 실험의 정보 이득으로 대체할 수 없다.
7. **더 강한 기준과 대조:** 고정된 자연자극 pool의 exact/Monte Carlo EIG와 coverage baseline을 먼저 비교하고 정책과 독립된 공통 test set에서 posterior predictive score를 평가한다.
8. **부정적 결과의 의미:** 단순 coverage와 동등하면 학습 정책의 추가 복잡성이 불필요하다. 모든 정책이 실패하면 경쟁 모형의 관측 구별 가능성 자체를 재검토한다.

**필수 수정**

- 우선 감각/의미 충분 모형 M0와 사전정의 A 관련 상호작용 모형 M1의 실제 likelihood와 경쟁 예측을 명시한다. 이 구별이 관측 연산 후 가능한지 확인한다.
- 첫 구현은 유한 후보 pool의 비학습 Bayesian batch selection으로 축소하고 DAD policy 학습은 반복 설계 비용이 정당화될 때만 추가한다.
- 정책별 선택 데이터로 갱신한 모형을 동일한 독립 고정 test 자극에서 평가한다. 시행수뿐 아니라 후보 생성·주석·계산 및 탈락 자극까지 예산에 포함한다.

**판별력이 더 큰 대조:** 자연 후보 pool에서 validity가 거의 일정한 대조와 생성 후보 pool을 나누어 policy×pool을 비교한다. 같은 M0/M1·관측 noise에서 validity-aware 이득이 생성 pool에 특이적인지, 공통 test에서 구별·calibration을 개선하는지 검정한다.

**부정 결과의 가치:** validity 계층이 도움이 되는 범위와 단순 선택으로 충분한 범위를 분리한다. EIG 모델이 아니라 자극 validity가 병목이었다는 결과도 비용 배분에 유용하다.

**모델 지원과 계산 범위:** 공개 TRIBE는 평균 피질 출력이며 calibrated Bayesian likelihood를 곧바로 제공하지 않는다. DAD의 연속 설계 가정을 유한 이미지 pool에 자동 적용하지 않는다. 작은 pool의 고정 모델 Monte Carlo EIG로 시작하고 이중 posterior 계산 횟수·forward 호출·실측 비용을 기록한다.

**자기 후보와 구별:** C04-02의 두 조건부 모형을 M0/M1 후보로 가져올 수 있으나 입력 가용성과 출력 타깃을 같게 해야 한다. 현재는 구체적 신경 질문의 실험설계 부속 방법으로 두는 것이 낫다.

**남은 이견:** 현재 정보 이득이 모형 index, parameter, 독립 A contrast 중 무엇에 관한 것인지 확정되지 않았다. 정의 전에는 상세 신경 파일럿으로 추천하지 않는다.

근거: P077, P100, P098, P070, P027. 기존 canonical 검증 기록의 범위에서 사용.

## C09-05 — 수정

**가장 강한 반론:** 생성기 두 개의 계보 독립성은 완전 확인하기 어렵다. 한 family에서 다른 family로 전이된다고 공통 artifact를 제거한 보편적 정서 개입이 되는 것은 아니다.

**여덟 필수 검사**

1. **선행이 답한 부분과 남은 부분:** P098/P099는 domain 분리와 model selection의 원리를 제공한다. 생성기 family를 건너는 신경 contrast의 보편성을 보장하지 않는다.
2. **단순 모델·benchmark 교체 여부:** 조작 구현의 family×neural contrast interaction이면 단순 두 모델 benchmark를 넘는다. 서로 다른 평균 품질 비교만 남으면 도구 평가다.
3. **독립 정서 대비 여부:** 전체 BOLD가 아닌 고정 정서 neural contrast를 둔 점은 타당하다. A 조작 크기와 contrast를 개발 family에서 정한 뒤 test에서 조정하지 않아야 한다.
4. **실제 필요한 자료·지원 조건:** 모델 계보·실제 가중치·중복 학습자료의 확인 범위·독립 주석·원본 family·새 BOLD·각 pipeline의 조작 성공률과 신뢰도가 필요하다.
5. **자극·motion·의미·HRF 대안:** 두 family가 같은 latent encoder/text encoder/대규모 학습자료를 공유하면 같은 artifact도 전이할 수 있다. 자연 matched control이 이 공통 결손에 필요하다.
6. **추론 수준 혼동:** family 일반화는 해당 도구 범위의 재현성이지 생성기 전체 모집단이나 뇌 회로의 인과 기제 증거가 아니다.
7. **더 강한 기준과 대조:** 생성 pipeline 2개만이면 fixed-domain replication으로 명명하고 자연 자극의 같은 의미/A contrast를 제3의 관측 대조로 둔다.
8. **부정적 결과의 의미:** 충분한 조작 강도와 신뢰도에서 family interaction이 크면 원래 신경 효과가 도구 의존적이다. 차이 없음은 낮은 검정력과 구별할 equivalence margin이 필요하다.

**필수 수정**

- claim을 확인한 두 pipeline의 조작 재현성으로 제한하고, backbone/text encoder/VAE/학습자료 공개 여부를 각각 기록한다. 여러 seed를 독립 family 표본으로 세지 않는다.
- family별 같은 A 변화량·보존/자연성·시각 변화량의 공통 지지 영역을 개발 주석으로 정의한다. test family 실패 때 prompt를 재조정하면 새 개발 라운드로 분류한다.
- 자연 matched 자극의 고정 대비를 추가하고, family×contrast의 의미 있는 차이 및 동등성 범위를 개발 신뢰도 근거로 사전 고정한다.

**판별력이 더 큰 대조:** 같은 원본 family의 두 생성 pipeline과 자연 matched control에서 목표 대 비목표 contrast를 비교한다. 생성기 artifact classifier 점수와 neural contrast의 관계를 외부 자극에서 평가하되 classifier 실패를 artifact 부재 증명으로 쓰지 않는다. 두 생성기 모두에서만 보이는 효과와 자연 대조까지 유지되는 효과를 구별한다.

**부정 결과의 가치:** 도구 범위에 따른 효과 경계를 명시한다. 교차 pipeline 전이는 있지만 자연 대조에서는 사라지면 공통 생성 artifact 또는 조작 내용 불일치가 남았다는 결과다.

**모델 지원과 계산 범위:** FlowEdit의 SD3/FLUX 구현과 Prompt-to-Prompt의 모델 계보는 method 이름만으로 독립성이 확정되지 않는다. inference GPU·VRAM을 측정 전 추정 숫자로 확정하지 않는다. 먼저 두 pipeline의 동일 후보/주석 budget을 고정하고 성공률·추론비용을 계측한다.

**자기 후보와 구별:** C04-04의 개인 일반화와 검증 단위는 다르다. 참가자/자극/생성 pipeline의 일반화를 분리해 표본 수를 늘려 세지 않는 공통 원칙을 공유한다.

**남은 이견:** 두 pipeline의 결과를 생성기 family 모집단의 random effect로 일반화하는 데는 동의하지 않는다. 확인한 도구의 fixed-domain 비교와 더 넓은 모집단 주장을 분리해야 한다.

근거: P078, P070, P098, P099, P100, P051. 기존 canonical 검증 기록의 범위에서 사용.

## 라운드 한계

- 배정된 두 역할 후보 10개를 JSON 전문 기준으로 실제 검토했다. Markdown은 서두와 검증/한계 절을 대조했으며 별도 원문 신규 검증으로 세지 않는다.
- 판정은 수정 8개·보류 2개다. 보류는 C05-04의 사건 단계 대응 타당성, C09-04의 구별할 신경 모형/estimand가 먼저 구체화되어야 한다는 설계상의 이유이며 자료 스키마 미확인만을 이유로 한 기각이 아니다.
- 모든 계산 비용 계획은 제안이며 GPU/VRAM/실행시간을 측정하지 않았다. 가중치·실제 모델 출력 지원·licensing·로컬 자료 스키마는 후속 실행 조건이다.
- 기존 canonical 문헌 기록과 모델 카드의 확인 범위를 사용했다. 포괄적 신규성 역검색·새 외부 원문 확인·뇌분석·simulator calibration은 수행하지 않았다.
- C09-03/04/05는 새 인간 뇌 측정이 필요하다. 현재 다섯 데이터셋 보유가 그 측정을 대신하지 않는다. 기존 생성물의 예상 BOLD를 실제 관측으로 취급하지 않는다.
- 자기 Round2와 관측대상/조작/추정량을 대조했으며 비슷한 용어만으로 후보를 중복 처리하지 않았다. 공유 파일과 Git은 수정하지 않았다.
