# Agent01 독립 조사 1차 보고

2026-11-12. 기존 EmoBrain 및 타 Agent의 조사 결과는 열람하지 않았다. 사실의 근거는 각 dataset/verified_spec.md, 실제 원본과 URL/해시는 evidence/에 있다. 코드와 metadata 문서는 E1, 논문 서지 확인은 E2, 아래 연구 아이디어는 모두 E3, 논문 본문/Discussion과 확보하지 않은 값은 E0이다. 공통 스키마는 MISSION의 30필드를 사용하고 provenance 4필드를 추가했다.

## 가장 중요한 독립 발견

1. Horikawa 305개 이벤트 전수 파싱: 5명 각각 61런/2,196 자극행. actual `stim_index` 대 README `stimulus_index` 불일치. 모든 이벤트 ID가 고유해도 원분석은 15개 내용 중복 인덱스를 제거한다. ID 수와 내용 독립성을 혼동하면 안 된다.
2. Horikawa raw 8세션과 처리본 코드의 5/7/6/5/5 묶음은 별개다. Python tutorial에는 nested CV가 없다. 간단한 재현 코드 실행은 원논문 결과 재현 증거가 아니다.
3. Emo-FilM 30명 fMRI와 44명 연속 평정은 별도 코호트다. 14영화/50개 1Hz consensus와 fMRI 참가자의 clip validation은 같은 관측값이 아니다. Description–Instructions 극성 충돌도 발견했다.
4. Emo-FilM `lins_ccc` 기본 분기는 Pearson r다. 변수명 `ccc`만으로 측정 척도를 확정하면 오류다. 코드 실행 없이 실제 신뢰도 숫자는 보고하지 않는다.
5. Spacetop 소개 N=101 대 현행 raw 117행; 5개 예시 alignvideo 런의 28개 평정 중 유효값은 0–27개로 다르다. 현재 metadata 행 수로 유효 분석 N을 정하지 않는다.
6. NSD 공식 예제에는 8명, 세션 [40,40,32,30,40,32,40,30], 750시행/세션, masterordering→subjectim 매핑 및 noise ceiling 코드가 있다. 감정 ground truth는 이번 공식 자료에서 확인하지 못했다.

## 미해결 질문 5개(E3, 저자의 Discussion 제안 아님)

| ID | 질문 | 직접 근거·판별 조건 |
|---|---|---|
| U1 | 감정 관련 표현의 일반화는 새로운 영상 내용에도 유지되는가? | Horikawa 원 코드 dupidx + 이벤트 전수 검산; ID 분할 대 내용 그룹 분할 비교 |
| U2 | 시간 감정 구조로 보이는 신호가 annotation/HRF 지연에 의해 만들어지는가? | Emo-FilM 1Hz StartTime=0 + 실제 film onset; 독립 지연모형과 hold-out film 비교 |
| U3 | 합의가 낮은 항목에서 모델-뇌 불일치가 신경정보의 차이인가 측정 오차인가? | Emo-FilM 원평정/QC 코드 + NSD 반복 기반 ncsnr 공식 코드; 독립 평정자 평가 |
| U4 | 영상별 정서 관련 뇌 분산이 task와 평정 결측에 따라 바뀌는가? | Spacetop task-specific events + 유효평정 차이; 완전사례 선택편향과 missingness 모형 비교 |
| U5 | 서로 다른 annotation ontology를 정렬한 뒤에도 공유 감정 관련 뇌정보를 검증할 수 있는가? | Horikawa feature groups + Emo-FilM exact labels + Spacetop trial ratings; 공동 독립 평정 없으면 확증 유보 |

## 방법 기회 5개(E3)

| ID | 방법 | 새 판별력·실패 조건 |
|---|---|---|
| M1 | 내용 중복 그래프 기반 group CV | 수치 ID와 실제 내용 독립성을 분리; 영상 미확보 시 dupidx만 보수적으로 적용 |
| M2 | annotation–BOLD 결합 지연의 민감도 분석 | 고정 HRF/평정 지연 가정에 의존하는 시간 효과를 분리; 신경 인과 지연으로 해석 금지 |
| M3 | 평정자 계층 모형과 독립 검증 평정자 | consensus 평균의 확실성과 individual signal을 분리; 숫자 원평정 확보 전 보류 |
| M4 | 참가자×영화 coverage와 결측 메커니즘 감사 | 높은 점수의 완전사례만 남기는 편향 검출; 결측 원인이 미확인이라면 선택모형 민감도 보고 |
| M5 | 측정 오차를 반영한 조건부 representational comparison | 모델 정확도 대 감정 정보 잔차의 구별; 신뢰도 상한보다 작은 차이를 과장하지 않음 |

## 타 분야 전이 5개(E3, 특정 최신 모델 성과 검증 아님)

| 원 분야 | 가져오는 계산 원리 | 정서·뇌 질문 | 자료·통제 |
|---|---|---|---|
| 데이터베이스 | 타입이 있는 join·provenance 추적 | annotation과 BOLD 연결 오류가 표상 차이를 만드는가? | Horikawa stim_index 및 NSD 2단계 index; join assertion |
| 컴퓨터 비전 | perceptual deduplication | 새 내용으로 일반화되는 정서 관련 정보인가? | Horikawa 영상 내용 중복; ID baseline 비교 |
| 시계열 분석 | 상태공간/관측지연 분리 | 정서 시간 변화와 측정 지연을 구분할 수 있는가? | Emo-FilM 1Hz/scan onset/HRF; leave-film-out |
| 계량심리 | 측정 불변성·계층 평정자 모형 | 데이터 간 공유 감정 표상이 측정 체계의 차이를 넘는가? | 세 영상 데이터의 실제 문항; 독립 공통 평정 필요 |
| missing-data 통계 | 결측 메커니즘 민감도 | 뇌-정서 관계가 응답 가능한 참가자/자극에만 나타나는가? | Spacetop response_value n/a + cohort 정리 |

## 예상 밖의 연결 3개(E3)

- C1. **원영상 중복 제거 ↔ 감정 표상 기하학**: Horikawa 공식 duplicate 코드와 NSD 공식 trial→image mapping을 연결한다. 같은 내용이 여러 ID로 남으면 표상 거리가 안정적으로 보일 수 있다. 내용 독립 일반화가 남지 않으면 공통 감정 기하학 주장을 축소한다.
- C2. **평정 합의 선별 ↔ noise ceiling**: Emo-FilM QC 코드와 NSD export_noiseceiling을 연결한다. 신뢰도를 올리는 선별과 평가를 같은 표본에서 하면 비교 기준 자체가 달라진다. 독립 평정자/반복 자료에서 불확실성을 재추정한다.
- C3. **BIDS 이벤트 타입 ↔ 측정 이론**: Horikawa onsets, Emo-FilM film-relative validation, Spacetop post-clip rating을 연결한다. 시간 좌표와 측정 대상이 다른 세 변수를 같은 label 행렬로 만들 수 없다는 사실이 모델 구조 선택을 결정한다. 단순 이름 유사도 정렬은 기각한다.

## 숨겨진 가정 3개와 반론

| 가정(E3) | 왜 취약한가 | 검증 기술·수정 |
|---|---|---|
| 같은 stimulus ID 분할이면 독립이다 | Horikawa 내용 중복 제거 목록은 서로 다른 ID를 포함한다 | 영상 fingerprint/독립 audit; 그룹 분할; 의미 일반화 claim 축소 |
| consensus가 모든 참가자·시점의 정답이다 | Emo-FilM 다른 코호트·타임베이스; Spacetop 사후평정 | 계층 관측모형·개별 검증; 개인 정서 궤적 주장은 보류 |
| 데이터셋 이름이 같으면 N·schema·신뢰도 정의가 고정이다 | Spacetop 101/117, Horikawa 필드 불일치, CCC/CORR 차이 | commit 고정·파일 전수검산·코드 분기 감사; 버전별 결과 보고 |

이는 해당 논문 저자가 명시적으로 채택한 가정이라고 단정한 것이 아니라, 재사용 분석에서 발생할 수 있는 가정이다.

## 신규 Sub-axis 3개

| axis_id | name/definition | type_tags | representative_papers / models | open_questions / transfer | dataset_feasibility |
|---|---|---|---|---|---|
| P-A01 | 자극 독립성의 의미적 단위: ID/파일/내용의 차이를 표현 | Construct / Stimulus; Inference / Measurement; Structure / Dynamics | Horikawa2020 서지 + 공식 dupidx; perceptual fingerprint/group CV | U1; 데이터 중복 감사 전이 | Horikawa 영상 확보 필요 |
| Q-A01 | 시간 좌표와 관측지연: 영화·스캐너·평정 시계의 분리 | Neural; Structure / Dynamics; Inference / Measurement | Emo-FilM2025 서지 + BIDS 이벤트; 상태공간 관측모형 | U2; 시계열 식별성 전이 | Emo-FilM 실물 주석/신경신호 필요 |
| X-A01 | 주석 불확실성과 공유 표상: 타깃/평정자/척도 차이를 모형화 | Construct / Stimulus; Model / Method; Inference / Measurement | Emo-FilM·Spacetop 공식 metadata; 계층 측정모형 | U3/U5; 측정 불변성 전이 | 자료 간 독립 공동 평정 추가 필요 |

각 행 confidence=E3 조건부, origin_agent=Agent01, last_verified=2026-11-12. 모델은 계산 원리 후보이며 체크포인트 실재 검증을 완료한 특정 제품이 아니다. 연계 대상은 Agent05(시간·멀티모달), Agent07(기하학/정보), Agent12(식별성·누수), Agent03(내용 중복/시각 통제)이다. 1차 독립성 때문에 실제 결과 교환은 아직 하지 않았다.

## 여덟 탐색 질문에 대한 검토

1. 아직 검증하기 어려웠던 이유: 서로 다른 ID/시간 좌표/평정 집계와 자극 접근 제약이 비교를 방해한다는 E3 진단. 과거 연구가 시도하지 않았다는 역사적 단정은 미검증.
2. 최근 가능해진 것: 공식 Python 재현·BIDS 메타데이터·공개 처리 코드로 독립성·타임베이스·관측모형을 명시적으로 감사할 수 있다. 최신 AI 성능 증가는 이 Agent가 검증하지 않았다.
3. 틀릴 수 있는 가정: ID 독립성, consensus 보편성, schema 고정성.
4. AI가 더 포착할 수 있는 것: 영상 내용·동작·시간 맥락의 조합 후보(E3). 감정 효과와 구별하는 통제가 필요.
5. AI가 놓칠 수 있는 것: 영상·라벨·측정 오차로 설명되지 않는 신경 분산. 이를 곧바로 감정 고유 신호로 선언하지 않음.
6. 타 분야 전이: 데이터베이스 타입, 측정 불변성, missingness, perceptual deduplication.
7. 기존 데이터의 다른 용도: 높은 정확도 달성보다 어떤 단위에서 일반화가 사라지는지 판별하는 실험.
8. 신경 계산 이해의 변화: 감정 관련 신경표상 주장이 내용/측정/시간 좌표에 견고한지 판별. 부정 결과도 해당 설명의 범위를 제한한다.

## 강한 반론과 실제 남은 작업

가장 큰 반론은 metadata 감사만으로 새로운 정서 신경 계산을 발견했다고 할 수 없다는 점이다. 수정은 각 감사가 판별하는 경쟁 설명과 독립 평가를 명시하고, 실제 신경/영상/주석 접근 후에만 결과를 주장하는 것이다. 이 보고서의 E3 기회는 신규성 검증을 통과한 RQ가 아니다.

서지 확인 3편, NSD 제목 확인 후보 1편; 논문 본문·Discussion 직접 확인 0편. 정확한 Horikawa 라벨/척도, 영상 접근 권리, Emo-FilM 숫자 annotation, Spacetop 유효 cohort·전체 결측·preprocessing, NSD 공식 매뉴얼/완전 서지/감정 측정 확인이 남는다. 네트워크 403을 우회하지 않았으며 100편 목표 달성을 주장하지 않는다.
