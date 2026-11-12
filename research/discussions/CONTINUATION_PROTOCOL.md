# 전체 후속 작업 수행 규약

2026-11-12 (Asia/Seoul). 최신 사용자 요청: **남은 작업을 끝까지 진행하고 전체 완료 후 알린다.** 사용자 중간 검토를 단계 진입 조건으로 두지 않는다. 공개 GitHub 단계별 저장은 계속한다. 데이터 보유5종과 미확인 스키마를 구별하며, 상세 스키마 검증을 문헌 연구·Axis·RQ 생성의 차단 조건으로 사용하지 않는다.

## 실제 토론 순서

Round1 원본12역할은 이미 완료됐다. Round2 정보교환 → Round3 다른 두 역할에 대한 비판 → Round4 비판에 대한 응답과 새 연결 → Round5 유망 후보별 제안자·비판자·데이터통계 검토자·Coordinator 판정 순서를 실제로 실행한다. 이전 Axis 검토를 이 라운드로 소급 계산하지 않는다. 역할 Agent가 없으면 새 Agent에게 해당 역할 원본 보고서와 본 규약을 읽혀 재개하며 실제 Agent 매핑을 기록한다.

각 역할은 자기 `agents/NN_.../` 폴더의 round02_exchange.json/md, round03_critique.json/md, round04_revision.json/md, round05_debate.json/md만 쓴다. 공유 결과·Git 백업은 Coordinator만 쓴다. 같은 파일을 동시에 수정하지 않는다.

## Round2 공통 형식

자기 분야 밖의 실제 역할 보고서 최소2개를 읽고 두 계산 원리/질문을 수입한다. 독립 후보 방향5개를 제시하되 모델명·데이터셋만 바꾸지 않는다. 원본 문헌 문제와 새 신경 질문의 차이를 명시한다. 후보당 기존 문헌의 canonical Pxxx ID 최소2개 또는 문헌+확인된 공식 문서; 근거 없음은 E0로 남긴다.

JSON 루트: `role`, `read_files`, `imports`(최소2개), `candidates`(5개), `limitations`.

각 candidate 필수: `candidate_id`(C역할2자리-번호2자리), `title`, `axis_ids`(ASxx 배열), `research_question`, `neural_target`, `external_principle`, `model_application`, `scientific_question`, `assumption_challenge`, `main_hypothesis`, `alternative`, `measurable_contrast`, `falsification`, `baseline`, `dataset_plan`, `missing_conditions`, `source_papers`(Pxxx 또는 DOC-xxx 배열), `closest_prior_ids`, `what_is_new`, `novelty_risk`, `conceptual_signature`(관측대상/조작/경쟁설명), `eight_questions`(미션0.1의 여덟 질문에 각각 구체적 짧은 답), `status`.

미확인 새 문헌으로 수량을 채우지 않는다. 최소 원논문ID/링크는 기존 literature/papers.csv와 axis_map/reference_catalog.csv에 있다. 원문·공식 코드·서지 확인은 구별한다. 모델의 feature 편집이 인간 뇌 인과를 입증한다고 하지 않는다. 뇌신호 전체의 예측 향상과 독립 정서 대비를 구별한다.

## 분석과 계획의 경계

최종 산출물은 문헌 기반 연구 제안과 구현 계획이다. 원자료 분석을 실제 수행하지 않았다면 수행했다고 쓰지 않는다. 모델 체크포인트·경로·스키마가 미확인일 때 실제 식별 가능한 확인 절차와 fallback을 적고 준비 상태를 조건부로 표시한다. 신규성 역검색이 현재 네트워크에서 제한되면 기존 문헌 역대조와 시도한 외부 쿼리 범위를 보존하고 세계 최초를 확정하지 않는다.
