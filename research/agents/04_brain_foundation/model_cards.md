# Agent04 모델 가용성 카드 — 2026-11-12

공통 상태: 코드 설치·실행·학습·추론·체크포인트 다운로드는 수행하지 않았다. 공식 링크 또는 파일 목록의 존재 확인은 가중치의 실제 가용성 확인과 다르다. 아래 E1은 명시한 README·코드·본문 범위에만 적용한다. 임의 GPU 견적은 제시하지 않았다. `source_manifest.csv`에 URL·실패·파일 해시, `sources/observed_commits.json`에 관측한 Git commit을 보존했다.

## 1. SwiFT — BF01

- 정확한 실체: **SwiFT: Swin 4D fMRI Transformer**, Kim 등, NeurIPS 2023. [공식 저장소](https://github.com/Transconnectome/SwiFT), [논문](https://arxiv.org/abs/2307.05916). 논문 본문 미열람.
- 계산 역할: 4D fMRI → 공간·시간 표현 → 분류/회귀. 자극→뇌 인코더가 아니다. 4D shifted window attention과 instance/local-local temporal contrastive 설정을 제공한다.
- 학습 자료: 공식 `contrastive_pretrained.ckpt` 설명에 HCP·ABCD·UKB가 명시된다. 학습 피험자 ID와 현재 후보 데이터의 중복은 미검사.
- 입력/전처리: MNI 정렬·뇌마스크, 주로 whole-brain z-normalization, float16 volume 파일. 기본 도움말은 `96×96×96×20`, patch `6×6×6×1`, first window `2×2×2×2`를 제시한다. 이것은 tensor 모양이며 mm 해상도나 20초를 의미하지 않는다. TR·stride가 실제 시간 범위를 결정한다.
- 출력/공간·시간 제약: downstream head와 latent. 기본 전체-window pooling이 transient 정보를 얼마나 지우는지는 별도 검증해야 한다. 하위 피질 포함 여부는 crop/mask를 실제 확인해야 하며 whole-brain이라는 명칭만으로 보장하지 않는다.
- 체크포인트: 공식 `pretrained_models/` tree에서 `contrastive_pretrained.ckpt`, `hcp_sex_classification.ckpt`, `split_hcp.txt` 파일명 확인. 용량·해시·load 성공 미확인.
- 라이선스: 저장소 LICENSE Apache-2.0 직접 확인. 별도 모델 라이선스 문서와 데이터 이용조건은 추가 확인 대상.
- 컴퓨팅: README 샘플 스크립트 시험 환경 8×RTX3090. 최소 추론 GPU 수나 VRAM을 뜻하지 않는다.
- 재활용 판정: **조건부**. frozen feature 비교에 유망하나 입력 제작·실제 checkpoint load 검증이 필요하다.
- 근거: `sources/swift.txt` §§4,6,8; `swift_pretrained_tree.txt`; `swift_tail.txt`. 신뢰: 구현 설명 높음 / 실제 재현 미확인.

## 2. CortexMAE — BF02

- 정확한 실체: 모델명 CortexMAE, 논문 **Scaling Vision Transformers for Functional MRI with Flat Maps**, Lane 등. 공식 README는 ICML2026을 인용하고 [arXiv2510.13768](https://arxiv.org/abs/2510.13768)을 연결한다. 2025 preprint와 2026 게재를 두 논문으로 세지 않는다. [공식 저장소](https://github.com/MedARC-AI/CortexMAE).
- 계산 역할: fMRI → masked reconstruction/latent. P=parcel, F=flat map, V=cortex-only volume 표현을 비교하는 계열.
- 학습 자료: README상 HCP-YA 2.1K시간. 학습 shard 설정은 unrelated subject batch20개 중18개를 이용한다고 설명한다. 해당 설정이 모든 공개 variant에 같다고 가정하지 않는다.
- 입력: P `400×1` Schaefer400, F `224×560` flat map, V `465×512` cortex-only 배열. V의 465×512는 MRI의 물리 voxel grid 설명이 아니다. 기본 16frame, 시간 patch4, 공간 patch16(F), mask0.9 tube. 코드에 다른 atlas reader도 있으나 기본 P/F/V가 subcortex를 포함한다는 근거는 아니다.
- 시간 처리: `inference.py` Transform은 target TR1초로 필요시 선형 보간하고 frame normalization·±3 clipping을 적용한다. 코드 주석은 사전학습 자료 생성에서 pchip 보간을 썼다고 적는다. 샘플링 격자 통일이며 신경시간 해상도의 향상이 아니다. 기본16frame은 이 처리 후16초 구간에 해당하나 실제 입력 측정해상도는 원자료 TR에 제한된다.
- 출력: `run_embedding`의 patch embeds `(clips,tokens,dim)`; reconstruction 관련 API도 코드에 존재한다. 각 API의 반환자료를 실제 실행 확인하지 않았다.
- 체크포인트: [medarc/CortexMAE](https://huggingface.co/medarc/CortexMAE). 공식 registry에서 `input_space_v3/flat_lr1e-3_1/pretrain/checkpoint-last.pth` 등 경로와 다중seed/data/model-scale variant 확인. HuggingFace 접근403이므로 파일 다운로드·메타데이터 미검증.
- 라이선스: 코드 Apache-2.0, 모델 CC-BY-NC4.0 파일 직접 확인. HCP와 benchmark 자료는 별도 접근 요청을 요구한다.
- 컴퓨팅: 기본 pretrain config batch32/GPU,100epochs,float16 AMP. GPU 종류·수·벽시계시간 미확인. inference 기본 batch8, CUDA 가능시 사용/CPU fallback 코드 존재. 이것만으로 CPU 실용성을 보장하지 않는다.
- 재활용 판정: **비교 목적에 가장 구조화된 후보**. 동일 입력자료에서 P/F/V 차이를 검증할 수 있으나 정서 관련 하위피질 질문의 단독 도구로 부적합할 수 있다.
- 근거: `cortexmae.md`; `cortex_config.txt`; `cortex_inference.txt`; 두 license. 신뢰: 구현·라이선스 높음 / 본문 결과·가중치 실행 미확인.

## 3. TRIBE v2 — BF03

- 정확한 실체: **A foundation model of vision, audition, and language for in-silico neuroscience**, d’Ascoli 등, [arXiv2605.04326](https://arxiv.org/abs/2605.04326), [공식 저장소](https://github.com/facebookresearch/tribev2). 본문 미열람.
- 계산 역할: video/audio/text → 모달별 feature → 통합 Transformer → fMRI. brain-input foundation encoder와 입력방향이 다르다.
- 입력: 공개 API는 동영상·오디오·텍스트 파일 및 event dataframe. 코드상 text-only demo는 TTS 및 transcription을 거쳐 timing을 구성하므로 문장 자체의 순수한 언어 조건과 합성 타이밍을 구분해야 한다. 이 사실은 음성특징 연구축을 제안하는 것이 아니다.
- backbone: 기본 설정 Llama3.2-3B, V-JEPA2 `vjepa2-vitg-fpc64-256`, Wav2VecBert. DINOv2 image 옵션도 있지만 기본 features는 text/audio/video다. 전체 upstream checkpoint와 라이선스에 대한 별도 감사 필요.
- 학습 자료: `defaults.py`는 Algonauts2025Bold/Wen2017/Lahner2024Bold/Lebel2023Bold를 열거. 이를 논문 전체 corpus나 피험자·시간수의 완전한 검증으로 대체하지 않는다.
- 출력: 공개 pretrained inference는 평균 피험자의 `(n_timesteps,n_vertices)`, fsaverage5 약2만vertex. README는 혈역학지연 보정용5초 offset을 명시한다. 코드가 subcortical grid를 포함한다는 사실은 공개 기본 checkpoint의 subcortical 예측 지원을 뜻하지 않는다.
- 시간해상도: default feature/data frequency2Hz, neuro extractor1Hz가 공존한다. `predict`는 `data.TR` 단위 segment 출력을 만든다. **배포 checkpoint의 config를 받기 전 최종 출력Hz를 확정하지 않는다.** 어떤 경우도 fMRI 실측보다 세밀한 신경시간 해상도의 증거가 아니다.
- 목적함수/개인화: MSE, modality dropout0.3, subject dropout0.1, subject-specific layer·low-rank head 코드 확인. 공개 wrapper는 `average_subjects=True`를 사용한다.
- 체크포인트: [facebook/tribev2](https://huggingface.co/facebook/tribev2), 코드 기본 `config.yaml`, `best.ckpt`. 링크만 확인, 파일·실행 미확인.
- 라이선스: 프로젝트 CC-BY-NC4.0. upstream 모델·자료와 별도이다.
- 컴퓨팅: default Slurm 자원1GPU/128GB CPU RAM/72h timeout. timeout은 실제 학습시간이 아니다. feature extraction이 별도 GPU job을 사용하며 실제 추론VRAM 미확인.
- 재활용 판정: **자극 조건부 예측 baseline으로 유망**. 출력=실제 개인 뇌반응 또는 인과적 simulator라는 해석은 허용하지 않는다.
- 근거: `tribev2.md`; `tribe_config.txt`; `tribe_model.txt`; `tribe_demo.txt`; `tribe_license.txt`.

## 4. Brain-Mamba / BrainMamba — BF04

- 정확한 실체: **Brain-Mamba: Encoding Brain Activity via Selective State Space Models**, Ali Behrouz·Farnoosh Hashemi, CHIL2024, PMLR248:233–250. [공식 서지](https://proceedings.mlr.press/v248/behrouz24a.html), [출판사 PDF](https://raw.githubusercontent.com/mlresearch/v248/main/assets/behrouz24a/behrouz24a.pdf). 본문·부록 직접 읽음.
- 동일성 주의: 논문 제목은 Brain-Mamba, 본문 모델명 BrainMamba. `whuhxb/BrainMamba`는 인용만 있는 README, `ucalyptus/brainmamba`는 다른 제목을 표방한 제3자 구현이다. 이들을 공식 코드나 공식 checkpoint로 승격하지 않았다. whuhxb README의 arXiv badge는 논문식별 근거로 사용하지 않는다.
- 계산 역할: 신경 multivariate time series와 Pearson 기반 연결 그래프 → BTMamba/BNMamba → fusion gate → 분류·이상탐지. 그래프 노드 순서와 입력 의존 scan은 과학적 가정으로 검사할 수 있다.
- 학습 자료: BVFC, BVFC-MEG, ADHD, TUH-EEG, MPI-EEG, HCP-Mental, HCP-Age. modalities fMRI/MEG/EEG. 공동의 범용 pretrained checkpoint가 있다는 뜻은 아니다.
- 입출력/해상도: BVFC Table5 평균11776node, HCP1000, ADHD400; 시계열 길이는 자료에 의존. ROI/voxel/channel를 동일 물리 공간해상도로 보지 않는다. 출력은 latent와 task 결과이며 자극에서 neural response를 생성하는 모델이 아니다.
- 학습/성능: encoder 사이 상호정보량 사전학습. Table2/3 및Fig2–4 직접 확인. AppendixD는 random70/10/20분할과 batch64를 명시. 현재 독립 피험자·자극·반복 분할이 충분히 기술됐다고 말할 수 없다. 합성corruption 강건성 실험과 미검증 OOD 강건성은 구분한다.
- 체크포인트/코드: 공식 PMLR metadata `software`가 연결하는 [GraphMamba/BrainMamba](https://github.com/GraphMamba/BrainMamba)는2026-11-12에404. 가중치·실행코드·code license 미확인. 논문 copyright는 코드 라이선스를 대신하지 않는다.
- 컴퓨팅: scaling 그림은 확인했으나 실행GPU·VRAM·시간의 확정값은 확인하지 못함. 제3자 repo의H100 언급을 원논문의 요구사항으로 복사하지 않는다.
- 저자 후속과제: AppendixE pp249–250의 학습형 연결망, 피험자품질 강건성, 다중모달 및 distribution shift평가. 자세한 분리는 `discussion_mining.csv`.
- 후속 모델 구분: Mamba2/3는 upstream SSM 후속이며 Brain-Mamba 후속 실험으로 확인되지 않았다. BrainMamba 후속작을 검색 범위 내에서 확정하지 못했다.
- 재활용 판정: **즉시 pretrained 활용 보류**. 계산원리·반증설계는 재사용 가능하나 공식 코드 복구 또는 독립 재구현 검증이 필요하다.

## 5. Brain-JEPA — BF05

[공식 코드](https://github.com/Eric-LRL/Brain-JEPA), [논문](https://arxiv.org/abs/2409.19407). NeurIPS2024 Spotlight는 공식 README에서 확인. fMRI450ROI(400Schaefer+50Tian) → latent prediction. population brain gradient positioning과 Cross-ROI/Cross-Time/Double-Cross masking. config예시 입력450×160, patch_size16, ViT-base/predictor6층; 초 단위 길이는 원자료TR·downsample 확인 후 정한다. UKB/HCP-Aging/ADNI/MACC가 README에 열거되며 정확한 pretrain/eval 규모는 미확인. [GoogleDrive checkpoint 링크](https://drive.google.com/drive/folders/1zoe5zjWkj2KY824XWTukrXxrMno2mlN5?usp=sharing)는 제공되지만 다운로드 미수행. README상 pretrain4×A10040GB. root tree에서 LICENSE파일을 찾지 못했으므로 공개코드=자유재배포로 간주하지 않는다. reconstruction code는TODO. **재활용 조건부**, 권한·가중치 load·gradient생성의 학습누수 점검 필요. 공식 README는 Brain Harmony를 새 버전으로 연결하나 두 학습 목표와 입력은 구분한다. 근거 `brainjepa.md`, `jepa_config.txt`, `jepa_repo.txt`.

## 6. Brain Harmony / BrainHarmonix — BF06

[공식 코드](https://github.com/hzlab/Brain-Harmony), [논문](https://arxiv.org/abs/2509.24693), NeurIPS2025. 제목 Brain Harmony, 구현 이름 BrainHarmonix. fMRI/T1/joint 모델과 embedding→pretrain→finetune pipeline. 공개 stage0 config의UKB_fusion,400corticalROI, nominal400×864(48×18)과sequence490/시간 변환 옵션을 확인했다. 이 예시를 모든모델 입력이나 실제학습 자료 전체로 확장하지 않는다. structural입력 세부해상도·모든목적함수·공식GPU비용은 미확인. [가중치Drive링크](https://drive.google.com/drive/folders/12MkUAOcegU60YVlK8u8_Owmgk4eQVheB?usp=sharing)만 확인. README license badge는CC-BY-NC-SA4.0이나 별도 LICENSE파일·모델조건 미확인. **재활용 조건부**. 구조MRI가 없거나 공간등록이 일치하지 않으면 joint checkpoint 경로를 가정할 수 없다. 근거 `brainharmony.md`, `harmony_config.txt`.

## 7. BrainLM — 모델코드 확인, 논문 집계 제외

[공식 코드](https://github.com/vandijklab/BrainLM)는 masked prediction 기반 뇌표현모델과UKBiobank pretraining을 설명한다. [가중치 링크](https://huggingface.co/vandijklab/brainlm)는111M/650M모델을 제시한다. notebook은A424parcellation,200timepoint,temporalpatch20,mask0.75 예시와CLS집계를 사용한다. 별도configuration에는424×490/patch49기본이 있어 **실제 checkpoint별config가 기준**이다. notebook의 미정의사용자변수와 경로도 있어 그대로 실행되었다고 주장하지 않는다. 저장소LICENSE는CC-BY-NC-ND4.0 직접 확인; 변경·재배포 조건은 실제사용 전에 검토해야 한다. 학습script의1×RTX3090·32GB hostRAM·48h limit은 작은hidden128/4layer예시로111M/650M훈련비용에 적용할 수 없다. **정확 논문서지의1차출처 일치확인이 완료되지 않아papers.csv10편 집계에 제외**했다. 코드 문서 E1, 학술서지 E0이며 추가확인 필요. 근거 `brainlm.md`, `brainlm_config.txt`, `brainlm_tutorial.txt`, `brainlm_license.txt`, `brainlm_train.txt`.

## 8. 원 계산원리와 baseline

- **TFF(BF07)**: [공식 코드](https://github.com/GonyRosenman/TFF). 3DCNN + temporalTransformer 및 reconstruction/downstream head, HCP/UCLA. 정확 hyperparameter 공개가 README에 미래형으로 남고 checkpoint/license/hardware확인 안됨. 최근모델의 우월성이 목적함수·비용때문인지 검사할 baseline.
- **MAE(BF08)**: [공식 코드](https://github.com/facebookresearch/mae). 이미지mask복원, ViT-B/L/H 변환가중치 링크, CC-BY-NC4.0. 뇌checkpoint가 아님. fMRI mask 설계의 원리적 대조에 사용.
- **I-JEPA(BF09)**: [공식 코드](https://github.com/facebookresearch/ijepa). 이미지부분latent예측,ImageNet1K/22K가중치 링크. README ViT-H/14재현16×A10080GB; 뇌모델비용에 그대로 적용하지 않는다. LICENSE CC-BY-NC4.0. 정적인 부분예측을 미래신경상태예측과 혼동하지 않는다.
- **Mamba(BF10)**: [공식 코드](https://github.com/state-spaces/mamba), Apache2.0. sequence[B,L,D]→동일shapeblock, Pile/SlimPajama언어가중치. Brain-Mamba가중치가 아니다. Mamba2[arXiv2405.21060](https://arxiv.org/abs/2405.21060), Mamba3[arXiv2603.15569](https://arxiv.org/abs/2603.15569) 항목과구현을README에서 식별했지만 본문은 미검증이며10편에 추가집계하지 않았다.

모든 카드: origin_agent=04_brain_foundation, verified_on=2026-11-12. 직접조회 근거에 한정해 신뢰하며 checkpoint가동·성능·데이터적합성은 미확인이다.
