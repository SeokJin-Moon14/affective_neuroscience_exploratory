# Coordinator 초기 발견 — 원증거 사실검사와 수정 권고

검사일 2026-11-12, Agent03. 대상 `synthesis/phase1_findings.md` 검사본 SHA256: `72ada5ce703f86e653227a44b38c302f5c7fc666de2658d3409ec0c988f20e19`. 아래 줄 번호는 이 검사본 기준이다. 지정된 Agent01/02 보고서와 관련 원증거를 읽었으며, 필요한 범위에서 Agent04–06의 해당 원문·코드만 대조했다. 공유 파일은 수정하지 않았다. **이 작업은 출처 사실검사이며 Round2–5 과학토론의 완료 기록이 아니다.**

## 수정 확인 완료 1 — §3의 세 측정값을 세 독립 시간축으로 취급

- **대상:** 23·25행, 제목 “세 가지 시간 좌표”, 본문 “annotation의 영화 시작 0초, 스캐너 이벤트 onset, 참가자 clip validation의 영화 내 onset은 같은 좌표가 아니다.”
- **문제:** 세 종류의 시간값/관측 단위와 세 독립 좌표계를 혼동한다. annotation의 영화 시작 기준 시각과 validation clip의 영화 파일 기준 onset은 영화 시간축에서 연결되는 값이다. 연속 주석과 clip별 validation은 측정 단위가 다르지만, 이를 서로 다른 시간 원점이라고 단정할 근거는 없다. 스캐너 onset은 별도의 시간축이다.
- **원증거:** `agents/01_dataset/evidence/ds004872/derivatives/Annot_AfterTheRain_stim.json`의 `SamplingFrequency=1.0`, `StartTime=0`; `ds004892/sub-S01/ses-1/beh/sub-S01_ses-1_task-BigBuckBunny_events.json`의 onset 설명은 정확히 “Onset of clip relative to full film file”. `emofilm_AnnotationVal.py` 79행 이후는 clip의 시간 구간을 읽고, 92행 이후 영화 길이 배열에 `n_times[tim[0]:tim[1]]=item[l]`로 배치한다. `func/*scan_acq-BigBuckBunny_events.tsv`는 film onset `93.844512590862`초를 제공한다.
- **수정 권고 제목:** “Emo-FilM: 영화·스캐너 시간축과 평정 단위를 분리한다”.
- **수정 권고 문장:** “연속 annotation은 영화 시작 기준이고, clip validation onset도 전체 영화 파일에서의 구간 위치를 뜻한다. 두 자료는 측정 단위가 다르며 영화 시간축에서 연결해야 한다. 스캐너 이벤트 onset은 별도 시간축이므로 해당 런의 film onset을 적용해야 한다. 대표 런에서는 영화 앞 rest 때문에 annotation 0초를 스캐너 0초에 붙일 수 없다.”
- annotation 표본화 간격·반응 지연·HRF 처리까지 단일 상수 이동으로 모두 해결된다고 확대하지 않는다.

## 수정 확인 완료 2 — §3의 ‘별도 코호트’가 사람의 비중복까지 뜻하지 않도록 범위 제한

- **대상:** 25행 “뇌 측정 30명과 주석 44명은 별도 코호트다.”
- **문제:** 이번에 보존된 두 `participants.tsv`에서 각각 30행·44행이라는 점은 직접 재검산했다. 두 저장소의 participant 목록과 측정 종류가 다르다는 점도 확인된다. 그러나 이것만으로 동일인의 교차 참여가 전혀 없다는 뜻의 ‘완전히 독립된 코호트’를 입증하지는 못한다. 원문 미접근 상태에서 사람 간 비중복을 확정하는 별도의 문구/대응표는 이번 검사 범위에서 찾지 못했다. 실제 독립 코호트가 아니라는 반증은 아니다.
- **원증거:** `agents/01_dataset/evidence/ds004892/participants.tsv`, `ds004872/participants.tsv`; 두 dataset_description은 참가자의 교차 동일성 여부를 설명하지 않는다. `ds004892/README.md`는 논문 URL만 담고 있다.
- **수정 권고:** “뇌 측정 자료의 참여자 목록은 30행, 주석 자료의 참여자 목록은 44행으로 별도로 제공된다. 두 자료를 개인별 대응 평정으로 합치지 않는다. 참여자 간 동일성/비중복은 원문 또는 대응 정보로 추가 확인한다.” 공식 원문에서 독립 코호트 문장을 확보하면 그 문장·위치를 근거로 현 표현을 복원할 수 있다.

## 권고 3 — §1의 코드상 중복 제외와 실제 누수 확정을 분리

- **대상:** 7·9행.
- **판정:** 핵심 수치 오류는 없다. 저장된 305개 events.tsv를 이번에도 별도 Python 파싱으로 재검산했으며, 5명 각각 61런·2,196개 `trial_type=1` 이벤트·고유 `stim_index` 2,196개·헤더 일치가 확인됐다. 공식 MATLAB `emotion2020_analysis_BATCH.m` 84–85행은 해당 목록을 “label index of duplicated videos”라고 직접 설명하고 15개를 열거한다. `perform_decoding_analysis.m` 66–67행은 `metainf.Label`로 제외한다. 2,185와의 불일치는 미해결로 보존하는 것이 맞다.
- **주의:** 공식 코드가 중복으로 지정한 목록의 존재는 확인된 사실이다. 반대로 그 목록과 raw 이벤트/실제 영상의 대응, 현재 split의 중복 누수 발생, 누수 규모는 미확인이다. ‘중복 가능성’이라는 단어로 공식 중복 목록의 존재까지 낮추거나, 공식 목록만으로 새로운 분석의 실제 train/test 누수를 확정해서는 안 된다.
- **소폭 수정 권고:** “원분석 코드는 중복 영상의 label index로 명시한 `dupidx` 15개를 제외하며, 주석은 2,196개 중 고유 2,181개라고 설명한다. 실제 처리본과 원영상의 대응은 미확인이다.”
- Python README의 nested CV 생략은 원문 31행에 있으므로 그대로 유지해도 된다. 이것은 원논문 전체의 엄밀 재현이 아니라는 뜻이며, 고정 hyperparameter의 모든 외부 평가가 자동으로 무효라는 뜻으로 확대하지 않는다.

## 권고 4 — §2의 제목을 본문과 같은 조건부 표현으로 조정

- **대상:** 15행 제목; 17–19행은 핵심 내용 유지 가능.
- **문제:** “EmoNet은 독립적인 외부 자극 기준으로 바로 쓸 수 없다”만 따로 읽으면 모든 데이터에서 외부 검증이 불가능하거나 Horikawa의 모든 평가 시행이 EmoNet 학습에 들어갔다고 오인할 수 있다. 본문은 이미 원영상 풀 공유와 개별 ID 중복 미확인을 적절히 나눈다.
- **원증거:** `agents/02_affective_neuroscience/evidence/kragel2019_fulltext.txt` 532–536행은 2,185개 영상 DB에서 137,482프레임을 추출하고 training/testing 90–10 split을 했다고 설명한다. 해당 DB는 참고문헌25의 Cowen & Keltner이다. 적은 frame 수의 범주를 제외했다는 문장도 있어 “풀의 모든 영상/프레임이 training에 사용”이라고 추론할 수 없다. `horikawa_python_readme.source` 7·16행이 같은 Cowen–Keltner 풀을 가리킨다. Kragel 원문 다음 페이지는 IAPS와 별도 trailer 평가도 기술한다.
- **수정 권고 제목:** “EmoNet–Horikawa 비교: 원자극 풀 공유를 먼저 감사한다”.
- **유지할 결론:** Horikawa를 새 자극 분포의 독립 검증으로 주장하려면 실제 model-training/frame/video ID와 평가 ID를 대조해야 한다. 풀 공유만으로 모든 개별 시행 중복이나 신경 encoding 분석 전체의 무효를 확정하지 않는다. Agent02의 ‘정확한 학습/시험 영상ID 중복 미확인’ 문구를 유지한다.

## §4 — 현 문장의 범위를 유지할 것

- 확인한 범위에서 수정이 필요한 수치 오류나 데이터 가용성 과장은 찾지 못했다. `evidence/ds005256/README` 7행의 N=101과 participants.tsv 117행을 직접 대조했다. 대표 다섯 alignvideo TSV의 유효 응답은 각각 17/28, 5/28, 1/28, 27/28, 0/28로 다시 계산됐으나 모집단 결측률이 아니다.
- **수정 금지에 가까운 유지 권고:** “현재 확인한 공식 자료에서 공통 정서 라벨 근거를 확보하지 못했다”는 의미를 유지한다. 이를 “NSD에 정서 라벨은 어디에도 없다”, “117명 분석 가능”, “alignvideo 연속 정서 주석 있음”으로 바꾸지 않는다. AI 파생 점수와 인간 측정값의 구분은 타당하다.

## 권고 5 — §5 검색 수치의 조건과 근거 종류를 보강

- **대상:** 43·45행.
- **판정:** 1시간 brain→image **57.4%는 정확하다**. `sources/mindeye2_readme.txt` 7–15행의 공식 정정과 일치하며 새 재현 결과라고 하지 않은 것도 맞다. 같은 정정표의 image→brain은 79.0%, 40시간 brain→image는 98.3%, image→brain은 98.8%다. 방향을 바꿔 기재한 추가 오류는 없다.
- **보강 권고:** 문장에 “공식 300-way 검색 평가의 정정된 해석”을 덧붙이거나 모델카드로 해당 평가 조건을 직접 연결한다. 저장된 `mindeye2_eval_cells.txt` cell11은 300후보·30회 표집·top1을 계산하므로 이를 임의 후보 수의 일반 검색 정확도로 재인용하지 않는다.
- **근거표지 수정 권고:** §5 전체가 “공식 저장소 범위”로 읽히면 Brain-Mamba도 공식 실행 저장소가 확인된 것처럼 보일 수 있다. Agent04 카드는 Brain-Mamba의 출판사 PDF 직접 확인과 공식 software 링크404를 구별한다. “공식 저장소·논문 등 모델별 지정 근거 범위” 또는 각 문단의 근거 유형으로 나누는 것이 정확하다.
- CortexMAE의 cortex-only 표현과 보간, TRIBE v2의 평균 피험자 cortical mesh 출력은 관련 공식 README/코드와 일치한다. 체크포인트 load 성공이나 개인별 예측 검증으로 확대하지 않는 현재 제한을 유지한다.

## 권고 6 — §6의 masked objective 일반화와 16프레임 표현 수정

- **대상:** 51행.
- **문제 A:** “masked video objective 자체는 과거만으로 미래를 예측하는 과제가 아니다”는 모든 mask 설계에 대한 일반 명제로 읽힐 수 있다. 마스킹 위치와 가시 문맥에 따라 미래 구간 예측을 구성할 수 있으므로, 이번에 조사한 설정에서 past-only 조건이 보장되지 않는다는 범위로 한정해야 한다.
- **수정 권고:** “확인한 일반 masked-video 학습 설정은 그 명칭만으로 과거만을 사용하는 미래 예측을 보장하지 않는다. mask와 실제 가시 문맥을 확인해야 한다.” AVE `ave_models.py` 16–17행의 `bidirectional=True`, VideoMamba `videomamba_model.py` 110·215행의 기본 `bimamba=True`, TCC README 116–122행의 counting shortcut 경고는 확인됐으므로 유지한다.
- **문제 B:** “16프레임 짧은 클립”은 입력 프레임 표본 수와 원 클립의 재생 길이를 혼동하기 쉽다. 논문의 Limitations는 **짧은 video clip에서 16프레임을 샘플링**한다고 말한다. Appendix B는 사전학습 8프레임·평가16프레임을 구분한다.
- **원증거:** `agents/05_multimodal_dynamics/evidence/videoprism_paper.txt` 530–534행, 1061–1063행. 16프레임이 모든 학습·평가의 고정 상한이라는 뜻은 아니다.
- **수정 권고:** “VideoPrism Limitations는 짧은 영상에서 16프레임을 표집하는 현재 설정 때문에 긴 영상 이해가 남은 과제라고 설명한다.” 필요하면 “Appendix B의 기본 사전학습은 8프레임, 평가는 16프레임”을 덧붙인다.
- **근거표지 수정 권고:** 이 문단은 코드와 논문 Limitations를 함께 쓰므로 “공식 구현·논문 범위”가 정확하다. 현재의 후속 문단은 새 가설로 명시되고 최초성·실현성을 유보하므로 과학적 발견을 이미 확정한 문장으로 고칠 필요는 없다.

## 미확인 데이터와 실패 응답에 대한 유지 권고

- Emo-FilM `.tsv.gz`는 실제로 `.git/annex/objects/...` 문자열이므로 시계열을 읽은 것으로 세면 안 된다. 현 §3의 미확인 구분은 적절하다.
- `lins_ccc(output="CORR")`는 `np.corrcoef`를 반환하고, `emofilm_MakeMasterfile.py` 134–136행의 해당 호출은 `output`을 생략한다. 현 §3은 코드상 경고로 정확하며 ‘배포 논문의 모든 신뢰도 값이 오기’라고 확대하지 않는다.
- 몇몇 사전 탐색 파일(`emofilm_brain_README`, `emofilm_annotation_README.md`, `spacetop_README.md`)은 `404: Not Found` 내용이다. 실제 성공 파일·원증거는 `fetch_log.jsonl`의 status와 경로로 식별해야 한다. 이번 검사에서는 성공한 participant/event JSON·TSV·정식 경로 README를 사용했다. 404 파일의 존재를 원문 확보로 계산하지 않도록 출처 링크를 유지한다.

## Coordinator 수정본 재확인

Coordinator의 수정 통지를 받은 뒤 `synthesis/phase1_findings.md`를 직접 다시 읽었다. 수정본 SHA256은 `9fc389e3d58adfe1076829c498ce762e6b03b7936d21b012ae0e332c85f3af0f`이다.

- §3 제목이 “두 시간축과 서로 다른 측정 단위”로 바뀌었고, 연속 annotation과 clip validation은 영화 시간축 공유/측정 단위 차이, scanner onset은 별도 축이라고 명시했다. **우선 수정1 해결 확인.**
- §3은 뇌 측정 목록30명·주석 목록44명으로 표현하고, 별도 목록만으로 사람이 전혀 겹치지 않는다고 확정하지 않는다는 문장을 추가했다. **우선 수정2 해결 확인.**
- 위 지적의 원문 기록은 수정 이력으로 보존한다. 나머지는 수치 오류의 정정이 아니라 범위·평가 조건·근거 종류의 명료화를 위한 권고이며, 수용/수정 여부는 이 재확인에서 확정하지 않았다.
