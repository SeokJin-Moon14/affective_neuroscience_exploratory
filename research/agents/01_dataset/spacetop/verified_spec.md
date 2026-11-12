# Spacetop 검증 명세

검증일: 2026-11-12 · 담당: Agent01 Dataset & Metadata Forensics.

E1은 직접 읽은 공식 코드·데이터 문서·실제 텍스트 메타데이터 범위의 검증이다. 논문 본문을 읽었다는 뜻이 아니다. E2는 공식 문서의 서지/요약 확인, E3는 본 에이전트의 추론, E0는 미확인이다. 전체 데이터 본체·영상·모델은 다운로드하거나 실행하지 않았다. 원문/URL/응답/해시는 `../evidence/fetch_log.jsonl`, 저장소 파일 목록은 `../evidence/repos/*_tree.txt`에 보존했다.

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
