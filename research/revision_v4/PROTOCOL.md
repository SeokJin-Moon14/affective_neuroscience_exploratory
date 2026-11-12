# 보유 데이터와 최근 선행을 함께 고려한 RQ 발굴

최신 사용자 지시를 따른다. 중간 승인 없이 실제 에이전트 제안·교차 비판·저자 수정·최종 선정·실행 가능한 파일럿 계획까지 진행한다. 뇌 분석을 실제 실행한 것처럼 쓰지 않는다. 원자료가 현재 환경에 없다는 사실로 새 신경 실험을 필요로 하는 질문을 제시하지 않는다.

## 데이터와 연구 범위

1순위 Horikawa·MC·NSD, 2순위 Emo-FilM, 3순위 Spacetop. datasets/DATASET_INTELLIGENCE_REPORT.md, datasets/mind_captioning/verified_spec.md, agents/01_dataset/priority_recheck.md, agents/03_vision_decoding/dataset_priority_nsd.md를 읽는다. 정서 주석을 제공하는 Horikawa, 지각·심상 및 사람 캡션이 있는 MC, 반복 시각 반응이 있는 NSD의 실제 관측에서 출발한다. 세 자료를 무조건 합치거나 모두 사용해야 하는 것은 아니다.

MC의 영상 출처와 Horikawa가 같다고 해서 처리 행·자극 ID·제외 목록을 같게 보지 않는다. NSD에 없는 정서 평정을 AI 점수로 대신해 정서 정답이라고 부르지 않는다. MC accuracy/vividness를 객관적 기억 오류로 취급하지 않는다. 새 신경·행동·시선 실험이 핵심 결론에 필수이면 주력에서 제외한다. 기존 자극에 새로 계산할 특징은 허용하며 추가 인간 주석은 필요한 비용으로 별도 표시한다. 주력은 기존 관측과 기존 주석으로 핵심 검정이 가능해야 한다.

배제 주제는 RESEARCH_MISSION.md §1.1을 따른다. 정서 전용 회로나 시각·의미 정보와 완전히 독립된 정서 계산을 발견해야 한다는 요구는 없다. 일반 시각/의미 표상과 정서의 관계를 새로 설명하는 것도 기여가 될 수 있다.

## 최근 선행과 기여

사용자가 제시한 Huang et al., Human and Machine Annotations Predict Brain Responses to Naturalistic Movies Across Development, arXiv2611.13637v1은 관련 후보의 필수 근접 선행이다. 현재는 사용자가 제공한 요약과 실제로 직접 읽은 자료를 구별한다. 단순 시각·설명문·AI 정서 점수의 fMRI encoding 비교, 모델 교체, 다른 데이터로 반복은 독립 기여로 삼지 않는다. 새 영화 일반화 하나를 추가해 모든 신규성 문제가 해결됐다고 쓰지 않는다.

가까운 선행의 이미 알려진 결론을 먼저 적고, 제안이 추가로 구별하는 설명과 중요한 결론을 쓴다. 관찰자료의 예측 차이를 뇌의 인과 경로나 알고리즘 발견으로 확대하지 않는다. 성능만 더 좋은 모델, 더 안전한 통계, 잔차가 있다는 사실만으로 필요성을 정당화하지 않는다.

## 독립 제안과 실제 토론

다섯 역할은 서로의 이번 원안을 읽기 전에 각자 1개, 서로 다른 기여가 충분하면 2개까지 제안한다. 원본은 자기 폴더 revision_v4_candidates.json에 배열로 저장한다. 역할 밖 공통파일·Git은 수정하지 않는다. 이후 실제로 다른 두 역할의 질문을 비판하고 저자가 응답·수정한다. 수를 유지하려고 후보를 살리지 않는다. 원저자에게 비판을 실제 메시지로 전달하고 변경·통합·보류 이력을 남긴다.

JSON 원고 필드:
- candidate_id: D02-A 등 역할 번호 사용. question: 처음 읽어도 뜻을 아는 질문.
- why_needed: 어떤 중요한 기존 설명/판단이 왜 부족한가.
- primary_data: 우선 데이터와 사용 조건. secondary_data: 선택적 확장, 없어도 핵심결론이 되는지.
- data_binding: 배열. dataset, existing_observation, source_path, use_in_test, still_to_verify.
- decisive_comparison: 실제 기존 자료에서 비교할 관측·대상. 인위적 편집본의 BOLD 등을 발명하지 말 것.
- competing_accounts: account와 distinguishing_result를 가진 배열.
- decisive_result, conclusion_if_supported, conclusion_if_alternative, noncontribution_result, field_impact.
- contribution_type: 신경과학적 발견/방법론/둘 다.
- analysis_plan: 5~8문장, 입력·출력·학습/평가·직접비교 설명.
- ai_enables: AI가 어떤 과학적 구별을 가능하게 하는가.
- existing_data_only: boolean. new_observations_needed: [] 또는 필요 목록. 새 관측 필수면 주력 불가.
- nearest_prior: paper_id(기존 canonical 또는 U001), known, proposed_difference, access_scope.
- strongest_objection, response_to_objection, claim_limit, minimum_pilot, abandon_if, uncertainty.
- excluded_scope_check: 제외 의제 재도입 여부.

U001은 사용자 제공 최근 논문으로 문헌 장부의 검증된 canonical ID 수에 추가하지 않는다. 출처를 직접 읽은 경우만 확인 수준을 갱신한다. 모든 결론은 아직 얻지 않은 조건부 결론이다. 원자료의 경로/배열 검사는 실행 전 확인 항목으로 두되, 관측 자체가 없는 것과 혼동하지 않는다.

MC2025 직접 선행의 ID는 U002로 사용한다. revision_v4/REFERENCES.json의 실제 확인 범위를 따른다. 기존 canonical 장부를 임의로 증식시키지 않는다.
