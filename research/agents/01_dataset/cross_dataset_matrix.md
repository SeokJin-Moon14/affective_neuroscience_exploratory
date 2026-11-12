# 데이터 간 비교의 가능 범위

검증일 2026-11-12 · Agent01. 출처는 각 데이터의 verified_spec.md 및 evidence/fetch_log.jsonl. 사실 열은 E1 문서/코드 범위, 정렬 제안은 E3. 원문 Discussion은 확인하지 않았다.

| 비교 변수 | Horikawa | Emo-FilM | Spacetop | NSD |
|---|---|---|---|---|
| 자극 단위 | 짧은 영상 사건 2,196; 내용 중복 제외 코드 | consensus 14영화 | alignvideo 등 task별 영상 | 정지 이미지 |
| fMRI 표본 확인 | raw 5명 | raw 30명 | raw metadata 117; 소개 101; 유효 N 미확정 | 공식 코드 8명 |
| 정서 측정 | 34/14 feature group; 정확한 개별 명칭/척도 미확인 | 별도 44명, 1Hz/50 consensus 항목; fMRI clip validation 분리 | alignvideo 참가자 클립 후 0–100 평정 | 감정 ground truth 확인 못 함 |
| 시간 정렬 | 사건 onset/duration; processed HRF 처리 미확인 | 영화→scanner onset 변환 필수 | video와 뒤따르는 rating phase 분리 | trial→10k→73k 매핑 |
| TR 직접 근거 | 2 s 대표 sidecar | 1.3 s 대표 sidecar | 0.46 s alignvideo sidecar | 1.333 s 공식 예제 |
| 본체 현재 확보 | 없음 | 없음; annotation gzip도 annex 포인터 | 없음 | 없음 |

허용 가능한 전이(E3)는 자극별 독립 특징 추출 후 공통 표현 공간의 가설을 평가하는 것이다. 공통 공간은 데이터에서 이미 제공하는 라벨이 아니다. 직접 통합 전에 실제 라벨의 대상·척도·평정자·시간 단위, 자극 modality, 획득, preprocessing, ROI와 신뢰도를 확인한다.

직접 비교 불가: Horikawa category와 Emo-FilM 이름을 단어 유사도만으로 동일 잠재 감정으로 묶기; Spacetop 클립 후 점수를 Emo-FilM 1Hz 궤적으로 복제하기; NSD AI 생성 점수를 인간 감정 ground truth로 취급하기; 서로 다른 TR을 resampling했다는 이유로 시간 정보가 같다고 가정하기. 공통 영상/참가자/감정 문항이 있다는 증거는 아직 없다.

필요 후속: 새로운 독립 공동 평정 또는 명시적 측정 모형, 모달리티별 features, 공통 anatomy/ROI 변환 검증, 소스별 hold-out 및 stimulus-content group split. confidence: 직접 호환성 낮음, 공통 시각 특징 수준의 방법 전이는 조건부.
