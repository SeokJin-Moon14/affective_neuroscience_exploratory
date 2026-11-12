> Coordinator 통합 사본. [Agent01 원본](../../agents/01_dataset/spacetop/modeling_opportunities.md). 문서의 evidence 경로는 `agents/01_dataset/` 기준이며 실제 데이터 본체 확보를 뜻하지 않는다.

# spacetop 모델링 기회

검증일: 2026-11-12 · 담당: Agent01 Dataset & Metadata Forensics.

E1은 직접 읽은 공식 코드·데이터 문서·실제 텍스트 메타데이터 범위의 검증이다. 논문 본문을 읽었다는 뜻이 아니다. E2는 공식 문서의 서지/요약 확인, E3는 본 에이전트의 추론, E0는 미확인이다. 전체 데이터 본체·영상·모델은 다운로드하거나 실행하지 않았다. 원문/URL/응답/해시는 `../evidence/fetch_log.jsonl`, 저장소 파일 목록은 `../evidence/repos/*_tree.txt`에 보존했다.

아래는 E3 연구 설계 제안이며 수행 결과가 아니다.

| 작업 | 판정 | 필수 전제와 통제 |
|---|---|---|
| alignvideo의 클립 후 정서 점수와 신경표상 | 가능(자료 접근 및 유효 cohort 확정 후) | n/a 결측, 영화별 길이, rating phase 운동 반응, 자극 identity 통제 |
| 공통 영상 기반 참가자 표상 정렬 | 가능(실제 공유 coverage 확인 후) | 117 metadata 행을 유효 N으로 가정하지 않음; 영상×참가자 coverage 표 먼저 |
| 짧은 영상 대 다른 task의 감정 수치 직접 비교 | 현재 불가능 | shortvideo는 다른 타깃·문항·척도이며 범위 밖 의제 포함; 변수명만 ontology 정렬 금지 |
| 영상 내부 감정 시간 궤적 추정 | 추가 annotation 필요 | alignvideo 후평정을 전체 시간에 복제하면 측정 오류 |
| Horikawa와 동일 감정 코드 전이 | 외부 데이터/추가 annotation 필요 | 실제 공유 자극·동일 문항 없음; 독립 공동 평정 또는 검증된 측정 모형 필요 |

첫 파일럿 전 중단 기준은 유효 평정/공유 영상 coverage 부족 또는 cohort 선정 근거 부재다. 데이터셋에 존재한다는 이유로 제외 주제 과제를 연구축으로 승격하지 않는다.

출처: 같은 폴더 verified_spec.md 및 metadata_inventory.csv. needs_followup: 본체 접근·정렬·신뢰도 확인. confidence: 조건부 설계 수준. origin_agent: Agent01 Dataset & Metadata Forensics
