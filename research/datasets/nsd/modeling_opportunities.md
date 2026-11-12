> Coordinator 통합 사본. [Agent01 원본](../../agents/01_dataset/nsd/modeling_opportunities.md). 문서의 evidence 경로는 `agents/01_dataset/` 기준이며 실제 데이터 본체 확보를 뜻하지 않는다.

# nsd 모델링 기회

검증일: 2026-11-12 · 담당: Agent01 Dataset & Metadata Forensics.

E1은 직접 읽은 공식 코드·데이터 문서·실제 텍스트 메타데이터 범위의 검증이다. 논문 본문을 읽었다는 뜻이 아니다. E2는 공식 문서의 서지/요약 확인, E3는 본 에이전트의 추론, E0는 미확인이다. 전체 데이터 본체·영상·모델은 다운로드하거나 실행하지 않았다. 원문/URL/응답/해시는 `../evidence/fetch_log.jsonl`, 저장소 파일 목록은 `../evidence/repos/*_tree.txt`에 보존했다.

아래는 E3 연구 설계 제안이며 수행 결과가 아니다.

| 작업 | 판정 | 필수 전제와 통제 |
|---|---|---|
| 시각 encoding·정렬의 신뢰도 기준선 | 가능(자료 접근 후) | 반복 ID를 train/test 분리, betas 포맷 스케일 확인, noise ceiling 비교 |
| 정서 데이터의 시각/의미 confound 제거를 위한 시각 모델 | 가능(방법 전이) | NSD에서 훈련한 공간을 감정 개념 정답으로 선언하지 않음; task/domain 이동 평가 |
| 독립 감정 점수 supervised decoding | 추가 annotation 필요 | 공식 검토 자료에서 해당 ground truth 미확인; AI 점수는 독립 정답 아님 |
| 자연 영상 시간 감정 궤적·청각 통합 | 현재 불가능 | 정지 이미지 자료의 제시 순서를 자연 동영상 맥락으로 재해석하지 않음 |
| 생성형 재구성의 감정 의미 평가 | 추가 annotation 필요 | 실제 fMRI 자극 정서 평정·생성물 독립 평정 필요; reconstruction만으로 원 정서 보존 주장 금지 |

이미지 ID(73k), 개인 10k 인덱스, masterordering, 세션 시행을 분리한다. 반복 일부의 평균이나 shared1000을 다른 역할에 중복 배정하는 누수를 감사한다. NSD 사전학습 모델의 NSD 평가는 데이터 오염 가능성을 먼저 기록한다.

출처: 같은 폴더 verified_spec.md 및 metadata_inventory.csv. needs_followup: 본체 접근·정렬·신뢰도 확인. confidence: 조건부 설계 수준. origin_agent: Agent01 Dataset & Metadata Forensics
