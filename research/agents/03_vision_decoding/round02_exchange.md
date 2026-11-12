# Agent03 실제 Round2 교환

Agent02와 Agent09의 원본 보고서를 읽고 계산 원리를 수입했다. 다섯 데이터의 보유를 인정하며 미확인 스키마는 실행 조건으로 남긴다. 후보는 모두 E3로서 실제 분석·실험·최초성 확정이 아니다. 다른 단계와 Git 작업은 수행하지 않았다.

## 실제 읽은 파일
- AGENTS.md
- RESEARCH_MISSION.md
- discussions/CONTINUATION_PROTOCOL.md
- agents/03_vision_decoding/ROUND1_REPORT.md
- agents/02_affective_neuroscience/report.md
- agents/09_generative_ai/report.md
- axis_map/reference_catalog.csv
- axis_map/integrated_subaxes.csv
- literature/papers.csv

## 수입 원리

### 02_affective_neuroscience: 총정보·공유정보·조건부정보를 구분하는 내용 환경 일반화
정서 범주와 시각 schema의 신경표상이 자극 내용과 어떻게 연결되고 다른 하위도메인에서도 일반화하는가(P001/P007/P008).
시각 특징으로 회귀 제거한 잔차만 정서 정보로 취급하던 위험을 수정한다. 디코더 정렬 전후의 총 예측과 내용 조건부 증분을 함께 측정하고 내용군을 통째로 보류한다.
Agent02가 확인한 공식 코드 및 지정 본문/Discussion의 보고를 실제 읽음. 정서 디코더로의 연결은 E3.

### 09_generative_ai: 잡음 있는 역문제의 비유일성과 관측 등가 후보 집합
Diffusion Posterior Sampling은 생성 prior와 관측 잔차를 결합해 역해를 근사 표집한다(P076).
고품질 복원 한 장에 정서 내용이 나타나는가에서, 같은 보류 뇌 관측으로 허용되는 후보 집합에 그 정서 대비가 식별되는가로 목표를 바꾼다. sampler 빈도는 calibrated posterior로 가정하지 않는다.
Agent09 공식 코드·README 확인 보고를 읽음; 해당 논문 본문 직접 열람을 상속 주장하지 않음; 신경 전이 E3.

### 09_generative_ai: 의미 보존의 독립 검증과 기대 정보이득에 의한 경쟁 모형 선택
Prompt-to-Prompt의 cross-attention 제어는 배치 보존 편집, Deep Adaptive Design은 likelihood에 따른 순차 실험 정보이득 최적화가 목표(P070/P077).
decoder가 좋아하는 자극 대신 객체 목록과 비목표 시각 변화를 검증한 상태에서 경쟁 신경 가설이 다른 예측을 하는 자극을 선택한다. 새 편집물에 원본 BOLD를 붙이지 않는다.
Agent09의 지정 원문 절 확인과 한계 보고를 읽음; 여기서는 설계 원리 수입이며 새 생성·뇌 측정 없음.

## C03-01 시각 정렬이 보존하는 정서 정보와 버리는 정서 정보의 내용 일반화 경계

Axis: AS01, AS05, AS07, AS29

**연구 질문**
시각 검색이 유지되는 조건에서 공유 디코더 정렬은 내용 환경을 넘어 일반화하는 정서 관련 뇌정보를 선택적으로 소실시키는가?

**신경 대상**
시각 및 transmodal 패턴에서 원 뇌와 공유 latent가 담는 정서 주석 관련 총 예측 및 조건부 증분

**외부 원리**
Agent02의 내용 하위도메인 일반화와 총/공유/조건부 정보 구분을 목적함수 정보 보존 감사에 수입

**1차 모델 적용**
같은 자료에서 ridge→시각 특징, masked 뇌 표현, contrastive 뇌→시각 표현을 맞춘 용량의 readout으로 평가한다.

**2차 과학 질문**
시각과 정서 정보의 공유 부분까지 보존해야 내용 변화에 강한 코드가 되는지, 시각 식별 최적화가 그 코드를 압축해 버리는지 묻는다.

**3차 기존 가정 도전**
시각에 잘 정렬되면 관심 신경정보도 충분히 보존된다는 가정 및 시각 공유분산은 모두 nuisance라는 가정을 함께 시험한다.

**주가설**
시각 검색 성능이 동등한 모델 사이에도 내용군 보류에서 반복 가능한 정서 관련 증분의 보존량이 다르다.

**대립 설명**
차이는 정서 정보 선택성이 아니라 readout capacity·SNR·자료량 또는 시각모형 부적합으로 설명된다.

**측정 대비**
원 뇌/공유 trunk/CLIP head의 정서 총 예측과 시각·의미 조건부 증분 차이; 동시에 동일 후보군의 뇌→영상 검색을 평가하고 객체·장면군과 피험자를 보류한다.

**반증**
용량·신뢰도·내용분포를 맞추면 정렬 단계 간 차이가 사라지거나 원 뇌에도 신뢰 가능한 정서 대비가 없으면 선택적 소실 주장을 기각/식별불가로 구분한다.

**기준선**
- 원 뇌의 정규화 선형 readout
- 동일 차원의 무작위 projection
- ridge→CLIP
- 시각·의미만으로 정서 주석 예측
- 동일 architecture의 masked/contrastive 비교

**다섯 보유 데이터 계획**
- possession: Horikawa·Emo-FilM·Mind Captioning·NSD·Spacetop 다섯 보유본을 전제로 진행
- primary: Horikawa의 자극 단위 주석과 뇌 반응으로 총/조건부 추정량 정의
- validation: Emo-FilM 및 Spacetop은 각 측정 단위별 독립 재검증; 공통 척도를 가정하지 않음
- controls: NSD는 시각 정렬/신뢰도 대조; Mind Captioning은 정확한 식별과 제공 주석 확인 뒤 의미 통제 후보
- fallback: 학습 checkpoint를 못 쓰면 고정 시각 특징+작은 ridge와 원 뇌 readout으로 보존 경계부터 검증

**분석 조건**
- 원영상 내용군·dupidx와 처리 Label 대응
- 정서 주석 단위와 reliability 추정 가능 자료
- 독립 fold 안 전처리·조건화·차원 선택
- 각 보유본 voxel adapter와 split 정의

**가까운 선행**
- P001
- P015
- P022

**후보 기여**
복원 순위 대신 동일한 시각 성공 아래 사라지는 신경정보를 내용 변화와 학습 목표의 상호작용으로 판별한다. 아직 최초성 확정 아님.

**신규성 반론**
기존 representation transfer/정서 encoding 비교의 엄격한 재평가에 그칠 수 있음; 단계별 선택적 손실이 없으면 방법 감사로 축소.

**중복 판별 서명**
- observation: 원 뇌와 디코더 단계별 정서 관련 예측
- manipulation: 시각 정렬 목표와 내용군 보류
- competing_explanations: 선택적 정보 소실 대 SNR·capacity·내용 난도

**필수 여덟 질문**
- q1: 선행 비교는 존재하므로 미시도라 단정하지 않는다; 복원 성능과 정서 보존의 분리 평가가 확인 문헌의 공백이다.
- q2: 공유 피험자 디코더와 masked 뇌 표현의 공개 구현으로 단계별 readout 비교가 가능해졌다.
- q3: 시각 식별에 충분한 표현이 정서 관련 신경정보에도 충분하다는 가정.
- q4: 복잡한 장면 의미의 비선형 조합을 포착할 수 있으나 우월성은 실측할 대상이다.
- q5: 시각 정렬 이후 잃어도 원 뇌에서 내용군을 넘어 예측되는 정보가 후보이며 모형오차와 경쟁한다.
- q6: domain generalization을 정서 관련 정보 보존의 측정 조건으로 옮긴다.
- q7: 보유 자료를 복원 benchmark 대신 학습 목적의 정보 선택성을 시험하는 자료로 쓴다.
- q8: 긍정 결과는 시각·정서 코드의 공유/분리 경계를 제한하고 음성 결과는 범용 latent 충분성의 조건을 좁힌다.

**판정**
발전: E3 판별 후보; 분석 준비 조건부

**실제 출처와 확인 범위**
- P001: [The neural representation of visually evoked emotion is high-dimensional, categorical, and distributed across transmodal brain regions](https://raw.githubusercontent.com/OpenNeuroDatasets/ds002425/3f94b2bf9a75ddb62637c529d30dc40dd4ab5ba1/dataset_description.json) — 본문: 아니오; 프록시 403; Discussion: 아니오; 근거: E2
- P008: [Emotion schemas are embedded in the human visual system](https://raw.githubusercontent.com/canlab/Neuroimaging_Pattern_Masks/master/Multivariate_signature_patterns/2019_Kragel_Emotion_Schemas/Kragel_2019_SciAdv_emotion_schemas.pdf) — 본문: 공식 연구실 PDF 다운로드; 초록과 지정 본문/Discussion/Limitations 직접 검토; Discussion: 예: 지정 페이지 직접 검토; 근거: E1
- P015: [MindEye2: Shared-Subject Models Enable fMRI-To-Image With 1 Hour of Data](https://github.com/MedARC-AI/MindEyeV2) — 본문: 아니오; 공식 코드/README만 직접 확인; Discussion: 아니오; 근거: E2
- P022: [Seeing Beyond the Brain: Masked Modeling Conditioned Diffusion Model for Human Vision Decoding](https://github.com/zjc062/mind-vis) — 본문: 아니오; 공식 코드/README만 직접 확인; Discussion: 아니오; 근거: E2

## C03-02 관측과 양립하는 여러 복원에서 정서 대비는 생성 prior와 독립적으로 식별되는가

Axis: AS04, AS20, AS29, AS33

**연구 질문**
서로 다른 영상이 같은 fMRI 관측을 설명할 때 정서 관련 특징의 허용 범위는 뇌 관측에 의해 좁아지는가, 생성 prior가 결정하는가?

**신경 대상**
보류 fMRI 반응에 대해 정서 주석이 상반되는 자극 후보들의 관측 적합도

**외부 원리**
Agent09의 비유일 역문제와 Agent02의 조건부 해석 경계를 결합

**1차 모델 적용**
검증한 encoding 연산자 아래 여러 prior·seed의 후보를 만들고 held-out 관측 적합도와 독립 정서 주석을 계산한다. 초기에는 보유 자연 자극에서 matched retrieval로 후보 집합을 만든다.

**2차 과학 질문**
뇌 측정이 어떤 정서 대비를 구분하도록 충분한 정보를 제공하는지 영상 복원값이 아닌 관측 등가 집합으로 평가한다.

**3차 기존 가정 도전**
한 장의 재구성에서 정서 특징이 보이면 그 특징이 뇌로부터 복원되었다는 가정.

**주가설**
일부 정서 대비는 뇌 조건을 주면 후보 집합의 변동 폭이 축소되고 서로 다른 prior에서도 보류 관측으로 지지된다.

**대립 설명**
축소는 prior 편향·encoding 오지정·선택 과정 또는 주석의 시각 의미 의존성 때문이다.

**측정 대비**
진짜 뇌/자극 블록 내 교환 뇌/prior-only에서 후보 집합의 정서 대비 분산과 관측 적합도 비교; prior 교체 및 선택에 사용하지 않은 ROI 또는 반복 반응에서 검증.

**반증**
관측을 교환해도 같은 축소가 나타나거나 prior 교체에 따라 정서 방향이 역전되면 신경 식별성을 기각한다. 후보 다양성 부족은 식별 성공이 아닌 sampler 실패로 분리한다.

**기준선**
- 자연 자극 matched retrieval
- prior-only 후보
- 자극 블록 내 shuffled observation
- 선형 Gaussian encoding의 시뮬레이션 정답
- 생성기와 독립적인 주석/시각 모델

**다섯 보유 데이터 계획**
- possession: 다섯 보유본의 접근 여부를 개념 생성 차단 조건으로 삼지 않음
- primary: Horikawa의 실제 관측과 자연 영상 pool에서 관측 등가 후보 평가
- extension: Emo-FilM은 사건 구간 단위, Spacetop은 clip 단위로 별도 평가
- controls: NSD는 시각 역해 calibration 대조; Mind Captioning은 확인된 caption/뇌 대응이 있을 경우 의미 등가 후보 생성에 활용
- fallback: 생성기 실행 전 기존 자극 retrieval 집합으로 부분 식별 범위를 제시; 생성 posterior라는 이름을 사용하지 않음

**분석 조건**
- encoding 관측잡음모형의 독립 검증
- 여러 prior 후보의 충분한 coverage
- 주석을 선택과 평가에서 독립시키는 절차
- 반복/독립 ROI가 없을 때 시행·피험자 보류 대안

**가까운 선행**
- P076
- P015

**후보 기여**
복원 품질이 아니라 정서 대비의 부분 식별 범위와 prior 민감도를 산출한다. Agent09의 일반 역해 문제를 실제 정서-뇌 대비로 좁힌다.

**신규성 반론**
posterior uncertainty를 정서에 재명명한 수준일 수 있음; 보류 관측의 정서 대비 판별력이 핵심 추가 기여.

**중복 판별 서명**
- observation: 관측 적합도가 유사한 자극 집합의 정서 대비
- manipulation: 뇌 조건·생성 prior 교체
- competing_explanations: 뇌 관측의 식별력 대 prior에 의한 내용 결정

**필수 여덟 질문**
- q1: 일반 역문제는 기존 연구이며 정서적 식별성을 실제 뇌 관측에서 검증한 최신 선행연구 역검색은 남는다.
- q2: 관측 조건부 생성과 복수 시각 prior를 모듈별로 비교할 수 있다.
- q3: 재구성의 정서 내용이 곧 신경정보라는 가정.
- q4: 여러 양립 자극을 체계적으로 탐색하는 계산 능력을 제공한다.
- q5: generator 표현으로 동일해 보여도 실제 뇌가 구분하는 미세 단서가 후보이나 직접 관측으로 검증한다.
- q6: 역문제의 부분 식별·calibration을 정서 디코딩으로 옮긴다.
- q7: 기존 보유 뇌 반응을 새 자극 반응으로 재사용하지 않고 원관측에 대한 허용 후보를 평가한다.
- q8: 무엇이 복원되지 않았는지까지 명시해 정서 코드에 대해 측정이 허용하는 주장 범위를 바꾼다.

**판정**
발전: E3 부분 식별 후보; calibration 필수

**실제 출처와 확인 범위**
- P015: [MindEye2: Shared-Subject Models Enable fMRI-To-Image With 1 Hour of Data](https://github.com/MedARC-AI/MindEyeV2) — 본문: 아니오; 공식 코드/README만 직접 확인; Discussion: 아니오; 근거: E2
- P019: [High-resolution image reconstruction with latent diffusion models from human brain activity](https://github.com/yu-takagi/StableDiffusionReconstruction) — 본문: 아니오; 공식 코드/README만 직접 확인; Discussion: 아니오; 근거: E2
- P076: [Diffusion Posterior Sampling for General Noisy Inverse Problems](https://github.com/DPS2022/diffusion-posterior-sampling) — 본문: 아니오: 논문 본문 미열람; Discussion: 아니오; 근거: E1
- P008: [Emotion schemas are embedded in the human visual system](https://raw.githubusercontent.com/canlab/Neuroimaging_Pattern_Masks/master/Multivariate_signature_patterns/2019_Kragel_Emotion_Schemas/Kragel_2019_SciAdv_emotion_schemas.pdf) — 본문: 공식 연구실 PDF 다운로드; 초록과 지정 본문/Discussion/Limitations 직접 검토; Discussion: 예: 지정 페이지 직접 검토; 근거: E1

## C03-03 분산 뇌영역의 결합은 정서 대비를 새로 구별하는가, 같은 증거의 잡음만 줄이는가

Axis: AS03, AS16, AS20, AS30

**연구 질문**
개별 영역이 허용하는 정서적으로 다른 영상 후보를 영역 결합이 배제할 때, 그 개선은 단순 증거 평균을 넘는 결합 정보인가?

**신경 대상**
시각 및 transmodal ROI별·결합 관측으로 제약되는 정서 대비와 보류 뇌반응

**외부 원리**
Agent02의 분산 코드 중복/결합 구분과 Agent09의 관측 등가 후보 집합

**1차 모델 적용**
ROI별 encoder likelihood 또는 보정된 거리로 후보 집합을 구성하고 가산 evidence 결합과 상호작용 readout을 같은 capacity에서 비교한다.

**2차 과학 질문**
분산 정서 코드의 복원 이득이 반복 증거 축적으로 충분한지, 여러 지역의 공동 패턴에만 있는 대비인지 묻는다.

**3차 기존 가정 도전**
ROI를 합쳐 복원이 좋아지면 정보 시너지 또는 생물학적 필수성이 있다는 가정.

**주가설**
같은 voxel 수·신뢰도·모형 자유도에서 비가산 결합이 가산 증거 모형보다 정서적으로 상반된 후보를 더 잘 구별한다.

**대립 설명**
결합 이득은 SNR 증가·영역 크기·관측잡음 상관 또는 일반 시각 정보의 누적이다.

**측정 대비**
가산 대 비가산 결합의 보류 정서 대비 판별 로그점수 차이; 같은 정서/다른 객체와 같은 객체/다른 정서 후보를 구분해 상호작용이 어디에 생기는지 비교.

**반증**
SNR·영역 크기·noise covariance를 맞추면 비가산 이득이 없어지거나 시각 대조에도 동일하면 정서 결합 특이성 주장을 축소한다. ROI 삭제는 뇌 인과 결론으로 쓰지 않는다.

**기준선**
- capacity 일치 nonlinear additive 모형
- 동일 ROI 내부 무작위 voxel 분할
- noise covariance를 맞춘 합성 additive 양성/음성 대조
- 단일 ROI와 voxel 수 일치 pooled ROI
- 시각 정체성 후보 판별

**다섯 보유 데이터 계획**
- possession: 다섯 데이터 보유를 전제
- primary: Horikawa에서 코드상 ROI와 실제 coverage를 확인한 후 영역별 후보 제약
- extension: Emo-FilM/Spacetop은 독립 측정 단위의 복제 후보
- controls: NSD는 시각적 증거 결합 대조; Mind Captioning은 의미 대비 자료가 확인될 때 언어 설명 가능한 결합과 비교
- fallback: 복잡한 정보분해 estimator 대신 보류 predictive log score의 가산/비가산 차이로 주장을 제한

**분석 조건**
- 영역 coverage와 voxel 수·신뢰도 보정
- 정서 대비와 객체 대비의 충분한 교차 지지
- 후보 선택과 ROI 선택의 완전 train-fold 격리
- noise covariance와 참가자·자극 계층 불확실성

**가까운 선행**
- P005
- P009
- P017

**후보 기여**
부분망 제거의 강건성 대신 영역별 관측 등가 자극 집합이 결합으로 어떻게 달라지는지 가산 증거와 직접 경쟁시킨다.

**신규성 반론**
기존 multi-ROI 정보 비교일 수 있음; 후보 집합의 정서 대비와 capacity/noise 대조 없이는 새 기여로 세지 않음.

**중복 판별 서명**
- observation: 영역별 허용 자극 후보의 정서적 구별
- manipulation: 영역 증거의 가산/비가산 결합
- competing_explanations: 새 결합 정보 대 잡음 평균 및 공통 시각 증거

**필수 여덟 질문**
- q1: 분산성은 이미 알려졌고 영역 결합 이득의 원인 분리는 추정기·관측잡음 때문에 어렵다.
- q2: 공식 decoder와 관측 조건부 후보 집합을 통해 이득이 어떤 자극 대비에서 생기는지 조사할 수 있다.
- q3: 결합 정확도 상승이 시너지이며 ROI 제거가 인과 필수성이라는 가정.
- q4: 복잡한 공동 시각 특징을 복원 후보로 표현할 수 있으나 계산 자유도 대조가 필요하다.
- q5: 단일 시각 latent가 지운 영역 간 정서 대비가 후보이며 직접 predictive contrast로 시험한다.
- q6: 결측 센서/증거 결합을 신경 영역들의 중복과 결합 문제로 전이한다.
- q7: 보유 fMRI를 영역 중요도 순위 대신 영역이 배제하는 자극 해의 구조로 평가한다.
- q8: 가산 충분성의 음성 결과도 분산성의 설명에 비가산 신경 계산이 필요한지 제한한다.

**판정**
발전: E3; 시너지·인과 용어 사용 범위 제한

**실제 출처와 확인 범위**
- P005: [A Sensitive and Specific Neural Signature for Picture-Induced Negative Affect](https://raw.githubusercontent.com/canlab/Neuroimaging_Pattern_Masks/master/Multivariate_signature_patterns/2015_Chang_PLoSBiology_PINES/Chang_2015_PLoSBiol_PINES.pdf) — 본문: 공식 연구실 PDF 다운로드; 초록과 지정 본문/Discussion/Limitations 직접 검토; Discussion: 예: 지정 페이지 직접 검토; 근거: E1
- P009: [Common and stimulus-type-specific brain representations of negative affect](https://raw.githubusercontent.com/canlab/Neuroimaging_Pattern_Masks/master/Multivariate_signature_patterns/2021_Ceko_MPA2_multiaversive/Ceko_2022_NatNeurosci_MPA2_negative_affect.pdf) — 본문: 공식 연구실 PDF 다운로드; 초록과 지정 본문/Discussion/Limitations 직접 검토; Discussion: 예: 지정 페이지 직접 검토; 근거: E1
- P017: [Brain-IT: Image Reconstruction from fMRI via Brain-Interaction Transformer](https://github.com/WeizmannVision/brainit-fmri) — 본문: 아니오; 공식 코드/README만 직접 확인; Discussion: 아니오; 근거: E2
- P076: [Diffusion Posterior Sampling for General Noisy Inverse Problems](https://github.com/DPS2022/diffusion-posterior-sampling) — 본문: 아니오: 논문 본문 미열람; Discussion: 아니오; 근거: E1

## C03-04 복원 영상의 정서 전환은 뇌의 과거 상태 정보인가 생성기의 시간 보간인가

Axis: AS02, AS06, AS23, AS32, AS35

**연구 질문**
현재 장면 내용이 비슷한 구간에서 선행 이력에 따른 정서 관련 뇌 대비가 생성 전 latent에도 남는가, 생성 후 영상에서만 만들어지는가?

**신경 대상**
연속 fMRI의 과거 문맥 관련 정서 대비와 생성 전/후 잠재 궤적

**외부 원리**
Agent02의 현재 내용 대 이력 의존 구분; Agent09의 편집 시간 일관성과 실제 사건 의미 보존 구분

**1차 모델 적용**
과거만 보이는 영상·뇌 조건으로 잠재 궤적을 추정하고 full history/reset/history-shuffle을 비교; 생성 전 특징과 생성 영상의 정서 주석을 나눠 평가한다.

**2차 과학 질문**
정서 관련 신경 시간정보의 추가 예측력이 현재 프레임 누적이나 temporal prior로 충분히 설명되는지 시험한다.

**3차 기존 가정 도전**
매끄러운 고FPS 복원이 실제 뇌 시간상태를 복원했다는 가정과 양방향 모델의 성공을 미래예측으로 읽는 가정.

**주가설**
현재 영상·motion·사건 경계를 맞춘 뒤에도 실제 과거 뇌 조건에서만 생성 전 latent의 정서 관련 예측이 증가한다.

**대립 설명**
효과는 영상 자기상관·HRF 정렬·현재 내용·미래 입력 누출 또는 생성기의 보간이다.

**측정 대비**
고정 과거 길이에서 원이력/경계 reset/자기상관 보존 이력교환 간 보류 정서 예측 차이; 뇌→latent와 latent→영상 단계의 효과를 따로 보고한다.

**반증**
미래 입력 차단·HRF·사건경계 통제 뒤 효과가 사라지거나 생성 후에만 나타나면 뇌의 이력 정보 복원 주장을 기각한다.

**기준선**
- 프레임 평균
- 현재 프레임+FIR HRF
- motion·사건경계 누적
- 동일 관찰 길이의 과거 전용 모형
- prior-only 시간 보간

**다섯 보유 데이터 계획**
- possession: 다섯 보유본을 전제로 시간 질문을 설계
- primary: Emo-FilM의 영화축 주석과 scanner축 반응을 구분해 적용
- extension: Horikawa는 연속 신호 및 clip 내부 정보가 있을 때만 시간 질문에 적용; Spacetop은 clip후 평정으로 clip 내부 정서 궤적을 가정하지 않음
- controls: NSD는 정적 대조; Mind Captioning은 정확한 식별 후 사건 구간/시계열 자료가 있을 때 시간 의미 통제
- fallback: 연속 정서 주석이 없는 보유본에서는 clip수준 이력 대비만 분석하고 순간 전환 주장은 후속 주석/측정 조건으로 유지

**분석 조건**
- 영화·scanner onset 및 HRF/평정 지연 모형
- 실제 과거 전용 feature 추출과 bidirectional 경로 검사
- 같은 현재 내용/다른 이력의 공통 지지
- 영화·자극 family 보류와 자기상관 보존 null

**가까운 선행**
- P008
- P024
- P073

**후보 기여**
시간 생성 품질과 신경 시간정보를 단계별로 분리하고 실제 과거 조건에만 존재하는 정서 대비를 판별한다.

**신규성 반론**
정적 대 동적 encoding 비교의 반복일 수 있음; 단계별 출처 분리와 현재 내용 일치 대비가 필수.

**중복 판별 서명**
- observation: 정서 전환의 생성 전후 latent 예측
- manipulation: 과거 상태 reset/교환과 미래 차단
- competing_explanations: 신경 이력 정보 대 HRF·내용·생성 시간 prior

**필수 여덟 질문**
- q1: 시간 문맥 연구는 기존에 있으나 생성 전후 출처와 HRF를 함께 분리한 근접 선행은 아직 충분히 역검색하지 못했다.
- q2: 연속 뇌→영상 잠재와 attention 기반 영상 조작을 별도 단계로 비교할 구현이 있다.
- q3: 출력의 시간적 연속성이 신경 시간정보의 증거라는 가정.
- q4: 장면·motion·사건 순서의 복합 의존을 계산할 수 있다.
- q5: 같은 현재 내용 아래 이력에 따른 반복 가능한 뇌 차이가 후보이나 HRF로 설명되는지 먼저 시험한다.
- q6: temporal negative sampling과 편집 타당성 검사를 뇌 복원에 전이한다.
- q7: 연속 보유본을 출력FPS benchmark 대신 정보의 시간적 출처 감사에 쓴다.
- q8: 시간적 정서 코드 주장에 필요한 관측 과거의 범위를 제한하며 성공해도 방향성 회로 인과는 입증하지 않는다.

**판정**
발전: E3; 연속 측정 단위에 따라 실행 범위 조정

**실제 출처와 확인 범위**
- P008: [Emotion schemas are embedded in the human visual system](https://raw.githubusercontent.com/canlab/Neuroimaging_Pattern_Masks/master/Multivariate_signature_patterns/2019_Kragel_Emotion_Schemas/Kragel_2019_SciAdv_emotion_schemas.pdf) — 본문: 공식 연구실 PDF 다운로드; 초록과 지정 본문/Discussion/Limitations 직접 검토; Discussion: 예: 지정 페이지 직접 검토; 근거: E1
- P024: [Cinematic Mindscapes: High-quality Video Reconstruction from Brain Activity](https://github.com/jqin4749/MindVideo) — 본문: 아니오; 공식 코드/README만 직접 확인; Discussion: 아니오; 근거: E2
- P073: [FateZero: Fusing Attentions for Zero-shot Text-based Video Editing](https://github.com/ChenyangQiQi/FateZero) — 본문: 아니오: 논문 본문 미열람; Discussion: 아니오; 근거: E1
- P015: [MindEye2: Shared-Subject Models Enable fMRI-To-Image With 1 Hour of Data](https://github.com/MedARC-AI/MindEyeV2) — 본문: 아니오; 공식 코드/README만 직접 확인; Discussion: 아니오; 근거: E2

## C03-05 객체 목록을 보존한 장면 관계 변경은 정서 신경 대비에 별도 결합 계산을 요구하는가

Axis: AS19, AS21, AS24, AS29

**연구 질문**
객체·저수준 변화가 통제된 장면 관계 변화에서 정서 관련 뇌 대비는 객체별 감각·의미 예측의 합으로 충분한가, 관계에 따른 결합항이 필요한가?

**신경 대상**
객체 목록이 같은 장면들 사이의 정서 관련 시각/transmodal neural contrast

**외부 원리**
Agent09의 의미 보존 검증과 기대 정보이득 설계; Agent02의 정서 schema와 내용 조건부 해석

**1차 모델 적용**
자연 자극 matched retrieval과 보존 제약 편집을 이용해 가산 객체 모형과 관계 결합 모형의 예측이 갈리는 후보를 선택한다. 선택은 독립 주석의 조작 타당성을 통과한 뒤 고정한다.

**2차 과학 질문**
정서와 연결된 장면 정보가 객체·감각 요소의 누적만으로 설명되는지, 요소 간 관계가 다른 신경 대비를 만드는지 묻는다.

**3차 기존 가정 도전**
객체/캡션 목록을 맞추면 의미가 완전히 같고 남은 차이는 순수 정서라는 가정 및 decoder activation 극대화가 가설 판별이라는 가정.

**주가설**
비목표 시각 변화와 객체 내용을 맞춘 조건에서 관계 결합 모형이 독립 정서 주석과 관련된 실제 뇌 대비를 가산 모형보다 더 잘 예측한다.

**대립 설명**
차이는 위치·질감·편집 artifact·누락 의미 특징 때문이며 관계 결합이나 정서 관련 추가 계산이 필요하지 않다.

**측정 대비**
원본/무편집 왕복/목표 관계편집/동일 강도 비목표편집을 비교하고 자연 matched pair에서 방향 재현; 고정 예산의 random/coverage/disagreement/EIG 선택으로 실제 보류 log score 비교.

**반증**
독립 생성기·자극군에서 실제 뇌 대비가 재현되지 않거나 저수준/비목표 편집이 차이를 설명하면 결합 해석을 기각한다. 새 편집물의 뇌 반응 미측정 상태에서는 in-silico 후보 선택까지만 주장한다.

**기준선**
- 비선형 additive 객체/감각 모형
- 관계 특징 없는 동일 capacity 모형
- 자연 자극 matched pair
- 무편집 inversion
- 동일 강도 비목표 편집
- random·coverage·단순 disagreement 자극 선택

**다섯 보유 데이터 계획**
- possession: 다섯 보유본으로 먼저 자연 자극 비교와 관측모형을 개발
- primary: Horikawa에서 객체 목록이 비슷하고 관계/정서 주석이 다른 자연 자극군 탐색
- extension: Emo-FilM/Spacetop은 사건 또는 clip단위 자연 대비; 같은 neural estimand로 강제 통합하지 않음
- controls: NSD는 시각·관계 encoding 대조; Mind Captioning은 보유본의 실제 설명 단위 확인 후 객체 목록과 관계 설명 비교에 활용
- new_measurement: 편집 효과의 뇌검증은 새 자극의 실제 제시·측정이 필요; 원본 BOLD 전용 금지
- fallback: 생성기 실행 없이 보유 자연자극의 matched observational contrast로 시작하고 인과 주장을 제외

**분석 조건**
- 객체 목록·공간/사건관계·정서 주석의 독립 측정
- 내용·편집 강도의 공통 지지 및 자연성 문턱 사전 고정
- 선택에 쓰지 않은 encoding 모형·피험자·자극 평가
- 새 편집 자극에 대한 실제 뇌 측정 및 관측 likelihood 검증

**가까운 선행**
- P008
- P070
- P077

**후보 기여**
adversarial 자극 자체는 이미 제안됐다. 객체별 가산과 관계 결합이라는 특정 경쟁 신경 설명을 보존 제약 및 실제 관측 판별로 좁힌다는 점이 후보 기여다.

**신규성 반론**
기존 scene/emotion schema 또는 최적 자극 연구의 재실행일 위험 높음; 관계 결합의 별도 예측과 독립 뇌관측이 없으면 기각.

**중복 판별 서명**
- observation: 같은 객체 목록의 관계 변화에 따른 정서 관련 뇌 대비
- manipulation: 독립 검증된 관계/비목표 편집과 가설 판별 선택
- competing_explanations: 관계 결합 계산 대 객체 감각 가산 및 편집 artifact

**필수 여덟 질문**
- q1: 장면 schema와 adversarial 자극은 이미 있었고 보존 검증과 새 뇌측정 비용이 주요 제약이다; 최초성을 주장하지 않는다.
- q2: attention 편집과 amortized design으로 여러 후보를 만들고 실제 경쟁 예측을 비교할 수 있다.
- q3: 같은 객체/캡션이면 모든 의미가 보존되고 정서만 변했다는 가정.
- q4: 장면의 복잡한 관계를 조건별 생성·분해하는 계산 능력을 제공한다.
- q5: 동일 객체 설명에 압축되지 않는 관계 의존 신경 대비가 후보이며 시각모형 오류와 비교한다.
- q6: Bayesian design을 activation 최적화가 아닌 가산 대 결합 모형 판별로 전이한다.
- q7: 다섯 보유본을 자연 통제군·관측모형·신뢰도 추정에 쓰되 새 편집 반응은 별도로 측정한다.
- q8: 관계 결합이 필요하다는 결과 또는 가산 충분성 모두 정서 관련 장면 계산의 최소 설명을 제한한다.

**판정**
수정 필요: E3 장기 후보; 자연 대비부터 진행, 새 편집 뇌검증은 추가 측정

**실제 출처와 확인 범위**
- P008: [Emotion schemas are embedded in the human visual system](https://raw.githubusercontent.com/canlab/Neuroimaging_Pattern_Masks/master/Multivariate_signature_patterns/2019_Kragel_Emotion_Schemas/Kragel_2019_SciAdv_emotion_schemas.pdf) — 본문: 공식 연구실 PDF 다운로드; 초록과 지정 본문/Discussion/Limitations 직접 검토; Discussion: 예: 지정 페이지 직접 검토; 근거: E1
- P001: [The neural representation of visually evoked emotion is high-dimensional, categorical, and distributed across transmodal brain regions](https://raw.githubusercontent.com/OpenNeuroDatasets/ds002425/3f94b2bf9a75ddb62637c529d30dc40dd4ab5ba1/dataset_description.json) — 본문: 아니오; 프록시 403; Discussion: 아니오; 근거: E2
- P070: [Prompt-to-Prompt Image Editing with Cross-Attention Control](https://raw.githubusercontent.com/prompt-to-prompt/prompt-to-prompt.github.io/main/ptp_files/Prompt-to-Prompt_preprint.pdf) — 본문: 예: 공식 PDF 확보·§1/§3/§4/§5 관련 부분 직접 열람; 전체 정독 아님; Discussion: 예: §5 Limitations p.9; §4 평가 논의 p.9; 근거: E1
- P077: [Deep Adaptive Design: Amortizing Sequential Bayesian Experimental Design](https://proceedings.mlr.press/v139/foster21a.html) — 본문: 예: 공식 PDF 확보; §2–4/§7 직접 열람; Discussion: 예: §7 Discussion 및 Limitations and Future Work p.9; 근거: E1

## 한계와 검증
- 본 Round2에서 실제로 Agent02/09 보고서를 읽고 수입 원리를 재구성했다. 과거 원증거 사실검사는 이 Round2로 소급 계산하지 않는다.
- 다섯 데이터의 보유는 사용자 진술로 인정한다. 정확한 schema·version·checkpoint는 실행 조건이며 문헌·Axis·RQ 진행을 막는 조건이 아니다. Mind Captioning의 식별자는 이름으로 추정하지 않는다.
- 모든 후보의 과학적 연결은 E3이며 실험 결과가 아니다. source_papers의 공식 코드/서지/본문 범위는 reference_catalog의 source_scope를 따른다.
- 기존 문헌 역대조만 수행했고 새 네트워크 검색·최초성 확정·모델 실행·뇌 분석·생성 자극 실험은 하지 않았다.
- 읽은 Agent02/09의 원문 검토를 본 Agent의 독립 본문 정독으로 세지 않는다. 생성 편집·ROI삭제·특징조작은 인간 뇌 인과를 자동 입증하지 않는다.
- C03-01은 목적함수에 의한 표현 소실, C03-02는 관측 역해 비유일성, C03-03은 영역 증거 결합, C03-04는 과거 시간정보 출처, C03-05는 장면 관계 결합을 대상으로 하므로 모델·데이터명 교체로 만든 중복 후보가 아니다.
- JSON 필수23필드×후보5건, 후보별 canonical 출처 최소2개, AS 식별자 실재, 후보별 여덟 답변을 로컬 구조검사로 확인했다.
