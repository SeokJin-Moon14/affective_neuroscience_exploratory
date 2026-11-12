# Emo-FilM 검증 명세

검증일: 2026-11-12 · 담당: Agent01 Dataset & Metadata Forensics.

E1은 직접 읽은 공식 코드·데이터 문서·실제 텍스트 메타데이터 범위의 검증이다. 논문 본문을 읽었다는 뜻이 아니다. E2는 공식 문서의 서지/요약 확인, E3는 본 에이전트의 추론, E0는 미확인이다. 전체 데이터 본체·영상·모델은 다운로드하거나 실행하지 않았다. 원문/URL/응답/해시는 `../evidence/fetch_log.jsonl`, 저장소 파일 목록은 `../evidence/repos/*_tree.txt`에 보존했다.

## 공식 출처

- E1 [뇌 데이터 ds004892](https://github.com/OpenNeuroDatasets/ds004892), commit `cdf68fe448ad180a476fa2371473a1a6ed063774`; DOI `10.18112/openneuro.ds004892.v1.0.2`.
- E1 [주석 데이터 ds004872](https://github.com/OpenNeuroDatasets/ds004872), commit `e9b1bf0b05975f7815f2924da16e3ff37111739e`; DOI `10.18112/openneuro.ds004872.v1.0.3`.
- E1 [공식 처리 코드](https://github.com/MIPLabCH/Emo-FilM): `constants_emo_film.py`, `MakeMasterfile.py`, `helper_annot.py`, `AnnotationVal.py`, `Statistical analysis/PP_design.fsf`.
- E2 뇌 `dataset_description.json`의 정식 서지: Morgenroth 등 (2025), *Emo-FilM: A multimodal dataset for affective neuroscience using naturalistic stimuli*, Scientific Data 12, 684, DOI `10.1038/s41597-025-04803-5`. 주석 description은 2024 preprint `10.31234/osf.io/qzdbu`를 유지한다. 같은 연구로 한 번만 집계.

## 확인된 구조

| 항목 | E1 확인값 | 범위·주의 |
|---|---|---|
| fMRI 참여자 | 30명 | participants.tsv 및 tree 일치 |
| 주석 참여자 | 44명 | 별도 participants.tsv, fMRI 참여자와 합치면 안 됨 |
| 영화 | consensus 14개 | 14×30 film bold 경로 + 30 rest 경로 = raw bold 450개 |
| 세션 | ses-1–ses-5가 tree에 존재 | 개인별 배치 상이; 모든 사람이 5회라고 주장하지 않음 |
| 장비 | Siemens TrioTim 3T | S01/ses-1/BigBuckBunny 대표 sidecar |
| TR / TE | 1.3 s / 0.03 s | 대표 sidecar |
| slice / MB | 2.5 mm / 3 | in-plane 복셀 크기 전체는 헤더 미확인 |
| 연속 주석 | 1 Hz, StartTime=0, consensus 50열 | derivatives/Annot_AfterTheRain_stim.json |
| 라이선스 | CC0, BIDS 1.7.0 | 두 dataset_description; 영화 라이선스로 확대하지 않음 |
| 처리본 tree | preprocessing, mriqc, physioqc, onset_validation, annotation_validation | 파일 존재 경로만, 수치·전체 파이프라인 실행 여부 E0 |

공식 constants는 원래 16영화/55항목, 제외 영화 `DamagedKungFu,RidingTheRails`, 제외 항목 `Jaw,EyesOpen,Breathing,Movement,Consequences`를 정의한다. consensus에는 14영화/50항목이 남는다. 원주석 55개 항목 각각의 JSON 한 개를 직접 내려받아 label·Instructions·Levels를 확인했다. 단, `*.tsv.gz` 2개 테스트 응답은 **git-annex 포인터**였으며 숫자 시계열 다운로드 성공으로 간주하지 않았다.

## 시간 정렬과 측정 대상

- scan 이벤트 `sub-S01/ses-1/func/sub-S01_ses-1_task-scan_acq-BigBuckBunny_events.tsv`: `onset,duration,trial_type`; film onset 약 93.845초, film duration 약 490.007초, 앞뒤 약 90초 rest. `StartTime=0` annotation을 scanner time 0에 붙이면 어긋난다.
- 별도 `beh/*BigBuckBunny_events.tsv`: `onset,duration,Tears,PleasantOther,Predictable,Stop,Anxiety,trial`. JSON은 onset을 **전체 영화 파일 기준 clip onset**으로 정의한다. 이 값은 scanner time이 아니다.
- 1 Hz 외부 연속 주석, fMRI 참여자의 clip별 validation, 참가자 파일의 영화별 Absorbed/Enjoyed/Interested를 서로 다른 관측 단위로 유지한다. 개인별 전체 연속 정서 시계열이 있다고 가정하지 않는다.
- 대표 beh JSON의 `Predictable`은 Description이 unpredictable, Instructions가 predictable 방향이다. `PleasantOther`도 Description과 Instructions의 극성이 다르다. 역코딩 여부를 원문·제시 스크립트로 확인하기 전 표면 변수명만 해석하지 않는다.

## 신뢰도·전처리 감사

공식 helper의 함수명은 `lins_ccc`지만 기본 인수는 `output="CORR"`이다. 명시적으로 `"CCC"`를 주지 않는 호출은 `np.corrcoef`를 반환한다. 따라서 `mean_ccc`라는 변수명만으로 Lin CCC 신뢰도라고 보고하면 안 된다. 코드는 NaN 보간, flat/outlier 제외, 평정자 agreement 선별, 남은 평정자 평균을 수행한다. **실제 신뢰도 수치는 실행하거나 읽지 않았다.** 같은 선별 데이터로 agreement를 재평가하면 선택 편향이 생길 수 있다는 지적은 E3이다.

공식 FSL FEAT template은 smoothing 6 mm, high-pass 100 s를 설정한다. template 자체의 설정만 E1이며 모든 배포 처리본이 같은 설정·버전으로 생성되었다고 확인하지 않았다. fMRI 시간별 예측에는 효과적인 시간 해상도, HRF와 평정 지연을 별도 모델링한다.

E0: 원 논문·Discussion, 전체 영화 자극 다운로드 경로/권리, 원주석 숫자 범위·분포·결측·평정자별 유효 수, 전체 참가자의 scan onset coverage, QC 결과 수치, full fMRI preprocessing provenance. `needs_followup`: 특히 원문과 실물 annotation/주석 척도. `confidence`: JSON/CSV 필드 높음; 전체 수치 신뢰도 미평가.
