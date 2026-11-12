# 연구 진행 상태

기준일: 2026-11-12 (Asia/Seoul). 현재 **Stage4 실제 교차토론 진행: Round3 완료**. 사용자 요청에 따라 남은 산출물 전체를 중간 승인 없이 수행 중이다. Stage2 세부 검증은 병행·후속 보완이며 Axis 진행을 차단하지 않는다. 전체 미션 완료 아님.

최신 사용자 지시: **Horikawa·Emo-FilM·Mind Captioning·NSD·Spacetop을 이미 보유하며 Axis부터 진행한다.** 사용자 보유, 현재 환경의 파일 접근, 정확한 스키마 검증을 구별한다. GitHub 공개 백업 허용은 유지한다.

| Stage | 실제 상태 |
|---|---|
| 0 독립 초기화 | 완료. 첨부 미션 먼저 읽음, 새 폴더·한국어·전용 작업영역. EmoBrain 내용 미접근. |
| 1 독립 탐색 | 12개 실제 전문 Agent, 두 Wave, 각 역할 보고서 저장. 본문/서지/코드의 검증 범위는 개별 명시. |
| 2 데이터·문헌 | 부분 완료. 기존4종 공식 메타데이터 감사. 5종 사용자 보유 확인; Mind Captioning 명세는 미확인. 원본111행→고유103편→엄격 서지확인100편·보류3편. 지정 본문/한계 등 직접확인27편. 실제 분석에 필요한 필드·추가 원문·최신성 보강은 후속 조건으로 기록. |
| 3 Axis | **통합 v1 완료.** A–X24축, 12역할36개 원 제안 등록, 8개 탐색 묶음, 수동 교차연결8개. Agent07·10·12 실제 검토 반영. 22개 상위축 활성; U·W 근거 공백 명시. 36개를 고유 RQ 수로 집계하지 않음. |
| 4 교차 토론 | Round1 독립 보고, Round2 12역할 정보교환·60개 원 후보, Round3 120개 실제 비판 완료. 모든 후보에 다른 두 역할 검토·8체크. 수정94/유지14/보류12. Round4–5 이어서 수행. |
| 5 조합 | 수동 문헌 연결8개, seed20261112 실제 무작위30개 추출·조합별 판정 완료(발전13/수정8/보류4/기각5). 최종 RQ와의 중복 통합은 후속. |
| 6–8 RQ·신규성·10개 제안 | 미완료. 독립 보고서의 E3 질문을 확정 landscape/shortlist로 집계하지 않음. |
| 9 기존 자원 실현성 | 미수행. EmoBrain 자원 미접근. |
| 10 파일럿3·최종종합 | 미완료. 현재 보고서는 초기 조사 종합. |

주요 보고서: [Axis Encyclopedia](axis_map/AXIS_ENCYCLOPEDIA.md), [교차연결8개](axis_map/cross_connections.md), [통합 판정](axis_map/integration_review.md), [보유 데이터 연결](datasets/ownership_and_readiness.md), [문헌 집계](literature/README.md), [초기 보고](synthesis/initial_report.md).

## 다음 작업과 남은 확인

추가 원문 확보에는 일부 사이트의 기존 프록시403 제약이 남는다. 네트워크 허용 초안은 저장됐으나 아직 적용되지 않았다. **이 제약은 기존 근거를 이용하는 Axis·토론·개념 조합의 차단 사유가 아니다.** 이번 통합은 새 네트워크 조회 없이 기존 연구 근거를 사용했다.

다음: **실제 교차토론 Round2–5 → 조합·RQ → 신규성 감사 → 상세제안·파일럿**. 필요한 문헌·스키마 확인은 후보별로 병행한다. Axis 근거 목록에 연결한 별도 보류 출처 A12-P02는 기존103편 집계 밖의 보조 출처이며 확정 문헌 수를 늘리지 않았다. 외부 제출·메시지·영상 신청, 모델·뇌 분석은 수행하지 않았다.

## 검산

- 12개 역할 papers.csv의 미션 필수30필드 확인, 추가 provenance 열 보존.
- DOI/arXiv·정규화 제목으로 중복 병합, 유사 제목 추가 검사, 보류 이유 기록.
- Horikawa 305개 이벤트의 수치·헤더를 Coordinator와 별도 Agent가 재계산.
- 통합 발견 문서의 사실검사 지적을 반영. 기록은 agents/03_vision_decoding/coordinator_fact_check.md.
- 재실행: scripts/merge_literature.py → scripts/finalize_inventory.py. 새 근거 확보 시 수동 보류 판정부터 갱신할 것.
- Axis 재생성: scripts/build_axis_registry.py → scripts/build_axis_connections.py. 필수12필드·12역할·36개 원본 대응·출처ID·유형·상위축·교차연결을 검사했다.
- 공개 원격 백업의 성공 정본은 GitHub 브랜치 `backup/LAST_SUCCESS.json`이다. 새 데이터 본체를 업로드한 것은 아니다.
