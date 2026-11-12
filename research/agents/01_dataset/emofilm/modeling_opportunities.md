# emofilm 모델링 기회

검증일: 2026-11-12 · 담당: Agent01 Dataset & Metadata Forensics.

E1은 직접 읽은 공식 코드·데이터 문서·실제 텍스트 메타데이터 범위의 검증이다. 논문 본문을 읽었다는 뜻이 아니다. E2는 공식 문서의 서지/요약 확인, E3는 본 에이전트의 추론, E0는 미확인이다. 전체 데이터 본체·영상·모델은 다운로드하거나 실행하지 않았다. 원문/URL/응답/해시는 `../evidence/fetch_log.jsonl`, 저장소 파일 목록은 `../evidence/repos/*_tree.txt`에 보존했다.

아래는 E3 연구 설계 제안이며 수행 결과가 아니다.

| 작업 | 판정 | 필수 전제와 통제 |
|---|---|---|
| 1 Hz consensus와 영상/BOLD 시간 정렬 | 가능(실물 확보 후) | film onset을 scanner time에 더하고 HRF·평정 지연을 분리; resampling은 새 정보 생성이 아님 |
| 영화별 정서 정보의 맥락 일반화 | 가능(자료 접근 후) | leave-film-out; contiguous time random split 금지; 영화·인물·장면 특징 통제 |
| 참가자별 개인 정서 궤적 모델 | 추가 annotation 필요 | 외부 44명 consensus를 각 fMRI 참가자 개인 궤적으로 대체하지 않음 |
| annotation uncertainty를 반영한 표상 비교 | 가능(원평정 확보 후) | QC 전후 평정자를 분리, agreement 함수 실제 분기 확인, 별도 검증 평정자 활용 |
| 영상-청각의 독립 기여와 결합 | 가능(영상·audio 확보 후) | 모달리티별 특징·상호작용을 held-out film에서 검증; 단순 높은 성능을 통합 메커니즘으로 해석 금지 |

독립 추론 단위는 영화/참가자/평정자에 걸친 계층이다. 14영화의 수천 timepoint를 독립 표본으로 세지 않는다. 원판정에 실패하면 시간구조 주장보다 측정 정렬과 불확실성 연구로 축소한다.

출처: 같은 폴더 verified_spec.md 및 metadata_inventory.csv. needs_followup: 본체 접근·정렬·신뢰도 확인. confidence: 조건부 설계 수준. origin_agent: Agent01 Dataset & Metadata Forensics
