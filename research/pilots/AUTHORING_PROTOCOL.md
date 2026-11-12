# 세 가지 파일럿 계획 작성 규약

파일럿은 실제 분석 결과가 아니라 실행 가능한 수준의 **계획**이다. 각 담당자는 관련 Top10 카드·실제 Round5 비판과 공통 RESOURCE_AND_MODEL_PLAN.md를 읽는다. 서로 다른 과학 질문/모델 접근을 대표하도록 작성한다.

자기 Agent 폴더에 `pilot_PILOTxx.json`을 쓴다. 필수 키:

`pilot_id`, `proposal_id`, `rq_id`, `title`, `hypotheses`, `data_and_access`, `model_and_environment`, `inputs_outputs`, `experiment_sequence`, `evaluation`, `ablations_controls`, `decision_points`, `failure_modes_and_claim_limits`, `readiness`, `references`.

`references`는 canonical 문헌ID 또는 공식 URL의 문자열 배열로 작성한다.

최소 요구:

1. 핵심 가설·경쟁 가설 및 어떤 결과가 각각을 반박하는지.
2. 실제 확인한 공식 출처·경로 계약, 계획 하위집합과 선택 규칙. 보유 데이터 경로를 임의로 만들지 않는다. 새 feature/manifest는 분석 계약임을 명시한다.
3. 실제 checkpoint 식별자와 공식 코드/가중치 링크·라이선스 확인 범위. 아직 load하지 않은 것을 동작 검증했다고 쓰지 않는다. 특징 cache baseline과 확장 모델을 구분한다.
4. 주석/자극/뇌 관측 단위·시간 정렬과 예상 array shape. 데이터에 없는 주석·반복·영상 스트림을 있다고 가정하지 않는다.
5. QC → 비학습/선형 기준 → 모형 비교 → 대조 → 통계/재현성의 구체 순서.
6. train/validation/test 독립단위, nested fit, 신뢰도/uncertainty/다중비교, 효과크기와 동등성 기준. 교차참가자 calibration을 zero-shot으로 부르지 않는다.
7. 필요에 맞는 감각·의미·motion·ID·시간·생성 prior 대조. 새로운 정서 신경계산 주장이 사라질 수 있는 강한 baseline 포함.
8. 확대/수정/중단의 사전 기준. 단순 비유의성을 정보 부재로 해석하지 않는다. 과학적으로 의미있는 최소효과·허용손실 기준은 근거/정의와 함께 제안한다.
9. 이 자료로 주장 불가능한 것과 예상 실패 원인. 조건부 항목은 readiness에 공개하고 계획 완료와 실행 준비/실험 완료를 구별한다.

GPU/시간 수치는 원문 또는 실제 측정 근거가 없으면 미확인이다. 메모리 산술 견적은 array 크기와 dtype으로 계산하고 activation·원자료 비용을 별도로 둔다. 사용자 컴퓨터의 저장공간을 요구하지 않는다. 새 개인정보·원본 사용자 데이터를 공개 저장소에 업로드하지 않는다.
