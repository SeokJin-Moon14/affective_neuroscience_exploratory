# Top10 카드 작성 규약

이 규약은 실제 Round5 세 입장을 수신한 뒤 적용한다. 각 담당자는 원 질문·Round3/4 수정·Round5 제안자/비판자/통계검토자의 실제 기록을 읽고, 소수 의견과 남은 식별 한계를 보존한다. 세계 최초·실험 성공을 주장하지 않는다.

자기 Agent 폴더에 `proposal_RPxx.json`을 작성한다. Coordinator가 공유 proposals/로 렌더링한다. 공통 파일을 직접 수정하지 않는다. JSON 필수:

`proposal_id`, `rq_id`, `title`, `core_question`, `scientific_motivation`, `idea_provenance`, `prior_literature`, `closest_prior_and_novelty`, `dataset_and_metadata`, `computational_framework`, `neural_target`, `proposed_analyses`, `competing_explanations`, `falsifiable_outcomes`, `scientific_and_modeling_contribution`, `limitations_and_risks`, `smallest_informative_pilot`, `priority`, `debate_response`.

16개 본문 항목은 미션§10을 그대로 충족한다. `prior_literature`는 최소5개 배열이며 각 항목 `paper_id`(canonical), `contribution`, `limitation`, `access_scope`를 가진다. 가능한 범위에서 직접 관련 논문과 해당 분석에 실제 필요한 방법론을 선택하며 무관한 인용으로 수량을 채우지 않는다. 공식URL은 Coordinator가 기존 근거표에서 연결한다. 서지/코드/본문 확인을 구별한다.

다른 본문 필드는 구체적인 한국어 문장·목록·객체로 작성할 수 있다. 단 다음 내용을 반드시 포함한다.

- 데이터: 이미 보유한5종 중 정확히 어떤 관측 단위를 쓸지. 원문에서 확인한 실제 필드와 새로 만들 분석 계약 필드를 구별. 파일 경로·스키마가 미확인이면 해당 조건을 남김.
- 모형: 입력/출력, frozen backbone 또는 작은 baseline, 적응·loss·checkpoint 식별 범위. 고정 backbone 간 비교만으로 학습목표 인과를 주장하지 않음.
- 분석: 같은 독립 test의 비교, 강한 baseline, confound·자기상관·측정오차, nested 선택, 검정단위·다중비교·신뢰도, 부정/동등성 해석.
- 차별점: 가장 가까운 기존 논문과 정확히 다른 대비, 여전히 겹치는 부분, 접근 제한 때문에 확인하지 못한 신규성.
- 결과: 긍정·부정·혼합 결과 모두 설명. 새로운 결과를 얻었다고 쓰지 않음.
- 파일럿: 최소정보를 주는 하위집합·실행 순서·확대/수정/중단 기준. 실물 확인 전 실행 준비완료라고 표시하지 않음.
- 우선순위: 과학적 잠재력·독창성·단기실현성·종합 판단을 구분하고 새 주석/새 뇌측정 필요 여부를 명시.

`debate_response`는 실제 Round5 비판·통계 의견을 항목별로 수용/반박/미해결로 답한다. 별도 `round05_rebuttal.json/md`에도 자기 담당 카드의 응답을 기록한다. 루트 `role`, `responses`; 각 response `proposal_id`, `critic_role`, `critique_summary`, `response`, `decision`, `remaining_disagreement`.

자원 참고는 pilots/RESOURCE_AND_MODEL_PLAN.md, 데이터 근거는 datasets/DATASET_INTELLIGENCE_REPORT.md. 현재 GPU 실행은 확인되지 않았고, baseline/cache 단계와 고비용 feature 추출을 나눈다. 코드 공개와 checkpoint load 성공을 혼동하지 않는다.
