# 초기 감사에서 연구 설계를 바꾸는 발견

확인일: 2026-11-12. Coordinator가 실제 역할별 근거를 대조한 초기 기록이다. 신규성 심사·최종 질문 선정·파일럿 결과가 아니다. 기존 EmoBrain의 가설·분석 결과를 사용하지 않았다.

## 1. Horikawa: 표본 단위를 먼저 고정해야 한다

**검증됨, 공식 메타데이터·코드 범위.** Agent01은 OpenNeuro 공식 미러의 events.tsv 305개를 파싱했다. 참여자 5명 각각 61개 런·2,196개 자극 이벤트가 있다. 실제 열은 `stim_index`이며 README의 `stimulus_index`와 다르다. 원분석 코드는 중복 영상의 label index로 명시한 `dupidx` 15개를 제외하고 2,181개로 계산한다. 실제 처리본과 원영상의 대응은 미확인이다. 소개문에 나오는 2,185개 영상과의 차이는 아직 해결하지 못했다. 이벤트 ID가 고유하다는 사실은 영상 내용이 고유하다는 증거가 아니다.

**문헌 기반 추론.** 새 특징을 추출하기 전에 이벤트 ID·원영상 ID·내용 중복·처리 데이터 Label의 연결표를 확정해야 한다. ID만으로 train/test를 나누면 내용 중복이 남을 수 있다. 공식 Python 예제는 nested cross-validation 생략을 명시하므로 그대로 실행한 값을 엄밀한 재현으로 보고할 수 없다.

**검증 불가.** 공식 코드가 사용하는 category34/dimension14/semantic73/vision1000의 묶음 차원은 확인했지만, feature 본체의 개별 이름·척도·평정자·분포를 열어 확인하지 못했다. 이 차원 수를 검증된 감정 범주 사전으로 취급하지 않는다.

근거: [데이터 감사](../datasets/horikawa/verified_spec.md), [공식 원분석](https://github.com/KamitaniLab/EmotionVideoNeuralRepresentation), [공식 Python 재현](https://github.com/KamitaniLab/EmotionVideoNeuralRepresentationPython).

## 2. EmoNet–Horikawa 비교: 원자극 풀 공유를 먼저 감사한다

**검증됨.** Agent02가 읽은 Kragel et al. (2019) 본문은 Cowen & Keltner의 2,185개 영상에서 얻은 프레임으로 EmoNet을 학습했다고 설명한다. Horikawa 공식 문서도 같은 원영상 풀을 가리킨다.

**문헌 기반 추론.** EmoNet과 Horikawa의 비교는 의미 있는 분석 후보지만, 이를 새로운 자극 분포에서의 독립 검증으로 해석하려면 실제 학습·평가 영상 ID의 중복을 조사해야 한다. 원영상 풀의 공유만으로 모든 개별 시행의 중복을 확정할 수는 없다.

근거: [Agent02 보고서와 Discussion 위치](../agents/02_affective_neuroscience/report.md), 논문 *Emotion schemas are embedded in the human visual system*.

## 3. Emo-FilM: 두 시간축과 서로 다른 측정 단위를 분리한다

**검증됨, 공식 JSON·TSV·코드 범위.** 뇌 측정 목록은 30명, 주석 목록은 44명이다. 별도 참여자 목록만으로 두 집단의 사람이 전혀 겹치지 않는다고 확정하지 않는다. consensus에는 14개 영화·50개 항목·1Hz 정보가 명시된다. 원래 55개 주석 항목에서 일부가 제외된다. 연속 annotation과 clip validation onset은 영화 시간축을 공유하지만 측정·표본 단위가 다르다. 스캐너 onset은 별도의 시간축이다. 대표 scan 이벤트에는 영화 앞 rest가 있어 annotation 0초를 스캐너 0초에 그대로 붙일 수 없다.

공식 `lins_ccc` 함수는 기본 `output="CORR"`에서 Pearson 상관을 반환한다. `mean_ccc`라는 변수명만으로 Lin CCC 측정치를 얻었다고 보고해서는 안 된다. 일부 주석 Description과 Instructions의 극성도 다르므로 원문·제시 스크립트 대조가 필요하다.

**검증 불가.** 다운로드를 시도한 annotation gzip 응답은 git-annex 포인터였다. 숫자 시계열·전체 결측·신뢰도 분포를 확보하거나 검증한 것이 아니다.

근거: [Emo-FilM 감사](../datasets/emofilm/verified_spec.md), [공식 코드](https://github.com/MIPLabCH/Emo-FilM), [뇌 데이터](https://github.com/OpenNeuroDatasets/ds004892), [주석 데이터](https://github.com/OpenNeuroDatasets/ds004872).

## 4. Spacetop과 NSD: 메타데이터 존재와 분석 적합성은 다르다

**검증됨.** Spacetop README의 참여자 101명과 현재 participants.tsv 117행이 다르다. 후자를 품질 통과 분석 인원이라고 해석할 수 없다. alignvideo는 영상 후 평정이며 영상 내부의 연속 정서 궤적이 아니다. 대표 5개 런에서는 응답 결측이 확인됐지만 이것을 전체 결측률로 추정하지 않았다.

NSD 공식 코드에서는 자극·시행 매핑을 확인했으나, 네 연구 데이터셋이 공통 정서 라벨을 제공한다는 근거는 없다. NSD에 AI로 생성한 정서 점수를 붙이더라도 인간이 측정한 정서 정답과 구분해야 한다.

근거: [Spacetop](../datasets/spacetop/verified_spec.md), [NSD](../datasets/nsd/verified_spec.md), [데이터 간 비교](../datasets/cross_dataset_matrix.md).

## 5. 최신 모델의 명칭·버전·평가 방향을 확인해야 한다

**검증됨, 공식 저장소·논문 등 모델별 지정 근거 범위.** Brain-IT의 정확한 논문은 *Image Reconstruction from fMRI via Brain-Interaction Transformer*다. 같은 저장소의 *The Wisdom of a Crowd of Brains*는 영상→뇌 encoder 연구로 방향이 다르다. MindEye2 공식 README는 검색 유사도 행렬 전치로 brain→image와 image→brain 명칭이 바뀌었다고 정정한다. 공식 300-way 평가의 정정된 1시간 학습 brain→image 검색 수치는 57.4%이며, 본 프로젝트가 이를 재현한 것은 아니다.

CortexMAE, TRIBE v2, Brain-Mamba의 입력·출력·공간 범위도 서로 다르다. 피질 전용 표현과 피질하 표상, 평균 피험자 예측과 개인차, 재표본화 간격과 실제 측정 해상도를 혼동하면 안 된다. 모델별 확인 범위와 체크포인트 미확인 항목은 별도 카드에 보존했다.

근거: [Vision 모델 카드](../agents/03_vision_decoding/MODEL_CARDS.md), [뇌 모델 카드](../agents/04_brain_foundation/model_cards.md), [MindEye2 공식 정정](https://github.com/MedARC-AI/MindEyeV2).

## 6. 시간모델 성능을 뇌의 미래 예측으로 해석하기 전 필요한 통제

**검증됨, 공식 구현·논문 범위.** 조사한 AVE와 VideoMamba 구현에는 양방향 처리가 있다. 확인한 일반 masked-video 학습 설정은 그 명칭만으로 과거만을 사용하는 미래 예측을 보장하지 않으므로 mask와 실제 가시 문맥을 확인해야 한다. TCC 공식 문서는 위치를 세는 shortcut을 경고한다. VideoPrism 논문의 Limitations는 짧은 영상에서 16프레임을 표집하는 설정의 장기영상 이해 제약을 설명한다. 이는 원영상 길이가 16프레임이라는 뜻이 아니다.

**새 가설.** 뇌의 정서 관련 시간정보가 현재 장면의 누적보다 상태 전이에 더 가까운지 비교하려면, 특징 추출 단계부터 미래 프레임을 차단하고 관찰 과거 길이를 맞춰야 한다. 위치·motion·사건 경계·의미·HRF 설명과 비교했을 때 남는 정보만 다음 후보로 발전시킬 수 있다. 이 연구의 최초성·데이터 실현성은 아직 확정되지 않았다.

근거: [멀티모달 독립 보고서](../agents/05_multimodal_dynamics/report.md), [Frontier AI 독립 보고서](../agents/06_frontier_ai/report.md).

## 사실검사 이력

[별도 Agent의 원증거 검사](../agents/03_vision_decoding/coordinator_fact_check.md)를 거쳐 시간축·참여자 비중복·중복 영상 매핑·평가 후보 수·masked objective의 범위·프레임 표집 표현을 수정했다. 이는 문서 품질검사이며 5라운드 과학토론을 대신하지 않는다.
