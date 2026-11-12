# Agent12 독립 1차 조사 — 반론을 식별 가능한 질문으로 바꾸기

작성·검증일: 2026-11-12. 담당: Agent12 Adversarial Reviewer & Methodology Auditor.

## 실제 완료 범위와 증거 경계

프로젝트 `AGENTS.md`와 `RESEARCH_MISSION.md`를 읽었다. 타 Agent 결과와 EmoBrain은 검색·열람하지 않았다. 이 문서는 **독립 조사**이며 실제 교차 토론이나 특정 Agent 제안에 대한 심사 결과가 아니다. 모델 학습·뇌 분석·시뮬레이션을 실행하지 않았다. 원문 다운로드, 텍스트 추출, 공식 코드의 정적 확인, 산출물 구조 검증만 수행했다.

확정 문헌 목록은 9편이다. **논문 본문 직접 확인 5편, 저자 공식 코드·문서 확인 3편, 신뢰 가능한 구현팀의 서지만 확인한 E2 1편**이다. 코드 확인 3편을 논문 본문 열람으로 세지 않는다. Snoek 자료는 2018년 preprint 연결과 코드가 검증되었지만 논문 저자 순서·최종 출판본을 확인하지 못했으므로 **별도 `pending_papers.csv`에 두고 9편 집계에서 제외**했다. Cawley–Talbot은 원문 접근이 차단되어 scikit-learn 공식 예제의 정확한 서지만 확인했다. 따라서 9편 모두를 원저자 또는 출판사 원문으로 검증했다고 주장하지 않는다. 코드·문서·서지마다 적용되는 증거 범위를 `papers.csv`와 `source_manifest.csv`에 분리했다.

- **E1-본문**: 원문에서 확인한 주장. 본문 전체를 내려받았어도 실제 검토한 절을 적었다.
- **E1-코드/문서**: 해당 구현·문서의 동작만 확인. 논문의 실험 성능·Discussion·정리 증명을 확인한 것으로 확대하지 않는다.
- **E2**: 서지 또는 초록 확인. **E3**: 아래 연구 연결과 설계 제안. **E0**: 확인하지 못한 데이터 존재·방법 효과·신규성.

학술 웹사이트의 접근 제한 때문에 무제한 문헌 검색은 수행하지 못했다. PMLR와 eLife의 **출판사 공식 GitHub 원문**, 저자 공식 저장소를 사용했다. 프록시 변경·차단 회피·비공식 복제 사이트 이용은 하지 않았다. 따라서 ‘가장 가까운 선행연구를 모두 배제했다’는 신규성 판정은 보류한다.

## 중심 판단

정서 관련 모델–뇌 정렬에서 가장 위험한 실패는 유의한 점수를 얻지 못하는 일이 아니라, **점수가 답하는 일반화 대상과 연구자가 주장하는 신경 계산의 대상이 다른 것**이다. 같은 자극의 반복에 대한 예측, 새로운 자극으로의 일반화, 새로운 참가자로의 일반화, 잠재 원인의 식별은 서로 다른 질문이다. 이 구분을 먼저 고정하면 최신 모델의 가치를 단순 성능 향상이 아닌 경쟁 계산 가설의 판별력으로 평가할 수 있다. 이 판단은 문헌들을 연결한 E3이며 정서 데이터에서 입증된 결론이 아니다.

## 확인한 핵심 문헌과 보조 코드

| ID | 문헌 | 확인한 범위와 감사에 쓰는 내용 |
|---|---|---|
| A12-P01 | Cawley & Talbot, 2010, *On over-fitting in model selection and subsequent selection bias in performance evaluation* | E2 서지. 원문 미확인. nested CV 필요성의 실제 구현은 별도 scikit-learn 공식 예제 E1로 확인했다. |
| A12-P02 (보류·집계 제외) | Snoek 공식 MVCA 저장소; 연결 논문 제목 *How to control for confounds in decoding analyses of neuroimaging data* | E1 코드·README. `ConfoundRegressor.fit`은 train 자료를 요구하고 학습한 계수를 test에 적용한다. 코드가 권장하는 foldwise 제거를 확인했으며 논문 전체의 실험 결과·저자 순서는 미검증이다. 포스터의 저자 집합을 논문 저자 순서로 대신하지 않는다. |
| A12-P03 | Koh et al., 2021, *WILDS: A Benchmark of in-the-Wild Distribution Shifts* | E1 본문 §3–4, §7. domain generalization과 subpopulation shift를 구분하며 OOD validation과 최종 test의 용도를 분리한다. 정서 뇌 데이터에서도 같은 효과가 난다는 주장은 하지 않는다. |
| A12-P04 | Gulrajani & Lopez-Paz, 2020 preprint, *In Search of Lost Domain Generalization* | E1 공식 코드, E2 서지. `model_selection.py`가 학습 도메인 validation, leave-one-domain-out, target-domain oracle 선택을 구분한다. 논문 원문·최종 학회판 미확인. |
| A12-P05 | Schütt et al., 2023, *Statistical inference on representational geometries* | E1 eLife 원문. Discussion s3-1–s3-6, Results·Methods 관련 절. 참가자·조건에 대한 일반화, 유연 모델의 cross-validation, 2요인 bootstrap, noise ceiling, 단일 모델 유의성의 낮은 판별력을 직접 확인했다. |
| A12-P06 | Diedrichsen & Kriegeskorte, 2017, *Representational models: A common framework for understanding encoding, pattern-component, and representational-similarity analysis* | E1 공식 시뮬레이션 코드·README, E2 출판 서지. 같은 생성 공분산·잡음·모델 집합에서 RSA/PCM/encoding을 비교하는 구현을 확인했다. 논문 성능 순위와 Discussion은 미확인. |
| A12-P07 | van den Bosch et al., 2025, *A Python Toolbox for Representational Similarity Analysis* | E1 공식 문서·코드, E2 `CITATION.cff`. 모델 fitting·cross-validation·조건/참가자 bootstrap과 noise ceiling 함수 확인. 2025 preprint 본문은 미확인. |
| A12-P08 | Runge, 2018, *Conditional independence testing based on a nearest-neighbor estimator of conditional mutual information* | E1 본문 §1–2, §5. 고차원 조건부 변수의 어려움, local permutation, 계산 비용과 검정 calibration을 확인했다. 관측적 CMI는 그 자체로 개입 효과를 식별하지 않는다. |
| A12-P09 | Khemakhem et al., 2020, *Variational Autoencoders and Nonlinear ICA: A Unifying Framework* | E1 본문 §3–4 Theorem 1, §5.2, §6. 보조 변수 조건부 factorized prior·injective mixing·충분한 변화에 대한 rank 조건 아래 식별성을 얻는다. 정서 latent의 인과적 실재를 자동 보장하지 않는다. |
| A12-P10 | Locatello et al., 2019, *Challenging Common Assumptions in the Unsupervised Learning of Disentangled Representations* | E1 본문 §3 Theorem 1, §5–6. 가정 없는 비지도 disentanglement의 비식별성과 평가·선택 문제. 모든 구조화·약지도 방법이 불가능하다는 뜻은 아니다. |

공식 원문·코드 URL은 `papers.csv`와 보류 목록에, 로컬 파일·해시·검토 위치는 `source_manifest.csv`에 있다. 확정 논문 9편과 별개로 scikit-learn의 누수·nested CV 공식 문서와 MVCA 코드를 보조 근거로 확인했다.

## 8개 방법론 취약점과 수정·폐기 조건

| 취약점 | 가장 강한 반론 | 구체적 수정 | 주장 축소 또는 폐기 조건 |
|---|---|---|---|
| 누수·의존성 | 같은 자극 반복, 인접 시간창, 동일 영상의 장면이 train/test에 걸치면 자극 기억이나 자기상관으로 정서 점수를 얻을 수 있다. | 예측 대상을 먼저 정의하고 stimulus/clip/run/session/subject 그룹별 외부 분할을 설계한다. 시간 purge 간격은 실제 HRF·특징 입력창·전처리 지지구간에서 정한다. 모든 관측량 기반 학습 변환을 fold 내에서 한다. | 독립적인 test 단위가 없다면 새 자극 일반화 주장을 폐기하고 같은 자극의 반복 예측으로 범위를 좁힌다. 근거 P03/P05 및 공식 누수 문서; 뇌 적용은 E3. |
| nested CV·모델 탐색 | layer·시간 지연·prompt·ROI·특징 수·metric 중 최선만 선택한 뒤 같은 test를 보고하면 모델 계열 전체를 test에 맞춘 것이다. | 이 선택을 inner loop 또는 별도 development 집합에 넣는다. 외부 test를 본 뒤 변경했다면 새로운 검증 자료가 필요하다. | test 재사용을 복구할 독립 검증이 없으면 확인적 우월성 주장을 폐기하고 탐색으로 표시한다. P01은 E2, 구현 원칙은 scikit-learn E1. |
| train/test 분포 | 새 참가자 예측 성공을 새 자극 의미 조합에 대한 일반화로 부를 수 없다. | 참가자×자극의 2차원 분할 표와 분포 차이를 따로 보고한다. target label을 본 model selection은 oracle 또는 adaptation으로 명시한다. | 의미·annotation·획득 차이를 분리할 metadata가 없으면 cross-dataset 불변 계산 주장을 보류한다. P03/P04/P05. |
| 신뢰도·noise ceiling | 모델의 낮은 점수는 뇌가 다른 계산을 해서가 아니라 반복 신뢰도·평정 신뢰도 부족일 수 있다. | 반복/참가자 수준 중 목표와 맞는 ceiling을 추정한다. 원점수, ceiling, 불확실성을 함께 제시하고 test 점수로 voxel을 고르지 않는다. | ceiling이 0 부근이거나 모델 차이 CI가 사전 최소 의미 효과를 판별하지 못하면 모델 부적합 결론을 폐기하고 측정 부족으로 분류한다. P05/P07. |
| RSA 유연성·다중 선택 | 유연한 선형 혼합·layer 선택·거리 선택으로 정렬되었다고 동일한 신경 알고리즘이 되는 것은 아니다. | 고정 모델과 유연 모델을 분리하고 각 fitting을 교차검증한다. metric과 noise normalization을 사전 지정하며 사전 지정한 소수 대안의 민감도를 보고한다. | 우위가 특정 metric 또는 post-hoc layer에만 존재하면 표상 대응을 그 조건으로 제한한다. ‘동일 기전’ 주장은 이 자료만으로 폐기한다. P05/P06/P07. |
| confound 제거 | 의미를 제거하면 정서 관련 표상을 정의하는 실제 내용까지 제거할 수 있다. 잔차가 곧 순수 정서라는 해석은 성립하지 않는다. | 추정 대상부터 고정한다: total 예측력과 주어진 시각/의미 집합에 대한 conditional 추가 예측력을 별도로 보고한다. residualizer는 fold 안에서 학습하고 실제 ID로 행을 정렬한다. | target과 confound가 거의 결정적으로 겹쳐 비교 가능한 표본이 없으면 고유 정서 성분의 식별을 폐기한다. P02/P08/P09; 이 인과 해석 반론은 E3. |
| voxel/ROI 선택 | 높은 정서 예측 voxel을 동일 자료로 선택하고 그 ROI의 점수를 검정하면 순환성이 생긴다. | 독립 localizer·해부학적 ROI·train-fold 내 선택 중 하나를 목적에 맞게 사용한다. ROI 선택·voxel 수·noise threshold 선택도 평가 pipeline에 포함한다. | 독립 선택/재검증이 불가능하면 선택 ROI의 확인적 효과·지역 특이성 주장을 폐기한다. 직접 구현 근거는 scikit-learn feature-selection 누수 문서이며 뇌 적용은 E3. |
| 조건부정보·인과/모델 일반화 | CMI>0, 해석 가능한 latent, 생성 영상의 변화가 실제 뇌의 인과효과를 뜻하지 않는다. | 관측 조건부 연관·가정 아래 latent 식별·자극 개입 결과·신경 개입 결과를 구별한다. 이론의 가정에 대한 스트레스 테스트와 새로운 자극 검증을 계획한다. | 보조 변수 가정·overlap·HRF/동시 입력 문제를 해결하지 못하면 신경 인과 방향 주장을 폐기하고 경쟁 예측 모델의 판별로 재정의한다. P08/P09/P10. |

모든 모델의 사전학습 자료·학습 목표·동일 자극 포함 가능성을 별도로 추적해야 한다(E3). 같은 공개 자극을 본 것과 test 뇌반응/target을 본 것은 다른 오염 경로이며, 전자를 곧바로 뇌 라벨 누수라고 단정하지 않는다. 학습 데이터가 비공개이면 ‘오염 없음’ 대신 미확인으로 기록하고 가능한 새 자극 검증을 우선한다.

## 숨겨진 가정 3개

1. **가정 H1: 정서 주석에서 잘 맞는 모델은 정서 관련 뇌 계산도 설명한다.** 주석·자극 의미·신경반응은 서로 다른 변수다. 시각/의미만으로도 두 예측이 동시에 좋아질 수 있다. 시험: 같은 전체 예측력을 가진 모델들이 새로운 시각–의미 조합에서 정서 관련 neural contrast에 상반된 예측을 내도록 설계한다(P03/P05, E3). 수정: ‘주석 예측’과 ‘뇌 정보’의 평가를 나눈다. 상반 예측이 없으면 기전 비교 후보를 폐기한다.
2. **가정 H2: 더 큰 모델의 잔차 개선은 새로운 계산이다.** 표현 차원·regularization·noise ceiling 차이로 생길 수 있다. 시험: 동일한 출력 차원·동일한 학습 표본·독립적인 hyperparameter 선택 예산 아래 선형/비선형 기준 모델과 비교한다(P01/P06/P07, E3). 차원·선택 예산을 맞추면 개선이 사라질 경우 계산적 신규성 주장을 폐기한다.
3. **가정 H3: 안정적인 latent가 실제 정서 원인이다.** latent 회전·선택 방식이 같아도 원인은 비식별일 수 있다. 시험: 보조 변수의 변경·약지도 제거·분포 이동에 대한 식별 가정 스트레스 테스트와 out-of-sample 행동을 비교한다(P09/P10, E3). 가정을 확인할 자료가 없다면 latent는 유용한 좌표로만 해석한다.

## 미해결 문제 5개

| ID | 과학 질문·근거 | 강한 반론 | 수정 또는 중단 기준 |
|---|---|---|---|
| U1 | 정서 관련 신경표상이 새로운 **시각–의미 조합**으로 전이되는가, 익숙한 자극 군집에 제한되는가? P03/P04/P05, E3. | 조합별 표본 부족과 분포 난도 차이가 실패를 만든다. | 조합 cell의 overlap과 신뢰도를 검사하고 matched baseline을 둔다. cell이 비어 있으면 이 자료로 질문을 검증하지 않는다. |
| U2 | 시각·의미를 조건화한 뒤에도 어떤 정서 주석 관련 신경 차이가 남는가? P02/P08, E3. | 조건화 집합에 따라 질문 자체가 달라진다. | 중첩된 confound 집합별 estimand와 결과를 보고한다. overlap 부족이면 ‘순수 성분’ 분리를 포기하고 공유 정보 구조를 연구한다. |
| U3 | 서로 다른 학습 목표를 가진 AI들의 뇌 정렬 차이가 metric과 fitting 자유도를 넘어서 유지되는가? P05/P06/P07, E3. | 몇 모델·몇 metric만 고르면 임의성만 다시 늘어난다. | 사전 선정한 경쟁 목표와 동일한 fitting budget으로 제한한다. 선택 변화에 따라 순위가 바뀌면 우월성 대신 조건 의존성을 결과로 삼는다. |
| U4 | 설명되지 않은 정서 관련 뇌 변동은 모델 결손인가, 반복·평정의 불확실성인가? P05/P07, E3. | ceiling을 과대 추정하거나 서로 다른 population ceiling을 섞는다. | 반복·참가자·조건별 ceiling을 구분하고 관련 원점수를 함께 보고한다. 독립 반복이 없으면 해당 수준의 ceiling은 미확인이다. |
| U5 | 시간/맥락 보조 변수가 정서 관련 latent의 식별을 실제로 강화하는가? P08/P09/P10, E3. | 보조 변수는 정서 원인보다 run·자극 ID를 알려주는 shortcut일 수 있다. | 시간/맥락/ID를 바꾼 보조 변수와 새 run·새 자극 비교를 둔다. ID 기준선과 구분되지 않으면 신경 계산 해석을 폐기한다. |

## 방법론 기회 5개

1. **참가자×자극 이중 일반화 지도**: P03의 domain 개념과 P05의 2요인 추론을 결합해 동일 자극/새 자극×동일 참가자/새 참가자의 네 질문을 명시한다. 강한 반론은 측정 구조 때문에 네 칸 모두 관측할 수 없다는 것. 가능한 칸만 분석하며 없는 칸을 보간한 결론은 폐기한다.
2. **조건부 정보의 가정 민감도 지도**: P02의 foldwise 조정, P08의 CMI 검정, 단순한 joint encoding baseline을 병렬 비교한다. CMI의 차원·표본 민감성이 핵심 반론이다. 작은 사전 지정 feature set에서 calibration 가능성을 확인하지 못하면 고차원 CMI를 중단하고 예측 차이만 보고한다.
3. **신뢰도에 의해 제한된 모델 반증**: P05/P07의 ceiling과 불확실성을 사용해 모델 우열 검정 전에 측정이 경쟁 모델을 구분할 여지가 있는지 평가한다. ceiling 추정치 자체가 불안정하면 ‘모델이 뇌를 못 설명한다’는 결론을 중단한다.
4. **동일 자유도하의 표현 비교**: P06의 공통 생성 모델 비교 원리를 최신 표현에 적용한다. representation dimension·readout·정규화·선택 예산을 맞춘다. 이 통제가 모델의 유용한 구조까지 지운다는 반론에는 통제 전/후를 함께 제시한다. 통제 후 차이 소실이면 ‘특별한 계산’ 해석을 철회한다.
5. **식별 가정의 실험 설계 도구화**: P09의 보조 변수 요구를 ‘어떤 추가 자극/반복/맥락 조합을 수집해야 원인을 구별할 수 있는가’로 전환한다. P10의 비식별성 반론을 모델 개발 실패가 아닌 수집 설계 기준으로 사용한다. 가정 검증과 반증 예측을 적을 수 없으면 ‘인과 latent’ 명칭을 쓰지 않는다.

모두 E3 제안이며 실행 결과가 아니다. Agent01·03·04·05·07과 연결 가능한 작업이지만 해당 Agent와 실제 정보를 교환한 것으로 기록하지 않는다.

## 타 분야에서의 전이 5개

| ID | 원래 문제 → 새 계산 원리 → 정서 뇌 질문 | 필요한 자료와 반론·수정 |
|---|---|---|
| T1 | 도메인 일반화(P03/P04) → domain별 선택·test 분리 → 정서 관련 코드의 자극 조합 불변성 | 공식 stimulus ID와 조합 metadata 필요. label ontology가 다르면 같은 domain이라고 볼 수 없으므로 cross-dataset pooling을 중단하고 dataset별 estimand를 유지한다. |
| T2 | 조건부 독립성 검정(P08)+confound 조정(P02) → 단순 선형 잔차보다 넓은 조건부 의존성 비교 → 시각·의미를 넘는 추가 신경정보 | 낮은 차원의 조건 변수와 독립 표본 필요. 검정의 영가설 calibration이 실패하면 유의성 주장을 폐기한다. |
| T3 | nonlinear ICA(P09)+비지도 식별 불가능성(P10) → 보조 변수에 의한 식별 조건 → 시간/맥락이 정서 관련 신경 좌표를 구별하는가 | 보조 변수가 실제로 변동하는 관측 설계 필요. run ID와 동치이면 의미 해석을 폐기한다. |
| T4 | 기하학 모델 비교(P05/P06) → readout 자유도와 측정 잡음을 분리 → 서로 다른 AI 목표가 뇌의 어떤 구분을 놓치는가 | 반복·noise covariance 추정 가능 여부 확인. 단일 모델의 유의성만 있으면 경쟁 계산 가설의 증거로 쓰지 않는다. |
| T5 | 모델 선택 감사(P01/P04)+measurement inference(P05) → 탐색 전체를 평가 대상화 → 최고 layer/ROI에서 얻은 정서 alignment가 재현되는가 | 전체 탐색 이력과 고정 외부 test 필요. 이력이 없으면 확인적 재현 대신 탐색 결과로만 보존한다. |

## 예상 밖의 연결 3개

1. **높은 모델 유연성과 낮은 인과 식별성은 동시에 생길 수 있다.** P05는 fitting 자유도를 검증해야 함을, P10은 관측 분포가 같은 여러 latent 설명을 허용함을 보인다. E3 연결: 뇌에 잘 맞는 생성 모델이 많을수록 정답을 찾았다는 주장이 아니라 새 자극에서 예측이 갈리는 실험을 설계할 기회가 늘어난다. 반론: 모델들의 예측이 실질적으로 동일할 수 있다. 수정·폐기: disagreement를 독립 자극에서 만들지 못하면 인과 판별 후보에서 제외한다.
2. **noise ceiling은 성능 보정치인 동시에 일반화 대상의 선언이다.** P03의 domain 구분과 P05/P07의 ceiling·bootstrap은 어떤 참가자/조건 모집단을 대상으로 하는지가 평가를 바꿈을 보여준다. E3 연결: 전체 집계 ceiling 대신 새로운 조합에서의 신뢰도 감소가 정서 모델 실패와 함께 움직이는지 묻는다. 반론: 각 domain의 반복 부족. 수정·폐기: 반복이 없는 domain의 ceiling을 임의 추정하지 않는다.
3. **confound 제거와 disentanglement는 둘 다 무엇을 보존할지 정하는 식별 문제다.** P02의 foldwise 조정만으로 의미 있는 잔차가 보장되지는 않으며 P09의 조건부 prior도 의미를 자동 부여하지 않는다. E3 연결: ‘제거할 의미’ 대신 정서–시각–맥락이 공유하는 부분과 추가 예측 부분의 경계를 competing estimand로 비교한다. 반론: 이름만 다른 variance partitioning일 수 있다. 수정·폐기: 기존 선형 분산분해와 다른 반증 예측·새 조합 일반화가 없으면 신규 연구 질문으로 채택하지 않는다.

## 신규 Sub-axis 3개

상세 등록은 `subaxes.csv`에 있다.

- **S/T/Q: 일반화 대상에 따른 정서 표상 안정성** — 참가자·자극·맥락별 일반화와 그 수준의 불확실성을 결합한다. 모델 수를 늘리는 대신 어느 수준에서 코드가 바뀌는지 묻는다. 근거 P03/P04/P05/P07.
- **P/X/B/C: 조건화 집합에 따른 정서 신경정보의 식별 범위** — confound를 더 제거할수록 더 순수해진다는 가정을 버리고, 조건화 집합·overlap·측정 오차에 따라 식별 가능한 주장을 명시한다. 근거 P02/P08/P09.
- **K/R/T/A: 분석 선택을 통과하는 모델–뇌 구별 가능성** — layer·거리·ROI·readout 자유도를 포함한 선택 전체를 평가하고 경쟁 모델의 독립 예측 차이를 찾는다. 근거 P01/P05/P06/P10.

새 Sub-axis는 모두 E3이며 선행연구가 없는 새로운 분야라는 뜻이 아니다. 독창성은 후속 역검색과 실제 교차 검토에서 판정해야 한다.

## 여덟 가지 탐색 질문에 대한 답

1. **왜 아직 시도되지 않았는가?** 단절 자체를 사실로 확정할 수 없다. 적은 참가자·반복, 자극 metadata 불일치, high-dimensional conditional estimation, 모델 선택 비용이 가능한 장벽이다(E3). P05는 유연 모델을 수천 번 fitting하는 계산 비용을 직접 논의한다(E1).
2. **최근에야 가능해진 것은 무엇인가?** P05의 일반화 추론과 P07의 구현은 정서 데이터에 적용할 방법 기반을 제공한다(E1). 공개 pretrained 표현을 활용하면 경쟁 모델군을 만들 수 있다는 것은 E3이며 구체 모델의 접근성·자원은 아직 확인하지 않았다.
3. **어떤 기존 가정이 틀릴 수 있는가?** 단일 alignment 유의성이 특정 모델을 지지한다는 가정, 조건화 잔차가 순수 정서라는 가정, 분리 latent가 원인이라는 가정이다. 첫째는 P05 원문, 뒤의 정서 적용은 P02/P08/P09/P10에 근거한 E3다.
4. **AI가 기존 모델보다 잘 포착할 수 있는 것은?** 복합 시각·맥락의 비선형 공변동이다(E3). 바로 그 강점이 confound 흡수와 더 많은 선택 자유도를 만들어 엄격한 비교를 요구한다. 실제 우위는 미확인이다.
5. **뇌가 표상하지만 AI가 놓칠 수 있는 것은?** 새로운 맥락에서 유지되거나 바뀌는 정서 관련 구분이다(E3). ceiling·주석·입력 차이를 통제한 뒤에만 ‘AI–brain gap’ 후보로 해석한다. 현재 무엇을 놓친다고 입증된 것은 없다.
6. **다른 분야 방법이 새 사실을 밝힐 수 있는가?** domain generalization은 코드의 적용 범위를, conditional testing은 지정된 변수 집합에 대한 추가 정보를, 식별 이론은 관측 자료로 가능한 주장 한계를 분리한다(P03/P08/P09). 정서 결과는 E3다.
7. **기존 데이터셋을 다른 질문에 재사용할 수 있는가?** Horikawa 우선으로 반복·stimulus ID·run·주석 집계 수준을 확인한 후 일반화 지도에 재사용할 수 있다. Emo-FilM·Spacetop은 시간 경계·annotation 정렬 검증 후 후보, NSD는 실제 정서 주석이 확인되기 전에는 측정/RSA 대조 목적만 후보로 둔다. 이 Agent는 해당 metadata를 직접 확인하지 않았으므로 모두 조건부 E0/E3다.
8. **신경 계산 이해가 실제로 달라지는가?** 특정 모델 점수 대신 ‘정서 관련 구분이 의미 조합을 넘어 유지되는가’, ‘어느 조건화 집합에서 추가 정보가 식별되는가’, ‘경쟁 계산이 언제 다른 예측을 내는가’가 답이 되어야 한다. 이 세 질문의 판별적 결과가 없으면 분석 개선으로만 보고하고 새로운 신경 기전이라고 하지 않는다(E3).

## 저자 후속 제안과 Agent 추론의 분리

| 출처·직접 확인 위치 | 저자가 실제로 논의한 후속 방향 | Agent12의 별도 전이(E3) |
|---|---|---|
| P03 §7 Discussion, PDF p.9 | 다른 분포 이동 응용·자료, architecture/pretraining 확장, 특정 test domain에 대한 과적합 방지와 OOD validation 활용. | 정서 모델도 새로운 자극 조합을 development와 test에 분리하고, target domain 수 부족을 한계로 보고한다. |
| P05 Discussion s3-2, s3-6 | 반복 fitting 비용이 크면 독립 신경자료로 먼저 fitting하는 대안; 참가자·조건 모집단에 일반화할 Bayesian 모델의 개발 필요. | 먼저 작은 readout으로 경쟁 계산을 판별하고, 큰 모델은 별도 fitting 자료가 있을 때만 확장한다. |
| P08 §5 Conclusion, PDF p.8 | 근사 nearest-neighbor·병렬화로 가속하고 큰 표본 영분포의 이론적 근사를 더 연구할 필요. | fMRI 조건부 검정은 차원을 줄이고 국소 교환가능성·시간 의존성부터 점검한다. 이 적용은 원저자 정서 제안이 아니다. |
| P10 §6 Conclusions, PDF p.8 | inductive bias/약지도/시간 구조의 역할을 명시하고 실제 downstream 이득·다양한 데이터에서 평가. | 정서 latent를 찾았다는 주장 전에 어떤 supervision이 의미를 부여했는지 공개한다. |

P09의 Conclusion은 직접 읽었으나 확인한 범위에서 별도의 후속 연구 권고를 추출하지 않았다. P01/P02/P04/P06/P07은 Discussion을 읽지 못했으므로 저자 future direction을 기입하지 않았다.

## 다음 단계와 종료 기준

독립 1차 조사는 완료했다. 다음은 Coordinator가 허용한 뒤 수행할 별도 작업이다: (1) Agent01의 공식 metadata와 후보의 최소 관측 단위·반복·label을 대조, (2) 서로 다른 두 Agent 이상의 제안에 실제 반론 전달, (3) shortlist별 가까운 선행연구 역검색, (4) 반론 수용·수정·기각 이력 기록. 아직 수행하지 않았다.

우선 통과 기준은 새 모델의 점수가 아니라 **분리된 test 단위, 정확한 측정 대상, 경쟁 설명, 불확실성, 독립 검증에서 달라지는 예측**이다. 독립 표본/label/반복이 없으면 그 한계를 숨겨 실행 계획으로 넘기지 않는다. 다만 데이터 제약이 질문 자체의 과학적 가치를 부정하는 것은 아니며 추가 자료가 필요한 질문으로 보존할 수 있다.
