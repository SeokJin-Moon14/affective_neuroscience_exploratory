# Round4 비판 응답과 예상 밖의 연결

자기 원본 후보5개, Round3에서 받은 실제 비판 두 묶음, discussions/round_03/collected.json을 읽고 비판 ID를 명시하여 응답한다. 수정·보류·기각·유지를 기록하고 소수 의견을 지우지 않는다.

자기 폴더 round04_revision.json/md만 작성한다. JSON 루트 `role`, `read_files`, `responses`(원 후보5개 각각), `new_connections`(최소2개), `revised_candidates`(원5개 전체), `limitations`.

각 response: `candidate_id`, `critique_ids`, `accepted_changes`, `contested_points`, `final_status`, `reason`.

각 new_connection: `connection_id`(UC역할2자리-번호), `source_field`, `original_computational_goal`, `imported_structure`, `new_neural_question`, `why_not_same_as_round2`, `candidate_ids`, `source_papers`(2개이상), `assumptions`, `discriminating_test`, `failure_interpretation`. 기존 조합을 그대로 반복하지 말고 다른 학문의 계산목적 구조를 전이한다. 실제 대상 문헌 범위와 E3 신경 전이를 구별한다.

revised_candidates는 Round2의 모든 필수필드를 보존하고 `revision_history`, `reverse_search_query_en`(해당 대비를 겨냥하는 영어 역검색어8–15단어), `research_role`(과학RQ후보/방법후보/보류/기각), `shortlist_recommendation`(최상위로 제안할 자기후보 최대2개+이유)를 추가한다. 새로운 연결이 원 질문을 실질적으로 바꾸었다면 구체적으로 명시한다. 정의되지 않은 잔차비율·관측등가·조건부독립을 측정결과처럼 쓰지 않는다.

각 수정 후보에 `evaluation`을 추가한다. 다음10키마다 `score`(1–5), `reason`(구체적 한 문장), `uncertainty`, `source_papers`를 기록: novelty, neuro_importance, ai_necessity, data_feasibility, rigor, falsifiability, interpretability, generalization, technical_feasibility, exploration_value. 점수는 최종 Coordinator 판단의 입력이며 자동 가중합으로 선정하지 않는다. 서지·스키마·checkpoint 미확인을 반영하고 높은 신규성을 확정 사실로 쓰지 않는다. 기존 모델 교체로 충분하면 AI필요성 점수를 낮추고 그 결과를 보존한다.

사용자는 전체완료를 요청했다. 스키마 미확인은 실제 분석 착수 조건이며 이 문헌·토론 작업의 선행 차단 조건이 아니다. 최종 파일럿은 실행 계획이며 인간 뇌 분석을 이미 수행했다고 주장하지 않는다.
