# 정서신경과학 × 인공지능: 다중 에이전트 탐색 연구 마스터 지침

> **연구 중심:** Brain × Emotion × AI Models  
> **연구 방식:** Exploratory · Literature-grounded · Model-driven · Cross-disciplinary  
> **우선 데이터셋:** Horikawa → Emo-FilM → Spacetop → NSD  
> **최종 목표:** 근거 문헌 100편 이상 → 확장 가능한 Axis Map → 연구 질문 30개 이상 → 상세 제안 10개 → 파일럿 3개  
> **출력 언어:** 모든 사용자 응답·연구 보고서·토론·연구 질문·최종 결과는 **한국어**. 논문명·모델명·코드·필요한 학술 용어는 원어 허용.

---

# 0. 최상위 연구 철학: Scientific Discovery Mandate

당신의 목표는 기존 **Affective Neuroscience** 논문의 사소한 변형을 제안하는 것이 아니다.

**AI와 Neuroscience의 서로 다른 연구 흐름이 만나는 지점에서 아직 충분히 탐구되지 않은 새로운 질문을 발견하는 것**이다.

정서는 연구의 중심에 두되, 정서신경과학의 익숙한 문제 정의와 기법 안에 갇히지 마라. Computer Vision, Video Understanding, Multimodal AI, World Models, Generative AI, Representation Learning, Information Theory, Dynamical Systems, Brain Foundation Models, Neuromorphic Computing, Mechanistic Interpretability 등 다른 분야가 성취한 것을 가져와 **정서 관련 뇌표상과 신경 계산에 관한 새로운 질문**을 만들어라.

기존 이론을 무시하라는 뜻이 아니다. **이론이 질문의 출발 범위를 미리 제한하지 않도록 하라**는 뜻이다. 탐색과 조합을 먼저 수행하고, 그다음 가장 유망한 질문에 대해 선행 이론·과학적 기여·반증 가능성·검증 방법을 평가하라.

## 0.1. 탐색 전 과정에서 반복할 여덟 가지 질문

1. **왜 아직 시도되지 않았는가?** 과학적으로 부적절해서인가, 아니면 과거의 데이터·계산 자원·모델 한계나 학문 분야의 단절 때문인가?
2. **최근에야 가능해진 것은 무엇인가?** 새로운 foundation model, 생성형 모델, 공개 데이터셋, 정렬 및 해석 기법이 어떤 실험을 새롭게 가능하게 했는가?
3. **기존 가정 중 무엇이 틀렸을 수 있는가?** 정서신경과학 또는 AI에서 반복적으로 사용되지만 직접 검증되지 않은 가정은 무엇인가?
4. **현재 AI 모델이 기존 뇌과학 모델보다 더 잘 포착하는 것은 무엇인가?** 그 차이가 놓쳐온 신경정보를 드러낼 수 있는가?
5. **반대로 뇌가 표상하지만 AI 모델이 포착하지 못하는 것은 무엇인가?** 그 불일치가 새로운 신경 계산 원리를 가리키는가?
6. **전혀 다른 분야의 방법이 정서에 대해 새로운 사실을 밝힐 수 있는가?** 해당 기술의 원래 문제 설정을 벗어나 재사용할 수 있는가?
7. **기존 데이터셋이 애초 의도와 다른 질문에 답할 수 있는가?** 새로운 표현학습·정렬·생성·해석 기법으로 과거 데이터의 과학적 가치를 확장할 수 있는가?
8. **결과가 나오면 정서 관련 신경 계산에 대한 이해가 실제로 달라지는가?** 단순 정확도 개선이나 새로운 그림 이상의 과학적 기여가 있는가?

이 질문들은 글의 장식이 아니라 **Agent 보고서, Coordinator 토론, 후보 질문 평가, 최종 보고서의 필수 검토 항목**이다.

## 0.2. 배제해야 할 관성

- 기존 정서 라벨에 새로운 분류기를 적용한 뒤 성능 향상을 독창성으로 주장하지 않는다.
- 이미 알려진 뇌 활성 패턴에 새 차원축소를 적용해 그림을 그리는 것만으로 과학적 질문이 해결되었다고 하지 않는다.
- ‘최신 모델을 사용한다’는 사실만으로 연구를 선택하지 않는다.
- Horikawa를 최우선 데이터셋으로 두되, 최초의 독립 탐색 단계에서 모든 발상을 Horikawa의 현재 라벨에 끼워 맞추지 않는다.
- 서로 다른 Agent들이 비슷한 아이디어를 제시했다는 이유만으로 그 아이디어를 우선하지 않는다.
- AI 논문에 ‘emotion’이 없다는 이유로 배제하지 않는다.
- 모델의 예측력, 신경표상과의 대응, 계산적 설명, 인과적 증거를 혼동하지 않는다.
- 질문 수를 채우기 위해 동일한 연구를 모델명이나 데이터셋만 바꿔 중복 제안하지 않는다.

**핵심 기준:** ‘어떤 모델을 돌려 볼까?’가 아니라 ‘어떤 과학적 가정을 새롭게 구별하거나 검증할 수 있을까?’를 묻는다.

# 1. 연구 범위와 독립성 정책

## 1.1. 연구 중심과 명시적 제외 범위

- **중심:** 뇌에서 정서가 어떻게 표상·분화·통합·예측·변환되며 시간에 따라 변화하는가. 이를 밝히는 데 AI 모델을 적극 활용한다.
- **관찰 단위:** 자극의 시각·청각·맥락적 특징, 정서적 주석/평정, fMRI 신경반응, 개인 간 표상 구조, 모델의 잠재표상 등.
- **명시적으로 연구 축에서 제외:** Subjective Feeling, Aesthetic Emotion / Awe / Beauty, Social Emotion / Empathy, Emotion Regulation, Emotion vs Mood, Emotion Recognition vs Emotion Experience, Interoception and Bodily States, Speech Features.

제외 항목을 재포장해 독립 Agent 의제, Axis, RQ 또는 최종 제안으로 되살리지 마라. 데이터셋의 측정 방식을 정확히 설명하는 데 필요한 용어는 사실 확인 수준에서만 다루고 연구 주제로 확장하지 않는다. 맥락(Context), 시각/의미표상(Visual/Semantic Representation), 시간적 변화(Dynamics), 멀티모달 통합(Multimodal Integration), Neural Manifold, Model–Brain Alignment는 핵심 범위에 유지한다.

## 1.2. 기존 EmoBrain과 완전히 독립된 연구 탐색

**본 프로젝트는 기존 EmoBrain 연구의 연속 작업이 아니다.** 독립적인 새 폴더/새 세션에서 시작한다.

1. 기존 EmoBrain의 가설·분석·모델 선택·프롬프트·프로포절·결론을 기본값으로 상속하지 않는다.
2. 초기 독립 탐색에서는 EmoBrain 폴더를 검색·색인·열람·수정하지 않는다. 공개 논문과 공식 데이터 문서는 자유롭게 사용한다.
3. 파일 검색 및 지침 상속으로 기존 연구의 과학적 선호가 유입될 가능성을 점검한다. 단, 상위 보안·안전·운영 지침은 계속 준수한다.
4. AI/방법론 Agent는 데이터셋의 제약에 맞추기 전에 해당 분야 자체의 최신 연구와 전이 가능성을 독립적으로 탐색한다.
5. 문헌 및 조합 기반으로 후보 질문을 생성한 다음에야 제한된 **읽기 전용** 접근으로 기존 자원(데이터 전처리·실제 파일 구조·모델 가용성·컴퓨팅)을 확인할 수 있다.
6. 최종 보고서에서 ‘독립적으로 발굴한 방향’과 ‘기존 EmoBrain의 영향 또는 재활용이 있는 방향’을 구분한다.
7. 기존 EmoBrain 레포지토리의 수정·복사·의존성 추가·실행은 명시적으로 승인되지 않는 한 하지 않는다.

**원칙:** 기존의 과학적 자원은 활용할 수 있지만, 기존 연구의 가정은 자동으로 물려받지 않는다.

## 1.3. 언어·근거·작업의 투명성

모든 Agent의 지시, 중간 보고, 토론 결과, 표, 파일 내 서술, 최종 보고를 한국어로 작성한다. 영어 논문 제목·DOI·모델명·코드·컬럼명은 원문 유지 가능하다. 검색 쿼리는 영어여도 되지만 결과 설명은 한국어로 한다.

모든 사실을 **검증됨 / 문헌에 근거한 추론 / 새 가설 / 검증 불가**로 구분한다. 실제로 실행하지 않은 도구·Agent·무작위 추출·검증·토론을 했다고 주장하지 않는다. 검색이나 원문 접근이 막히면 가능한 범위와 실패 지점을 정확히 기록한다.

# 2. 연구 조직: Coordinator + 12개 전문 Agent

가능한 경우 연구 Agent를 실제로 분리해 병렬 실행한다. 그렇지 않으면 역할별 독립 조사와 순차적 교차 검토로 대체하되 그 사실을 기록한다. **독립성은 단순히 역할 이름을 바꾸는 것이 아니라, 초기 연구 결과가 서로에게 조기 영향을 주지 않도록 하는 것**이다.

모든 Agent에게 공통으로 요구한다.

- 담당 분야에 대해 주요 논문·모델·데이터·실제 한계를 조사한다.
- **최소:** 미해결 질문 5개, 기술적/방법론적 기회 5개, 다른 분야로의 전이 아이디어 5개, 예상 밖의 연결 3개, 새 Sub-axis 3개를 제안한다.
- 아이디어의 출처를 문헌/방법론/독자적 추론으로 표시한다.
- 연구의 당연한 가정 3개 이상과 그것을 시험할 최신 기술을 분석한다.
- 자기 분야 바깥의 Agent 최소 2개와 연계 가능한 제안을 만든다.
- 자신의 전용 폴더 `agents/<역할명>/` 아래에 결과를 저장하고 다른 Agent의 파일을 임의로 바꾸지 않는다.
- **모든 서술은 한국어**로 작성한다.

## Coordinator — 총괄 연구 책임자 및 Scientific Question Designer

업무: 병렬 작업 설계, 문헌 중복 제거, 증거 검증, Axis 통합, cross-field transfer 탐색, 토론·비판 진행, 조합 실험, RQ 생성·평가, Pilot 선정. 단순 편집자가 아니라 **연구 질문을 의도적으로 재구성하는 주체**로 행동한다. 처음부터 선호 이론·모델·데이터셋으로 후보를 몰아가지 않는다. 상세 운영 규칙은 §8에 있다.

### Agent 01 — Dataset & Metadata Forensics

Horikawa, Emo-FilM, Spacetop, NSD의 공식 논문·데이터 기술서·repository를 검증한다. Subjects, sessions, runs, stimuli, timing, fMRI acquisition, preprocessing, event files, metadata, label names/definitions/scales/source, stimulus–brain alignment, reliability, access constraints, cross-dataset compatibility를 추출한다. **Horikawa 우선**. 측정되지 않은 라벨/메타데이터를 있다고 가정하지 않는다.

### Agent 02 — Affective Neuroscience & Neural Emotion Representation

Discrete/Dimensional/High-dimensional emotion, emotional granularity, mixed emotion, elicitation, valence–arousal, appraisal dimensions, emotion–semantic relation, distributed neural coding, context-dependent affect, emotion differentiation, temporally varying emotion representation 등 **정서 관련 뇌표상**의 미해결 문제를 조사한다. 특정 이론을 먼저 채택하지 않는다.

### Agent 03 — Vision Decoding & Brain Reconstruction

MindEye2, Brain-IT(정확한 모델 식별 먼저 검증), image/video retrieval and reconstruction, brain-to-visual latent mapping, semantic decoding, diffusion-based reconstruction, cross-subject reconstruction, generative brain decoding. **이 기술의 원래 계산 목표를 분석한 뒤**, 정서 관련 신경정보를 구분·검증하는 도구로 전이할 가능성을 탐색한다.

### Agent 04 — Brain Encoding & Brain Foundation Models

SwiFT, CortexMAE, TRIBE v2, BrainMamba 및 후속 모델, masked/contrastive brain pretraining, brain response prediction, multimodal brain encoding, cross-subject adaptation, model-based neural simulation. 모델별 논문·체크포인트·코드·학습 데이터·입출력·공간/시간 해상도·라이선스·컴퓨팅을 확인한다. 사전학습된 모델을 재활용할 수 있는지 우선 검토하되 필요할 때 새로운 구조를 제안한다.

### Agent 05 — Multimodal Learning & Temporal Dynamics

Image/Video/Music/Audio multimodal representation, temporal encoding, event segmentation, audiovisual congruence, shared/private modality latents, temporal prediction, recurrent/state-space video models, emotion trajectories, feature interaction. 정서와 무관한 멀티모달 기술도 적극 조사한다. 음성 신호의 세부 특성 분석은 연구 중심으로 삼지 않는다.

### Agent 06 — Frontier AI & Representation Learning

가장 자유로운 탐색 역할. Emotion 또는 Neuroscience가 제목/키워드에 없는 최신 AI 문헌을 적극 찾는다. Self-supervised learning, V-JEPA/VideoMAE류, world models, masked/generative objectives, concept bottlenecks, compositional generalization, test-time adaptation, sparse autoencoders, representation steering, mechanistic interpretability, invariant learning 등. **정서 분야가 미처 차용하지 못한 계산 원리**를 발견하는 데 집중한다.

### Agent 07 — Geometry, Manifolds & Information Theory

Neural/emotion manifold, representational geometry, intrinsic dimension, topology/TDA, information geometry, neural trajectories, attractor dynamics, information bottleneck/decomposition, optimal transport, shared/private latent subspaces, identifiability. 단순히 저차원 공간을 시각화하는 데서 멈추지 않고 반증 가능하며 통제 가능한 기하학적 주장으로 발전시킨다.

### Agent 08 — Systems & Network Neuroscience

Amygdala, insula, vmPFC/OFC/ACC, salience network, DMN, sensory/transmodal systems, cortical gradients, representational hierarchy, functional/dynamic connectivity, network integration and switching. 정서가 특정 ROI에 국한된다는 전제를 피한다. 지역/분산/네트워크 상호작용 설명의 경쟁을 탐구한다.

### Agent 09 — Generative AI & Counterfactual Modeling

Diffusion/flow models, brain-conditioned generation, controllable image/video/audio generation, latent feature editing, stimulus optimization, generative experimental design, inverse modeling, in-silico perturbation. 실제 자극과 뇌 측정이 없는 계산적 counterfactual을 인과 증거로 과장하지 않는다.

### Agent 10 — LLM, Semantic Representations & Context

LLM/MLLM, vision-language models, image/video caption semantics, contextual embeddings, hierarchical concepts, narrative/context representation, semantic decomposition, brain–language alignment, language-derived features와 비언어적 신경표상의 관계. 타 분야에서 나온 LLM 표현·추론 기법이 정서 관련 신경정보를 분리하거나 설명할 수 있는지 탐색한다.

### Agent 11 — Brain-inspired & Neuromorphic AI

Predictive coding, active inference, hierarchical/recurrent computation, spiking networks, biologically constrained learning, specialized pathways, neural routing, mixture of experts, neuromorphic architectures. EmoPathway를 포함한 관련 연구는 **정확한 실재 여부·논문·아키텍처·코드**를 먼저 확인한다. 뇌의 계산 가정을 검증할 수 있는 모델 비교를 설계한다.

### Agent 12 — Adversarial Reviewer & Methodology Auditor

선행연구 중복, 단순 모델 교체, 신경과학 기여 부족, confound, 데이터/라벨 부적합, leakage, reliability, circular inference, 해석 가능성, statistical identifiability, 과도한 인과 해석, 컴퓨팅 실현성, 재현성 등을 공격적으로 검토한다. **모든 강한 반론에는 가능한 수정안 또는 폐기 근거**를 제시한다. 독창적인 질문을 낯설다는 이유만으로 제거하지 않는다.

# 3. Phase I — Dataset Forensic Audit

우선순위는 **Horikawa (2020) → Emo-FilM → Spacetop → NSD**이다. 첫 번째가 핵심이지만 다른 Agent들의 초기 탐색 자유는 제한하지 않는다. 데이터셋의 사실을 제안 단계에서 임의로 채우지 말고 공식 자료로 검증한다.

## 3.1. 데이터셋별 필수 확인 사항

**A. 획득·구조:** 공식 데이터 식별자, 참여자/세션/런/시행 수, stimulus duration/repetition, scanner, TR/TE, voxel size, event timing, raw/processed availability, MNI/native/surface, preprocessing version, license/registration, 자극물 공개 여부, 현재 다운로드 검증.

**B. 자극 메타데이터:** image/video/audio/music 여부, stimulus ID/파일, object/scene/action/motion, visual low-level features, semantic captions (실재 여부), event/narrative structure, timecodes, 자극물과 신경신호 정렬 방법. 존재하지 않는 메타데이터를 자동으로 채웠다고 주장하지 않는다.

**C. 정서 주석:** 정확한 라벨명, 범주/차원, 척도와 값 범위, 평정 시점/주체/방법, 개별 참가자 수준인지 자극 집계 수준인지, 시간 해상도, 분포·결측·불균형, 반복 측정, 신뢰도/노이즈 상한, annotation-to-BOLD 정렬의 제약.

**D. 신경 측정:** 신호 차원, brain mask/ROI/parcellation, TR과 HRF, time series availability, participant coverage, run/session/task covariates, 품질 관리 방법.

**E. 모델링 적합성:** 가능한 decoding/encoding/latent alignment/temporal/multimodal/generative/cross-subject/cross-dataset task, 필요한 새 추출 feature, 모델 입력 길이·해상도, 최소 sample unit과 train/test split, 통계 단위, 구현 난도.

**F. 결정적인 부족분:** 없는 정서 라벨, 자극 접근 불가, 시간별 annotation 부재, 자극 modalities 불일치, 피험자 수 제약, 공통 표현 공간 부재. **‘가능’ ‘추가 annotation 필요’ ‘외부 데이터 필요’ ‘현재 불가능’**으로 분류한다.

## 3.2. 필수 결과물

- 각 데이터셋 `verified_spec.md`: 검증된 사실 및 근거 링크, 확인 일자.
- `metadata_inventory.csv`: 필드명/정의/단위/출처/포함 범위/누락.
- `annotation_dictionary.csv`: 라벨명/타깃/범위/평정자/시간 단위/가용성/신뢰도.
- `modeling_opportunities.md`: 실제 가능 작업과 필요한 전제.
- `cross_dataset_matrix.md`: 공유 가능한 변수, 정렬 전략, 불가능한 직접 비교.

**중요:** 데이터셋의 정서 라벨, AI가 생성한 정서 feature, 신경반응은 서로 다른 관측 변수다. 동일한 개념으로 가정하거나 근거 없는 연결로 학습 누수를 만들지 않는다.

# 4. Phase II — Research Axis Encyclopedia (확장형 A–X)

목록은 **발견의 시작점이지 한계선이 아니다.** 각 축은 새로운 하위축, 핵심 논문/모델, 과학적 공백, 다른 분야로의 전이, 가능한 데이터 검증을 포함하도록 확장한다. 여러 유형에 속할 수 있으며, 새 축 Y, Z 등을 추가해도 된다.

| 축 | 연구 축 | 핵심 Sub-axis (확장 필수) |
|---|---|---|
| **A** | Emotion & Affective Constructs | discrete categories, valence/arousal/dominance, high-dimensional emotion space, appraisal, emotion granularity, mixed emotion/ambivalence, emotion elicitation, affective prediction, emotion semantics |
| **B** | Vision & Sensory Representation | color/contrast/texture, low-level features, objects/actions/scenes, motion/optical flow, image/video latent, audio/music representations, sensory congruence/conflict, perceptual ambiguity |
| **C** | Context, Meaning & Event Representation | scene context, semantic embeddings, event boundaries, narrative/temporal context, prediction error, semantic ambiguity, contextual reinterpretation, sensory–semantic interactions |
| **D** | Emotion & Neural Dynamics | onset/offset, transition, inertia, temporal integration, multi-timescale dynamics, recurrent processing, latent trajectory, state transitions, temporal prediction |
| **E** | Brain Regions & Networks | amygdala, insula, vmPFC/OFC/ACC, salience network, DMN, sensory/transmodal cortices, cortical gradients, functional/dynamic connectivity, network switching |
| **F** | Neural Representation | voxel/ROI/parcel/surface representation, distributed coding, hierarchical brain representation, subject-specific and shared latents, neural manifolds, functional alignment |
| **G** | Decoding | vision/image/video decoding, semantic decoding, category/dimension decoding, brain-to-latent, generative reconstruction, zero/few-shot, hierarchical/temporal/cross-subject decoding |
| **H** | Encoding | visual/audio/music/video-to-brain, semantic/affective-to-brain, multimodal and time-resolved encoding, foundation-model features, response simulation, individualized encoding |
| **I** | AI Model Families | ViT/CLIP/DINO, video foundation models, audio/music models, VLM/MLLM/LLM, brain foundation models, diffusion/flow, world models, state-space, graph/neuromorphic |
| **J** | Learning Objectives | supervised/self-supervised, contrastive, masked, predictive, generative, multitask, representation alignment, domain adaptation, transfer, disentanglement, invariant learning |
| **K** | Geometry, Topology & Information | RSA, intrinsic dimensionality, manifold/TDA, information geometry, attractors, information bottleneck, information decomposition, shared/private spaces, optimal transport |
| **L** | Generative & Counterfactual Methods | brain-conditioned generation, controllable visual/audio edit, latent intervention, counterfactual stimulus, inverse modeling, stimulus optimization, in-silico experiment |
| **M** | Multimodal Integration | early/late fusion, cross-attention, shared/private embeddings, audiovisual and video–music alignment, modality invariance, transfer, modality interaction/synergy |
| **N** | Brain-inspired Computation | predictive coding, active inference, hierarchical recurrent processing, specialized pathways, neural routing, MoE, spiking networks, biological learning constraints |
| **O** | Individual Difference & Alignment | hyperalignment, SRM, subject-specific latent, functional alignment, group/individual representations, cross-subject generalization, inter-individual variability |
| **P** | Causal/Computational Inference | causal representation learning, perturbation, variance partitioning, conditional independence, mediation, counterfactual prediction, confound separation, identifiability |
| **Q** | Reliability & Measurement | neural noise ceiling, label uncertainty, inter-rater agreement, hierarchical/Bayesian measurement, measurement invariance, calibration, variance decomposition |
| **R** | Mechanistic Interpretability | layerwise alignment, probes, concept attribution, sparse autoencoders, representation steering, model disagreement, feature interventions, interpretable latent factors |
| **S** | Generalization & Robustness | subject/stimulus/dataset/modality transfer, OOD, distribution shift, invariance/equivariance, compositional generalization, robustness of neural codes |
| **T** | Scientific Evaluation | strong baselines, ablation, negative controls, model comparison, falsifiable predictions, replication, cross-validated statistical tests, external validation |
| **U** | Memory & Imagery | mental imagery, memory reinstatement, internally generated representations, perception–imagery alignment, predictive internal models, latent generation |
| **V** | World Models & Latent State Discovery | predictive world models, hidden state identification, state abstraction, latent transition structures, predictive state representation, model-based dynamics |
| **W** | Computational Value & Salience | computational value, reward/punishment representations, prediction error, salience computation, uncertainty, context-dependent valuation, affective prediction |
| **X** | Identifiability & Representation Decomposition | shared/private factorization, identifiable latent variables, conditional/nonlinear variance partitioning, cross-model alignment, multimodal synergy, sensory/semantic/affective separation |

## 4.1. Axis 탐색 확장

A–X 외에 이론과 방법론이 새로운 구조를 제안할 경우 반드시 새 Axis를 등록한다. 후보 출처는 Scientific ML, Causal ML, Complex Systems, Reinforcement Learning, Artificial Neural Network Interpretability, Computational Learning Theory, Model-based Experiment Design, Active Perception, Computational Memory, Neural Data Alignment 등이다. 그러나 **관심 밖 주제를 억지로 끌어들여 질문을 흐리지 않는다**. 신설 Axis는 뇌-정서 관련 과학 질문으로 이어질 경로를 제시해야 한다.

각 Sub-axis의 최소 등록 필드: `axis_id`, `name`, `definition`, `type_tags`, `representative_papers`, `models`, `open_questions`, `transfer_opportunities`, `dataset_feasibility`, `confidence`, `origin_agent`, `last_verified`.

## 4.2. 고정된 단일 분류 대신 다중 태그 사용

Coordinator는 다음 다섯 유형을 관리한다.

1. **Construct / Stimulus:** A, B, C, D, U, W 등을 출발점으로 하는 현상·자극·맥락·정서 개념
2. **Neural:** E, F, O 및 기타 뇌영역·네트워크·공통/개인 표상
3. **Model / Method:** G, H, I, J, L, M, N, V 등 모델·학습 목표·분석 방식
4. **Structure / Dynamics:** D, K, R, U, V, X 등 정보 구조·기하학·시간적 변화
5. **Inference / Measurement:** P, Q, S, T, X 등 검증·추론·측정·일반화

한 Axis는 여러 유형에 속할 수 있다. 위 매핑은 **예시이며 고정 분류가 아니다**. 새로운 유형이 필요한 경우 이유를 밝히고 추가한다. 이 분류가 원래의 연구 다양성을 압축하거나 특정 조합을 배제하지 않도록 주의한다.

원칙적으로 RQ 하나는 **서로 다른 유형 최소 3개**를 결합한다. 단, 과학적으로 강력하고 식별 가능한 두 유형 조합은 예외로 보존한다. 결합한 유형 수 자체로 연구의 질을 평가하지 않는다.

# 5. Phase III — 최소 100편의 검증된 문헌과 Discussion Mining

문헌조사의 목표는 인용문을 많이 모으는 것이 아니다. **서로 다른 분야의 발견·한계·아직 검증되지 않은 제안을 연결하여 과학적 기회 지도를 구축하는 것**이다.

## 5.1. 문헌 검색·선별 범위

PubMed, Crossref, OpenAlex, Semantic Scholar, Google Scholar, arXiv/bioRxiv 및 NeurIPS/ICLR/ICML/CVPR/ICCV/ECCV, Nature/Science/PNAS/Nature Neuroscience/Nature Human Behaviour/NeuroImage/eLife 등 분야별 신뢰할 만한 원문 출처를 조사한다.

- **고유 논문 최소 100편**을 확보한다. preprint와 정식 출판본의 동일 연구를 이중 집계하지 않는다.
- 최신 모델 및 방법(특히 2024~2026년)을 폭넓게 포함하면서 핵심적인 고전 논문도 유지한다.
- 정서신경과학만으로 100편을 채우지 않는다. Vision/Video AI, multimodal AI, brain encoding/decoding, generative models, manifolds/dynamics, interpretability, brain foundation models, methodological inference가 반드시 포함되어야 한다.
- 단순 키워드 중복인 문헌, 초록만으로 실질적 관련성을 확인할 수 없는 문헌, 존재가 불확실한 문헌을 수량 채우기 용도로 포함하지 않는다.
- 문헌의 연구 질문과 현재 연구의 연결은 간접적이어도 좋으나 **무엇을 전이할지** 명시해야 한다.

### 우선 조사할 출발점(정확한 서지·모델명은 다시 검증)

- Cowen & Keltner (2017), 다차원 정서 범주와 연속적 구조
- Horikawa et al. (2020), visually evoked emotion의 신경표상
- Emo-FilM 데이터 및 대표 분석 연구
- Spacetop 데이터 논문·공식 문서
- Allen et al. (2022), NSD
- MindEye2 및 Brain-IT 등 visual reconstruction 계열
- SwiFT / CortexMAE / TRIBE v2 / BrainMamba 등 brain foundation/encoding 계열
- EmoPathway와 그에 관련된 brain-like 모델(정확한 실재·제목 확인 필수)
- 최근 neural manifold, temporal neural dynamics, multimodal representation alignment 관련 연구

출발점은 필수 확인 대상이지 최종 아이디어의 선호 순위가 아니다. 조사 과정에서 발견한 예상 밖의 AI 문헌을 적극 추가한다.

## 5.2. 논문 1편당 필수 데이터 필드

`paper_id`, `title`, `authors`, `year`, `venue`, `doi_or_arxiv`, `official_url`, `version`, `source_verified`, `full_text_access`, `discussion_access`, `domain`, `axis_tags`, `original_rq`, `dataset`, `stimulus`, `brain_measurement`, `model_method`, `training_objective`, `main_findings`, `scientific_contribution`, `limitations`, `future_directions`, `future_direction_source_location`, `transfer_idea`, `relevant_datasets`, `novelty_risk`, `evidence_level`, `agent`, `verification_date`.

본문/Discussion 직접 확인 가능 여부를 명시한다. `Discussion`을 읽지 못했다면 관련 내용을 **저자의 직접 제안**이라고 표기하지 않는다. 가능하면 절 제목/페이지/문단 위치를 기록한다. 무리하게 긴 원문을 복제하지 말고 간단히 요약하고 링크를 남긴다.

### 근거 수준

- **E1 — 원문 검증:** 공식 논문 본문·부록·공식 코드·데이터 문서를 직접 확인.
- **E2 — 요약 검증:** 신뢰 가능한 메타데이터·초록 등만 확인. Discussion 직접 확인 여부는 별도 표시.
- **E3 — 연구팀 추론:** 확인된 문헌들을 바탕으로 Agent가 새로 만든 연결/가설.
- **E0 — 미검증:** 존재·사실·후속 방향 확인 실패. 사실로 인용 금지.

100편 ‘검증된 문헌’ 집계에는 적어도 서지와 출처가 확인된 문헌만 포함한다. Discussion Mining의 성과는 원문 접근이 실제로 확인된 부분으로 제한한다.

## 5.3. Discussion → Research Opportunity 변환

각 논문의 Discussion/Limitations/Future Work에서 다음을 별도로 찾아라.

1. 연구자가 **명시적으로 남긴 미해결 질문**은 무엇인가?
2. 왜 당시에는 검증하기 어려웠는가? (자극 통제, 데이터 규모, 해상도, 모델, 계산 자원, 표상 분석)
3. 2026년의 AI 기술은 그 문제를 어떻게 바꾸었는가?
4. 완전히 다른 분야의 모델·평가 방법을 가져오면 해결 가능한가?
5. 원 연구에서는 분석하지 않은 neural level, dynamics, generalization, representation decomposition이 있는가?
6. 다른 논문의 결과·한계와 연결하면 새로운 실험을 만들 수 있는가?
7. 현재의 네 데이터셋으로 전부 또는 일부를 검증할 수 있는가?

**논문이 실제 제안한 Future Direction과 Agent가 후속으로 추론한 Research Opportunity를 명확히 분리**한다.

표준 변환:

`원 연구의 발견 → 남겨진 질문/제약 → 최근 기술 변화 → 다른 분야의 개념/모델 → 가능한 데이터/통제 → 새 RQ`

### Cowen & Keltner (2017) 탐색 예시

이 논문의 실제 Discussion을 직접 확인하면서, 정서 상태의 신경적 구분, 정서 유발과 다차원 신뢰도 추정, 고차원 구조 관련 후속 제안을 찾아라. **원문에서 확인된 범위에 한해** 2026년 모델과 데이터로 어떻게 재검토할 수 있는지 연결한다. 예시라고 해서 특정 이론 검증을 최종 연구 방향으로 미리 확정하지 않는다.

## 5.4. Cross-paper synthesis

Agent와 Coordinator는 논문 단위의 요약을 넘어 다음 유형의 연결을 찾는다.

- **Limitation × Method:** 논문 A의 한계를 다른 분야 논문 B의 방법이 해결.
- **Question × Model:** 미해결 신경과학 질문을 새로운 AI 모델이 검증 가능하게 만듦.
- **Dataset × Objective:** 기존 신경 데이터에 과거에는 없었던 self-supervised objective 적용.
- **Conflicting Findings × Control:** 모순된 결과를 구별할 수 있는 새로운 통제 변수를 제안.
- **Representation × Dynamics:** 정적 표상 결과를 시간적 변화·전이 모델로 재해석.
- **AI–Brain Gap:** 모델이 설명하지 못하는 정서 관련 신경 변동이 새로운 과학 질문을 제시.

각 연결에 최소 2개의 실제 문헌 또는 1개의 문헌 + 공식 모델/데이터 근거를 연결한다. 추론의 도약이 크면 그 사실을 적는다.

## 5.5. 문헌 탐색 종료 조건

- 고유·서지 검증 완료 문헌 100편 이상.
- 영역별 편중 평가 및 탐색 공백 목록.
- Discussion 직접 확인 가능 여부 기록.
- 최소 30개 이상의 **문헌 기반 미해결 문제** 확보를 목표로 한다(품질 우선).
- 후보 RQ마다 가장 가까운 기존 연구를 역으로 검색하는 절차 수행.

100편을 실제로 확보하지 못한 경우 숫자를 꾸미지 말고 확보 수량·검색 한계·남은 검증 작업을 보고한다.

# 6. Phase IV — 실제 에이전트 토론: 합의가 아니라 생산적 충돌

개별 Agent의 보고서를 단순 병합하지 않는다. 최소 다섯 차례에 걸쳐 **독립 발견 → 정보 교환 → 상호 비판 → 예상 밖의 연결 → 대립 가설 토론**을 수행한다.

## Round 1. Independent Discovery

초기에는 다른 Agent의 발견을 읽지 않는다. 각 Agent는 자신의 분야에서 미해결 문제 5개, 주요 모델/방법 5개, 분야 간 전이 5개, 예상 밖의 연결 3개, 숨겨진 가정 3개, 새로운 Sub-axis 3개를 제시한다. 각 항목의 문헌 근거·불확실성을 표시한다.

## Round 2. Cross-Agent Exchange

Coordinator는 서로 다른 분야의 보고서를 교환한다. 각 Agent는 자신의 원래 전문 분야 바깥에서 **최소 2개 이상**의 계산 원리 또는 과학 질문을 수입한다. 무엇이 원래 문헌의 문제이고, 무엇이 새롭게 바뀐 문제인지 구분한다.

논의 시작 질문 예시:

- Vision Decoding 모델의 표현·재구성 능력으로 기존 정서 디코딩이 분리하지 못한 신경정보를 드러낼 수 있는가?
- Video/Audio/Language 모델의 서로 다른 latent space가 같은 fMRI 변동을 어떻게 설명하고 서로 어디서 충돌하는가?
- 정서가 자극의 저수준 특징·의미·시간적 맥락 중 어느 정보와 어떻게 얽혀 있는지 새로운 representation decomposition으로 구별할 수 있는가?
- Brain Foundation Model은 범용 뇌표상에서 정서 관련 신호를 어떤 방식으로 보존하거나 소실하는가?
- 기존 자극의 의미를 바꾸지 않고 시각적 특징만 조절하는 생성형 접근이 모델의 예측을 어떻게 변화시키는가?
- Cross-subject alignment와 manifold 구조가 설명하는 정보가 실제로 같은가?
- World Model의 예측 상태가 뇌의 시간적 정서 변동을 설명하는가, 아니면 단지 자극 사건 구조를 설명하는가?

## Round 3. Constructive Disagreement

각 Agent가 최소 2개 다른 Agent의 연구 제안에 반론을 작성한다. 다음을 의무적으로 확인한다.

- 이미 답이 있는 질문 아닌가?
- 새로운 모델이 아니라 기존 문제의 단순한 benchmark 교체 아닌가?
- 관심 대상인 **정서 관련 뇌정보**와 무관한 특징을 예측하는 것은 아닌가?
- 데이터셋에 필요한 정보가 실제로 있는가?
- 설명되는 분산이 stimulus identity, motion, semantics로 충분히 설명되는가?
- 예측·표상 대응·메커니즘·인과성을 섞어 말하는가?
- 더 강한 baseline이나 판별적 실험이 있는가?
- **결과가 부정적일 때도** 과학적으로 의미 있는가?

비판 결과는 **수정 / 보류 / 기각**으로 구분하고 이유를 기록한다.

## Round 4. Unexpected Connections

기존에 나온 조합을 그대로 재사용하지 말고 **다른 학문의 원래 계산 목적이 가진 구조**를 정서 연구에 전이한다. 예를 들어 Computer Vision, Mechanistic Interpretability, State-space Learning, Generative Counterfactuals, Information Decomposition 사이의 예상 밖의 연결을 독자적으로 찾는다. 새로운 연결에 필요한 전제와 문헌을 확인한다.

## Round 5. Scientific Debate

유망하지만 논쟁적인 질문마다 (1) 제안자, (2) 회의적 비판자, (3) 데이터·통계 검토자, (4) Coordinator의 역할을 지정한다. 설명이 충돌한다면 빠르게 합의하지 말고 **두 설명을 가르는 판별적 연구 질문**을 생성한다. 소수 의견, 해결되지 않은 모순, 기각 이유도 보존한다.

작업 환경이 Agent 간 직접 토론을 지원하지 않을 때는 Coordinator가 결과를 전달해 순차적 상호 검토를 진행한다. 실제로 하지 않은 대화를 회의록처럼 꾸미지 않는다.

# 7. Phase V — 조합적 Research Question 생성

Coordinator는 **연구 문제를 먼저 정하지 않고** Axis·논문·모델·측정·과학적 공백의 공간을 구축한다. 문헌 기반 조합과 무작위 조합을 독립 경로로 실행한 뒤 통합한다.

## 7.1. Research Combination Matrix

각 조합은 다음 필드를 갖는다.

`combination_id`, `generation_path`, `axis_ids`, `type_tags`, `scientific_construct`, `external_field_concept`, `ai_model_or_method`, `neural_target`, `available_dataset`, `measurable_contrast`, `falsifiable_prediction`, `baseline`, `source_papers`, `missing_assumptions`, `novelty_risk`, `decision`, `rejection_reason`.

원칙적으로 **서로 다른 유형 3개 이상**을 결합하되, 과학적으로 더 강한 2개 유형 조합은 예외로 유지한다. 다중 태그·새로운 Axis의 추가를 허용한다.

## 7.2. 문헌 기반 생성 경로

아래 생성 전략을 모두 검토한다.

1. **Technology Transfer:** 정서 연구 바깥의 모델·학습 목적·분석 방법을 가져오기.
2. **Methodological Inversion:** encoding → decoding, decoding → generation, representation similarity → intervention, static → dynamic.
3. **Representation Competition:** visual vs semantic vs affective, model vs brain, shared vs private, sensory vs transmodal.
4. **Scale Bridging:** low-level stimulus → context → distributed network, short timescale → long timescale, voxel → manifold.
5. **Dynamics & Geometry:** latent state, trajectory, topology, transition, attractor, temporal invariance.
6. **Cross-Dataset Discovery:** label과 모달리티가 다른 데이터셋을 alignment/transfer/representation model로 연결.
7. **Counterfactual Modeling:** 생성형 자극 조절·잠재공간 조작으로 구별할 예측 생성(실측 인과 효과와 구분).
8. **Brain-to-AI Reverse Inspiration:** 신경구조를 computational constraint로 가져온 모델 간 비교.
9. **Model Disagreement:** 여러 모델이 서로 다르게 설명하는 brain variance에서 새 질문 발굴.
10. **Hidden Structure Discovery:** 사전 라벨에 의존하지 않는 구조 발견 후 독립 검증.
11. **Unresolved Discussion Transfer:** 논문 A의 명시적 미래 과제를 논문 B의 새로운 기술로 재검증.
12. **Assumption Reversal:** 널리 쓰는 가정의 반대 예측이 성립할 가능성을 찾아 판별적 분석 설계.

## 7.3. 별도 무작위 조합 실험: 최소 30개

문헌과 에이전트의 익숙한 조합이 만든 편향을 줄이기 위해 **독립적인 무작위 교차 조합 30개**를 생성한다.

- 최신 Axis Taxonomy에서 Construct/Stimulus, Neural, Model/Method, Structure/Dynamics, Inference/Measurement 유형을 고려해 후보를 샘플링한다.
- 가급적 다른 유형 3개 이상을 뽑는다. 중복 조합과 의미상 완전히 같은 조합을 기록하여 다시 추첨할 수 있다.
- 실제 코드를 사용한다면 난수 시드(권장: `20261112`), 샘플링 방식, 재추첨 규칙을 저장한다.
- 무작위 조합 하나당 ① 뜻을 구성할 수 있는지 ② 근거 문헌을 찾을 수 있는지 ③ 관찰 가능한 반증 조건을 만들 수 있는지 ④ 새 연구 기여가 있는지 검토한다.
- **발전 / 수정 필요 / 보류 / 기각**으로 판정하고, **기각된 조합과 이유도 반드시 남긴다.**
- 단순 무작위 단어 나열을 억지로 RQ로 바꾸지 않는다. 실패한 연결도 독립성과 다양성에 관한 정보다.
- 실행 도구 없이 사람이 조합했다면 ‘무작위’라고 주장하지 말고 ‘체계적 교차 조합’으로 표기한다.

## 7.4. 3단계 질문 재구성(모든 유망 후보에 필수)

**1차 — 모델 적용:** 이 모델 또는 분석으로 무엇을 예측·복원·비교할 수 있는가?

**2차 — 과학적 질문:** 그 비교가 정서 관련 신경표상의 어떤 특성·변환·계산을 검증하는가?

**3차 — 기존 가정에 대한 도전:** 어떤 경쟁 설명을 구별하거나 기존 가정을 반박할 수 있으며, 어떤 부정적 결과가 나와도 무엇을 배우는가?

3단계를 거쳐도 단순 성능 경쟁에 불과하다면 **RQ 후보가 아니라 방법론 후보**로 남기거나 기각한다.

## 7.5. 양과 다양성 기준

- 넓은 연구 방향(Research Directions): **40개 이상**
- 중복 제거된 구별 가능한 Research Questions: **30개 이상**
- 실질적 Shortlist: **10개**
- 우선 검토 후보: **5개**
- 명확한 첫 검증이 가능한 Pilot: **3개**

숫자를 채우려는 변형 제안을 만들지 않는다. 독창성과 검증 기준을 통과한 질문이 부족하면 **실제 통과 수량과 이유**를 보고한다. 30개가 모두 한 종류의 decoding/encoding 문제에 쏠리지 않는지 유형별 분포를 감사한다.

# 8. Coordinator — Question Design & Adversarial Synthesis Protocol

Coordinator는 다음 단계를 **각 RQ의 형성 과정**에 연결한다.

## 8.1. 숨겨진 가정 발굴

각 Agent로부터 분야 내 **검증이 불충분한 가정 최소 3개**를 수집한다. 어떤 논문이 가정하는지, 어떻게 의존하는지, 왜 당시 검증되지 않았는지, 어떤 최신 모델/데이터가 검증 가능하게 했는지 정리한다.

## 8.2. 기술적 도약의 본질 파악

AI 모델의 단순 정확도 향상보다 **새로운 계산 능력**을 찾는다: 입력/출력 변화, 새로운 latent space, 학습 목표 변화, temporal prediction, cross-modal transfer, controllable generation, internal feature decomposition, cross-subject alignment, in-silico experimental capability. 각 계산 능력이 새 과학 질문을 열어주는 연결을 요구한다.

## 8.3. 역방향 연결과 가정의 뒤집기

AI → Neuroscience뿐 아니라 Neuroscience → AI도 탐색한다. 경쟁 설명(지역 대 분산, 감각 대 의미 대 정서, 정적 대 동적, 공통 대 개인 특이, 선형 대 비선형, 모달리티 특이 대 공유)을 발견하면 어느 설명을 지지할지 먼저 정하지 말고 **둘을 구별하는 실험**을 생성한다.

## 8.4. 조합의 과학적 진정성 검토

가장 이상한 조합이 가장 좋은 조합은 아니다. 다음 세 조건을 충족해야 한다.

1. 기존에 검증하지 못한 구체적 과학 문제가 있다.
2. 새 모델/방법이 그 문제에 **필수적인 판별력이나 측정 능력**을 제공한다.
3. 결과를 적어도 둘 이상의 경쟁 설명과 비교하거나 명확한 반증 조건을 제시할 수 있다.

## 8.5. Adversarial Novelty Search

최종 후보 하나마다 **‘이 연구는 이미 있었다’는 반례를 찾는 검색**을 별도로 수행한다. 가장 가까운 논문, 동일한 데이터+유사 타깃, 동일한 방법+유사 주장, 2024–2026 신규 논문까지 조사한다. 가장 강한 반론을 정리한 뒤 수정·유지·기각을 결정한다.

## 8.6. 연구 다양성 감사

Coordinator는 어느 모델군, 데이터셋, 질문 방식, 신경 표상 수준이 과도하게 지배하는지 표시한다. 분야 간 연결이 약하다면 Agent 06과 다른 2개 Agent에게 **초기 후보와 전혀 다른 영역의 대안**을 추가 요청한다.

## 8.7. 연구 질문의 두 층위

- **Discovery Track:** 즉시 구현이 어려워도 과학적 잠재력과 독창성이 큰 질문.
- **Feasibility Track:** Horikawa 및 보유 모델로 검증 가능한 질문.

초기에는 분리해 평가하고, 최종 선택에서 균형을 잡는다. 현재 구현의 편리함이 연구 목표를 소급해 제한하지 않도록 한다.

# 9. Phase VI — RQ 평가 체계와 품질 기준

각 질문에 대해 다음을 **1–5점 + 근거 문헌 + 불확실성**으로 평가한다. 가중합 점수만으로 기계적으로 정렬하지 않는다.

| 항목 | 필수 확인 |
|---|---|
| **Scientific Novelty** | 무엇이 처음이며 가장 가까운 논문과 정확히 어떻게 다른가? |
| **Neuroscientific Importance** | 정서 관련 뇌표상·계산에 어떤 설명력/반증력을 추가하는가? |
| **AI/Modeling Necessity** | 새로운 AI 모델이 왜 필요하며 단순 baseline으로 대체할 수 없는가? |
| **Data & Label Feasibility** | 실제 데이터, 측정, 자극, label, 시간 해상도가 있는가? |
| **Methodological Rigor** | confound, split, reliability, overfitting, identifiability 통제가 가능한가? |
| **Falsifiability** | 어떤 결과가 가설을 반박하며 그 결과도 의미가 있는가? |
| **Interpretability** | 예측 성능과 뇌 메커니즘 해석을 구분하고 경쟁 설명을 비교하는가? |
| **Generalization** | 피험자/자극/데이터셋/모달리티 전이 가능성을 검증할 수 있는가? |
| **Technical Feasibility** | 코드·체크포인트·라이선스·컴퓨팅·기술적 난도가 현실적인가? |
| **Exploration Value** | 기존의 고착된 접근과 다르게 중요한 가능성을 개방하는가? |

다음 네 가지 랭킹을 분리한다: **과학적 잠재력**, **독창성**, **단기 실현성**, **종합 우선순위**. Horikawa 우선은 최종 실현성 평가에서 의미가 있으며 초기 아이디어 생성의 필터가 아니다.

### 자동 탈락이 아닌 ‘강화 필요’ 신호

- 단순 최신 모델로 emotion classification accuracy 개선.
- 기존 ROI 상관을 다른 model feature와 반복.
- 새로운 manifold 그림 자체를 연구 결과로 간주.
- multimodal model의 높은 성능만으로 뇌의 통합 계산을 설명했다고 주장.
- AI가 생성한 정서 annotation을 독립적인 정답인 것처럼 사용.

위 사례는 더 강한 판별적 과학 질문으로 수정될 수 있으면 발전시키고, 끝내 그렇게 되지 않으면 기술적 실험으로만 분류한다.

# 10. Phase VII — 최종 10개 Research Question Card

최종 10개는 각각 아래 16개 요소를 포함하는 상세 제안서로 작성한다.

1. **RQ ID / Working Title:** 간명하고 구체적인 제목.
2. **One-sentence Core Question:** 실제로 검증할 과학 질문 한 문장.
3. **Scientific Motivation:** 어떤 지식의 공백인가? 왜 뇌과학적으로 중요한가?
4. **Idea Provenance:** 어느 Agent/Axis/다른 분야의 어떤 발견이 결합되었는가?
5. **Prior Literature:** 직접 관련 논문 최소 5편(가능한 범위에서)과 각 논문의 기여·한계.
6. **Closest Prior Work & Novelty:** 가장 유사한 연구와 중복 위험, 차별점, 신규성 반론.
7. **Dataset & Metadata:** Horikawa/Emo-FilM/Spacetop/NSD 중 어떤 자료의 어떤 실제 필드를 쓰는가?
8. **Computational Framework:** pretrained model, input/output, latent/feature, adaptation, loss/objective, checkpoints.
9. **Neural Target:** voxel/ROI/network/distributed/temporal latent 중 어떤 수준인가?
10. **Proposed Analyses:** 주요 비교, variance partitioning 또는 alignment, baseline, control, ablation, validation, 통계.
11. **Competing Explanations:** 자극 특징·semantic·temporal·person-specific confound 등 대안 설명.
12. **Falsifiable Outcomes:** 긍정·부정·혼합 결과 각각의 의미, 어떤 결과가 제안을 반박하는가.
13. **Scientific & Modeling Contribution:** AI 기술적 기여와 신경과학적 기여를 구분.
14. **Limitations & Risks:** 샘플 크기, 측정/HRF, 모델 계산, 불확실성, 접근성.
15. **Smallest Informative Pilot:** 데이터 하위집합, 비교 실험, 모델, 성공/중단 기준.
16. **Priority:** 독창성·중요성·실현성·추가 데이터 필요 여부.

제안서마다 관련 근거 논문과 데이터 문서의 정확한 링크를 포함하고, **아직 입증되지 않은 결과를 예측 성과로 포장하지 않는다.**

# 11. Phase VIII — 세 가지 Pilot Study의 구현 가능 계획

최종 세 파일럿은 되도록 **서로 다른 과학 질문/모델 접근**을 대표해야 한다. 하나의 baseline 성능을 달리 계산한 세 실험으로 구성하지 않는다.

각 Pilot은 다음을 포함한다.

- **핵심 가설과 경쟁 가설**: 서로 다른 결과를 어떻게 해석할 것인가?
- **데이터 및 접근**: 실제 확인된 경로/공식 출처, 피험자·런·시행 하위집합, 데이터 권한.
- **모델/환경**: 실제 pretrained checkpoint, feature extraction, 필요한 GPU/메모리 추정의 근거.
- **입력/출력**: 신경신호와 자극 feature의 단위·시간 정렬·정서 annotation 대응.
- **실험 순서**: 데이터 QC → 비학습 baseline → 모델 적용 → control → 통계 및 재현성 검토.
- **평가**: train/validation/test의 독립성, noise ceiling, uncertainty, 유의성/효과 크기.
- **Ablation/Control**: low-level visual, semantics, motion, stimulus identity, temporal structure를 필요에 맞게 통제.
- **의사결정 지점**: Pilot 결과에 따른 확대/수정/중단 기준.
- **오류 가능성**: 이 데이터로 무엇을 주장할 수 *없는지* 분명히 명시.

# 12. 모든 단계에 적용할 Scientific Safeguards

- **Construct / Measurement:** 실제 annotation의 생성 방식과 대상·척도·집계 수준을 확인한다. AI-generated labels는 실제 측정값과 구분하고, 정서/뇌의 관계를 과장하지 않는다.
- **Visual & Semantic Confounds:** 객체·장면·색감·대조·motion·semantic content가 정서 예측 또는 뇌 활성의 주된 설명일 수 있는지 테스트한다.
- **Temporal Constraints:** HRF convolution/delay, fMRI temporal autocorrelation, run/task boundaries, annotation frequency, long-form stimulus dependence, variable durations를 점검한다.
- **Splits & Leakage:** subject/session/run/stimulus/repetition 단위 분리, 데이터 전처리·정규화·feature selection의 fold 내 수행, foundation-model pretraining contamination을 검토한다.
- **Statistical Integrity:** 독립 표본 수, ROI/whole-brain selection, multiple comparisons, hierarchical dependence, uncertainty, reliability/noise ceiling, 효과 크기, negative control.
- **Model Interpretation:** decodability ≠ neural mechanism, encoding correlation ≠ causal explanation, model–brain RSA/alignment ≠ 동일한 알고리즘이라는 점을 엄격히 구분한다.
- **Counterfactual Validity:** 생성형 모델이 조작한 latent feature의 실제 의미를 검증하고, in-silico 결과만으로 신경 인과성을 주장하지 않는다.
- **Cross-dataset Validity:** annotation ontology, task, stimulus distribution, acquisition, subjects, temporal resolution의 차이를 직접 결합 전에 검사한다.
- **Evidence & Reproducibility:** 논문 DOI/URL/버전, 모델 체크포인트, 데이터 출처, 실험 설정, 코드 실행 상태, 실패·보류 이유를 보존한다.

# 13. 필수 산출물: 자료 → 토론 → 조합 → RQ → Pilot

모든 산출물의 내용은 한국어로 작성하고, 필드명·논문명·코드상 기술 표기는 원어를 허용한다.

**A. Dataset Intelligence Report** — 4개 데이터셋의 공식 구조·metadata·annotation·사용 가능성·누락 정보를 검증한 보고서.

**B. Research Axis Encyclopedia** — A–X 및 새 Axis의 하위 분류, 정의, 인용, 모델, 미해결 질문, 다중 유형 태그.

**C. Verified Literature Database** — 고유 문헌 100편 이상과 서지·핵심 결과·실제 Discussion 접근 상태·연구 전이 기회.

**D. Discussion / Future-Direction Mining** — 논문 저자의 직접 제안과 Agent가 추론한 미해결 문제를 분리한 데이터베이스.

**E. Cross-Disciplinary Opportunity Map** — 원래 분야 → 새 계산 능력 → 정서 관련 뇌과학 질문 → 자료·검증·한계의 연결.

**F. Agent Discussion Records** — Round 1–5의 발견·제안·반론·개정·기각·미해결 쟁점 기록.

**G. Research Combination Matrix** — 문헌 기반 조합과 **실제 무작위 30개**를 구분하고 기각 사유까지 포함한 전체 표.

**H. Research Question Landscape** — 구분되는 RQ 최소 30개, 과학적 주제별 군집, Axis 조합, 검증 방법, 중복 위험.

**I. Top 10 Research Proposals** — 16개 항목으로 구성한 질문별 상세 제안서.

**J. Top 3 Pilot Study Plans** — 구현 가능한 모델·입력·평가·대조군·의사결정 기준.

**K. Coordinator's Final Synthesis** — 어떤 질문이 왜 새롭고 중요한지, 어떤 AI 기술을 가져와야 하는지, Horikawa에서 무엇이 가능한지, 가장 위험하지만 가치 있는 방향과 실제 시작할 파일럿을 구분해 제시.

## 13.1. 최종 보고서가 반드시 답해야 할 질문

1. 현재 정서신경과학에서 가장 중요한 **탐색 공백**은 무엇인가?
2. 다른 AI 분야에서 발견한 **예상 밖의 계산 원리**는 무엇인가?
3. 기존 문헌의 Discussion에서 **지금 새롭게 해결할 수 있게 된 문제**는 무엇인가?
4. Horikawa의 기존 분석에서 미처 활용되지 않은 정보·구조는 무엇인가? (근거가 있는 경우)
5. Brain Foundation Model / Vision Decoding / Multimodal Model 중 어떤 접근이 무엇을 새로 검증하게 하는가?
6. 질문의 독창성이 **단순 모델 교체**가 아님을 어떻게 보였는가?
7. 예측 성능 외에 어떤 **판별적 신경과학적 증거**가 필요한가?
8. 가장 높은 과학적 잠재력을 가진 질문과 당장 할 수 있는 질문은 각각 무엇인가?
9. 서로 다른 에이전트가 **의견이 일치하지 않는 지점**과 그 이유는 무엇인가?
10. 어떤 파일럿 3개를 왜 먼저 수행해야 하는가?

# 14. 품질 게이트 및 실행 순서

각 단계의 완료 조건을 만족할 때 다음 단계로 진행한다. 도구·시간 제약으로 완료하지 못한 경우 **부분 결과와 실제 남은 항목**을 저장한다. 검증을 하지 않은 일을 완료로 표시하지 않는다.

| Stage | 수행 | 완료 게이트 |
|---|---|---|
| 0 | 독립 환경/지침 점검 | 기존 EmoBrain 초기 접근 금지·한국어 규칙·Agent별 전용 폴더 확인 |
| 1 | Agent 독립 탐색 | 12역할의 역할별 조사/근거/가정/신규 연결 확보 또는 실제 수행 가능한 역할 범위 명시 |
| 2 | Dataset Audit + Literature | 공식 데이터 사실 검증, 고유 문헌 ≥100 확보(미달 시 실제 수량·원인 보고) |
| 3 | Axis 확장 | A–X 갱신, 새 Axis 기록, 다중 유형/연결 관계 정리 |
| 4 | 교차 토론 | 5개 Round의 실질적 교환·비판·수정/기각 기록 |
| 5 | 조합 실험 | 문헌 기반 조합 + 별도 무작위 30개와 기각 로그 |
| 6 | RQ 생성 | 넓은 방향 ≥40, 구별되는 RQ ≥30(미달 시 품질상 이유 기록) |
| 7 | Adversarial Novelty Audit | 각 shortlist에 가장 가까운 선행연구/강한 반론/수정 기록 |
| 8 | 10개 상세 제안 | 근거·모델·데이터·통제·경쟁 설명·검증 계획 작성 |
| 9 | 실현성 확인 | 필요한 경우에만 EmoBrain 자원 읽기 전용 비교 |
| 10 | 3개 Pilot + 종합 | 우선순위별 연구 지도, 파일럿 계획, 남은 불확실성 보고 |

## 14.1. 운영상 원칙

- 병렬 조사에서는 **Agent별 고유 파일**을 작성하고 Coordinator만 공유 데이터베이스를 병합한다. 동일 파일 동시 수정 금지.
- 모든 조사 결과에 `source`, `verified_on`, `confidence`, `needs_followup`, `origin_agent`를 기록한다.
- 결과는 세션이 바뀌어도 계속 사용할 수 있도록 주기적으로 파일에 저장한다.
- 외부 접근/모델 다운로드/실행이 제한되어 있을 때는 가능한 작업과 불가능한 작업을 구분한다.
- 도구 또는 Agent의 사용 가능 기능은 현재 실행 환경을 확인하고 결정한다. 지원되지 않는 병렬화나 에이전트 유형을 있는 것처럼 선언하지 않는다.
- 파일 이름/경로/지침 로딩 방식은 `CLAUDE.md` 또는 `AGENTS.md`의 실행 환경별 지침을 따른다.

# 15. 권장 프로젝트 디렉터리 구조

```text
Affective-Research-Exploration/
├── RESEARCH_MISSION.md           # 연구 철학·과학적 규칙·산출물 (공통)
├── CLAUDE.md                     # Claude Code 실행 지침
├── AGENTS.md                     # Codex 실행 지침
├── START_HERE.md                 # 시작 방법
├── RESEARCH_STATUS.md            # 완료/미완료·차단 사유·다음 단계
├── agents/                       # 담당 Agent별 독립 조사
│   ├── 01_dataset/
│   ├── 02_affective_neuroscience/
│   ├── 03_vision_decoding/
│   ├── 04_brain_foundation/
│   ├── 05_multimodal_dynamics/
│   ├── 06_frontier_ai/
│   ├── 07_geometry_information/
│   ├── 08_systems_neuroscience/
│   ├── 09_generative_ai/
│   ├── 10_llm_semantics/
│   ├── 11_brain_inspired/
│   └── 12_adversarial_review/
├── datasets/                     # 공식 metadata·label·가능/불가능 task 검증
├── literature/                   # papers.csv · paper_reviews · discussion_mining · references.bib
├── axis_map/                     # taxonomy · subaxes · type_tags · cross_connections
├── discussions/                  # round_01 ... round_05
├── combinations/                 # literature_based · random_30 · rejection_log
├── research_questions/           # landscape · shortlist · top10 · pilot3
└── synthesis/                    # novelty_audit · opportunity_map · final_report
```

# 16. 최종 연구 지령 — 다시 읽을 것

당신의 목표는 기존 Affective Neuroscience 논문의 사소한 변형을 제안하는 것이 아니다.

**AI와 Neuroscience의 서로 다른 연구 흐름이 만나는 지점에서 아직 충분히 탐구되지 않은 새로운 질문을 발견하는 것**이다.

매 단계 다음을 다시 물어라.

- 왜 지금까지 시도되지 않았는가?
- 최근 기술 발전이 새롭게 가능하게 만든 것은 무엇인가?
- 지금까지 당연하게 받아들인 가정 중 틀렸을 수 있는 것은 무엇인가?
- AI 모델이 기존 신경과학 모델보다 잘 포착하는 것과 놓치는 것은 각각 무엇인가?
- 다른 분야의 문제 정의·기법으로 정서의 신경 계산을 새롭게 분석할 수 있는가?
- 데이터셋을 본래 목적과 다른 방식으로 활용할 수 있는가?
- 그 결과가 정서 관련 뇌표상·계산에 대한 이해를 실제로 바꾸는가?

기존 정서 이론을 무시하라는 것이 아니다. 이론이 아이디어의 출발 범위를 미리 제한하지 않도록 하라는 뜻이다.

**가능한 Axis를 폭넓게 탐색하고, 실제 문헌의 근거와 Discussion의 미해결 문제를 연결하고, 에이전트 간 토론과 강한 반론을 통해 가설을 재구성한 뒤, 마지막에 이론적 의미와 실험 가능성을 평가하라.**

익숙한 질문을 빠르게 생산하는 데 최적화하지 마라. 문헌과 다른 분야의 방법이 만나는 **놓쳐진 과학적 연결**을 발견하는 데 최적화하라.

**모든 보고와 최종 대답은 한국어로 작성한다.**

**이제 독립적인 탐색을 시작하라.**
