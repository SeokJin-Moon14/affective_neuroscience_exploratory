# 최종 독립감사 2차 — Agent12

추가7카드의 명시한 핵심 범위에서 새 high/critical 결함을 발견하지 못했다. 1차 핵심 수정5건은 해결을 확인했고 시간질문 범위는 일부 본문 정정이 남는다. 새 medium1/low1은 통합/가설 문구의 불일치이며 데이터 미확인을 자동 차단한 것이 아니다.

최신 목록: 30개 조건부 과학 RQ / 40개 방향 / 60개 원후보 대응. 숫자는 신규성·실제 분석 성공의 인증이 아니다.

## 파일별 검토 범위

- **RP01** `agents/03_vision_decoding/proposal_RP01.json`: 추가 중대 오류 없음. 같은 입력/시각표적/소형 encoder의 contrastive–regression 목표 비교와 같은 공통 pair의 정서/비정서 순서 loss가 구체화됐다. 정보삭제·뇌 학습목표 주장을 하지 않으며 방법후보 축소와 소수 의견을 보존했다.
- **RP05** `agents/04_brain_foundation/proposal_RP05.json`: 추가 중대 오류 없음. 같은 참가자/같은 자극의 독립 획득과 전처리부터 target-free인 경로를 요구한다. target perturbation·선형 mixing 경로 검사, 동일/독립 반복/타자극 비교와 입력 예산 차이를 명시한다. 현재 Horikawa 반복 확증/즉시착수로 과장하지 않았다.
- **RP08** `agents/04_brain_foundation/proposal_RP08.json`: 추가 중대 오류 없음. W-metric projection P=CG와 Gr=0, train-only residual PCA, 강한 nonlinear 평균 readout을 정의하고 H1 일반 잔차효용/H2 atlas/H3 정서선택성을 구분한다. 반복 없는 held-out prediction은 허용하되 repeat ceiling·정보전체 부재는 주장하지 않는다.
- **RP03** `agents/05_multimodal_dynamics/proposal_RP03.json`: 추가 중대 오류 없음. 경계 cue를 update/readout 모두 제공하고 exact absorbed-function control은 같은 가중치의 한 동치류로 묶는다. 효과는 유한 함수/학습예산의 예측 효용이며 실제 뇌 기억삭제로 확대하지 않는다. 외부 Fear consensus·가용시점·영화/scanner축·반복 미확인이 구분됐다.
- **RP04** `agents/05_multimodal_dynamics/proposal_RP04.json`: 추가 중대 오류 없음. 실제 시청각 제시 확인 전 Horikawa AV 주장을 하지 않고, S+R과 full X의 동일정보 가능성·운영 잔차·rank/readout 범위를 명시한다. 정서/비정서 대비의 비교 가능성과 shared라는 이름의 한계를 조건으로 남겼다.
- **RP07** `agents/09_generative_ai/proposal_RP07.json`: 추가 중대 오류 없음. 자연 후보 우선, 원본 실제 독립 반복, 새 NSD 정서 주석, 원본 참조 유지와 정확히 한 후보만 배제하는 endpoint를 명시한다. 둘다 탈락/참조 탈락/미발견을 구분하고 모델조건부 배제를 후보 실제 뇌반응과 혼동하지 않는다.
- **RP10** `agents/09_generative_ai/proposal_RP10.json`: 추가 중대 오류 없음. family-level 허용집합·독립 선별/주석검증/새 BOLD를 분리하고 원본 BOLD를 편집물에 재사용하지 않는다. 새 개발 neural projection의 비용과 동일 family의 두 editor 공통지지를 명시하며 결과를 S=1 자극묶음의 효과로 한정한다.

위7카드에서 실제 읽은 필드: title, core_question, dataset_and_metadata, computational_framework, neural_target, proposed_analyses, falsifiable_outcomes, prior_literature, closest_prior_and_novelty, scientific_and_modeling_contribution, limitations_and_risks, priority. debate_response·smallest_informative_pilot 전문을 이번2차에서 전부 재독했다고 주장하지 않는다.

세 파일럿에서는 hypotheses/evaluation/decision_points/failure_modes_and_claim_limits/readiness만 읽었다. 데이터·메모리·배열 상세 감사는 Agent01 담당 범위다.

## 추가 수정 권고

### A12-F2-01 · medium

대상: research_questions/landscape.json:RQ20.measurable_contrast와 final_audit_condition

최종 감사 조건은 이 축소를 명시했으나 measurable_contrast에는 여전히 두 사전 대비 중 (1) order-aware state 대 recency-weighted bag, (2) 미래 목표 대 과거 복원을 병렬로 적는다. 메인 필드를 읽는 독자는 (1)도 RQ20의 독립 주기여로 재집계할 수 있다. 이는 1차 중복 감사에서 합의한 수정의 본문 반영 공백이다.

- measurable_contrast에서 (2)를 유일한 primary로 재작성하고 (1)은 RQ07/RQ29와 공유하는 baseline/이차 검증임을 명시한다.
- 원래 두 대비의 문장은 round4_original_fields 등 이력으로 보존하되 최종 본문·CSV·요약은 한 계약을 사용한다.

### A12-F2-02 · low

대상: agents/03_vision_decoding/pilot_PILOT01.json:hypotheses.H1; evaluation.statistics.primary_estimand; decision_points.G4

실제 판정/통계는 양측으로 일관되지만 H1 문장만 양의 효과를 요구하는 것처럼 읽힌다. 음의 I는 contrastive의 상대적 정서 접근성 개선이라는 별도 방향이므로 효과크기와 부호를 명확히 해야 한다. 새로운 분석 결함은 아니며 가설 표기의 작은 불일치다.

- H1을 |I|>δ 또는 두 사전 방향을 모두 검정한다고 명시하고 각 부호의 뜻을 붙인다.
- 만일 양의 방향만 과학가설이라면 음의 효과는 반대 방향 결과로 보고하고 양측 탐색과 H1 지지를 구별한다. 현재 G4와 맞추려면 첫 수정이 자연스럽다.

## 1차 지적의 후속 확인

- **A12-F1-01 — 해결 확인**: RP02 final_audit_revision 및 falsifiable_outcomes.positive에 g(O), r_R, δ의 사전 양수 문턱·공동 추론을 요구하고 δ 단독은 차등 변조로 명명했다.
- **A12-F1-02 — 해결 확인**: 최신 landscape30행에서 RQ30은 없고 RQ25의 gate/error 분기로 병합됐다. candidate_crosswalk에서 C11-01/C11-02가 모두 RQ25로 연결된다. 원 ID 재사용 없이 추적한다.
- **A12-F1-03 — 해결 확인**: RQ22는 과학 landscape에서 제외되고 C06-03의 crosswalk rq_id는 비어 있으며 방법후보 이유가 보존됐다.
- **A12-F1-04 — 부분 반영·본문 정정 권고**: RQ07은 동일현재 probe의 실제 이력상태/HRF, RQ29는 현재·최근성 일치 순서 비가산, RQ20은 미래 목표로 final_audit_condition을 추가했다. RQ20 본문의 두 primary 병기는 F2-01로 남는다. RQ07/RQ29의 차이는 좁은 사전 신경 대비로 유지해야 하며 모델명/자료 수준 차이로 다시 확장하지 않는다.
- **A12-F1-05 — 해결 확인**: 숫자 목표의 강제 assert가 제거됐고 실제 counts와 quantity_targets_met 보고로 변경됐다. 60 원후보 추적 검사는 유지한다.
- **A12-F1-06 — 해결 확인**: directions.csv status가 Round4·Round5 및 최종 독립 감사 반영으로 갱신됐다.

## 최종 요약에 남겨야 할 조건

- RP03/PILOT02는 exact 동등쌍을 반드시 동등하게 복구하고 구별 불가능한 기전은 한 동치류로 남기는 규칙을 둔다. 여기의 성공은 신경 reset 구현의 고유성 증명이 아니다.
- PILOT01/03의 n=5 사람 추론과 자극 조건부 CI가 구별되고, 반복 없는 예측 경로를 가짜 반복/ceiling으로 설명하지 않는다.
- 세 파일럿은 문서 계획 완료와 데이터 mount·weight load·뇌분석 완료를 분리했다. power/최소효과 숫자는 계획 해상도로 표시하며 실제 결과로 제시하지 않는다.
- 후속 실행에서 저신뢰 대비를 보고 바꾸거나 새 family를 test 결과에 맞춰 선택해서는 안 된다는 계약이 존재한다. 실제 준수 여부는 실행 전후 검증 사항이다.
- 모든 비교가 정서 특수성을 이미 입증한 것은 아니다. RP01/RP08을 비롯해 일반 접근성/압축손실만 남으면 방법후보로 낮추는 조건을 최종 요약에서도 보존해야 한다.

## 한계

- 1차3카드와2차7카드를 합해10카드의 핵심 과학내용을 읽었지만 모든 카드의 모든 필드·최종 렌더링·원문 재검증을 완료했다는 뜻은 아니다. 파일별 실제 읽은 필드를 위에 표시했다.
- 3파일럿은 핵심 가설·평가·판정·미실행 상태만 검토했다. 세부 데이터·메모리·경로·배열 스키마 감사는 Agent01의 별도 결과와 함께 최종 판단한다.
- 실험·모델실행·신경분석·신규 문헌 검증 없음. 현재30개는 수정된 조건부 RQ 목록 수이며 전세계 신규성이나 실제 판별 성공이 확정된 수가 아니다.
- RQ07/RQ29의 고유성은 좁힌 관측 대비를 유지하는 조건부 판단이다. 중복 우려를 수량 목표 때문에 지우지 않는다.
- 자기 감사 파일2개만 작성했으며 공유파일/Git를 수정하지 않았다. 작성 중 공유파일 변경 가능성에 대비해 해시를 저장했다.
