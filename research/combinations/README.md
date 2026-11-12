# 연구 조합 기록

2026-11-12 seed `20261112`로 실제 무작위 교차 조합30개를 추출했다. 최신 A–X taxonomy에서 유형3개를 뽑고 유형별 Axis를 추출했다. 중복 Axis/동일3축집합만 재추첨하여34회 시도에서30개를 얻었다. 과학적으로 부적합한 조합은 재추첨하지 않았다.

- [원 추출·전체 시도·taxonomy 해시](random_draws.json)
- [조합별 의미·근거·반증·판정](random_evaluated.csv): 발전13, 수정 필요8, 보류4, 기각5.
- 실제 구현: `scripts/draw_research_combinations.py`, `scripts/evaluate_random_combinations.py`.
- Agent12가 seed 재현·hash·전체 판정 보존을 독립 확인했다. [감사](../agents/12_adversarial_review/combination_curation_audit.md).

문헌 기반12전략 조합과 최종 통합 행렬은 Round4 수정 후보에 연결하여 작성한다. 무작위 조합의 발전 판정은 신규 RQ 확정이 아니다. 기존 문헌 경로와 같은 질문이면 병합하고, U/W의 측정 공백·과도한 인과·단순 모델교체는 보류/기각 사유로 보존한다.

사용자가 다섯 자료를 보유한다는 전제로 진행한다. 상세 스키마 확인은 실제 분석 조건이며 조합 생성의 선행 차단 조건이 아니다.
