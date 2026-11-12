# PILOT02. 동일 경계 접근에서 forgetting 좌표와 관측필터를 분리하는 첫 검정

연결: [RP03](https://github.com/SeokJin-Moon14/affective_neuroscience_exploratory/blob/bee5c041fca8ff8a6dcf99c9c8906252c2cbe2a6/research/proposals/RP03.md), RQ18.

**준비 상태:** **plan complete:** True

**execution ready:** False

**data mounted verified:** False

**model loaded:** False

**brain analysis executed:** False

**reason:** 문헌·실제 토론에 기반한 계획 완료다. 보유본 경로/숫자/품질·모델 load·핵심 복구 검증 전 실행 준비 또는 실험 완료로 표시하지 않는다.



이 문서는 파일럿 실행 계획이다. 실험·모델 추론·뇌 분석 결과를 보고하는 문서가 아니다.

## 1. 핵심·경쟁 가설

**H1:** 제한된 동일정보 head family와 학습예산에서 explicit forgetting이 강한 boundary-input no-explicit head보다 고정 Fear 전이 신경대비의 손실을 δ 이상 줄인다.

**H0 alternatives:** - boundary-aware continuous update/readout 또는 finite-window로 충분하다.
- reset 노출·초기상태·유효HRF가 차이를 만든다.
- 서로 다른 hidden state도 HRF 후 같은 관측을 낸다.

**refutation:** 정밀한 동등성/연속모형 우위는 explicit 좌표의 필요성을 낮춘다. exact control 실패·모형복구 실패는 과학H0가 아니라 검정체계 실패다.



## 2. 자료·접근·하위집합

**owned:** Horikawa·Emo-FilM·Mind Captioning·NSD·Spacetop 보유는 사용자 진술. 본 계획 주자료는 Emo-FilM이며 실제 마운트 경로·배열은 미확인.

**official sources:** - https://github.com/OpenNeuroDatasets/ds004892
- https://github.com/OpenNeuroDatasets/ds004872
- https://raw.githubusercontent.com/OpenNeuroDatasets/ds004872/e9b1bf0b05975f7815f2924da16e3ff37111739e/sub-bird/beh/sub-bird_task-AfterTheRain_recording-Fear_stim.json

**actual known:** 외부 consensus14영화/50열/1Hz, Fear high/low 정의 및 annotation StartTime=0, fMRI30명/주석44명은 기존 감사 범위다. 실제 TR·coverage·척도·반복은 아직 확인하지 않았다.

**planned subset:** 단계A: QC로 선택한1영화의 warm-up 이후 유효120TR로 shape/timebase/exact-control만 확인. 단계B: valid onset·stimulus·Fear 존재를 기준으로 최대6영화×8참가자; 먼저 coverage가 넓은 영화, 동률이면 film ID, 참가자는 coverage 후 ID로 선정한다. Y–Fear 상관·모델 성능으로 선정하지 않는다. 관측된 participant×film 셀만 사용하고 없는 셀을 만들지 않는다. 단계A는 shape-only로 로그를 남기며, noise/recovery/effect 조정에 사용했다면 execution_contract.fit_scope의 전역개발 제외 규칙을 적용한다.

**minimum support:** 6영화의 test1·validation1·train4 구조와 실제 관측 coverage를 확인한다. S_f 및 공통 TR 마스크는 execution_contract의 규칙으로 고정하고 모든 head에 같은 셀을 쓴다. 빈 셀을 보간하지 않으며 영화 하나의 S_f가 비면6영화 비교를 강행하지 않는다. 조건 미충족 시 계약/합성 검증까지만 수행한다.

**new manifest:** source_path/hash, subject/film/run, scanner_onset_s, TR_s, observed_modality, feature support, time_available_s, b_source/available_s, split를 검증해 만드는 분석계약이다. 실제 원컬럼처럼 가장하지 않는다.

**repetition limit:** 동일영화 개인 내 독립반복은 현재 미확인이고 요구된 기본가정이 아니다. 원평정이 있을 때만 평정자분할 신뢰도. 개인 반복 noise ceiling과 참가자 간 일치는 구별한다.

**audio:** 첫 시간검정은 실제 시각입력으로 가능하다. audio를 추가하려면 음원 존재와 스캐너 내 실제 청각 제시를 별도 확인하며 미제시 오디오는 배제한다. Speech Features는 제외.

**privacy:** 원본·개인별 숫자자료·새 개인정보를 공개 백업에 업로드하지 않는다. 계획과 허용된 aggregate/코드만 결과물로 검토한다.



## 3. 모델·체크포인트·자원

**current:** 공통 보고서의 cgroup4CPU·32GiB, GPU load/추론 성공 미확인. 사용자 다른 장비 자원에 대한 단정은 하지 않는다.

**cache first:** time_available과 추출 모델이 검증된 고정 feature cache가 있으면 먼저 사용한다. legacy full-clip feature는 retrospective로 분리한다.

**checkpoint:** **name:** OpenAI CLIP ViT-B/32

**canonical id:** P079

**code url:** https://github.com/openai/CLIP/blob/main/clip/clip.py

**weights url:** https://openaipublic.azureedge.net/clip/models/40d365715913c9da98579312b702a82c18be219cc2a73407c4526f58eba950af/ViT-B-32.pt

**sha256:** 40d365715913c9da98579312b702a82c18be219cc2a73407c4526f58eba950af

**license url:** https://github.com/openai/CLIP/blob/main/LICENSE

**verified scope:** 공통 자원계획이 loader·공식 URL/해시·MIT 코드 LICENSE를 확인했다. 가중치 다운로드/load/추론·본 환경 peak 메모리는 미확인. 라이선스·원자극 사용조건은 실제 실행 전 재확인.

**expected output:** 공식 구조상 ViT-B/32 image embedding 512차원을 예상하되 smoke test로 확인; state model이나 audio encoder가 아니다.

**extraction:** 계획은 1Hz 시점 t의 현재 프레임 한 장→ViT-B/32 embedding. decoder/frame sampling이 t 이후 프레임을 고르지 않게 한다. 연속 prefix head가 시간정보를 담당한다. d_X=512를 예상하되 실제 smoke test shape로 계약을 고정한다.

**heads:** train PCA≤32, state64 tanh RNN을 첫 신규 head로 구현할 계획이다. 같은 x_t,b_t로 next-feature MSE 학습; train epochs cap50, validation patience5, seeds[0,1,2]를 초기 제한으로 둔다. 모든 후보의 동일예산 검토 후 test 전 동결한다. h0/rho 선택은 inner split만. checkpoint는 새로 학습할 예정이며 현재 존재하지 않는다. 학습은 execution_contract.training_runtime_budget의 TBPTT64스텝·batch1·state carry/detach를 사용하며 full-film BPTT는 하지 않는다.

**state readout separation:** state는 비정서 자극 예측만으로 학습하고 neural readout은 별도 inner fitting이다. next feature는 학습 target으로만 쓰고 test state input은 x_≤t다.

**memory:** 가령 T=20,000 float32일 때512차원 feature≈39.06MiB,64차원 state≈4.88MiB. 원본·voxel·복사·autograd·model weights 제외다. actual peak를 단계A에서 측정한다. GPU VRAM·벽시계시간은 미확인. 학습 autograd/optimizer peak는 별도 대표 chunk에서 측정한다. 전체 cgroup24GiB 상한·8GiB 여유, thread≤4, fold/seed/model 순차 실행과 공통 unroll 축소 규칙은 execution_contract에 따른다.

**expansion:** Mamba/PredNet/VideoPrism은 공식코드 근거만 있는 확장경로이며 첫파일럿에 필수 아니다. cache/작은head로 복구가 실패하면 대형모델로 자동확장하지 않는다.



## 4. 입력·출력과 정렬

**input arrays:** 영화별 시각 cache X_f[T_feat,512 예상], boundary b_f[T_feat,1], times/available[T_feat], participant-run BOLD Y_sfr[T_TR,P], Fear E_f[T_ann,1]. T_feat는1Hz 계획, T_TR는실제TR, P는보유공간/독립parcellation 확인 뒤 고정하며 숫자를 임의로 확정하지 않는다.

**target:** **annotation:** Fear: high=Fearful, low=Not Fearful; 1초 consensus 포함은 공식 JSON/기존 사전에서 확인. 숫자 범위·개별 평정수·신뢰도는 미확인.

**annotation source:** https://raw.githubusercontent.com/OpenNeuroDatasets/ds004872/e9b1bf0b05975f7815f2924da16e3ff37111739e/sub-bird/beh/sub-bird_task-AfterTheRain_recording-Fear_stim.json

**primary contrast:** 원 film-time 1Hz에서 먼저 d[n]=A[n]−A[n−3]의 3초 차분을 계산한다. 초기3초·결측은 무효이며 3TR 차분이 아니다. 이후 train-only 표준화·ell 이동·공통 H_ref·TR-bin 적분을 execution_contract.observation_operator 순서대로 적용한다. Fear가 상수/불량이면 다른 라벨로 test 최적 교체하지 않는다.

**neural:** outer train의 공통 Y와 q_A,j=R_j[H_ref*e_ell]로 u_A를 적합한다. z_raw,j=u_AᵀY_j로 계산한 뒤 z_A,j=(z_raw,j−mu_outer_train)/sd_outer_train으로 표준화한다. 평균과 SD는 outer-train에서만 적합해 모든 head와 test에 같은 변환으로 고정하며 train SD=0이면 보류한다. δ=.01은 이 train 분산1 target의 MSE 단위다. inner selection→outer refit의 범위는 execution_contract.fit_scope에 따른다. z_A/Y에 HRF를 다시 적용하지 않는다.

**time contract:** 원1Hz 차분→평정지연 ell(양수는 늦은 평정을 앞선 자극으로 매핑)→공통 H_ref 1회→scanner/TR-bin 적분으로 q_A를 만든다. state 예측은 별도 H_m/FIR 1회 경로다. 각 경로에 HRF/lag를 중복 적용하지 않고 모든 head에 같은 유효 TR 마스크를 쓴다. 상세 식·부호·범위는 execution_contract.observation_operator에 고정했다.

**validity:** 동일 공통 유효 TR 마스크 M_sf에서 z_A와 TR 관측목표 q_A의 held-out 관계를 별도로 확인하되 그 결과로 projection/라벨을 다시 고르지 않는다. raw 1Hz d_A와 z_A를 직접 비교하지 않는다. 현재 동일 영화 개인 내 반복은 미확인이다. 반복 신뢰도·noise ceiling은 가정하지 않으며 원평정이 있을 때만 평정자 split 신뢰도를 추정한다.

**output arrays:** head H_mf[T_feat,64]→원시간 HRF/FIR→Zhat_m,sfr[T_TR,1]; 고정 Z_sfr[T_TR,1]와 paired loss[T_TR,1]. 전체Y 예측은 보조.

**alignment:** execution_contract.observation_operator의 tau_j/TR-bin·film onset·zero-order hold·0.1초 적분 규칙을 적용한다. volume 대표시각 계약을 확인할 수 없으면 임의 정렬하지 않는다. target와 prediction 경로는 각각 한 번의 관측 연산이며 이중 HRF/lag 보정은 금지한다.

**causal boundary:** 독립 prefix 경계 annotation/비정서 causal detector가 있으면 b를 사용한다. full-film 사후 boundary만 있으면 online branch는 착수하지 않고 retrospective로 분리한다. 단순 임베딩 변화 detector를 쓰는 fallback은 representation-change 경계 방법검정이며 인간 사건경계로 이름 바꾸지 않는다. matching/schedule도 execution_contract.prefix_only_matching의 available_time≤t 제약을 만족해야 한다. 완료 사건 duration과 영화 전체 밀도는 online schedule에 쓰지 않는다.

**buffer:** feature 최대과거 support+HRF/FIR support+boundary 검출지연의 합으로 경계buffer를 계산한다. run초기화·인위적 clip 경계와 자연경계를 분리한다.



## 5. 실험 순서

- **step:** 1
  
  **action:** manifest/실제시계열 확인
  
  **output:** 읽기전용 local경로·hash·coverage·TR/onset·Fear 숫자/극성·제시모달리티·결측 기록. 원자료 미확인 필드를 추정으로 채우지 않음.
- **step:** 2
  
  **action:** 작은120TR 계약·체크포인트 검사
  
  **output:** cache provenance/공식 weight hash·한 입력 shape/finite 검사와 합성 입력 최대 chunk의 forward/backward/optimizer peak를 확인한다. TBPTT·순차 실행·24GiB 중단선은 execution_contract를 따른다. 실측·load 성공은 아직 미확인.
- **step:** 3
  
  **action:** target와 split 고정
  
  **output:** execution_contract의 원1Hz 차분·ell 부호·HRF/TR 연산·공통mask 및 fold fit-scope를 고정한다. shape-only 단계A와 수치개발 자료를 분리한다.
- **step:** 4
  
  **action:** 비학습·선형 기준
  
  **output:** 현재프레임+경계 ridge/FIR, 단순 causal mean/finite-window/generic decay. 훈련 공통scale와 loss 확인.
- **step:** 5
  
  **action:** exact functional audit
  
  **output:** 같은 theta/h0/rho의 explicit/absorbed 경로, state/예측 및 HRF후 출력 동등 확인. 차이나면 과학비교 중단.
- **step:** 6
  
  **action:** HRF 이후 복구·거짓양성 calibration
  
  **output:** 각 outer-train 안에서만 상태/경계지연/HRF 복구와 noise calibration을 시행할 계획이다. 전역 조정 영화는 test에서 제외하거나 fold 안에서 재적합한다. 실제 결과는 없다.
- **step:** 7
  
  **action:** 동일정보 모형 적합·고정
  
  **output:** state/readout 모두같은 b를 받는 제한된 head, explicit hard/soft, randomschedule·노출 통제. A/Y는state학습에 주지 않으며 test 최적모형을 고르지 않음.
- **step:** 8
  
  **action:** 독립영화 평가
  
  **output:** primary paired risk·영화/참가자별효과·공통고정HRF 및 후보별재적합HRF·비정서/전체Y 보조결과. 예상결과를 실제성과처럼 쓰지 않음.
- **step:** 9
  
  **action:** 결정과 재현성
  
  **output:** δ/CI·복구·timing게이트에 따라 확대/수정/중단. config·seed·hash·허용 aggregate를 저장하되 새 원자료/개인정보 공개업로드 금지.


## 6. 평가·통계

**loss and effect:** **primary:** d_sft=(z_sft−pred_no_explicit_sft)^2−(z_sft−pred_forgetting_sft)^2; D=(1/F)Σ_f[(1/|S_f|)Σ_{s∈S_f}(1/|M_sf|)Σ_{t∈M_sf}d_sft]. 영화는 동일 가중, 영화 안 관측 참가자는 동일 가중, 셀 안 공통 TR은 동일 가중이다. 모든 영화의 S_f·유효 TR 수를 공개한다.

**secondary:** matched-random forgetting 대비 위치특이 손실차, 전체 Y 손실, 비정서 z_C 대비는 별도 보고. 같은 함수 exact control은 독립 모델 증거로 세지 않는다.

**minimum effect:** 계획용 δ=0.01: train에서 분산1로 표준화한 z_A의 MSE를 0.01 줄이는 효과, 즉 train target variance 1%에 해당한다. 생리적 임계치나 알려진 임상효과가 아닌 사전 의사결정 해상도다. δ=0.005/0.02 민감도를 함께 고정한다. test 전 개발 신뢰도·복구로 이 해상도를 판정할 수 없으면 확증/동등성 판단을 보류한다.

**decision:** 95% 조건부 cluster 구간 하한>δ이면 고정 적합모형 범위의 확대 검토 근거, 전체 구간이 [−δ,+δ] 안이면 해당 범위의 실용 동등성으로만 해석한다. 이는 전체 학습절차 불확실성이 아니다. execution_contract의 coverage/재표집 안정성 게이트가 실패하면 동등성·확대 판정을 보류한다.

**split:** execution_contract.fit_scope의 shape-only 전역 QC와 fold별 수치적합을 분리한다. 6-film LOFO는 train4/validation1/test1, 선택 후 outer train5 refit이다. 전역 noise/recovery 조정에 사용한 영화는 독립 test에서 제외하거나 해당 조정을 fold train 안에서 다시 수행한다.

**reliability:** raw ratings 존재 시 평가자 분할로 Fear 전이 안정성을 추정한다. consensus만 있으면 lag/평활도 오차 민감도를 보고하고 측정오차를0으로 두지 않는다. 개인 반복 미확인으로 repeat noise ceiling을 만들지 않는다. 동일 M_sf에서 고정 z_A와 TR 관측목표 q_A의 held-out 관계가 성립하지 않으면 정서 해석을 중단한다. raw 1Hz d_A와 z_A를 직접 비교하지 않는다.

**uncertainty:** execution_contract.cell_weighting_and_conditional_CI의 실제 셀 가중·2,000회 crossed cluster 재표집·빈 셀 처리·95% percentile을 적용한다. 고정 OOF loss이므로 fitted models/targets에 조건부인 CI다. 전체 학습절차 불확실성을 포함했다고 하지 않으며 소수 영화 불안정 시 동등성 판단을 보류한다.

**multiplicity:** 주비교1개·Fear1개·u_A target1개. random위치·HRF민감도·비정서/ROI분석은 사전 부차family로 나누고 필요시 Holm보정. 여러 관측모형 중 유리한 결과만 제시하지 않는다.

**recovery decisions:** 복구·noise calibration은 각 outer fold의 train/inner-validation 안에서만 수행한다. exact control은 수치 동등해야 한다. 최소200개 개발 seed에서 δ 신호의 검출률·영효과 false positive와 이항구간을 보고한다. 검출률80%/false positive5%는 목표이며 실제 결과가 아니다. 전역 개발 영화의 test 제외와 조건부 CI 범위를 execution_contract에 따른다.



## 7. Ablation·대조

**exact function:** **identity:** explicit: h_t=F_theta((1−rho_t)h_prev+rho_t*h0,x_t); absorbed: F_tilde_theta(h,x,b)=F_theta((1−rho(b))h+rho(b)*h0,x). 동일 theta,h0,rho,입력,seed와 readout이면 동일 함수다.

**test:** 학습 없는 동일 가중치 복사와 고정 test 입력에서 state·출력·HRF 후 예측을 비교한다. float32 기준 atol=1e−5,rtol=1e−4를 계획값으로 두고 정규화된 출력이 이를 넘으면 구현/수치 문제를 먼저 해결한다.

**interpretation:** exact control은 기전 검증이 아니라 구현 감사다. 통과하면 하나의 관측 동치류로 묶고, 이 둘의 신경 점수 차이는 과학결과로 쓰지 않는다. 제한된 별도 학습 no-explicit-reset 함수족과의 차이는 parameterization/최적화/자료효율을 포함한 유한예산 효용이다.

**same information:** 주비교의 모든 모형에 state update와 readout 양쪽으로 x_t, b_t, 같은 초기 시점을 제공한다. readout-only 2×2는 보조 ablation이며 모형 전체의 경계정보 유무로 명명하지 않는다.

**reference matching:** execution_contract.prefix_only_matching에 따라 비개입 reference 사전 state, 현재까지 경과시간, 과거60초 가용 경계밀도와 이미 도착한 오차만 사용한다. 처리 후 state·test Fear/Y·완료 사건길이·미래 전체 통계는 online matching에서 제외한다.

**observation:** 단일 고정 HRF 결과와 동일 family 안에서 각 후보의 train nuisance를 최적화한 결과를 모두 보존한다. zero-phase 필터·미래 caption·미래 clip 특징은 causal 모형에서 금지한다.

**function budget:** 같은 state 폭·학습목적·자료·seed·탐색 예산을 적용하고 train-fit h0·soft rho·reset exposure를 표로 남긴다. exact 동치류는 한 모형으로 집계한다.

**sensory semantic:** 현재 장면·motion·cuts·비정서 사건 의미·경계밀도와 유한창 기준을 비교한다. audio를 포함하면 실제 제시된 음악·환경음만 사용한다.



## 8. 확대·수정·중단 기준

- **gate:** 계약
  
  **expand:** 실제 timebase·target·feature available time·presentation 확인
  
  **revise:** 오디오 미확인 시 시각만의 시간검정; 사후 경계는 별도 retrospective 분석
  
  **stop:** 연속 BOLD 또는 Fear 원숫자 정렬이 없으면 해당 신경검정 중단
- **gate:** 함수 동등성
  
  **expand:** exact control의 수치 동등성 확인
  
  **revise:** readout·수치·구현 차이의 원인 수정
  
  **stop:** 동등 통제의 불일치를 해결하기 전 과학 비교 금지
- **gate:** 관측 후 복구
  
  **expand:** δ 규모의 구별 가능한 모형쌍과 영효과 calibration을 충분한 정밀도로 확인
  
  **revise:** 구별 불가능한 모형은 동치류로 묶거나 정서 시간 해석을 축소
  
  **stop:** 모든 기전이 HRF 후 구별 불가능하면 큰 모델 확장 중단
- **gate:** 실자료
  
  **expand:** 고정 fitted model에 조건부인 D의95% cluster CI 하한>δ, 영화별 방향 견고성 및 고정 정서대비 검증이 있을 때만 확대를 검토한다. 전체 학습절차 확증으로 해석하지 않는다.
  
  **revise:** 전체 Y만 개선되면 일반 경계모형; HRF 재적합 후 소멸하면 관측필터 설명
  
  **stop:** 95% CI 전체가 ±δ 안이면 explicit 좌표의 우선성을 낮춤. 넓은 CI는 기각이 아닌 미결정


## 9. 실패 가능성과 주장 한계

- exact 흡수 함수가 존재하므로 전체 함수족에서 신경 forgetting 기전의 고유 필요성을 증명할 수 없다.
- 별도 코호트의 Fear consensus는 개별 fMRI 참가자의 연속 정답이 아니다.
- 독립 반복이 확인되지 않은 자료의 개인 내 신뢰도·noise ceiling을 확정하지 않는다.
- 모델 내부 reset·audio 제거는 인간 기억 삭제·모달리티 차단 실험이 아니다.
- Spacetop 사후 clip 평정·NSD 정적 시행으로 연속 Fear 전이 정답을 만들지 않는다.
- 6영화 파일럿의 CI·복구 추정 불안정은 계획 수정 또는 자료 확대의 조건이다.
- 신규성은 P066 직접 비교 및 제한적 코퍼스 역검색 범위다. 외부 CONNECT403 때문에 전면 확인하지 못했다.


## 최종 감사로 확정한 실행 계약

**version:** FPA2-01-final-20261112

**execution status:** 문서 계약만 수정; 실제 자료·모델·검정 미실행

**observation operator:** **audit id:** FPA2-01-01

**native difference:** 원 film-time 1Hz의 A[n]에서 d[n]=A[n]−A[n−3]을 먼저 계산한다. 3은 3초이며 3TR이 아니다. n<3 및 어느 원소든 결측이면 무효다. 표준화 계수는 outer-train에서만 적합한다.

**lag sign:** 평정지연 ell∈{0,2,4}초를 inner train/validation에서 선택한다. 양의 ell은 평정이 자극보다 늦었다는 뜻으로, 자극시간 s의 주석은 e_ell(s)=d(s+ell)에 대응한다. 이는 사후 평가주석 매핑이며 모형 입력이나 경계 검출에 주지 않는다.

**continuous time:** d[n]은 [n,n+1)에서 값을 유지하는 zero-order hold로 연속화한다. 0.1초 공통 격자에서 아래 인과 convolution 및 TR-bin 적분을 계산한다. 결측을 보간하거나 미래 값으로 채우지 않는다.

**scanner TR operator:** 실제 preprocessing의 volume 대표시각 tau_j와 TR_j, 실제 film onset o를 확인한다. 대표시각 계약이 없으면 정렬을 추정하지 않고 중단한다. B_j=[tau_j−TR_j/2,tau_j+TR_j/2), R_j[g]=(1/TR_j)∫_{B_j}g(v−o)dv로 고정한다. boxcar 적분은 명시한 관측 근사이며 별도 zero-phase 필터를 추가하지 않는다. 예측 관측값의 available time은 bin 끝으로 표기하고 midpoint 실시간 예측이라고 주장하지 않는다.

**target path:** q_A,j=R_j[H_ref*e_ell]. H_ref는 인과 double-gamma [Gamma(shape6,scale1)−Gamma(shape16,scale1)/6]를 0–32초에서 면적1로 정규화한 공통 고정 kernel이다. 이것은 분석계약이며 실측 HRF 사실이 아니다. u_A는 훈련 Y→q_A의 ridge로 정하고 z_raw,j=u_A^T Y_j에서 train-only 표준화한 z_A,j를 모든 head의 같은 신경 표적으로 쓴다. z_A 또는 Y에 HRF를 다시 적용하지 않는다. z_raw,j=u_AᵀY_j로 계산한 뒤 z_A,j=(z_raw,j−mu_outer_train)/sd_outer_train으로 표준화한다. 평균과 SD는 outer-train에서만 적합해 모든 head와 test에 같은 변환으로 고정하며 train SD=0이면 보류한다. δ=.01은 이 train 분산1 target의 MSE 단위다.

**prediction path:** 각 causal head의 h_m(s)는 s까지의 자극만 사용한다. p_m,j=readout_m(R_j[H_m*h_m])로 feature/state 경로에서 HRF/FIR를 정확히 한 번만 적용한다. H_m의 family·최대 support32초·선택 예산은 동일하며 각 outer train에서만 적합한다. FIR가 선택되면 HRF convolution 대신 사용하고 둘을 직렬로 적용하지 않는다. annotation ell을 feature/state 경로에 재적용하지 않는다.

**common mask:** 모든 head·허용 ell·관측 kernel의 최대 support에 대해 원주석·feature·Y QC가 유효한 TR 교집합 M_sf를 fitting 전에 만든다. 초기3초, 필요한 convolution support, 영화 끝의 ell 확보, run/boundary buffer를 반영한다. 같은 M_sf를 모든 loss에 적용하고 head별로 유리한 TR을 제거하지 않는다.

**index example:** 가상 예: 원주석 n=10의 차분은 A[10]−A[7]. ell=2이면 film s=8에 대응하고 onset100이면 scanner108이다. 이후 H_ref의 6초 지연 성분은 scanner114에 기여한다. TR2초·대표시각114라면 [113,115) bin에 적분한다. 실제 TR이나 효과를 측정한 예가 아니다.

**prefix only matching:** **audit id:** FPA2-01-02

**allowed covariates:** online matching에는 현재까지 run 경과초, 마지막으로 가용해진 경계 이후 경과초, [t−60,t) 고정 과거창의 가용 경계 수/실제 관찰 창길이, 공통 비개입 reference의 사전 state norm·age, t까지 도착한 예측오차, 현재 관찰 가능한 cut/motion/onset만 쓴다. duration은 완료 사건길이가 아니라 경과시간이다.

**availability:** 공변량·reference state·matching/schedule 출력마다 time_available을 저장하고 online 가지에서는 모두 ≤t인지 확인한다. treatment 이후 state와 test Fear/Y는 사용하지 않는다.

**schedule:** 훈련 영화의 prefix 공변량으로만 random schedule의 hazard/층별 발생률을 적합하고 test에서는 고정된 규칙과 사전 seed의 순차 Bernoulli draw로 위치를 정한다. test 영화의 미래 경계 총수·전체 길이를 보고 횟수를 정확히 맞추거나 schedule을 사후 재선택하지 않는다. 실현 횟수/겹침 차이는 진단으로 보고한다.

**retrospective limit:** 완료 사건길이·영화 전체 경계밀도·전체 경계 수에 맞춘 일정은 retrospective로 표기하며 online 위치특이 주검정에 포함하지 않는다. 현재 계약에서 이를 추가 연구로 확장하지 않는다.

**cell weighting and conditional CI:** **audit id:** FPA2-01-03

**cell set:** S_f는 해당 outer fold의 train/validation/test coverage와 사전 QC·공통 유효 TR M_sf를 충족하는 실제 참가자 집합이다. 없는 셀은 보간하지 않는다. 모든 비교 head에 동일 S_f,M_sf를 적용한다. 수치 실패 head는 비교를 중단/수정하며 해당 head에 유리하게 셀을 제외하지 않는다.

**estimand:** d_sft=(z_sft−pred_no_explicit_sft)^2−(z_sft−pred_forgetting_sft)^2; D=(1/F)Σ_f[(1/|S_f|)Σ_{s∈S_f}(1/|M_sf|)Σ_{t∈M_sf}d_sft]. 영화는 동일 가중, 영화 안 관측 참가자는 동일 가중, 셀 안 공통 TR은 동일 가중이다. 모든 영화의 S_f·유효 TR 수를 공개한다.

**bootstrap:** 고정 OOF cell loss에 대해 영화 F개와 전체 관측 참가자 집합의 ID를 각각 독립 복원추출하는 crossed cluster bootstrap을 2,000회 계획한다(seed20261112). 참가자 중복수로 각 영화의 관측 셀 가중을 계산하고 영화 중복수로 평균한다. 선택 영화에서 관측 참가자 가중 합이0이면 그 replicate 전체를 다시 뽑으며 빈 셀을 만들지 않는다. 최대20,000회 시도와 무효 비율을 기록한다.

**interval scope:** 유효 replicate의 2.5/97.5 percentile을 95% 구간으로 보고한다. u_A/PCA/state/readout/lag/HRF/선택·schedule을 재적합하지 않으므로 이는 이미 적합된 fold별 모형과 target에 조건부인 cluster 구간이다. 겹친 outer-train의 학습절차 변동이나 전체 procedure 불확실성을 포함했다고 하지 않는다.

**instability:** 유효2,000회 미달, 무효 replicate>5%, 단일 영화 영향으로 결론 변경 등 소표본 불안정이면 CI 기반 동등성/확대 판정을 보류하고 영화별 효과만 보고한다. 6영화의 한계를 반복시점 수로 보충하지 않는다. 전체 학습절차의 추론에는 모든 적합단계 재실행 또는 독립 holdout이 필요하지만 이번 문서 수정에서는 새 분석으로 추가하지 않는다.

**training runtime budget:** **audit id:** FPA2-01-04

**unroll:** full-film BPTT 대신 TBPTT를 고정한다. 1Hz feature 기준 최대 unroll64스텝, batch1 영화 chunk, 마지막 짧은 chunk 허용. 동일 영화/run 안에서는 수치 state를 다음 chunk로 carry하되 chunk 경계에서 autograd만 detach한다. detach는 state를0으로 만드는 reset이 아니다. 영화/run 시작에서만 공통 초기화하고 명시적 forgetting은 각 모형 정의대로 적용한다.

**execution:** 동결 backbone 특징은 autograd 없이 cache한다. optimizer/gradient graph는 chunk 단위로 해제한다. fold·seed·모형은 순차 실행하며 동시에 학습하지 않는다. torch/BLAS intra-op thread≤4, inter-op1, DataLoader worker0으로 제한한다.

**measurement:** 합성 입력의 대표 최대64스텝 chunk에서 forward+backward+optimizer step의 process 및 cgroup memory peak를 측정한 뒤 전체 학습 여부를 정한다. feature/state 저장량 산술은 학습 peak 검증이 아니다. 입력 shape 외 실제 test 수치로 자원 설정을 튜닝하지 않는다.

**stop line:** 32GiB cgroup에서 전체 사용량 peak24GiB 이하와 최소8GiB headroom을 요구한다. 측정/실행 중24GiB 도달 또는 OOM이면 학습을 중단한다. CPU4분량을 넘는 병렬 fold/seed를 허용하지 않는다. watchdog/step 경계 관측은 순간 peak를 완전 보장하지 못하므로 실제 peak 기록을 남긴다.

**fallback:** 자원 실패 시 test 평가 전에 모든 head 공통으로 unroll32, 이후16 순으로만 낮춰 대표 chunk를 재측정한다.16에서도 실패하면 RNN 비교를 중단하고 계약/cache 단계만 남긴다. 선택된 unroll·batch·detach 규칙은 모든 비교 head와 fold에서 같게 동결하며 memory를 지운 것으로 해석하지 않는다.

**fit scope:** **audit id:** FPA2-01-05

**global shape only:** 공통 QC는 파일/ID·shape·TR/onset·결측 존재·제시 modality·체크포인트 hash·한 입력 finite/shape 및 합성입력 exact-function 단위검사까지만 허용한다. 단계A120TR이 나중 test 영화에 속해도 effect·라벨 관계·noise·lag·threshold·모형 선택에 쓰지 않으면 shape-only 로그로 남긴다.

**outer fold:** 6영화 LOFO에서 test1을 완전히 잠그고 outer train5 중 ID 규칙으로 validation1/train4를 정한다. 표준화·PCA·u_A·annotation ell·boundary threshold/hazard·noise/recovery calibration·state/readout·HRF 선택은 이 train4/validation1 안에서 수행한다. 선택규칙 고정 후 outer train5로 재적합하고 test 영화에서는 한 번 평가한다.

**scope ledger:** 모든 fit 객체에 source_film_ids, subject_ids, stage(shape_only/inner_train/inner_validation/outer_refit/test), target_used, config_hash를 기록한다. held-out 영화가 다른 outer fold에서 training인 일반 LOFO와 같은 fold의 test 누수를 구별한다.

**global development:** 기본 계획에는 전역 수치 조정용 영화를 두지 않는다. 한 영화를 전역 noise/recovery/threshold/effect 조정에 사용했다면 그 영화는 모든 독립 test 집계에서 제외해 외부개발로 표시하거나 그 조정을 각 outer train 안에서 처음부터 다시 수행한다. 단계A라는 이름만으로 개발 사용을 면제하지 않는다.

**no post test revision:** δ·수치 tolerance·TBPTT 및 절차는 test 전 고정한다. test 결과 뒤 변경이 필요하면 해당 결과는 탐색으로 표시하고 같은 test를 독립 확증으로 재사용하지 않는다.



## 근거

- [P002 Emo-FilM: A multimodal dataset for affective neuroscience using naturalistic stimuli](https://doi.org/10.1038/s41597-025-04803-5) · [실제 확인 출처](https://raw.githubusercontent.com/OpenNeuroDatasets/ds004892/cdf68fe448ad180a476fa2371473a1a6ed063774/dataset_description.json)
- [P066 Discovering event structure in continuous narrative perception and memory](https://doi.org/10.1016/j.neuron.2017.06.041) · [실제 확인 출처](https://github.com/brainiak/brainiak/blob/master/src/brainiak/eventseg/event.py)
- [P089 Deep Predictive Coding Networks for Video Prediction and Unsupervised Learning](https://arxiv.org/abs/1605.08104) · [실제 확인 출처](https://github.com/coxlab/prednet)
- [P034 Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://arxiv.org/abs/2312.00752) · [실제 확인 출처](https://github.com/state-spaces/mamba)
- [P044 VideoPrism: A Foundational Visual Encoder for Video Understanding](https://arxiv.org/abs/2402.13217) · [실제 확인 출처](https://github.com/google-deepmind/videoprism)
- [P079 Learning Transferable Visual Models From Natural Language Supervision](https://raw.githubusercontent.com/mlresearch/v139/gh-pages/radford21a/radford21a.pdf)
- [P100 Statistical inference on representational geometries](https://doi.org/10.7554/eLife.82566) · [실제 확인 출처](https://elifesciences.org/articles/82566)
- [P101 Representational models: A common framework for understanding encoding, pattern-component, and representational-similarity analysis](https://doi.org/10.1371/journal.pcbi.1005508) · [실제 확인 출처](https://github.com/rsagroup/rsaModelComparison)
- https://github.com/openai/CLIP/blob/main/clip/clip.py
- https://openaipublic.azureedge.net/clip/models/40d365715913c9da98579312b702a82c18be219cc2a73407c4526f58eba950af/ViT-B-32.pt
- https://github.com/openai/CLIP/blob/main/LICENSE
- https://raw.githubusercontent.com/OpenNeuroDatasets/ds004872/e9b1bf0b05975f7815f2924da16e3ff37111739e/sub-bird/beh/sub-bird_task-AfterTheRain_recording-Fear_stim.json

작성 원본: [05_multimodal_dynamics](https://github.com/SeokJin-Moon14/affective_neuroscience_exploratory/blob/bee5c041fca8ff8a6dcf99c9c8906252c2cbe2a6/research/agents/05_multimodal_dynamics/pilot_PILOT02.json). [공통 자원·모델 근거](https://github.com/SeokJin-Moon14/affective_neuroscience_exploratory/blob/bee5c041fca8ff8a6dcf99c9c8906252c2cbe2a6/research/pilots/RESOURCE_AND_MODEL_PLAN.md).
