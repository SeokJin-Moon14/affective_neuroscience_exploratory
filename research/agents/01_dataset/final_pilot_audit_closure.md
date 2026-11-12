# 최종 파일럿 자료·통계 계약 감사 종료

**기존 14건 모두 문서상 해소 확인. 미해소 지적과 새 미해결 모순은 없다.** PILOT01 5건·PILOT02 5건·PILOT03 4건의 수정된 제안서, 파일럿 계획, 응답 JSON/Markdown을 직접 대조했다.

이는 문서 계약 기준의 **조건부 실행 준비** 판정이다. 실제 자료 접근·스키마/척도·시간/공간 mapping·checkpoint load·학습·효과·CI·자원 계측 성공을 뜻하지 않는다.

| 기존 지적 | 해소 | 확인한 실제 필드 | 남은 실행 조건 |
|---|---|---|---|
| FPA1-01-01 | 확인 | pilot_PILOT01.json#/hypotheses/H1; pilot_PILOT01.json#/evaluation/statistics/outcome_partition; proposal_RP01.json#/falsifiable_outcomes/mixed | 실제 D_A,D_C,I와 불확실성은 미계산이며 양측 차등성/동등성의 실증 판정은 남는다. |
| FPA1-01-02 | 확인 | pilot_PILOT01.json#/evaluation/statistics/effect_threshold | 0.02는 개발 후 test전 각각 잠글 제안값이다. 생물학적 최소효과의 검증이 아니다. |
| FPA1-01-03 | 확인 | proposal_RP01.json#/computational_framework/model_selection; pilot_PILOT01.json#/evaluation/statistics/learning_curves; proposal_RP01.json#/computational_framework/fit_scope | 실제 family 수로 inner fit/calibration/validation과 학습분율이 성립하는지 확인 필요. 비용 때문에 encoder 재학습을 생략하지 않는다. |
| FPA1-01-04 | 확인 | pilot_PILOT01.json#/evaluation/statistics/uncertainty; pilot_PILOT01.json#/evaluation/statistics/independent_confirmation; pilot_PILOT01.json#/evaluation/statistics/equivalence | OOF는 학습절차 CI가 아니다. H지지·독립성·실제 conditional interval 계산이 미검증이고 사람5명 및 training sample 변동 한계가 남는다. |
| FPA1-01-05 | 확인 | pilot_PILOT01.json#/model_and_environment/resource_execution_contract | 당시 cgroup 잔여량·shape·solver수렴·단계별 peakRSS/시간이 미측정이다. guard도 외부 순간 allocation의 OOM 부재를 보증하지 않는다. |
| FPA2-01-01 | 확인 | proposal_RP03.json#/execution_contract/observation_operator; pilot_PILOT02.json#/inputs_outputs/target; pilot_PILOT02.json#/evaluation/reliability | 실제 TR 대표시각·onset·숫자 annotation·결측 및 연산자 구현은 미검증이다. target/HRF 매핑은 계약이며 실측 생리 사실이 아니다. 실제 training target SD 및 같은 변환 적용·q_A/z_A held-out 관계는 미검증이다. |
| FPA2-01-02 | 확인 | proposal_RP03.json#/execution_contract/prefix_only_matching; pilot_PILOT02.json#/execution_contract/prefix_only_matching | 실제 경계/공변량 available time과 schedule calibration은 실행 때 확인해야 한다. |
| FPA2-01-03 | 확인 | proposal_RP03.json#/execution_contract/cell_weighting_and_conditional_CI; pilot_PILOT02.json#/execution_contract/cell_weighting_and_conditional_CI | 실제 coverage·조건부 bootstrap 안정성은 미검증이다. 전체 학습절차의 CI와 개인 내 반복 신뢰도는 제공하지 않는다. |
| FPA2-01-04 | 확인 | proposal_RP03.json#/execution_contract/training_runtime_budget; pilot_PILOT02.json#/execution_contract/training_runtime_budget | 대표 chunk peak·모델load·실행시간은 아직 측정하지 않았다.24GiB는 사전 중단선이며 실행 성공 보장이 아니다. |
| FPA2-01-05 | 확인 | proposal_RP03.json#/execution_contract/fit_scope; pilot_PILOT02.json#/execution_contract/fit_scope | 실제 fit ledger와 각 fold의 자료 접근은 코드 실행 시 검증해야 한다. test를 본 뒤 조정하면 독립 확증으로 재사용하지 않는다. |
| FPA3-01-01 | 확인 | proposal_RP08.json#/execution_contract/A_B_target_scale_gate; pilot_PILOT03.json#/decision_points/start | 실제 주석 스키마와 정량적 loss 의미 미확인; H3 scale/난도/신뢰도 비교가능성 미검증. |
| FPA3-01-02 | 확인 | proposal_RP08.json#/execution_contract/fixed_spatial_support | 실제 좌표·coverage·W·공통 mapping·공간제약 충족 여부 미검증; native 매핑 없으면 참가자별 Ω_s 범위. |
| FPA3-01-03 | 확인 | pilot_PILOT03.json#/evaluation/effect_CI_contract; pilot_PILOT03.json#/evaluation/conditional_null; pilot_PILOT03.json#/decision_points/equivalence | 실제 independent cluster 수·OOF prediction·coverage 미확인. 사람5명 모집단 및 전체학습절차 CI는 제공하지 않음. |
| FPA3-01-04 | 확인 | pilot_PILOT03.json#/model_and_environment/resource_execution_contract | 실제 baseline memory/workspace/peak·config·projection보존 수치계측 미실행. cap 초과시 scope를 조용히 바꾸지 않고 실행 보류. |

PILOT02 마지막 재확인에서는 새 TR 목표 `q_A`에 validity/reliability 문구를 맞추고 `z_raw`의 train-only 평균·SD 표준화를 명시하도록 기존 FPA2-01-01 안에서 보완했다. 최종 두 문서의 target·loss·execution_contract 일치와 응답 해시를 다시 확인했다.

확인한 필드의 실제 값, 대응 블록 일치 검사, 검토 시점과 12개 문서의 최종 SHA256은 [동명의 JSON](final_pilot_audit_closure.json)에 보존했다. 공유 파일과 Git은 수정하지 않았다.
