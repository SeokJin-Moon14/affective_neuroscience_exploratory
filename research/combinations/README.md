# 실제 조합 실험

문헌 기반 12개 전략과 별도의 실제 무작위 30개를 [전체42개 표](combination_matrix.csv)에 모았다. 문헌 전략은 미션의 12개 생성 경로를 각각 검토했다. 기존 Axis 통합의 수동 교차연결8개와 별도 산출물이다.

무작위는 seed20261112로 유형3개를 뽑고 유형별 Axis 하나씩 추출했다. 중복 Axis/동일3축 집합만 재추첨해 34회 시도 중 30개를 채택했다. 전체 가능한3축 집합에 대한 균등추출은 아니다. [원 추출과 해시](random_draws.json), [과학적 판정](random_evaluated.csv), [독립 감사](../agents/12_adversarial_review/combination_curation_audit.md)를 보존한다.

판정은 발전13·수정8·보류4·기각5다. 발전13개를 추가 고유 RQ13개로 세지 않는다. [내용 대응표](random_to_questions.csv)에서 이미 존재하는 질문과 병합하거나 공통 검증으로 남겼다. 이 대응은 사후 내용 비교이며 원 질문이 해당 무작위 조합에서 발생했다고 주장하지 않는다. 특히 R11/R27은 같은 오차좌표 질문으로 통합했다.

재현: scripts/draw_research_combinations.py. 보존된 실행시각은 최초 실행 기록이며 재실행 시각과 구별한다.
