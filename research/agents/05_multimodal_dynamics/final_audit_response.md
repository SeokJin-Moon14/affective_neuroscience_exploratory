# RP03 / PILOT02 최종 감사 응답

기존 FPA2-01-01…05의 실행 계약만 수정했다. 실제 자료·모델 실행과 새 연구 확장은 하지 않았다. 두 문서에 동일한 execution_contract를 추가하고 충돌할 수 있는 요약만 갱신했다.

## FPA2-01-01 — 수용·문서 반영 완료

원1Hz 3초 차분, ell의 부호/범위, 공통 target HRF와 후보 state 관측 경로, scanner/TR-bin 적분·공통mask를 고정했다.

수정 위치:
- `agents/05_multimodal_dynamics/proposal_RP03.json#/execution_contract/observation_operator`
- `agents/05_multimodal_dynamics/pilot_PILOT02.json#/execution_contract/observation_operator`

남은 조건: 실제 TR 대표시각·onset·숫자 annotation·결측 및 연산자 구현은 미검증이다. target/HRF 매핑은 계약이며 실측 생리 사실이 아니다.

## FPA2-01-02 — 수용·문서 반영 완료

duration을 prefix 경과시간으로 제한하고 과거60초 밀도·available time 및 순차 schedule을 명시했다. 미래 전체 통계 matching은 online에서 제외했다.

수정 위치:
- `agents/05_multimodal_dynamics/proposal_RP03.json#/execution_contract/prefix_only_matching`
- `agents/05_multimodal_dynamics/pilot_PILOT02.json#/execution_contract/prefix_only_matching`

남은 조건: 실제 경계/공변량 available time과 schedule calibration은 실행 때 확인해야 한다.

## FPA2-01-03 — 수용·문서 반영 완료

실제 S_f/M_sf 셀의 영화·참가자·TR 가중, crossed bootstrap2,000회·빈 셀·95%조건부구간과 소표본 중단을 고정했다.

수정 위치:
- `agents/05_multimodal_dynamics/proposal_RP03.json#/execution_contract/cell_weighting_and_conditional_CI`
- `agents/05_multimodal_dynamics/pilot_PILOT02.json#/execution_contract/cell_weighting_and_conditional_CI`

남은 조건: 실제 coverage·조건부 bootstrap 안정성은 미검증이다. 전체 학습절차의 CI와 개인 내 반복 신뢰도는 제공하지 않는다.

## FPA2-01-04 — 수용·문서 반영 완료

TBPTT64·batch1·state carry/gradient detach·4thread·순차실행·대표 backward peak 및24GiB 중단선을 고정했다.

수정 위치:
- `agents/05_multimodal_dynamics/proposal_RP03.json#/execution_contract/training_runtime_budget`
- `agents/05_multimodal_dynamics/pilot_PILOT02.json#/execution_contract/training_runtime_budget`

남은 조건: 대표 chunk peak·모델load·실행시간은 아직 측정하지 않았다.24GiB는 사전 중단선이며 실행 성공 보장이 아니다.

## FPA2-01-05 — 수용·문서 반영 완료

전역 shape-only QC와 outer train4/validation1/refit5/test1 수치선택을 나누고 전역개발 영화의 제외/재적합 규칙을 명시했다.

수정 위치:
- `agents/05_multimodal_dynamics/proposal_RP03.json#/execution_contract/fit_scope`
- `agents/05_multimodal_dynamics/pilot_PILOT02.json#/execution_contract/fit_scope`

남은 조건: 실제 fit ledger와 각 fold의 자료 접근은 코드 실행 시 검증해야 한다. test를 본 뒤 조정하면 독립 확증으로 재사용하지 않는다.

## 문서 검증

- JSON 파싱, execution_contract 동일성, 중복 target·primary loss 동일성: PASS.
- RP04 및 Round5 최초 입장/응답 JSON·Markdown 해시 무변경: PASS.
- 실제 데이터·모델 검증: 미실행. 실행 준비 완료 또는 Agent01 재감사 통과를 주장하지 않는다.

공통 계약 SHA256: `3c0b911e10f8c15c1813d38d9c03725a55657bc87997261b640926278ddf9f93`

## FPA2-01-01 마지막 중복 요약 정리

- 동일 M_sf의 z_A와 TR 목표 q_A를 비교하며 raw 1Hz d_A와 직접 비교하지 않도록 validity/reliability를 맞췄다.
- z_raw=u_AᵀY 이후 outer-train 평균·SD로 z_A를 표준화하고 모든 head/test에 같은 변환을 고정했다. SD=0이면 보류하며 δ=.01은 이 target의 분산1 MSE 단위다.
- 두 문서의 execution_contract·target·loss 동일성 및 보호 파일 무변경 확인. 실제 자료·모델 실행 없음.
