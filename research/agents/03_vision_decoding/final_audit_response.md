# Agent03 RP01/PILOT01 최종 독립감사 응답

Agent01의 실제 감사 FPA1-01-01–05를 모두 수용했다. 카드와 파일럿의 대응 계약을 함께 수정했으며 실제 Round5 debate/rebuttal과 카드의 debate_response는 바꾸지 않았다. 이는 후속 감사 수정 기록이다.

## FPA1-01-01 — 수용

수용. 일차 H1=|I|>δ_I로 명시하고 부호별 해석을 나눴다. 공통 상대 손상과 차등 접근성은 배타적이지 않으며, 둘다악화+큰|I|는 혼합으로 기록한다. 같은부호만으로 일반손상 판정하지 않는다.

수정 위치:

- proposal:/proposed_analyses/statistics/primary_estimand
- proposal:/proposed_analyses/statistics/outcome_partition
- proposal:/falsifiable_outcomes
- pilot:/hypotheses
- pilot:/evaluation/statistics/primary_estimand
- pilot:/evaluation/statistics/outcome_partition
- proposal:/smallest_informative_pilot/decision_points/G4–G5
- pilot:/decision_points/G4–G5

남은 조건: 실제 D_A,D_C,I와 불확실성은 미계산이며 양측 차등성/동등성의 실증 판정은 남는다.

## FPA1-01-02 — 수용

수용. exp(D_t)의 기하평균 확률비와 exp(I)의 비의비를 구분했다. δ_I와 원뇌 gate의 δ_signal을 별도 기획 임계로 정의했다.

수정 위치:

- proposal:/proposed_analyses/statistics/effect_threshold
- pilot:/evaluation/statistics/effect_threshold
- proposal:/smallest_informative_pilot/decision_points/G1/G3
- pilot:/decision_points/G1/G3

남은 조건: 0.02는 개발 후 test전 각각 잠글 제안값이다. 생물학적 최소효과의 검증이 아니다.

## FPA1-01-03 — 수용

수용. 전체 pipeline 학습량 축을 택해 fraction/inner fold마다 encoder까지 재학습한다. F_fit/C_calibration/V_validation 역할표와 최종 outer/H fit 경로를 명시했다. pair는 분할 확정 후 내부에서만 생성한다.

수정 위치:

- proposal:/computational_framework/input_preprocessing
- proposal:/computational_framework/model_selection
- proposal:/computational_framework/probe
- proposal:/computational_framework/fit_scope
- proposal:/proposed_analyses/statistics/split
- proposal:/proposed_analyses/statistics/learning_curves
- pilot:/model_and_environment/framework
- pilot:/evaluation/statistics/fit_scope
- pilot:/experiment_sequence/step6

남은 조건: 실제 family 수로 inner fit/calibration/validation과 학습분율이 성립하는지 확인 필요. 비용 때문에 encoder 재학습을 생략하지 않는다.

## FPA1-01-04 — 수용

수용. OOF 재표집을 고정 fitted models/현재 예측에 조건부인 기술 구간으로 한정했다. D20/R60/H20 경로에서 잠근 H를 최종1회 검정하도록 추가했고, H도 재학습 불확실성까지 포함하지 않음을 명시했다.

수정 위치:

- proposal:/proposed_analyses/statistics/uncertainty
- proposal:/proposed_analyses/statistics/independent_confirmation
- proposal:/proposed_analyses/statistics/equivalence
- proposal:/falsifiable_outcomes
- pilot:/evaluation/statistics
- pilot:/decision_points/G4–G5
- pilot:/experiment_sequence/step8

남은 조건: OOF는 학습절차 CI가 아니다. H지지·독립성·실제 conditional interval 계산이 미검증이고 사람5명 및 training sample 변동 한계가 남는다.

## FPA1-01-05 — 수용

수용. 단일프로세스·thread1·workers0 순차 실행, V×V 금지 dual/iterative ridge·block/truncated PCA, 단계별 RSS/cgroup 계측, 명시적 예산/중단선 및 smoke 기반 wall budget을 추가했다.

수정 위치:

- proposal:/computational_framework/resource_execution_contract
- proposal:/smallest_informative_pilot/sequence
- pilot:/model_and_environment/resource_execution_contract
- pilot:/model_and_environment/memory_arithmetic
- pilot:/model_and_environment/runtime
- pilot:/experiment_sequence/step2/step5/step6
- pilot:/decision_points/G3

남은 조건: 당시 cgroup 잔여량·shape·solver수렴·단계별 peakRSS/시간이 미측정이다. guard도 외부 순간 allocation의 OOM 부재를 보증하지 않는다.

## 보존 및 검증

- 두 문서의 data/framework/loss/statistics/sequence/decision_points 일치를 구조 비교로 확인했다.
- Round5 debate/rebuttal JSON·Markdown4개의 전후 SHA256이 동일하고 카드 debate_response도 동일하다.
- 기존 통과7항목의 보유/스키마·공통pair/loss·5명/가짜반복 금지·CLIP미load·A/B단계 구분을 보존했다.
- 현재 원자료/가중치/fit/CI/RSS 실행은 하지 않았으며 실행 준비는 여전히 조건부다.
- 공유 파일·타 역할 문서·Git을 수정하지 않았다.
