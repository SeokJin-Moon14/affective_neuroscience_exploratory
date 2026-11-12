# Agent04 최종 자료·통계 계약 감사 응답

RP08/PILOT03의 기존 계약만 보완했다. 자료/학습/CI 실행 및 감사자 재승인 결과가 아니다. RP05와 기존 Round5 기록은 수정하지 않았다.

## FPA3-01-01 — 수용·문서 계약 수정

A0와 B의 정의·범위·극성·집계·척도·결측/상수를 검사하는 MSE 착수 gate를 공통화했다. nominal/ordinal 임의간격을 금지하고 loss 변경 시δ/H3 재고정을 요구한다.

**수정 위치**

- proposal:/execution_contract/A_B_target_scale_gate
- proposal:/dataset_and_metadata/target_scale_gate
- proposal:/neural_target
- proposal:/proposed_analyses/estimand
- pilot:/execution_contract/A_B_target_scale_gate
- pilot:/data_and_access/target_scale_gate
- pilot:/inputs_outputs/input_shapes
- pilot:/evaluation/primary_loss
- pilot:/decision_points/start

**남은 실행 조건:** 실제 주석 스키마와 정량적 loss 의미 미확인; H3 scale/난도/신뢰도 비교가능성 미검증.

## FPA3-01-02 — 수용·문서 계약 수정

완전 parcel 단위 coverage와 고정Ω·W·빈 parcel/중복/미할당 검사를 추가했다. H2 실제/random은 동일Ω/y/W 완전분할만 허용하고 제약 불가능 시 H2만 보류한다.

**수정 위치**

- proposal:/execution_contract/fixed_spatial_support
- proposal:/computational_framework/projection/support_contract
- proposal:/dataset_and_metadata/fixed_support
- pilot:/execution_contract/fixed_spatial_support
- pilot:/data_and_access/planned_subset/fixed_support
- pilot:/inputs_outputs/projection/support_contract
- pilot:/ablations_controls

**남은 실행 조건:** 실제 좌표·coverage·W·공통 mapping·공간제약 충족 여부 미검증; native 매핑 없으면 참가자별 Ω_s 범위.

## FPA3-01-03 — 수용·문서 계약 수정

일차95% fixed-fitted-pipeline conditional CI와 연결 run/content cluster·2,000회 planned bootstrap을 명시했다. shared training과 학습선택 불확실성 미포함, null재적합과 전체학습재적합의 차이를 기록했다.

**수정 위치**

- proposal:/execution_contract/conditional_CI_and_learning_uncertainty
- proposal:/proposed_analyses/effect_CI_contract
- proposal:/proposed_analyses/inference
- pilot:/execution_contract/conditional_CI_and_learning_uncertainty
- pilot:/evaluation/effect_CI_contract
- pilot:/evaluation/statistics
- pilot:/evaluation/conditional_null
- pilot:/evaluation/minimum_effect_and_equivalence
- pilot:/decision_points/equivalence

**남은 실행 조건:** 실제 independent cluster 수·OOF prediction·coverage 미확인. 사람5명 모집단 및 전체학습절차 CI는 제공하지 않음.

## FPA3-01-04 — 수용·문서 계약 수정

대표block 계측 후 totalpeak≤min(.75L,L−8GiB), 현재32GiB일 때최대24GiB·경고90%·thread총합≤4·순차fit를 정했다. exact whole-parcel weighted accumulation과 동일Ω train PCA로 G/P를 보존한다.

**수정 위치**

- proposal:/execution_contract/measured_resource_and_operator_preservation
- proposal:/computational_framework/resource_execution_contract
- pilot:/execution_contract/measured_resource_and_operator_preservation
- pilot:/model_and_environment/resource_execution_contract
- pilot:/model_and_environment/compute_gate
- pilot:/model_and_environment/memory_plan
- pilot:/inputs_outputs/projection/block_preservation

**남은 실행 조건:** 실제 baseline memory/workspace/peak·config·projection보존 수치계측 미실행. cap 초과시 scope를 조용히 바꾸지 않고 실행 보류.

## 일치·보존 검사

- execution_contract_equal: 통과
- weighted_projection_equal: 통과
- A_B_gate_equal: 통과
- fixed_support_equal: 통과
- paired_loss_equal: 통과
- effect_CI_equal: 통과
- statistics_equal: 통과
- null_scope_equal: 통과
- delta_scope_equal: 통과
- resource_rule_equal: 통과
- protected_files_unchanged: 통과

네 지적을 카드/파일럿 동일계약으로 반영하고 11개 일치/보존 검사를 통과했다. 감사자의 재감사 통과나 실행 준비완료는 주장하지 않는다.

RP05와 실제 Round5 최초 발언·rebuttal 파일은 SHA256으로 변경 없음을 확인했다. 본 로그는 후속 감사에 대한 별도 기록이다.
