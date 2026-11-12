# PILOT01. 동일 입력·시각표적에서 contrastive 대 regression의 정서 대비 접근성 비교

연결: [RP01](../proposals/RP01.md), RQ09.

**준비 상태:** **plan:** 최종 리뷰 가능한 문서 계획 작성 완료

**execution:** 조건부; 실행 준비 완료 아님

**completed now:** - 실제 세 입장 검토
- 두 검토자의 12개 필수수정 및2개 미해결 의견 응답
- 공식 CLIP 경로/해시/코드 범위를 공통 근거에서 연결
- 효과·동등성·축소·중단 기준 제안
- 독립 최종감사 FPA1-01-01..05에 따른 판정/fit-scope/추론범위/자원 계약 수정

**unverified:** - 사용자 보유 자료의 현재 마운트·숫자 배열·실제 target_id·척도
- 독립 내용-family와 개인 내 실제 반복
- 캐시 identity·frame 추출 규칙·정서/비정서 공통 지지
- 체크포인트 다운로드·SHA 검증·load·한입력 추론
- 작은 encoder 구현·학습 안정성·한 batch 실측 시간/메모리
- δ와 원척도 최소차의 개발자료 근거·잠긴 split manifest
- D/R/H 및 각 inner/outer fit/calibration ID의 실제 지지
- 전체pipeline 재학습 비용·단계별 RSS/cgroup 잔여량·solver 수렴·wall budget
- 고정 OOF 및 잠근 H의 조건부 구간 계산; 재학습 불확실성은 현재 추론범위 밖

**not required to finish document:** 이 미확인은 문헌·토론·계획 작성을 막지 않는다. 실행 착수 때만 gate로 적용한다.



이 문서는 파일럿 실행 계획이다. 실험·모델 추론·뇌 분석 결과를 보고하는 문서가 아니다.

## 1. 핵심·경쟁 가설

**H1:** 일차 대립가설은 |I|>δ_I인 양측 차등 접근성이다. I>δ_I는 contrastive가 regression보다 A에서 C 대비 상대적으로 더 나쁜 방향, I<−δ_I는 상대적으로 더 좋은 방향이다. 방향을 결과 후 선택하지 않는다.

**H0 general:** D_A,D_C의 같은 방향 변화와 I의 ±δ_I 동등성이 함께 확인되면 두 목표 차이의 공통 손상/이득으로 해석한다. 둘 다 악화되더라도 |I|>δ_I이면 공통 상대 손상+차등 접근성의 혼합 결과다.

**H0 recode:** 차이는 가역 재부호화·유한 probe 접근성이며 정확 역변환/유연 probe에서 회복된다.

**refutation:** 적절한 신호·대조와 잠근 H의 제한된 동등성 결과는 H1의 실용적 크기를 낮춘다. OOF 조건부 구간만으로 학습절차 일반화/동등성을 선언하지 않는다. 일반 내용 대조가 차이를 설명하면 정서 선택성 해석을 낮추며 원뇌 신호 미확인은 H1 반증이 아니다.



## 2. 자료·접근·하위집합

**primary dataset:** 사용자 보유 Horikawa; 참가자별 자극 시행 반응과 자극 수준의 독립 인간 정서 집계주석. 현재 마운트·배열·코드북은 열지 않았다.

**official sources:** - https://github.com/OpenNeuroDatasets/ds002425
- https://github.com/KamitaniLab/EmotionVideoNeuralRepresentation
- https://github.com/KamitaniLab/EmotionVideoNeuralRepresentationPython

**verified facts:** 공식 metadata에서 5명×61런=305 events와 각2196 자극 이벤트. 2196개 ID를 독립 내용/반복 수로 읽지 않는다. 제외15 후2181과 소개2185 차이를 원자료 계보로 설명하기 전 자동 보정하지 않는다.

**verified event fields:** - onset
- duration
- trial_type
- stimulus_name
- stim_index

**code contract not loaded:** - Session
- Run
- Block
- Label
- VoxelData

**source paths:** **user data mount:** None

**processed neural array:** None

**annotation file:** None

**stimulus video directory:** None

**existing feature cache:** None

**new analysis contract fields:** - subject_id
- source_event_row
- stimulus_id
- content_family
- duplicate_group
- target_id
- annotation_source
- annotation_scale
- feature_source
- source_run
- outer_fold
- pair_id
- pair_orientation_seed
- eligible_reason
- normalization_fit_fold

**contract status:** 위 새 필드는 분석자가 검증 후 만드는 계약이며 원자료의 실제 열이라고 하지 않는다. 경로는 확인 후 등록하며 임의 폴더를 데이터 위치로 만들어 쓰지 않는다.

**join and qc:** stim_index→원영상→처리 Label→주석의 cardinality·결측·중복을 전수 확인한다. 실제 동일 자극 반복은 run/session·제시 이력으로 별도 입증해야 한다. content_family는 뇌·정서 점수와 독립적인 원본 계보/중복 metadata로 정의하고 검증한다.

**target registration:** target_id는 현재 미확인(null)이다. 코드북에서 실제 제공된 인간 정서 항목 하나와 정서와 독립적으로 측정할 비정서 scalar 하나를 개발표본에서 선정·등록한다. 비정서 scalar는 문서화된 motion energy 또는 명시적 내용량이 후보이며 AI 정서 점수는 제외한다. 원 타깃의 방향·척도·집계와 대비를 등록하기 전 본검정은 시작하지 않는다.

**other owned data:** **Emo-FilM:** 후속 별도 검정; 외부 연속 consensus와 개인 clip 평정은 다른 단위이며 영화축/scanner축을 구분한다.

**Spacetop:** 후속 clip 단위 별도 검정; clip후 평정을 clip 내부 연속 정답으로 쓰지 않는다.

**NSD:** 실제 반복·시각 판독 대조 후보; 현재 인간 정서 ground truth 미확인이다.

**Mind Captioning:** 정확한 식별자·버전·텍스트 생성 출처·뇌 대응 확인 후 의미 통제 후보; 이름만으로 주석을 추정하지 않는다.

**privacy:** 이 계획은 개인자료·원본영상·신경배열을 공개 저장소에 업로드하지 않는다. 공개 보고에는 집계·코드·비식별 분석 계약만 검토해 사용한다.



## 3. 모델·체크포인트·자원

**framework:** **stage A:** cache/원뇌 ridge와 비학습 대조는 접근성·감도·파이프라인 검사다. 목적함수 효과를 시험한 결과가 아니다.

**stage B:** 같은 피험자의 같은 X와 같은 frozen 시각 target V에서 동일 작은 encoder를 두 목표로 학습한다. CLIP backbone은 고정하고 생성 diffusion은 사용하지 않는다.

**input preprocessing:** 각 outer/inner fold 및25/50/100% nested fraction의 명시적 fit IDs만으로 결측처리·voxel 표준화·선택·PCA를 적합한다. D=min(128,해당 fit행수−1,유효voxel수)를 동일 objective쌍에 공통 적용한다. calibration/validation/test는 transform만 수행한다. 원 voxel 기준의 iterative/dual solver는 별도 보고하며 V×V dense normal matrix를 만들지 않는다.

**encoder:** 공통 X의 D차원→128 GELU trunk→K 선형 head; 출력과 시각 V를 동일 L2정규화한다. trunk와 head에서 같은 시행별 feature를 기록한다. 원뇌/PCA/trunk/head는 차원이 달라질 수 있으므로 차원 일치 projection 대조와 원형 결과를 함께 보고한다.

**contrastive loss:** 같은 batch의 정규화 head u_i와 visual v_i에 대한 대칭 InfoNCE; 계획 temperature=0.07 고정. duplicate/content-family의 다른 항목을 음성으로 취급하지 않도록 공통 batch를 구성하며 유효 음성 수를 기록한다.

**regression loss:** 같은 u_i,v_i의 평균 squared Euclidean distance. 같은 표적·입력·정규화·batch를 쓰고 목표 수식만 다르다.

**optimization budget:** 계획 기본: AdamW lr=0.001, weight_decay=0.0001, batch≤64, 200 epoch 상한, 3 paired seed(20261112–20261114). 두 목표의 초기화·batch순서·총 update 수를 같게 고정한다. 비정상 loss가 있으면 test 이전 공통 안정화 규칙을 수정해 양쪽 재시작한다. 파일럿 기술 실행에서 필요한 learning rate 변경은 잠금 전에 기록한다. 목표별 test 결과를 보고 튜닝하지 않는다.

**model selection:** 일차 hyperparameter는 D에서 잠근다. probe 또는 추가 grid를 선택하는 inner 검증에서는 각 후보마다 encoder를 포함한 전체 pipeline을 F_inner에서만 fit하고 C_inner에서 calibration한 뒤 V_inner에서 평가한다. outer-train으로 먼저 학습한 encoder를 inner validation에 재사용하는 probe-only 경로는 이 파일럿에서 사용하지 않는다. 동일 후보 수·총 compute 예산을 objective쌍에 적용하며 inner encoder 재학습 비용도 포함한다. 최종 outer pipeline은 선택 후 F_outer/C_outer로 새로 fit/calibrate한다.

**probe:** 명시한 fit IDs 내부의 공통 자극쌍 feature차이에 선형 L2 logistic 및 사전 고정64-unit MLP probe를 적합한다. 25/50/100%는 encoder를 포함한 전체 pipeline 학습량이다. 일차는head·선형·100%; 나머지는 등록된 보조/다중비교 대상이다. calibration labels는 encoder/probe 적합에 쓰지 않는다.

**conditional probe:** 객체·관계·motion content-only 특징과 content+neural을 같은 타깃에서 nested 비교한다. content feature가 정서와 공유하는 설명까지 제거할 수 있으므로 총 성능도 함께 보고한다.

**checkpoint:** **model id:** OpenAI CLIP ViT-B/32

**code url:** https://github.com/openai/CLIP/blob/main/clip/clip.py

**architecture url:** https://github.com/openai/CLIP/blob/main/clip/model.py

**checkpoint url:** https://openaipublic.azureedge.net/clip/models/40d365715913c9da98579312b702a82c18be219cc2a73407c4526f58eba950af/ViT-B-32.pt

**expected sha256:** 40d365715913c9da98579312b702a82c18be219cc2a73407c4526f58eba950af

**license url:** https://github.com/openai/CLIP/blob/main/LICENSE

**verified scope:** 공통 자원 문서에서 공식 loader·URL·해시 검증 규칙과 MIT 코드 라이선스 확인. 이 Agent의 새 다운로드·load·추론은 없음. 가중치의 독립적인 추가 이용조건은 공식 문서 적용 범위 확인 필요.

**local checkpoint path:** None

**load status:** 미확인

**feature dimension:** ViT-B/32 출력 K는 실제 load/cache header에서 확인해 manifest에 기록; 수치 shape 미검증

**feature rule:** 캐시가 있으면 모델 ID·hash·frame sampling·정규화·stim_index 계보가 모두 일치해야 사용한다. 없으면 실제 원영상 접근 확인 후 clip 유효구간의 고정 균등 8 frame을 계획 기본값으로 사용하고 평균 후 L2 정규화한다. 8은 원자료 필드가 아닌 제안한 추출 규칙이며 영상 길이/유효 frame 확인 뒤 test 이전 고정한다.

**not required:** 원형 MindEye2 훈련이나 Horikawa용 pretrained adapter를 가정하지 않는다. masked 재구성 대 contrastive는 입력/표적 변경을 포함하므로 이 파일럿의 일차 대비에서 제외한다.

**fit scope:** - **component:** frozen CLIP feature 추출
  
  **fit ids:** 외부 사전학습 checkpoint 고정; 현 연구 ID로 backbone을 적합하지 않음
  
  **validation ids:** 고정 변환의 실행만 D/R/H에서 허용; H feature를 목표나 선택에 사용하지 않음
  
  **rule:** 모델/추출 규칙은 D에서 잠금; 캐시를 모든 행에 계산했다는 사실과 encoder가 그 target을 학습했다는 사실을 구분.
- **component:** inner 전처리·PCA
  
  **fit ids:** T_q의 inner-train을 다시 나눈 F_inner(80% 계획)
  
  **validation ids:** C_inner(20% calibration)와 V_inner에는 transform만
  
  **rule:** 평균·scale·voxel선택·PCA의 모든 fitted state는 F_inner만 사용.
- **component:** inner 뇌→시각 encoder
  
  **fit ids:** F_inner의 X와 같은 ID의 V만
  
  **validation ids:** C_inner/V_inner의 X·V는 parameter fit/early stopping에 쓰지 않음
  
  **rule:** 각 fraction·inner fold·objective·seed마다 초기화부터 재학습; 고정 update 이후 validation scoring만 허용.
- **component:** inner probe
  
  **fit ids:** F_inner 내부에서 만든 쌍의 neural/content 특징과 label
  
  **validation ids:** C_inner에는 calibration용 prediction, V_inner에는 평가용 prediction만
  
  **rule:** probe hyperparameter 후보도 같은 F_inner에서 fit; 전체 pipeline 후보 선택 점수는 V_inner.
- **component:** inner probability calibration
  
  **fit ids:** C_inner의 고정 encoder/probe out-of-sample 예측과 label
  
  **validation ids:** V_inner로 보정된 전체 pipeline 평가
  
  **rule:** C_inner는 encoder/probe fit에 포함하지 않으며 calibration을 V_inner label에 적합하지 않음.
- **component:** outer 최종 적합
  
  **fit ids:** 선택 뒤 T_q를 고정 group split한 F_outer(80%)/C_outer(20%)
  
  **validation ids:** outer test O_k에는 고정 pipeline 적용만
  
  **rule:** 전처리/PCA/encoder/probe를 F_outer에서 재학습하고 calibration은 C_outer만 사용. calibration 이후 F_outer+C_outer로 재학습하지 않음.
- **component:** 독립 H 평가용 최종 모형
  
  **fit ids:** R의 선택된 fraction을 F_R/C_R로 고정 분리; 일차는100% R 분할
  
  **validation ids:** H는 한 번의 최종 평가만
  
  **rule:** R 안에서 잠근 hyperparameter로 F_R 전체 pipeline을 fit하고 C_R로 calibration. H를 본 뒤 재선택·재보정하지 않음.

**resource execution contract:** **concurrency:** 첫 전체 실행은 단일 작업 프로세스에서 참가자→outer fold→fraction→inner fold/후보→seed→objective를 순차 처리한다. DataLoader workers=0, joblib n_jobs=1, OMP_NUM_THREADS=MKL_NUM_THREADS=OPENBLAS_NUM_THREADS=1, torch intra/inter-op thread=1을 실행 전에 고정하고 라이브 thread 수를 기록한다. 4 CPU quota 안에서의 의도적 보수 설정이며 병렬 fold/seed를 띄우지 않는다.

**ridge solver:** 실제 N,V를 확인해 V×V dense normal matrix를 생성하지 않는다. N_fit×N_fit dual Gram이 예산 안이면 voxel chunk로 Gram을 누적한 dual ridge를 사용한다. 그조차 예산을 넘으면 LinearOperator 기반 LSQR/iterative ridge를 사용하고 tolerance·수렴·iteration cap을 D에서 잠근다. 선형 logistic도 feature-block/iterative 경로로 Hessian V×V를 만들지 않는다. solver 변경은 두 objective/기준에 같은 규칙으로 적용한다.

**pca solver:** train-only streaming mean/scale과 block 또는 randomized truncated SVD의 D=128이하 경로를 사용한다. 원행렬은 실제 저장형식이 허용하면 mmap/voxel chunk로 읽고 fold별 전체 dense 복사본을 동시에 만들지 않는다. N,V,D별 workspace·dtype·temporary 배열 상한과 solver 품질을 기술 smoke에서 확인한다.

**stage measurement:** 전처리·PCA·시각 cache 생성/읽기·최대 한 fold의 inner/outer encoder+probe+calibration·평가·bootstrap 각각 예상 working arrays와 실측 process-tree RSS peak·cgroup memory.current·시간을 기록한다. 한 batch peak만으로 전체 peak를 대체하지 않는다.

**memory budget:** 실행 직전 M=memory.max, C0=memory.current, R0=작업 process-tree RSS, A=M−C0를 측정한다. reserve=max(4GiB,0.2M); A≤reserve이면 시작하지 않는다. 계획 RSS상한 B_RSS=min(16GiB,R0+0.6A)을 manifest에 잠근다. 각 단계 예상 RSS가0.8B_RSS를 넘으면 시작 전 chunk/solver/범위를 수정한다. 실행 중 RSS≥B_RSS 또는 memory.current≥M−reserve이면 다음 allocation/step을 중단하고 안전한 checkpoint·로그만 남긴다. 1초 간격과 큰 allocation 전 확인한다. 외부 작업의 순간 메모리 사용에 대해 OOM 부재를 보장하는 것은 아니다.

**time budget:** 각 단계 기술 smoke의 단위시간×실제 참가자/fold/fraction/inner후보/seed/objective 재적합 횟수로 총 예측 T_est를 계산한다. 첫 전체 run의 계획 wall budget은 B_time=min(8시간,ceil(2*T_est))로 manifest에 고정한다. 2*T_est>8시간이면 test 개봉 전 필수 일차100%만의 비용 또는 명시적 여러 순차 run 일정으로 재계획하며 encoder 재적합을 생략하지 않는다. run budget 초과 시 기록된 step에서 중단/재개하고 실패한 학습을 완료로 세지 않는다. 실제 수치 T_est·RSS·벽시계는 현재 미측정이다.

**claim boundary:** 이는 실행 계약과 제안한 운영 상한이며 현재 자원 측정/실행 성공이 아니다. 예산·solver 변경은 test 전 공통 규칙으로 잠그고 사후 성능에 따라 바꾸지 않는다.

**observed environment:** pilots/RESOURCE_AND_MODEL_PLAN.md 기준 CPU 노출5·cgroup quota4 CPU 상당·32GiB; nvidia-smi 없음·GPU 실행 미확인. 사용자 외부 자원 부재가 아니다.

**memory arithmetic:** float32 배열은4*N*K bytes이나 이를 전체 peak로 사용하지 않는다. X_s·PCA workspace·N_fit×N_fit dual Gram·캐시·optimizer·calibration·bootstrap을 각각 실제 shape로 계산한다. V×V dense normal matrix를 만들지 않고 블록/iterative 경로를 사용한다. 각 단계 예상 RSS는 잠근 B_RSS의80% 아래로 계획하고 실제 RSS/cgroup 중단선을 적용한다. 예시 N2196,K1024의8.58MiB는 특징 한 행렬의 산술일 뿐이다.

**runtime:** 단일 프로세스·thread1·workers0로 참가자/fold/후보/seed/objective를 순차 실행한다. wall budget은 단계별 smoke와 모든 inner/fraction 재적합 횟수로 산출한 T_est에 근거해 min(8시간,ceil(2*T_est))로 잠근다. 현재 T_est·peak RSS·벽시계/VRAM은 미측정이며 resource_execution_contract의 중단·재계획 규칙을 따른다.

**resource execution contract:** **concurrency:** 첫 전체 실행은 단일 작업 프로세스에서 참가자→outer fold→fraction→inner fold/후보→seed→objective를 순차 처리한다. DataLoader workers=0, joblib n_jobs=1, OMP_NUM_THREADS=MKL_NUM_THREADS=OPENBLAS_NUM_THREADS=1, torch intra/inter-op thread=1을 실행 전에 고정하고 라이브 thread 수를 기록한다. 4 CPU quota 안에서의 의도적 보수 설정이며 병렬 fold/seed를 띄우지 않는다.

**ridge solver:** 실제 N,V를 확인해 V×V dense normal matrix를 생성하지 않는다. N_fit×N_fit dual Gram이 예산 안이면 voxel chunk로 Gram을 누적한 dual ridge를 사용한다. 그조차 예산을 넘으면 LinearOperator 기반 LSQR/iterative ridge를 사용하고 tolerance·수렴·iteration cap을 D에서 잠근다. 선형 logistic도 feature-block/iterative 경로로 Hessian V×V를 만들지 않는다. solver 변경은 두 objective/기준에 같은 규칙으로 적용한다.

**pca solver:** train-only streaming mean/scale과 block 또는 randomized truncated SVD의 D=128이하 경로를 사용한다. 원행렬은 실제 저장형식이 허용하면 mmap/voxel chunk로 읽고 fold별 전체 dense 복사본을 동시에 만들지 않는다. N,V,D별 workspace·dtype·temporary 배열 상한과 solver 품질을 기술 smoke에서 확인한다.

**stage measurement:** 전처리·PCA·시각 cache 생성/읽기·최대 한 fold의 inner/outer encoder+probe+calibration·평가·bootstrap 각각 예상 working arrays와 실측 process-tree RSS peak·cgroup memory.current·시간을 기록한다. 한 batch peak만으로 전체 peak를 대체하지 않는다.

**memory budget:** 실행 직전 M=memory.max, C0=memory.current, R0=작업 process-tree RSS, A=M−C0를 측정한다. reserve=max(4GiB,0.2M); A≤reserve이면 시작하지 않는다. 계획 RSS상한 B_RSS=min(16GiB,R0+0.6A)을 manifest에 잠근다. 각 단계 예상 RSS가0.8B_RSS를 넘으면 시작 전 chunk/solver/범위를 수정한다. 실행 중 RSS≥B_RSS 또는 memory.current≥M−reserve이면 다음 allocation/step을 중단하고 안전한 checkpoint·로그만 남긴다. 1초 간격과 큰 allocation 전 확인한다. 외부 작업의 순간 메모리 사용에 대해 OOM 부재를 보장하는 것은 아니다.

**time budget:** 각 단계 기술 smoke의 단위시간×실제 참가자/fold/fraction/inner후보/seed/objective 재적합 횟수로 총 예측 T_est를 계산한다. 첫 전체 run의 계획 wall budget은 B_time=min(8시간,ceil(2*T_est))로 manifest에 고정한다. 2*T_est>8시간이면 test 개봉 전 필수 일차100%만의 비용 또는 명시적 여러 순차 run 일정으로 재계획하며 encoder 재적합을 생략하지 않는다. run budget 초과 시 기록된 step에서 중단/재개하고 실패한 학습을 완료로 세지 않는다. 실제 수치 T_est·RSS·벽시계는 현재 미측정이다.

**claim boundary:** 이는 실행 계약과 제안한 운영 상한이며 현재 자원 측정/실행 성공이 아니다. 예산·solver 변경은 test 전 공통 규칙으로 잠그고 사후 성능에 따라 바꾸지 않는다.



## 4. 입력·출력과 정렬

**neural:** X_s∈R^(N_s×V_s): 실제 처리본에서 얻을 자극시행×voxel 반응. 현재 array shape 미확인. 각행 source_run/stim_index/Label을 연결한다. 연속TR을 독립 clip반응으로 임의 변환하지 않는다.

**visual:** V∈R^(N_unique×K): 동일 CLIP 모델·frame 규칙의 frozen 시각표적. 각 participant X행은 정확한 stimulus key로 V에 연결한다.

**annotation:** A∈R^(N_unique×J) 또는 실제 코드북의 다른 구조; 현재 J/척도 미확인. 한 인간 정서 target과 독립 비정서 scalar를 잠근 뒤 쌍의 0/1 순서 타깃을 만든다. 명목 범주만 있다면 ordinal 순서를 만들어내지 않고 실제척도에 맞춰 설계를 재등록한다.

**pair features:** split 내부의 최대매칭 쌍 M_t개에 대해 z_i−z_j∈R^(M_t×D_z), y_t∈{0,1}^(M_t). 같은 pair_id/orientation을 모든 목표·단계에서 공유한다.

**outputs:** 원뇌/PCA/trunk/head의 paired probability·loss, D_A,D_C,I, 내용조건부 증분, 참가자별 uncertainty, 실제 반복 여부·관측 신뢰도, 가역/절단 QC와 비용 측정.

**timing:** Horikawa events의 onset/duration과 처리반응의 지연·집계 계약을 검증한다. 영상 feature는 실제 stimulus 유효구간을 쓰고 주석/반응 창을 혼용하지 않는다.



## 5. 실험 순서

- **step:** 1
  
  **action:** 공식 provenance와 보유 경로/shape를 읽기 전용 검증하고 분석 manifest를 만든다.
  
  **deliverable:** 경로·hash·join·결측·중복·허용 관측 단위 목록; 현재 미실행.
- **step:** 2
  
  **action:** 첫 유효 참가자의 D 개발 family 안 최대128자극에서 기술 smoke를 수행한다. 전처리/PCA/cache/작은 전체 fit·calibration·평가 각각 RSS·cgroup usage·벽시계를 측정하며 한 batch만 측정하지 않는다.
  
  **deliverable:** array shape·dtype·메모리·한 batch 시간·checkpoint/cache 상태.
- **step:** 3
  
  **action:** target·순서 대비·원척도 차이·D/R/H 및 family/run split·fit/calibration IDs·δ_signal/δ_I·loss·RSS/시간budget을 D에서 등록한다. H는 완전히 잠근다.
  
  **deliverable:** test 잠금 manifest 및 주석 신뢰도와 미확인 항목.
- **step:** 4
  
  **action:** mean/label-prior·원 voxel ridge·train PCA ridge·고정 CLIP content-only·ridge→CLIP와 가역/절단 검사를 수행한다.
  
  **deliverable:** 접근성 기준과 QC만 보고; 목적함수 효과 없음.
- **step:** 5
  
  **action:** D 안 최대512자극·첫 유효 참가자·같은 작은 encoder2목표×paired2seed로 기술 학습을 점검한다. inner재적합·calibration 분리까지 한 전체 fold 비용을 추정하고 단일 프로세스/solver/thread 계약을 확인한다.
  
  **deliverable:** 공통 batch/update·shape·실측 peak memory·학습곡선; 탐색용 기술 결과.
- **step:** 6
  
  **action:** G0–G3 통과 후 R의5fold OOF 일차 head/linear/100%를 가용5명·3seed에 대해 순차 실행한다. inner 선택마다 encoder부터 재적합하고 fit/calibration/test IDs를 로그에 남긴다. 25/50%는 전체pipeline 재학습인 보조 단계로, 자원 gate를 다시 통과한 경우만 확대한다.
  
  **deliverable:** 현재 fitted model에 조건부인 OOF 예측·loss·재표집 구간, fit ID 해시, 각 단계RSS/시간. encoder 재학습 생략이나 seed의 인간N 합산 없음.
- **step:** 7
  
  **action:** 내용-only/조건부·비정서·가역·시간·중복·누수 대조를 독립 test에서 동일 계약으로 평가한다.
  
  **deliverable:** 경쟁 설명별 잔존/소실과 대조 실패 구분.
- **step:** 8
  
  **action:** OOF 조건부 구간으로 G4를 판단하고 계획이 유지되면 R에서만 최종 fit/calibration한 뒤 잠근 H를 한 번 평가한다. H의 고정모형 조건부 차이/동등성과 OOF 기술 구간을 분리하고 개인별 결과·미해결 학습불확실성을 기록한다.
  
  **deliverable:** G4/G5 결정, 공통손상+차등성 혼합 판정, H 또는 미실행 상태, 자원 중단/재개 로그. 사람 모집단·재학습 일반화·정보삭제 주장은 제외.


## 6. 평가·통계

**loss:** **primary task:** 검증된 순서가 있는 원 정서 주석 A_i에서 사전 최소 원척도 차이를 넘는 자극쌍(i,j)의 A_i>A_j 여부를 예측한다. 이는 새 분석용 순서 대비이며 원평정 자체의 Bernoulli 생성모형이라는 뜻이 아니다. 방향은 고정 seed로 뒤집고 대응 label도 뒤집는다.

**nonaffective comparator:** 비정서 scalar C_i의 순서 대비도 같은 방식으로 만들어 같은 0/1 관측과 log loss 단위를 사용한다. 개발자료의 원뇌 판독 난도·유효 쌍수·관측 불확실성을 가능한 범위에서 맞춘다. 적절한 비교표적 또는 교차 지지가 없으면 정서 선택성 추정량을 보류한다.

**pair construction:** 원척도 최소차·의미 매칭 caliper는 codebook와 개발 주석으로 고정한다. 두 타깃 모두 차이가 있는 공통 자극쌍 목록을 split 안에서 뇌 test 반응 없이 결정적 최대매칭으로 만든다. 원영상/중복 family당 최대 한 쌍의 한쪽 endpoint만 허용해 쌍 간 family 중첩을 막는다. 같은 쌍에서 정서 및 비정서 순서 label을 각각 평가한다. 두 label의 일치/불일치 교차 지지를 개발에서 확인하고 test에도 고정 기준을 적용한다. 공통 목록으로 난도/지지를 맞출 수 없으면 선택성 I를 보류한다. 쌍은 fold를 넘지 않고 선정된 대비 모집단만 해석한다.

**proper loss:** 일차는 L(y,p)=−y log p−(1−y)log(1−p), natural-log 단위의 Bernoulli log loss다. 안정된 logit 구현을 쓰고 모델별 clipping·분모를 바꾸지 않는다. 예측 확률은 inner validation에서 점검·보정하고 보정기 선택도 nested 처리한다.

**native scale secondary:** 연속 인간 평균평정이 확인되면 같은 원척도 squared error를 보조 지표로 사용한다. ordinal이면 순서를 넘는 간격 가정을 피하고 누적 ordinal score 또는 순서 대비만 사용한다. 실제 범주 빈도/확률이면 분모와 상호배타성 확인 후 log/Brier score를 고정한다. 독립 복수 범주 rating을 softmax 단일분포로 가정하지 않는다.

**same test:** 총 예측과 의미조건부 증분은 같은 타깃·같은 test 쌍·같은 score를 사용한다. 서로 다른 타깃의 z-score MSE를 빼는 방식으로 선택성을 만들지 않는다.

**statistics:** **primary estimand:** D_A=mean[L_contrastive,A−L_regression,A], D_C도 동일 정의, I=D_A−D_C. 같은 공통 자극쌍·이진 타깃 log loss와 개발 난도/교차지지 매칭이 충족될 때만 계산한다. 일차 대립가설은 |I|>δ_I인 양측 차등 접근성이다. I>δ_I이면 contrastive가 regression보다 정서 A에서 비정서 C 대비 상대적으로 더 나쁘고, I<−δ_I이면 상대적으로 더 좋다. 이것은 두 모델 대비이며 각 모델이 원뇌보다 나쁜지 여부는 별도 기준 비교이다.

**primary units:** 동일 test 자극쌍의 paired loss. 기술 반복 seed는 평균·민감도로 보고 인간 N에 더하지 않는다. 쌍/family를 공유하는 참가자·표적의 의존성을 보존한다.

**split:** 원영상/중복 family를 고정 seed로 D(개발20%), H(완전히 잠근 독립 final holdout20%), R(모형개발/OOF60%)로 먼저 나눈다. 실제 family·run 지지로 이 비율이 불가능하면 어떤 test도 개봉하기 전에 분할안을 재등록하거나 착수를 보류한다. D는 척도·caliper·δ·기술 smoke에만 사용하고 R/H 평가에서 제외한다. R 안의 고정 group outer5-fold와 각 outer-train의 group inner3-fold를 계획한다. H는 모든 특징/목표/probe 선택과 OOF 검토까지 잠그고 한 번만 평가한다. fit-scope 표에 따라 encoder를 포함한 전체 학습을 해당 fit IDs만으로 다시 수행한다. pair는 split/subsplit/fraction을 정한 뒤 각 내부에서만 생성한다.

**time dependence:** 실제 반응추출/HRF 창을 확인해 인접 trial의 겹침이 있으면 run-group holdout 또는 시간 purge를 잠금 전에 정한다. 불가능한 content/run 분할을 임의 강제하지 않고 정의 가능한 일반화 범위를 낮춘다. 참가자별 source_run을 기록하며 pooled row shuffle은 금지한다.

**learning curves:** 25/50/100% 축은 probe-only가 아닌 전체 pipeline 학습량이다. 각 outer-train에서 nested family subset T_q를 만들고 전처리·PCA·encoder·probe·calibration 모두 해당 T_q 내부의 fit/calibration IDs로 다시 적합한다. inner 검증도 각 T_q의 inner-fit에서 encoder부터 새로 학습한다. 100% encoder를 낮은 fraction이나 inner fold에 재사용하지 않는다. 동일 fraction·fold·seed의 두 objective는 동일 IDs·초기화·batch순서·update예산을 공유한다. 일차100%와 보조25/50%의 계산비용을 각각 기록한다.

**uncertainty:** 첫 OOF 분석은 이미 적합·선택된 fold별 모형과 현재 OOF 예측을 고정한 채 독립 family-pair block을 재표집하는 조건부 기술 구간이다(계획2000회, 같은 쌍의 두 타깃·5명 관측을 함께 유지). 95% 차이 구간/90% 실용동등성 구간은 평가쌍 구성의 변동만 반영하며 encoder/probe 재학습·선택·겹치는 outer training sets의 학습절차 불확실성을 포함하지 않는다. OOF를 단일 독립 test 표본처럼 취급한 엄밀한95%/90% coverage나 학습알고리즘의 일반화·동등성을 주장하지 않는다. 참가자 고정·run/time-purge 의존성의 기존 제한도 유지한다. 참가자별 효과와 fold/seed 민감도를 별도 표시한다.

**five subject limit:** 독립5명에서 부호반전 검정의 양측 최소 p는 비영 차이 전부 같은 방향이어도 2/32=0.0625이므로 이를 α=0.05 모집단 유의성 증거로 내세우지 않는다. 자극 수가 많아져도 사람5명 제한은 해소되지 않는다.

**multiplicity:** 일차 한 표적쌍·head·선형·100% I를 미리 고정한다. trunk·MLP·train fraction·다른 타깃의 추가 confirmatory 검정은 하나의 Holm family로 등록하고, 등록하지 않은 결과는 탐색이라고 표시한다. seed별 최상 점수 선택을 하지 않는다.

**reliability:** 원 주석의 raters/집계오차, 실제 반응 반복 신뢰도, 원뇌 holdout 판독, objective 차이 CI는 별도 항목이다. 반복 없으면 repeat ceiling은 NA이며 내용 중복·다른 사람·가역검사를 가짜 반복으로 쓰지 않는다.

**effect threshold:** δ_I=0.02 nats/이진 쌍을 차이의 차이 I의 계획상 실용 임계로 제안한다. g_o,t=exp(mean log p_o,t(true label))라 두면 exp(D_t)=g_regression,t/g_contrastive,t이고 exp(I)=(g_regression,A/g_contrastive,A)/(g_regression,C/g_contrastive,C)이다. 따라서 exp(δ_I)≈1.0202는 I에서는 비의비 임계이며 단일 타깃의 확률 비가 아니다. 원뇌 신호 gate는 별도 δ_signal=0.02 nats/쌍(계획 제안)을 사용해 L_label-prior,A−L_rawbrain,A와 비교한다. 숫자가 같아도 서로 다른 용도이며 생물학적 최소효과가 아니다. 두 값은 개발 신뢰도·비용 근거와 함께 test 전 각각 잠그며 결과를 보고 변경하지 않는다.

**equivalence:** OOF의90% 조건부 재표집 구간이 [−δ_I,+δ_I] 안이면 현재 고정 OOF 예측의 실용동등성 신호로만 표시한다. formal 전체 pipeline 동등성이나 학습절차 일반화 결론은 내리지 않는다. 잠근 독립 H에서 같은 범위를 충족하고 원뇌 신호·대조·독립 block 지지가 충분하면 관측5명·고정 최종 모형·선정 자극 모집단에 제한된 실용동등성으로 해석한다. 비유의/넓은 구간은 미식별이며 90%와95% 구간 모두 학습 재적합 불확실성을 포함하지 않는다.

**outcome partition:** **relative general change:** D_A,D_C가 같은 부호이고 I의90%구간이 [−δ_I,+δ_I] 안이면 두 목표의 차이가 두 대비에 대체로 공통인 결과다. D_A,D_C>0은 contrastive의 공통 상대 손상, 둘다<0은 공통 상대 이득이다.

**mixed:** D_A,D_C>0이면서 I의 구간이 +δ_I 초과 또는 −δ_I 미만이면 공통 상대 손상과 차등 접근성이 공존한다. 둘 다 악화라는 이유만으로 선택성 대비를 자동 폐기하지 않는다. 둘 다<0과 큰 |I|도 공통 이득+차등 접근성으로 표시한다.

**opposite:** D_A,D_C 부호가 다르면 두 대비의 목표 선호가 반대인 패턴이며 I의 크기·불확실성을 별도 판단한다.

**inconclusive:** 같은 부호만으로 일반손상을 확정하지 않는다. I 구간이 임계를 가로지르면 동등성/차등성 미판정이다. 범위가 다른 OOF/독립 holdout 구간은 아래 계약대로 구분한다.

**fit scope:** - **component:** frozen CLIP feature 추출
  
  **fit ids:** 외부 사전학습 checkpoint 고정; 현 연구 ID로 backbone을 적합하지 않음
  
  **validation ids:** 고정 변환의 실행만 D/R/H에서 허용; H feature를 목표나 선택에 사용하지 않음
  
  **rule:** 모델/추출 규칙은 D에서 잠금; 캐시를 모든 행에 계산했다는 사실과 encoder가 그 target을 학습했다는 사실을 구분.
- **component:** inner 전처리·PCA
  
  **fit ids:** T_q의 inner-train을 다시 나눈 F_inner(80% 계획)
  
  **validation ids:** C_inner(20% calibration)와 V_inner에는 transform만
  
  **rule:** 평균·scale·voxel선택·PCA의 모든 fitted state는 F_inner만 사용.
- **component:** inner 뇌→시각 encoder
  
  **fit ids:** F_inner의 X와 같은 ID의 V만
  
  **validation ids:** C_inner/V_inner의 X·V는 parameter fit/early stopping에 쓰지 않음
  
  **rule:** 각 fraction·inner fold·objective·seed마다 초기화부터 재학습; 고정 update 이후 validation scoring만 허용.
- **component:** inner probe
  
  **fit ids:** F_inner 내부에서 만든 쌍의 neural/content 특징과 label
  
  **validation ids:** C_inner에는 calibration용 prediction, V_inner에는 평가용 prediction만
  
  **rule:** probe hyperparameter 후보도 같은 F_inner에서 fit; 전체 pipeline 후보 선택 점수는 V_inner.
- **component:** inner probability calibration
  
  **fit ids:** C_inner의 고정 encoder/probe out-of-sample 예측과 label
  
  **validation ids:** V_inner로 보정된 전체 pipeline 평가
  
  **rule:** C_inner는 encoder/probe fit에 포함하지 않으며 calibration을 V_inner label에 적합하지 않음.
- **component:** outer 최종 적합
  
  **fit ids:** 선택 뒤 T_q를 고정 group split한 F_outer(80%)/C_outer(20%)
  
  **validation ids:** outer test O_k에는 고정 pipeline 적용만
  
  **rule:** 전처리/PCA/encoder/probe를 F_outer에서 재학습하고 calibration은 C_outer만 사용. calibration 이후 F_outer+C_outer로 재학습하지 않음.
- **component:** 독립 H 평가용 최종 모형
  
  **fit ids:** R의 선택된 fraction을 F_R/C_R로 고정 분리; 일차는100% R 분할
  
  **validation ids:** H는 한 번의 최종 평가만
  
  **rule:** R 안에서 잠근 hyperparameter로 F_R 전체 pipeline을 fit하고 C_R로 calibration. H를 본 뒤 재선택·재보정하지 않음.

**independent confirmation:** OOF 결과는 G4의 다음 단계 선택용이다. 사전 잠근 H에서, R로만 적합·선택·보정한 최종 pipeline을 한 번 평가하는 경로를 추가한다. 충분한 독립 family-pair/run blocks가 있을 때 H의95% 차이 및90% 동등성 구간을 계산해 고정 최종 모형이 새로운 선정 자극쌍에서 보이는 성능을 추론한다. 이는 관측5명과 해당 학습자료/적합모형에 조건부이며 새 training sample의 재학습 변동은 포함하지 않는다. 전체 학습절차의 일반화/동등성 주장은 현재 범위 밖이고, 필요하면 학습/선택/보정까지 재실행하는 사전 설계된 재표집 또는 독립 반복 연구를 별도 수행한다. H 지지가 부족하거나 이미 사용됐으면 확인 결과를 내지 않고 탐색으로 남긴다.



## 7. Ablation·대조

- **name:** 동일 Gram 직교 대조
  
  **procedure:** train에서 고정한 직교 Q로 ZQ를 만들고 Gram 보존과 동일 등방 ridge/logistic 재적합 결과를 확인한다. intercept·최적화 tolerance를 공통으로 고정한다.
  
  **failure meaning:** 예측 불일치가 크면 데이터 처리·최적화·정규화 구현 문제이며 신경정보 손실이 아니다.
- **name:** 조건수 제한 가역 선형·비선형
  
  **procedure:** invertible matrix와 명시적 역함수가 있는 affine-coupling 변환을 별도 사용한다. 역변환 후 feature를 원래와 비교하고 같은 원 probe 예측이 복구되는지 확인한다. learned nonlinear probe 회복과 정확 역변환 복구는 다른 검사다.
  
  **failure meaning:** 정확 역변환 실패는 구현 오류; 학습 probe 비회복은 유한 함수·표본의 접근성 한계다.
- **name:** 알려진 신호 rank 절단
  
  **procedure:** 실뇌 정서와 별개인 합성 독립 target을 한 좌표에 주입한 대조에서 그 좌표를 제거한다. 남은 좌표와 독립인 생성규칙을 보존한다.
  
  **failure meaning:** 주입 전 신호 미검출 또는 제거 후 잔존은 감도/누수 문제다. 실제 인간 정서정보의 삭제를 증명하지 않는다.
- **name:** 정서/비정서 대비
  
  **procedure:** 같은 proper loss·개발 난도·표본수·내용지지에서 목표차를 비교한다. 비정서 전반 악화와 정서 관련 차이를 구분한다.
  
  **failure meaning:** 같은 악화이면 일반 병목/최적화 설명을 남기고 정서 선택성 주장을 낮춘다.
- **name:** 내용·영상·motion
  
  **procedure:** low-level 영상통계·고정 CLIP·관계/객체 내용·motion의 content-only 기준과 content+brain을 비교한다. 관계 metadata 부재는 누락 의미 대안을 남긴다.
  
  **failure meaning:** 강한 내용모형이 차이를 설명하면 독립 정서 계산 주장을 축소한다.
- **name:** ID·중복·시간
  
  **procedure:** 원영상/dupidx family를 한 fold에 묶고, run/session 및 반응 추출 창의 시간 의존성을 확인한다. 같은 자극5명의 행을 무작위로 섞거나 clip 내부 frame을 독립 시행으로 세지 않는다.
  
  **failure meaning:** 중복·시간 누수에서만 효과가 생기면 현재 효과를 기각하고 split부터 수정한다.
- **name:** 교환 null
  
  **procedure:** 원영상 그룹·run 시간 의존성과 사전 조건군을 보존하는 label/brain exchange가 가능할 때 사용한다. 교환가능성이 불명확하면 permutation p값을 확정 검정으로 쓰지 않는다.
  
  **failure meaning:** null 분포의 타당성 부족은 검정 설계 문제다.


## 8. 확대·수정·중단 기준

- **id:** G0
  
  **stage:** 자료·권한·계약
  
  **advance:** 실제 경로·헤더·모든 사용행의 stimulus↔brain↔annotation join과 family split이 검증되며 provenance가 잠겼을 때만 진행.
  
  **modify or stop:** 경로/주석 미확인은 계획 완료·실행 조건부 상태로 둔다. 오류행은 사전 원칙대로 제외하고 제외 이유·개수를 공개하며 대체값을 만들지 않는다.
- **id:** G1
  
  **stage:** 관측척도·대비
  
  **advance:** 실제 인간 순서 주석·비정서 대비·원척도 최소차·교차지지를 확정하고 δ_signal과 δ_I를 별도 정의하여 잠근다. D/R/H 분할과 각 단계 fit/calibration IDs도 확정한다.
  
  **modify or stop:** 비정서 매칭이 불가능하면 선택성 I는 중단하고 D_A 접근성 방법검사만 수행한다. 정서 주석 자체 없으면 이 자료의 RP01 신경 검정을 착수하지 않는다.
- **id:** G2
  
  **stage:** 비학습·가역·절단 기술 대조
  
  **advance:** 정확 역변환 feature 상대오차≤1e−5, 동일 원 probe 예측 최대차≤1e−5를 float32 기본 허용치로 제안하고 실제 dtype의 수치오차 근거로 test 전 확정한다. 알려진 독립 주입 target은 절단 전 검출·후 기대 chance로 돌아와야 한다.
  
  **modify or stop:** 정확 역복구 실패 또는 합성 누수는 실제데이터 가설검정 중단·구현 수정 사유. 이 통과가 실제뇌 repeat 신뢰도를 대체하지 않는다.
- **id:** G3
  
  **stage:** 기준 신호와 소형 목표쌍
  
  **advance:** 개발자료에서 L_label-prior,A−L_rawbrain,A가 별도 δ_signal을 넘는 안정된 이득을 보이고 같은 작은 두 목표가 공통 budget에서 finite loss·재현 가능한 학습을 보일 때 확대한다. 전처리/PCA/cache/최대 한 fold 전체의 RSS·시간 예측과 관측이 resource_execution_contract의 budget 아래여야 한다.
  
  **modify or stop:** 원뇌 이득 불안정은 저신뢰/저검출력으로 표시한다. 목표쌍 구현 또는 inner encoder 재학습 비용을 감당하지 못하면 A단계 방법검사로 축소하며 누수 경로로 대체하지 않는다. RSS/cgroup/시간 중단선에 도달하면 다음 step을 중단하고 test 전 계획을 수정한다.
- **id:** G4
  
  **stage:** 고정 OOF 결과의 조건부 검토
  
  **advance:** OOF95% 조건부 재표집 구간이 +δ_I 초과 또는 −δ_I 미만이며 기술 대조·교차지지가 충족되면 사전 잠근 독립 H 확인 단계로만 진행한다. 이 구간은 고정 학습모형의 현재 예측에 조건부인 선택 지표이며 전체 학습절차의 검증된 coverage를 갖는 구간으로 주장하지 않는다.
  
  **modify or stop:** D_A,D_C>0이면서 I의90%조건부 구간이 ±δ_I 안이면 공통 상대 손상과 차등성 미지지로 기록한다. 두 D가 양수이나 I구간이 임계 밖이면 공통 손상+차등 접근성의 혼합으로 보존한다. 같은부호만으로 축소하지 않는다. 구간이 임계를 가로지르면 미판정; 누수/스코어 오류가 원인이면 기각·수정한다. OOF 동등성 신호만으로 formal 동등성을 확정하지 않는다.
- **id:** G5
  
  **stage:** 잠근 H의 독립 확인·모집단/자원 확대
  
  **advance:** R로만 적합/선택/보정한 최종 모형을 잠근 H에 한 번 적용한다. H95%구간이 +δ_I 초과 또는 −δ_I 미만이면 고정 최종 모형·관측5명·선정 자극 모집단에서 차등 접근성을 지지한다. H90%구간이 ±δ_I 안이면 같은 범위의 실용동등성으로 제한한다. 공통손상과 차등효과는 동시에 보고한다. 새로운 학습표본/사람 모집단으로의 확대는 별도 재적합·복제 설계가 필요하다.
  
  **modify or stop:** H가 이미 선택에 쓰였거나 독립 block·신뢰도·지지가 부족하면 확인 추론을 내리지 않는다. 현재 구간은 재학습/모형선택 변동을 포함하지 않는다. 5명을 더 많은 시행으로 늘려 인구 유의성을 만들지 않으며 resource gate 실패시 대형모형 확대를 중단한다.


## 9. 실패 가능성과 주장 한계

- 현재 사용자 데이터 경로·배열·정서 target_id·내용군·cache 및 checkpoint load는 미확인이다.
- 순서 대비는 원평정을 이진화한 새 분석 타깃으로 정보 일부를 버리며 선정된 쌍 모집단에만 일반화한다. 원척도 보조 결과를 병기한다.
- 의미 매칭과 난도 매칭은 불완전할 수 있다. 같은 log loss라도 두 과제의 원주석 불확실성이 같다고 보장하지 못한다.
- Horikawa5명으로 인구 효과의 정밀한 추론을 약속하지 않는다. 내용 중복과 개인 반복은 다르다.
- 유한 probe 실패는 삭제 증명이 아니며 절단 양성대조도 인간 신경정보 삭제의 증거가 아니다.
- 원 코드/가중치 공개가 현재 환경 실행 성공이나 Horikawa 호환성을 뜻하지 않는다.
- 목표 변경의 효과는 지정 optimizer·유한예산과 함께 정의된다. 뇌 학습 원리를 추정하지 않는다.
- 최종 감사 후 OOF 재표집을 현재 fitted models/예측에 조건부인 기술 구간으로 한정했다. 독립 H도 해당 고정모형의 자극 일반화이며 재학습 변동을 담지 않는다.
- 전체pipeline inner/fraction 재학습과 calibration 분리는 계산비용을 늘린다. 실제 solver·RSS·시간·자원 budget은 기술 smoke 전 미확인이다.
- 동일 관측5명과 고정 학습모형에 조건부인 구간을 인구/새 training sample 일반화 CI로 바꾸어 읽지 않는다.
- 자원 guard는 외부 작업의 순간 메모리 사용에 대해 OOM 부재를 보장하지 않으며 초과 시 중단·기록한다.
- 계획 수정이며 실제 신경 분석·가중치load·학습 실행은 하지 않았다.


## 근거

- [P001 The neural representation of visually evoked emotion is high-dimensional, categorical, and distributed across transmodal brain regions](https://doi.org/10.1016/j.isci.2020.101060) · [실제 확인 출처](https://raw.githubusercontent.com/OpenNeuroDatasets/ds002425/3f94b2bf9a75ddb62637c529d30dc40dd4ab5ba1/dataset_description.json)
- [P008 Emotion schemas are embedded in the human visual system](https://doi.org/10.1126/sciadv.aaw4358) · [실제 확인 출처](https://raw.githubusercontent.com/canlab/Neuroimaging_Pattern_Masks/master/Multivariate_signature_patterns/2019_Kragel_Emotion_Schemas/Kragel_2019_SciAdv_emotion_schemas.pdf)
- [P015 MindEye2: Shared-Subject Models Enable fMRI-To-Image With 1 Hour of Data](https://arxiv.org/abs/2403.11207) · [실제 확인 출처](https://github.com/MedARC-AI/MindEyeV2)
- [P016 Reconstructing the Mind's Eye: fMRI-to-Image with Contrastive Learning and Diffusion Priors](https://arxiv.org/abs/2305.18274) · [실제 확인 출처](https://github.com/MedARC-AI/fMRI-reconstruction-NSD)
- [P022 Seeing Beyond the Brain: Masked Modeling Conditioned Diffusion Model for Human Vision Decoding](https://github.com/zjc062/mind-vis)
- [P051 Similarity of Neural Network Representations Revisited](https://proceedings.mlr.press/v97/kornblith19a.html)
- [P079 Learning Transferable Visual Models From Natural Language Supervision](https://raw.githubusercontent.com/mlresearch/v139/gh-pages/radford21a/radford21a.pdf)
- [P100 Statistical inference on representational geometries](https://doi.org/10.7554/eLife.82566) · [실제 확인 출처](https://elifesciences.org/articles/82566)
- https://github.com/OpenNeuroDatasets/ds002425
- https://github.com/KamitaniLab/EmotionVideoNeuralRepresentation
- https://github.com/KamitaniLab/EmotionVideoNeuralRepresentationPython
- https://github.com/openai/CLIP/blob/main/clip/clip.py
- https://openaipublic.azureedge.net/clip/models/40d365715913c9da98579312b702a82c18be219cc2a73407c4526f58eba950af/ViT-B-32.pt
- https://github.com/openai/CLIP/blob/main/LICENSE

작성 원본: [03_vision_decoding](../agents/03_vision_decoding/pilot_PILOT01.json). [공통 자원·모델 근거](RESOURCE_AND_MODEL_PLAN.md).
