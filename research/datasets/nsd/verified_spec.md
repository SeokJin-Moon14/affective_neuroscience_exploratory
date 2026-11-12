> Coordinator 통합 사본. [Agent01 원본](../../agents/01_dataset/nsd/verified_spec.md). 문서의 evidence 경로는 `agents/01_dataset/` 기준이며 실제 데이터 본체 확보를 뜻하지 않는다.

# NSD 검증 명세

검증일: 2026-11-12 · 담당: Agent01 Dataset & Metadata Forensics.

E1은 직접 읽은 공식 코드·데이터 문서·실제 텍스트 메타데이터 범위의 검증이다. 논문 본문을 읽었다는 뜻이 아니다. E2는 공식 문서의 서지/요약 확인, E3는 본 에이전트의 추론, E0는 미확인이다. 전체 데이터 본체·영상·모델은 다운로드하거나 실행하지 않았다. 원문/URL/응답/해시는 `../evidence/fetch_log.jsonl`, 저장소 파일 목록은 `../evidence/repos/*_tree.txt`에 보존했다.

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
