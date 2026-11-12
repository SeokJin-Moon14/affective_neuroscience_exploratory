# Agent06 Frontier AI — Round2 실제 정보 교환

2026-11-12. 기존 Agent06 원본과 Agent02·Agent08 원본을 실제로 읽고 두 원리를 수입했다. 모든 연구 연결은 E3 새 가설이며 신규성 미확정이다. 모델·뇌 자료 분석은 수행하지 않았다.

## 수입한 원리

### 02_affective_neuroscience

출처: `agents/02_affective_neuroscience/report.md` §1·3 U1/U2/U3·5 T1/T3·7

표상 차원의 존재와 내용환경 일반화는 다르며, 혼합 주석의 선형 결합과 새로운 관계 계산을 조합 유보로 구별한다.

원래 질문: 정서 범주/차원 및 시각 schema의 일반성과 맥락 의존성을 설명한다.

수정: AI의 OOD 점수 자체를 목표로 삼지 않고, 독립 주석으로 정한 신경 대비가 보존되는지를 핵심으로 변경한다. 구성 일반화는 자극·평가자 집계의 혼합을 먼저 분리한다.

### 08_systems_neuroscience

출처: `agents/08_systems_neuroscience/report.md` §3 L/D/N 경쟁·4 U2·8 A1/A2·11

분산 예측과 영역 간 상호작용을 구분하며, 긴 문맥의 효과는 HRF·자극 자기상관과 경쟁시켜야 한다.

원래 질문: 지역 제한·분산 가산·네트워크 상호작용 및 신경 통합시간의 설명력을 구별한다.

수정: V-JEPA의 긴 문맥 이득을 시간기전으로 곧바로 읽지 않고 동일 encoder 문맥 제한·FIR 기준을 둔다. 희소 feature의 공간적 분산을 신경회로라고 부르지 않고 안정된 subspace 수준의 대응으로 제한한다.

## C06-01 — 정서 관련 신경정보는 현재 장면의 복원보다 과거에서 추론한 예측 상태를 보존하는가

Axis: AS10, AS02, AS17, AS35

**연구 질문:** 현재 시각·의미 내용이 비슷한 사건에서, 과거만으로 계산한 잠재 예측 상태가 픽셀 복원정보와 긴 문맥 평균을 넘어 독립 정서 대비의 신경반응을 설명하는가?

**신경 타깃:** 사전 정의 감각 및 transmodal parcel의 자극별 BOLD 패턴과 독립 정서 주석 대비; 전체 BOLD 예측 증가와 정서 대비 설명을 별도 보고

**외부 원래 원리와 전이:** 원래 JEPA는 부분 관측에서 잠재 feature를, VideoMAE는 가려진 영상 내용을 복원한다. 이는 동일한 현재 관측에서도 과거에 따른 상태 구별과 외형 복원이 다른 정보라는 E3 전이 원리다.

**1차: 모델 적용:** V-JEPA 계열 prefix-only 입력의 상태·예측오차, VideoMAE 복원오차, 현재 프레임 표현을 추출하여 encoding 비교한다. 공개 checkpoint 간 비교는 방법 탐색이며 목표함수 원인성은 matched-backbone 소형 학습에서만 따로 시험한다.

**2차: 과학적 질문:** 정서 관련 신경 차이가 현재 내용 압축인지, 이력에 따른 다음 사건의 구별을 보존하는 상태인지 판별한다.

**3차: 기존 가정 도전:** 추상적 영상 특징의 우위가 곧 미래 기대나 신경 통합시간을 뜻한다는 가정을 시험한다. 부정적이면 현재 내용 또는 단순 시간 평활만으로 충분하다는 범위를 정한다.

**주가설:** 과거 정보량·용량·HRF를 맞춘 후에도 예측 상태가 현재 내용과 복원오차보다 정서 대비를 더 설명하며, 이는 독립 사건에서 재현된다.

**경쟁 설명:** 긴 문맥 semantics, motion, 사건경계, HRF 또는 특징 차원수가 이득을 모두 설명한다. 양방향 masking의 미래 누출이 apparent prediction을 만든다.

**측정 대비:** 외부 자극 유보에서 ΔR²=현재+FIR+motion+의미+복원정보+예측상태 모형 minus 예측상태를 뺀 모형. 독립 주석 대비의 예측 오차 차이를 주지표로 함께 설정. 입력 미래 포함 여부와 문맥 길이×parcel 효과는 별도 검증한다.

**반증:** 미래 누출 제거 또는 FIR·긴 의미 기준 추가 후 ΔR²의 실질적 이득이 사라지거나 정서 대비에서는 재현되지 않으면 예측 상태의 정서 관련 우위 기각. 낮은 신뢰도로 구별 불가능하면 보류.

**기준모형:** 현재 프레임 encoder와 시간 평균 / 같은 encoder의 짧은/긴 문맥 / FIR와 저차원 자기회귀 / motion·scene/object·사건경계 / 동일 유효차원·정규화의 복원표현

**데이터 계획:** Horikawa 우선으로 시행별 상태 요약의 조건부 encoding을 설계한다. trial 평균만 있으면 시간 방향은 주장하지 않는다. Emo-FilM·Spacetop은 연속 BOLD/자극 timecode·주석이 확인될 때 시간 검증. 동일 현재/다른 과거 조작의 인간 효과는 새 측정 단계다.

**미확인 조건:** 연속 BOLD와 HRF 모델에 충분한 run 길이 여부 / prefix-only feature 추출 구현 및 미래 token 접근 감사 / 자극 timing·motion·독립 정서 주석 정렬 / 모델 학습데이터·구조가 다른 비교의 식별 한계

**원문 문제와 새 질문의 차이:** 영상모델 적용 자체가 아니라 현재 내용·복원·과거 상태를 분리하고 독립 정서 대비에서 필요한 정보를 규정하는 실험적 대립이다.

**신규성 위험:** Kragel2019의 recurrent feedback 및 기존 시간적 encoding과 중복 가능. 최근 원문 역검색 미실행으로 신규성 미확정.

**판정:** E3 조건부 발전; 시계열·신규성·목표함수 식별 미확인

**개념 서명:** {"관측대상": "과거 제한 예측표현과 정서 대비 BOLD", "조작": "입력 문맥·미래 가림·목표함수", "경쟁설명": "상태 추론 vs 현재복원·평활·HRF"}

**여덟 탐색 질문**

1. 이미 관련 시간적 encoding이 있어 미시도는 확정 못 한다. 과거 제한과 동일 내용 대조를 동시에 갖추기 어려웠다.
2. 공개 V-JEPA/VideoMAE 구현으로 잠재 상태·복원정보를 같은 자극에 계산할 수 있다.
3. 영상표현의 높은 예측력=미래 기대라는 가정이 틀릴 수 있다.
4. AI는 고차원 영상 이력을 계산 가능한 상태로 압축한다. 뇌 baseline 우월성은 아직 실측하지 않았다.
5. 반복 가능한 정서 대비가 모든 모델 상태에 남으면 누락 계산 후보지만 HRF·잡음도 대안이다.
6. 부분 관측 상태식별을 정서 관련 신경표상의 충분 정보 시험으로 옮긴다.
7. 기존 짧은 영상은 상태 요약 비교에, 연속 자료는 시간 창 비교에 재사용한다.
8. 현재 내용으로 충분한지 이력 상태가 필요한지 결정하면 신경표상의 기능 설명이 달라진다. 단순 모델 순위는 불충분하다.

**기존 canonical 근거**

- [P046: Revisiting Feature Prediction for Learning Visual Representations from Video](https://arxiv.org/abs/2404.08471) — 본문: 아니요: 논문 본문 미확인; 공식 README 확인; Discussion: 아니요: 저자 Discussion 및 미래 제안 미확인; 근거: E1-공식 README/코드 한정; 논문 본문 E0; 전이 주장 E3
- [P045: VideoMAE: Masked Autoencoders are Data-Efficient Learners for Self-Supervised Video Pre-Training](https://arxiv.org/abs/2203.12602) — 본문: 아니요: 논문 본문 미확인; 공식 README 확인; Discussion: 아니요: 저자 Discussion 및 미래 제안 미확인; 근거: E1-공식 README/코드 한정; 논문 본문 E0; 전이 주장 E3
- [P013: V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning](https://raw.githubusercontent.com/facebookresearch/vjepa2/main/README.md) — 본문: 논문 원문 미열람; 공식 코드/데이터 문서 직접 확인; Discussion: 아니오; 근거: E1
- [P008: Emotion schemas are embedded in the human visual system](https://raw.githubusercontent.com/canlab/Neuroimaging_Pattern_Masks/master/Multivariate_signature_patterns/2019_Kragel_Emotion_Schemas/Kragel_2019_SciAdv_emotion_schemas.pdf) — 본문: 공식 연구실 PDF 다운로드; 초록과 지정 본문/Discussion/Limitations 직접 검토; Discussion: 예: 지정 페이지 직접 검토; 근거: E1
- [P066: Discovering event structure in continuous narrative perception and memory](https://github.com/brainiak/brainiak/blob/master/src/brainiak/eventseg/event.py) — 본문: 아니오; 공식 문서/코드만 확인; Discussion: 아니오; 근거: E1-공식 코드 및 tutorial; 논문 본문·Discussion 미확인

가장 가까운 선행근거: P008, P046, P066

## C06-02 — 제거해도 되는 환경과 보존해야 하는 맥락의 선택적 불변성 경계

Axis: AS12, AS01, AS13, AS29

**연구 질문:** 동일한 적응 예산에서 촬영 양식 정보 억제와 사건 맥락 정보 억제가 정서 관련 신경 대비에 서로 다른 손실을 만드는가?

**신경 타깃:** 사전 정의 자극환경을 넘는 정서 주석 관련 BOLD 패턴의 일반화; 맥락별 신경 대비의 조건부 안정성

**외부 원래 원리와 전이:** IRM의 환경별 predictor 안정성과 FINO의 metadata 보존/억제는 원래 도메인 적응 문제다. 이를 어떤 불변성을 강제할 때 신경 정보가 소실되는지 밝히는 대칭 조작으로 전환한다.

**1차: 모델 적용:** 동일 backbone에 nuisance 보존/억제, context 보존/억제, sham guide를 적용한다. 환경은 뇌와 정서 타깃을 보지 않고 외부 자극 metadata로 정한다.

**2차: 과학적 질문:** 정서 관련 뇌표상이 모든 환경에 불변인지, 상태를 정하는 맥락에 선택적으로 의존하는지 판별한다.

**3차: 기존 가정 도전:** 시각·환경 정보 제거가 항상 더 일반적인 정서 코드를 남긴다는 가정을 뒤집는다. 맥락 억제에도 보존되면 맥락 필수 가설을 축소한다.

**주가설:** 사전 정의 촬영 nuisance 억제는 외부 환경 일반화를 유지/개선하지만 사건 맥락 억제는 동일 정서 라벨 내 신경 대비를 선택적으로 줄인다.

**경쟁 설명:** guide 간 학습 난도·신호량·라벨 상관이 다르기 때문에 생기는 손실이며, 정서 관련 맥락의 선택적 필요성과 무관하다.

**측정 대비:** guide 종류×보존/억제의 2×2 interaction을 독립 자극의 신경 대비 예측손실로 측정한다. probe 정확도·표현 rank·reconstruction·guide 정보량을 맞춘 뒤 비교한다.

**반증:** 정보 제거량·성능·환경별 표본 수를 맞추면 interaction이 사라지거나 sham guide도 동일 손실을 만들면 선택적 불변성 주장 기각.

**기준모형:** frozen backbone / ERM / 외부환경 유보 IRM / guide label permutation / 동일 rank 무작위 정보 제거 / 의미 특징을 포함/제외한 민감도 분석

**데이터 계획:** Horikawa의 실제 자극 목록과 정서 주석을 확인한 뒤 내용×환경 교차가 있는 하위군을 선정한다. NSD는 촬영/시각 정보 보존의 음성 대조이며 정서 정답이 있다고 가정하지 않는다. 다른 보유 자료로의 전이는 ontology 확인 후 수행한다.

**미확인 조건:** 독립적으로 정의할 촬영 양식·사건 맥락 metadata / 정서 주석과 환경의 충분한 교차 및 공통 지지집합 / FINO checkpoint/guide 경로 확인 / nuisance 명칭이 실제 무관성을 보장하지 않음

**원문 문제와 새 질문의 차이:** 일반화 점수의 최대화 대신 제거 가능한 환경과 유지되어야 하는 맥락의 비대칭 신경 손실을 설명 대상으로 삼는다.

**신규성 위험:** 기존 domain-general representation 및 context-dependent affect와 중복 가능. 명확한 2×2 신경 대비가 없으면 단순 adaptation benchmark로 격하.

**판정:** E3 조건부 발전; metadata 교차·신규성 미확인

**개념 서명:** {"관측대상": "환경 간 정서 신경 대비", "조작": "서로 다른 metadata의 보존/억제", "경쟁설명": "선택적 맥락 의존 vs 일반 정보손실"}

**여덟 탐색 질문**

1. 미시도는 미확인이다. nuisance와 필수 맥락의 경계를 선험적으로 정하기 어렵고 라벨 교차가 부족했다.
2. metadata guide를 보존·억제하는 공식 구현이 대칭 비교를 가능하게 한다.
3. 환경 정보를 지울수록 정서 표상에 가까워진다는 가정이 틀릴 수 있다.
4. AI는 같은 backbone의 정보 보존 압력을 조절할 수 있어 인간 자료에서 직접 할 수 없는 표상 비교를 제공한다.
5. AI가 제거한 맥락을 뇌가 계속 구별하는지가 질문이며, 존재한다고 전제하지 않는다.
6. 위성영상 metadata 적응과 불변학습을 정서 코드의 맥락 의존성 시험으로 전이한다.
7. 보유 영상의 환경별 하위군을 기존 정서 분류와 다른 일반화 단위로 재사용한다.
8. 어떤 정보가 없어도 되는지를 밝혀 신경표상에서 추상화의 경계를 규정한다. 모든 결과는 관찰적 신경 대응이다.

**기존 canonical 근거**

- [P049: Invariant Risk Minimization](https://arxiv.org/abs/1907.02893) — 본문: 아니요: 논문 본문 미확인; 공식 README 확인; 구현 코드 일부 확인; Discussion: 아니요: 저자 Discussion 및 미래 제안 미확인; 근거: E1-공식 README/코드 한정; 논문 본문 E0; 전이 주장 E3
- [P050: Who Needs Labels? Adapting Vision Foundation Models With the Metadata You Already Have](https://arxiv.org/abs/2606.05107) — 본문: 아니요: 논문 본문 미확인; 공식 README 확인; Discussion: 아니요: 저자 Discussion 및 미래 제안 미확인; 근거: E1-공식 README/코드 한정; 논문 본문 E0; 전이 주장 E3
- [P001: The neural representation of visually evoked emotion is high-dimensional, categorical, and distributed across transmodal brain regions](https://raw.githubusercontent.com/OpenNeuroDatasets/ds002425/3f94b2bf9a75ddb62637c529d30dc40dd4ab5ba1/dataset_description.json) — 본문: 아니오; 프록시 403; Discussion: 아니오; 근거: E2
- [P007: Generalizable representations of pain, cognitive control, and negative emotion in medial frontal cortex](https://raw.githubusercontent.com/canlab/Neuroimaging_Pattern_Masks/master/Multivariate_signature_patterns/2018_Kragel_MFC_Generalizability/Kragel_2018_NatNeurosci_MFC_generalizability.pdf) — 본문: 공식 연구실 PDF 다운로드; 초록과 지정 본문/Discussion/Limitations 직접 검토; Discussion: 예: 지정 페이지 직접 검토; 근거: E1

가장 가까운 선행근거: P049, P050, P007

## C06-03 — 해석 가능한 개념은 신경 정렬 방향인가 모델 계산에 쓰이는 안정된 성분인가

Axis: AS11, AS15, AS24, AS16

**연구 질문:** 정서 관련 BOLD와 정렬된 희소/개념 성분은 분해 seed를 넘어 안정적이며 모델의 후속 상태 예측에 필요한가, 아니면 임의 basis에서 읽어낸 방향인가?

**신경 타깃:** 정서 주석 대비에 연결되는 parcel별 encoding 성분과 SAE/개념 분해의 잔차가 설명하는 신경정보

**외부 원래 원리와 전이:** SAE는 활성 재구성의 희소 basis를, transcoder는 계산 대체를, concept bottleneck은 개념 경유 예측을 제공한다. 해석 가능한 이름·정보 readout·계산 사용은 서로 다른 검증 대상이다.

**1차: 모델 적용:** 동일 영상 encoder에 여러 seed/width SAE와 PCA·random sparse basis를 맞춘다. 안정된 feature 또는 subspace, 재구성 잔차, 모델 내 ablation 효과를 독립 자료에서 교차 평가한다. DOC-SAE 구현의 비디오 호환은 검증 과제다.

**2차: 과학적 질문:** 정서 관련 모델–뇌 대응이 개별 개념 단위에 있는지, 여러 분해에 공통인 분산 subspace에 있는지 구별한다.

**3차: 기존 가정 도전:** 이름 붙이기 쉬운 feature가 신경 계산 단위이며 높은 decoding이 실제 모델 내 사용을 뜻한다는 가정을 시험한다. 개별 feature가 실패해도 안정된 subspace라는 대안을 남긴다.

**주가설:** 반복 분해에서 대응되는 subspace는 신경 정렬과 모델 예측 기여를 모두 보이지만 개별 feature의 의미 이름은 덜 안정적일 수 있다.

**경쟁 설명:** 신경 정렬은 단순 dense 표현 readout이며 sparse basis의 안정성·ablation 효과는 재구성 품질·에너지 제거량·분해 선택으로 설명된다.

**측정 대비:** feature/subspace 재현도 × 독립 신경 ΔR² × 모델 내 예측 변화의 세 지표를 별도 계산한다. 선택은 train fold에 한정하며 동일 에너지/재구성 손실의 무작위 ablation과 비교. SAE 잔차가 독립 신경 대비를 설명하는지도 평가한다.

**반증:** 안정 성분의 신경 기여가 random/PCA 기준과 구별되지 않거나 동일 손상량 ablation에서 사용 효과가 사라지면 계산적 개념 주장 기각. 잔차가 주요 신경정보를 담으면 개념 분해의 충분성 기각.

**기준모형:** dense 원표현 / matched-rank PCA / 무작위 희소 dictionary / matched-reconstruction SAE / 동일 에너지 random ablation / 분해 재구성 잔차 encoding

**데이터 계획:** Horikawa를 우선하여 시행별 신경 대비와 정렬한다. NSD는 정서 주석을 가정하지 않는 일반 시각 성분 안정성 대조다. Mind Captioning은 정확한 데이터 식별자·caption 및 신경 정렬 단위를 확인한 경우에만 언어 개념 대조로 사용한다.

**미확인 조건:** 선택 backbone activation 추출 및 SAE 호환성 / 개념 이름과 독립 인간 주석의 구별 / seed/width 간 component alignment는 train 자료에서 수행 / 모델 feature intervention은 인간 뇌 인과 증거가 아님

**원문 문제와 새 질문의 차이:** 희소 특징을 뇌지도에 붙이는 것에서 벗어나 분해의 비유일성·계산 사용·신경 대비·잔차의 충분성을 동시에 반박 가능한 기준으로 나눈다.

**신규성 위험:** 기존 SAE 안정성·concept completeness와 brain alignment 조합의 중복 가능. DOC 출처는 코드/README 근거이며 해당 논문 본문이나 실증을 확인했다는 의미가 아니다.

**판정:** E3 조건부 발전; SAE는 DOC 근거, 개별 신경회로·인과 주장 금지

**개념 서명:** {"관측대상": "개념 feature·공통 subspace·재구성 잔차의 신경 대응", "조작": "분해 seed/width 및 모델 내부 제거", "경쟁설명": "안정 계산 성분 vs 임의 basis readout"}

**여덟 탐색 질문**

1. 기존 해석 연구는 있으나 신경표상과 동일한 feature 단위를 대응시키는 식별성이 어렵다. 미시도는 확정 못 한다.
2. 공개 SAE·transcoder·circuit 도구가 activation 분해와 모델 내 기능 검사를 분리해 제공한다.
3. 해석 가능한 개념=안정된 신경 계산 단위라는 가정이 틀릴 수 있다.
4. AI는 계산 내부 성분 제거와 오류 잔차의 명시가 가능하며 이를 BOLD의 인과 조작과 동일시하지 않는다.
5. 희소 분해가 설명 못 한 반복 가능한 신경 대비는 개념 불완전성 후보지만 노이즈·부적합과 경쟁한다.
6. mechanistic interpretability의 error node 원리를 encoding 잔차 감사로 가져온다.
7. 기존 brain encoding 자료를 개념 분해의 충분성과 비유일성 평가에 재사용한다.
8. 개별 개념인지 분산 subspace인지 구별하면 신경 정렬의 해석 단위가 바뀐다. feature 이름 나열만으로 끝내지 않는다.

**기존 canonical 근거**

- [P083: Concept Bottleneck Models](https://raw.githubusercontent.com/mlresearch/v119/gh-pages/koh20a/koh20a.pdf) — 본문: PDF 접근; 첫 페이지·§8 Discussion PDF9쪽 직접검토; Discussion: §8 Discussion PDF9쪽 직접확인; 근거: E1(선택 본문); 전이 E3
- [P007: Generalizable representations of pain, cognitive control, and negative emotion in medial frontal cortex](https://raw.githubusercontent.com/canlab/Neuroimaging_Pattern_Masks/master/Multivariate_signature_patterns/2018_Kragel_MFC_Generalizability/Kragel_2018_NatNeurosci_MFC_generalizability.pdf) — 본문: 공식 연구실 PDF 다운로드; 초록과 지정 본문/Discussion/Limitations 직접 검토; Discussion: 예: 지정 페이지 직접 검토; 근거: E1
- [P009: Common and stimulus-type-specific brain representations of negative affect](https://raw.githubusercontent.com/canlab/Neuroimaging_Pattern_Masks/master/Multivariate_signature_patterns/2021_Ceko_MPA2_multiaversive/Ceko_2022_NatNeurosci_MPA2_negative_affect.pdf) — 본문: 공식 연구실 PDF 다운로드; 초록과 지정 본문/Discussion/Limitations 직접 검토; Discussion: 예: 지정 페이지 직접 검토; 근거: E1
- [DOC-SAE: OpenAI sparse_autoencoder 공식 코드](https://github.com/openai/sparse_autoencoder) — agents/06_frontier_ai/report.md §공식 도구; 본문 확인과 구분
- [DOC-TRANSCODER: transcoder_circuits 공식 코드](https://github.com/jacobdunefsky/transcoder_circuits) — agents/06_frontier_ai/report.md §공식 도구; 본문 확인과 구분
- [DOC-CIRCUIT: circuit-tracer 공식 코드](https://github.com/safety-research/circuit-tracer) — agents/06_frontier_ai/report.md §공식 도구; 본문 확인과 구분

가장 가까운 선행근거: P083, DOC-SAE, DOC-TRANSCODER

## C06-04 — 분포 밖 적응의 성공이 정서 관련 신경정보의 보존을 보장하는가

Axis: AS07, AS13, AS28, AS30

**연구 질문:** 외부 환경에서 일반 시각 과제 성능을 높이는 적응이 독립 정서 대비의 신경정보를 보존하는지, 일부 적응 경로에서는 체계적으로 지우는지 시험할 수 있는가?

**신경 타깃:** 적응 전후 표현이 설명하는 동일 자극의 신뢰 가능한 정서 대비 BOLD 및 감각/의미 대비 BOLD의 차이

**외부 원래 원리와 전이:** 도메인 적응은 target 환경의 과제 위험을 줄이는 것이 원목표다. 여기서는 같은 과제 성능을 가진 적응 경로들의 신경정보 보존 차이를 다목적 정보 손실 문제로 전환한다.

**1차: 모델 적용:** frozen backbone과 metadata 기반 적응을 여러 강도에서 비교한다. 비정서 OOD 성능으로만 선택한 모델의 신경 alignment를 후속 독립 평가한다. 실제 test-time 적응 API·검증 문헌이 없으면 사전 정의 비지도 target 적응으로 제한한다.

**2차: 과학적 질문:** 일반 과제에 충분한 표상이 정서 관련 신경 계산에도 충분한지, 과제 성공이 제거해도 된다고 판단한 정보에 신경 코드가 있는지 구별한다.

**3차: 기존 가정 도전:** 더 강건한 시각 모델이 더 좋은 뇌 모델이라는 가정을 반박한다. 보존되면 관측 범위에서 적응과 신경정보가 양립함을 배운다.

**주가설:** 일부 적응 강도에서 비정서 OOD 성능은 증가하지만 정서 대비 BOLD의 조건부 예측은 감소하며 일반 시각 BOLD 감소만으로 설명되지 않는다.

**경쟁 설명:** 측정된 하락은 전체 표현 손상, target leakage, 과제 성능의 측정오차 또는 neural readout 재학습 부족 때문이다.

**측정 대비:** ΔOOD 과제성능 대 Δ정서 신경 대비 예측의 joint confidence region과 adaptation strength 곡선을 계산한다. 두 신경 대비의 변화 차이로 선택적 손실을 시험하고, frozen/readapted 동일 용량 readout을 모두 비교한다.

**반증:** 독립 test 환경에서 OOD 이득이 재현되지 않거나 neural readout 재적합·전체 시각 손실 통제로 정서 대비 손실이 사라지면 선택적 손실 가설 기각.

**기준모형:** frozen encoder / ERM 및 동일 예산 fine-tuning / target label을 쓰지 않는 model selection / sham adaptation / frozen/retrained linear readout / general visual neural contrast

**데이터 계획:** Horikawa를 신경 대비 주 자료로 사용하되 적응은 독립 자극/metadata로 수행한다. NSD는 일반 시각 신경정보 보존 대조로 조건부 사용. Emo-FilM·Spacetop 간 전이는 자극 modality/주석 ontology 확인 후 별도 domain으로 취급한다.

**미확인 조건:** 독립 비정서 과제 및 domain 정의 / 적응·validation·test 자극과 neural 평가의 엄격한 분리 / 동일 자극 neural 비교 또는 정당화된 공통 feature 공간 / 소수 domain에서 효과 일반화 불확실성

**원문 문제와 새 질문의 차이:** C06-02가 특정 맥락의 기능을 guide 조작으로 묻는 데 비해, 이 후보는 동일 외부 과제 성공 뒤의 적응 경로·강도에 따른 신경정보 손실을 묻는다. 실험에서 두 대비가 분리되지 않으면 후보를 병합한다.

**신규성 위험:** robustness–brain alignment 및 adaptation forgetting 연구와 중복 가능. 일반 feature forgetting을 정서로 이름 바꾼 수준이면 기각; 최신 역검색 미완료.

**판정:** E3 조건부 발전; C06-02와 대비가 중복되면 병합; test-time 방법 미검증

**개념 서명:** {"관측대상": "적응 전후 정서/시각 신경정보 보존 곡선", "조작": "정서 타깃을 보지 않는 적응 경로·강도", "경쟁설명": "과제 충분성의 한계 vs 전반적 손상·readout 변화"}

**여덟 탐색 질문**

1. 관련 강건성 연구는 존재하므로 미시도 확정 불가. 독립 적응 성능과 신경 대비를 함께 추적하는 평가 비용이 컸다.
2. foundation model의 metadata 적응과 명시적 OOD 평가 도구가 정보 소실 궤적을 비교하게 한다.
3. OOD 성능 향상=신경 설명력 향상이라는 가정이 틀릴 수 있다.
4. AI는 여러 적응 경로에서 같은 과제 성공에 도달하는 표상들을 제공해 충분성의 대안을 만든다.
5. AI 과제가 버려도 되는 정보가 뇌의 정서 대비에는 남는지 시험한다. 잔여의 존재는 아직 가설이다.
6. domain adaptation의 model selection과 forgetting 측정을 신경정보 보존 감사로 전이한다.
7. 기존 fMRI를 모델 적응의 독립 평가계로 재사용하며 target neural score로 적응을 선택하지 않는다.
8. 적응에 의한 정서정보 손실이 있으면 AI 과제에 충분한 정보와 신경 계산에 필요한 정보의 경계가 드러난다.

**기존 canonical 근거**

- [P050: Who Needs Labels? Adapting Vision Foundation Models With the Metadata You Already Have](https://arxiv.org/abs/2606.05107) — 본문: 아니요: 논문 본문 미확인; 공식 README 확인; Discussion: 아니요: 저자 Discussion 및 미래 제안 미확인; 근거: E1-공식 README/코드 한정; 논문 본문 E0; 전이 주장 E3
- [P098: WILDS: A Benchmark of in-the-Wild Distribution Shifts](https://proceedings.mlr.press/v139/koh21a.html) — 본문: 예: PDF 저장; 검토 절은 source_location 참조; Discussion: 예: §7 PDF p.9; 근거: E1
- [P099: In Search of Lost Domain Generalization](https://github.com/facebookresearch/DomainBed) — 본문: 아니오; Discussion: 아니오; 근거: E1
- [P001: The neural representation of visually evoked emotion is high-dimensional, categorical, and distributed across transmodal brain regions](https://raw.githubusercontent.com/OpenNeuroDatasets/ds002425/3f94b2bf9a75ddb62637c529d30dc40dd4ab5ba1/dataset_description.json) — 본문: 아니오; 프록시 403; Discussion: 아니오; 근거: E2

가장 가까운 선행근거: P050, P098, P099

## C06-05 — 보지 않은 내용–정서 조합에서 신경표상은 성분의 합으로 구성되는가

Axis: AS01, AS03, AS16, AS24, AS31

**연구 질문:** 단일 성분과 관측한 내용–정서 조합에서 학습한 모델이 보지 않은 조합의 뇌반응을 가산적으로 예측하는가, 아니면 새로운 관계 항이 필요한가?

**신경 타깃:** 독립 조합 자극에 대한 정서 관련 BOLD 패턴; 영역 내 비선형과 영역 간 통계적 상호작용은 별도 계층으로 비교

**외부 원래 원리와 전이:** compositional generalization은 관측한 원자 성분의 새로운 조합을 예측하는 문제다. concept bottleneck의 성분 경유 설명을 완전하다고 가정하지 않고 관계 연산의 필요성을 시험한다.

**1차: 모델 적용:** 검증된 내용·정서 주석 성분으로 additive concept model, within-component nonlinear model, low-rank interaction model을 만든다. unseen-combination split에서 동일 유효복잡도와 noisy-label 모델을 비교한다.

**2차: 과학적 질문:** 고차원 정서 관련 신경표상이 재사용 가능한 성분의 조합인지, 맥락에 따라 만들어지는 새로운 결합 코드인지 구별한다.

**3차: 기존 가정 도전:** 여러 범주의 높은 주석값이 독립 신경 성분의 단순 합을 뜻한다는 가정을 시험한다. 단순 합이 충분하면 복잡한 상호작용을 요구하는 설명을 축소한다.

**주가설:** 개별 성분을 충분히 학습했음에도 특정 새 조합에서는 관계 항이 독립 신경 대비를 추가 설명하며, 이 이득은 일반 의미 비선형성과 주석 불확실성만으로 설명되지 않는다.

**경쟁 설명:** 가산 성분과 강한 within-component nonlinear 기준으로 충분하다. 조합 이득은 희귀 자극·내용 OOD·평가자 집계 혼합·모형용량의 산물이다.

**측정 대비:** 각 성분은 train에서 관측하되 조합만 test로 유보한다. additive→within-component nonlinear→cross-component interaction의 nested held-out ΔR²를 비교. 성분 빈도와 시각/의미 거리를 맞춘 split을 별도 둔다.

**반증:** 새 조합에서 관계 항의 고유 이득이 없거나 평가자 혼합/내용거리·capacity 통제로 사라지면 결합 신경 코드 가설 기각. 조합의 지지집합이 부족하면 검증 불가로 보류.

**기준모형:** 성분 가산 모형 / 같은 복잡도의 성분 내부 비선형 / dense vision/semantic encoding / 빈도·거리 일치 조합 유보 / 주석 측정오차 모형 / 지역 제한/분산 가산/통계 상호작용의 분리

**데이터 계획:** Horikawa의 실제 다범주 주석 행렬과 stimulus ID로 조합 빈도·평가 단위를 감사한 뒤 설계한다. 개인 평정이 없으면 집계 수준의 복합 주석이라고만 명명한다. Mind Captioning은 데이터 식별·주석 구조가 확인된 경우 내용 성분 대조; NSD는 내용 조합 대조로만 사용한다.

**미확인 조건:** 충분한 조합 수와 성분별 관측 범위 / 주석이 개별 평가인지 집계인지 확인 / 고정 조합 ontology와 독립 train/test split / 관측 fMRI interaction을 신경 인과 coupling으로 읽지 않을 것

**원문 문제와 새 질문의 차이:** 범주 수나 비선형 정확도를 비교하는 대신 성분은 관측했지만 관계는 보지 못한 평가에서 재사용 가능한 신경 연산의 충분성을 판별한다.

**신규성 위험:** Agent02 U2와 직접 겹치는 문제를 AI 조합 유보/성분 내부 비선형 통제로 구체화한 공동 후보이며 독립 원안으로 이중 집계하지 않는다. compositional emotion 연구 역검색은 남아 있다.

**판정:** E3 공동 후보; Agent02 U2와 통합 필요; 조합 지지집합 조건부

**개념 서명:** {"관측대상": "보지 않은 내용–정서 조합의 신경반응", "조작": "원자 성분 관측을 보존한 조합 유보", "경쟁설명": "가산 재사용 vs 새로운 관계 연산·집계 혼합"}

**여덟 탐색 질문**

1. 조합 일반화와 혼합 정서 연구는 이미 있어 미시도는 확정 못 한다. 성분 관측을 보존한 충분한 새 조합이 드물다.
2. 개념 기반 모델과 공개 고차원 표상으로 가산·관계 연산을 동일 용량에서 비교할 수 있다.
3. 혼합 주석=독립 신경 성분의 합이라는 가정이 틀릴 수 있다.
4. AI는 고차원 성분 조합을 명시적으로 예측하고 관계 항의 필요성을 비교할 수 있다.
5. 새 조합에서만 나타나는 재현 가능한 신경 대비가 AI의 성분 사전에 없을 수 있으나 측정오차와 경쟁해야 한다.
6. 구성 일반화와 개념 불완전성 검사를 신경표상의 성분 재사용 문제로 전이한다.
7. 기존 영상 주석 행렬을 조합 유보 설계로 재사용하며 없는 개인 평정이나 혼합 경험을 만들어내지 않는다.
8. 가산 성분과 관계 계산을 구별하면 정서 코드의 구성 원리를 바꾼다. 정확도가 조금 오르는 것만으로는 충분하지 않다.

**기존 canonical 근거**

- [P001: The neural representation of visually evoked emotion is high-dimensional, categorical, and distributed across transmodal brain regions](https://raw.githubusercontent.com/OpenNeuroDatasets/ds002425/3f94b2bf9a75ddb62637c529d30dc40dd4ab5ba1/dataset_description.json) — 본문: 아니오; 프록시 403; Discussion: 아니오; 근거: E2
- [P008: Emotion schemas are embedded in the human visual system](https://raw.githubusercontent.com/canlab/Neuroimaging_Pattern_Masks/master/Multivariate_signature_patterns/2019_Kragel_Emotion_Schemas/Kragel_2019_SciAdv_emotion_schemas.pdf) — 본문: 공식 연구실 PDF 다운로드; 초록과 지정 본문/Discussion/Limitations 직접 검토; Discussion: 예: 지정 페이지 직접 검토; 근거: E1
- [P009: Common and stimulus-type-specific brain representations of negative affect](https://raw.githubusercontent.com/canlab/Neuroimaging_Pattern_Masks/master/Multivariate_signature_patterns/2021_Ceko_MPA2_multiaversive/Ceko_2022_NatNeurosci_MPA2_negative_affect.pdf) — 본문: 공식 연구실 PDF 다운로드; 초록과 지정 본문/Discussion/Limitations 직접 검토; Discussion: 예: 지정 페이지 직접 검토; 근거: E1
- [P083: Concept Bottleneck Models](https://raw.githubusercontent.com/mlresearch/v119/gh-pages/koh20a/koh20a.pdf) — 본문: PDF 접근; 첫 페이지·§8 Discussion PDF9쪽 직접검토; Discussion: §8 Discussion PDF9쪽 직접확인; 근거: E1(선택 본문); 전이 E3

가장 가까운 선행근거: P001, P008, P083

## 수행 범위와 남은 일

- 이번 Round2는 지정된 실제 보고서 교차 열람과 후보 재구성이다. Round3의 상대 비판·Round4 응답·Round5 토론 완료를 주장하지 않는다.
- 기존 논문·공식 문서의 검증 상태를 승계했다. 이번에 새 원문 다운로드·Discussion 검증·외부 신규성 검색·뇌 분석·모델 실행을 하지 않았다.
- DOC-SAE/DOC-TRANSCODER/DOC-CIRCUIT은 공식 코드 문서 근거로 논문 본문 검증 수에 포함하지 않는다. P013/P046/P050 등도 canonical ID가 곧 본문 확인을 의미하지 않는다.
- 5종 데이터 보유는 사용자 진술로 인정하지만 현재 환경 접근·버전·필드 검증은 별도다. Mind Captioning의 정확한 식별자를 이름으로 추정하지 않았다.
- 전체 BOLD 예측·독립 정서 대비·모델 내 인과적 기여·인간 신경 인과성은 다른 주장이다. 모든 후보는 관찰 신경 대응 또는 향후 통제 측정 계획이다.
- 정서–의미 공통분산을 모두 제거해 순수 정서를 얻었다고 하지 않는다. 공통/고유 분산과 조건화 집합 민감도를 함께 보고해야 한다.
- 후보 5개는 원리별 구분이지만 C06-02/04는 최종 대비가 중복되면 병합하고 C06-05는 Agent02 U2 공동 발전으로 중복 집계를 막는다.
- 모든 분석은 자극 identity/중복·run·participant 의존성을 보존하는 외부 평가, inner-fold feature/ROI/lag 선택, 주석 신뢰도와 noise ceiling을 전제로 한다. 검정력 부족은 가설 반증과 구분한다.
