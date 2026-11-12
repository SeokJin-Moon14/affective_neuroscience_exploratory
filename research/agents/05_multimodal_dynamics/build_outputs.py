"""독립조사 산출물 생성. 네트워크 요청·모델 실행은 하지 않는다."""
from pathlib import Path
import csv, hashlib, json, re

ROOT = Path(__file__).resolve().parent
E = ROOT / 'evidence'
DATE = '2026-11-12'
FIELDS = 'paper_id title authors year venue doi_or_arxiv official_url version source_verified full_text_access discussion_access domain axis_tags original_rq dataset stimulus brain_measurement model_method training_objective main_findings scientific_contribution limitations future_directions future_direction_source_location transfer_idea relevant_datasets novelty_risk evidence_level agent verification_date confidence needs_followup'.split()

# 내용은 읽은 공식 문서·코드의 범위로 한정한다. 과학적 전이는 E3이다.
PAPERS = [
 dict(key='imagebind', repo='facebookresearch/ImageBind', title='ImageBind: One Embedding Space To Bind Them All', year=2023, venue='CVPR 2023', ident='arXiv:2305.05665', axis='B;M;J;X;S',
 rq='이미지와 짝지은 학습만으로 여러 모달리티를 하나의 검색 가능한 공간에 묶을 수 있는가?',
 dataset='모델카드: AudioSet; SUN RGB-D; Ego4D; LLVIP; OpenCLIP 초기화', stimulus='이미지/영상; 일반 오디오; 텍스트; 깊이; 열영상; IMU',
 method='모달리티별 인코더와 공통 차원 출력; imagebind_huge 출력1024차원; 기본 영상 입력2프레임',
 objective='이미지-모달리티 쌍 정렬; 이미지·텍스트 인코더 동결(모델카드 직접확인); 세부 학습 손실 본문 미확인',
 findings='공식 README는 교차모달 검색·임베딩 산술과 emergent zero-shot 응용을 보고한다. 모델 구현에서 공통 출력차원을 직접확인했다.',
 contribution='완전한 모든 모달리티 쌍 없이 공통 좌표를 제공하는 계산 도구.',
 limitations='공식 모델카드는 작은 모달리티별 학습셋으로 개념 범위가 제한됨을 명시. E3: 공통 좌표는 고유정보 보존 또는 뇌의 통합 알고리즘을 보증하지 않는다.',
 transfer='E3: 이미지 중심 공통 공간과 모달리티별 인코더의 잔여 정보를 비교하여 정서 관련 신경정보가 공유표상만으로 충분한지 시험.',
 novelty='공통 공간을 fMRI에 단순 회귀하면 기존 encoding의 모델 교체. 고유정보의 일반화되는 추가 기여가 핵심 판별.',
 code='imagebind_model.py; imagebind_model_card.md; imagebind_LICENSE',
 follow='README는 CC-BY-NC, LICENSE·모델카드는 CC-BY-NC-SA4.0으로 표기 차이. 사용 전 LICENSE 우선 재검토; 체크포인트 미다운로드.'),
 dict(key='cavmae', readme='cavmae_master_README.md', branch='master', repo='YuanGongND/cav-mae', title='Contrastive Audio-Visual Masked Autoencoder', year=2023, venue='ICLR 2023', ident='DOI/arXiv 미확인; OpenReview:QPtMRyk5rb', axis='M;J;X;H',
 rq='대조학습과 마스킹 복원을 함께 사용해 오디오-시각 공통 표상을 개선할 수 있는가?',
 dataset='AudioSet; VGGSound; ImageNet 사전학습 초기화', stimulus='mel spectrogram과 이미지 프레임 쌍',
 method='모달리티별 블록+공유 블록; 공동 reconstruction latent와 개별 contrastive latent; 이미지224×224 입력',
 objective='마스킹된 패치의 MSE 합+시청각 NCE; 코드에서 손실 가중치와 모달리티별 마스킹 분리 확인',
 findings='공식 README는 대조 목적이 검색과 공동표상에 도움을 준다고 보고. 코드 forward_encoder/forward에서 별도 경로와 두 손실 조합을 직접확인.',
 contribution='대응성 보존과 각 모달리티 복원을 독립적으로 조절하는 계산적 비교가 가능.',
 limitations='E3: 복원 잔여는 정서 고유정보와 동치가 아니다. 프레임 기반 시각 입력을 장기영상 모델로 취급 불가. 공개 raw 데이터는 저작권상 제공하지 않는다고 README 명시.',
 transfer='E3: contrastive-only·MAE-only·결합의 고유 잔여가 동일한 신경표상을 설명하는지, 정서 주석과 독립적으로 학습해 비교.',
 novelty='세 손실의 encoding 점수 비교만으로는 약함. 어떤 정보가 어느 목표에서 제거되는지 반증 가능한 분해가 필요.',
 code='cavmae_models.py', follow='main 브랜치 README는 오래된 미공개 안내이고 master가 실제 공개 구현. Scale++는 원논문 외 후속으로 명시되어 원논문 결과와 혼합 금지.'),
 dict(key='factorcl', repo='pliang279/FactorCL', title='Factorized Contrastive Learning: Going Beyond Multi-view Redundancy', year=2023, venue='NeurIPS 2023', ident='arXiv:2306.05268', axis='M;X;K;J;P',
 rq='여러 view에 공통인 정보뿐 아니라 과제 관련 고유정보도 보존하는 대조학습을 만들 수 있는가?',
 dataset='공유·고유정보를 조절한 합성자료; MultiBench; IRFL', stimulus='일반 다중모달 feature; 이미지·텍스트; 합성 벡터',
 method='공유/고유 표상 분해; MI 하한·상한; NCE-CLUB critic; 합성자료 생성기',
 objective='과제 관련 MI 하한 최대화와 과제 무관 MI 상한 최소화(README); critic 구현 직접확인',
 findings='공식 README는 공유·고유 task-relevant 분해를 제시. 합성 생성기와 InfoNCE/NCE-CLUB 구현 확인; 이론 가정·성능 수치는 원문 미확인.',
 contribution='공통 표현이 충분하다는 가정을 직접 경쟁 모델로 만들 수 있다.',
 limitations='E3: 식별성 정리와 독립성 가정은 원문 미확인. neural synergy의 정확한 PID 추정법으로 취급하면 안 된다. 타깃 의존 학습은 label leakage 위험.',
 transfer='E3: 영상/비언어 오디오 공유정보와 고유정보의 신경 예측 기여를 synthetic null과 함께 평가. 정서 라벨은 외부검증으로만 사용.',
 novelty='shared/private latent 자체는 선행방법. 정서 관련 뇌정보가 그 분해 어디에 있고 어떤 조건에서 바뀌는지가 새 질문.',
 code='factorcl_critic_objectives.py; factorcl_dataset.py', follow='정리·가정·전체 ablation 원문 확인 필요. 표상 회전·비유일성 및 추정기 편향 검토.'),
 dict(key='mbt', repo='google-research/scenic', title='Attention Bottlenecks for Multimodal Fusion', year=2021, venue='NeurIPS 2021', ident='arXiv:2107.00135', axis='M;X;I;R;H',
 rq='시청각 token의 모든 쌍 대신 좁은 latent 통로로 정보를 교환해 효과적으로 융합할 수 있는가?',
 dataset='AudioSet; EPIC-KITCHENS100; VGGSound', stimulus='RGB 패치; spectrogram 패치',
 method='Multimodal Bottleneck Transformer; fusion_layer·use_bottleneck·share_encoder 선택; bottleneck 모달리티 평균 갱신',
 objective='분류 supervision; 코드에서 sigmoid 또는 softmax cross-entropy 계열 손실 확인',
 findings='공식 README는 세 시청각 benchmark 결과와 RGB/Spec/양쪽 체크포인트를 제공. 코드에서 통합 시작 층과 좁은 정보 통로 직접확인.',
 contribution='정보 교환 시점과 용량을 분리 조절하는 구조적 대조군.',
 limitations='E3: bottleneck token 수는 뇌의 통합 차원과 같지 않다. 분류 supervision·모델 크기·최적화 차이가 설명할 수 있음.',
 transfer='E3: 같은 감각 정보에서 통로 용량·통합 시점을 바꾼 모델의 신경 설명력 변화로 정서 관련 정보의 선택적 압축을 시험.',
 novelty='융합층별 RSA 자체는 약함. parameter-matched late fusion와 충분성 곡선·외부자극 전이가 필요.',
 code='mbt_model.py', follow='모델 zoo는 Scenic/Flax; 체크포인트 링크 존재만 확인. GPU 실행·다운로드·정확한 버전 재현 미확인.'),
 dict(key='mert', repo='yizhilll/MERT', title='MERT: Acoustic Music Understanding Model with Large-Scale Self-supervised Training', year=2023, venue='arXiv preprint(공식 README 인용판); 정식학회 버전 별도 미확인', ident='arXiv:2306.00107', axis='B;J;I;H;D',
 rq='음악 신호에 맞춘 자기지도 목표로 범용 음악 이해 표현을 만들 수 있는가?',
 dataset='README에서 music4all public 변형 확인; 전체 사전학습 corpus는 본문 미확인', stimulus='음악 waveform; 24kHz 준비 예제',
 method='MERT 95M/330M; RVQ-VAE 또는 K-means acoustic teacher와 CQT musical teacher',
 objective='masked acoustic teacher token 예측과 CQT 복원; 모델의 CQT MSE 모듈 직접확인',
 findings='공식 문서는 음악 특화 teacher·체크포인트·feature 추출 경로를 제공. 성능 수치·음악 정서 타깃의 적합성은 미확인.',
 contribution='텍스트 정렬 없이 음악 구조를 학습한 표현을 CLAP과 비교할 수 있다.',
 limitations='E3: 영화 음악과 사전학습 음악의 분포 차이. 음악 표현은 정서 정답이 아니다. README의 v0 링크 일부가 v1으로 연결되어 버전 주의.',
 transfer='E3: MERT와 CLAP이 서로 보존·소실하는 음악 정보를 분해하고, 음량·스펙트럼 통제 후 정서 관련 신경잔여와의 관계 검증.',
 novelty='음악 정서 분류가 아니라 텍스트 공통표상에 남지 않는 음악 정보의 신경적 필요성이 타깃.',
 code='mert_model.py; mert_model_README.md', follow='정식 출판 서지; 체크포인트·음악 license; inference 시간해상도 검증 필요. Speech Features는 연구대상 아님.'),
 dict(key='clap', repo='LAION-AI/CLAP', title='Large-scale Contrastive Language-Audio Pretraining with Feature Fusion and Keyword-to-Caption Augmentation', year=2023, venue='ICASSP 2023', ident='arXiv:2211.06687', axis='B;M;J;X;S',
 rq='자유 길이 오디오와 텍스트를 정렬하여 범용 오디오 이해·검색을 개선할 수 있는가?',
 dataset='LAION-Audio-630K; README의 ESC50 평가; 후속 음악/음성 체크포인트는 별도', stimulus='일반 소리·음악 waveform과 텍스트; API48kHz',
 method='CLAP audio/text 인코더; feature fusion; keyword-to-caption augmentation',
 objective='시청각이 아닌 오디오-텍스트 대조학습; 코드의 양방향 cross-entropy 확인',
 findings='공식 README는 오디오·텍스트 latent 추출 API, fusion 선택과 retrieval/zero-shot 평가를 제공. 재현실행은 하지 않음.',
 contribution='음악·환경음에서 언어와 공유하는 정보를 측정할 비교공간.',
 limitations='README는 ESC50 데모 평가 조건이 논문과 달라 수치가 조금 높다고 명시. E3: 텍스트 표현이 담지 못하는 소리를 정서 무관으로 오판할 위험.',
 transfer='E3: MERT/일반 오디오 특징의 CLAP 공통공간 밖 잔여가 신경 정서표상에 필요한지 검증.',
 novelty='CLAP 텍스트 프롬프트 점수로 만든 정서 라벨을 독립 정답처럼 평가하면 순환논증. 실측 주석과 분리.',
 code='clap_loss.py', follow='후속 음악 모델과 2023 원논문 모델 버전 분리; 체크포인트 미다운로드. 음성 feature 연구 제외.'),
 dict(key='ave', repo='YapengTian/AVE-ECCV18', branch='master', title='Audio-Visual Event Localization in Unconstrained Videos', year=2018, venue='ECCV 2018', ident='arXiv:1803.08842', axis='C;D;M;H;T',
 rq='무제약 영상에서 소리와 영상에 함께 해당하는 사건의 시간적 위치를 찾을 수 있는가?',
 dataset='AVE; 공식 feature 다운로드 링크; 직접 데이터 다운로드 안 함', stimulus='영상과 오디오 feature; 코드10개 시간구간',
 method='audio-guided visual attention; 모달리티별 Bi-LSTM; 융합 예측; supervised/weakly supervised/cross-modality localization',
 objective='사건 위치의 supervision 및 약지도 분류; cross-modal matching',
 findings='공식 저장소는 세 localization 과제와 attention 시각화 제공. models.py에서10구간·양방향 LSTM·시청각 결합 직접확인.',
 contribution='프레임 전환과 모달리티가 함께 나타나는 사건을 구분할 출발 도구.',
 limitations='E3: co-occurrence localization은 정서적 의미의 congruence 또는 뇌의 event boundary와 동치가 아니다. 과거 PyTorch0.3·Keras2 구현.',
 transfer='E3: 시각 cut·오디오 onset·교차모달 일치 변화 중 무엇이 정서 관련 신경전이를 설명하는지 분리.',
 novelty='event boundary와 정서 변화의 일반적 상관은 중복 위험 높음. 통합 구조의 전환 여부와 일치/불일치 대조 필요.',
 code='ave_models.py', follow='실시간 예측 주장 금지: Bi-LSTM의 미래입력 있음. event label과 신경자극 시간정렬은 별도 확인.'),
 dict(key='tcc', repo='google-research/google-research', branch='master', title='Temporal Cycle-Consistency Learning', year=2019, venue='CVPR 2019', ident='arXiv:1904.07846', axis='C;D;J;K;T',
 rq='서로 다른 속도의 수행 영상들을 시간적으로 왕복 정렬하며 의미 있는 단계표상을 학습할 수 있는가?',
 dataset='README: pouring data; phase classification/progression·Kendall tau 평가', stimulus='프레임 시퀀스; 순차 embedding',
 method='soft nearest-neighbor 왕복정렬; cycle-consistency; phase progression 평가',
 objective='시퀀스 A→B→A 후 시작 위치로 돌아오게 하는 classification/regression loss',
 findings='코드 align_pair_of_sequences에서 soft 이웃과 왕복 logits 확인. 공식 README는 positional/LSTM 인코더가 단순 frame 위치를 외우는 trivial solution을 경고.',
 contribution='동일 시간 대신 대응되는 사건 진행 단계로 비교할 수 있는 원리.',
 limitations='공식문서 경고: 위치정보만으로 cycle loss가 내려갈 수 있음. E3: 강제 정렬이 실제 신경 시간차를 지워버릴 수 있음.',
 transfer='E3: 정서 관련 신경전이가 경과시간에 정렬되는지 의미적 사건단계에 정렬되는지 비교. 정렬 학습과 신경검정 자극을 분리.',
 novelty='DTW 대비 장점 없이 TCC를 사용하는 것은 모델교체. 위치-only·DTW·독립 사건주석과 경쟁 필요.',
 code='tcc_alignment.py', follow='tcc가 별도 repo가 아니라 google-research/google-research 하위 디렉터리. pretrained 범용 시간정렬 checkpoint 확인 안 됨.'),
 dict(key='videomamba', repo='OpenGVLab/VideoMamba', title='VideoMamba: State Space Model for Efficient Video Understanding', year=2024, venue='arXiv preprint(공식 README 인용판); 정식학회 버전 별도 미확인', ident='arXiv:2403.06977', axis='D;I;V;H;T',
 rq='영상의 국소 중복과 전역 의존성을 선형 복잡도의 상태공간 연산으로 함께 처리할 수 있는가?',
 dataset='공식 README에 short-term/long-term/video-text tasks; 개별 dataset 목록은 하위 config 후속확인', stimulus='시공간 영상 token; 영상-텍스트 쌍',
 method='Mamba 기반 시공간 모델; self-distillation; 코드 기본 bimamba=True',
 objective='자기증류·분류·masked modeling·영상텍스트 retrieval 경로 제공; 개별 목표 수식 원문 미확인',
 findings='공식 README는 장기 처리의 효율과 여러 영상과제를 보고. 코드에서 양방향 Mamba 옵션과 시공간 tokenization 직접확인.',
 contribution='긴 문맥을 처리하는 계산 용량과 신경적 시간통합의 관계를 시험할 후보.',
 limitations='E3: state-space라는 명칭은 생물학적 상태 또는 인과적 online prediction을 뜻하지 않음. 양방향 처리와 학습량이 통제되어야 함.',
 transfer='E3: 미래 접근을 차단한 입력창 길이별 표현으로 정서 관련 신경정보의 문맥 지속시간과 boundary reset을 평가.',
 novelty='긴 window의 단순 encoding 향상은 자극정보 증가로 설명 가능. matched-history·shuffle·state reset 대조가 필수.',
 code='videomamba_model.py', follow='README에 layer-decay bug/후속 변경 이력 있음. 체크포인트와 code revision 고정; 실제 causal cache 호환성 후속검증.'),
 dict(key='vjepa2', repo='facebookresearch/vjepa2', title='V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning', year=2025, venue='arXiv preprint(공식 README 인용판)', ident='arXiv:2506.09985', axis='D;V;J;I;H;T',
 rq='영상 잠재표상 예측으로 이해·미래 예측과 행동조건 계획에 재사용 가능한 모델을 배울 수 있는가?',
 dataset='인터넷 규모 영상; V-JEPA2-AC는 로봇 궤적 posttraining; 세부 전체 corpus 본문 미확인', stimulus='영상; AC 변형만 로봇 행동',
 method='encoder+predictor; masked latent feature prediction; V-JEPA2와 V-JEPA2-AC를 구별',
 objective='마스킹된 영상 latent 예측; 행동조건 posttraining은 별도 목적·체크포인트',
 findings='공식 README는 motion understanding·action anticipation·AC planning을 보고. predictor.py에서 위치/마스크 token 및 projection 직접확인.',
 contribution='픽셀 차이와 잠재 상태 예측오류를 비교하는 도구.',
 limitations='E3: masked latent 복원이 자동으로 과거→미래 예측인 것은 아니다. 로봇 action-conditioning을 수동 영상 관람의 뇌 계산으로 직접 전이 불가.',
 transfer='E3: 과거 입력만 허용한 잠재 예측 잔차가 저수준 변화·의미·사건 경계를 넘는 정서 관련 신경전이 정보를 갖는지 평가.',
 novelty='prediction error와 정서변화의 상관은 오래된 일반문제. 표현오류와 통합 오류를 분리한 반증대조가 있어야 유지.',
 code='vjepa2_predictor.py', follow='같은 README에2026 V-JEPA2.1(arXiv2603.14482)이 공존. 본 행은2025 원논문만 집계; 코드 snapshot은 현재 통합판임.'),
 dict(key='videoprism', repo='google-deepmind/videoprism', title='VideoPrism: A Foundational Visual Encoder for Video Understanding', year=2024, venue='ICML 2024; PMLR235:60785–60811', ident='arXiv:2402.13217', axis='B;D;I;J;H;S',
 rq='고정된 하나의 영상 인코더로 외형·동작 중심의 다양한 영상과제를 처리할 수 있는가?',
 dataset='본문:36M 고품질 video-caption쌍+582M noisy-text clips; WebLI 초기/1단계 이미지자료;33개 평가 benchmark', stimulus='영상16프레임(원논문); 영상-텍스트 학습',
 method='1단계 영상텍스트 contrastive;2단계 global-local latent distillation+token shuffling; frozen encoder',
 objective='대칭 cross-entropy 정렬 후, 첫 단계 teacher의 전역·token embedding을 마스킹된 영상으로 예측(본문§2.3,p3–4)',
 findings='본문§3.5 Figure4,p8에서 global distillation·token shuffling ablation 직접확인. 여러 구성요소가 motion-rich SSv2와 appearance-driven K400에 다른 영향을 보여 전체 점수로 정보보존을 대체하기 어려움.',
 contribution='언어로 얻은 의미와 영상문맥에서 얻은 동작정보를 함께 유지하는 학습 원리.',
 limitations='저자§3.6,p8: noisy text의 불완전성·편향;16프레임 짧은 클립으로 장기영상 이해의 한계; 일부 과제는 end-to-end/parameter-efficient adaptation에 이점. E3: public model은 원논문 모델과 같지 않음.',
 transfer='E3: 외형·동작·전역 의미의 보존 정도가 다른 표현을 대조해, 정서 관련 신경정보가 사건 흐름에서 생기는지 정적 의미의 누적만으로 충분한지 검정.',
 novelty='범용 video encoder의 neuroscience 적용 자체는 논문이 이미 CV for Science에서 다룸(뇌 BOLD 분석은 아님). 정서 신경통합의 경쟁가설 판별로 한정.',
 code='videoprism_models.py; videoprism_paper.pdf; videoprism_paper.txt', follow='2025 공개 base/large와2024 논문 base/giant 모델 차이; 데이터 wipeout·학습 contamination을 별도로 감사.',
 future='저자 직접제안: 현재 인코더를 장기영상 이해 시스템의 구성요소로 활용(§3.6,p8). Agent E3: causal temporal module과 결합하여 사건경계에서 신경시간통합의 재설정을 시험.',
 futureloc='공식 PMLR PDF §3.6 Limitations,p8; 로컬 videoprism_paper.txt 529–543행. §5 Conclusion,p9도 읽음.')
]

versions = json.loads((E / 'repository_versions.json').read_text())
vmap = {}
for x in versions:
    for line in x['refs'].splitlines():
        sha, ref = line.split('\t')
        vmap[(x['repo'], ref.rsplit('/',1)[-1])] = sha

rows=[]
for n,p in enumerate(PAPERS,1):
    fn=p.get('readme',p['key']+'_README.md')
    text=(E/fn).read_text()
    m=re.search(r'author\s*=\s*\{(.*?)\}',text,re.S|re.I)
    authors=re.sub(r'\s+',' ',m.group(1)).replace(' and ','; ') if m else '미확인'
    branch=p.get('branch','main')
    src='https://github.com/'+p['repo']
    if p['key']=='mbt':src+='/tree/main/scenic/projects/mbt'
    if p['key']=='tcc':src+='/tree/master/tcc'
    if p['key']=='cavmae':src+='/tree/master'
    full=p['key']=='videoprism'
    rows.append(dict(zip(FIELDS,[
        f'MD05-P{n:02}',p['title'],authors,p['year'],p['venue'],p['ident'],src,
        f"공식 저장소 {branch}@{vmap[(p['repo'],branch)]}; {DATE} 수집; 논문판과 현재코드 차이 별도",
        f'검증됨: 공식 README 서지·방법 및 {p["code"]}; evidence_manifest.csv의 원본URL·SHA256 참조',
        '예: 공식PMLR PDF27쪽 확보;§1–2.3,§3.5–3.6,§5 직접읽음;전문 전체 정독은 아님' if full else '아니오: 논문 본문 미접근; 공식 코드·문서만 직접확인',
        '전용 Discussion 절 없음;§3.6 Limitations,p8와§5 Conclusion,p9 직접읽음' if full else '아니오: 저자 Discussion·논문 future work 미확인',
        '멀티모달 표현학습/시간적 영상·오디오·음악 계산',p['axis'],p['rq'],p['dataset'],p['stimulus'],
        '해당 연구의 인간 뇌측정 없음; 본 과제 fMRI 전이는 E3',p['method'],p['objective'],p['findings'],p['contribution'],p['limitations'],
        p.get('future','저자 Discussion 미확인; 다음은 Agent E3 전이: '+p['transfer']),
        p.get('futureloc','저자 future direction 위치 없음. Agent 추론은 report.md의 문제·전이 항목.'),p['transfer'],
        'Horikawa→Emo-FilM→Spacetop→NSD 순 실현성검토 예정; 본 독립조사에서 실제 modalities·시간별주석·자극 접근성 미검증',p['novelty'],
        'E1(논문 방법·Limitations 직접+공식코드);신경전이는E3' if full else 'E1(공식코드·README 범위);논문본문 미검증;신경전이는E3',
        'Agent05 Multimodal Dynamics',DATE,'서지·문서/코드 높음;신경전이 가설 낮음~중간',p['follow']
    ])))
with (ROOT/'papers.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=FIELDS);w.writeheader();w.writerows(rows)

# 성공·실패 HTTP 요청과 현재 사본을 연결한다.
logs=[]
for fn in ['retrieval_log.json','retrieval_details.json','retrieval_additional.json','retrieval_mert.json','retrieval_pmlr.json','retrieval_paper.json']:
    for r in json.loads((E/fn).read_text()):
        name=r.get('file',r.get('key','')+'_README.md');local=E/name
        logs.append(dict(source=r.get('url','초기 실패 로그에 최종 URL 미기록'),local_file='evidence/'+name,status=str(r['status']),
                         sha256=hashlib.sha256(local.read_bytes()).hexdigest() if local.exists() and r['status']==200 else '',
                         verified_on=DATE,confidence='직접확인' if r['status']==200 else '접근실패',needs_followup='본문·체크포인트 후속 확인' if r['status']==200 else '별도 허용 경로에서 재확인',origin_agent='Agent05'))
logs.extend([
 dict(source='https://raw.githubusercontent.com/mlresearch/v235/gh-pages/_posts/2024-07-08-zhao24f.md',local_file='evidence/videoprism_publisher_metadata.md',status='200/git clone',sha256='',verified_on=DATE,confidence='출판사 공식 서지',needs_followup='없음',origin_agent='Agent05'),
 dict(source='https://raw.githubusercontent.com/facebookresearch/ImageBind/84c25a9869d516bdf3b68a06864849a7df513df8/paper.html',local_file='evidence/imagebind_official_ghpages/paper.html',status='200/git clone',sha256='',verified_on=DATE,confidence='arXiv 식별자 직접확인',needs_followup='원문 접근',origin_agent='Agent05')])
meta=E/'pmlr_v235_metadata/_posts/2024-07-08-zhao24f.md'
if meta.exists():
    (E/'videoprism_publisher_metadata.md').write_bytes(meta.read_bytes())
for r in logs:
    lp=ROOT/r['local_file']
    if lp.exists() and not r['sha256'] and r['status'].startswith('200'):
        r['sha256']=hashlib.sha256(lp.read_bytes()).hexdigest()
with (ROOT/'evidence_manifest.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=list(logs[0]));w.writeheader();w.writerows(logs)
assert len(rows)==11 and len(FIELDS)==32
assert all(r['authors']!='미확인' for r in rows)
print(json.dumps({'papers':len(rows),'fields':len(FIELDS),'fulltext_selected_sections':sum('예:' in r['full_text_access'] for r in rows),'source_records':len(logs)},ensure_ascii=False))
