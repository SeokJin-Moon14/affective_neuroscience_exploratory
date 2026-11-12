# Axis 통합 v1

[Axis Encyclopedia](AXIS_ENCYCLOPEDIA.md): A–X 24개 상위축, 12역할의 36개 하위축, 8개 탐색 묶음. 2026-11-12 실제 교차 검토를 반영했다. 36개는 원 제안 등록 수이며 고유 RQ 수가 아니다. U·W의 현재 근거 공백은 명시했다.

- [통합 JSON](integrated_subaxes.json) / [CSV](integrated_subaxes.csv): 필수12필드, 경쟁 설명, 반증 관측, 대조, 분석 조건.
- [교차연결](cross_connections.md) / [CSV](cross_connections.csv): 수동 문헌 기반 연결8개. 무작위 추출은 아직 미실행.
- [통합 판정·검토 이력](integration_review.md), [상위축](taxonomy.csv), [원본 대응](source_crosswalk.csv), [출처 목록](reference_catalog.csv), [구조 검사](validation.json).
- [보유한 다섯 데이터셋의 연결](../datasets/ownership_and_readiness.md).

원본24축은 seed_taxonomy.csv, 초기30개는 candidate_subaxes.json에 보존했다. 추가6개를 포함한 source_proposals.json은 원문 추적용이다. 재생성: `python scripts/build_axis_registry.py` 다음 `python scripts/build_axis_connections.py`.

Stage3 통합 v1 완료이며 전체 연구 완료가 아니다. 하위축은 E3 가설이고, 실제 데이터 분석·신규성 역검색·토론 Round2–5는 후속 작업이다. 데이터 상세 검증은 Axis 진행을 막지 않는다.
