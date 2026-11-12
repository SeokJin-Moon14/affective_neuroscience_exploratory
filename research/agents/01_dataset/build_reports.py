from pathlib import Path
import csv,json,re,datetime,subprocess,collections,hashlib
R=Path(__file__).parent; E=R/'evidence'; D='2026-11-12'; A='Agent01 Dataset & Metadata Forensics'
def write(p,t): (R/p).write_text(t.strip()+'\n')
def csvwrite(p,rows,fields=None):
 fields=fields or list(rows[0]);
 with (R/p).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
def src(name):
 for x in reversed([json.loads(x) for x in (E/'fetch_log.jsonl').read_text().splitlines()]):
  if x['name']==name:return x['url']
 return ''
common='''검증일: 2026-11-12 · 담당: Agent01 Dataset & Metadata Forensics.

E1은 직접 읽은 공식 코드·데이터 문서·실제 텍스트 메타데이터 범위의 검증이다. 논문 본문을 읽었다는 뜻이 아니다. E2는 공식 문서의 서지/요약 확인, E3는 본 에이전트의 추론, E0는 미확인이다. 전체 데이터 본체·영상·모델은 다운로드하거나 실행하지 않았다. 원문/URL/응답/해시는 `../evidence/fetch_log.jsonl`, 저장소 파일 목록은 `../evidence/repos/*_tree.txt`에 보존했다.''' 
write('horikawa/verified_spec.md',f'''# Horikawa (2020) 검증 명세

{common}

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
- E1 경로 계약: `data/features/amt/mean_score_concat/{{category,dimension,semantic,vision}}`, `data/fmri/paper2020/fmri_Subject1.h5` 등. 이는 공식 코드가 요구하는 경로이며 로컬에 본체가 존재하지 않는다.
- E1 MRI metadata 키: `Session,Run,Block,Label,VoxelData,voxel_x,voxel_y,voxel_z`를 원 코드가 소비한다. 실제 HDF5 내부를 열어 검증하지 않았다.
- E1 ROI 코드: HCP360, 13 individual ROI, 10 subcortical ROI 및 WholeBrain/Cortex를 조합한다. 개별 ROI 크기·실제 피험자별 coverage는 E0.
- E1 원 영상은 Cowen & Keltner 자료 신청 폼으로 요청하도록 README가 안내한다. 신청·승인·영상 다운로드는 수행하지 않았다. 데이터 CC0를 영상 저작권에 확대하지 않는다.
- E0: 원문 방법 상세, fmriprep 버전, HRF 지연·시행 요약 방식, 개별 평정 존재 여부, 청각 제시 여부, 시간별 감정 annotation, 원시 자극 captions/객체·행동 라벨.

`needs_followup`: feature ZIP 접근 및 정확한 라벨/척도, 영상 신청 조건, 2,185/2,181 차이, raw↔처리본 세션 매핑·시간 정렬 확인. `confidence`: 직접 메타데이터 높음; 미확인 항목 판단 유보.
''')
write('emofilm/verified_spec.md',f'''# Emo-FilM 검증 명세

{common}

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
''')
write('spacetop/verified_spec.md',f'''# Spacetop 검증 명세

{common}

## 공식 출처·버전

- E1 [spatialtopology/ds005256](https://github.com/spatialtopology/ds005256), commit `a90932e8eb31036b89eeb4488ba1ef705baad2a2`. README는 canonical location을 OpenNeuro ds005256으로 지정.
- E1 `DatasetDOI=10.18112/openneuro.ds005256.v1.1.0`, CC0, BIDS 1.9.0, HED 8.3.0.
- E2 `dataset_description.json`의 인용은 Jung 등 (2024), *A massive multimodal fMRI dataset unifying naturalistic processes with a rich array of experimental tasks*, bioRxiv `10.1101/2024.06.21.599974`. 정식 출판 여부·Discussion 미확인. Authors 배열의 Hung과 인용문의 Hunt 등 서지 표기 차이가 있어 확인 필요.
- E1 [spacetop-prep](https://github.com/spatialtopology/spacetop-prep) README는 fMRI/행동/생리 처리 코드라고 명시. 코드 MIT와 데이터 CC0, 자극 권리는 구별.

## 코호트·획득

README의 N=101, 1인 6시간 스캔 및 2시간 naturalistic viewing은 **README 요약값**이다. 현행 `participants.tsv`는 117행이고 tree도 117개 sub 디렉터리다. 제외자/불완전 사례/업데이트 차이를 확인하지 못했으므로 **분석 가능한 N=117 또는 N=101 중 하나를 임의로 선택하지 않는다**. 세션 디렉터리는 ses-01–ses-04.

현재 raw tree의 bold 경로 수: alignvideo 1,361, faces 315, narratives 423, shortvideo 99, fractional 200, social 1,780. 이는 파일 목록 수이며 품질을 통과한 런 수가 아니다. 범위 밖 과제는 데이터 구조 설명에만 기록한다.

대표 `task-alignvideo_acq-mb8_bold.json`: Siemens Prisma 3T, TR=0.46 s, TE=0.0272 s, MB8, slice thickness/spacing=2.7 mm. 전체 in-plane voxel geometry와 모든 task 동일 프로토콜 여부는 미확인. raw 및 stimuli 경로는 존재하지만 annex 본체/영상은 받지 않았다.

## 정서와 직접 연결되는 확인된 필드

`task-alignvideo_events.json` 및 실제 TSV에서 `onset,duration,trial_type,response_value,stim_file`을 확인했다. `trial_type`은 video 및 `rating_relevance,rating_happy,rating_sad,rating_afraid,rating_disgusted,rating_warm,rating_engaged`. 점수는 0(Barely at all)–100(Strongest imaginable); 무응답은 duration과 response_value가 n/a. **클립 후 평정**이며 영상 내부 연속 주석이 아니다.

5개 예시 런만 확인한 완전성: sub-0001 17/28, sub-0002 5/28, sub-0020 1/28, sub-0060 27/28, sub-0100 0/28 유효 평정. 대표 표본의 결측 경고이지 전체 결측률 추정은 아니다. 영상 행 다음 평정 행의 `stim_file`은 n/a이므로 런 내 앞선 영상과 연결하는 검증된 순서 규칙이 필요하다(E3 구현 제안).

shortvideo JSON에는 `response_angle` 0–180도, `response_label`, `block_condition`, `mentalizing_level`, `stim_file`이 있다. 공식 task README는 약 5초 영상, 21블록×3시행 및 인물에 대한 질문을 명시한다. **이를 시청자 자신의 일반 정서 라벨로 바꿔 부르지 않는다.** 연구 미션의 제외 범위를 확장하는 데 사용하지 않는다.

## 접근·남은 점

- E1 stimulus 예: `stimuli/task-alignvideo/ses-01_run-01_order-01_content-idiots.mp4` 및 해당 events.tsv의 상대 `stim_file`이 tree에서 일치한다.
- E0 직접 영상 접근/영상별 라이선스, usable cohort, BOLD 품질, fmriprep 배포 처리본의 버전, individual score reliability, 전체 결측 패턴, annotation ontology 호환성.
- E0 연속 valence/arousal 주석, 공통 Horikawa stimulus ID, captions 존재는 확인하지 못했다. 있다고 가정하지 않는다.
- 원 논문 접속은 프록시 403. `needs_followup`: 101/117 차이와 QC·결측 및 영상 접근. `confidence`: 현재 메타데이터 높음, 분석 코호트 미확정.
''')
write('nsd/verified_spec.md',f'''# NSD 검증 명세

{common}

## 공식 자료 범위

E1 [cvnlab/nsdcode](https://github.com/cvnlab/nsdcode), [cvnlab/nsdexamples](https://github.com/cvnlab/nsdexamples) commit `d06ba1aaa5587e05f6b043c48491c4e7a4693278`, [cvnlab/nsddatapaper](https://github.com/cvnlab/nsddatapaper) commit `80e891b8bd734a985d3621a0495f2cc91b9d3cfa`를 확인했다. README는 *A massive 7T fMRI dataset to bridge cognitive neuroscience and artificial intelligence* 논문을 지칭하지만 전체 서지·원문을 직접 확보하지 못했다. 이 논문은 `paper_candidates.csv`에 두고 검증 문헌 수에 넣지 않는다. 공식 사이트 연결은 프록시 403.

## 코드에서 확인한 데이터 계약

| 항목 | 공식 예제/코드의 E1 사실 | 직접 실물 검증 한계 |
|---|---|---|
| 참여자 | subj01–subj08, 8명 | 예제와 export_noiseceiling 코드 기준 |
| 세션 | [40,40,32,30,40,32,40,30] | export_noiseceiling.m; 전체 다운로드 대조 없음 |
| 시행 | 세션당 750 beta | example02/06; up to 30,000 trials/subject |
| 반복 | 3회 관측된 이미지 선택 코드 존재 | 모든 이미지가 3회 관측된 것은 아님 |
| 이미지 | 73,000 bank, 425×425 RGB uint8 | example02/06의 HDF5 읽기 계약 |
| shared1000 | 별도 1,000 이미지 경로 | 예제 경로 존재 언급, 실제 파일 다운로드 E0 |
| 공간 | func1pt8mm 및 1 mm 기능 공간; anat 0.5/0.8/1.0 mm; native/fsaverage/MNI | 공식 예제 설명 |
| 시간 | 1.8 mm 예제 time series의 TR 1.333 s | example02 주석; acquisition 모든 파라미터 E0 |
| BOLD 스케일 | 예제 MAT 정수 beta를 300으로 나누면 percent signal change | 포맷에 한정; HDF5/surface에 일괄 적용 금지 |
| 신뢰도 | ncsnr 및 split1/2 산출 코드 | 실제 숫자 미확인 |

주요 코드 경로 계약: `nsddata/experiments/nsd/nsd_expdesign.mat`의 `masterordering,subjectim`; `nsddata_stimuli/stimuli/nsd/nsd_stimuli.hdf5`의 `/imgBrick`; `nsddata_betas/ppdata/subj%02d/func1pt8mm/betas_fithrf/betas_session%02d.mat`의 `betas`; `nsddata/ppdata/subj%02d/behav/responses.tsv`. 예제는 trial→개인별 10k index→73k image ID의 두 단계 매핑을 수행한다. 서로 같은 숫자 범위라고 직접 join하면 안 된다.

`responses.tsv`에서 예제가 사용하는 이름/열 번호는 session(2), time(7), iscorrect(9), RT(10), missingdata(19)이다. 헤더 원본을 직접 읽은 것은 아니다. 이 다섯 열을 감정 평정으로 취급하지 않는다.

## 정서 연구의 경계

공식 검토 범위에서 **정서 범주·valence·arousal ground truth를 확인하지 못했다**. 따라서 정서 라벨이 없다는 전역적 단정도 피하지만, 현재 자료만으로 supervised emotion encoding/decoding의 독립 정답을 제공한다고 주장할 수 없다. AI 추론 점수를 만들면 모델 파생 특징이다. 객체·장면·caption의 COCO 매핑 세부 필드도 이번 공식 검증에서는 미확인이다.

NSD는 이미지 내용 통제, 시각 표상 정렬, 반복 기반 측정 오차 추정에 조건부로 유용하다(E3). 자연 영상의 감정 시간 궤적이나 청각 통합을 직접 검증하는 자료로 취급하지 않는다. NSD 학습 모델을 NSD 자체에서 평가할 경우 pretraining 및 shared stimulus 누수를 별도 감사한다.

E0: 논문 전체 서지/Discussion, 현재 다운로드·등록·데이터/자극 라이선스, 정확한 acquisition TE/영상 제시시간, 원본 HDF5/TSV 실제 shape·결측, 감정 annotation. `needs_followup`: 공식 Data Manual과 해당 메타데이터 확보. `confidence`: 공식 코드 경로·동작 높음, 실제 배포본 무결성 미확인.
''')

# metadata inventories
fields=['field_name','definition','unit','observed_path','source','coverage','missingness','evidence_level','source_scope','verified_on','confidence','needs_followup','origin_agent']
meta={k:[] for k in ['horikawa','emofilm','spacetop','nsd']}
def add(ds,f,d,u,p,cover='',missing='미평가',scope='실제 텍스트 metadata',follow='없음',url=None):
 meta[ds].append(dict(zip(fields,[f,d,u,p,url or src(p),cover,missing,'E1',scope,D,'높음(명시 범위)',follow,A])))
hp='ds002425/sub-01/ses-01/func/sub-01_ses-01_task-CowenKeltnerEmotionMovie_run-01_events.tsv'
for f,d,u in [('onset','런 기준 이벤트 시작','s'),('duration','자극/휴지 이벤트 길이; 원 영상 길이와 동일성 미확인','s'),('trial_type','1=자극; -1/-2=전후 휴지','정수'),('stimulus_name','선행 0을 포함한 자극명 문자열','문자열'),('stim_index','실제 헤더의 자극 인덱스; README stimulus_index와 불일치','정수')]:add('horikawa',f,d,u,hp,'5명×61런 전체 헤더/행 감사','휴지의 stimulus 필드는 n/a')
for f in ['Session','Run','Block','Label','VoxelData','voxel_x','voxel_y','voxel_z']:
 add('horikawa',f,'원 ROI 준비 코드가 소비하는 HDF5 metadata 키','미확인','repos/horikawa_code/code/sub/prepare_roidata_individual.m','코드 계약','본체 미확인','공식 코드', '실제 HDF5 키·shape 확인', 'https://github.com/KamitaniLab/EmotionVideoNeuralRepresentation/blob/8fe23a015c4f4ff11de6fb90fcbf20ebc87994ef/code/sub/prepare_roidata_individual.m')
for ds,n in [('emofilm','ds004872'),('emofilm','ds004892'),('spacetop','ds005256')]:
 p=n+'/participants.tsv';rows=list(csv.DictReader((E/p).open(),delimiter='\t'));j=json.loads((E/n/'participants.json').read_text())
 for f in rows[0]:
  missing=sum(x[f] in ['n/a','','NaN','nan'] for x in rows)
  add(ds,f,'참가자 메타데이터; 상세 정의는 공식 participants.json 참조','원 JSON 참조',p,str(len(rows))+'행',str(missing)+'행(빈값/n/a/NaN만 집계)',follow='척도 해석 시 JSON 정의 확인')
for p in ['ds004892/sub-S01/ses-1/func/sub-S01_ses-1_task-scan_acq-BigBuckBunny_events.tsv','ds004892/sub-S01/ses-1/beh/sub-S01_ses-1_task-BigBuckBunny_events.tsv']:
 rows=list(csv.DictReader((E/p).open(),delimiter='\t'))
 for f in rows[0]:add('emofilm',f,'scanner 이벤트' if '/func/' in p else '영화 기준 clip validation; scanner 기준 아님','s' if f in ['onset','duration'] else '원 JSON 참조',p,'S01 BigBuckBunny 예시')
for f in ['SamplingFrequency','StartTime','Columns']:
 add('emofilm',f,{'SamplingFrequency':'1 Hz','StartTime':'영화 기준 0','Columns':'50개 consensus 항목'}[f],'Hz/s/목록', 'ds004872/derivatives/Annot_AfterTheRain_stim.json','대표 consensus sidecar','숫자 시계열은 annex 포인터')
for task in ['alignvideo','shortvideo']:
 p='ds005256/task-'+task+'_events.json';j=json.loads((E/p).read_text())
 for f in j:add('spacetop',f,'공식 task 이벤트 정의; alignvideo 점수 0–100; shortvideo angle 0–180도','원 JSON 참조',p,'task '+task,'개별 결측 존재')
for ds,p in [('horikawa','ds002425/sub-01/ses-01/func/sub-01_ses-01_task-CowenKeltnerEmotionMovie_run-01_bold.json'),('emofilm','ds004892/sub-S01/ses-1/func/sub-S01_ses-1_task-BigBuckBunny_bold.json'),('spacetop','ds005256/task-alignvideo_acq-mb8_bold.json')]:
 j=json.loads((E/p).read_text())
 for f in ['RepetitionTime','EchoTime','Manufacturer','ManufacturersModelName','MagneticFieldStrength','SliceThickness','SpacingBetweenSlices','MultibandAccelerationFactor']:
  if f in j:add(ds,f,str(j[f]),'s' if f in ['RepetitionTime','EchoTime'] else 'BIDS 정의',p,'대표 sidecar','없음(대표 파일)')
for f,d,p in [('masterordering','시행→개인 10k 인덱스','nsdexamples/matlab/example06_basicbetaloading.m'),('subjectim','개인 10k→73k 이미지 ID','nsdexamples/matlab/example06_basicbetaloading.m'),('/imgBrick','425×425 RGB 이미지 bank','nsdexamples/matlab/example06_basicbetaloading.m'),('betas','시행별 beta; 예제 MAT는 /300 percent signal change','nsdexamples/matlab/example06_basicbetaloading.m'),('ncsnr','3회 관측 이미지로 추정하는 SNR; 수치 미확인','nsddatapaper/main/export_noiseceiling.m')]:add('nsd',f,d,'코드 참조',p,'공식 예제/생성 코드','실물 미확인','공식 코드', '배포본 직접 헤더 검증')
for f in ['session','time','iscorrect','RT','missingdata']:add('nsd',f,'behavioral responses.tsv 예제 주석의 열 이름','RT는 ms; time은 days','nsdexamples/matlab/example09_behavioraldata.m','공식 예제','실제 TSV 미확인','공식 코드','헤더 원본 확인')
for ds,rows in meta.items():csvwrite(ds+'/metadata_inventory.csv',rows,fields)

annfields=['label_name','annotation_type','target','scale_range','rater','time_unit','availability','reliability','observed_path','source','evidence_level','source_scope','verified_on','confidence','needs_followup','origin_agent','research_scope']
anns={k:[] for k in meta}
def ann(ds,label,typ,target,scale,rater,time,avail,rel,p,scope='실제 JSON/코드',follow='필요',research='미션 적합성 별도 평가'):
 anns[ds].append(dict(zip(annfields,[label,typ,target,scale,rater,time,avail,rel,p,src(p),'E1',scope,D,'명시 범위 높음',follow,A,research])))
for lab,n in [('category',34),('dimension',14),('semantic',73),('vision',1000)]:
 ann('horikawa',lab,'개별 라벨명이 아닌 공식 feature group',f'{n}개 특징; 개별 명칭 E0','미확인','개별 평정자/집계 상세 미확인','영상 단위; 시간별 여부 미확인','공식 파일 위치만 확인; figshare 차단','미확인','horikawa_Tutorials.ipynb','공식 튜토리얼','개별 명칭/척도/타깃·집계 방식 실물 검증','semantic/vision은 감정 ground truth 아님' if lab in ['semantic','vision'] else '라벨 실물 검증 전 개념 확정 금지')
cols=json.loads((E/'ds004872/derivatives/Annot_AfterTheRain_stim.json').read_text())['Columns'];seen={}
for p in (E/'ds004872').rglob('*recording-*_stim.json'):
 j=json.loads(p.read_text());
 for lab in j.get('Columns',[]):seen.setdefault(lab,(p,j))
excluded={'Jaw','EyesOpen','Breathing','Movement','Consequences'}
for lab,(p,j) in sorted(seen.items()):
 sub=j.get(lab,{});levels=sub.get('Levels',{});scale='숫자 범위 미확인; '+('high='+levels.get('high','')+'; low='+levels.get('low','') if levels else '극값 정의 없음')
 ann('emofilm',lab,'단일 항목 연속 주석','문항별 Instructions에 정의; 타깃 동일성 가정 금지',scale,'별도 주석 참가자 44명 중 항목별 일부','1초','consensus 50열 포함' if lab in cols else '원항목 존재; consensus 제외','QC 코드의 기본 agreement는 Pearson r; 수치 미확인',str(p.relative_to(E)),follow='숫자 시계열·척도·항목별 평정자 수',research='제외 주제 관련 항목도 데이터 사전의 사실 기록에만 사용')
for lab in ['rating_relevance','rating_happy','rating_sad','rating_afraid','rating_disgusted','rating_warm','rating_engaged']:
 ann('spacetop',lab,'alignvideo 클립 후 평정','해당 클립의 평정 응답; 문항 원문 추가 확인','0–100; Barely at all–Strongest imaginable','동일 fMRI 참가자','클립 후 event','actual TSV/JSON 확인; n/a 다수 존재','미확인','ds005256/task-alignvideo_events.json',follow='전체 결측·문항·반복 신뢰도',research='미션 제외 주제는 연구축으로 확장하지 않음')
for lab in ['response_angle','response_label','block_condition','mentalizing_level']:
 ann('spacetop',lab,'shortvideo 과제 변수','인물에 대한 과제별 판단; 시청자 일반 감정과 다름','response_angle 0–180; 나머지 JSON Levels/라벨','동일 fMRI 참가자','시행','JSON 확인','미확인','ds005256/task-shortvideo_events.json',research='과제 사실 기록만; 제외 의제 연구로 확장 금지')
for lab in ['iscorrect','RT','missingdata']:
 ann('nsd',lab,'행동/품질 변수','정서 annotation 아님','RT ms; 기타 실제 TSV 미확인','fMRI 참가자','시행','공식 예제 코드 계약만','감정 평정 신뢰도 해당 없음','nsdexamples/matlab/example09_behavioraldata.m','공식 코드',research='정서 ground truth로 사용 금지')
for ds,rows in anns.items():csvwrite(ds+'/annotation_dictionary.csv',rows,annfields)

opps={
'horikawa':'''| 작업 | 판정 | 필수 전제와 통제 |
|---|---|---|
| category/dimension/semantic/vision의 조건부 encoding·분산 비교 | 가능(자료 접근 후) | 원라벨 척도·중복 내용·nested CV·fold 내 정규화 확인; 정확도만으로 정서 계산 주장 금지 |
| 비디오 모델 특징으로 의미·동작과 정서 정보 분해 | 가능(영상 권리/실물 확보 후) | 원영상 길이/이벤트 길이 분리, 저수준·객체·장면·동작 통제, 내용 그룹 분할 |
| 참가자 간 일반화 | 가능(자료 접근 후) | 동일 영상으로 평가하면 개인 일반화와 새로운 내용 일반화를 구별; N=5 불확실성 |
| 시간별 감정 전이 모델 | 추가 annotation 필요 | 시계열 정서 측정 확인 안 됨; raw BOLD만으로 정서 궤적 정답을 만들 수 없음 |
| 생성 자극으로 뇌의 정서 인과성 검증 | 현재 불가능 | 생성 영상에 대한 새 신경 측정 필요; 기존 관찰 자료의 in-silico 예측은 인과 증거 아님 |

최소 단위는 자극 사건이며 독립 분할 그룹은 영상 내용 중복 집합이다. 15 dupidx 처리와 실제 stimulus ID 매핑부터 감사한다. 보관 자료로 지금 실행할 수 있는 것은 metadata 검산이며, 신경 모델은 아직 실행하지 않았다.''',
'emofilm':'''| 작업 | 판정 | 필수 전제와 통제 |
|---|---|---|
| 1 Hz consensus와 영상/BOLD 시간 정렬 | 가능(실물 확보 후) | film onset을 scanner time에 더하고 HRF·평정 지연을 분리; resampling은 새 정보 생성이 아님 |
| 영화별 정서 정보의 맥락 일반화 | 가능(자료 접근 후) | leave-film-out; contiguous time random split 금지; 영화·인물·장면 특징 통제 |
| 참가자별 개인 정서 궤적 모델 | 추가 annotation 필요 | 외부 44명 consensus를 각 fMRI 참가자 개인 궤적으로 대체하지 않음 |
| annotation uncertainty를 반영한 표상 비교 | 가능(원평정 확보 후) | QC 전후 평정자를 분리, agreement 함수 실제 분기 확인, 별도 검증 평정자 활용 |
| 영상-청각의 독립 기여와 결합 | 가능(영상·audio 확보 후) | 모달리티별 특징·상호작용을 held-out film에서 검증; 단순 높은 성능을 통합 메커니즘으로 해석 금지 |

독립 추론 단위는 영화/참가자/평정자에 걸친 계층이다. 14영화의 수천 timepoint를 독립 표본으로 세지 않는다. 원판정에 실패하면 시간구조 주장보다 측정 정렬과 불확실성 연구로 축소한다.''',
'spacetop':'''| 작업 | 판정 | 필수 전제와 통제 |
|---|---|---|
| alignvideo의 클립 후 정서 점수와 신경표상 | 가능(자료 접근 및 유효 cohort 확정 후) | n/a 결측, 영화별 길이, rating phase 운동 반응, 자극 identity 통제 |
| 공통 영상 기반 참가자 표상 정렬 | 가능(실제 공유 coverage 확인 후) | 117 metadata 행을 유효 N으로 가정하지 않음; 영상×참가자 coverage 표 먼저 |
| 짧은 영상 대 다른 task의 감정 수치 직접 비교 | 현재 불가능 | shortvideo는 다른 타깃·문항·척도이며 범위 밖 의제 포함; 변수명만 ontology 정렬 금지 |
| 영상 내부 감정 시간 궤적 추정 | 추가 annotation 필요 | alignvideo 후평정을 전체 시간에 복제하면 측정 오류 |
| Horikawa와 동일 감정 코드 전이 | 외부 데이터/추가 annotation 필요 | 실제 공유 자극·동일 문항 없음; 독립 공동 평정 또는 검증된 측정 모형 필요 |

첫 파일럿 전 중단 기준은 유효 평정/공유 영상 coverage 부족 또는 cohort 선정 근거 부재다. 데이터셋에 존재한다는 이유로 제외 주제 과제를 연구축으로 승격하지 않는다.''',
'nsd':'''| 작업 | 판정 | 필수 전제와 통제 |
|---|---|---|
| 시각 encoding·정렬의 신뢰도 기준선 | 가능(자료 접근 후) | 반복 ID를 train/test 분리, betas 포맷 스케일 확인, noise ceiling 비교 |
| 정서 데이터의 시각/의미 confound 제거를 위한 시각 모델 | 가능(방법 전이) | NSD에서 훈련한 공간을 감정 개념 정답으로 선언하지 않음; task/domain 이동 평가 |
| 독립 감정 점수 supervised decoding | 추가 annotation 필요 | 공식 검토 자료에서 해당 ground truth 미확인; AI 점수는 독립 정답 아님 |
| 자연 영상 시간 감정 궤적·청각 통합 | 현재 불가능 | 정지 이미지 자료의 제시 순서를 자연 동영상 맥락으로 재해석하지 않음 |
| 생성형 재구성의 감정 의미 평가 | 추가 annotation 필요 | 실제 fMRI 자극 정서 평정·생성물 독립 평정 필요; reconstruction만으로 원 정서 보존 주장 금지 |

이미지 ID(73k), 개인 10k 인덱스, masterordering, 세션 시행을 분리한다. 반복 일부의 평균이나 shared1000을 다른 역할에 중복 배정하는 누수를 감사한다. NSD 사전학습 모델의 NSD 평가는 데이터 오염 가능성을 먼저 기록한다.'''}
for ds,t in opps.items():write(ds+'/modeling_opportunities.md',f'# {ds} 모델링 기회\n\n{common}\n\n아래는 E3 연구 설계 제안이며 수행 결과가 아니다.\n\n'+t+'\n\n출처: 같은 폴더 verified_spec.md 및 metadata_inventory.csv. needs_followup: 본체 접근·정렬·신뢰도 확인. confidence: 조건부 설계 수준. origin_agent: '+A)

write('cross_dataset_matrix.md','''# 데이터 간 비교의 가능 범위

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
''')

# papers: canonical schema plus provenance extras
base=['paper_id','title','authors','year','venue','doi_or_arxiv','official_url','version','source_verified','full_text_access','discussion_access','domain','axis_tags','original_rq','dataset','stimulus','brain_measurement','model_method','training_objective','main_findings','scientific_contribution','limitations','future_directions','future_direction_source_location','transfer_idea','relevant_datasets','novelty_risk','evidence_level','agent','verification_date']
papers=[]
for pid,title,authors,year,venue,doi,url,ds,method,transfer in [
('A01-HORIKAWA2020','The neural representation of visually evoked emotion is high-dimensional, categorical, and distributed across transmodal brain regions','Tomoyasu Horikawa; Alan S. Cowen; Dacher Keltner; Yukiyasu Kamitani','2020','iScience','10.1016/j.isci.2020.101060',src('ds002425/dataset_description.json'),'Horikawa','공식 코드의 regularized encoding/decoding 및 RSA','E3: 내용 중복·주석 불확실성을 통제한 조건부 표현 비교'),
('A01-EMOFILM2025','Emo-FilM: A multimodal dataset for affective neuroscience using naturalistic stimuli','Elenor Morgenroth; Stefano Moia; Laura Vilaclara; Raphael Fournier; Michal Muszynski; Maria Ploumitsakou; Marina Almató-Bellavista; Patrik Vuilleumier; Dimitri Van De Ville','2025','Scientific Data','10.1038/s41597-025-04803-5',src('ds004892/dataset_description.json'),'Emo-FilM','공식 데이터 문서/주석 consensus 처리 코드','E3: 영화별/평정자별 불확실성을 보존한 시간 정렬'),
('A01-SPACETOP2024','A massive multimodal fMRI dataset unifying naturalistic processes with a rich array of experimental tasks','Heejung Jung 외; 전체 인용 표기는 공식 HowToAcknowledge 참조(Authors 배열과 일부 이름 불일치)','2024','bioRxiv','10.1101/2024.06.21.599974',src('ds005256/dataset_description.json'),'Spacetop','공식 BIDS/HED 데이터 기술','E3: 결측과 task 차이를 통제한 영상 기반 참가자 일반화')]:
 row={k:'미확인' for k in base};row.update(paper_id=pid,title=title,authors=authors,year=year,venue=venue,doi_or_arxiv=doi,official_url=url,version='공식 저장소 서지의 정식판' if year!='2024' else '2024 preprint; 최신 출판 상태 미확인',source_verified='서지 및 공식 저장소 확인; 본문은 확인 안 함',full_text_access='아니오; 프록시 403',discussion_access='아니오',domain='데이터·정서신경과학',axis_tags='P;Q;S;T',original_rq='공식 제목/데이터 기술 범위 확인; 논문 서술의 세부 RQ 미확인',dataset=ds,stimulus='영상(세부는 데이터 감사 참조)',brain_measurement='fMRI',model_method=method,training_objective='논문 원문 미확인',main_findings='논문 결과 원문 미확인; 제목을 실험 결과 검증으로 대체하지 않음',scientific_contribution='공식 배포 구조를 직접 확인; 논문 주장 원문 검증 미완료',limitations='본 에이전트의 데이터 감사는 별도 보고서; 저자 한계 미확인',future_directions='저자 제안 미확인',future_direction_source_location='Discussion 접근 없음',transfer_idea=transfer,relevant_datasets=ds,novelty_risk='새로운 분석 제안의 선행연구 중복 검색 미완료',evidence_level='E2',agent=A,verification_date=D)
 row.update(source_scope='공식 dataset_description/README 서지; 데이터 코드 E1은 별도 보고',counted_verified_bibliography='예',needs_followup='원문 Discussion·방법·서지 불일치 확인',confidence='서지 식별 높음; 논문 결과 미검증');papers.append(row)
csvwrite('papers.csv',papers,base+['source_scope','counted_verified_bibliography','needs_followup','confidence'])
csvwrite('paper_candidates.csv',[{'title':'A massive 7T fMRI dataset to bridge cognitive neuroscience and artificial intelligence','official_source':src('nsddatapaper_README.md'),'status':'공식 README에서 논문 제목만 확인; 전체 저자/연도/DOI 미검증','counted':'아니오','evidence_level':'E2(제목·공식 코드 연결만)','needs_followup':'공식 원문 서지 확보','verified_on':D,'origin_agent':A}])

write('round1_independent_report.md','''# Agent01 독립 조사 1차 보고

2026-11-12. 기존 EmoBrain 및 타 Agent의 조사 결과는 열람하지 않았다. 사실의 근거는 각 dataset/verified_spec.md, 실제 원본과 URL/해시는 evidence/에 있다. 코드와 metadata 문서는 E1, 논문 서지 확인은 E2, 아래 연구 아이디어는 모두 E3, 논문 본문/Discussion과 확보하지 않은 값은 E0이다. 공통 스키마는 MISSION의 30필드를 사용하고 provenance 4필드를 추가했다.

## 가장 중요한 독립 발견

1. Horikawa 305개 이벤트 전수 파싱: 5명 각각 61런/2,196 자극행. actual `stim_index` 대 README `stimulus_index` 불일치. 모든 이벤트 ID가 고유해도 원분석은 15개 내용 중복 인덱스를 제거한다. ID 수와 내용 독립성을 혼동하면 안 된다.
2. Horikawa raw 8세션과 처리본 코드의 5/7/6/5/5 묶음은 별개다. Python tutorial에는 nested CV가 없다. 간단한 재현 코드 실행은 원논문 결과 재현 증거가 아니다.
3. Emo-FilM 30명 fMRI와 44명 연속 평정은 별도 코호트다. 14영화/50개 1Hz consensus와 fMRI 참가자의 clip validation은 같은 관측값이 아니다. Description–Instructions 극성 충돌도 발견했다.
4. Emo-FilM `lins_ccc` 기본 분기는 Pearson r다. 변수명 `ccc`만으로 측정 척도를 확정하면 오류다. 코드 실행 없이 실제 신뢰도 숫자는 보고하지 않는다.
5. Spacetop 소개 N=101 대 현행 raw 117행; 5개 예시 alignvideo 런의 28개 평정 중 유효값은 0–27개로 다르다. 현재 metadata 행 수로 유효 분석 N을 정하지 않는다.
6. NSD 공식 예제에는 8명, 세션 [40,40,32,30,40,32,40,30], 750시행/세션, masterordering→subjectim 매핑 및 noise ceiling 코드가 있다. 감정 ground truth는 이번 공식 자료에서 확인하지 못했다.

## 미해결 질문 5개(E3, 저자의 Discussion 제안 아님)

| ID | 질문 | 직접 근거·판별 조건 |
|---|---|---|
| U1 | 감정 관련 표현의 일반화는 새로운 영상 내용에도 유지되는가? | Horikawa 원 코드 dupidx + 이벤트 전수 검산; ID 분할 대 내용 그룹 분할 비교 |
| U2 | 시간 감정 구조로 보이는 신호가 annotation/HRF 지연에 의해 만들어지는가? | Emo-FilM 1Hz StartTime=0 + 실제 film onset; 독립 지연모형과 hold-out film 비교 |
| U3 | 합의가 낮은 항목에서 모델-뇌 불일치가 신경정보의 차이인가 측정 오차인가? | Emo-FilM 원평정/QC 코드 + NSD 반복 기반 ncsnr 공식 코드; 독립 평정자 평가 |
| U4 | 영상별 정서 관련 뇌 분산이 task와 평정 결측에 따라 바뀌는가? | Spacetop task-specific events + 유효평정 차이; 완전사례 선택편향과 missingness 모형 비교 |
| U5 | 서로 다른 annotation ontology를 정렬한 뒤에도 공유 감정 관련 뇌정보를 검증할 수 있는가? | Horikawa feature groups + Emo-FilM exact labels + Spacetop trial ratings; 공동 독립 평정 없으면 확증 유보 |

## 방법 기회 5개(E3)

| ID | 방법 | 새 판별력·실패 조건 |
|---|---|---|
| M1 | 내용 중복 그래프 기반 group CV | 수치 ID와 실제 내용 독립성을 분리; 영상 미확보 시 dupidx만 보수적으로 적용 |
| M2 | annotation–BOLD 결합 지연의 민감도 분석 | 고정 HRF/평정 지연 가정에 의존하는 시간 효과를 분리; 신경 인과 지연으로 해석 금지 |
| M3 | 평정자 계층 모형과 독립 검증 평정자 | consensus 평균의 확실성과 individual signal을 분리; 숫자 원평정 확보 전 보류 |
| M4 | 참가자×영화 coverage와 결측 메커니즘 감사 | 높은 점수의 완전사례만 남기는 편향 검출; 결측 원인이 미확인이라면 선택모형 민감도 보고 |
| M5 | 측정 오차를 반영한 조건부 representational comparison | 모델 정확도 대 감정 정보 잔차의 구별; 신뢰도 상한보다 작은 차이를 과장하지 않음 |

## 타 분야 전이 5개(E3, 특정 최신 모델 성과 검증 아님)

| 원 분야 | 가져오는 계산 원리 | 정서·뇌 질문 | 자료·통제 |
|---|---|---|---|
| 데이터베이스 | 타입이 있는 join·provenance 추적 | annotation과 BOLD 연결 오류가 표상 차이를 만드는가? | Horikawa stim_index 및 NSD 2단계 index; join assertion |
| 컴퓨터 비전 | perceptual deduplication | 새 내용으로 일반화되는 정서 관련 정보인가? | Horikawa 영상 내용 중복; ID baseline 비교 |
| 시계열 분석 | 상태공간/관측지연 분리 | 정서 시간 변화와 측정 지연을 구분할 수 있는가? | Emo-FilM 1Hz/scan onset/HRF; leave-film-out |
| 계량심리 | 측정 불변성·계층 평정자 모형 | 데이터 간 공유 감정 표상이 측정 체계의 차이를 넘는가? | 세 영상 데이터의 실제 문항; 독립 공통 평정 필요 |
| missing-data 통계 | 결측 메커니즘 민감도 | 뇌-정서 관계가 응답 가능한 참가자/자극에만 나타나는가? | Spacetop response_value n/a + cohort 정리 |

## 예상 밖의 연결 3개(E3)

- C1. **원영상 중복 제거 ↔ 감정 표상 기하학**: Horikawa 공식 duplicate 코드와 NSD 공식 trial→image mapping을 연결한다. 같은 내용이 여러 ID로 남으면 표상 거리가 안정적으로 보일 수 있다. 내용 독립 일반화가 남지 않으면 공통 감정 기하학 주장을 축소한다.
- C2. **평정 합의 선별 ↔ noise ceiling**: Emo-FilM QC 코드와 NSD export_noiseceiling을 연결한다. 신뢰도를 올리는 선별과 평가를 같은 표본에서 하면 비교 기준 자체가 달라진다. 독립 평정자/반복 자료에서 불확실성을 재추정한다.
- C3. **BIDS 이벤트 타입 ↔ 측정 이론**: Horikawa onsets, Emo-FilM film-relative validation, Spacetop post-clip rating을 연결한다. 시간 좌표와 측정 대상이 다른 세 변수를 같은 label 행렬로 만들 수 없다는 사실이 모델 구조 선택을 결정한다. 단순 이름 유사도 정렬은 기각한다.

## 숨겨진 가정 3개와 반론

| 가정(E3) | 왜 취약한가 | 검증 기술·수정 |
|---|---|---|
| 같은 stimulus ID 분할이면 독립이다 | Horikawa 내용 중복 제거 목록은 서로 다른 ID를 포함한다 | 영상 fingerprint/독립 audit; 그룹 분할; 의미 일반화 claim 축소 |
| consensus가 모든 참가자·시점의 정답이다 | Emo-FilM 다른 코호트·타임베이스; Spacetop 사후평정 | 계층 관측모형·개별 검증; 개인 정서 궤적 주장은 보류 |
| 데이터셋 이름이 같으면 N·schema·신뢰도 정의가 고정이다 | Spacetop 101/117, Horikawa 필드 불일치, CCC/CORR 차이 | commit 고정·파일 전수검산·코드 분기 감사; 버전별 결과 보고 |

이는 해당 논문 저자가 명시적으로 채택한 가정이라고 단정한 것이 아니라, 재사용 분석에서 발생할 수 있는 가정이다.

## 신규 Sub-axis 3개

| axis_id | name/definition | type_tags | representative_papers / models | open_questions / transfer | dataset_feasibility |
|---|---|---|---|---|---|
| P-A01 | 자극 독립성의 의미적 단위: ID/파일/내용의 차이를 표현 | Construct / Stimulus; Inference / Measurement; Structure / Dynamics | Horikawa2020 서지 + 공식 dupidx; perceptual fingerprint/group CV | U1; 데이터 중복 감사 전이 | Horikawa 영상 확보 필요 |
| Q-A01 | 시간 좌표와 관측지연: 영화·스캐너·평정 시계의 분리 | Neural; Structure / Dynamics; Inference / Measurement | Emo-FilM2025 서지 + BIDS 이벤트; 상태공간 관측모형 | U2; 시계열 식별성 전이 | Emo-FilM 실물 주석/신경신호 필요 |
| X-A01 | 주석 불확실성과 공유 표상: 타깃/평정자/척도 차이를 모형화 | Construct / Stimulus; Model / Method; Inference / Measurement | Emo-FilM·Spacetop 공식 metadata; 계층 측정모형 | U3/U5; 측정 불변성 전이 | 자료 간 독립 공동 평정 추가 필요 |

각 행 confidence=E3 조건부, origin_agent=Agent01, last_verified=2026-11-12. 모델은 계산 원리 후보이며 체크포인트 실재 검증을 완료한 특정 제품이 아니다. 연계 대상은 Agent05(시간·멀티모달), Agent07(기하학/정보), Agent12(식별성·누수), Agent03(내용 중복/시각 통제)이다. 1차 독립성 때문에 실제 결과 교환은 아직 하지 않았다.

## 여덟 탐색 질문에 대한 검토

1. 아직 검증하기 어려웠던 이유: 서로 다른 ID/시간 좌표/평정 집계와 자극 접근 제약이 비교를 방해한다는 E3 진단. 과거 연구가 시도하지 않았다는 역사적 단정은 미검증.
2. 최근 가능해진 것: 공식 Python 재현·BIDS 메타데이터·공개 처리 코드로 독립성·타임베이스·관측모형을 명시적으로 감사할 수 있다. 최신 AI 성능 증가는 이 Agent가 검증하지 않았다.
3. 틀릴 수 있는 가정: ID 독립성, consensus 보편성, schema 고정성.
4. AI가 더 포착할 수 있는 것: 영상 내용·동작·시간 맥락의 조합 후보(E3). 감정 효과와 구별하는 통제가 필요.
5. AI가 놓칠 수 있는 것: 영상·라벨·측정 오차로 설명되지 않는 신경 분산. 이를 곧바로 감정 고유 신호로 선언하지 않음.
6. 타 분야 전이: 데이터베이스 타입, 측정 불변성, missingness, perceptual deduplication.
7. 기존 데이터의 다른 용도: 높은 정확도 달성보다 어떤 단위에서 일반화가 사라지는지 판별하는 실험.
8. 신경 계산 이해의 변화: 감정 관련 신경표상 주장이 내용/측정/시간 좌표에 견고한지 판별. 부정 결과도 해당 설명의 범위를 제한한다.

## 강한 반론과 실제 남은 작업

가장 큰 반론은 metadata 감사만으로 새로운 정서 신경 계산을 발견했다고 할 수 없다는 점이다. 수정은 각 감사가 판별하는 경쟁 설명과 독립 평가를 명시하고, 실제 신경/영상/주석 접근 후에만 결과를 주장하는 것이다. 이 보고서의 E3 기회는 신규성 검증을 통과한 RQ가 아니다.

서지 확인 3편, NSD 제목 확인 후보 1편; 논문 본문·Discussion 직접 확인 0편. 정확한 Horikawa 라벨/척도, 영상 접근 권리, Emo-FilM 숫자 annotation, Spacetop 유효 cohort·전체 결측·preprocessing, NSD 공식 매뉴얼/완전 서지/감정 측정 확인이 남는다. 네트워크 403을 우회하지 않았으며 100편 목표 달성을 주장하지 않는다.
''')
write('STATUS.md','''# Agent01 상태

- 날짜/담당: 2026-11-12 / Agent01 Dataset & Metadata Forensics.
- 완료: 지침 확인, 독립 공식 조사, 4개 데이터셋별 verified_spec/metadata_inventory/annotation_dictionary/modeling_opportunities, cross_dataset_matrix, 독립 보고서 5문제·5방법·5전이·3연결·3가정·3subaxis·8질문 검토.
- 완료: Horikawa 305개 이벤트 전수 감사 및 15개 dupidx 근거 보존; Emo-FilM label JSON·타임베이스·QC 코드 감사; Spacetop 현행 cohort/schema/결측 예시; NSD 공식 코드 경로 계약.
- 문헌: 3개 서지확인 E2 행; NSD 후보 1개 별도. 논문 본문/Discussion 0개. papers.csv는 공통 30필드+4 provenance 필드.
- 미완료: 데이터 본체/영상/특징 숫자·라이선스 세부·신경 분석 실행·최신성/신규성 반례 검색. 결과나 Discussion을 만들지 않음.
- 차단: Cell/Nature/bioRxiv/NSD 사이트/figshare는 프록시 403. 공식 GitHub와 raw 접근만 이용; 차단 우회 없음.
- 독립성: EmoBrain 및 타 Agent 조사 결과 미열람. 타 Agent/공유 파일 수정 없음.
- evidence/fetch_log.jsonl: 모든 HTTP 다운로드의 URL/상태/시간/해시. evidence/repos/: 저장소 snapshot/파일목록. evidence/derived_audit_counts.json: 실제 이벤트 검산. audit_counts.py: 재실행 절차.
''')
print('보고서 작성 완료',sum(1 for p in R.rglob('*') if p.is_file() and '.git' not in p.parts))
