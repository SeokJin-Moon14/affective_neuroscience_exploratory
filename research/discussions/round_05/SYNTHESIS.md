# Round5 실제 대립·후속 응답·최종 판정

서로 다른 역할의 제안자·회의적 비판자·데이터통계 검토자가 Top10에 각각 독립 입장을 작성했다. 30개 입장 파일을 수집한 뒤 제안자가 실제 상대 기록을 읽고 후속 응답을 남겼다. 아래 Coordinator 판정은 다수결 합의가 아니며 조건·철회·해결되지 않은 반론을 보존한다.

최종 감사 후 RP02 등의 응답 문서에는 판정식 정정이 반영됐다. 아래는 현재 수정본이며 초기 세 입장과 별도 감사·수정 로그를 함께 보존한다. 과거에 검토자 모두가 최종 재합의했다고 뜻하지 않는다. [감사와 수정 이력](../../synthesis/FINAL_AUDIT.md).

최초 30개 판단: {'조건부': 20, '수정': 9, '추진': 1}. 실제 후속 응답 항목: 59개. 동일 역할 응답에 여러 비판이 함께 기록될 수 있으므로 응답 항목 수를 독립 과학 주장 수로 해석하지 않는다.

| 제안 | 제안자 / 비판자 / 통계 | Coordinator 판정 |
|---|---|---|
| [RP01](../../proposals/RP01.md) | 03: 조건부 / 12: 수정 / 01: 조건부 | 수정 후 조건부 파일럿 |
| [RP02](../../proposals/RP02.md) | 10: 조건부 / 07: 수정 / 12: 조건부 | 수정 후 조건부 제안 |
| [RP03](../../proposals/RP03.md) | 05: 조건부 / 11: 수정 / 08: 조건부 | 수정 후 조건부 파일럿 |
| [RP04](../../proposals/RP04.md) | 05: 조건부 / 06: 조건부 / 04: 조건부 | 조건부 제안 |
| [RP05](../../proposals/RP05.md) | 04: 조건부 / 10: 수정 / 01: 수정 | 설계 유지·신경 확증 착수 보류 |
| [RP06](../../proposals/RP06.md) | 02: 조건부 / 01: 조건부 / 12: 수정 | 설계·관측 탐색 유지·crossnobis 확증 보류 |
| [RP07](../../proposals/RP07.md) | 09: 조건부 / 03: 수정 / 07: 조건부 | Discovery 유지·첫3파일럿 제외 |
| [RP08](../../proposals/RP08.md) | 04: 추진 / 08: 수정 / 11: 조건부 | 수정 후 조건부 파일럿 |
| [RP09](../../proposals/RP09.md) | 07: 조건부 / 02: 수정 / 08: 조건부 | Discovery 유지·자료 내 교정부터 |
| [RP10](../../proposals/RP10.md) | 09: 조건부 / 06: 조건부 / 10: 조건부 | Discovery 유지·새 주석/신경 측정 조건 |

## RP01. 시각 정렬 목표가 정서 대비의 판독 접근성을 바꾸는 조건

**최종 판정:** 수정 후 조건부 파일럿

동일 입력·작은 encoder·시각표적에서 contrastive 대 회귀를 비교한다. cache/ridge는 접근성·검증 기준이며 목표효과와 분리한다.

**남은 대립:** 유한 readout·학습량의 실패로 정보 소실을 증명할 수 없다. 내용 통제도 정서 특수성의 완전 보장은 아니다.

**실제 제안자의 응답:**

- **검토자 12 회의적비판자 / 수용:** 첫 baseline의 역할을 원뇌/특징 접근성 감사와 동일조건 목표함수 비교로 분리한다. 원뇌→CLIP ridge가 가능하다는 사실은 masked/contrastive 목적의 효과를 검정한 것이 아니다.

  **응답:** PILOT01을 A 접근성 기준·측정검사와 B 동일 encoder의 contrastive 대 regression으로 분리한다. A만 완료하면 목적효과 결론을 보류한다.

  **남은 쟁점:** 실제 데이터·구현 검증은 미실행이며 실행 전 조건으로 남는다.

  [작성 원본](../../agents/03_vision_decoding/round05_rebuttal.json)

- **검토자 12 회의적비판자 / 수용:** 목표함수만 다른 비교에는 같은 자료·입력·구조·dimension·최적화·총 선택예산을 요구한다. 불가능하면 frozen 모델군의 조건부 접근성 비교로 제목과 결론을 좁힌다.

  **응답:** 같은 train-only PCA, D→128→K encoder, 정규화 시각표적, 초기화·batch 순서·optimizer·update budget·탐색 예산을 쌍으로 고정한다. backbone이나 입력을 함께 바꾸는 비교는 별도 확장이다.

  **남은 쟁점:** 실제 데이터·구현 검증은 미실행이며 실행 전 조건으로 남는다.

  [작성 원본](../../agents/03_vision_decoding/round05_rebuttal.json)

- **검토자 12 회의적비판자 / 수용:** 정서 및 난도 일치 비정서 대비를 사전 고정하고 전체 성능저하를 선택적 정서 손실과 구별한다. 난도 매칭은 독립 개발자료에서 한다.

  **응답:** 개발자료에서 인간 정서 대비와 비정서 감각/내용 대비의 원뇌 판독 난도·표본수를 맞춘다. 주 파일럿은 두 대비를 같은 이진 순서 판별 log loss로 평가하고, 공통 지지 부족이면 선택성 상호작용을 보고하지 않는다.

  **남은 쟁점:** 실제 데이터·구현 검증은 미실행이며 실행 전 조건으로 남는다.

  [작성 원본](../../agents/03_vision_decoding/round05_rebuttal.json)

- **검토자 12 회의적비판자 / 수용:** 동일 Gram·정확 가역변환 양성대조와 실제 rank 절단 대조를 추가한다. nonlinear probe의 회복 실패는 정보부재의 증명이 아니다.

  **응답:** 직교회전 뒤 Gram 오차와 등방 ridge 예측의 수치 복구, 조건수 제한 선형변환의 정확 역변환, 알려진 비선형 변환의 정확 역변환을 검사한다. 독립 주입 신호를 지운 rank 절단도 함께 사용한다. 학습 probe의 비회복은 삭제 증명이 아니다.

  **남은 쟁점:** 실제 데이터·구현 검증은 미실행이며 실행 전 조건으로 남는다.

  [작성 원본](../../agents/03_vision_decoding/round05_rebuttal.json)

- **검토자 12 회의적비판자 / 수용:** 정서 타깃의 척도에 맞는 하나의 proper loss를 정하고 총/의미조건부 손실을 같은 타깃·표본·단위로 보고한다. 모델이나 타깃별 표준화·분모 차이를 차감하지 않는다.

  **응답:** 원척도 확인 후 고정할 별도 loss 계약을 만들었다. 이진 순서 대비에는 Bernoulli log loss, 연속 원평정의 보조 예측에는 squared error, 실제 범주 분포에는 확인된 분포 계약을 사용한다. 다른 타깃의 z-score MSE나 likelihood 분모를 임의 차감하지 않는다.

  **남은 쟁점:** 실제 데이터·구현 검증은 미실행이며 실행 전 조건으로 남는다.

  [작성 원본](../../agents/03_vision_decoding/round05_rebuttal.json)

- **검토자 12 회의적비판자 / 수용:** Horikawa의 독립 반복이 확인되지 않으면 개인별 repeat ceiling을 가정하지 않는다. 원뇌의 보류자극 판독 가능성과 참 신뢰도 상한을 구별한다.

  **응답:** dupidx·같은 자극의 타 참가자·여러 run을 개인 내 반복으로 세지 않는다. 실제 반복 없으면 개인 repeat ceiling을 산출하지 않으며 원뇌 보류자극 예측과 주석 신뢰도·기술 대조를 각각 보고한다.

  **남은 쟁점:** 실제 데이터·구현 검증은 미실행이며 실행 전 조건으로 남는다.

  [작성 원본](../../agents/03_vision_decoding/round05_rebuttal.json)

- **검토자 01 데이터통계검토자 / 수용:** 실제 주석의 척도·집계단위에 맞는 한 가지 proper scoring rule과 관측모형을 사전 고정한다. 범주 확률이면 적절한 log score, 연속이면 명시한 분포모형의 점수/보조 squared loss를 사용하며 결과에 따라 유리한 척도를 바꾸지 않는다.

  **응답:** 모든 표적의 척도·집계·결측·분모를 codebook과 함께 잠근다. 순서 대비는 새 분석용 이진 타깃이며 원평정의 확률분포라는 주장을 하지 않는다. 원평정 보조 loss는 실제 측정척도에 맞춰 test 개봉 전에 고정한다.

  **남은 쟁점:** 실제 데이터·구현 검증은 미실행이며 실행 전 조건으로 남는다.

  [작성 원본](../../agents/03_vision_decoding/round05_rebuttal.json)

- **검토자 01 데이터통계검토자 / 수용:** 동일 보류 자극별 score 차이를 계산한다. 클래스·주석문항·피험자×시행을 모두 독립 N으로 세지 말고 참가자와 내용/원영상 그룹의 의존성을 보존한다.

  **응답:** 같은 test 쌍의 단계별 손실 차이를 짝지어 계산한다. 참가자×자극 행·범주 수·seed를 독립 N으로 세지 않고 원영상 가족 의존성 및 5명별 결과를 보존한다.

  **남은 쟁점:** 실제 데이터·구현 검증은 미실행이며 실행 전 조건으로 남는다.

  [작성 원본](../../agents/03_vision_decoding/round05_rebuttal.json)

- **검토자 01 데이터통계검토자 / 수용:** 원뇌 대비 신뢰도, 외부 주석의 신뢰도, 접근성 차이의 CI를 분리한다. 반복이 없으면 가역/절단 모의 대조의 성공만으로 원뇌 신뢰도를 대체하지 않는다.

  **응답:** 주석 신뢰도·반응 반복 신뢰도·원뇌 보류 예측·목표차 CI를 별도 표로 둔다. 반복 미확인 시 ceiling은 미확인으로 남기며 가역/절단 검사로 대체하지 않는다.

  **남은 쟁점:** 실제 데이터·구현 검증은 미실행이며 실행 전 조건으로 남는다.

  [작성 원본](../../agents/03_vision_decoding/round05_rebuttal.json)

- **검토자 01 데이터통계검토자 / 반박:** 현재 fallback인 ridge→CLIP 비교는 접근성 탐색이다. 정렬 학습목표의 효과를 주장하려면 작은 동일 backbone·입력·split·최적화 탐색예산에서 masked/contrastive 목표를 실제 비교해야 한다.

  **응답:** 동일 작은 backbone과 통제된 목적함수 비교 요구는 수용한다. 다만 masked 재구성과 contrastive는 예측 표적·입력 마스킹이 함께 바뀔 수 있어 일차 조작으로 쓰지 않는다. 동일 시각표적에 대한 contrastive 대 regression을 일차로 변경한다. 이는 제안자 초기 입장과 Coordinator 후속 지시에도 일치한다.

  **남은 쟁점:** 비판의 matched-objective 원칙에는 동의하며 masked/contrastive라는 예시를 순수 목표 차이로 사용하는 부분만 수정한다.

  [작성 원본](../../agents/03_vision_decoding/round05_rebuttal.json)

- **검토자 01 데이터통계검토자 / 수용:** 가역 대조는 알려진 역변환이 있는 조건수 제한 선형변환과 제한된 비선형 혼합을 구분한다. 선형변환 효과가 정규화/최적화 때문인지 확인하고 비가역 절단은 독립 주입 신호의 제거를 알고 있는 양성 대조로 쓴다.

  **응답:** 조건수 제한 선형·알려진 비선형 변환을 분리하고 정확 역변환 복구를 필수 검사한다. 주입 신호는 인간 정서 신호가 아니라 측정 감도 확인용 별도 합성 타깃임을 표시한다.

  **남은 쟁점:** 실제 데이터·구현 검증은 미실행이며 실행 전 조건으로 남는다.

  [작성 원본](../../agents/03_vision_decoding/round05_rebuttal.json)

- **검토자 01 데이터통계검토자 / 수용:** 총 주석 예측과 의미조건부 증분은 같은 test 표본/타깃/score로 계산한다. 의미 통제가 정서 공통분산을 제거할 수 있으므로 조건부 감소를 정서 정보 부재로 해석하지 않는다.

  **응답:** 같은 test 쌍·타깃·log loss에서 content-only와 content+brain을 비교한다. 총 점수와 증분을 모두 보고하며 의미조건화에 따른 감소를 인간 정서 정보 부재로 해석하지 않는다.

  **남은 쟁점:** 실제 데이터·구현 검증은 미실행이며 실행 전 조건으로 남는다.

  [작성 원본](../../agents/03_vision_decoding/round05_rebuttal.json)

- **검토자 12 회의적비판자 / 미해결:** 제안자는 접근성 곡선 자체를 신경과학 질문으로 볼 수 있다. 나는 신경기전 경쟁설명이나 정서 선택성이 없으면 독립적인 새 신경과학 RQ보다 측정방법 감사에 가깝다고 판단한다. 최상위 과학 카드 유지에 조건을 남긴다.

  **응답:** 선택성이나 신경기전 경쟁설명 없이 접근성 곡선만 남으면 방법 감사에 가깝다는 소수 의견을 보존한다. 조건부 과학 질문으로 카드에 남기되 선택성 대비 실패 시 방법 기여로 낮춘다.

  **남은 쟁점:** 신경측정 연구의 기여와 인간 신경계산 기전 발견 사이의 경계는 남는다. 억지 합의로 지우지 않는다.

  [작성 원본](../../agents/03_vision_decoding/round05_rebuttal.json)

- **검토자 01 데이터통계검토자 / 미해결:** 유한한 probe와 표본량에서의 비회복은 정보론적 삭제의 증거가 아니다. 반대로 회복 가능한 표현이라도 유한 자료에서의 접근성 변화는 과학적 결과가 될 수 있다는 점은 유지한다. 이 결과가 인간 신경 계산의 동일 목적함수를 뜻하는지는 여전히 미해결이다.

  **응답:** 유한 자료에서 회복 가능한 접근성 변화도 결과라는 입장을 수용한다. 인간 뇌가 같은 학습목표를 쓴다는 결론은 이 설계로 해소할 수 없다.

  **남은 쟁점:** 신경측정 연구의 기여와 인간 신경계산 기전 발견 사이의 경계는 남는다. 억지 합의로 지우지 않는다.

  [작성 원본](../../agents/03_vision_decoding/round05_rebuttal.json)

**최초 입장 원본:**

- [데이터통계검토자 01_dataset](../../agents/01_dataset/round05_debate.json)

- [제안자 03_vision_decoding](../../agents/03_vision_decoding/round05_debate.json)

- [회의적비판자 12_adversarial_review](../../agents/12_adversarial_review/round05_debate.json)


## RP02. 관계 의미의 설명력과 비가산 신경 예측의 중복을 고정 타깃에서 구별

**최종 판정:** 수정 후 조건부 제안

고정 A·loss·표본에서 D/N 함수족의 S 접근을 맞추고 δ=g(O+B)-g(O+R)를 검정한다. matching은 개발에서만 한다. 감소 주장에는 g(O) 기준·r_R의 실제 감소·δ 비교우위의 공동 조건을 요구하며 δ만 양수이면 차등 변조다.

**남은 대립:** 관계/비관계의 같은 예측력은 신경과의 오류 중복을 같게 하지 않는다. no-coupling 공통원인 모형이 같은 결과를 낼 수 있고 정확 direct prior도 미확정이다.

**실제 제안자의 응답:**

- **검토자 07 / 수정 수용·조건부 유지:** 가산/비가산 예측 차이는 함수군에 상대적이다. S×영역 유연성 차이, 빈약한 객체 기준, 공통 원인 U가 관계 특정 효과처럼 보일 수 있다. 예측력 matching은 신경 중복 구조를 맞추지 못한다.

  **응답:** point: 함수족과 해석; decision: 수용; change: 고정 A의 decoding 방향으로 한정하고 D=b(S)+Σr f_r(S,X_r), N=D+Σr<s h_rs(S,X_r,X_s)를 명시한다. 두 모형에 동일 S×영역·영역 내 비선형 접근을 준다. 관계 누락이 가짜 신경작용을 만든다는 표현과 인과·통신 주장을 철회한다. / point: 강한 기준과 관계 특이성; decision: 수용; change: O를 객체 목록에 한정하지 않고 공통 원 영상의 감각/전체 의미 특징을 포함한 강화 조건으로 평가한다. B는 O 조건부 A 예측력을 개발자료에서 맞추고 관계 역할·방향 교란 및 동의어 대조를 사람이 검수한다. 외부 test의 matching 실패도 결과로 보고한다. / point: 공통 입력 대안; decision: 수용; change: U→R,B,A와 U→각 ROI, ROI 간 직접 화살표가 없는 생성계를 두고 개인별 관측 혼합·HRF·측정잡음을 변화시켜 δ의 발생을 검사한다. 실제 구조와 유사한 no-coupling 모형도 δ>0를 낼 수 있음을 설계상 허용한다. / point: 신경과학적 기전 설명 가능성; decision: 미해결; change: baseline·실제 감소 r_R·차등 변화 δ의 공동 기준과 다른 대조를 통과했을 때에만 관계 정보와 고정 A의 지정 readout 사이 조건부 예측 중복/부분 대체를 지지한다. δ만 양수이면 차등 변조로 명명한다. no-coupling의 특정 모형을 넘는다고 신경 통신을 식별하지 않는다. / point: 출처·내용 지지·g(O); decision: 수용; change: R/B 생성에 평가 A·평가 BOLD를 사용하지 않고 Mind Captioning의 같은 뇌→설명→같은 뇌 순환을 금지한다. g(O)가 작거나 부정확하면 감소 가설 미검정이다. 충분한 baseline에서도 실제 감소 r_R와 차등 변화 δ의 공동 양수 기준을 요구한다. 내용 가족별 보류와 고정된 5명에 대한 추론 범위를 명시한다.

  **남은 쟁점:** 중립 관계 설명과 B의 예측력이 같아도 X와 공유하는 정보가 같지는 않다. 관계 전용 계산 또는 관계 의미를 제거한 순수 정서 신호라는 해석에 동의하지 않는다는 검토자의 소수 의견을 보존한다. 정확한 direct prior도 미확정이다.

  [작성 원본](../../agents/10_llm_semantics/round05_rebuttal.json)

- **검토자 12 / 수정 수용·조건부 유지:** 같은 A·proper loss·표본의 paired δ를 사용하고 B는 O 조건부 개발 예측력으로만 맞춰야 한다. 5명×자극 행을 독립 n으로 세지 말고 주석 형태, nested 선택, baseline g(O), 반복 유무를 확인해야 한다.

  **응답:** point: 추정량·손실; decision: 수용; change: r_R=g(O)-g(O+R), r_B=g(O)-g(O+B), δ=r_R-r_B=g(O+B)-g(O+R)를 여섯 조건의 동일 외부 표본 paired 손실로 계산한다. 실제 감소 r_R와 대조 차이 δ를 구분한다. 연속 평정의 평균제곱오차 또는 범주 확률의 Brier score처럼 실제 A 구조에 맞는 단일 proper loss를 BOLD 결과를 보기 전에 고정한다. 잔차 타깃·조건별 R² 분모 비교는 하지 않는다. / point: matching과 모형 선택; decision: 수용; change: O가 있을 때 R/B의 추가 A 예측력을 독립 개발 가족에서 cross-fitting하여 matching한다. ROI·차원축소·정규화·하이퍼파라미터는 inner fold에서 선택한다. 일차 nested 비교와 별도 계산량 일치 D 비교를 나누며 동일 파라미터 수라고 거짓으로 표시하지 않는다. / point: 추론 단위·사람 수; decision: 수용; change: 일차 추정은 관측된 5명에서 새로운 내용 가족으로의 일반화다. 가족별 g(O), r_R, δ를 같은 가중·재표집으로 공동 추론하고 참가자별 결과도 제시한다. 사람 모집단 추론은 별도이며 독립 5명 정확 양측 sign-flip 최소 p=2/32=0.0625 한계를 명시한다. hierarchical bootstrap이 사람 수를 늘리지 않는다. / point: 귀무와 측정 신뢰도; decision: 수용; change: A 전체 permutation은 δ=0의 귀무가 아니므로 주검정으로 쓰지 않는다. 가족 군집 손실차 CI, 조건부 B 대조, 공통 원인 합성 실험을 병행한다. 반복 없는 개인 ceiling·crossnobis나 개별 rater 없는 주석 재표집을 가정하지 않는다. / point: 감소 기준점·지지집합; decision: 수용; change: 충분한 g(O)는 필요하지만 충분하지 않다. 감소/부분 대체에는 g(O)>ε_g, r_R>ε_R, δ>ε_δ의 사전 양수 문턱을 각 단측 공동 신뢰하한이 모두 넘어야 한다. 개발 gate 이후 외부 표본을 한 번 평가하며 외부 g(O) 부재/작음은 미검정이다. r_R 감소가 확인되지 않은 양수 δ는 차등 변조로만 보고한다. A 누출이나 R/B overlap 부재는 비교 수정·중단 조건이다. / point: 최종감사: 실제 감소가 없는 양수 δ 반례; decision: 수용; change: Coordinator가 전달한 Agent12 최종감사 반례 g(O)=0.10, g(O+R)=0.20, g(O+B)=0.30에서 δ=0.10이지만 r_R=-0.10, r_B=-0.20이므로 두 조건 모두 증가한다. 이를 관계 감소의 양성으로 판정하던 불충분한 규칙을 수정했다. 실제 감소 r_R의 의미 있는 양수와 δ의 의미 있는 양수를 baseline 조건과 공동 요구하며, 그 외 양수 δ는 차등 변조로 분리한다. 이 항목은 기존 Round5 원문 인용이 아니라 최종감사 후 제안자의 수정 응답이다.

  **남은 쟁점:** 유한 B 집합의 길이·정보량·조건부 예측력 matching은 완전한 교환가능성을 만들지 않는다. 정확한 주석 스키마, 실효 가족 수, 최소 의미효과와 검출력은 아직 확정하지 않았다. 외부 주석은 개별 참가자의 정서 상태 정답이 아니다.

  [작성 원본](../../agents/10_llm_semantics/round05_rebuttal.json)

**최초 입장 원본:**

- [회의적비판자 07_geometry_information](../../agents/07_geometry_information/round05_debate.json)

- [제안자 10_llm_semantics](../../agents/10_llm_semantics/round05_debate.json)

- [데이터통계검토자 12_adversarial_review](../../agents/12_adversarial_review/round05_debate.json)


## RP03. 경계 단서와 과거 소거를 분리한 상태 갱신의 필요성

**최종 판정:** 수정 후 조건부 파일럿

경계를 같은 시점에 받는 연속 상태 대조와 exact functional control, HRF 이후 모형복구를 먼저 둔다.

**남은 대립:** 우세한 forgetting 매개화가 관측상 효율적일 수 있으나 인간 기억 소거나 전체 함수족에서의 필요성은 식별되지 않는다.

**실제 제안자의 응답:**

- **검토자 11_brain_inspired / 수용:** readout의 같은 boundary indicator만으로 state update의 정보 접근이 같아지지 않는다. 명시적 forgetting은 비명시 상태함수에 정확히 흡수될 수 있다.

  **응답:** 모든 주대조의 state update와 readout에 같은 b_t를 같은 available time에 제공한다. h_t=F((1−rho_t)h_prev+rho_t h0,x_t)와 F_tilde(h,x,b)=F((1−rho(b))h+rho(b)h0,x)의 exact functional control을 같은 가중치로 만들고 동일 출력을 확인하도록 계획했다. 이 둘은 하나의 함수 동치류이며 독립 기전으로 비교하지 않는다. 제목·결론도 제한된 parameterization의 예측 효용으로 축소했다.

  **남은 쟁점:** 유연한 상태함수가 같은 연산을 구현할 수 있으므로 미시적 기억 소거는 식별 불가능하다. 유한 예산에서의 효용은 남을 수 있다.

  [작성 원본](../../agents/05_multimodal_dynamics/round05_rebuttal.json)

- **검토자 11_brain_inspired / 수용:** random forgetting의 norm/예상오차 matching은 처리 이후 상태에 조건화할 수 있고, 사후 경계·미래 smoothing이 online 검정에 섞일 위험이 있다.

  **응답:** 위치 매칭은 forgetting을 적용하지 않은 공통 reference head의 사전 상태·과거에 도착한 오차·컷/음향 onset으로만 한다. boundary time_available, zero-phase 필터 금지, prefix feature 범위를 명시한다. 사후 인간 경계는 retrospective 분기로 격리하고 위치 대조를 실험적 무작위배정 null로 부르지 않는다.

  **남은 쟁점:** 자연 사건경계와 내용 변화의 완전한 분리는 보장되지 않는다. 위치특이 효용은 관찰 범위의 주장이다.

  [작성 원본](../../agents/05_multimodal_dynamics/round05_rebuttal.json)

- **검토자 08_systems_neuroscience / 수용:** 한 A 대비와 loss를 고정하고 외부 consensus를 개인 정답으로 취급하지 않아야 한다. 반복 신경자료를 가정하면 안 된다.

  **응답:** PILOT02의 주석은 실제 annotation dictionary에서 확인한 Fear 한 항목으로 고정한다. 개발에서 동일 target projection u_A와 lag를 정하고 모든 head에 같은 z_A를 사용한다. 현재 개인 내 동일 영화 독립 반복은 확인되지 않았으며 test–retest noise ceiling을 계산 가능하다고 가정하지 않는다. 외부 A와 held-out z_A 관계, 참가자/영화별 효과와 측정오차 민감도를 분리한다.

  **남은 쟁점:** 반복이 없으면 개인 신경 대비의 반복 신뢰도와 잡음상한을 직접 추정할 수 없다. 참가자 간 일치는 그 대체가 아니다.

  [작성 원본](../../agents/05_multimodal_dynamics/round05_rebuttal.json)

- **검토자 08_systems_neuroscience / 수용:** reset·연속 gate·유한창이 HRF 이후 같은 예측을 만들 수 있다. 영화14개를 다수 독립 경계창으로 세면 안 된다.

  **응답:** state기전×경계오차×HRF폭 합성 복구에 상대모형의 nuisance 재적합을 포함한다. exact controls는 동일해야 하며 다른 생성세계도 구분되지 않으면 신경기전 판정을 중단한다. 계획 하위집합은 최대6영화×8명이고 영화 전체 outer split을 사용한다. 작은 영화 수에서는 영화별 손실과 CI를 우선하고 유의성·동등성 확증을 보장하지 않는다.

  **남은 쟁점:** BOLD 관측동등성 내부의 기전 선택은 남긴다. 복구 시뮬레이션의 성공도 가정한 생성세계 밖의 식별을 보증하지 않는다.

  [작성 원본](../../agents/05_multimodal_dynamics/round05_rebuttal.json)

**최초 입장 원본:**

- [제안자 05_multimodal_dynamics](../../agents/05_multimodal_dynamics/round05_debate.json)

- [데이터통계검토자 08_systems_neuroscience](../../agents/08_systems_neuroscience/round05_debate.json)

- [회의적비판자 11_brain_inspired](../../agents/11_brain_inspired/round05_debate.json)


## RP04. 공유 병목의 용량을 넘어 남는 모달리티 정보의 예측 충분성

**최종 판정:** 조건부 제안

고정 shared 용량·readout·학습량에서 operational residual/full입력을 비교하고 실제 오디오 제시를 확인한다.

**남은 대립:** private의 비유일성과 유한 shared family 밖의 대안이 남는다. 양성도 생물학적 고유 경로 또는 PID 분해의 확증은 아니다.

**실제 제안자의 응답:**

- **검토자 06_frontier_ai / 수용:** 큰 k의 잔차 이득은 유한 shared/readout family의 한계이며 잔차는 독립 또는 biological private 정보가 아니다.

  **응답:** 카드 제목에 사전 지정 병목·판독 범위를 명시했다. R_k=X−g_train(S_k)는 해당 predictor의 operational residual이며 통계 독립을 뜻하지 않는다. S_k+R_k가 원정보의 가역 재표현인 설정은 full X와 같은 정보 접근 대조로 표기한다. 모든 조건에 같은 ridge/제한 nonlinear family·탐색·seed·학습량 곡선을 적용한다.

  **남은 쟁점:** 유한 k와 자료량에서 shared 표현이 충분히 강하다는 보편 기준은 없다. 결과는 명시한 family의 예측 충분성으로만 보고한다.

  [작성 원본](../../agents/05_multimodal_dynamics/round05_rebuttal.json)

- **검토자 06_frontier_ai / 수용:** 정서 특수성은 같은 자극의 신뢰도·난도를 맞춘 비정서 대비와 비교해야 한다. 좌표 난도와 정보 절단을 구분해야 한다.

  **응답:** 동일 자극·참가자에서 z_A와 사전 정의 z_C의 D_k를 공통 train 표준화로 비교하는 선택성 검정을 부차 분기로 추가한다. 이것이 없거나 효과가 동등하면 정서 관련 대비에서도 나타나는 일반 압축/접근성 결과라고 명명한다. 알려진 가역변환·rank 절단 신호주입과 학습량 회복을 먼저 검사한다.

  **남은 쟁점:** z_A와 z_C의 측정 신뢰도·난도가 완전히 같다고 보장할 수 없다. 정서 선택성은 추가 조건을 통과한 범위에서만 쓴다.

  [작성 원본](../../agents/05_multimodal_dynamics/round05_rebuttal.json)

- **검토자 04_brain_foundation / 수용:** 파일의 오디오와 실제 스캐너 내 오디오 재생을 구분하고 독립 대비·내용군·FactorCL 감독 경로를 확인해야 한다.

  **응답:** 실제 presentation 로그/공식 프로토콜과 원음원 매핑을 착수 계약에 둔다. Horikawa 재생이 확인되지 않으면 해당 시청각 분기를 실행하지 않고 재생조건이 확인된 Emo-FilM으로 전환한다. u_A·분해·readout·표준화는 모두 outer train 안에서 적합하고 독립 test A/BOLD로 재선택하지 않는다. FactorCL 감독이 미확인일 때는 frozen cache+train-only 투영으로 좁힌다.

  **남은 쟁점:** 현재 실제 보유본의 AV 재생·숫자주석·체크포인트 load는 확인되지 않았다. 데이터 보유와 실행 준비를 구분한다.

  [작성 원본](../../agents/05_multimodal_dynamics/round05_rebuttal.json)

- **검토자 04_brain_foundation / 수용:** 이벤트 수와 독립 표본수를 구분하고 반복을 가정하지 않아야 한다. Horikawa 5명 exact 양측 sign-flip은 최소 p=0.0625다.

  **응답:** 내용 중복은 같은 fold에 묶고 2,196행을 독립 자극 수로 세지 않는다. 개인 내 반복은 현재 미확인이라고 명시했다. 5명만의 모든 부호반전 32개에서 양측 최소 p=2/32임을 카드에 기록하고 p<0.05 보장을 제거한다. 참가자별 효과와 내용군 조건부 불확실성을 병기하며 정밀도 부족은 충분성 입증이 아니다.

  **남은 쟁점:** 새 참가자 모집단 추론은 5명 표본으로 제한된다. 자극 수·voxel 수 증가는 참가자 수를 대체하지 않는다.

  [작성 원본](../../agents/05_multimodal_dynamics/round05_rebuttal.json)

**최초 입장 원본:**

- [데이터통계검토자 04_brain_foundation](../../agents/04_brain_foundation/round05_debate.json)

- [제안자 05_multimodal_dynamics](../../agents/05_multimodal_dynamics/round05_debate.json)

- [회의적비판자 06_frontier_ai](../../agents/06_frontier_ai/round05_debate.json)


## RP05. 독립 반복의 신경 문맥이 자극모형 밖 정서 대비 예측을 회수하는가?

**최종 판정:** 설계 유지·신경 확증 착수 보류

같은 사람/자극의 독립 반복과 target-free 전처리가 확인될 때만 신경 문맥 회수 검정을 시작한다. 동시공간/과거미래 분기를 구별한다.

**남은 대립:** 안정적 미모형화 의미·혈관·해부학·추가 관측량이 신경 문맥 이득을 설명할 수 있다. 보유 사실만으로 반복 조건을 충족하지 않는다.

**실제 제안자의 응답:**

- **검토자 10_llm_semantics / 회의적비판자 / 수용:** 추가 신경 관측은 원 자극의 풍부한 proxy이므로 S 밖의 이득을 자극 밖 내부 정서 기전으로 해석할 수 없다.

  **응답:** 수용한다. 제목과 주장은 지정 S에 대한 독립 관측 문맥의 조건부 예측가치로 제한한다. 객체→관계→사건/맥락→유연한 raw stimulus 모형의 S 강화와 A/비정서 대비를 같이 보고한다. 같은 뇌에서 생성한 caption을 그 뇌 예측 입력으로 되넣지 않는다.

  **남은 쟁점:** 유한 S 강화로 의미 완전성은 입증되지 않는다. 양성 결과도 내부 상태와 미모형화 자극을 구별하지 않는다.

  [작성 원본](../../agents/04_brain_foundation/round05_rebuttal.json)

- **검토자 10_llm_semantics / 회의적비판자 / 수용:** 반복 입력의 추가 측정 비용, target 포함 여부, 동시 완성과 미래 예측의 차이를 선언해야 한다.

  **응답:** 수용한다. RP05-A는 test 자극에서 target 밖 N_a를 추가로 측정한 공간완성 계약이다. S-only와 같은 입력예산이라고 하지 않으며 동일 N을 쓰는 raw-context ridge를 따로 비교한다. target 자체의 다른 반복을 제공하는 것은 신뢰도 benchmark로 분리한다. RP05-B 과거→미래는 별도 관측 가지로 유지한다.

  **남은 쟁점:** A/B를 한 점수로 합치지 않는다. 독립 반복 존재 미확인으로 A의 신경 실증 착수는 보류한다.

  [작성 원본](../../agents/04_brain_foundation/round05_rebuttal.json)

- **검토자 01_dataset / 데이터통계검토자 / 수용:** 전처리 전파로 context에 target이 섞일 수 있어 단순 masking 순서 기술만으로 target-free가 성립하지 않는다.

  **응답:** 수용한다. 원입력에서 target와 buffer를 변경해도 고정 전처리 경로의 context feature가 허용 수치오차 안에서 불변인지 직접 확인하는 게이트를 둔다. affine H를 명시할 수 있으면 context←target block이 0인지도 확인한다. 이미 비가역 혼합된 처리본밖에 없어 이를 입증할 수 없으면 독립 문맥 가설을 착수하지 않는다.

  **남은 쟁점:** 유한 perturbation 검사는 일반 nonlinear 경로의 수학적 독립성 증명이 아니다. 구현 구조 감사와 함께 사용하고 검증 범위를 명시한다.

  [작성 원본](../../agents/04_brain_foundation/round05_rebuttal.json)

- **검토자 01_dataset / 데이터통계검토자 / 수용:** 반복 a/b가 실제 독립 측정인지, 적응·nuisance와 N 신뢰도 차이를 별도로 확인해야 한다.

  **응답:** 수용한다. 참가자·동일 원자극 hash·run/session·노출순서·측정일의 mapping을 요구한다. Horikawa 2,196개 고유 ID와 dupidx는 그 증거가 아니다. 같은 run 다른 자극뿐 아니라 A/내용/context 신뢰도 일치 다른 자극 N을 대조하며 Q·w·mask는 train에서 고정한다.

  **남은 쟁점:** 반복 적응과 안정 nuisance는 완전히 제거되지 않을 수 있다. 음성 결과를 독립 문맥 정보 부재로 단정하지 않는다.

  [작성 원본](../../agents/04_brain_foundation/round05_rebuttal.json)

**최초 입장 원본:**

- [데이터통계검토자 01_dataset](../../agents/01_dataset/round05_debate.json)

- [제안자 04_brain_foundation](../../agents/04_brain_foundation/round05_debate.json)

- [회의적비판자 10_llm_semantics](../../agents/10_llm_semantics/round05_debate.json)


## RP06. 내용 거리와 주석 불확실성을 맞춘 정서 경계의 초과 신경 거리

**최종 판정:** 설계·관측 탐색 유지·crossnobis 확증 보류

현 Horikawa는 경계·내용 지지집합과 보류 모형차이 탐색부터 한다. 개별 자극 경계거리 확증에는 실제 독립 추정치를 요구한다.

**남은 대립:** 내용 metric 공통 누락과 주석 불확실성이 남는다. condition 평균·다른 참가자 교차거리는 다른 추정대상이고 개인내 반복 대체가 아니다.

**실제 제안자의 응답:**

- **검토자 01_dataset / 회의적비판자 / 수용하여 범위 축소; 기전·전용성 해석은 하지 않음:** 복수 내용metric도 같은 누락을 공유할 수 있으며, 경계 초과량은 내용모형에 상대적인 관측 연관이다. 경계확률·독립 비정서 경계·pair graph 의존성과 새 사건 가족 일반화를 요구했다.

  **응답:** point: 누락 내용과 해석 범위; decision: 수용; answer: 일차 주장은 사전 고정한 내용모형 집합 아래 정서 경계 관련 잔여거리로 제한한다. 범주고유 코드·불연속성·곡률·순수 정서 인과를 주장하지 않는다. 사후 새 metric을 추가해 유리한 결과만 고르는 절차를 금지한다. / point: 경계확률과 주석 불확실성; decision: 수용; answer: 정확한 원 category 명칭·척도·평정자·집계법이 현재 미확인임을 기입했다. 실제 공통척도와 평정자 자료가 있을 때만 경계 가로지름 확률을 산출한다. 집계값만 있으면 가짜 rater split을 만들지 않고 새 독립 경계주석을 조건으로 둔다. / point: 비정서 경계와 내용매칭; decision: 수용; answer: 독립 객체·행위·사건 의미 경계를 정서 결과를 보지 않고 만들고 내용거리·개념 강도·주석 확실성·밀도를 맞춘다. 임의 label cut과 독립 의미경계는 별도 대조로 둔다. 매칭 실패면 정서 선택성을 주장하지 않는다. / point: pair 수와 독립성; decision: 수용; answer: 모든 endpoint가 outer fold 하나에만 속하도록 자극/내용 가족을 배정하고, 평가용 pair는 그 뒤 만든다. 공유 endpoint를 가진 edge를 독립 N으로 세지 않는다. 연결된 원자극 가족이나 중복 없는 matched pair 설계로 재표집 단위를 제한한다. / point: 관측적 기여의 과학 지위; decision: 미해결; answer: 제안자는 좁은 내용조건부 경계 대비 자체를 과학적으로 유익하다고 본다. 비판자가 경고한 미측정 의미의 인과 비식별은 그대로 보존하며 결과가 단순 매칭 민감도에 그치면 방법 결과로 낮춘다.

  **남은 쟁점:** 모든 의미 누락을 배제할 수 없으므로 양성 경계 연관을 정서 범주가 뇌 거리를 만드는 인과 원리로 승격할 수 없다. 이 한계는 최종 카드에 유지한다.

  [작성 원본](../../agents/02_affective_neuroscience/round05_rebuttal.json)

- **검토자 12_adversarial_review / 데이터통계검토자 / 수용; 현재 개인별 crossnobis 확증 보류, 설계·관측 탐색과 새 반복 분리:** 확인된 Horikawa는 각 참가자 2,196개 서로 다른 event ID/name이며 독립 반복 근거가 없어 개인별 자극 crossnobis 즉시 확증이 불가하다. 대체 추정량·endpoint 의존성·5명 모집단 정밀도·정확한 null을 구분해야 한다.

  **응답:** point: 반복 없는 crossnobis 확증; decision: 수용; answer: 현재 확인된 Horikawa 경로의 개인별 자극쌍 crossnobis 확증 계획을 즉시 실행 범위에서 제외했다. 기존자료는 ID·경계·내용 지지·관측적 예측 탐색에 한정하고, 동일 자극의 독립 반복이 실제 확인되거나 새 반복 신경측정을 수집하는 분기를 분리했다. / point: 가짜 반복 방지; decision: 수용; answer: 동일 event odd/even TR, voxel 반쪽, 다른 평정자, 임의 trial fold, 참가자간 평균을 개인 내 독립 반복으로 부르지 않는다. 15개 제외 인덱스나 61런도 반복 증거가 아니다. / point: 대체 관측설계의 추정대상; decision: 수용; answer: raw distance는 잡음이 섞인 관측 패턴거리, condition mean은 구성 exemplar의 평균 조건차, 참가자 교차거리는 정렬된 집단공유 패턴, held-out encoding 손실차는 모델 접근성이다. 카드에 별도 분기 ID와 변경된 해석을 적었고 개인 내 경계거리와 합치지 않는다. / point: pair graph·noise covariance·다중선택; decision: 수용; answer: 훈련에서 noise precision/shrinkage·metric·경계·매칭을 고정한다. outer split은 endpoint/family 단위이며 null도 node·family 구조와 내용조건부 교환가능성을 보존한다. 1개 경계·1개 주ROI·1개 primary metric을 먼저 고정하고 확장 대비는 별도 다중비교로 처리한다. / point: 5명 통계 한계; decision: 수용; answer: 5명의 양측 exact sign-flip 검정은 최소 p=2/32=0.0625여서 그 방법으로 0.05 사람모집단 유의성을 얻을 수 없다. 자극 가족 일반화는 관측된 5명에 조건부로 보고하고 참가자별 효과·CI를 제시한다. 더 많은 pair를 피험자 수 증가로 간주하지 않는다. / point: 당장 자연쌍 분석 가능이라는 표현; decision: 수용; answer: 당장 가능한 범위를 독립 주석·ID·matching·반복설계 감사와 탐색으로 정정했다. 실제 신경분석은 수행하지 않았고 확증 준비 완료라고 표시하지 않는다.

  **남은 쟁점:** 통계검토자의 즉시 확증 반대는 해결되지 않은 반론이 아니라 수용한 실행 경계다. 원자료 처리본에 미확인 반복이 있을 가능성은 새 증거가 제시될 때만 별도 확인하며 현재 있다고 가정하지 않는다.

  [작성 원본](../../agents/02_affective_neuroscience/round05_rebuttal.json)

**최초 입장 원본:**

- [회의적비판자 01_dataset](../../agents/01_dataset/round05_debate.json)

- [제안자 02_affective_neuroscience](../../agents/02_affective_neuroscience/round05_debate.json)

- [데이터통계검토자 12_adversarial_review](../../agents/12_adversarial_review/round05_debate.json)


## RP07. 독립 관측이 배제하는 정서 상반 witness 쌍

**최종 판정:** Discovery 유지·첫3파일럿 제외

유한 자연 universe의 witness와 참조 유지부터 설계한다. 정서주석+독립반복 경로 또는 명시적인 집단 관측 계약이 확보되어야 한다.

**남은 대립:** 생성 후보의 forward calibration은 자연 관측에서 보장되지 않는다. 단순 SNR 개선·encoder 취약점·선택 후 오배제율이 남으며 미발견은 유일성 증명이 아니다.

**실제 제안자의 응답:**

- **검토자 03_vision_decoding / 회의적비판자 / 수용:** 추가 반복의 한쪽 배제는 일반 SNR 향상이나 발견 관측에 과적합한 encoder 취약점의 제거로 설명할 수 있다.

  **응답:** 수용한다. 참조 원본을 포함한 유한 자연 후보군을 일차 경로로 바꾸고, 정서 차이 큰/작은 witness를 감각거리·객체/사건 관계·초기 오차·난도에서 맞춘다. 같은 추가 관측량에서 배제 이득의 차이를 일반 시각/SNR 모형과 비교한다. 동일 관측 재사용, 독립 반복 평균, 동일 총 관측량의 대조를 둔다. 배제 이득이 모든 후보군에 균일하면 정서 신경과학 기여를 주장하지 않고 측정 방법 결과로 낮춘다.

  **남은 쟁점:** 측정한 의미 공변량 밖의 차이는 남는다. 정서 관련 관측 제약이라는 표현은 허용하지만 정서 특이 계산으로 승격할 조건은 아직 충족되지 않았다.

  [작성 원본](../../agents/09_generative_ai/round05_rebuttal.json)

- **검토자 03_vision_decoding / 회의적비판자 / 수용:** 반복을 늘려 계속 검사하면 오배제가 누적되며, 둘 모두 탈락·참조 탈락을 모호성 해결로 셀 위험이 있다. 유한 내부 근사는 실제 뇌 허용집합이 아니라 지정 모형 집합에 대해서만 성립한다.

  **응답:** 수용한다. 일차 추가 관측량 k* 하나를 개발 단계에서 고정하고 곡선은 사전 그리드의 보정된 이차 분석으로 둔다. 별도 calibration 자극에서 각 k의 covariance·참조 오배제율과 누적 검사 오류를 보정한다. 정확히 한쪽 배제+다른 쪽 양립+참조 양립일 때만 지정 witness 판별로 기록한다. 둘 모두 탈락, 참조 탈락, 두 후보 유지, 불확실, 미발견을 별도 보고한다. sample min/max나 미발견을 전역 경계·유일성으로 해석하지 않는다.

  **남은 쟁점:** 오지정 forward의 허용집합은 실제 뇌의 참 해집합에 대한 내부 근사라는 보장도 없다. 자연 참조 calibration 성공이 생성 후보의 coverage까지 보증하지 않는다.

  [작성 원본](../../agents/09_generative_ai/round05_rebuttal.json)

- **검토자 07_geometry_information / 데이터통계검토자 / 수용:** discovery/calibration/test 분리, 실제 반복 독립성, p>α와 양립성의 구별, 후보의 분포 이동·계층 의존성 통제가 필요하다.

  **응답:** 수용한다. 자극 family를 train/calibration/evaluation으로 먼저 나누고 evaluation 원본의 discovery 획득과 최종 holdout 획득을 분리한다. witness 선택·ROI·정규화·허용폭·forward 튜닝에 holdout을 쓰지 않는다. 개발에서 정한 예측오차 허용폭과 보정된 오차 구간으로 양립/배제/미결정을 판정하며 비유의를 양립으로 치환하지 않는다. run drift·HRF·공유 전처리 상관을 반영한 shrinkage covariance와 참가자×원본 군집 추론을 사용한다. 생성 후보에는 별도 분포 이동 gate를 두고 seed나 모델 수를 신경 표본 수로 세지 않는다.

  **남은 쟁점:** 생성 후보의 오차가 자연 calibration과 교환가능하다는 보장은 없다. 정서층·감각층별 참조 유지와 합성 오류 통제는 필요한 검사이며 실제 뇌 coverage의 충분조건은 아니다.

  [작성 원본](../../agents/09_generative_ai/round05_rebuttal.json)

- **검토자 07_geometry_information / 데이터통계검토자 / 수용:** Horikawa 반복·NSD 정서 주석을 가정할 수 없고, 원본의 보류 반복은 생성 후보를 제시한 실제 반응이 아니다.

  **응답:** 수용한다. Horikawa의 내용 중복·61런·2196 이벤트를 개인 내 독립 반복으로 사용하지 않는다. NSD는 검증된 정서 정답이 없으므로 첫 작은 단계는 시각 역문제 방법검정이다. 정서 질문에는 원본과 후보의 새 독립 인간 주석 또는 실제 확인된 기존 주석이 필요하다. 원본 반복이 부족하면 새 원본 반복 측정이 필요하며, 두 후보 자체의 신경 동등성/차이를 주장하려면 두 후보를 새로 제시한 BOLD가 별도로 필요하다. Horikawa 공통 자극에 독립 참가자를 추가하는 관찰 분기는 집단 자극 표적과 train-only 개인 mapping을 가진 별도 질문으로 표시한다.

  **남은 쟁점:** 보유본의 정확 반복·주석·mapping은 아직 실물 검증 전이다. RP07은 첫 3개 파일럿에서 제외된 장기 카드이며 개인 반복 경로를 실행 준비 완료로 표시하지 않는다.

  [작성 원본](../../agents/09_generative_ai/round05_rebuttal.json)

- **검토자 03_vision_decoding / 회의적비판자 / 미해결:** 정서 상반 witness 배제가 새로운 정서 신경 계산인가, 기존 역문제 정밀도 개선을 정서로 재명명한 것인가가 남는다.

  **응답:** 이견을 보존한다. 과학 질문은 측정된 정서 대비가 큰 고정 후보의 배제 곡선이 의미·감각·초기 오차·SNR 대조와 다른가로 좁힌다. 현재의 설계만으로 정서 고유 계산을 약속하지 않는다. 자연 후보에서 같은 비용의 직접 판독·retrieval이 설명하는 결과를 넘어서는 대비가 없으면 방법 기여만 남긴다. 별도 forward 일치도 공통 훈련자료의 오류 독립성 증거로 사용하지 않는다.

  **남은 쟁점:** 최신 근접 선행의 전수 확인과 실제 효과가 없어 독창성과 정서 특이성의 최종 판단은 미결이다. 비판자의 수정 판정을 조건부 유지와 함께 카드에 남긴다.

  [작성 원본](../../agents/09_generative_ai/round05_rebuttal.json)

**최초 입장 원본:**

- [회의적비판자 03_vision_decoding](../../agents/03_vision_decoding/round05_debate.json)

- [데이터통계검토자 07_geometry_information](../../agents/07_geometry_information/round05_debate.json)

- [제안자 09_generative_ai](../../agents/09_generative_ai/round05_debate.json)


## RP08. parcel 평균이 지운 내부 공간 대비는 정서 관련 예측에 필요한가?

**최종 판정:** 수정 후 조건부 파일럿

면적가중 평균/영공간 좌표를 분리하고 H1일반상쇄·H2atlas·H3정서선택성을 별도 검정한다. 강한 평균-only 대조와 train-only k곡선을 둔다.

**남은 대립:** PCA r_k의 실패는 전체 영공간의 실패가 아니다. H1만 양성이면 일반 공간 접근성으로 제한하고 반복 신뢰도·피험자 모집단 결론을 추가하지 않는다.

**실제 제안자의 응답:**

- **검토자 08_systems_neuroscience / 회의적비판자 / 수용:** 영공간의 존재는 자명하며 강한 nonlinear mean-only가 잔차 이득을 회수할 수 있다.

  **응답:** 수용한다. H1 주비교에 tuned ridge와 kernel ridge 또는 작은 MLP의 m-only를 넣고 같은 정보입력·선택예산·nested tuning을 유지한다. 잔차 k곡선을 train-selected primary k와 함께 전체 보고한다. 일반 MVPA 우위만 확인되면 공간 QC 모듈로 낮춘다.

  **남은 쟁점:** 제안자는 제한된 접근성 검정도 첫 파일럿 가치가 있다고 보지만 비판자는 정서 선택성과 반복 없이는 독립 과학 RQ의 신규성이 약하다고 본다. 이 소수 의견을 보존한다.

  [작성 원본](../../agents/04_brain_foundation/round05_rebuttal.json)

- **검토자 08_systems_neuroscience / 회의적비판자 / 수용:** 면적가중 G/P, 타깃 척도, k와 신뢰도 선택을 명확히 해야 한다.

  **응답:** 수용한다. C를 비중첩 parcel membership, W를 고정 양의 voxel-volume/vertex-area 가중으로 두고 G=(CᵀWC)⁻¹CᵀW, P=CG를 정의한다. H3는 train 표준화한 A와 비교가능한 비정서 B의 paired-risk interaction으로 고정한다. 원효과와 신뢰도/공간대역 matching 후 효과를 모두 보존한다.

  **남은 쟁점:** 면적 정보가 없으면 W=I인 명시적 무가중 관측만 수행한다. 동일 rank는 동일 정보량이 아니며 모든 타깃의 난도/신뢰도를 완전히 맞출 수 없다.

  [작성 원본](../../agents/04_brain_foundation/round05_rebuttal.json)

- **검토자 11_brain_inspired / 데이터통계검토자 / 수용:** Horikawa 5명과 고유 이벤트 ID는 반복 신뢰도나 강한 사람 모집단 추론을 보장하지 않는다.

  **응답:** 수용한다. 첫 PILOT03은 다섯 명 각각과 그 참가자들에 조건부인 새 자극 일반화만 평가한다. 독립 반복이 실제 없으면 반복 noise ceiling과 반복 재현 witness를 계산하지 않는다. 내용 중복·복사본·다른 사람의 같은 자극을 개인 내 반복으로 바꾸지 않는다. 양측 exact sign-flip 최소 p=.0625와 집단 CI의 불안정성을 명시한다.

  **남은 쟁점:** 새 자극에서의 접근성 이득은 반복 신호의 안정성과 다른 증거다. 참가자 모집단 일반화/반복 주장은 별도 자료를 요구한다.

  [작성 원본](../../agents/04_brain_foundation/round05_rebuttal.json)

- **검토자 11_brain_inspired / 데이터통계검토자 / 수용:** H1/H2/H3·k·atlas 탐색과 잘못된 label permutation이 conditional null을 흐릴 수 있다.

  **응답:** 수용한다. H1을 일차, H2/H3를 사전 순서가 있는 별도 이차 가족으로 둔다. k/alpha/basis/atlas 선택은 내부훈련에만 두고 primary k와 고정 k곡선을 같이 보고한다. A 무조건 permutation은 평균의 실제 신호도 제거하므로 H1 정확 null로 부르지 않는다. known m-only 생성 null과 reduced-model 적합·exchangeability를 점검한 residual resampling을 별도로 사용한다.

  **남은 쟁점:** 조건부 null의 오지정 위험이 남는다. 대조가 실패하거나 precision이 부족하면 확증이 아니라 방법 점검으로 제한한다.

  [작성 원본](../../agents/04_brain_foundation/round05_rebuttal.json)

**최초 입장 원본:**

- [제안자 04_brain_foundation](../../agents/04_brain_foundation/round05_debate.json)

- [회의적비판자 08_systems_neuroscience](../../agents/08_systems_neuroscience/round05_debate.json)

- [데이터통계검토자 11_brain_inspired](../../agents/11_brain_inspired/round05_debate.json)


## RP09. 비정서 anchor 선택으로 정서 의미 대응을 결정할 수 있는가

**최종 판정:** Discovery 유지·자료 내 교정부터

anchor 정의·정보예산·ID 접근·inductive extension을 명세하고 geometry/anchor-only 대조를 둔다. 정서감독 미사용의 단계 범위를 명시한다.

**남은 대립:** 의미 feature 자체의 정서정보는 제거되지 않는다. 유한 다중시작의 범위가 전역 식별집합이나 의미 유일성을 보장하지 않는다.

**실제 제안자의 응답:**

- **검토자 02 / 수용:** anchor-only 의미/identity 지름길만으로 정서 전이가 가능하므로 신경기하의 추가 기여가 필요하다.

  **응답:** 주 outcome을 측정 R로 정의한 target B의 보류 정서 대비 예측위험 ℛ로 고정한다. 동일 queried pair와 source 시각/의미 특징만 쓰는 V→B_target ridge, paired B→B ridge/Procrustes, neural geometry 제거/내용조건부 교란을 비교한다. 정서 주석 예측은 보조 지표이며 B 추가 이득이 없으면 방법후보로 축소한다.

  **남은 쟁점:** 없음: 이 응답은 제안자의 수정이며 검토자의 사후 동의를 뜻하지 않는다.

  [작성 원본](../../agents/07_geometry_information/round05_rebuttal.json)

- **검토자 02 / 수용:** 정서 감독 미사용의 범위와 reference 평가 readout을 명시하라.

  **응답:** 정서 감독 미사용은 alignment와 anchor-selection의 훈련·개발·하이퍼파라미터·보상에 R 및 R로 감독한 모델을 쓰지 않는다는 뜻이다. 별도 evaluator reference는 R로 대비 정의를 고정할 수 있고 모든 정책에 공통이다. 최종 B/R/ID는 evaluator에만 공개한다. 정서 감독 대조군은 사용한 R값의 수·대비·출처를 기록한다.

  **남은 쟁점:** 없음: 이 응답은 제안자의 수정이며 검토자의 사후 동의를 뜻하지 않는다.

  [작성 원본](../../agents/07_geometry_information/round05_rebuttal.json)

- **검토자 02 / 미해결:** anchor 수만 같으면 정보·신뢰도·비용이 같다는 가정은 부당하다.

  **응답:** anchor 하나는 익명 source calibration row와 target calibration row의 동일 자극 대응 하나를 공개하는 pair query로 통일한다. 모든 군은 같은 익명 B pool을 기본 제공받는다. semantic 벡터와 정서 R의 사전 노출은 별도 ledger에 차원·수·신뢰도·비용으로 기록한다. 고정 pair-budget 결과와 실제 비용을 확인한 cost-matched 민감도를 분리한다. 동일 비트 정보량이라는 주장은 삭제한다.

  **남은 쟁점:** pair payload는 같게 할 수 있지만 사전학습 특징과 정서 주석의 유효 정보량을 완전히 같게 할 수 없다. 비교는 공개된 접근 계약에 조건부다.

  [작성 원본](../../agents/07_geometry_information/round05_rebuttal.json)

- **검토자 02 / 반박:** identity oracle을 포함하고 그 대조를 넘어야 한다.

  **응답:** identity baseline을 추가한다. 같은 pair-budget의 lookup/시각의미 mapping은 정당한 경쟁모형이다. 모든 학습 pair ID를 아는 supervised ridge/Procrustes oracle은 추가 정보 접근의 참고 기준이다. 최종 target B를 ID로 직접 조회하는 oracle은 정답 접근이므로 경쟁모형으로 금지한다. 더 많은 정보를 가진 oracle을 반드시 능가해야 한다는 문자적 기준은 채택하지 않는다.

  **남은 쟁점:** oracle 포함은 수용하지만 oracle 능가를 과학후보 유지의 필요조건으로 삼지 않는다. 같은 접근예산 기준을 넘는 신경 예측과 oracle까지의 간극을 각각 보고한다.

  [작성 원본](../../agents/07_geometry_information/round05_rebuttal.json)

- **검토자 02 / 수용:** 동일 자극 주석 재사용과 실제 target neural contrast의 전이를 구별하라.

  **응답:** R은 자극 집계 주석이며 참가자별 독립 라벨이 아니다. 새 내용의 source B로 target B를 예측한 뒤 evaluator가 고정 R 가중치의 실제 target B 대비와 비교한다. 최종 내용과 최종 정서 대비는 alignment/selection에 사용하지 않는다. 새 참가자 결과도 source/target 적응 B 접근량을 기록하며 무관측 참가자 zero-shot으로 부르지 않는다.

  **남은 쟁점:** 없음: 이 응답은 제안자의 수정이며 검토자의 사후 동의를 뜻하지 않는다.

  [작성 원본](../../agents/07_geometry_information/round05_rebuttal.json)

- **검토자 02 / 수용:** 자료간 bridge 없이 공통 정서 척도·공유 신경코드를 주장하지 말라.

  **응답:** 첫 자료는 Horikawa 내부 참가자쌍/내용 보류다. 실제 공통 coverage와 처리단위를 확인한다. Emo-FilM·Spacetop 확장은 독립 bridge와 측정모형이 확인될 때만 수행하고 서로 다른 집계 주석을 합치지 않는다. Mind Captioning의 이름으로 ontology나 정서 주석을 추정하지 않는다.

  **남은 쟁점:** 없음: 이 응답은 제안자의 수정이며 검토자의 사후 동의를 뜻하지 않는다.

  [작성 원본](../../agents/07_geometry_information/round05_rebuttal.json)

- **검토자 02 / 수용:** 동치류 정의·해선택에 final test label을 쓰면 누수다. 유한해 범위는 전체 식별집합이 아니다.

  **응답:** 고정한 비정서 development 예측함수로 동치류를 표시하고 모든 ε-허용해를 보존한다. 최종 test에서 해를 선택·재군집·최적화하지 않는다. primary point estimator는 train objective로 고정하고, 최종 ℬ는 보존된 모든 해의 예측직경이다. development 동치류가 test에서도 동치라는 가정은 하지 않는다. ℬ는 global bound·posterior·CI가 아니다.

  **남은 쟁점:** 없음: 이 응답은 제안자의 수정이며 검토자의 사후 동의를 뜻하지 않는다.

  [작성 원본](../../agents/07_geometry_information/round05_rebuttal.json)

- **검토자 02 / 수용:** row/column 동시 permutation으로 기하구조를 보존하면서 내용·SNR null을 검증하라.

  **응답:** 순수 동시 재라벨링은 예측을 바꾸지 않아야 하는 구현 검사로 둔다. 신경정보 제거 대조는 V/ID/R를 고정한 채 B와 그로부터 재계산한 D의 의미 결합을 바꾼다. train-only V→B 잔차를 내용·run·SNR 층에서 교환하는 조건부 대조와 알려진 공통입력 null을 사용한다. 교환가능성이 미검증이면 permutation p-value가 아닌 민감도로 보고하고 신경 고유 해석을 보류한다.

  **남은 쟁점:** 모든 라벨까지 같이 교환하는 기하 재표기는 null 효과를 만들 수 없다. 기하 교란이 신경 고유성의 완전한 인과검정이라는 해석도 채택하지 않는다.

  [작성 원본](../../agents/07_geometry_information/round05_rebuttal.json)

- **검토자 08 / 미해결:** pair/scalar/vector anchor는 같은 개수라는 이유로 동일 정보예산이 아니다.

  **응답:** primary query는 pair correspondence 하나로 고정한다. 정서/의미 scalar 또는 vector는 별도 metadata access이며 pool 전체를 정책이 봤다면 선택한 b개만 아니라 노출된 M×d개 값을 예산표에 기록한다. 주석 신뢰도·결측·수집비용 미확인시 cost-matched라는 표현을 쓰지 않는다.

  **남은 쟁점:** 동일 query payload 이상의 유효 정보량 등가는 보장하지 못한다. 정보감사 가능한 조건부 비교로 유지한다.

  [작성 원본](../../agents/07_geometry_information/round05_rebuttal.json)

- **검토자 08 / 수용:** 정렬·정책개발·ε calibration·최종평가를 나누고 참 ID 접근을 명시하라.

  **응답:** D_policy/T_align/C_calibration/R_reference/E_test의 역할을 분리해 내용그룹 단위로 구성한다. 실제 표본수에 따라 D와 C를 nested 교차검증으로 재사용할 수 있으나 E는 봉인한다. ID는 evaluator join과 b개 query 응답에만 쓰며 모델 입력에서 파일명·row ordering·세션 정렬의 숨은 ID를 제거한다. 접근표를 카드에 추가한다.

  **남은 쟁점:** 없음: 이 응답은 제안자의 수정이며 검토자의 사후 동의를 뜻하지 않는다.

  [작성 원본](../../agents/07_geometry_information/round05_rebuttal.json)

- **검토자 08 / 수용:** GW에서 새 자극으로 가는 extension map과 inductive/transductive를 명시하라.

  **응답:** 학습 coupling T의 barycentric target Z_i=Σ_jT_ij B_target,j/p_i를 만들고 B_source→Z ridge를 훈련에서 적합한다. λ는 정서값 없는 개발 pair response loss로 정하며 query 노출을 ledger에 포함한다. inductive는 test source B만 입력하며 test target B와 test target geometry를 보지 않는다. transductive는 test geometry를 쓰는 별도 정보조건과 결과로 기록한다.

  **남은 쟁점:** 없음: 이 응답은 제안자의 수정이며 검토자의 사후 동의를 뜻하지 않는다.

  [작성 원본](../../agents/07_geometry_information/round05_rebuttal.json)

- **검토자 08 / 수용:** 동등비용 반대 의미해는 비유일성 witness이며 미발견은 global 유일성이 아니다.

  **응답:** 같은 고정 objective에서 cost 차이≤ε인 해만 비교하고 regularization 변경은 별도 조건으로 둔다. synthetic 대칭/비대칭에서 search 검출력과 오확신을 점검한다. ℬ 축소만으로 성공을 선언하지 않으며 ℛ·신뢰도·noise calibration과 함께 보고한다. global 유일성은 끝까지 미확정이다.

  **남은 쟁점:** 없음: 이 응답은 제안자의 수정이며 검토자의 사후 동의를 뜻하지 않는다.

  [작성 원본](../../agents/07_geometry_information/round05_rebuttal.json)

- **검토자 08 / 수용:** RDM 쌍·adaptive round는 독립 N이 아니며 Horikawa 5명·자료별 측정 단위를 구별하라.

  **응답:** 독립 내용 family를 기본 재표집 단위로 삼고 참가자쌍 의존성을 유지한다. 같은 참가자가 포함된 20개 방향쌍을 20명으로 세지 않는다. RDM entry·seed·anchor round는 표본 N이 아니다. 참가자 일반화는 5명 범위의 불확실성과 개인별 결과를 함께 제시하고 신뢰도 낮은 contrast를 사후 제거하지 않는다.

  **남은 쟁점:** 없음: 이 응답은 제안자의 수정이며 검토자의 사후 동의를 뜻하지 않는다.

  [작성 원본](../../agents/07_geometry_information/round05_rebuttal.json)

- **검토자 08 / 수용:** 비유의 차이를 충분성으로 바꾸지 말고 최소효과·검정력·수렴실패를 검사하라.

  **응답:** 사전 실용적 허용폭 Δ와 최소 신경 추가효과 η를 reference/calibration의 측정척도에 연결해 고정한다. 정서감독 추가이득에 대한 동등성 CI와 paired 위험 차이를 보고한다. synthetic에서 알려진 효과의 회복·false confidence·optimizer 실패를 측정한다. 실제 효과크기·반복수가 미확인인 현재 수치 power는 선언하지 않는다.

  **남은 쟁점:** 없음: 이 응답은 제안자의 수정이며 검토자의 사후 동의를 뜻하지 않는다.

  [작성 원본](../../agents/07_geometry_information/round05_rebuttal.json)

- **검토자 08 / 수용:** 공통 anchor·extension이 없으면 C01-04 방법후보 지위와 C07-04 과학후보를 같은 완료로 병합할 수 없다.

  **응답:** 조건부 과학후보를 유지하되 계약/extension/null gate 미충족이면 방법 감사로 낮춘다. C01-04의 방법후보 판정은 그대로 보존한다. synthetic 회복만 성공하면 절차 점검 완료이며 신경과학 결과 완료가 아니다.

  **남은 쟁점:** 현재 기획은 완료했으나 실제 신경 추가효과와 과학적 식별성은 미검증이다. 두 원안의 지위를 하나의 성공으로 합치지 않는다.

  [작성 원본](../../agents/07_geometry_information/round05_rebuttal.json)

**최초 입장 원본:**

- [회의적비판자 02_affective_neuroscience](../../agents/02_affective_neuroscience/round05_debate.json)

- [제안자 07_geometry_information](../../agents/07_geometry_information/round05_debate.json)

- [데이터통계검토자 08_systems_neuroscience](../../agents/08_systems_neuroscience/round05_debate.json)


## RP10. 사전 허용집합 안에서 검증하는 정서 관련 편집 신경 대비

**최종 판정:** Discovery 유지·새 주석/신경 측정 조건

family 수준 허용집합을 BOLD 이전에 고정하고 독립 realization·모든 실패·새 주석/제시를 포함한다.

**남은 대립:** 양성 효과는 선택된 실제 자극 묶음의 차이다. 미측정 의미·생성 흔적을 배제한 순수 정서 인과량으로 해석할 수 없다.

**실제 제안자의 응답:**

- **검토자 06_frontier_ai / 회의적비판자 / 수용:** 동강도 편집·CLIP 유사도·제한된 평정은 정서 외 모든 의미를 보존하지 않으며 실제 효과는 자극 묶음의 효과다.

  **응답:** 수용한다. A는 새 독립 인간이 측정하는 자극의 부정적 정서 내용 강도로 명시하고 객체·행동·관계·사건 결과·가림·색/대비·자연성을 보존/감각 차원으로 따로 기록한다. 목표 A 변화의 하한과 비목표 차이의 상한을 구분하며 A 변화 자체를 양 조건에서 매칭해 없애지 않는다. 결론은 S_f=1 family에서 실제 목표−비목표 자극 묶음이 만드는 신경 대비다. 무작위 자극 할당으로부터 정서 단일 잠재 요인·회로의 인과성을 추론하지 않는다.

  **남은 쟁점:** 정서 단서와 사건 의미는 구성적으로 겹칠 수 있다. 독립 평정 통과 이후에도 미측정 의미 차이가 남으므로 정서만의 효과는 주장하지 않는다.

  [작성 원본](../../agents/09_generative_ai/round05_rebuttal.json)

- **검토자 06_frontier_ai / 회의적비판자 / 수용:** 목표 편집의 artifact와 내용 변화가 paired 신경 대비를 설명할 수 있으며 같은 함수족의 강한 기준과 여러 realization이 필요하다.

  **응답:** 수용한다. 원본·무편집 왕복·감각 변형량을 맞춘 비목표·자연 matched 대조를 둔다. 같은 실제 Y와 family split에서 감각, 감각+독립 관계 의미, 이에 A 또는 목표 대비를 추가한 ridge 모형을 같은 정규화·선택 예산으로 비교한다. prompt를 독립 정서 정답으로 쓰지 않는다. 최소 두 realization을 family 내부 반복으로 두고, 가능한 두 지정 editor의 효과 및 상호작용을 고정효과로 보고한다. 공유 backbone/data 때문에 두 editor의 일치도 독립 생성기 모집단 증거가 아니다.

  **남은 쟁점:** 자연 matched 자극으로의 전이가 없으면 공통 생성 artifact가 남는다. 강한 내용 기준을 넘는 예측 개선도 미측정 의미를 제거하지 못한다.

  [작성 원본](../../agents/09_generative_ai/round05_rebuttal.json)

- **검토자 10_llm_semantics / 데이터통계검토자 / 수용:** family 단위 S와 목표 모집단, 개발/검증/신경확인의 분리, 허용 실패·S=1 내부 누락을 명시해야 한다.

  **응답:** 수용한다. 원본·목표·비목표·무편집의 완전한 family가 공동 지지를 갖는 S_f를 개발 주석에서 동결한다. 독립 검증 주석은 고정 절차의 조작/보존 타당성을 검사하고 결과에 맞춘 재선택은 새 개발 라운드로 처리한다. 새 BOLD는 그 뒤 별도 확인 표본에서 수집한다. 모든 생성시도·seed·prompt·오류·탈락·누락과 원본별 통과율을 남기며 한쪽만 통과한 family를 성공 pair로 메우지 않는다. S=0을 가중치로 복원하거나 S=1의 누락을 무시한 원모집단 일반화를 하지 않는다.

  **남은 쟁점:** 관찰 가능한 모집단은 허용된 family와 실제 표집 참가자로 제한된다. 확인 표본이 부분 교차라면 이상적인 E_f E_s보다 좁은 대상만 식별할 수 있다.

  [작성 원본](../../agents/09_generative_ai/round05_rebuttal.json)

- **검토자 10_llm_semantics / 데이터통계검토자 / 수용:** 고정 신경요약 v와 최소효과, 참가자×family 추론, 타당한 null·검정력 계획이 필요하며 기존 BOLD는 새 편집물에 붙일 수 없다.

  **응답:** 수용한다. 독립 개발 신경표본에서 v의 방향과 스케일을 고정하고 d_sf=v^T(Y_target−Y_control), theta=E_f E_s[d_sf|S_f=1]를 주추정량으로 둔다. v를 정당화할 수 없으면 test 전 비부호 cross-validated 거리 질문으로 변경하고 별도 등록한다. 참가자·family·run·반복/seed 의존성과 순서/적응 효과를 반영하며 실제 무작위 배정이 허용하는 제한적 null 또는 계층 모의자료로 오류율을 검증한다. 새 독립 주석과 새 편집 자극 BOLD가 필수이고 개발 분산·통과율로 최소효과의 검출력/등가성 정밀도를 산정한다.

  **남은 쟁점:** 새 신경표본·반복 신뢰도·효과크기가 아직 없어서 N을 확정할 수 없다. 새 family와 참가자에 대한 일반화도 실제 표집설계가 충족하는 범위에 한정한다.

  [작성 원본](../../agents/09_generative_ai/round05_rebuttal.json)

- **검토자 06_frontier_ai / 회의적비판자 / 미해결:** 생성 편집이 자연 matched 자극보다 과학적으로 필요한지는 통과율·대비 크기·비용을 보기 전 미결이다.

  **응답:** 이견을 보존한다. 처음에는 생성 없는 자연 matched 비교를 기준으로 만들고, 생성 경로가 독립 검증에서 더 큰 A 대비와 유사한 비목표 차이의 family를 제공하는지 비용·실패까지 함께 비교한다. 이득이 없으면 생성 확장을 중단하고 자연 자극의 관찰 질문 또는 타당성 방법 연구로 낮춘다. 생성모델 사용이나 성공 영상 자체를 신규성으로 계산하지 않는다.

  **남은 쟁점:** 현재 생성·인간 주석·새 BOLD를 실행하지 않았으므로 생성의 필요성과 제한된 신경 가설의 실현성은 모두 조건부다.

  [작성 원본](../../agents/09_generative_ai/round05_rebuttal.json)

**최초 입장 원본:**

- [회의적비판자 06_frontier_ai](../../agents/06_frontier_ai/round05_debate.json)

- [제안자 09_generative_ai](../../agents/09_generative_ai/round05_debate.json)

- [데이터통계검토자 10_llm_semantics](../../agents/10_llm_semantics/round05_debate.json)

## 토론으로 실제 바뀐 결정

RP01의 비가역 손실 표현을 철회했다. RP02의 주추정량을 고정 정서 타깃의 조건부 판독 대비로 명확히 했다. RP03의 reset을 실제 인간 소거 기전으로 해석하지 않기로 했다. RP05/06의 확인되지 않은 Horikawa 독립 반복을 착수조건으로 올렸다. RP07은 제안자도 독립 관측/주석 조건을 인정하여 첫3파일럿에서 제외하고 RP08 공간 대비로 교체했다. RP08은 H1/H2/H3를 분리했다. RP09의 비정서를 감독 미사용의 단계적 정의로 좁혔고 RP10은 새 주석/새 BOLD를 필수로 유지했다.

[Round3 실제120개 비판](../round_03/SYNTHESIS.md) → [Round4 실제60개 수정](../round_04/SYNTHESIS.md) → [최종 RQ 반영조건](../../research_questions/round05_amendments.json).
