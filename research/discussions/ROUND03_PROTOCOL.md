# Round3 실제 상호 비판

자기 Round2와 배정된 두 역할의 round02_exchange.json/md를 실제 읽는다. 각 대상 역할의5개 후보 전부, 총10개 후보를 검토한다. 이름만 비슷하다는 중복 판단이 아니라 **관측 대상·조작·추정량·경쟁 설명·반증 결과**를 비교한다. 각 후보에 아래 여덟 질문을 실제로 적용한다.

1. 선행문헌이 이미 답한 부분과 남은 부분은 무엇인가?
2. 단순 모델/benchmark 교체인가?
3. 독립 정서 대비인가 전체 BOLD 예측 향상인가?
4. 보유자료의 어떤 미확인 필드가 실제 분석에 필요한가?
5. 자극 ID·motion·semantics·HRF로 설명되는가?
6. 예측·대응·모델 기전·인간 뇌 인과의 수준을 혼동하는가?
7. 더 강한 baseline/판별 대조가 있는가?
8. 부정적 결과에서 무엇을 배울 수 있는가?

자기 폴더 round03_critique.json/md만 작성한다. JSON 루트 `role`, `read_files`, `reviews`, `round_limitations`.

각 review 필수: `review_id`(R3-검토자2자리-대상candidateID), `target_candidate_id`, `target_role`, `decision`(수정/보류/기각/유지), `checks`(위8개 질문에 대한 짧은 구체적 판정), `strongest_objection`, `required_revision`, `better_discriminating_test`, `negative_result_value`, `source_papers`(canonical배열), `unresolved_disagreement`.

불확실성이 있다는 이유만으로 기각하지 않는다. 수정 가능한 판별 설계를 제안한다. 단순QC만 남으면 방법후보로 분리할 것을 권고한다. 모든 후보를 똑같은 일반론으로 비판하지 않는다. 미검증 세계최초나 새 논문 실재를 만들어내지 않는다.
