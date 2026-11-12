> Coordinator 통합 사본. [Agent01 원본](../../agents/01_dataset/horikawa/verified_spec.md). 문서의 evidence 경로는 `agents/01_dataset/` 기준이며 실제 데이터 본체 확보를 뜻하지 않는다.

# Horikawa (2020) 검증 명세

검증일: 2026-11-12 · 담당: Agent01 Dataset & Metadata Forensics.

E1은 직접 읽은 공식 코드·데이터 문서·실제 텍스트 메타데이터 범위의 검증이다. 논문 본문을 읽었다는 뜻이 아니다. E2는 공식 문서의 서지/요약 확인, E3는 본 에이전트의 추론, E0는 미확인이다. 전체 데이터 본체·영상·모델은 다운로드하거나 실행하지 않았다. 원문/URL/응답/해시는 `../evidence/fetch_log.jsonl`, 저장소 파일 목록은 `../evidence/repos/*_tree.txt`에 보존했다.

## 식별자와 직접 근거

- E1: 공식 원분석 [KamitaniLab/EmotionVideoNeuralRepresentation](https://github.com/KamitaniLab/EmotionVideoNeuralRepresentation), commit `8fe23a015c4f4ff11de6fb90fcbf20ebc87994ef`. 원분석 코드는 `evidence/repos/horikawa_code/`에 보존.
- E1: [Python 재현 저장소](https://github.com/KamitaniLab/EmotionVideoNeuralRepresentationPython), commit `451236ca2fc3ada704d0b34a30a792c3d6397bf0`.
- E1: [OpenNeuro 공식 미러 ds002425](https://github.com/OpenNeuroDatasets/ds002425), commit `3f94b2bf9a75ddb62637c529d30dc40dd4ab5ba1`; `DatasetDOI=10.18112/openneuro.ds002425.v1.0.2`, BIDSVersion 1.0.2, License CC0.
- E2: 공식 README/description에 Horikawa, Cowen, Keltner, Kamitani (2020), iScience, DOI `10.1016/j.isci.2020.101060` 명시. 논문 본문·Discussion E0. `evidence/horikawa_paper_access.txt`는 프록시 403 기록.

## 획득·표본·정렬

| 항목 | 확인된 값 | 근거와 범위 |
|---|---|---|
| 참여자 | 5명, sub-01–sub-05 | 공식 README 및 현재 raw tree E1 |
| raw 세션 | 각 8개 기능 세션 + ses-anatomy | raw tree/README E1 |
| 런 | 각 61개, 총 305개 | 모든 events.tsv 직접 다운로드·검산 E1 |
| 자극 이벤트 | 각 2,196행, 각 ID/name 2,196개 | `trial_type=1`만 집계 E1 |
| 이벤트 길이 | 10–94초, 10초 이벤트 1,573개/인 | 모든 이벤트 검산; 원 영상 재생 길이와 동일하다고 단정하지 않음 |
| 장비 | Siemens Verio 3T | sub-01 ses-01 run-01 bold.json 대표 1개 E1 |
| TR / TE | 2 s / 0.043 s | README와 대표 sidecar E1 |
| 복셀 | 2×2×2 mm, 76 slices, MB4 | README 획득 명세 E1 |
| raw 좌표 | raw NIfTI, 개별 T1·inplane T2 | README E1 |
| 처리본 | BDTB2 HDF5, ROI별 .mat; fmriprep 언급 | 공식 코드에서 확인; 실행/실물 헤더/버전 E0 |

`evidence/ds002425/sub-*/ses-*/func/*events.tsv`가 305개 원본이다. 재검산은 `python agents/01_dataset/audit_counts.py`; 결과는 `evidence/derived_audit_counts.json`이다. 세션당 런 수는 개인마다 다르다. 원 코드 `prepare_roidata.m`의 처리 파일 묶음 수는 5/7/6/5/5로 raw의 8세션과 다르므로 동일 개념으로 합치지 않는다.

## 결정적 불일치와 누수 위험

1. **실제 열 이름은 `stim_index`**이다. README가 설명한 `stimulus_index`는 305개 실제 헤더에 없다. 실제 헤더는 `onset,duration,trial_type,stimulus_name,stim_index`.
2. README의 2,185 영상 소개와 2,196 시행/2,181 고유 영상 분석 설명은 별개다. 이벤트 ID는 2,196개 모두 서로 다르다. 실제 영상 내용의 고유성을 ID로 검증한 것은 아니다.
3. 원분석 `code/emotion2020_analysis_BATCH.m`의 `p.dupidx=[1,4:8,11,859,866,1673,2157,2187,2188,2194,2195]`는 15개 인덱스를 제외한다. `perform_decoding_analysis.m`은 `metainf.Label`에 이 제외를 적용한다. 2,196−15=2,181은 코드상 일치하지만 2,185와의 차이는 미해결이다.
4. Python 설정은 `label_key=stimulus_name`, `cv.key=Run`, `cv.exclusive_key=stimulus_name`, 61런의 6분할. 그러나 서로 다른 ID에 해당하는 내용 중복은 이 키만으로 제거되지 않을 수 있다(E3). 영상 본체 확인 전 `dupidx`의 ID/내용 매핑을 삭제하지 말고 감사한다.
5. Python README는 nested cross-validation이 빠져 있다고 명시한다. 기본 alpha=100 결과를 원논문 엄밀 재현으로 보고하지 않는다.

## 주석·특징과 가용성

- E1 공식 튜토리얼: category 34, dimension 14, semantic 73, vision 1,000개 특징. 이는 **34개 감정명이 실물로 확인되었다는 뜻이 아니다**. figshare feature ZIP 차단으로 정확한 개별 명칭·척도·평정자 수·분포·결측·신뢰도 미확인.
- E1 경로 계약: `data/features/amt/mean_score_concat/{category,dimension,semantic,vision}`, `data/fmri/paper2020/fmri_Subject1.h5` 등. 이는 공식 코드가 요구하는 경로이며 로컬에 본체가 존재하지 않는다.
- E1 MRI metadata 키: `Session,Run,Block,Label,VoxelData,voxel_x,voxel_y,voxel_z`를 원 코드가 소비한다. 실제 HDF5 내부를 열어 검증하지 않았다.
- E1 ROI 코드: HCP360, 13 individual ROI, 10 subcortical ROI 및 WholeBrain/Cortex를 조합한다. 개별 ROI 크기·실제 피험자별 coverage는 E0.
- E1 원 영상은 Cowen & Keltner 자료 신청 폼으로 요청하도록 README가 안내한다. 신청·승인·영상 다운로드는 수행하지 않았다. 데이터 CC0를 영상 저작권에 확대하지 않는다.
- E0: 원문 방법 상세, fmriprep 버전, HRF 지연·시행 요약 방식, 개별 평정 존재 여부, 청각 제시 여부, 시간별 감정 annotation, 원시 자극 captions/객체·행동 라벨.

`needs_followup`: feature ZIP 접근 및 정확한 라벨/척도, 영상 신청 조건, 2,185/2,181 차이, raw↔처리본 세션 매핑·시간 정렬 확인. `confidence`: 직접 메타데이터 높음; 미확인 항목 판단 유보.
