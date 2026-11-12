# 보유 데이터와 연구 질문의 범위

**1순위 Horikawa·MC·NSD, 2순위 Emo-FilM, 3순위 Spacetop.** 사용자가 모두 보유한다고 밝혔다. 아래는 공개 문서·코드·일부 실제 주석/이벤트를 확인한 범위이며 사용자 보유 BOLD 배열을 직접 분석한 결과가 아니다.

| 우선순위 | 자료 | 현재 확인한 관측 | 질문을 정할 때 지켜야 할 범위 |
|---|---|---|---|
| 1 | Horikawa | 짧은 영상의 fMRI, 영상별 정서 category/dimension 및 시각·의미 특징을 사용하는 공식 분석. 5명·305개 이벤트 파일을 직접 재확인. | 기존 영상의 내용·정서 주석·뇌 반응을 연결한다. 외부 평균 주석을 개인의 시행별 정서 평정으로 바꾸지 않는다. |
| 1 | MC | ds005191의 지각/심상 과제, 6명, 영상별 20개 사람 캡션. 공개 CSV 43,920행을 직접 파싱. | 내용 설명·의미 특징·뇌 표현을 연결할 수 있다. 심상 자기평가는 특정 세부의 객관적 기억 오류 자료가 아니다. |
| 1 | NSD | 정지 사진의 반복 fMRI, 시행별 beta와 행동 정확도·RT를 읽는 공식 코드. 시선 분석 코드도 있다. | 정서 주석·캡션 연결·시선 원자료의 실제 범위는 확인 대상이다. 기존 관측으로 새 시선·회상·자극 조작을 대신하지 않는다. |
| 2 | Emo-FilM | 자연 영화 fMRI와 외부 연속 정서 consensus, 별도 clip validation 평정. | 영화의 정서·내용 변화와 뇌 반응을 확장 검토한다. 외부 consensus를 개인의 연속 정답으로 보지 않는다. |
| 3 | Spacetop | alignvideo의 영상과 참가자별 clip 후 0–100 평정 구조. | 후순위 확장 자료다. clip 평정을 연속 정답이나 원 PINES 문항으로 대체하지 않는다. |

주력 RQ는 표의 자료 이름을 붙이는 것으로 성립하지 않는다. **핵심 결론에 필요한 관측이 해당 자료에 있어야 한다.** v3의 기억 정확성·정보 순서 조작·편집 장면 뇌 반응·원 PINES 측정 비교는 이 조건을 충족했다고 확인하지 못했으므로 현재 선정에서 제외했다.

[이전 선정의 정정과 기준](../revision_v4/DATA_FIT_REVIEW.md) · [Horikawa·Emo-FilM·Spacetop의 직접 근거](../agents/01_dataset/priority_recheck.md) · [NSD 직접 근거](../agents/03_vision_decoding/dataset_priority_nsd.md) · [MC 직접 근거](mind_captioning/verified_spec.md).

Horikawa와 MC의 공통 영상 출처는 연결 가능성의 근거다. 그러나 자극 ID·제외 목록·처리본 대응을 확인하기 전에 자동으로 같은 행으로 합치지 않는다. NSD에서 AI가 만든 정서 점수도 인간 정서 정답으로 취급하지 않는다. 새 주석이나 새 측정이 필요하면 기존 자료로 가능한 것으로 표시하지 않는다.

[MC–Horikawa 원ID 연결과 학습/시험 중복의 실제 검산](../agents/01_dataset/revision_v4_data_bridge.md) · [현재 RQ와 자료 연결](../proposals/README.md).
