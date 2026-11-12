# 검증 문헌과 접근 범위

2026-11-12 기준.

| 집계 | 수 |
|---|---:|
| 원본 행(역할별110+Coordinator1) | 111 |
| 중복 제거 고유 후보 | 103 |
| 서지·출처 확인 | 100 |
| 서지 충돌/누락으로 목표에서 제외 | 3 |
| 논문 본문 또는 지정 절 직접 확인 | 27 |
| Discussion·Limitations·Conclusion 지정 절 확인 | 27 |
| 저자 명시 후속방향 기록 | 25 |

- [verified_papers.csv](verified_papers.csv): 엄격 집계에 포함한100편. 원문100편 확인을 뜻하지 않는다.
- [pending_verification.csv](pending_verification.csv): Spacetop·PID의 저자 표기 충돌, e-prop의 연도 미확인 등3편.
- [papers.csv](papers.csv): 고유 후보103편, 보류 포함.
- [papers_all_evidence.csv](papers_all_evidence.csv): 역할별110행과 Coordinator 추가검증1행 및 원본 경로.
- [discussion_mining.csv](discussion_mining.csv): 직접 확인27편의 접근 위치와 저자 기록/E3 전이 분리.2편은 명시적 미래방향 추가 추출 없음.

DOI/arXiv 또는 정규화 제목으로 병합하고 유사 제목도 검사했다. preprint와 정식본의 연결은 원 Agent 기록을 함께 보존했다. 서지 일부 누락이나 공식 출처 내 충돌을 수량 충족을 위해 묵인하지 않았다. Snoek·EmoPathway 등 다른 보류 후보는 각 역할 원본에 남아 있으며103편 집계 밖에 있다. NSD는 Coordinator가 공식 eLife XML의 bib6 참고문헌으로2021 preprint 서지를 추가 대조해 포함했다(nsd_bibliography_evidence.json). NSD2022 정식판의 최종 서지·원문은 미확인이고 두 버전을 별도 연구로 세지 않았다.

원문 전체 정독을 주장하지 않는다. 지정 본문·한계 절만 읽은 경우를 포함한다. E1 공식 코드 검증과 논문 본문 접근은 다르다. 최신성·신규성 전수 검색은 수행되지 않았고 GitHub 접근 가능한 자료로 편중되어 있다.

재병합은 scripts/merge_literature.py 다음 scripts/finalize_inventory.py 순서로 실행한다. 새 근거가 생기면 보류 사유와 수동 판정을 먼저 갱신해야 한다.

최종 탐색 연결: [영역·연도 편중과 공백](COVERAGE_AND_GAPS.md), [문헌 기반 E3 원 후보별 미해결 문제60행](unresolved_problems.csv), [실제 후보별 역검색과 접근 한계](novelty/README.md), [Top10 중복 반론](novelty/TOP10_REVIEW.md). 로컬103편의 실제 전수 역대조와 세계 문헌 전체의 전수 검색을 구분한다.
