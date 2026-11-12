# MC — 공식 공개 자료와 관측 범위 확인

MC는 사용자가 보유한 Mind Captioning을 뜻한다. 이번에 [저자 공식 저장소](https://github.com/horikawa-t/MindCaptioning)를 찾아 직접 확인했다. 공식 링크는 Horikawa (2025), *Mind captioning: Evolving descriptive text of mental content from human brain activity*, DOI 10.1126/sciadv.adw1464, OpenNeuro **ds005191 v1.0.2**와 연결된다. 사용자가 보유한 릴리스·처리본과 일치하는지는 아직 파일로 대조하지 않았다.

## 직접 읽은 자료

- [공식 README](evidence/official_README.md): 논문·OpenNeuro·전처리 자료·캡션·영상 출처 링크.
- [BIDS README](evidence/bids_README), [dataset_description](evidence/dataset_description.json): 여섯 참가자, `trainPerception`, `testPerception`, `testImagery`; 이벤트 열과 평정 설명.
- [처리 자료 README](evidence/data_README.md): trainPerception 2,108 samples, testPerception 72×5 repetitions, testImagery 72×5 repetitions의 파일 구조. 이는 문서에 적힌 크기이며 실제 MAT 배열을 열어 센 것이 아니다. testImagery 줄의 괄호 설명에는 test perception이라고 쓰인 부분이 있지만 BIDS README는 imagery로 구별한다.
- [캡션 원본 CSV](evidence/caption_ck20.csv)를 실제 파싱했다. `video_id,description`, 43,920행, 영상 ID 2,196개, ID마다 20개 캡션을 확인했다. [재계산 결과](evidence/caption_schema_check.json). 공식 문서는 crowdsourcing으로 수집한 캡션이라고 설명한다.
- [코드 설명](evidence/code_README.md): 뇌→의미 특징→문장 생성 경로와 encoding/decoding 결과의 역할을 확인했다. 코드를 실행하거나 결과 배열을 읽은 것은 아니다.

## 연구 설계에서 쓸 수 있는 것

실제로 영상을 보는 조건과 심상 조건, 영상에 연결된 사람의 내용 설명, 공개 처리 자료의 의미·시각 특징이 있다. 공식 문서는 DeBERTa-large 의미 특징과 TimeSformer 시각 특징을 명시한다. 자극 내용·언어적 표현·시각적 표현과 뇌 반응의 관계를 기존 관측에서 검토할 출발점이다.

Horikawa와 MC는 모두 Cowen–Keltner (2017)의 영상 출처를 명시한다. MC 캡션은 원 영상 ID 1–2196을 쓰고 BIDS는 `stimID`와 `stimLabel`을 구별한다. 공통 출처만으로 사용 영상·제외 목록·ID 매핑·정서 주석의 일치를 확정하지 않는다. 실제 분석에는 그 대응을 확인해야 한다. 사람의 영상 내용 캡션과 뇌에서 생성한 문장은 출처가 다르며, 캡션 자체가 정서 정답은 아니다.

## C06-C에 사용할 수 없는 관측

BIDS README의 testImagery `accuracy`와 `vividness`는 참가자가 평가한 0–5점이다. **특정 세부를 정확히 보았는지의 객관적 판별, 이후 변형 유인 자극 선택, 그 오류의 방향을 제공한다는 근거가 없다.** 따라서 MC에 심상이 있다는 사실로 C06-C의 기억 정확성 결론을 검증할 수 있다고 하면 안 된다.

영상·뇌 MAT/NIfTI·의미 특징 본체와 사용자 보유본은 이 작업에서 열지 않았다. 공식 문서, 공개 캡션 CSV, BIDS 설명을 직접 확인한 범위와 구별한다. 원자료를 다시 받거나 사용자의 컴퓨터 공간을 사용할 필요는 없다. [공식 파일 접근 기록](evidence/primary_files_fetch.json).
