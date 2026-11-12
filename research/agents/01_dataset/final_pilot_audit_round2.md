# RP03 / PILOT02 최종 자료·통계·자원 계약 감사

판정: **조건부 수정** — medium 4건, low 1건; 통과 6항목. critical/high 없음. 실제 자료 분석 실행 승인을 뜻하지 않는다.

## 수정 요청

### FPA2-01-01 · medium

Fear의 원시간 3초 차분, 평정 지연, scanner/TR 정렬을 구별하지만 1Hz→TR의 실제 관측 연산자는 아직 하나로 고정되지 않았다. 3초를 3TR로 구현하거나 주석과 예측에 HRF를 중복 적용할 여지가 남는다.

**필수 보완:** 1Hz film-time에서 먼저 d_A(t)=A(t)−A(t−3s)를 계산하고 결측/초기 3초를 처리한다. 이후 annotation-lag 부호와 값 선택 범위, scanner onset 이동, TR 대표시각/구간, interpolation 또는 bin/anti-alias 연산자를 명시한다. u_A 적합에 들어가는 TR별 d_A와 feature/state의 HRF/FIR 경로를 각각 식이나 작은 time-index 표로 고정하여 평정 lag와 혈류 지연을 이중 보정하지 않게 한다. 같은 유효 TR 마스크를 모든 head와 loss에 적용한다.

근거/범위: 공식 Fear JSON은 SamplingFrequency=1.0,StartTime=0만 정한다. 3초 차분·scanner 매핑·HRF는 신규 분석계약이다. 기존 원시간 처리 방향을 바꾸라는 요청이 아니라 구현상 두 가지 매핑 가능성을 닫는 요청이다.

위치: pilot:/inputs_outputs/target/time_contract, pilot:/inputs_outputs/alignment

### FPA2-01-02 · medium

random 위치 matching의 duration·경계밀도가 prefix에서 이미 관측된 양인지 사후 전체 사건길이/영화 통계인지 명시되지 않았다. 후자이면 b 자체가 causal이어도 대조 일정은 미래 정보를 사용할 수 있다.

**필수 보완:** online 가지의 matching은 현재까지의 경과시간, 과거 고정 창의 경계밀도, 이미 도착한 오차처럼 time_available≤t인 공변량만 사용한다. 전체 사건길이·영화 전체 경계밀도가 필요한 matching은 retrospective 가지로 명시하고 causal 위치특이 결론과 구분한다. reference 상태뿐 아니라 schedule 생성·matching 각 입력에도 availability를 기록한다.

근거/범위: 기존 treatment 이후 state·test Fear/Y 금지는 적절하지만 자극의 미래 통계도 별도 시간 정보이다. 실제 미래 누수가 발생했다는 판정은 아니다.

위치: pilot:/ablations_controls/reference_matching, pilot:/inputs_outputs/causal_boundary

### FPA2-01-03 · medium

영화 동일가중과 참가자×영화 교차 재표집은 타당한 방향이나 불완전 coverage에서 참가자 가중·동일 셀 집합과 CI의 적합 불확실성 범위가 미정이다. 같은 outer-train을 공유한 OOF 예측값 재표집만으로 전체 학습절차 불확실성을 포함했다고 볼 수 없다.

**필수 보완:** 예를 들어 D=(1/F)Σ_f[1/|S_f|Σ_s∈S_f mean_t d_sft]처럼 실제 관측 셀 및 공통 유효 TR의 가중을 고정하고 비교 head가 같은 셀을 사용하게 한다. 참가자·영화 교차 bootstrap 방법/횟수·빈 셀 처리·95% 구간을 명시한다. 고정 OOF loss를 재표집하면 fitted model에 조건부인 CI라고 표시한다. 전체 학습절차 추론이면 projection/PCA/state/readout/선택을 포함하는 재적합이나 별도 독립 holdout의 범위를 명시한다. 적은 6영화에서 불안정하면 기존대로 동등성 판단을 보류한다.

근거/범위: 6×8은 계획 상한이지 완전 직사각 배열 보장이 아니다. 시간점 독립 bootstrap 금지와 작은 영화 수 경고는 이미 적절하다.

위치: pilot:/evaluation/loss_and_effect/primary, pilot:/evaluation/uncertainty, pilot:/data_and_access/minimum_support

### FPA2-01-04 · medium

120TR smoke와 feature/state 저장량만으로 전체 영화 RNN 학습의 autograd·optimizer·fold/seed 동시 실행 메모리를 제한할 수 없다. 계획은 저장량과 peak를 구분했으나 최대 학습 unroll 및 실행 중단 범위가 아직 미정이다.

**필수 보완:** full BPTT 또는 chunk/TBPTT를 사전 선택하고 최대 unroll·batch·state carry/detach·영화/run 초기화를 정의한다. detach는 기억을 0으로 만드는 reset과 구별한다. 대표 최대 chunk의 학습 peak를 측정하고 32GiB cgroup 아래 실제 여유를 둔 상한/중단 기준과 CPU thread≤4, fold/seed 순차 실행을 지정한다. chunk 변경은 모든 비교 head에 같은 규칙으로 적용하고 test 전 동결한다.

근거/범위: 20,000×512 float32=39.0625MiB 및 state64=4.8828125MiB 저장량 산술은 맞다. 이 수치는 backprop graph 메모리 검증이 아니다.

위치: pilot:/model_and_environment/heads, pilot:/model_and_environment/memory, pilot:/experiment_sequence/1

### FPA2-01-05 · low

단계 A는 shape/timebase/exact-only로 제한되어 있고 test 미사용도 명시되어 있다. 다만 전역 개발 noise/recovery/calibration에 쓴 영화가 이후 LOFO test가 될 수 있는지 운영 기록이 없다.

**필수 보완:** fit-scope 표에 shape-only 공통 QC, outer-fold별 train/inner-validation 수치 선택, 외부 개발용 자료를 구분한다. 6영화 중 한 영화를 전역 수치 조정에 사용하면 이후 독립 test로 세지 않거나 해당 조정을 각 outer-train 안에서 다시 한다. 순수 입력 shape·metadata·동일함수 단위검사는 효과/라벨 튜닝과 구분해 유지한다.

근거/범위: 현재 명시된 train-only 원칙을 뒤집는 결함이나 확인된 누수는 아니다. 코드로 옮길 때 개발이라는 말의 범위를 기록하는 낮은 우선순위 보완이다.

위치: pilot:/data_and_access/planned_subset, pilot:/evaluation/split, pilot:/experiment_sequence/5

## 통과한 계약

- **FPA2-P01** Fear의 1Hz, StartTime=0, high Fearful/low Not Fearful은 로컬에 보관된 공식 개별 recording JSON과 일치한다. 숫자 범위·실제 consensus 값·시점별 평정자수는 확인된 것으로 확대하지 않는다. 직접 읽은 evidence/ds004872/sub-bird/beh/sub-bird_task-AfterTheRain_recording-Fear_stim.json 및 annotation_dictionary.csv. 단일 recording JSON 자체가 consensus 숫자 파일 전체를 검증하는 것은 아니다.
- **FPA2-P02** 보유 진술/공식 메타데이터/실제 미검증 배열/새 manifest를 구분한다. 최대6영화×8명은 계획이며 없는 셀을 만들지 않고 독립 반복·noise ceiling도 가정하지 않는다. 계약과 현재 미실행 상태가 명시되어 있다.
- **FPA2-P03** 현재 프레임 또는 prefix 입력과 legacy full-clip/사후 경계를 분리하고 scanner onset을 annotation StartTime과 구별한다. 실제 제시 모달리티와 미제시 audio도 구분한다. 인과 feature의 기본 범위는 적절하다.
- **FPA2-P04** 같은 theta·rho·h0의 explicit/absorbed 함수 동일성을 과학적 두 모형 차이로 세지 않는다. 같은 입력·관측모형과 별도 최적화 no-reset의 유한예산 해석이 명확하다. 대수적 함수 동일성은 확인했으나 실제 head/HRF 구현은 아직 없다.
- **FPA2-P05** 공통 z_A와 squared loss·δ=.01의 계획적 의미, 양성/음성/동등성/미결정 및 정서 target 유효성 중단 조건이 구분되어 있다. 최소200 복구 seed·검출률 목표는 결과로 주장하지 않는다. 정서 주석은 개인 감정의 직접 참값이 아니다.
- **FPA2-P06** CLIP ViT-B/32 공식 URL/SHA256과 구조 확인, weight 미다운로드·미load·미추론 범위를 정확히 구분한다. 관측4CPU/32GiB와 외부 사용자 장비를 구분한다. 공통 자원 보고서와 일치한다.

## 자료와 검증 범위

실제 뇌·consensus 숫자 배열, 모델 weight load, 학습 및 신경 효과를 실행한 결과는 없다. 통과는 문서 계약과 명시된 메타데이터/작은 합성 검사 범위이다. 전체 artifact SHA256와 위치는 JSON에 보존했다.

