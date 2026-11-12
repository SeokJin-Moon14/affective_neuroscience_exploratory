# 보유 데이터 기반 연구 설계 보고서

2026-11-12. 사용자는 Horikawa·Emo-FilM·Mind Captioning·NSD·Spacetop을 이미 보유한다. 아래 내용은 기존 공식 메타데이터 감사와 사용자 보유 진술을 결합한 연구 설계용 정리다. 에이전트가 보유본의 모든 숫자 데이터·영상·HDF5를 직접 열었다는 뜻은 아니다. 상세 미확인은 후보별 분석 조건이며 연구 질문 발굴을 막지 않는다.

| 자료 | 공식 근거·확인 범위 | 관측 단위와 연결 가능한 연구 | 분석 전 확인할 핵심 |
|---|---|---|---|
| Horikawa | [ds002425](https://github.com/OpenNeuroDatasets/ds002425), [원분석](https://github.com/KamitaniLab/EmotionVideoNeuralRepresentation), [Python](https://github.com/KamitaniLab/EmotionVideoNeuralRepresentationPython). 5명×61런=305개 events 전수검산. 각2,196개 자극 이벤트 | 자극별 정서 주석·시각/의미 특징과 시행 신경반응. 내용 일반화, 정보 접근성, 지역/분산 결합의 우선 경로 | 실제 헤더 stim_index; 내용 중복과 ID 독립성 구별. 공식 제외15개 뒤2,181과 소개2,185 차이. 보유 feature의 라벨·척도·신뢰도·처리본 세션 대응 |
| Emo-FilM | [뇌 ds004892](https://github.com/OpenNeuroDatasets/ds004892), [주석 ds004872](https://github.com/OpenNeuroDatasets/ds004872), [처리 코드](https://github.com/MIPLabCH/Emo-FilM). fMRI30명, 주석44명, consensus14영화·50열·1Hz | 연속 자극/BOLD와 외부 consensus, 별도의 참가자 clip 평정. 시간 문맥·상태·모달리티 창의 우선 경로 | 주석과 clip 평정은 영화시간의 다른 관측 단위; scanner onset 별도 정렬. 외부 consensus는 개인별 연속 정답이 아님. 코드 lins_ccc 기본 CORR는 Pearson |
| Mind Captioning | 사용자 보유 진술. 특정 공개 식별자·버전·태스크를 이번에 확정하지 않음 | 텍스트–자극–뇌 대응이 있다면 언어 압축·의미 누락·생성 prior를 연결 | 텍스트 출처와 시간 대응. 같은 뇌반응으로 생성한 캡션을 독립 입력으로 그 뇌에 되넣는 순환 금지. 이름만으로 기억·심상/정서 주석 추정 금지 |
| NSD | [공식 코드](https://github.com/cvnlab/nsdcode), 확인한2021 preprint P103과 코드 문서 | 시각 정렬·복원·관측 등가성·반복 신뢰도의 대조 경로 | 보유본의 신경처리 공간·stimulus ID·반복. 측정 정서 ground truth는 현재 확인하지 않았으므로 AI 정서 점수로 대체하지 않음 |
| Spacetop | [ds005256](https://github.com/spatialtopology/ds005256)의 공식 metadata·일부 이벤트 | 사용 태스크의 clip 후 평정과 신경반응. 자료 간 측정·의미 비교 | README101명과 participants117행을 실제 유효 cohort로 단정하지 않음. clip 후0–100 평정은 영상 내부 연속 주석이 아님. 전체 결측·분석 cohort는 보유본에서 확인 |

## 실제 필드와 새 분석용 필드

Horikawa의 공식 이벤트 `onset,duration,trial_type,stimulus_name,stim_index`는 확인했다. 원 코드가 소비하는 `Session,Run,Block,Label,VoxelData`와 feature 경로는 코드 계약이며 보유 HDF5의 실제 헤더를 열어 확인한 것은 아니다. Emo-FilM의 film onset 이벤트와 annotation StartTime=0을 연결해야 하며 평정시간을 scanner time으로 직접 사용하지 않는다.

후속 계획에서 사용하는 `content_group`, `split`, `feature_source`, `annotation_source`, `event_boundary` 등의 이름은 **분석자가 생성·검증할 계약 필드**다. 원 데이터셋에 이미 같은 이름으로 존재한다고 주장하지 않는다. 값과 mapping을 확인하기 전 임의로 채우지 않는다.

## 비교 단위와 추론 경계

Horikawa 자극 집계 주석, Emo-FilM 외부 연속 consensus, Spacetop clip 후 평정을 동일 타깃으로 직접 합치지 않는다. 자료 간 비교는 독립 anchor·측정모형 또는 자료별 별도 검정을 사용한다. 공통 feature 공간에 투영했다는 사실만으로 공통 정서 척도가 확보되는 것은 아니다.

Emo-FilM의 fMRI 명단과 주석 명단이 별도로 제공된다는 사실만으로 사람의 비중복을 확정하지 않는다. 주석을 개별 fMRI 참가자의 연속 정답으로 사용하려면 실제 대응 근거가 필요하다.

정서 관련 신경 대비는 측정 주석과 연결해야 한다. AI-generated labels는 모델 특징으로만 사용한다. 보유 fMRI의 공간·시간 집계로 식별할 수 없는 spike timing·신경 경로의 인과방향은 추가 측정 없이 확정하지 않는다.

상세 근거: [Horikawa](horikawa/verified_spec.md), [Emo-FilM](emofilm/verified_spec.md), [Spacetop](spacetop/verified_spec.md), [NSD](nsd/verified_spec.md), [Mind Captioning](mind_captioning/verified_spec.md), [보유·조건 분기](ownership_and_readiness.md). 기존 감사의 “미확보” 표현은 에이전트 작업 환경에서의 미다운로드를 뜻하며 사용자의 보유 진술을 부정하지 않는다.
