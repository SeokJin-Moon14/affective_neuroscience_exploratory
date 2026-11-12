# Round5 실제 대립 가설 토론

Coordinator가 확정한 discussions/round05_assignments.json과 research_questions/shortlist.json을 읽는다. 각 유망 질문에는 서로 다른 Agent의 제안자·회의적 비판자·데이터통계 검토자를 지정한다. 이전 라운드의 가상 발언을 새로 쓰지 않고 자신의 입장을 독립적으로 작성한다.

자기 폴더 round05_debate.json/md만 작성한다. JSON 루트 `role`, `read_files`, `positions`, `limitations`.

각 position 필수: `proposal_id`, `rq_id`, `debate_role`(제안자/회의적비판자/데이터통계검토자), `claim`, `best_evidence`(canonical 배열), `weakest_assumption`, `discriminating_prediction`, `judgment`(추진/수정/조건부/기각), `required_change`, `unresolved_disagreement`, `resource_feasibility`.

제안자는 왜 이 비교가 새 신경과학 질문인지, 비판자는 가장 강한 대안 설명과 이미 알려진 부분을, 데이터통계 검토자는 관측 단위·측정 신뢰도·split·null·검정력·실제 모델지원·조건부 착수를 검토한다. 모두 긍정·부정 결과의 해석과 어떤 증거가 자기 판단을 바꿀지 적는다.

세 입장이 모인 후 Coordinator가 실제 결과를 제안자에게 전달하고, 제안자는 `round05_rebuttal.json/md`에서 각 비판을 수용·반박·미해결로 기록한다. Coordinator가 최종 추진범위·조건·기각사항·소수의견을 합성한다. 빠른 만장일치를 목표로 하지 않는다.
