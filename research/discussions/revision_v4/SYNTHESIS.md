# 실제 제안·비판·수정의 결과

이번에는 제안 역할7개와 데이터 담당을 실행했다. 원안10개를 보존하고 서로의 파일을 읽은 비판을 실제 메시지로 전달했다. 저자는 반론에 답하고 수정했다. 아래는 그 교환을 요약한 것이며, 과거 v1~v3 토론을 이번 검토로 계산하지 않는다.

| 원안 | 실제 비판의 요점 | 저자 수정과 최종 위치 |
|---|---|---|
| D02/03/04/05/06-A | 같은 MC 질문을 다섯 연구로 세고 있다. 심상 정서 판독은 이미 예상된 결과이며 일반적인 내용 보존·감도 저하와 구별해야 한다. | 다섯 저자가 한 연구로 통합에 동의. 정서·내용 관계의 상대적 변화가 주 분석, 시각 ROI/latent는 보조 분석. |
| D02-B | 혼합 자료의 valence 성공과 범주 내부 순서 오류를 구분해야 한다. 서로 다른 대상 자료를 받은 적응 모델 비교는 공정하지 않다. | 동일 대상 영상·정답으로 적응을 비교하도록 수정. 최종 검토에서 기존 맥락 의존성 주장을 넘어설 기여가 부족해 저자도 주력 보류에 동의. |
| D03-B | 시각 특징을 거치며 정보가 약해진다는 일반 압축 문제 이상으로 어떤 중요한 판단이 달라지는지 불명확하다. | 생성 영상 주장을 철회하고 실제 feature 판독으로 한정. 독립 연구 보류. |
| D04-B | 캡션의 정보 부족과 정렬 학습의 손실을 나눠야 한다. 구체적인 신경 대비를 정해도 그 경유가 필요한 과학 질문이 남지 않는다. | 원 캡션·원 시각·정렬 표현을 비교하도록 개선했지만 독립 연구 보류. D03-B와 합쳐 숫자로 구제하지 않기로 실제 합의. |
| D07-A | 집계 점수 동률은 개인의 범주 경계가 아니다. 연속 모델이 국소 변화를 잘 맞힌다고 그 변화가 없는 것은 아니다. | 척도·주석 정의를 먼저 확인. 국소 신경 구별의 존재와 모델 설명을 분리. 파일럿 후보로 유지. |
| D08-A | 서로 다른 평가 영상의 난도나 한 대비의 gain 차이로 ROI 순위가 바뀔 수 있다. 공통/영역별 모형이 같은 예측을 하면 비교가 안 된다. | 같은 평가 영상에서 학습 내용군만 변경. 여러 대비의 상대적 보존을 예측하고 공유·가변 요소를 명시. 파일럿 후보로 유지. |

## 원본과 실제 전달 기록

- 원안 해시: [첫5개](../../revision_v4/INITIAL_SOURCES.json), [지각 전용3개](../../revision_v4/PERCEPTION_SOURCES.json), [추가2개](../../revision_v4/ADDITIONAL_SOURCES.json).
- 데이터 심사: [첫8개](../../agents/01_dataset/revision_v4_data_review.json), [추가2개](../../agents/01_dataset/revision_v4_additional_data_reviews.json).
- MC 통합: [다섯 저자의 실제 합의](../../agents/02_affective_neuroscience/revision_v4_integration_agreement.json).
- B 후보 최종 비판: [검토와 실제 저자 교환](../../agents/06_frontier_ai/revision_v4_final_contribution_review.json).
- D07 비판: [정서 담당](../../agents/02_affective_neuroscience/revision_v4_review_D07.json), [시스템 담당](../../agents/08_systems_neuroscience/revision_v4_peer_review_D07.json).
- D08 비판: [AI 담당](../../agents/06_frontier_ai/revision_v4_review_D08.json), [기하 담당](../../agents/07_geometry_information/revision_v4_peer_review_D08.json).
- 최종 저자 파일과 해시: [출처 목록](../../revision_v4/FINAL_AUTHOR_SOURCES.json). 각 카드의 `response_log`에서 어떤 비판을 어떻게 반영했는지 볼 수 있다.

## 합의가 의미하지 않는 것

파일럿 후보로 남겼다고 신규성·효과·검정력이 검증된 것은 아니다. 반대로 기존 관측에서 중요한 표현 관계를 구별할 수 있다면 정서 전용 회로, 모든 시각·의미 정보와의 독립, 새 인과 실험을 요구하지 않았다. 데이터 적합성과 과학적 기여를 별도로 판단했다.

정서 조합 발상은 [데이터 검토](../../agents/01_dataset/revision_v4_composition_feasibility.md)와 [과학 검토](../../agents/02_affective_neuroscience/revision_v4_composition_science_review.md)에 별도로 남겼다.
