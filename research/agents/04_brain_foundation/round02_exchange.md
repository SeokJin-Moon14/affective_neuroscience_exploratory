# Agent04 Round2 실제 정보 교환

2026-11-12 · 작성: foundation_continuation · 원본 두 분야 보고서 열람 기반. 원자료 분석과 모델 실행은 하지 않았다.

## 수입 원리

- **07_geometry_information**: 표현 정렬·압축의 불변성과 정보 보존을 분리하고, 반복 신뢰도로 잡음 제거와 신호 소실을 구별한다.
  원래 문제: 신경망 표현 유사도, 비지도 잠재요인의 식별성과 기하 재현성을 평가한다. 새 질문: 정서 주석과 연결되는 재현 가능한 뇌정보가 사전학습 목적·공간집계·개인 평균에 따라 선택적으로 사라지는가?
  수정: 정렬값이나 고정 선형 probe의 실패만으로 완전한 정보 소실을 주장하지 않고, 유연한 probe·독립 반복·차원 일치 대조를 추가했다.
- **10_llm_semantics**: 언어 특징은 의미의 불완전한 측정이며, 개념 병목을 우회한 의미 정보가 잔차에 남는지 독립 probe로 감사한다.
  원래 문제: 시각–언어 모듈 연결의 효율과 해석 가능한 개념 예측, 캡션의 정보 압축을 평가한다. 새 질문: 자극조건부 모형이 놓치고 뇌조건부 모형이 회수한 정서 관련 신호는 의미 누락인가, 검토한 자극 표현을 넘는 재현 정보인가?
  수정: 캡션·사건 개념군을 단계적으로 강화하고 정서 주석 관련 증분과 전체 뇌 예측을 분리한다. 과거 문맥의 실제 입력 이력도 고정한다.

## 공통 해석과 자료 조건

Y=신경반응, A=독립 정서 주석, V=저수준 시각·운동 특징, S=검수된 사건·의미 표현. A가 자극 집계이면 개인의 정서 측정으로 해석하지 않는다.
자극/영상/런을 묶어 외부 평가하고 반복 자극은 같은 분할로 둔다. 층·ROI·정규화·차원축소·잔차화·probe 선택은 훈련 fold 내부에서만 수행한다. 참가자와 자극의 의존성을 계층 bootstrap 또는 적절한 블록 검정에 반영한다.
정서 관련 정보는 지정한 V,S와 모델군을 넘어서는 A 관련 외부 예측량이다. 완전한 정서 고유 정보, 인과 성분 또는 신경 알고리즘으로 명명하지 않는다. 모델 간 차이를 곧 정보이론적 상호정보량 차이로 부르지 않는다.

Horikawa, Emo-FilM, Mind Captioning, NSD, Spacetop 보유는 최신 사용자 진술로 확인. 실제 로컬 경로·버전·스키마를 확인한 것은 아니다.

Emo-FilM은 연속 시계열·시간 정렬 확인 뒤 동적 전이; NSD는 정서 주석 확인 전 의미/공간 방법 대조만; Spacetop은 과제별 실제 주석 확인 뒤 일반화; Mind Captioning은 정확한 식별자·버전·주석 사전 확인 전 특정 실험에 배정하지 않는다.

## C04-01 — 사전학습 목표는 재현 가능한 정서 관련 신호를 선택적으로 압축하는가?

연결 축: AS07, AS13, AS24. 상태: 조건부 발전: E3 연구 가설; 분석·신규성 확정 전.

**연구 질문:** 같은 신경 입력·encoder·학습량에서 복원, 잠재예측, contrastive 목적은 전체 신호 복원과 독립 정서 주석 관련 정보 보존 사이에 서로 다른 교환관계를 만드는가?

**신경 표적:** 피질 시계열 또는 대응되는 자극 단위 신경 패턴의 반복 재현 성분과 독립 정서 주석 관련 대비

**수입 계산 원리:** Agent07의 정보 보존/좌표 불변성 구별 + Agent10의 의미 측정 오차 감사

**1단계 모델 적용·정확한 입출력:** CortexMAE는 fMRI→latent/복원, Brain-JEPA는 ROI 시계열→latent prediction, SwiFT는 4D fMRI→표현이다. 공개 모델 교차 비교는 탐색이고, 목표함수 효과의 확정 비교는 동일 encoder·입력으로 별도 학습한 소규모 목적함수 ablation이다.

**2단계 과학 질문:** 정서 관련 재현 성분이 전체 신경분산에 최적인 자기지도 표현에도 충분히 남는지 검사한다.

**3단계 가정 도전:** 좋은 범용 신경표현이 모든 과학적 표적에 충분하다는 가정을 시험한다. 단순 모델 성능순위는 질문을 해결하지 않는다.

**주가설:** 예측가능 공통구조를 강조한 목적은 큰 분산 설명을 유지하면서 일부 재현 가능한 A 관련 대비의 접근성을 낮춘다.

**경쟁 설명:** 효과는 목표함수보다 입력공간·학습 corpus·차원·readout 제약 또는 의미 누락으로 설명된다.

**관측 대비:** 같은 외부 자극에서 raw Y와 각 latent Z가 A를 예측하는 V,S 조건부 증분을 비교하고, 별도로 보류 Y 복원량을 측정한다. frozen linear probe와 훈련 fold에서 용량을 정한 nonlinear probe를 병행한다. 일차 대비는 전체 복원 보존과 A 관련 예측 감소의 목적함수×표적 교호작용이다.

**반증:** 동일 encoder·입력·예산 비교에서 차이가 없거나, raw Y에도 A 관련 신뢰가능 신호가 없거나, 유연한 probe/강화된 S로 감소가 해소되면 선택적 정보 소실 주장을 기각 또는 접근성 한계로 낮춘다.

**강한 기준:** raw ridge; 차원 일치 PCA와 random projection; 미학습 encoder; 동일 encoder의 MAE/latent-prediction/contrastive 목적 비교; 검수 사건 목록을 늘린 의미 기준

**자료 계획:** ownership: Horikawa, Emo-FilM, Mind Captioning, NSD, Spacetop 보유는 최신 사용자 진술로 확인. 실제 로컬 경로·버전·스키마를 확인한 것은 아니다. / primary: Horikawa 우선. 독립 정서 주석 A, 자극 ID, 신경 Y, 런/반복 구조를 확보한 분석 단위에서 시작한다. / fallback: 자극 단위 beta만 있으면 정적 대비만 수행하고 연속 BOLD 입력을 요구하는 모형에는 넣지 않는다. 주석이나 신뢰도 추정이 없으면 방법 검증으로 범위를 축소한다. / additional: Emo-FilM은 연속 시계열·시간 정렬 확인 뒤 동적 전이; NSD는 정서 주석 확인 전 의미/공간 방법 대조만; Spacetop은 과제별 실제 주석 확인 뒤 일반화; Mind Captioning은 정확한 식별자·버전·주석 사전 확인 전 특정 실험에 배정하지 않는다.

**분석 전 확인 조건:** 사전학습 corpus 중복; 목표별 동일 입력/예산을 구성할 코드; checkpoint별 실제 config와 load; A와 Y의 독립 신뢰도; 재현 가능한 반복 또는 대체 신뢰도 설계

**원문 문제와 새로운 질문의 차이:** 원문은 일반 표현 학습·비교가 목표다. 새 질문은 목적함수를 통제해 전체 신호와 독립 정서 대비의 선택적 손실을 분리하는 것이다.

**중복 위험:** 기존 representation probing의 정서 표적 교체와 중복할 수 있다. 동일 architecture ablation과 이중 표적 대비가 없으면 방법 benchmark로 낮춘다.

**구별되는 개념 서명:** 관측대상: 재현 신경성분의 A 관련 예측 접근성 / 조작: 동일 encoder의 사전학습 목적 / 경쟁설명: 목표함수 선택성 대 readout·공간·corpus 차이

**여덟 탐색 질문에 대한 답:**

1. 미시도 여부는 E0다. 서로 다른 목적의 모델은 보통 입력·corpus도 달라 원인 분리가 어려웠다.
2. 공개 fMRI MAE·JEPA·contrastive 구현으로 목적의 통제 비교를 설계할 수 있다.
3. 범용 성능이 표적별 정보 보존을 보장한다는 가정.
4. 분산 시공간 상관과 예측가능 공통구조를 재사용할 수 있다.
5. 작지만 반복되는 A 관련 대비가 압축될 가능성은 E3이며 먼저 raw 신호의 신뢰도를 확인한다.
6. 표현 유사도의 불변성과 개념 우회 감사가 단순 probe 해석을 제한한다.
7. 기존 정서 자료를 분류 성능 대신 학습 목적에 따른 신호 보존 시험에 사용한다.
8. 선택적 소실이면 범용 모델 평가 기준을 바꾸고, 차이가 없으면 정보 결핍보다 측정/읽기 한계를 좁힌다.

**근거:** [P025](https://github.com/Transconnectome/SwiFT), [P026](https://github.com/MedARC-AI/CortexMAE), [P029](https://github.com/Eric-LRL/Brain-JEPA), [P051](https://proceedings.mlr.press/v97/kornblith19a.html), [P083](https://raw.githubusercontent.com/mlresearch/v119/gh-pages/koh20a/koh20a.pdf). 가까운 선행: P026, P029, P051.


## C04-02 — 자극조건부와 신경조건부 모형의 불일치는 의미 누락을 넘는가?

연결 축: AS08, AS24, AS29. 상태: 조건부 발전: E3 연구 가설; 분석·신규성 확정 전.

**연구 질문:** 자극→뇌 모형이 설명하지 못하지만 관측 뇌의 다른 블록이 예측하는 신호 중 독립 정서 주석 관련 재현 성분이 있는가?

**신경 표적:** 공통으로 지원되는 피질 영역의 보류 시간·공간 블록 Y와 A 관련 조건부 예측량

**수입 계산 원리:** Agent10의 개념 누출 감사·복수 설명 불확실성 + Agent07의 shared/private 비식별성

**1단계 모델 적용·정확한 입출력:** TRIBE v2는 video/audio/text→평균 피험자 fsaverage5 피질반응 예측이다. CortexMAE/Brain-JEPA는 brain→latent이며, 보류 블록 Y 예측은 훈련 자료에서 별도 head와 마스킹을 구현해야 한다. 두 출력 방향을 동일한 기능으로 취급하지 않는다.

**2단계 과학 질문:** 자극 모형의 불완전성과 신경 내 공변구조가 정서 관련 변동을 얼마나 다르게 포착하는지 검사한다.

**3단계 가정 도전:** 자극 encoding 잔차가 바로 비자극적 또는 정서 고유 신호라는 가정을 반박 가능하게 만든다.

**주가설:** 다양한 검수 의미 표현을 추가해도 brain-conditioned predictor만 회수하는 반복 가능한 A 관련 잔차가 일부 남는다.

**경쟁 설명:** 자극의 누락 사건·비선형성, 개인 평균화, 시공간 smoothing 또는 가까운 Y 누출이 불일치를 만든다.

**관측 대비:** 같은 target Y에서 자극 모형 S, neural-context N, S+N의 외부 예측을 비교한다. N에는 target 블록과 인접 HRF 영향권을 제외하고 target 전체를 본 latent는 금지한다. S의 잔차에서 A 관련 대비와 N의 추가 예측이 겹치는지 새 자극/런에서 검정하고 S에 인간 검수 사건·복수 캡션을 추가한 민감도 곡선을 보고한다.

**반증:** 추가 의미·개인별 보정·넓은 마스크 후 효과가 사라지거나 독립 반복에서 잔차가 재현되지 않으면 신경조건부 추가 정보 주장을 기각한다.

**강한 기준:** 저수준+사건 의미+FIR ridge; TRIBE 공개 평균 출력에 train-only 개인별 선형 보정; masked raw-neighbor ridge; 자기상관을 보존한 surrogate; 단순 nonlinear 자극 encoding

**자료 계획:** ownership: Horikawa, Emo-FilM, Mind Captioning, NSD, Spacetop 보유는 최신 사용자 진술로 확인. 실제 로컬 경로·버전·스키마를 확인한 것은 아니다. / primary: Horikawa 우선. 독립 정서 주석 A, 자극 ID, 신경 Y, 런/반복 구조를 확보한 분석 단위에서 시작한다. / fallback: 자극 단위 beta만 있으면 정적 대비만 수행하고 연속 BOLD 입력을 요구하는 모형에는 넣지 않는다. 주석이나 신뢰도 추정이 없으면 방법 검증으로 범위를 축소한다. / additional: Emo-FilM은 연속 시계열·시간 정렬 확인 뒤 동적 전이; NSD는 정서 주석 확인 전 의미/공간 방법 대조만; Spacetop은 과제별 실제 주석 확인 뒤 일반화; Mind Captioning은 정확한 식별자·버전·주석 사전 확인 전 특정 실험에 배정하지 않는다.

**분석 전 확인 조건:** 공통 cortical mask와 시간 정렬; TRIBE checkpoint의 최종 TR/config와 5초 offset 처리; brain model의 실제 mask token/보류 블록 동작; 개인 평균 출력과 개인 Y 차이의 통제; 독립 반복 및 개념 probe용 별도 자극

**원문 문제와 새로운 질문의 차이:** 원문은 자극 예측, brain pretraining, 개념 해석을 별개로 다룬다. 이 제안은 두 조건부 예측 집합의 불일치를 의미 측정 오차의 강화 과정에서 시험한다.

**중복 위험:** variance partitioning 재적용 위험이 높다. target 누출 방지와 의미 강화에 따른 불일치의 감소/잔존을 일차 판별로 고정한다.

**구별되는 개념 서명:** 관측대상: 같은 보류 피질 Y의 두 조건부 예측 잔차 / 조작: 조건부 입력원과 의미 측정의 완전성 / 경쟁설명: 신경 내 추가 재현 정보 대 자극모형 누락·누출

**여덟 탐색 질문에 대한 답:**

1. 잔차 분석 자체는 기존이다. 두 방향 모델의 공간·시간·개인 평균 차이가 비교를 어렵게 했다.
2. 자극→피질 예측과 fMRI→latent 구현이 같은 자료에서 비교 가능한 도구를 제공한다.
3. encoding 잔차의 정서 특이성과 private 정보의 자동 식별.
4. 멀티모달 자극의 비선형 결합과 신경 내 통계구조를 각각 포착할 수 있다.
5. 모형군이 누락한 재현 성분은 후보이나 정서 고유성은 미확인이다.
6. 개념 우회 감사로 잔차에 누락 사건 정보가 남는지 독립 검정한다.
7. 같은 자연자극 뇌자료를 두 조건부 예측의 적용범위 비교에 사용한다.
8. 잔차가 의미 보강으로 소실되면 정서 해석을 제한하고, 남으면 기존 자극 표현의 충분성을 반박한다.

**근거:** [P026](https://github.com/MedARC-AI/CortexMAE), [P027](https://github.com/facebookresearch/tribev2), [P029](https://github.com/Eric-LRL/Brain-JEPA), [P053](https://proceedings.mlr.press/v97/locatello19a.html), [P080](https://raw.githubusercontent.com/mlresearch/v162/gh-pages/li22n/li22n.pdf), [P083](https://raw.githubusercontent.com/mlresearch/v119/gh-pages/koh20a/koh20a.pdf). 가까운 선행: P027, P026, P083.


## C04-03 — 공간 평균은 정서 관련 분산 코드를 중립적으로 축약하는가?

연결 축: AS07, AS13, AS16. 상태: 조건부 발전: E3 연구 가설; 분석·신규성 확정 전.

**연구 질문:** 같은 피질 관측에서 parcel 평균과 정보량을 맞춘 대조 압축은 독립 정서 대비를 다르게 보존하는가?

**신경 표적:** 동일 피질 마스크의 dense 신호와 결정적 parcel 집계 후 신호; 하위피질로 일반화하지 않는다.

**수입 계산 원리:** Agent07의 압축 불변성·잡음 상한 + Agent10의 동일 backbone 병목 전후 비교

**1단계 모델 적용·정확한 입출력:** CortexMAE-P/F/V의 P=parcel,F=flat map,V=cortex-only 배열을 참고한다. 서로 다른 pretrained variant 차이는 공간 병목 효과의 증명이 아니다. 동일 원자료를 dense→parcel과 rank-matched 대조로 변환해 같은 head/encoder에서 평가한다.

**2단계 과학 질문:** 정서 관련 정보가 지역 평균에 충분한지, 평균에 상쇄되는 공간 분포에 의존하는지 구별한다.

**3단계 가정 도전:** atlas 집계가 통계 효율만 바꾸는 중립 전처리라는 가정.

**주가설:** 일부 A 관련 신뢰가능 대비는 동일 차원·예측 신뢰도를 가진 대조 압축보다 parcel 평균에서 더 크게 감소한다.

**경쟁 설명:** 차이는 SNR·유효 rank·평활화·등록오차 또는 압축량의 차이일 뿐이다.

**관측 대비:** 같은 Y에서 실제 parcel 평균, 동일 크기 공간 연속 random parcel, rank-matched PCA/random projection을 생성한다. 전체 신경 복원과 V,S를 조건화한 A 예측의 손실을 각각 평가한다. 훈련 반복으로만 신뢰도/차원을 정하고 보류 반복의 공간 대비로 확인한다.

**반증:** 손실이 차원·SNR 통제로 설명되거나 random parcel에서도 같으면 해부 atlas가 정서 대비를 선택적으로 제거한다는 주장을 기각한다. 모든 압축에서 동일하면 일반 압축 한계만 보고한다.

**강한 기준:** 동일 rank PCA; random projection; 공간 연속 random parcellation; 평활화 강도 일치 dense ridge; untrained encoder

**자료 계획:** ownership: Horikawa, Emo-FilM, Mind Captioning, NSD, Spacetop 보유는 최신 사용자 진술로 확인. 실제 로컬 경로·버전·스키마를 확인한 것은 아니다. / primary: Horikawa 우선. 독립 정서 주석 A, 자극 ID, 신경 Y, 런/반복 구조를 확보한 분석 단위에서 시작한다. / fallback: 자극 단위 beta만 있으면 정적 대비만 수행하고 연속 BOLD 입력을 요구하는 모형에는 넣지 않는다. 주석이나 신뢰도 추정이 없으면 방법 검증으로 범위를 축소한다. / additional: Emo-FilM은 연속 시계열·시간 정렬 확인 뒤 동적 전이; NSD는 정서 주석 확인 전 의미/공간 방법 대조만; Spacetop은 과제별 실제 주석 확인 뒤 일반화; Mind Captioning은 정확한 식별자·버전·주석 사전 확인 전 특정 실험에 배정하지 않는다.

**분석 전 확인 조건:** 동일 참가자의 dense와 parcel 변환 가능성; 정확한 cortical vertex/voxel 대응; 반복 신뢰도; 표면 재등록 및 smoothing 정보; CortexMAE variant별 학습 차이

**원문 문제와 새로운 질문의 차이:** 원문 병목은 효율적 표현 학습이 목적이다. 새 질문은 동일 관측의 공간 평균이 정서 관련 분산 코드의 충분 통계인지 시험하는 것이다.

**중복 위험:** parcellation benchmark와 중복 가능성이 크다. rank·SNR 일치 후 표적 특이적 손실이 없으면 방법론 결과로 제한한다.

**구별되는 개념 서명:** 관측대상: dense→parcel에서 소실되는 공간 대비 / 조작: 공간 집계 연산 / 경쟁설명: 공간적으로 상쇄되는 코드 대 SNR/차원 손실

**여덟 탐색 질문에 대한 답:**

1. 기존 parcellation 연구가 있어 최초 여부는 E0다. 압축 효과와 신뢰도 차이가 혼재했다.
2. CortexMAE 입력 계열과 병목 분석이 동일 입력의 비교 설계를 돕는다.
3. ROI 평균이 모든 정서 표적에 충분하다는 가정.
4. dense 신호의 분산 공간 패턴을 조합할 수 있다.
5. 평균에서 상쇄되는 재현 공간 대비는 측정 가능한 후보다.
6. VLM의 병목 전후 통제를 피질 집계 연산에 전이한다.
7. 정적 beta 자료도 공간 병목 검정에는 활용할 수 있다.
8. 지역 평균과 분산 패턴 설명의 충분성을 가르며 부정 결과는 더 단순한 공간 모형을 지지한다.

**근거:** [P026](https://github.com/MedARC-AI/CortexMAE), [P051](https://proceedings.mlr.press/v97/kornblith19a.html), [P060](https://github.com/rsagroup/rsatoolbox), [P081](https://raw.githubusercontent.com/mlresearch/v202/gh-pages/li23q/li23q.pdf). 가까운 선행: P026, P081, P051.


## C04-04 — 개인 공통표현은 반복되는 개인별 정서 관련 정보를 지우는가?

연결 축: AS05, AS15, AS28, AS33. 상태: 조건부 발전: E3 연구 가설; 분석·신규성 확정 전.

**연구 질문:** 개인간 정렬과 평균화가 제거한 성분은 측정 잡음인가, 새로운 자극에서도 반복되는 개인별 A 관련 신경 정보인가?

**신경 표적:** 개인별 피질 패턴 중 공유 예측을 뺀 잔차의 독립 반복 신뢰도와 자극 외부 A 관련성

**수입 계산 원리:** Agent07의 shared/private 비식별성·표현 수렴 한계 + Agent10의 입력과 신경 측정 불확실성 구별

**1단계 모델 적용·정확한 입출력:** TRIBE 공개 wrapper는 평균 피험자 cortical prediction을 반환한다. subject-specific layer 코드가 있다고 새 개인의 pretrained head를 제공한다고 가정하지 않는다. 평균 예측+훈련 자료에서 적합한 개인별 residual ridge와 정렬 전/후 신경 표현을 비교한다.

**2단계 과학 질문:** 공유 정서 관련 코드로 충분한지, 평균에서는 소실되지만 개인 내에서 재현되는 표상 차이가 추가로 필요한지 검정한다.

**3단계 가정 도전:** 개인 공통공간 밖의 변동은 모두 잡음이라는 가정. 여기서 개인별 정보는 정보보안/재식별 의제를 뜻하지 않는다.

**주가설:** 정렬 강도를 높일 때 전체 cross-subject 예측은 늘어도 일부 개인별 A 관련 반복 신호는 감소하고 개인 residual head가 새 자극에서 회수한다.

**경쟁 설명:** 개인 잔차는 해부 차이·motion·스캐너·정규화·반복 부족 또는 subject-ID 지름길이며 정서 관련 일반화가 없다.

**관측 대비:** 참가자별 독립 세션/반복에서 잔차 신뢰도를 추정하고, 정렬 강도×개인 residual head 유무를 새 자극에서 비교한다. 같은 participant의 test Y로 정렬을 맞추지 않는다. A가 자극 집계이면 개인별 A 평정을 예측했다고 하지 않고 공유 A와 연결되는 개인별 neural tuning만 평가한다.

**반증:** 개인 residual이 새 자극/세션에 전이하지 않거나 nuisance와 반복 신뢰도로 설명되면 개인별 정서 관련 정보 필요성 가설을 기각한다.

**강한 기준:** 공유 ridge; 공유+개인 intercept/scale; 공유+개인 residual ridge; 해부·motion·site 공변량 모형; subject-label permutation과 신뢰도 일치 대조

**자료 계획:** ownership: Horikawa, Emo-FilM, Mind Captioning, NSD, Spacetop 보유는 최신 사용자 진술로 확인. 실제 로컬 경로·버전·스키마를 확인한 것은 아니다. / primary: Horikawa 우선. 독립 정서 주석 A, 자극 ID, 신경 Y, 런/반복 구조를 확보한 분석 단위에서 시작한다. / fallback: 자극 단위 beta만 있으면 정적 대비만 수행하고 연속 BOLD 입력을 요구하는 모형에는 넣지 않는다. 주석이나 신뢰도 추정이 없으면 방법 검증으로 범위를 축소한다. / additional: Emo-FilM은 연속 시계열·시간 정렬 확인 뒤 동적 전이; NSD는 정서 주석 확인 전 의미/공간 방법 대조만; Spacetop은 과제별 실제 주석 확인 뒤 일반화; Mind Captioning은 정확한 식별자·버전·주석 사전 확인 전 특정 실험에 배정하지 않는다.

**분석 전 확인 조건:** 동일 개인의 독립 세션/반복; 공통 자극 및 참가자 연결 정보; 개인 정서 주석의 존재 여부: 없으면 개인 상태 해석 금지; 정렬 매핑의 training-only 구현; 새 개인 adaptation에 사용할 학습량 고정

**원문 문제와 새로운 질문의 차이:** 원문 평균 예측/표현 수렴의 성능 질문에서, 개인 평균이 제거하는 A 관련 재현 정보의 필요성으로 이동한다.

**중복 위험:** 개인화 encoding 연구와 중복할 수 있다. 단순 개인 head 성능 향상 대신 정렬 증가와 독립 개인 정보 감소의 교호작용을 요구한다.

**구별되는 개념 서명:** 관측대상: 공유공간 밖 개인 내 재현 신경 대비 / 조작: 개인간 정렬 강도/평균화와 개인 residual head / 경쟁설명: 개인 특이 신경 tuning 대 nuisance·ID 지름길

**여덟 탐색 질문에 대한 답:**

1. 개인화 자체는 기존 문제다. 개인 잔차의 신뢰도와 독립 정서 관련성을 함께 요구하면 표본 요구가 크다.
2. 평균 자극 예측과 개인 잔차 모델을 분리하고 정렬 강도를 통제할 수 있다.
3. 공유공간 밖은 잡음이라는 가정.
4. 집단에 공통된 자극–신경 변환을 안정적으로 포착할 수 있다.
5. 개인 내 반복되는 신경 tuning은 평균 모형이 놓칠 수 있다.
6. 식별성 이론은 private latent 이름보다 외부 전이·반복을 먼저 요구하게 한다.
7. 반복 측정 자료를 집단 평균 대신 개인 신경 대비의 안정성 검정에 사용한다.
8. 공유 코드의 충분성과 개인 적응의 과학적 필요를 가른다. 개인의 정서 경험에 관한 결론으로 확장하지 않는다.

**근거:** [P027](https://github.com/facebookresearch/tribev2), [P052](https://proceedings.mlr.press/v235/huh24a.html), [P053](https://proceedings.mlr.press/v97/locatello19a.html), [P060](https://github.com/rsagroup/rsatoolbox), [P086](https://github.com/HuthLab/encoding-model-scaling-laws). 가까운 선행: P027, P052, P053.


## C04-05 — 관측시간격자와 선택적 상태 계산을 분리할 수 있는가?

연결 축: AS09, AS14, AS23, AS32. 상태: 조건부 발전: E3 연구 가설; 분석·신규성 확정 전.

**연구 질문:** 긴 문맥·선택적 상태 모형의 정서 관련 예측 이점은 실제 이력 의존 정보인가, TR·HRF·보간이 만든 저주파 구조인가?

**신경 표적:** 연속 BOLD의 보류 미래 블록 또는 시점별 A 관련 대비; 충분한 시간 주석이 없으면 일반 시간 예측만 가능

**수입 계산 원리:** Agent07의 관측척도 재현성 + Agent10의 문맥 충실도·내용량과 순서 분리

**1단계 모델 적용·정확한 입출력:** Brain-Mamba는 신경 시계열+그래프→표현/과제 출력이며 공개 공식 코드 접근 실패로 pretrained 실행을 가정하지 않는다. Mamba block 원리를 이용한 명시적 새 selective SSM과 fixed SSM을 같은 데이터로 비교한다. CortexMAE의 TR1초 보간은 신경 해상도 향상이 아니다.

**2단계 과학 질문:** 관측 필터로 충분한 시간구조와 맥락에 따라 달라지는 상태 유지 계산의 추가 필요성을 구별한다.

**3단계 가정 도전:** 긴 문맥 모형의 우월성이 곧 긴 신경 통합시간을 입증한다는 가정.

**주가설:** native TR와 합리적인 재표본화/HRF 설정을 바꾸어도 selective-state의 추가 A 관련 예측이 유지되고 사건 이력의 순서에 민감하다.

**경쟁 설명:** FIR·자기회귀·HRF·보간·시간당 표본수 차이 또는 미래 정보 누출이 이점을 설명한다.

**관측 대비:** 같은 실제 시간 길이의 과거만 입력하고 native TR/재표본화 격자×fixed/selective SSM을 교차한다. 예측 시점에서 미래 데이터로 보간·정규화하지 않는다. FIR, 유사 스펙트럼 surrogate, 같은 내용량의 순서 대조를 사용하고 격자×모형 교호작용과 A 관련 외부 예측을 함께 평가한다.

**반증:** 효과가 특정 보간에서만 나타나거나 FIR/HRF와 시간 길이를 맞추면 사라지거나 과거 전용 조건에서 소실되면 신경 상태 선택 필요성 가설을 기각한다.

**강한 기준:** native-TR AR/FIR ridge; 동일 상태차원 fixed SSM; 같은 문맥 길이 temporal convolution; 자기상관/스펙트럼 보존 surrogate; 과거 사건 bag와 순서 보존 표현

**자료 계획:** ownership: Horikawa, Emo-FilM, Mind Captioning, NSD, Spacetop 보유는 최신 사용자 진술로 확인. 실제 로컬 경로·버전·스키마를 확인한 것은 아니다. / primary: Horikawa에서 연속 원시/전처리 시계열 지원을 먼저 확인한다. 없다면 이 동적 후보의 첫 검증은 연속 BOLD·주석을 확인한 Emo-FilM에 배정한다. / fallback: 시점별 A가 없으면 동적 정서 가설은 보류하고 관측격자 방법 검증만 한다. 자극 단위 beta는 이 후보 입력으로 만들지 않는다. / additional: Emo-FilM은 연속 시계열·시간 정렬 확인 뒤 동적 전이; NSD는 정서 주석 확인 전 의미/공간 방법 대조만; Spacetop은 과제별 실제 주석 확인 뒤 일반화; Mind Captioning은 정확한 식별자·버전·주석 사전 확인 전 특정 실험에 배정하지 않는다.

**분석 전 확인 조건:** 연속 BOLD와 정확한 TR/시간원점; 이벤트·정서 주석의 측정 시간 해상도; 보간의 과거 전용 구현; 모형 코드 독립 재구현 검증; 상태차원·학습량·문맥 실시간 길이 통제

**원문 문제와 새로운 질문의 차이:** 원문은 효율적 sequence computation/뇌과제 성능을 다룬다. 새 질문은 시간 관측 연산과 input-dependent state의 필요성을 독립 조작해 신경 이력 가설을 제한한다.

**중복 위험:** 일반 temporal benchmark로 환원될 수 있다. 관측격자에 견고한 독립 A 관련 대비가 없으면 정서 연구 후보에서 내린다.

**구별되는 개념 서명:** 관측대상: 연속 신경의 이력 의존 A 관련 예측 / 조작: 관측격자×상태 선택 계산 / 경쟁설명: 맥락 의존 상태 유지 대 HRF·보간·자기상관

**여덟 탐색 질문에 대한 답:**

1. 시간 모형 비교는 기존이다. 관측시간과 모델 step을 혼동하면 신경 시간 해석이 불가능했다.
2. 선택적 SSM과 공개 fMRI 전처리 코드로 두 요인을 명시적으로 분리할 수 있다.
3. 긴 문맥 성능=긴 신경 통합이라는 가정.
4. 입력에 따라 선택적으로 유지되는 예측 상태를 표현할 수 있다.
5. 단일 고정시간상수로 설명되지 않는 신경 이력 의존성은 아직 E3 후보다.
6. 관측척도 검사와 동일 사건 내용의 순서 통제를 결합한다.
7. 연속 원자료가 있는 보유 자료를 시간격자 민감도 시험에 재사용한다. beta-map 시행순서를 연속신호로 바꾸지 않는다.
8. 견고한 추가 효과면 관측 필터만의 설명을 제한하고, 소실이면 모델 step을 신경시간으로 해석하는 관행을 반박한다.

**근거:** [P026](https://github.com/MedARC-AI/CortexMAE), [P028](https://proceedings.mlr.press/v248/behrouz24a.html), [P034](https://github.com/state-spaces/mamba), [P056](https://proceedings.mlr.press/v119/moor20a.html), [P085](https://github.com/mschrimpf/neural-nlp), [P086](https://github.com/HuthLab/encoding-model-scaling-laws). 가까운 선행: P028, P034, P086.

## 검증 범위와 한계

- Round2는 타 역할 두 원본 보고서를 실제 읽고 수입 원리를 명시한 교환 산출물이다. 해당 원본 작성자와 실시간 대화했다는 뜻은 아니다.
- 원자료 분석·가중치 다운로드·모델 학습/추론은 실행하지 않았다.
- 후보 5개는 E3 제안이다. 기존 canonical 문헌과 역대조했으나 2024–2026의 포괄적 신규성 검색은 이번 라운드에 실행하지 않았고 세계 최초를 주장하지 않는다.
- 원본문/코드 확인 수준은 source_registry에 기존 기록 그대로 보존했다. 표준 모델 이름이 모든 입력·출력을 지원한다는 뜻이 아니다.
- 스키마 미확인은 후속 분석의 명시적 조건이며 현재 개념/RQ 생성의 차단 조건이 아니다.
- 선형 probe 실패만으로 정보 부재, 조건부 예측량만으로 고유 정서 코드, feature 편집만으로 인간 뇌 인과성을 주장하지 않는다.
- 공개 checkpoint의 cortex 지원과 reader의 subcortex 옵션은 구별한다. Brain-Mamba 공식 코드 미확보를 독립 재구현 완료로 표시하지 않는다.

## 근거별 확인 범위

- [P025: SwiFT: Swin 4D fMRI Transformer](https://github.com/Transconnectome/SwiFT): 아니오; 공식 README/코드만 확인; Discussion: 아니오. 이번 라운드는 기존 기록 대조.
- [P026: Scaling Vision Transformers for Functional MRI with Flat Maps](https://github.com/MedARC-AI/CortexMAE): 아니오; 공식 README/코드만 확인; Discussion: 아니오. 이번 라운드는 기존 기록 대조.
- [P027: A foundation model of vision, audition, and language for in-silico neuroscience](https://github.com/facebookresearch/tribev2): 아니오; 공식 README/코드만 확인; Discussion: 아니오. 이번 라운드는 기존 기록 대조.
- [P028: Brain-Mamba: Encoding Brain Activity via Selective State Space Models](https://proceedings.mlr.press/v248/behrouz24a.html): 예; 출판사 PDF 전체; Discussion: 예; Conclusion p242 및 Appendix E pp249–250. 이번 라운드는 기존 기록 대조.
- [P029: Brain-JEPA: Brain Dynamics Foundation Model with Gradient Positioning and Spatiotemporal Masking](https://github.com/Eric-LRL/Brain-JEPA): 아니오; 공식 README/코드만 확인; Discussion: 아니오. 이번 라운드는 기존 기록 대조.
- [P034: Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://github.com/state-spaces/mamba): 아니오; 공식 README/코드만 확인; Discussion: 아니오. 이번 라운드는 기존 기록 대조.
- [P051: Similarity of Neural Network Representations Revisited](https://proceedings.mlr.press/v97/kornblith19a.html): 예; 공식 PDF 직접 열람; Discussion: 예; 결론/한계 해당 절 직접 확인. 이번 라운드는 기존 기록 대조.
- [P052: Position: The Platonic Representation Hypothesis](https://proceedings.mlr.press/v235/huh24a.html): 예; 공식 PDF 직접 열람; Discussion: 예; 결론/한계 해당 절 직접 확인. 이번 라운드는 기존 기록 대조.
- [P053: Challenging Common Assumptions in the Unsupervised Learning of Disentangled Representations](https://proceedings.mlr.press/v97/locatello19a.html): 예; 공식 PDF 직접 열람; Discussion: 예; 결론/한계 해당 절 직접 확인. 이번 라운드는 기존 기록 대조.
- [P056: Topological Autoencoders](https://proceedings.mlr.press/v119/moor20a.html): 예; 공식 PDF 직접 열람; Discussion: 예; 결론/한계 해당 절 직접 확인. 이번 라운드는 기존 기록 대조.
- [P060: A Python Toolbox for Representational Similarity Analysis](https://github.com/rsagroup/rsatoolbox): 아니오; E1은 공식 코드·문서만; Discussion: 아니오. 이번 라운드는 기존 기록 대조.
- [P080: BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation](https://raw.githubusercontent.com/mlresearch/v162/gh-pages/li22n/li22n.pdf): PDF 접근; 첫 페이지·§6 PDF9쪽 직접검토; Discussion: §6 Conclusion PDF9쪽 직접확인. 이번 라운드는 기존 기록 대조.
- [P081: BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models](https://raw.githubusercontent.com/mlresearch/v202/gh-pages/li23q/li23q.pdf): PDF 접근; 첫 페이지·§3.1 PDF2–3쪽·§5/6 PDF8쪽 직접검토; 초기화 코드 확인; Discussion: §5 Limitation 및 §6 Conclusion PDF8쪽 직접확인. 이번 라운드는 기존 기록 대조.
- [P083: Concept Bottleneck Models](https://raw.githubusercontent.com/mlresearch/v119/gh-pages/koh20a/koh20a.pdf): PDF 접근; 첫 페이지·§8 Discussion PDF9쪽 직접검토; Discussion: §8 Discussion PDF9쪽 직접확인. 이번 라운드는 기존 기록 대조.
- [P085: The neural architecture of language: Integrative modeling converges on predictive processing](https://github.com/mschrimpf/neural-nlp): 논문 PDF 미열람; 공식 저장소 열람; Discussion: 미열람. 이번 라운드는 기존 기록 대조.
- [P086: Scaling laws for language encoding models in fMRI](https://github.com/HuthLab/encoding-model-scaling-laws): 논문 PDF 미열람; 공식 저장소 열람; Discussion: 미열람. 이번 라운드는 기존 기록 대조.
