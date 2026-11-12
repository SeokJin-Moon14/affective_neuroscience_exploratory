# Agent 11 Round 3 상호 비판

2026-11-12. 배정된 Agent12·04 후보 10개를 모두 검토했다. 유지 1개, 수정 9개. 이는 계획 수준의 E3 비판이며 새 실험·원문 검증을 수행하지 않았다.

공통 판단은 관측적으로 같은 예측을 내는 재매개화·개인 관측 map·비선형 용량 차이를 실제 신경 계산 차이로 읽지 않는 것이다. 미확인 스키마는 분석 조건으로 유지한다.

## R3-11-C12-01 · 수정

대상: 12_adversarial_review / C12-01

1. **선행 답과 남은 문제:** P007/P009는 공통·특이 표상의 공존을 다룬다. 제한된 맥락 변환의 새 환경 전이는 남은 후보이나 공통 계산의 실재가 입증되는 것은 아니다.

2. **모델 교체 여부:** 조건부 변환이 사전 제약 없는 추가 decoder이면 모델 복잡도 비교에 머문다. 변환군이 만드는 새로운 예측을 명시해야 한다.

3. **독립 정서 대비:** 독립 정서 대비가 명시되어 적절하다. 동일 표적의 예측으로만 공통 연산과 다른 좌표를 구분할 수 있는지는 별도 문제다.

4. **미확인 필드의 역할:** 환경×정서 공통 지지구간·자극군·반복이 필요하다. 미확인 시 새 환경 조합 실험으로 이어가며 개념을 중단할 이유는 아니다.

5. **자극·의미·HRF 대안:** 내용 환경을 정하는 특징이 의미 target의 대리변수일 수 있다. 보류 환경의 의미 외삽 난도와 SNR을 함께 맞춰야 한다.

6. **주장 수준:** 공통 readout 뒤의 변환은 동일 예측을 내는 여러 재매개화가 가능하다. 신경 알고리즘의 공통성으로 확대하면 수준 혼동이다.

7. **강한 baseline:** 기존 비구조적 decoder 대조에 더해, 미관측 맥락 조합에서 변환 합성 규칙을 예측하는 검정을 추가한다.

8. **부정 결과의 의미:** 변환 이득이 없으면 고정 코드의 관측 충분성을 제한적으로 지지한다. 변환 실패만으로 공통 계산 부재를 선언하지 않는다.

**가장 강한 반론:** T(context) 뒤 공통 readout은 관측 수준에서 context-dependent decoder와 동등할 수 있다. 단일 출력 예측만으로 좌표 변화와 연산 공유의 고유 분해는 식별되지 않는다.

**필수 수정:**

- 주장을 제한된 변환군으로 표현 가능한 공통 예측 규칙으로 낮춘다.

- 변환 차원·정규화·가능한 합성 규칙을 훈련 전 고정하고 다중 독립 정서 대비를 동시에 예측한다.

- 환경별 독립 모델은 미관측 환경에 적용할 수 없으므로 train-domain 대조와 OOD 주평가를 분리한다.

**더 판별적인 검정:** 두 훈련 맥락의 요소를 새 조합으로 제시했을 때 사전 정의된 변환 합성이 예측하는 다중 대비를 검정한다. 단순 조건부 decoder와 같은 예측만 내면 공통 계산 해석을 내리지 않는다.

**부정 결과의 가치:** 상황별 좌표 변환의 필요성과 그 예측 범위를 제한한다. 동등성 CI와 최소효과를 사전 설정한다.

**미해결 의견 차이:** 공통 연산이라는 용어를 예측 규칙의 공유로 허용할지, 실제 신경 연산의 공유로 읽힐 위험 때문에 제거할지가 미해결이다.

**기존 근거:** [P007](https://raw.githubusercontent.com/canlab/Neuroimaging_Pattern_Masks/master/Multivariate_signature_patterns/2018_Kragel_MFC_Generalizability/Kragel_2018_NatNeurosci_MFC_generalizability.pdf), [P009](https://raw.githubusercontent.com/canlab/Neuroimaging_Pattern_Masks/master/Multivariate_signature_patterns/2021_Ceko_MPA2_multiaversive/Ceko_2022_NatNeurosci_MPA2_negative_affect.pdf), [P049](https://arxiv.org/abs/1907.02893), [P100](https://elifesciences.org/articles/82566), [P053](https://proceedings.mlr.press/v97/locatello19a.html)

## R3-11-C12-02 · 수정

대상: 12_adversarial_review / C12-02

1. **선행 답과 남은 문제:** P008의 시각 schema 및 P050의 정보 guide는 출발점이다. 정서 대비에 필요한 모델 정보의 범위가 남은 문제다.

2. **모델 교체 여부:** 보존·억제·복원의 대칭 비교가 있어 단순 모델 교체는 아니다. 다만 회귀 성능 변화만 남으면 표현 진단이다.

3. **독립 정서 대비:** total/conditional 및 비정서 대비를 구별한 점은 적절하다. 대비와 정보량 매칭을 test로 정하면 순환한다.

4. **미확인 필드의 역할:** 관계·맥락과 정서가 교차하는 지지구간, guide 검증용 외부 라벨이 필요하다. 없으면 모델 내 정보 요구조건으로 범위를 낮춘다.

5. **자극·의미·HRF 대안:** guide가 목표 개념의 선형 접근성만 줄이고 비선형 정보를 남기거나, 의미 전체를 손상할 수 있다.

6. **주장 수준:** 표현 삭제 후 회복은 모델 readout 의존성을 보이며 인간의 구성적 입력 또는 매개를 직접 식별하지 못한다.

7. **강한 baseline:** 다중 probe·held-out 재구성·등에너지 무작위 삭제 및 frozen readout과 재학습 readout을 교차한다.

8. **부정 결과의 의미:** 억제 효과 소멸은 지정 guide로 특정 정보 필요성을 입증하지 못했다는 결과다. 뇌에서 그 맥락이 불필요하다는 뜻은 아니다.

**가장 강한 반론:** 삭제-복원으로 예측이 회복되는 현상은 해당 representation/readout의 사용 정보에 관한 결과다. 자연 자극의 상관을 그대로 둔 채 confound와 인간 뇌의 계산 입력을 구별했다고 할 수 없다.

**필수 수정:**

- 관측적 주장을 모델 정보 요구조건과 조건부 연관으로 한정한다.

- guide의 삭제 성공을 선형 probe 하나로 판단하지 말고 독립 nonlinear probe와 관련 없는 정보 보존을 함께 확인한다.

- 신경 계산 입력의 필요성은 별도의 교차 맥락 자극 실측이 필요한 강한 가지로 분리한다.

**더 판별적인 검정:** 동일 frozen decoder에서 의미 guide와 matched random guide의 삭제·복원을 비교하고, 이어 decoder 재학습에서 회복되는지를 확인한다. 회복되면 정보 삭제보다 좌표 접근성 변화로 해석한다.

**부정 결과의 가치:** 정서 대비가 어떤 조건화 집합·모델 읽기 방식에 견고한지 규정하며, 순수 정서 잔차의 주장을 제한한다.

**미해결 의견 차이:** 내용이 신경 대비를 운반한다는 관측적 표현은 유지 가능하나 매개·계산 입력의 인과적 표현은 별도 자료 없이는 허용하지 않는 입장이다.

**기존 근거:** [P008](https://raw.githubusercontent.com/canlab/Neuroimaging_Pattern_Masks/master/Multivariate_signature_patterns/2019_Kragel_Emotion_Schemas/Kragel_2019_SciAdv_emotion_schemas.pdf), [P050](https://arxiv.org/abs/2606.05107), [P102](https://proceedings.mlr.press/v84/runge18a.html), [P100](https://elifesciences.org/articles/82566)

## R3-11-C12-03 · 유지

대상: 12_adversarial_review / C12-03

1. **선행 답과 남은 문제:** 현재내용과 전이상태 원리는 P013/P048에 있으나 기존 관측 등가를 깨는 독립 정서 대비는 아직 제안이다.

2. **모델 교체 여부:** 모델 순위 대신 예측 불일치 자극을 선택하므로 단순 교체보다 강하다. Agent06 이력 후보와 합칠 수 있는 판별 설계다.

3. **독립 정서 대비:** 정서 관련 대비가 없으면 일반 사건 연구로 내리는 조건이 명료하다.

4. **미확인 필드의 역할:** 동일 현재내용/상이 이력 쌍, timing·독립 주석이 필요하며 없으면 새 제시 실험으로 발전 가능하다.

5. **자극·의미·HRF 대안:** 과거가 다르면 현재 BOLD에 HRF 잔류가 남는다. FIR 통제 실패만으로 잠재 상태가 신경 계산이라고 확정하지 않는다.

6. **주장 수준:** 신규 자극 실측과 모델-only 선택을 구별해 수준은 대체로 적절하다. 양방향 모델의 정보 접근은 주 비교와 다르다.

7. **강한 baseline:** 과거 에너지·사건 빈도는 맞추고 순서만 바꾼 counterbalance, 서로 다른 지연 간격, 완전한 과거 자극 FIR을 추가한다.

8. **부정 결과의 의미:** 정밀한 대비에서 계속 동등하면 해당 자극·관측 해상도의 식별 한계를 학습한다. 상태 계산의 일반적 부재가 아니다.

**가장 강한 반론:** 현재 장면이 같아도 다른 과거의 BOLD 잔류가 달라진다. 따라서 신경 대비가 생기는 사실만으로 과거 상태 계산을 선택할 수 없다.

**필수 수정:**

- prefix-only 주비교와 미래 접근 양방향 진단 대조를 분리하여 같은 정보 예산이라는 표현을 정정한다.

- 주 추정량을 명시적 자극 이력+HRF baseline을 넘어서는 보류 신경 대비로 고정한다.

- 동일 이력 에너지의 순서 반전과 지연을 교차하여 단순 잔류와 상태 예측이 다른 부호/크기를 내는 구간을 사전 선택한다.

**더 판별적인 검정:** 발견 fold에서 동등성 후보를 선정하고, 모델들이 방향이 다른 예측을 내는 별도 자극을 counterbalanced 순서·간격으로 실측한다. 선택에 쓴 neural data는 평가에 재사용하지 않는다.

**부정 결과의 가치:** 비판적 실험의 장점이 커 유지한다. 상태 우위가 없으면 더 단순한 내용+관측필터 설명의 충분 범위를 제시할 수 있다.

**미해결 의견 차이:** 독립 RQ로 별도 집계할지 기존 이력 질문의 실험 설계로 통합할지는 Coordinator의 중복 판정에 남긴다.

**기존 근거:** [P013](https://raw.githubusercontent.com/facebookresearch/vjepa2/main/README.md), [P048](https://arxiv.org/abs/2301.04104), [P053](https://proceedings.mlr.press/v97/locatello19a.html), [P100](https://elifesciences.org/articles/82566), [P089](https://github.com/coxlab/prednet)

## R3-11-C12-04 · 수정

대상: 12_adversarial_review / C12-04

1. **선행 답과 남은 문제:** P097/P100/P101의 선택 편향·표현 추론이 상당 부분 이미 답한 방법 문제다.

2. **모델 교체 여부:** 현 상태는 평가 모듈이다. 제안자도 독립 신경 RQ의 신규성 미확정을 인정하므로 방향 수를 늘리는 용도로 쓰지 않는다.

3. **독립 정서 대비:** state-dependent 정서 대비가 있으나 무엇이 반대 예측인지 C12-03 또는 C04-01에서 빌려와야 한다.

4. **미확인 필드의 역할:** 모든 탐색 이력·동일 목표대조 checkpoint·test 대비가 필요하다. 없는 부분은 frozen 관찰 비교로 표시하면 된다.

5. **자극·의미·HRF 대안:** 선택 통제는 입력 자료·의미·HRF 혼동을 제거하지 않는다. 목표만 다른 비교와 같은 관측창이 별도로 필요하다.

6. **주장 수준:** nested CV 통과를 계산 원리의 인과 우위로 해석하지 않는 경계가 적절하다.

7. **강한 baseline:** 동일 backbone에서 목표만 바꾼 대조와 rank/probe 포화곡선을 추가하고 탐색예산을 동일하게 맞춘다.

8. **부정 결과의 의미:** 선택 후 차이 소멸은 기존 우위의 강건성 실패이며 정보 등가성의 증거는 아니다.

**가장 강한 반론:** 선택 자유도를 통제하는 것은 모든 과학 후보에 필요한 평가 절차이며 그 자체로 정서 신경 계산의 독립 가설이 아니다.

**필수 수정:**

- 독립 과학후보 집계에서 분리하여 C12-03/C04-01의 평가 모듈로 연결한다.

- 통과 기준은 선택 후 효과 지속과 사전 정의된 경쟁 계산 대비를 동시에 만족하도록 한다.

- 탐색 후보 수뿐 아니라 총 학습/선택 예산과 test 재사용 여부를 기록한다.

**더 판별적인 검정:** 동일 구조의 목표함수 대조에서 특정 이력 대비의 예측 차이가 고정 probe·nested probe 양쪽에 남는지 검사한다. 구조가 다르면 원리 효과가 아닌 모델군 차이로 제한한다.

**부정 결과의 가치:** 어떤 모델 우위가 선택 과정에 취약한지와 주장의 신뢰도를 제공하는 방법론적 가치가 있다.

**미해결 의견 차이:** 신경과학 RQ 수에서는 제외하되 필수 방법 모듈로 유지하는 것이 권고다.

**기존 근거:** [P097](https://jmlr.org/papers/v11/cawley10a.html), [P100](https://elifesciences.org/articles/82566), [P101](https://github.com/rsagroup/rsaModelComparison), [P013](https://raw.githubusercontent.com/facebookresearch/vjepa2/main/README.md), [P045](https://arxiv.org/abs/2203.12602)

## R3-11-C12-05 · 수정

대상: 12_adversarial_review / C12-05

1. **선행 답과 남은 문제:** P007/P009의 공통·특이 공존은 선행 결과이고, 정렬로 삭제한 반복 가능한 정서 대비의 평가가 남는다.

2. **모델 교체 여부:** C04-04와 관측 대상·정렬 조작·잔차 추정·새 자극 반증이 크게 겹친다. ceiling 보고만 다른 별도 질문으로 세기 어렵다.

3. **독립 정서 대비:** 정서 대비 없는 잔차를 일반 신경 고유성으로 낮추는 조건은 적절하다.

4. **미확인 필드의 역할:** 내용군×참가자×독립 반복의 교차 구조와 실제 주석 단위가 필요하다. 일부 셀이 없으면 가능한 일반화 축만 유지한다.

5. **자극·의미·HRF 대안:** 반복 가능한 잔차는 안정된 등록 오차·개인별 감각 tuning·자극 ID일 수 있다. 반복성만으로 특이 정서 코드는 아니다.

6. **주장 수준:** 공유 ceiling과 개인 ceiling을 직접 비교하지 않는 점은 좋다. 공통 latent 밖이라는 말은 선택한 alignment family에 상대적이다.

7. **강한 baseline:** 공통 latent+개인 affine 관측모형, 내용군별 readout, 정렬 family 변화 및 nested 잔차 회수를 추가한다.

8. **부정 결과의 의미:** 신뢰도 충분한 잔차의 정서 대비 부재는 이 자료의 정서적 필요성을 제한한다. 신뢰도 부족은 미결정이다.

**가장 강한 반론:** 같은 잠재 계산에 개인/내용군별 관측 혼합이 붙어도 안정된 잔차가 생긴다. 또한 C04-04와 거의 같은 실험으로 두 RQ를 세는 중복 위험이 크다.

**필수 수정:**

- C04-04와 합치거나 이 후보를 내용군 특이성×개인 특이성의 교차 분해로 명시적으로 좁힌다.

- 공통 신경 계산의 다른 관측 좌표와 새로운 정보 성분을 경쟁 모형으로 둔다.

- 공통/개인 ceiling의 추정 대상과 고유 정보의 일반화 모집단을 별도 표로 고정한다.

**더 판별적인 검정:** 훈련 내용군·참가자에서 정의한 잔차를 같은 사람/새 내용, 새 사람/같은 내용, 둘 다 새 조건으로 구분 평가한다. 동일 shared latent에 개인 affine map을 붙인 대조로 충분하면 새로운 private 계산이라 부르지 않는다.

**부정 결과의 가치:** 정렬의 정보 손실이 내용군·개인·관측 좌표 중 어느 축에 관련되는지 제한할 수 있다.

**미해결 의견 차이:** 내용군 교차 조건이 없으면 C04-04와 통합해야 한다는 권고이며, 신뢰도 추정법 차이만으로 별도 RQ를 유지하는 데 반대한다.

**기존 근거:** [P009](https://raw.githubusercontent.com/canlab/Neuroimaging_Pattern_Masks/master/Multivariate_signature_patterns/2021_Ceko_MPA2_multiaversive/Ceko_2022_NatNeurosci_MPA2_negative_affect.pdf), [P007](https://raw.githubusercontent.com/canlab/Neuroimaging_Pattern_Masks/master/Multivariate_signature_patterns/2018_Kragel_MFC_Generalizability/Kragel_2018_NatNeurosci_MFC_generalizability.pdf), [P100](https://elifesciences.org/articles/82566), [P060](https://github.com/rsagroup/rsatoolbox), [P053](https://proceedings.mlr.press/v97/locatello19a.html)

## R3-11-C04-01 · 수정

대상: 04_brain_foundation / C04-01

1. **선행 답과 남은 문제:** P025/P026/P029의 신경 표현 목표와 P051의 표현 비교는 선행이다. 목표×정서 대비 접근성 교호작용이 새 후보다.

2. **모델 교체 여부:** 동일 encoder ablation과 이중 표적 대비가 실현되면 단순 benchmark 교체를 넘는다.

3. **독립 정서 대비:** 독립 A 대비가 명료하지만 raw Y와 Z의 유한 probe 성능 차이는 정보량 자체의 차이가 아니다.

4. **미확인 필드의 역할:** 독립 반복·A 신뢰도·같은 입력/목표 구현이 필요하다. beta-only이면 정적 압축 모형으로 유효한 가지를 유지한다.

5. **자극·의미·HRF 대안:** 입력 신경 공간·분산 규모·SNR·의미 baseline 누락이 선택적 손실처럼 보일 수 있다. 분산을 whitening한 대조가 유용하다.

6. **주장 수준:** 표현 접근성과 실제 정보 소실을 구별하는 조건은 있으나 제목의 압축과 소실 주장을 더 좁혀야 한다.

7. **강한 baseline:** 동일 rank·복원오차 곡선·probe capacity 곡선 및 알려진 저분산 신호 주입 복구 대조를 추가한다.

8. **부정 결과의 의미:** 유연한 probe로 회복되면 접근성 재배치, 회복 불가라도 지정 검정의 한계이며 정보 부재를 확정하지 않는다.

**가장 강한 반론:** raw와 latent의 예측 차이는 유한 표본·readout·정보 좌표의 접근성 차이일 수 있다. 목적함수가 신경 정보를 소실했다는 강한 결론은 같은 관측만으로 성립하지 않는다.

**필수 수정:**

- 일차 주장과 제목을 재현 신호의 선택적 접근성으로 명시한다.

- 동일 objective 내 압축량/복원량의 Pareto 곡선을 비교하여 차원·전체 복원 수준을 분리한다.

- A와 무관하게 주입한 검출가능 신호로 분석이 알려진 선택적 손실을 회수하는지 보정한다.

**더 판별적인 검정:** 같은 encoder·학습 입력에서 목표×rank를 교차하고 독립 A 대비와 일치 분산의 비정서 대비를 측정한다. 선형/비선형 probe 포화곡선 전체에서 상반된 선택성을 보일 때만 해당 모형군의 선택적 병목을 논한다.

**부정 결과의 가치:** 정보 소실이 아닌 좌표 접근성 효과였는지를 배울 수 있고 단순 압축으로 충분한 범위를 제시한다.

**미해결 의견 차이:** 실용적인 접근성 결과도 과학적 가치가 있지만 소실이라는 용어와 구분해야 한다.

**기존 근거:** [P026](https://github.com/MedARC-AI/CortexMAE), [P029](https://github.com/Eric-LRL/Brain-JEPA), [P051](https://proceedings.mlr.press/v97/kornblith19a.html), [P083](https://raw.githubusercontent.com/mlresearch/v119/gh-pages/koh20a/koh20a.pdf)

## R3-11-C04-02 · 수정

대상: 04_brain_foundation / C04-02

1. **선행 답과 남은 문제:** 자극 encoding과 masked brain prediction은 이미 존재한다. 두 조건부 정보집합의 불일치가 남은 비교다.

2. **모델 교체 여부:** 입력원 비교와 의미 강화 곡선은 단순 모델 교체보다 강하나 brain 입력의 추가 정보량 자체가 이득을 보장할 수 있다.

3. **독립 정서 대비:** A 관련 잔차를 명시했으나 trial/run 공통 잡음과 자극 주석이 결합하면 거짓 정서 추가분이 생긴다.

4. **미확인 필드의 역할:** 공통 mask·시간정렬·target 배제 범위·독립 반복이 필요하다. 연속 자료가 없으면 별도 시행/공간 블록의 제한된 정적 비교를 설계한다.

5. **자극·의미·HRF 대안:** 넓은 마스크로도 자극 이력·run 공통변동·비선형 smoothing이 남는다. 개인 평균화만 보정해서 해결되지 않는다.

6. **주장 수준:** 관측 N의 추가 예측은 지정한 자극 모형 S에 대한 조건부 연관이다. 뇌 고유 상태 또는 S에 원리적으로 없는 정보라고 부르면 과장이다.

7. **강한 baseline:** 같은 반복 N→Y와 독립 반복 N→Y의 비교, 공유 자극 효과·global/run nuisance 분해를 추가한다.

8. **부정 결과의 의미:** 효과 소멸은 추가 신경 문맥의 필요성 한계이며 모든 자극 모형의 완전성 증명이 아니다.

**가장 강한 반론:** S가 제한된 자극 모형이고 N이 실제 신경 관측인 이상, N의 추가 예측은 누락 자극 정보와 공통 측정 변동으로도 생긴다. 같은 관측의 조건부 비교만으로 그 기원을 고유하게 식별할 수 없다.

**필수 수정:**

- 주장을 특정 S와 관측 조건에서 N이 가진 재현 가능한 추가 정보로 제한한다.

- 한 반복의 N이 다른 반복의 동일 자극 Y를 예측하는 비교와 같은 반복 비교를 분리한다.

- 마스크·개인 보정·의미 확장에 따른 효과 감소를 하나의 선택된 결과 대신 전체 민감도 곡선으로 보고한다.

**더 판별적인 검정:** 동일 자극의 반복 a에서 N을 얻어 반복 b의 Y를 예측하고, 다른 자극/같은 run의 N 대조와 비교한다. 반복 간 전달되어도 자극 미모형화와 내부 상태는 추가 자극/상태 조작 없이는 구별 불가임을 남긴다.

**부정 결과의 가치:** 뇌 문맥을 추가해야 실용적으로 회수되는 안정된 정보와 같은 반복의 공통 잡음을 분리할 수 있다.

**미해결 의견 차이:** 신경조건부 추가 정보라는 상대적 주장은 허용하되 자극과 독립인 계산이라는 해석에는 동의하지 않는다.

**기존 근거:** [P026](https://github.com/MedARC-AI/CortexMAE), [P027](https://github.com/facebookresearch/tribev2), [P029](https://github.com/Eric-LRL/Brain-JEPA), [P053](https://proceedings.mlr.press/v97/locatello19a.html)

## R3-11-C04-03 · 수정

대상: 04_brain_foundation / C04-03

1. **선행 답과 남은 문제:** P026의 공간 표현 variant와 일반 압축 비교가 선행이다. parcel 내부에서 상쇄되는 정서 대비는 직접 시험할 수 있다.

2. **모델 교체 여부:** 같은 Y에 집계 연산만 바꾸는 설계라 모델 교체와 구별된다. atlas 우열만 보고하면 benchmark로 낮아진다.

3. **독립 정서 대비:** 정서 대비와 전체 복원을 병행한 점은 좋다. 비정서 대비의 공간 주파수·신뢰도도 맞춰야 선택성을 말할 수 있다.

4. **미확인 필드의 역할:** dense–parcel 대응·등록·반복이 필요하다. 없는 variant checkpoint를 기다리기보다 동일 Y의 선형 집계 대조로 진행 가능하다.

5. **자극·의미·HRF 대안:** rank/SNR만 같아도 공간 주파수 통과대역이 다를 수 있어 atlas 특이 효과처럼 보인다.

6. **주장 수준:** 압축 차이는 관측 표현의 정보 접근성이다. 지역 간 신경 계산이나 해부학적 기능 경계의 실재를 직접 입증하지 않는다.

7. **강한 baseline:** parcel 평균의 null space인 parcel 내부 zero-mean 잔차를 직접 복구하고 spatial-frequency-matched 대조와 비교한다.

8. **부정 결과의 의미:** random parcel에서도 같은 손실이면 atlas 특이성은 줄지만 공간 평균의 일반적 상쇄 효과까지 기각되지는 않는다.

**가장 강한 반론:** 원 반증문에서 random parcel도 같은 손실이면 atlas 특이성을 기각하는 것은 맞지만, 그것은 평균화 일반의 대비 상쇄 가설을 기각하지 않는다. 두 가설을 분리해야 한다.

**필수 수정:**

- atlas 경계의 특이성 대 공간 평균의 일반적 null-space 손실을 별도 가설로 둔다.

- parcel 평균에 직교하는 잔차를 훈련 fold에서 정해 held-out 대비의 추가 설명을 측정한다.

- 동일 차원뿐 아니라 공간 거리·통과 주파수·신뢰도 기준을 train에서만 맞춘다.

**더 판별적인 검정:** 같은 Y에서 parcel mean, mean+within-parcel zero-mean component, spatial-spectrum-matched random aggregation을 비교한다. 잔차가 회수하는 대비가 비정서 신뢰도 일치 대비보다 선택적인지 평가한다.

**부정 결과의 가치:** 경계 선택 문제인지 모든 평균화가 제거하는 미세 대비인지 구별할 수 있다.

**미해결 의견 차이:** 신경표상의 공간 충분 통계라는 표현은 관측·대조 가족에 상대적이어야 하며 뇌의 실제 압축 연산으로 읽지 않는다.

**기존 근거:** [P026](https://github.com/MedARC-AI/CortexMAE), [P051](https://proceedings.mlr.press/v97/kornblith19a.html), [P060](https://github.com/rsagroup/rsatoolbox)

## R3-11-C04-04 · 수정

대상: 04_brain_foundation / C04-04

1. **선행 답과 남은 문제:** 개인화 encoding과 공통 표현의 한계가 선행이다. 정렬 강도×독립 정서 대비의 선택적 손실이 추가 후보다.

2. **모델 교체 여부:** C12-05와 주요 관측·조작·반증이 중복한다. 이 후보는 개인별 관측 혼합 대 새로운 tuning으로 특화하는 것이 타당하다.

3. **독립 정서 대비:** 집계 A를 개인 정서 경험으로 읽지 않는 구분이 정확하다. 개인별 neural tuning으로 제한을 유지한다.

4. **미확인 필드의 역할:** 개인별 반복·새 자극/세션·training-only alignment가 필요하다. 확인 전에도 교차 조건 설계는 계속 가능하다.

5. **자극·의미·HRF 대안:** 안정된 해부학적 혼합·감각 tuning·global scale만으로 개인 잔차가 새 자극에 전이할 수 있다.

6. **주장 수준:** 개인 head의 이득이 새로운 개인별 계산의 증거는 아니다. 공통 latent를 다른 좌표로 관찰한 경우도 포함한다.

7. **강한 baseline:** 공통 latent+개인 선형/affine 관측 map 대 동일 rank의 개인 추가 latent를 비교한다.

8. **부정 결과의 의미:** 추가 latent가 불필요하면 공통 계산+개인 관측 map의 충분 범위를 지지하나 개인 정보 부재를 보편화하지 않는다.

**가장 강한 반론:** 공통 latent가 개인별로 다른 선형 혼합을 거치면 평균 예측의 잔차는 안정적이며 개인 head가 회수한다. 이는 private 계산이 아니라 같은 정보의 관측 좌표 차이일 수 있다.

**필수 수정:**

- 개인별 공통정보 readout과 개인별 추가정보 latent를 다른 모형으로 둔다.

- 정렬 강도가 증가하며 낮아지는 A 대비가 단순 gain/rotation인지 검증한다.

- C12-05는 내용군 교차로 특화하거나 본 후보의 신뢰도 평가 모듈로 병합한다.

**더 판별적인 검정:** 공통 latent+개인 affine map과 공통+개인 추가 latent를 같은 parameter/rank 예산에서 새 자극·세션에 평가한다. 추가 latent의 독립 A 대비가 남아야 관측 map 이상의 필요성을 말한다.

**부정 결과의 가치:** 개인별 적응이 추가 정보 때문인지 관측 좌표 보정 때문인지 구별한다.

**미해결 의견 차이:** 반복 가능한 개인 tuning은 가치 있지만 새로운 개인 특이 계산이라는 명명에는 관측 map 대조가 필수다.

**기존 근거:** [P027](https://github.com/facebookresearch/tribev2), [P052](https://proceedings.mlr.press/v235/huh24a.html), [P053](https://proceedings.mlr.press/v97/locatello19a.html), [P060](https://github.com/rsagroup/rsatoolbox)

## R3-11-C04-05 · 수정

대상: 04_brain_foundation / C04-05

1. **선행 답과 남은 문제:** P034의 selective SSM과 P028의 뇌 과제 적용은 선행이다. 격자×관측필터를 넘어선 정서 대비가 남은 질문이다.

2. **모델 교체 여부:** 관측격자와 선택 계산을 교차하므로 단순 Mamba 교체를 넘을 수 있다. 새 구현은 Brain-Mamba 재현으로 부르지 않아야 한다.

3. **독립 정서 대비:** 시간 A가 없으면 방법 검증으로 내리는 경계가 적절하다. 주 추정량은 전체 BOLD 개선과 별개로 고정한다.

4. **미확인 필드의 역할:** native TR·시간원점·연속 신호·과거 전용 전처리가 필요하다. beta 시행순서를 연속 신호로 대신하지 않는다.

5. **자극·의미·HRF 대안:** 선택적 SSM과 fixed SSM의 차이는 상태 선택뿐 아니라 입력 의존 비선형 표현력 차이다. HRF 민감도만으로 이를 제거할 수 없다.

6. **주장 수준:** 견고한 이득도 뇌가 input-dependent gate를 쓴다는 증거는 아니다. 선택한 관측 예측 함수군의 필요성으로 한정한다.

7. **강한 baseline:** 동일 nonlinear input/output map을 공유하는 fixed SSM·비선형 AR·gated 관측만 있고 state는 fixed인 대조를 추가한다.

8. **부정 결과의 의미:** 격자에 민감하면 관측 artefact 설명을 강화한다. 모든 강한 대조와 같으면 해당 자료의 선택 상태 필요성을 제한한다.

**가장 강한 반론:** linear/fixed SSM 대 selective SSM 비교는 상태 유지의 선택성과 일반적인 비선형 용량을 혼동한다. 관측격자에 견고하다는 사실만으로 이 차이가 신경 상태 선택이라는 결론은 나오지 않는다.

**필수 수정:**

- 입력/출력 비선형성을 일치시키고 고정 전이+입력 gate와 선택 전이를 구분한다.

- 실시간 문맥 길이·훈련 목표·표본수·정규화를 통일하고 미래 전처리 누수를 별도로 감사한다.

- 일차 주장을 관측상 유용한 이력 함수군의 판별로 제한한다.

**더 판별적인 검정:** 고정 전이+비선형 입력/관측, 고정 전이+입력 gate, 입력 의존 전이의 세 모델을 동일 상태차원에서 비교한다. 동일 내용량/스펙트럼의 이력 순서 대조에서 사전 지정 정서 대비 예측이 갈리는지 본다.

**부정 결과의 가치:** 어떤 시간 함수족이 관측 자료에 필요한지와 관측필터만으로 충분한지를 배운다. 신경 시간상수를 모델 step에서 읽지 않는다.

**미해결 의견 차이:** 선택 상태 계산이라는 표현을 모델 수준에서 유지하는 데 동의하지만 인간 신경 gate의 필요성으로 일반화하는 데 반대한다.

**기존 근거:** [P026](https://github.com/MedARC-AI/CortexMAE), [P028](https://proceedings.mlr.press/v248/behrouz24a.html), [P034](https://github.com/state-spaces/mamba), [P086](https://github.com/HuthLab/encoding-model-scaling-laws), [P090](https://github.com/dicarlolab/CORnet)

## 라운드 한계

- 10개 후보의 계획을 비판했으며 원자료·checkpoint·모델 실험을 실행하지 않았다.

- 원문을 신규 재열람하지 않았다. canonical 출처는 대상 보고의 기존 검증 수준이며 원문/공식 코드 확인을 새로 수행한 것으로 집계하지 않는다.

- 모든 반론은 E3 방법론 추론이다. 논문 저자의 발언 또는 이미 실증된 반례로 귀속하지 않는다.

- 스키마 미확인은 후보별 구현 조건과 축소 경로로 기록했으며 전체 연구 종료 이유로 사용하지 않았다.

- C12-04는 평가 모듈로 분리 권고; C12-05와 C04-04는 교차조건을 달리하지 않으면 통합 권고.

- e-prop와 EmoPathway의 미확인 상태를 변경하지 않았다. 공유 파일·Git·타 역할 파일은 수정하지 않았다.

## 실제 읽기 기록

- discussions/ROUND03_PROTOCOL.md

- discussions/round03_assignments.json

- agents/11_brain_inspired/round02_exchange.json

- agents/11_brain_inspired/round02_exchange.md

- agents/12_adversarial_review/round02_exchange.json

- agents/12_adversarial_review/round02_exchange.md

- agents/04_brain_foundation/round02_exchange.json

- agents/04_brain_foundation/round02_exchange.md

- axis_map/reference_catalog.csv
