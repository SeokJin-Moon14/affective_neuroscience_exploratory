> Coordinator 통합 사본. [Agent01 원본](../../agents/01_dataset/horikawa/modeling_opportunities.md). 문서의 evidence 경로는 `agents/01_dataset/` 기준이며 실제 데이터 본체 확보를 뜻하지 않는다.

# horikawa 모델링 기회

검증일: 2026-11-12 · 담당: Agent01 Dataset & Metadata Forensics.

E1은 직접 읽은 공식 코드·데이터 문서·실제 텍스트 메타데이터 범위의 검증이다. 논문 본문을 읽었다는 뜻이 아니다. E2는 공식 문서의 서지/요약 확인, E3는 본 에이전트의 추론, E0는 미확인이다. 전체 데이터 본체·영상·모델은 다운로드하거나 실행하지 않았다. 원문/URL/응답/해시는 `../evidence/fetch_log.jsonl`, 저장소 파일 목록은 `../evidence/repos/*_tree.txt`에 보존했다.

아래는 E3 연구 설계 제안이며 수행 결과가 아니다.

| 작업 | 판정 | 필수 전제와 통제 |
|---|---|---|
| category/dimension/semantic/vision의 조건부 encoding·분산 비교 | 가능(자료 접근 후) | 원라벨 척도·중복 내용·nested CV·fold 내 정규화 확인; 정확도만으로 정서 계산 주장 금지 |
| 비디오 모델 특징으로 의미·동작과 정서 정보 분해 | 가능(영상 권리/실물 확보 후) | 원영상 길이/이벤트 길이 분리, 저수준·객체·장면·동작 통제, 내용 그룹 분할 |
| 참가자 간 일반화 | 가능(자료 접근 후) | 동일 영상으로 평가하면 개인 일반화와 새로운 내용 일반화를 구별; N=5 불확실성 |
| 시간별 감정 전이 모델 | 추가 annotation 필요 | 시계열 정서 측정 확인 안 됨; raw BOLD만으로 정서 궤적 정답을 만들 수 없음 |
| 생성 자극으로 뇌의 정서 인과성 검증 | 현재 불가능 | 생성 영상에 대한 새 신경 측정 필요; 기존 관찰 자료의 in-silico 예측은 인과 증거 아님 |

최소 단위는 자극 사건이며 독립 분할 그룹은 영상 내용 중복 집합이다. 15 dupidx 처리와 실제 stimulus ID 매핑부터 감사한다. 보관 자료로 지금 실행할 수 있는 것은 metadata 검산이며, 신경 모델은 아직 실행하지 않았다.

출처: 같은 폴더 verified_spec.md 및 metadata_inventory.csv. needs_followup: 본체 접근·정렬·신뢰도 확인. confidence: 조건부 설계 수준. origin_agent: Agent01 Dataset & Metadata Forensics
