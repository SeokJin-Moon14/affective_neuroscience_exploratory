# Agent12 Round3 실제 상호 비판

2026-11-12. 배정된 Agent01·05의 후보 10개를 모두 검토했다. 판정: 수정 8개, 유지 2개. 새 실험이나 문헌 검증 없이 기존 근거와 관측대상·조작·추정량·반증을 비교했다.

가장 직접적인 중복은 C01-02와 C05-04의 사건좌표 질문이다. 하나의 RQ로 병합하고 TCC/normalized time을 그 안의 대조로 둔다. C01-01↔C12-01, C01-05↔C12-05도 통합 검토를 권고한다. 방법론 fallback은 과학 RQ 수에 더하지 않는다.

## R3-12-C01-01 · 자극 ID에서 내용 등가집합으로: 정서 신경 코드의 조합적 전이
대상: 01_dataset / C01-01 · 판정: **수정**

1. **선행이 답한 부분과 남은 부분:** P001은 시각/의미·정서 표상을 이미 비교하며 새로운 내용군에서의 방향 전이가 남은 문제다. 고정 좌표 실패와 공통 연산 부재는 구별해야 한다.
2. **모델/benchmark 교체 여부:** 내용 집합 및 불변/상호작용 대조가 있어 단순 decoder 교체는 아니다. 다만 embedding으로 그룹을 만든 것 자체는 QC다.
3. **독립 정서 대비 여부:** 정서 대비 방향을 명시했다. 집계 라벨과 개인 상태를 구별한 점은 타당하며 동일 대비의 내용군별 지지구간을 고정해야 한다.
4. **보유자료의 실제 분석 조건:** 보유 영상-ID join, 충분한 content×정서 cell, 반복/런이 실제 분석 조건이다. 미확인이라고 Axis/RQ 생성을 막지는 않는다.
5. **ID·motion·semantics·HRF 대안:** 내용 그룹을 정의한 embedding 자체가 평가 신경표상을 정렬할 수 있다. 그룹 정의는 타깃 독립적이어야 하고 별도 특징군으로도 민감도를 검사한다.
6. **예측·기전·신경 인과의 경계:** 방향 전이 실패는 고정 코드의 한계이며 회전한 공통 계산 부재나 인간 인과를 뜻하지 않는다.
7. **더 강한 기준·대조:** 보류 content를 범주 dummy로 넣은 interaction은 그 계수를 학습할 수 없다. 연속 외부 내용descriptor 기반 제한적 interaction을 추가해야 한다.
8. **부정 결과의 의미:** 충분한 신뢰도에서 고정 방향 실패·조건부 연산 성공은 내용조건부 코드의 근거다. 둘 다 실패하면 모델 부적합/지지구간 부족과 구별해야 한다.

**가장 강한 반론:** 완전히 보류한 내용군의 content×emotion 계수는 단순 범주형 모형으로 추정할 수 없다. 이 대조가 구현 불가능하면 불변모형만 불리해지거나 test 내용을 재학습하게 된다.

**필수 수정:**
- interaction을 외부 내용descriptor로 매개한 제한적 bilinear/저차원 조건부 readout으로 명세하고 train 내용군에서만 적합한다.
- 고정 축·맥락조건부 공통 연산·환경별 독립 모델의 주장 범위를 분리한다. 환경별 모델은 unseen-content 평가의 직접 경쟁자가 아닌 관측 환경 내 상한으로 표시한다.
- 내용 중복 QC만 남는 fallback은 방법후보로 분리한다.

**더 판별적인 검정:** 새 내용군의 외부 특징만으로 예측한 조건부 readout 대 고정 readout을 같은 test neural contrast에서 비교한다. label overlap, rank, 학습예산을 맞추고 test 뇌자료로 좌표를 맞추지 않는다.
**부정 결과의 가치:** 고정 정서 축이 없어도 맥락별 좌표변환 아래 연산이 전이할 수 있다는 중간 결론을 보존한다.
**남은 이견:** 내용 방향이 회전하면 별도 계산이라는 원래 대안과 좌표만 변할 수 있다는 감사자의 중간 가설이 남는다.
**중복 판정:** C12-01과 관측대상·내용 보류·불변/조건부 대조가 겹친다. 조건부 연산 설계를 합쳐 한 RQ로 구체화할 것을 권고.

**기존 근거:**
- [P001 · The neural representation of visually evoked emotion is high-dimensional, categorical, and distributed across transmodal brain regions](https://raw.githubusercontent.com/OpenNeuroDatasets/ds002425/3f94b2bf9a75ddb62637c529d30dc40dd4ab5ba1/dataset_description.json): E2; 아니오; 프록시 403
- [P007 · Generalizable representations of pain, cognitive control, and negative emotion in medial frontal cortex](https://raw.githubusercontent.com/canlab/Neuroimaging_Pattern_Masks/master/Multivariate_signature_patterns/2018_Kragel_MFC_Generalizability/Kragel_2018_NatNeurosci_MFC_generalizability.pdf): E1; 공식 연구실 PDF 다운로드; 초록과 지정 본문/Discussion/Limitations 직접 검토
- [P098 · WILDS: A Benchmark of in-the-Wild Distribution Shifts](https://proceedings.mlr.press/v139/koh21a.html): E1; 예: PDF 저장; 검토 절은 source_location 참조
- [P100 · Statistical inference on representational geometries](https://elifesciences.org/articles/82566): E1; 예: 공식 XML 저장·본문 검토

## R3-12-C01-02 · 시간 샘플에서 사건 진행 단계로: 정서 신경 궤적의 시간척도
대상: 01_dataset / C01-02 · 판정: **수정**

1. **선행이 답한 부분과 남은 부분:** 사건 분절·시간창 연구와 가까우며 P056은 정렬 방법의 근거이지 정서 사건단계 신경코드의 입증이 아니다.
2. **모델/benchmark 교체 여부:** 초 대 사건단계의 계산 단위 비교는 과학 질문이다. 단순 시간축 보정으로 끝나면 방법후보다.
3. **독립 정서 대비 여부:** 독립 주석 대비를 별도로 요구한 점은 적절하다. 사건 경계와 정서 대비를 동일 라벨에서 정의하지 않도록 해야 한다.
4. **보유자료의 실제 분석 조건:** Emo-FilM 영화시간·scanner onset·외부 consensus 단위와 사건 길이가 조건이다. Spacetop clip 평정을 연속 라벨로 늘리면 안 된다.
5. **ID·motion·semantics·HRF 대안:** 0–1 단계는 사건 길이를 알아야 계산된다. 나중의 종료점을 사용해 현재의 상태를 설명하면 retrospective 정렬과 online 계산이 섞인다.
6. **예측·기전·신경 인과의 경계:** 원시간으로 되돌린 후 HRF 적용은 타당하다. 그러나 단계좌표 예측 성공은 실시간 신경 상태 추정이나 속도 조작의 인과효과가 아니다.
7. **더 강한 기준·대조:** elapsed time 외 normalized position 및 과거만으로 추정한 semantic progress를 분리해야 한다. duration-only 대비가 빠지면 단계라는 이름이 과장된다.
8. **부정 결과의 의미:** normalized time으로 충분하면 복잡한 의미 단계의 추가 필요성을 줄인다. 정렬 후 효과 출현 자체는 반증이 아니며 독립 전이 여부가 중요하다.

**가장 강한 반론:** 현재의 0–1 사건 단계는 의미 진행과 단순 duration normalization을 구분하지 못하고 미래 종료점을 사용할 수 있다.

**필수 수정:**
- 경과초·정규화위치·비신경 의미단계의 세 모델을 구별한다.
- offline 사건 좌표의 retrospective encoding과 prefix-only online 진행 추정을 별도 주장으로 표시한다.
- C05-04와 관측대상/HRF 순서/길이 보류/반증을 합쳐 하나의 사건좌표 RQ로 등록한다.

**더 판별적인 검정:** 비신경 데이터로 학습한 의미단계를 새 영화×duration 층에 적용하고 elapsed/normalized time과 원 scanner 시간의 동일 neural contrast에서 비교한다. online 주장을 할 때는 사건 종료 정보 접근을 차단한다.
**부정 결과의 가치:** 고정 관측시간·정규화 위치·의미 단계 중 어느 설명까지 자료가 필요로 하는지 제한한다. 시간정렬 QC만 남으면 RQ 수에서 제외한다.
**남은 이견:** 사건 전체를 보고 정렬한 좌표를 뇌의 실시간 계산상태로 해석할 수 있는지에 대한 경계가 남는다.
**중복 판정:** C01-02와 C05-04는 동일 RQ 중복군: 후자의 TCC/normalized-time 대조를 전자의 관측모형 설계에 병합.

**기존 근거:**
- [P002 · Emo-FilM: A multimodal dataset for affective neuroscience using naturalistic stimuli](https://raw.githubusercontent.com/OpenNeuroDatasets/ds004892/cdf68fe448ad180a476fa2371473a1a6ed063774/dataset_description.json): E2; 아니오; 프록시 403
- [P042 · Temporal Cycle-Consistency Learning](https://github.com/google-research/google-research/tree/master/tcc): E1(공식코드·README 범위);논문본문 미검증;신경전이는E3; 아니오: 논문 본문 미접근; 공식 코드·문서만 직접확인
- [P056 · Topological Autoencoders](https://proceedings.mlr.press/v119/moor20a.html): E1(본문); 정서·뇌 전이는 E3; 예; 공식 PDF 직접 열람
- [P100 · Statistical inference on representational geometries](https://elifesciences.org/articles/82566): E1; 예: 공식 XML 저장·본문 검토

## R3-12-C01-03 · 합의 평균에서 주석 분포로: 정서 구조의 혼합을 뇌가 구별하는가
대상: 01_dataset / C01-03 · 판정: **수정**

1. **선행이 답한 부분과 남은 부분:** 평균의 비충분성과 분포적 표현은 알려진 원리이며 P055 식별 정리가 평정 분포의 신경적 실재를 보장하지 않는다. 남은 것은 독립 평정분포와 neural contrast의 관계다.
2. **모델/benchmark 교체 여부:** 독립 분포 대비가 있다면 새 관측대상이다. 평균 추정의 정확도만 좋아지면 측정 방법후보다.
3. **독립 정서 대비 여부:** 평정분포와 BOLD의 독립 집단이라는 제한을 적었지만 해석의 다중성 코드라는 명명은 더 강하다. 우선 외부 평정분포에 연관된 자극 신경구조로 한정한다.
4. **보유자료의 실제 분석 조건:** 보유 원평정의 문항·척도·평정자 수·시간단위가 필요하다. 연속 자료에서는 각 평정자의 lag와 missingness도 필요하다.
5. **ID·motion·semantics·HRF 대안:** 같은 1Hz 시점의 분산은 반응지연 차이·척도 범위·사건경계 이동에서 생길 수 있다. 의미 변화량을 맞추지 않으면 분포의 모양과 내용 복잡도가 혼동된다.
6. **예측·기전·신경 인과의 경계:** 외부 사람 사이 응답 분포를 fMRI 참가자 내부의 불확실성·혼합 상태로 추론할 수 없다. 분포와 신경 구조의 연관 수준을 유지해야 한다.
7. **더 강한 기준·대조:** 계층 ordinal/척도사용 모형과 rater-specific lag null을 추가한다. 평균+분산을 넘는 고차 분포 효과는 원평정 support가 충분한 경우에만 추정한다.
8. **부정 결과의 의미:** 분포 재현 실패는 측정 한계이고 neural diversity 부재가 아니다. 분포는 재현되나 신경 증분이 충분히 작으면 해당 분포특징의 추가 신경 연관을 제한한다.

**가장 강한 반론:** 평정자 사이의 지연·척도 혼합이 만든 분포를 자극의 해석 다중성으로 부를 위험이 있다. 독립 rater split만으로 이 구조적 대안을 없애지 못한다.

**필수 수정:**
- 제목·주가설의 다중성 코드를 외부 평정분포 관련 신경 대비로 좁힌다.
- rater-specific lag, ordinal scale, 유효평정자 수를 명시하고 이 측정모형의 posterior predictive 분포를 기준으로 사용한다.
- 평균/분산을 동일하게 맞춘 고차분포 대비는 별도 소규모 확장으로 두며 표본 부족시 하지 않는다.

**더 판별적인 검정:** 지연·척도모형만으로 생성한 평정분포 null과 실제 독립 rater 분포를 비교하고, 각각이 원시간 neural contrast에 주는 외부 예측 증분을 동일하게 평가한다.
**부정 결과의 가치:** 측정 혼합 설명과 자극분포 관련 추가 구조를 구분한다. 신경 대비 없이 평정 신뢰도만 개선되면 방법후보로 분리한다.
**남은 이견:** 외부 평정분포의 추가 예측만으로 신경표상이 분포를 표현한다고 할 수 있는지 남는다. 현재는 연관 주장만 허용.
**중복 판정:** 현재 단계에서 독립 여부 최종 확정하지 않음

**기존 근거:**
- [P002 · Emo-FilM: A multimodal dataset for affective neuroscience using naturalistic stimuli](https://raw.githubusercontent.com/OpenNeuroDatasets/ds004892/cdf68fe448ad180a476fa2371473a1a6ed063774/dataset_description.json): E2; 아니오; 프록시 403
- [P055 · Variational Autoencoders and Nonlinear ICA: A Unifying Framework](https://proceedings.mlr.press/v108/khemakhem20a.html): E1(본문); 정서·뇌 전이는 E3; 예; 공식 PDF 직접 열람
- [P100 · Statistical inference on representational geometries](https://elifesciences.org/articles/82566): E1; 예: 공식 XML 저장·본문 검토

## R3-12-C01-04 · 라벨 좌표에서 관계쌍으로: 공통 정서 기하와 공통 신경 코드의 분리
대상: 01_dataset / C01-04 · 판정: **수정**

1. **선행이 답한 부분과 남은 부분:** P057의 기하 정렬과 P055의 식별 원리는 선행이다. 남은 정서 질문은 정렬에 쓰지 않은 관계와 실제 신경 대비의 동시 전이다.
2. **모델/benchmark 교체 여부:** anchor 정답을 더 잘 맞추는 benchmark만이면 방법후보다. 두 측정계의 독립 neural contrast 전이가 있어야 연구 기여가 남는다.
3. **독립 정서 대비 여부:** 평정 anchor와 실제 신경 전이를 이미 구분한 점은 적절하다. 성공시 공통 코드보다는 명시한 정서 관계의 전이라고 제한한다.
4. **보유자료의 실제 분석 조건:** 양쪽 annotation ontology, 독립 bridge 및 양쪽 신경 대비가 분석 조건이다. 공통 자극이 있다는 가정 없이 보유자료의 연결 경로를 설계할 수 있다.
5. **ID·motion·semantics·HRF 대안:** 내용 domain과 획득 차이가 정렬을 지배할 수 있다. 자극 의미-only·획득 신뢰도·거리척도 대조가 모두 필요하다.
6. **예측·기전·신경 인과의 경계:** 낮은 GW비용 또는 후보결합들의 합의는 공통 뇌 알고리즘의 증거가 아니다. 탐색한 근접최적 해 집합 밖의 비유일성도 남는다.
7. **더 강한 기준·대조:** anchor를 fitting/모형선택/최종검증용으로 분리하고 유한한 탐색해 중 일치만 보고하지 않도록 대칭·의미순열 adversarial 대조를 추가한다.
8. **부정 결과의 의미:** 정서 관계 실패는 transport 기반 의미 해석을 제한하며 공통 정서코드 자체의 부재를 입증하지 않는다. neural contrast 없이 성공하면 의미 정렬까지만 남는다.

**가장 강한 반론:** 유한하게 찾은 근접최적 결합이 같은 anchor 답을 내더라도 공통 신경 코드가 식별된 것은 아니다. 정렬 알고리즘의 해공간 탐색 실패와 신경 가설 반증을 구분해야 한다.

**필수 수정:**
- 공통 정서 코드 가설의 기각을 현재 transport·관계모형에서 정서/신경 전이 주장의 기각으로 수정한다.
- anchor의 학습·선택·최종 검증 역할을 나누고 새로운 자극 관계를 예측하는 명시적 out-of-sample map을 지정한다.
- 평정 anchor만 확보된 단계는 방법후보로 분류하고 고유 신경과학 RQ 수에서 제외한다.

**더 판별적인 검정:** 동일 비용대 결합, 의미순열 결합, 감각-only 결합을 모든 fitting에 미사용한 관계와 독립 신경 대비에 평가한다. 두 전이가 모두 성립하는지 각각 보고한다.
**부정 결과의 가치:** 기하 유사성→의미 관계→신경 대비의 어느 연결이 실패하는지 분해할 수 있다. 뇌의 공통 코드가 없다는 일반 결론은 불가하다.
**남은 이견:** 관측가능한 관계 전이가 충분한 과학 성과인지, 공통 코드라는 더 강한 주장이 필요한지 제안자와 남은 쟁점이다.
**중복 판정:** 현재 단계에서 독립 여부 최종 확정하지 않음

**기존 근거:**
- [P001 · The neural representation of visually evoked emotion is high-dimensional, categorical, and distributed across transmodal brain regions](https://raw.githubusercontent.com/OpenNeuroDatasets/ds002425/3f94b2bf9a75ddb62637c529d30dc40dd4ab5ba1/dataset_description.json): E2; 아니오; 프록시 403
- [P002 · Emo-FilM: A multimodal dataset for affective neuroscience using naturalistic stimuli](https://raw.githubusercontent.com/OpenNeuroDatasets/ds004892/cdf68fe448ad180a476fa2371473a1a6ed063774/dataset_description.json): E2; 아니오; 프록시 403
- [P057 · Gromov-Wasserstein Averaging of Kernel and Distance Matrices](https://proceedings.mlr.press/v48/peyre16.html): E1(본문); 정서·뇌 전이는 E3; 예; 공식 PDF 직접 열람
- [P055 · Variational Autoencoders and Nonlinear ICA: A Unifying Framework](https://proceedings.mlr.press/v108/khemakhem20a.html): E1(본문); 정서·뇌 전이는 E3; 예; 공식 PDF 직접 열람
- [P100 · Statistical inference on representational geometries](https://elifesciences.org/articles/82566): E1; 예: 공식 XML 저장·본문 검토

## R3-12-C01-05 · 자극 평균에서 참가자×자극으로: 개인화는 좌표 보정인가 정보 복원인가
대상: 01_dataset / C01-05 · 판정: **유지**

1. **선행이 답한 부분과 남은 부분:** 개인화·shared/private 및 공통/특이 코드 연구가 이미 있다. 참가자×자극 잔차의 독립 정서 대비라는 관측 목표는 QC를 넘는다.
2. **모델/benchmark 교체 여부:** 독립 반복과 새 자극의 상호작용을 따로 검정하므로 retrieval 교체만은 아니다. 기존 정렬정보보존 후보와 통합할 여지는 크다.
3. **독립 정서 대비 여부:** 집계 자극 주석을 개인 내적 상태로 부르지 않고 정서 관련 관계로 제한한 점이 타당하다. 개인별 라벨이 없어도 해당 제한된 질문은 가능하다.
4. **보유자료의 실제 분석 조건:** 참가자×자극의 교차 관측과 반복별 BOLD가 필요하다. 5명으로 모집단 일반화를 과장하지 않고 participant별 CI를 제시한다.
5. **ID·motion·semantics·HRF 대안:** intercept/gain·HRF·시각민감도·SNR 대조가 구체적이다. 참가자별 신호 품질 차이가 interaction처럼 보일 수 있으므로 개인별 noise covariance 추정도 고려한다.
6. **예측·기전·신경 인과의 경계:** 개인 보정의 이득이 생물학적 개인 정서기전의 인과 증거가 아님을 유지해야 한다.
7. **더 강한 기준·대조:** 공유·선형 보정·동일 rank interaction에 동일 데이터량을 주고 새로운 자극×반복에서 같은 contrast를 예측한다. zero-shot과 few-shot은 별도 estimand다.
8. **부정 결과의 의미:** 신뢰로운 원 신호가 있어도 잔차 상한이 충분히 작으면 안정적 개인×자극 코드 필요성을 제한한다. precision 부족은 미결정이다.

**가장 강한 반론:** 주된 설계는 타당하지만 참가자별 파라미터 증가와 개인별 noise geometry를 통한 이득을 안정적 정보 복원으로 오독할 여지가 있다.

**필수 수정:**
- 개인별 noise covariance·학습자극 수를 맞춘 대조와 effect CI/최소효과 기준을 계획에 명시한다.
- 개인 보정 후 남는 interaction의 재현성과 독립 정서 대비를 별도 성공조건으로 둔다.
- C12-05와 공유공간 잔차·반복 신뢰도·정서 대비가 겹치므로 한 과학질문 안에서 참가자/내용군 하위 검증으로 합친다.

**더 판별적인 검정:** train 자극에서 적응하고 test 자극의 두 독립 반복에 대해 interaction 예측과 반복 RDM을 교차 평가한다. 실제 정서 대비 없는 NSD 결과는 시각 개인화 대조로 보고한다.
**부정 결과의 가치:** 공통+gain으로 충분한 범위, 안정적 개인별 관계변형이 필요한 범위, 현재 자료의 식별 한계를 구별한다.
**남은 이견:** 신뢰로운 interaction이 정서 관련성을 가진다는 것과 개인별 정서 주관 상태를 나타낸다는 것은 다른 주장이다. 후자는 다루지 않는다.
**중복 판정:** C12-05 및 AS05/AS13 정보보존군과 중복 통합. 개인×자극 교차 설계를 한 하위 대비로 유지.

**기존 근거:**
- [P001 · The neural representation of visually evoked emotion is high-dimensional, categorical, and distributed across transmodal brain regions](https://raw.githubusercontent.com/OpenNeuroDatasets/ds002425/3f94b2bf9a75ddb62637c529d30dc40dd4ab5ba1/dataset_description.json): E2; 아니오; 프록시 403
- [P015 · MindEye2: Shared-Subject Models Enable fMRI-To-Image With 1 Hour of Data](https://github.com/MedARC-AI/MindEyeV2): E2; 아니오; 공식 코드/README만 직접 확인
- [P009 · Common and stimulus-type-specific brain representations of negative affect](https://raw.githubusercontent.com/canlab/Neuroimaging_Pattern_Masks/master/Multivariate_signature_patterns/2021_Ceko_MPA2_multiaversive/Ceko_2022_NatNeurosci_MPA2_negative_affect.pdf): E1; 공식 연구실 PDF 다운로드; 초록과 지정 본문/Discussion/Limitations 직접 검토
- [P060 · A Python Toolbox for Representational Similarity Analysis](https://github.com/rsagroup/rsatoolbox): E1(공식 코드/문서만); E2(서지); E3(전이); 아니오; E1은 공식 코드·문서만
- [P100 · Statistical inference on representational geometries](https://elifesciences.org/articles/82566): E1; 예: 공식 XML 저장·본문 검토

## R3-12-C05-01 · 공유 통로와 고유 경로의 필요성을 내용과 경로 선택에서 분리
대상: 05_multimodal_dynamics / C05-01 · 판정: **수정**

1. **선행이 답한 부분과 남은 부분:** P035/P037 shared-private 보존 및 P093 gate는 기존 방법이다. 남은 질문은 정서 대비에 고유 입력 정보가 필요한지다.
2. **모델/benchmark 교체 여부:** 고유내용과 gate를 별도로 검사해 단순 fusion 성능을 넘으려 한다. 다만 현재 한 후보에 두 과학질문이 들어 있다.
3. **독립 정서 대비 여부:** 독립 정서 대비와 전체 BOLD를 분리한 것은 적절하다. private 증가가 그 대비에 연결되는 것을 일차 추정량으로 유지한다.
4. **보유자료의 실제 분석 조건:** 실제 시청각 자극·동시 재생과 주석 집계가 조건이다. 시각-only 보유본에서 소리를 만들어 기존 BOLD에 붙이지 않는다.
5. **ID·motion·semantics·HRF 대안:** private latent는 회전·잔차화 방식에 따라 달라지며 미측정 semantics도 들어간다. 내용독립 분해만으로 고유 신경 성분이 되지 않는다.
6. **예측·기전·신경 인과의 경계:** 모델 내 private 제거/gate 개입은 모델의 예측 민감도다. 생물학적 모달리티 경로의 필요성으로 일반화하면 안 된다.
7. **더 강한 기준·대조:** 같은 정보 합집합을 읽는 강한 nonlinear readout이 gate 역할을 흡수할 수 있다. gate+content 대 content를 다른 함수용량으로 비교하지 않아야 한다.
8. **부정 결과의 의미:** private 이득의 상한이 작으면 선택된 공유표현의 충분성을 제한된 자극군에서 지지한다. 한 분해의 실패는 모든 고유정보 부재를 뜻하지 않는다.

**가장 강한 반론:** private latent 정의의 비유일성과 gate의 비선형 readout 능력이 섞이면 내용의 필요성과 계산 경로의 필요성이 분리되지 않는다.

**필수 수정:**
- 일차 가설을 공유 정보 대 전체 모달리티 정보의 정서 대비 충분성으로 좁힌다.
- 고유 성분을 특정 분해의 operational residual로 명명하고 다른 seed/분해/동일 정보 readout에서 결과를 대조한다.
- gate 대조는 별도 확장 또는 C05-05의 조건부 결합 하위분석으로 이동한다.

**더 판별적인 검정:** 공유-only와 같은 rank의 전체정보 및 공유+고유 모델을 공통 nonlinear readout 예산으로 비교한다. 입력 정보원 가림과 latent 좌표 회전을 교차해 정보 접근 차이와 읽기 함수 차이를 분리한다.
**부정 결과의 가치:** 공유 통로의 충분성 또는 선택한 분해의 손실을 판별하되 보편 private 신경기전이나 PID로 확대하지 않는다.
**남은 이견:** 고유 정보를 어떤 분해에 불변하게 정의할 수 있는지, 아니면 정보원 조건부 추가 예측으로만 정의할지가 남는다.
**중복 판정:** 현재 단계에서 독립 여부 최종 확정하지 않음

**기존 근거:**
- [P035 · ImageBind: One Embedding Space To Bind Them All](https://github.com/facebookresearch/ImageBind): E1(공식코드·README 범위);논문본문 미검증;신경전이는E3; 아니오: 논문 본문 미접근; 공식 코드·문서만 직접확인
- [P037 · Factorized Contrastive Learning: Going Beyond Multi-view Redundancy](https://github.com/pliang279/FactorCL): E1(공식코드·README 범위);논문본문 미검증;신경전이는E3; 아니오: 논문 본문 미접근; 공식 코드·문서만 직접확인
- [P093 · Scaling Vision with Sparse Mixture of Experts](https://github.com/google-research/vmoe): E1: 직접 열람한 공식 코드/문서에 한정; E2: 서지·README 논문요약; E3: transfer_idea; 본문/Discussion 미확인; 논문 본문 미열람; 공식 코드·문서 직접 확인
- [P053 · Challenging Common Assumptions in the Unsupervised Learning of Disentangled Representations](https://proceedings.mlr.press/v97/locatello19a.html): E1(본문); 정서·뇌 전이는 E3; 예; 공식 PDF 직접 열람
- [P100 · Statistical inference on representational geometries](https://elifesciences.org/articles/82566): E1; 예: 공식 XML 저장·본문 검토

## R3-12-C05-02 · 모달리티별 과거 창의 비대칭과 측정 지연의 분리
대상: 05_multimodal_dynamics / C05-02 · 판정: **수정**

1. **선행이 답한 부분과 남은 부분:** 시간 receptive window와 modality 차이는 선행문제다. HRF/평정 지연을 맞춘 정서 대비의 모달리티×과거길이 상호작용이 남은 비교다.
2. **모델/benchmark 교체 여부:** 시간창 자유도만 늘려 성능이 오르면 모델 튜닝이다. 사전 정의한 modality×window의 차별적 대비가 있어야 신경질문으로 남는다.
3. **독립 정서 대비 여부:** 독립 정서 대비를 명시했으나 2차원 성능면의 최고점만으로 대비가 구체화되지는 않는다.
4. **보유자료의 실제 분석 조건:** TR·재생 동기·encoder receptive field·외부 평정 lag가 분석 조건이며 충분한 영화/사건을 표본 단위로 삼아야 한다.
5. **ID·motion·semantics·HRF 대안:** 입력 자체의 시간 자기상관과 encoder smoothing이 HRF와 합성된다. 공통 HRF를 쓴다고 모달리티별 잠재시간이 자동 식별되지는 않는다.
6. **예측·기전·신경 인과의 경계:** 현재 설계는 유효 예측창 비교이며 신경 처리 순서·물리적 시간상수의 직접 추정이 아니다.
7. **더 강한 기준·대조:** 사전 고정한 짧음/김 2×2창과 동일 효과 자유도의 공통창을 비교하고 실제 자극 특징에 합성 신경신호를 주입해 식별성을 검사한다.
8. **부정 결과의 의미:** 식별 가능한 상황에서 비대칭 이득의 상한이 작으면 공통 유효창으로 충분한 범위를 제시한다. 회복실험 실패는 신경 비대칭 부재가 아니다.

**가장 강한 반론:** La/Lv와 modality feature의 자기상관·인코더 시간평활·HRF의 조합은 동일 BOLD를 낼 수 있다. 단순 공통 관측모형만으로 뇌 통합창 비대칭을 식별하지 못한다.

**필수 수정:**
- 주장을 모달리티별 유효 예측창 비대칭으로 한정한다.
- 일차 대비를 사전 소수 창의 modality×window interaction으로 고정하고 전체 성능면 탐색은 보조로 둔다.
- 복구 시뮬레이션은 실제 자극 autocorrelation·run 구조·잡음 수준을 사용하도록 계획한다. IID 합성신호만으로 식별성을 선언하지 않는다.

**더 판별적인 검정:** 실제 특징으로 생성한 공통창/비대칭창 합성 BOLD를 같은 pipeline에서 구별한 뒤, 독립 영화의 정서 대비에서 사전 지정 창 interaction을 검정한다. 실패 시 시간관측 방법후보로 분리한다.
**부정 결과의 가치:** 자료가 구별할 수 있는 유효 시간적 정보 요구와 구별할 수 없는 시간상수의 경계를 제공한다.
**남은 이견:** 유효창 차이를 신경 통합시간이라는 언어로 어느 범위까지 부를 수 있는지에 대해 측정모형 의존성을 남긴다.
**중복 판정:** 현재 단계에서 독립 여부 최종 확정하지 않음

**기존 근거:**
- [P002 · Emo-FilM: A multimodal dataset for affective neuroscience using naturalistic stimuli](https://raw.githubusercontent.com/OpenNeuroDatasets/ds004892/cdf68fe448ad180a476fa2371473a1a6ed063774/dataset_description.json): E2; 아니오; 프록시 403
- [P038 · Attention Bottlenecks for Multimodal Fusion](https://github.com/google-research/scenic/tree/main/scenic/projects/mbt): E1(공식코드·README 범위);논문본문 미검증;신경전이는E3; 아니오: 논문 본문 미접근; 공식 코드·문서만 직접확인
- [P043 · VideoMamba: State Space Model for Efficient Video Understanding](https://github.com/OpenGVLab/VideoMamba): E1(공식코드·README 범위);논문본문 미검증;신경전이는E3; 아니오: 논문 본문 미접근; 공식 코드·문서만 직접확인
- [P100 · Statistical inference on representational geometries](https://elifesciences.org/articles/82566): E1; 예: 공식 XML 저장·본문 검토

## R3-12-C05-03 · 사건경계 상태 초기화와 연속 기억의 경쟁
대상: 05_multimodal_dynamics / C05-03 · 판정: **유지**

1. **선행이 답한 부분과 남은 부분:** 사건경계·예측상태 갱신은 기존 질문이며 후보 자체가 Agent11과의 중복을 인정한다. matched reset 위치 대조는 판별적이다.
2. **모델/benchmark 교체 여부:** 경계 대 무작위/never/finite-window는 신경 계산 설명을 가르므로 단순 SSM 적용은 아니다.
3. **독립 정서 대비 여부:** 감각 컷 이득과 독립 정서 전이 대비를 구분했다. 경계 정의가 정서 타깃을 보지 않는지 명시하면 된다.
4. **보유자료의 실제 분석 조건:** 연속 BOLD·독립 경계·clip/run 경계·평정 lag가 조건이다. Spacetop clip평정으로 경계주변 정답을 만들지 않는 점은 타당하다.
5. **ID·motion·semantics·HRF 대안:** 컷/음향 onset/입력량을 맞춘 대조가 강하다. remaining 대안은 reset의 분포이탈과 초기상태의 특정 prior다.
6. **예측·기전·신경 인과의 경계:** 모델 reset은 뇌를 reset한 실험이 아니므로 관찰 신경자료에서 경쟁 예측의 비교로 제한한다.
7. **더 강한 기준·대조:** 상태0 reset 외 학습된 초기상태·soft forgetting을 비교하고 reset 훈련 여부를 맞춘다. P044 VideoPrism만으로 recurrent state 구현이 있다고 가정하지 않는다.
8. **부정 결과의 의미:** finite-window와 동등하면 경계특이 갱신이 필수가 아닐 수 있다. 연속 모델 우위도 정식 경쟁 결과로 보고한다.

**가장 강한 반론:** 모델이 한 번도 보지 않은 상태0 강제 초기화의 실패/성공을 뇌의 사건 경계 갱신으로 읽을 위험은 남지만, 현재의 matched 대조와 양방향 판정으로 수정 가능하다.

**필수 수정:**
- 실제 state를 가진 인과적 모델을 명시하고 reset 연산·초기상태·학습 시 reset exposure를 기록한다.
- zero/learned-state/soft-forgetting 대조로 OOD reset 효과를 분리한다.
- Agent11 동일 조작 후보와 한 RQ로 합치고 고유 RQ 수를 두 번 늘리지 않는다.

**더 판별적인 검정:** 같은 모델·학습예산에서 boundary/random/never/soft decay를 비교하고, held-out 영화의 경계 주변 정서 대비에서 reset 위치특이 효과를 평가한다.
**부정 결과의 가치:** 경계특이 갱신·연속 누적·단순 유한창 중 어느 수준이 관측을 설명하는지 배울 수 있다.
**남은 이견:** 경계에 맞춘 모델 state 조작이 단순 시계열 정규화보다 강한 신경 계산 설명인지는 독립 대비의 판별력에 달려 있다.
**중복 판정:** 후보가 명시한 Agent11 BI-RQ08 계열과 실제 조작이 같으면 병합. 타 역할 Round2 candidateID는 본 배정 범위 밖이므로 새 대응을 추정하지 않는다.

**기존 근거:**
- [P044 · VideoPrism: A Foundational Visual Encoder for Video Understanding](https://github.com/google-deepmind/videoprism): E1(논문 방법·Limitations 직접+공식코드);신경전이는E3; 예: 공식PMLR PDF27쪽 확보;§1–2.3,§3.5–3.6,§5 직접읽음;전문 전체 정독은 아님
- [P089 · Deep Predictive Coding Networks for Video Prediction and Unsupervised Learning](https://github.com/coxlab/prednet): E1: 직접 열람한 공식 코드/문서에 한정; E2: 서지·README 논문요약; E3: transfer_idea; 본문/Discussion 미확인; 논문 본문 미열람; 공식 코드·문서 직접 확인
- [P002 · Emo-FilM: A multimodal dataset for affective neuroscience using naturalistic stimuli](https://raw.githubusercontent.com/OpenNeuroDatasets/ds004892/cdf68fe448ad180a476fa2371473a1a6ed063774/dataset_description.json): E2; 아니오; 프록시 403
- [P100 · Statistical inference on representational geometries](https://elifesciences.org/articles/82566): E1; 예: 공식 XML 저장·본문 검토

## R3-12-C05-04 · 사건 진행 단계와 시계시간에 따른 정서 신경전이의 분리
대상: 05_multimodal_dynamics / C05-04 · 판정: **수정**

1. **선행이 답한 부분과 남은 부분:** P042/TCC의 시퀀스 정렬과 P041 사건 위치는 선행 원리다. 정서 신경전이의 좌표 비교가 새 적용이나 C01-02와 실질적으로 같은 RQ다.
2. **모델/benchmark 교체 여부:** normalized time·위치암기·원시간 HRF 대조가 있으므로 단순 TCC 교체보다 구체적이다. 정렬품질만 남으면 방법후보다.
3. **독립 정서 대비 여부:** 신경전이와 독립 정서 대비의 동시 검증을 요구한다. clip 집계만으로는 이 시간 가설을 검증할 수 없다.
4. **보유자료의 실제 분석 조건:** 독립 사건계열, 자연 duration variation, 원시간 평가가 조건이다. 실제 재생속도 조작 자료가 없음을 올바르게 명시했다.
5. **ID·motion·semantics·HRF 대안:** 자연 duration과 내용·편집·사건 난도가 같이 변한다. matching만으로 속도 효과를 분리했다는 주장은 불가하며 common support를 먼저 명시해야 한다.
6. **예측·기전·신경 인과의 경계:** 모든 시간특징이 t 이후 입력을 차단한다는 전체 제한과 full-sequence TCC alignment가 충돌할 수 있다. retrospective 좌표인지 online state인지 선택해야 한다.
7. **더 강한 기준·대조:** C01-02의 관측모형에 본 후보의 elapsed/normalized/TCC 세분과 duration holdout을 합치면 더 강한 단일 설계가 된다.
8. **부정 결과의 의미:** TCC와 normalized time 동등성은 TCC의 추가 필요성만 낮추며 모든 사건단계 코드 부재를 뜻하지 않는다. 정렬 후 효과 출현만으로 기각하지 않는다.

**가장 강한 반론:** 같은 과학적 추정량과 반증을 가진 C01-02를 모델명이 다른 두 연구로 셀 위험이 가장 크다. 또한 완성 시퀀스 정렬을 online 뇌 진행 추정으로 읽지 않도록 해야 한다.

**필수 수정:**
- C01-02와 하나의 사건좌표 RQ로 병합하고 TCC는 semantic progress 구현 선택지로 둔다.
- retrospective mapping과 online prefix stage를 구분한다. 후자의 경우 test 종료점·미래 프레임 접근을 금지한다.
- duration 비교는 자연조건부 일반화로 표현하고 속도 불변성의 인간 인과 결론을 하지 않는다.

**더 판별적인 검정:** 같은 내용계열의 held-out duration에서 elapsed/normalized/독립 semantic progress 모델을 원시간 neural contrast에 평가한다. 정렬은 정서/BOLD 타깃 미사용, HRF는 원물리시간에서 적용한다.
**부정 결과의 가치:** 단순 시간위치로 충분한 부분과 별도 의미 진행 좌표가 필요한 부분을 분리한다.
**남은 이견:** 전체 시퀀스를 보아야 하는 정렬을 어느 정도까지 신경 계산의 설명으로 인정할지 원 제안과 논의가 필요하다.
**중복 판정:** C01-02와 직접 병합 권고. 관측대상=길이 다른 사건의 정서 신경전이, 조작=시간/단계 좌표, 추정량=보류 neural 대비 증분, 반증=위치/HRF 대조로 설명됨이 동일.

**기존 근거:**
- [P042 · Temporal Cycle-Consistency Learning](https://github.com/google-research/google-research/tree/master/tcc): E1(공식코드·README 범위);논문본문 미검증;신경전이는E3; 아니오: 논문 본문 미접근; 공식 코드·문서만 직접확인
- [P041 · Audio-Visual Event Localization in Unconstrained Videos](https://github.com/YapengTian/AVE-ECCV18): E1(공식코드·README 범위);논문본문 미검증;신경전이는E3; 아니오: 논문 본문 미접근; 공식 코드·문서만 직접확인
- [P002 · Emo-FilM: A multimodal dataset for affective neuroscience using naturalistic stimuli](https://raw.githubusercontent.com/OpenNeuroDatasets/ds004892/cdf68fe448ad180a476fa2371473a1a6ed063774/dataset_description.json): E2; 아니오; 프록시 403
- [P100 · Statistical inference on representational geometries](https://elifesciences.org/articles/82566): E1; 예: 공식 XML 저장·본문 검토

## R3-12-C05-05 · 감각 불일치 조건에서만 필요한 비가산적 시청각 결합
대상: 05_multimodal_dynamics / C05-05 · 판정: **수정**

1. **선행이 답한 부분과 남은 부분:** 시청각 congruence와 fusion은 선행 분야이며 남은 기여는 정서 neural contrast에서 조건별 비가산 결합 필요성이다.
2. **모델/benchmark 교체 여부:** joint−additive의 조건 상호작용을 명시하여 단순 fusion benchmark를 넘는다. 이 interaction을 정확히 정의해야 한다.
3. **독립 정서 대비 여부:** 독립 정서 대비와 total BOLD를 분리한다. congruence와 정서를 동일 응답으로 정의하지 않도록 독립 평정자를 유지한다.
4. **보유자료의 실제 분석 조건:** 실제 동시 시청각 입력·일치도 평정·내용 overlap·조건별 표본이 조건이다. 데이터 보유를 부정하지 않고 새 평정 필요 가능성만 둔다.
5. **ID·motion·semantics·HRF 대안:** 불일치 조건의 BOLD 분산·노이즈·감각 난도와 희귀성이 다르면 조건별 R²의 분모가 달라져 interaction이 생길 수 있다.
6. **예측·기전·신경 인과의 경계:** 관찰 조건별 모델 비교는 계산 설명의 후보이며 PID synergy 또는 신경 인과효과가 아니다. 원 제안의 제한을 유지한다.
7. **더 강한 기준·대조:** additive를 f(A,C)+g(V,C)처럼 함수 형태로 명시한다. concatenation 뒤 nonlinear MLP인 late fusion은 이미 interaction을 포함할 수 있어 additive baseline으로 부를 수 없다.
8. **부정 결과의 의미:** 공통 단위의 이득 interaction 상한이 작으면 조건부 비가산성의 추가 필요성을 제한한다. 조건별 인지/의미 overlap 부족은 null 결과가 아니라 판별 불가다.

**가장 강한 반론:** 조건별 ΔR²를 직접 뺀 값은 신경 신호 분산·노이즈 차이의 영향을 받으므로 결합규칙의 조건부 변화와 동일하지 않다. late fusion의 함수계열도 정의되지 않았다.

**필수 수정:**
- 공통 training 분포에서 학습한 동일 두 모델을 고정하고 각 조건에서 동일한 표적 단위의 paired squared-error 또는 적절한 held-out log-score 개선을 구한다.
- 표적 정규화는 train 자료의 공통 기준으로 고정하고 condition-specific R²는 보조로 보고한다.
- strict nonlinear additive와 joint의 함수클래스·차원·학습예산을 정의한다. 조건부 nuisance C를 양쪽에 동일 제공한다.
- congruence×model contrast를 영화/내용군·참가자 계층으로 추론하고 overlapping 지원 범위에 한정한다.

**더 판별적인 검정:** D(c)=E[(Y-f_add(A,V,C))²−(Y-f_joint(A,V,C))²|congruence=c]를 같은 출력단위에서 구하고 D(불일치)−D(일치)를 matched-support test에서 평가한다. 별도로 실제 정서 대비의 예측 개선을 요구한다.
**부정 결과의 가치:** 언제 additive 설명이 충분한지/부족한지를 조건부로 제한하며 전체 신호난도 차이를 통합효과로 오인하지 않는다.
**남은 이견:** 조건별 예측손실 차이가 결합규칙 변화인지 입력분포 난도 차이인지 완전히 식별되지는 않는다. 자연자료 주장은 조건부 설명 수준이며 추가 교차자극은 별도 신경측정이 필요하다.
**중복 판정:** 현재 단계에서 독립 여부 최종 확정하지 않음

**기존 근거:**
- [P036 · Contrastive Audio-Visual Masked Autoencoder](https://github.com/YuanGongND/cav-mae/tree/master): E1(공식코드·README 범위);논문본문 미검증;신경전이는E3; 아니오: 논문 본문 미접근; 공식 코드·문서만 직접확인
- [P038 · Attention Bottlenecks for Multimodal Fusion](https://github.com/google-research/scenic/tree/main/scenic/projects/mbt): E1(공식코드·README 범위);논문본문 미검증;신경전이는E3; 아니오: 논문 본문 미접근; 공식 코드·문서만 직접확인
- [P041 · Audio-Visual Event Localization in Unconstrained Videos](https://github.com/YapengTian/AVE-ECCV18): E1(공식코드·README 범위);논문본문 미검증;신경전이는E3; 아니오: 논문 본문 미접근; 공식 코드·문서만 직접확인
- [P093 · Scaling Vision with Sparse Mixture of Experts](https://github.com/google-research/vmoe): E1: 직접 열람한 공식 코드/문서에 한정; E2: 서지·README 논문요약; E3: transfer_idea; 본문/Discussion 미확인; 논문 본문 미열람; 공식 코드·문서 직접 확인
- [P100 · Statistical inference on representational geometries](https://elifesciences.org/articles/82566): E1; 예: 공식 XML 저장·본문 검토

## 실행 범위·한계

- 배정된 Agent01·05의 총10개 후보와 자기 Round2를 실제 대조했다. 후보 JSON이 상세 심사 기준이며 Markdown의 구조·설명과도 대조했다.
- 새 원문 확인·네트워크 검색·실물 데이터 검증·모델/신경 분석은 수행하지 않았다. source_papers는 기존 canonical 목록이며 본문/코드/서지 범위를 유지한다.
- 보유5종은 사용자 진술로 유지한다. 미확인 스키마는 분석 조건이며 연구 방향/개념 생성의 차단 조건이 아니다.
- 수정8·유지2는 후보 발전 판정이다. 유지도 novelty 확정 또는 분석 실행 승인이 아니다. C01-02/C05-04 병합 및 C12-01/05와의 중복 연결은 Coordinator가 실제 통합해야 한다.
- 모든 null 판단은 충분한 신뢰도·검정력 및 사전 최소효과 기준을 요구한다. 유의하지 않음을 동등성이나 정보부재로 해석하지 않는다.
- 직접적인 신경 대비가 없는 fallback(QC·평정 개선·label-free 정렬·시간창 민감도)은 방법후보로 분리하고 독립 신경과학 RQ 수에 넣지 않도록 권고했다.
- 현재는 실제 Round3 비판 작성이다. 상대의 수용·반박과 Round4 개정·Round5 판정은 아직 완료하지 않았다.

구조 검증: 10개 대상 후보 누락 없음, 후보당 8체크, canonical 문헌 ID 존재 확인. 공유파일·Git 수정 없음.
