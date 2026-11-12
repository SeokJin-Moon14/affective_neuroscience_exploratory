# PILOT03. 가중 parcel 평균과 내부 잔차의 독립 정서 예측 접근성 비교

연결: [RP08](../proposals/RP08.md), RQ14.

**준비 상태:** **plan complete:** True

**analysis executed:** False

**execution ready:** False

**confirmed:** 공식 데이터/code 경로 계약, 현재 CPU/메모리 보고, projection-baseline이 checkpoint 불필요하다는 설계, CLIP 공식 identity/URL/hash 규칙.

**conditional:** 실제 보유본 mount·A 사전·dense array·G/W 공간 대응·GLM/내용중복·cache·작은 실행 수치·power/δ 고정.

**repeat status:** 개인 내 동일 자극 반복 미확인. 첫 파일럿은 반복 없는 예측 범위로 제한하고 확인되면 추가 가지로 명시.

**checkpoint status:** 필수 baseline에는 없음. 보조 CLIP/CortexMAE load 미실행.

**completion boundary:** 계획·상세설계 완료와 분석 착수/실험 완료는 별개다.



이 문서는 파일럿 실행 계획이다. 실험·모델 추론·뇌 분석 결과를 보고하는 문서가 아니다.

## 1. 핵심·경쟁 가설

**H1:** 일차: 같은 참가자·새 자극에서 m-only의 강한 readout보다 [Gy,U_kᵀsqrt(W)r]가 A의 paired prediction risk를 낮추는가?

**H2:** 이차: 같은 참가자·자극의 H1 효과가 실제 atlas와 사전 정의 random contiguous atlas 분포에서 다른가?

**H3:** 이차: train에서 척도/난도/가능한 신뢰도 기준을 맞춘 A와 비정서 B의 model×target risk interaction이 있는가?

**logic:** H1만 양성이면 일반 spatial-pattern 접근성. H2 실패는 H1 반박 아님. H3 실패면 정서 선택성 철회. 반복이 실제 없으면 반복 재현 주장 없음.

**alternatives:** - 강한 nonlinear 평균 readout으로 충분
- 추가 feature/regularization 효과
- 일반 공간 주파수·감각/의미 정보

**falsification:** H1 precision이 충분한데 strongest m-only와 동등하면 제한된 함수족의 추가 잔차 필요성 반박. H2 실패는 경계 특수성만, H3 실패는 정서 선택성만 반박한다. 신뢰도/precision 불충분은 미결정.



## 2. 자료·접근·하위집합

**possession:** Horikawa·Emo-FilM·Mind Captioning·NSD·Spacetop 보유는 사용자 진술. 실제 workspace mount 및 array는 미확인.

**primary official:** - https://github.com/OpenNeuroDatasets/ds002425
- https://github.com/KamitaniLab/EmotionVideoNeuralRepresentation
- https://github.com/KamitaniLab/EmotionVideoNeuralRepresentationPython

**contracts:** **confirmed official event fields:** - onset
- duration
- trial_type
- stimulus_name
- stim_index

**official code contract only:** - Session
- Run
- Block
- Label
- VoxelData
- voxel_x
- voxel_y
- voxel_z

**path contracts:** - 공식 코드 계약: data/fmri/paper2020/fmri_Subject1.h5
- 공식 feature 계약: data/features/amt/mean_score_concat/{category,dimension,semantic,vision}

**not local verified:** 위 경로와 HDF5 키는 공식 코드의 계약이다. 사용자의 실제 보유본 경로·헤더·버전은 아직 열어 확인하지 않았으며 임의 로컬 경로를 만들지 않는다.

**generated analysis fields:** - content_group
- outer_split
- repeat_id
- preprocessing_provenance
- atlas_id
- space_id
- feature_source
- annotation_source

**generated field scope:** 분석자가 확인 후 만드는 계약 필드이며 원자료에 이미 있다는 뜻이 아니다.

**selection rule:** 먼저 실물manifest에 participant,stim_index,stimulus_name,run/session,content_group,space,preprocessing를 연결한다. 내용중복 exclusion은 근거 mapping을 기록한다. 원칙적으로 반응값을 보지 않은 deterministic seed20261112로 run/content coverage를 분산해 cap를 적용하며 같은 내용을 train/test로 나누지 않는다.

**planned subset:** **contract QC:** 가용 participant ID 중 사전순 첫1명, 최대32개 실제 자극행, atlas label 순서와 coverage를 이용해 고정한 완전8 parcels. 이 단계는 수치/입출력 검증이며 신경 효과 검정 아님.

**first comparison:** 가능하면 가용5명 모두, 공통/대응 가능한 최대512고유 자극/인과 최소12런 coverage를 목표로 한다. 실제 공통 자극/내용수 부족이면 수와 power를 재계획하고 숫자를 채우지 않는다. 사전 고정32개 완전 비중첩 cortical parcels를 전체 영역에 걸쳐 label순 균등간격으로 선택; 신경 효과로 고르지 않음.

**scope:** 선택된 participant와 cortical subset·자극범위 조건부 결론. atlas coverage가 다르면 공통지원 범위를 먼저 고정하거나 별개 분석으로 둔다.

**replicates:** 확인된 반복이 없으면 no-independent-repeat 플래그. dupidx·복사본·다른 사람을 개인 반복으로 변환하지 않음.

**fallback:** dense y가 없으면 첫 H1 실험 불가. 실제 dense 처리본 확인 또는 NSD의 비정서 projection 방법 대조만 가능하며 정서 분석을 한 것으로 세지 않는다.



## 3. 모델·체크포인트·자원

**baseline:** 고정 가중 G/P group-reduction, train-only weighted residual PCA, ridge와 kernel ridge(또는 사전 작은 MLP). checkpoint가 없는 직접 projection baseline이므로 미확보 foundation weight를 기다릴 필요 없음.

**optional visual model:** **model:** OpenAI CLIP ViT-B/32

**code:** https://github.com/openai/CLIP

**checkpoint url:** https://openaipublic.azureedge.net/clip/models/40d365715913c9da98579312b702a82c18be219cc2a73407c4526f58eba950af/ViT-B-32.pt

**sha256 expected:** 40d365715913c9da98579312b702a82c18be219cc2a73407c4526f58eba950af

**license scope:** 공식 코드 MIT 및 loader의 URL/hash 규칙 확인; 실제 weights 다운로드·해시·load·추론은 미검증.

**input output:** 이미지 또는 텍스트→모달별 embedding. 동영상은 사전 고정 frame sampling과 집계가 필요한 별도 자극 특징 구성이다. 오디오 또는 독립 정서 주석을 제공하지 않는다.

**role:** 보유 cache가 없을 때 검수된 비정서 V/S 통제의 보조 시각 특징. 첫 projection baseline에 필수 아님.

**optional brain model:** CortexMAE 공식 https://github.com/MedARC-AI/CortexMAE 및 https://huggingface.co/medarc/CortexMAE; 코드 Apache-2.0·모델 CC-BY-NC4.0의 기존 확인 범위. 실제 config/P-F-V 지원·checkpoint load 미확인. 첫 pilot에 사용하지 않으며 후속 비교는 별도 matched-data 설계.

**environment:** **observed environment:** 공통 관측 보고서 CPU quota4·memory.max32GiB·nvidia-smi 없음; GPU 추론 미실행. 다른 사용자 장비의 자원은 판단하지 않음.

**cost boundary:** 이미 추출된 feature cache 및 작은 신경 블록의 적합 비용과 새로운 backbone 추출 비용을 분리한다. 시간/VRAM은 작은 실행으로 계측 전 미확인.

**ownership:** 사용자 컴퓨터에 대형 자료를 받도록 요구하지 않고 새 원자료·개인 데이터를 공개 백업 산출물에 넣지 않는다.

**memory plan:** NxV float32 한 행렬4NV bytes. 계획 N=512,V=20000 예시는40,960,000bytes≈39.1MiB/인/행렬이며 실제 V 미확인. 반면 V×V P는 같은 V에서도1.6GB이므로 만들지 않는다. m/r·train copies·5명·PCA workspace·kernel NxN을 별도 계상하고 한 참가자/공간블록씩 처리한다.

**compute gate:** 실제 한 block의 peak memory·wall time·수치오차를 먼저 측정. 메모리 안전폭이 부족하면 parcel/자극 block 또는 incremental SVD로 조정하며 CPU/GPU 최소시간을 미리 확정하지 않음.



## 4. 입력·출력과 정렬

**input shapes:** 각 참가자 Y_s:[N_s,V_s], A:[N_s,D_A], 선택된 A0:[N_s,1], V/S:[N_s,K]가 있으면 보조, parcel_labels:[V_s], weights:[V_s]. N/V/K/정확 D_A는 실물확인 값으로 manifest에 기록. 원코드 category34/dimension14를 실제 라벨헤더 검증으로 대체하지 않음.

**projection:** **definition:** C∈R^(V×J)는 비중첩 parcel membership, W=diag(w_v)>0는 결과와 무관하게 고정한 voxel-volume/vertex-area 가중이다. G=(CᵀWC)⁻¹CᵀW, P=CG, m=Py, r=y-m. 그러면 P²=P, Gr=0, CᵀWr=0이며 W-metric에서 평균과 잔차가 직교한다. W=I이면 기존 Euclidean Gᵀ(GGᵀ)⁻¹G와 같다.

**weight policy:** native 동일부피 voxel을 확인한 첫 경로는 W=I 또는 공통 voxel-volume. surface로 바꿀 때 실제 vertex-area 자료가 있으면 W를 명시해 사용한다. 면적이 없으면 면적가중이라고 부르지 않는다. 두 관측은 합치지 않고 민감도 가지로 비교한다.

**implementation:** P를 V×V로 만들지 않고 parcel별 가중 group sum/division 및 broadcast로 m,r를 얻는다. train-only PCA는 sqrt(W)r에서 적합하고 feature는 U_kᵀsqrt(W)r로 정의한다. G/r와 weight를 모든 split에 고정한다.

**unit checks:** 합성 벡터에서 G r≈0, P²y≈Py, m+r≈y, CᵀWr≈0를 dtype tolerance로 확인한다. 이는 계획된 수치검사이며 아직 실행 결과가 아니다.

**feature shapes:** M=G y는 [N,J], Rcoord=[N,k]. readout 입력은 M 또는 concat(M,Rcoord); plus의 열수/규제효과는 중복좌표/noise 대조로 평가한다.

**outputs:** 각 outer-held-out 표본의 A 예측·paired loss, participant별 H1 추정치/CI, 사전 k곡선, secondary H2/H3, 누수/공간/실행 manifest. AI 점수는 A의 대체물이 아님.

**timing:** 정적 시행 요약에는 동일 GLM/HRF·onset/duration·adjacent trial nuisance를 모든 공간조건에 고정한다. raw TR2s가 beta의 시간분해능을 뜻하지 않으며 beta 순서를 temporal foundation 입력으로 만들지 않는다.



## 5. 실험 순서

- **step:** 1
  
  **action:** 계약 QC
  
  **detail:** 실제 경로/헤더·label척도·stim_index mapping·내용중복·dense/atlas/면적·smoothing/GLM provenance를 확인한다. 확인되지 않은 필드는 미확인으로 둔다.
- **step:** 2
  
  **action:** split와 목표 고정
  
  **detail:** A 차원1개는 데이터 사전에 근거해 의미적으로 사전 선택하고 뇌예측 최고차원으로 고르지 않는다. target scale·V/S 세트·outer3 run-block folds와 content-group train exclusion·inner3 group folds를 고정한다. 독립 group 수가 부족하면 k/모형규모를 줄이고 설계를 수정한다.
- **step:** 3
  
  **action:** 비학습 투영·음성/양성대조
  
  **detail:** 합성 constant/known-nullspace 벡터로 weighted G/P 항등식과 residual 복구를 수치 검증한다. known m-only+공간상관 noise 및 알려진 잔차 신호로 전체 split/readout pipeline의 false-positive·감도를 검사한다.
- **step:** 4
  
  **action:** 선형 기준
  
  **detail:** training M,weighted R의 scale/PCA와 ridge를 적합한다. k=4/8/16 및 log alpha grid를 inner fold에서 선택하고 test에서 재선택하지 않는다. mean+noise/duplicate-coordinate를 함께 평가한다.
- **step:** 5
  
  **action:** 강한 평균 읽기와 주비교
  
  **detail:** 같은 inner budget의 kernel ridge 또는 고정 작은 MLP를 각 정보입력에 적합한다. strong m-only를 포함한 함수족 선택 후 같은 outer test에서 paired H1 loss를 계산한다. linear와 nonlinear 결과를 별도 표시한다.
- **step:** 6
  
  **action:** 공간·의미 대조
  
  **detail:** 감각/검수 의미 조건부 및 총효과를 나란히 계산한다. 실제 atlas와 사전20개 random-contiguous atlas를 동일 parcel수/면적/공간대역 조건으로 비교하되 MC정밀도를 확인한다. seed20은 계획이며 실행/생물학 N이 아니다. H3용 B의 scale·난도·신뢰도 비교가능성이 없으면 H3를 보류한다.
- **step:** 7
  
  **action:** 통계·재현성 범위
  
  **detail:** content/run cluster를 존중한 participant조건부 불확실성과 5명 개인효과를 보고한다. outer fold를 독립 반복으로 세지 않는다. 실제 반복이 있으면 별도 held-out-repeat 분석, 없으면 repeat reliability 없음. code/config/split/feature provenance와 실패로그를 보존한다.


## 6. 평가·통계

**primary loss:** A를 train mean/SD로 표준화하고 test에서 d_is=ell(A_s,f_m(m_is))-ell(A_s,f_plus(m_is,r_k,is))를 같은 squared-error 단위로 계산한다. 일차δ는 이 paired loss 감소 단위다. 총 예측과 V,S를 함께 넣은 조건부 예측을 별개 estimand로 모두 보고한다.

**strong baseline:** 각 입력조건에서 ridge와 kernel ridge(작은 N) 또는 파라미터 제한 MLP를 동일 inner selection 예산으로 비교한다. m-only 최강 사전 함수족과 plus 함수족의 selection-adjusted 외부 손실이 주비교다. linear-only 결과는 보조로 별도 표시한다.

**k selection:** k∈{4,8,16}를 사전 계획하되 훈련 rank와 자료 크기에 맞는 유효 k만 사용한다. inner CV 선택 k를 일차로 두고 모든 사전 k의 외부 곡선을 보고한다. test-best k를 일차로 바꾸지 않는다.

**independence:** 내용중복 원영상 family를 같은 outer fold로 묶고 run/GLM 공통오차를 고려한다. run block 보류와 겹치는 content group은 train에서 제외하는 규칙을 사전 고정한다. PCA·whitening·alpha·k·target/probe·matching은 inner train만 사용한다. 외부 test 신경으로 atlas·정렬을 재적합하지 않는다.

**statistics:** Horikawa 참가자5명의 개별 효과를 모두 제시한다. 참가자 조건부 새 자극 추론과 사람 모집단 추론을 구별한다. n=5 양측 exact sign-flip의 최소 p는 2/32=.0625이며 자극·voxel·atlas seed를 사람 N으로 세지 않는다. 계층/모수 CI는 작은 n 가정 민감도와 함께 표시하고, 비유의성을 동등성으로 읽지 않는다.

**conditional null:** 무조건 A permutation은 m의 실제 신호까지 제거하므로 H1의 정확 conditional null이라고 하지 않는다. known m-only 자료에 공간상관 noise를 주입한 null과, reduced-model 적합 및 exchangeability가 검증된 경우의 residual resampling을 비교한다. null 재표본화는 pipeline 재적합을 포함한다.

**minimum effect and equivalence:** 표준화 MSE의 δ0=.01(훈련 A분산의1%에 해당하는 손실감소)을 파일럿 감도목표로 제안한다. 이는 확립된 신경학적 최소효과가 아닌 명시적 실용 허용손실이다. 개발 noise/cluster simulation으로 δ0 검출과 CI coverage를 확인하고, 타당하지 않으면 .005/.02 민감도를 포함해 최종δ와 표본계획을 test 개봉 전에 고정한다. CI상한<δ면 해당 함수족의 잔차가치가 작음, CI전체가[-δ,δ]면 동등성, CI폭이 크면 미결정으로 구분한다.

**power:** subset cap를 충분한 power라고 주장하지 않는다. 개발/합성의 cluster·noise/개인차 범위에서 δ의 CI coverage와 detectable effect를 측정한 뒤 untouched test를 연다. 독립 반복 미확보일 때 모델기반 error calibration은 그 가정을 명시한 보조 결과다.

**multiplicity:** H1 1개 A차원/1개 고정 공간집합을 일차 가족으로 둔다. H2/H3는 별도 사전 이차 가족이며 추가 ROI/target/k 선택을 포함한 교정 또는 새 보류 자료 검증이 필요하다.

**reliability:** Horikawa 동일 ID 개인내 반복은 미확인. 반복이 없으면 repeat ceiling/crossnobis 반복 재현을 계산하지 않는다. 모델기반 GLM 오차는 그 가정을 붙여 다른 보조량으로 표시한다. NSD 반복 신뢰도를 Horikawa로 이식하지 않는다.



## 7. Ablation·대조

- mean+k spectrum-matched noise
- mean의 중복/가역 회전 좌표 재표현 후 readout 재적합
- 동일 effective df·regularization·전체 rank 대조
- 감각 V/검수 사건 S를 조건으로 한 전체·조건부 예측
- native/surface·registration·smoothing·공간대역·parcel 크기/면적을 명시한 random atlas
- matched 비정서 B와 양성 null-space 신호 주입
- strong nonlinear m-only
- 같은 G/P에서 PCA basis 가역회전과 readout 재적합
- 같은 GLM/HRF 및 영상 duration/run nuisance
- H2 atlas seed를 실제 참가자 표본과 구분
- 추가 정서차원 결과는 탐색으로 표시 또는 새로운 독립평가 사용


## 8. 확대·수정·중단 기준

**start:** 독립 A/실제 dense y/고정 G-W/내용군 split/초기projection수치검사 모두 통과하면 제한된 H1 파일럿 착수. 반복은 H1 predictive first pass의 필수조건은 아니지만 반복주장의 필수조건이다.

**expand:** known-null calibration과 held-out H1 CI 하한>사전δ, strong mean-only·noise/규제 대조에서도 방향이 유지되면 더 많은 자극/영역으로 확장하고 H2/H3를 사전 secondary 계획으로 검정한다. 소수5명에서 사람 모집단 확증으로 승격하지 않는다.

**revise:** H1이 linear-only이고 nonlinear mean으로 회수되면 readout 접근성 결과로 제한. H3 비교가능성이 없으면 일반 spatial prediction 결과로 기록. 잔차가 일반 spectrum/비정서 이득과 같으면 QC모듈로 축소.

**stop:** dense/A 부재, projection/공간 mapping 오류, 내용중복 split 불가능, raw 관측에서 target/labels 오연결, 수렴/메모리 불능이면 수정 전 멈춘다. δ 검정 precision 부족이면 무효과 결론 없이 추가표본/범위축소 계획으로 남긴다.

**equivalence:** CI가 사전[-δ,δ] 내이면 지정 관측·함수족에서 mean/plus 실용 동등. CI상한<δ이나 음의 큰 효과 가능성 있으면 잔차 이득이 작다는 판단과 동등성을 구별한다.



## 9. 실패 가능성과 주장 한계

- P의 영공간이 있다는 항등식 또는 m+r=y 복원 자체는 새로운 신경 발견이 아니다.
- 수치 k곡선 실패는 전체 영공간의 정보 부재가 아니다.
- A는 자극 집계 주석이며 개인 정서 상태·경험을 추정했다고 하지 않는다.
- H1/H2/H3의 결과를 혼합하지 않는다.
- 반복 미확보 시 repeat ceiling·독립 반복 재현 주장을 하지 않는다.
- 사람5명에 조건부인 자극 일반화와 사람 모집단을 구별한다.
- 면적·공간주파수·신뢰도 matching이 실제 평균화 총효과를 제거할 수 있어 원효과/보정효과를 모두 남긴다.
- CortexMAE나 CLIP의 공개 코드/URL은 실제 가중치 실행·호환성·생물학적 메커니즘 증거가 아니다.


## 근거

- [P001 The neural representation of visually evoked emotion is high-dimensional, categorical, and distributed across transmodal brain regions](https://raw.githubusercontent.com/OpenNeuroDatasets/ds002425/3f94b2bf9a75ddb62637c529d30dc40dd4ab5ba1/dataset_description.json)
- [P026 Scaling Vision Transformers for Functional MRI with Flat Maps](https://github.com/MedARC-AI/CortexMAE)
- [P051 Similarity of Neural Network Representations Revisited](https://proceedings.mlr.press/v97/kornblith19a.html)
- [P060 A Python Toolbox for Representational Similarity Analysis](https://github.com/rsagroup/rsatoolbox)
- [P063 Comparing spatial null models for brain maps](https://github.com/netneurolab/markello_spatialnulls/blob/master/manuscript/main.tex)
- [P100 Statistical inference on representational geometries](https://elifesciences.org/articles/82566)
- https://github.com/OpenNeuroDatasets/ds002425
- https://github.com/KamitaniLab/EmotionVideoNeuralRepresentationPython
- https://github.com/openai/CLIP

작성 원본: [04_brain_foundation](../agents/04_brain_foundation/pilot_PILOT03.json). [공통 자원·모델 근거](RESOURCE_AND_MODEL_PLAN.md).
