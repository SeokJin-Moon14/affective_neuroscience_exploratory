# Agent05 Round 3: Frontier AI·LLM 의미표현 후보 비판

작성일: 2026-11-12. 실제 배정된 두 역할의 총 10후보를 검토했다. 판정: 수정 8, 보류 1, 유지 1. 후보별 반증 설계 제안이며 원자료 분석·합의·신규성 확정 결과가 아니다.

## 후보별 검토

### R3-05-C06-01 — 수정

대상: 06_frontier_ai / C06-01

| 검토 항목 | 구체적 판정 |
|---|---|
| 1. 선행문헌의 답과 남은 부분 | P045/P046/P013은 복원·잠재 예측의 계산 목표를 제공하지만 이력 의존 정서 신경 대비의 필요성을 답하지 않는다. P008/P066과의 신경 신규성은 미확정이다. |
| 2. 모델/benchmark 교체 여부 | matched-backbone 비교와 독립 대비가 있어 단순 모델 교체를 넘을 가능성이 있다. 공개 checkpoint 순위만 남으면 방법 후보로 축소한다. |
| 3. 독립 정서 대비 여부 | 전체 ΔR²와 독립 정서 대비를 구분한 점은 적절하다. 대비 선택·시간평가 단위와 예측 상태/오차의 서로 다른 시점이 아직 불명확하다. |
| 4. 미확인 필드와 실제 필요조건 | 미래 프레임 없는 encoder 입력·normalization·token 경로, 사건/영상/스캐너 시간 매핑, 연속 주석의 코호트·지연이 필요하다. Spacetop clip 평정은 연속 주석이 아니다. |
| 5. 자극·motion·semantics·HRF 대안 | FIR만 추가해도 최근 장면 가중치·의미 순서·feature 자기상관의 차이가 남는다. 동일 과거의 recency-weighted bag 및 order-aware causal baseline이 필요하다. |
| 6. 예측·대응·기전·인과 수준 | prefix-only 상태는 기대의 후보지만 관측 미래와 비교한 예측오차는 미래가 도착한 시점의 변수다. 이 오차를 이전 시점에 배치하면 관찰 가능한 과거 원칙을 위반한다. |
| 7. 강한 baseline과 판별 대조 | h_t=f(x≤t), 예측 zhat(t+h|t), 오차 e(t+h)=z(t+h)−zhat(t+h|t)를 분리하고 각자의 실제 가용시점에 놓는 대조가 더 강하다. |
| 8. 부정 결과의 과학적 가치 | causal 상태 이득이 없고 미래 접근 조건에서만 생기면 기대 설명을 제한한다. matched latent 차이가 HRF 후 소멸하면 현 측정으로 상태를 구분할 수 없음을 배운다. |

**가장 강한 반론**

과거-only 입력을 썼다는 조건은 예측오차까지 시점 t에 이용할 수 있다는 뜻이 아니다. 예측 상태와 관측 미래를 사용한 오차를 함께 넣으면 기대와 사후 놀라움을 구분하지 못한다.

**필수 수정**

- 상태·예측·오차 각각의 time_available 필드를 정의하고 미래 도착 전 오차를 모든 분석에서 금지한다. 영상 표준화·caption 생성·event detection에도 같은 cutoff를 적용한다.
- prefix 입력을 다루는 checkpoint의 학습목표와 실행 경로를 고정하고 미래 가림으로 생긴 분포 변화는 동일 입력의 단순 causal 모델과 비교한다.
- Emo-FilM은 별도 평정 코호트와 지연을 명시한다. Spacetop은 clip 평가로 분기하고 연속 정서 전이 검정에 재사용하지 않는다.
- 시간분할은 영화/내용군 기준으로 하고 최대 과거창과 HRF 지연을 포함한 buffer, train-only FIR 선택 및 효과 복구 시뮬레이션을 넣는다.

**더 강한 판별 대조**

동일 현재 구간·동일 과거량에서 현재-only, 시간가중 사건 bag, 순서보존 causal state, 미래허용 oracle을 비교한다. 예상 상태와 도착시점 오차는 별도 모델로 평가한다. 원시 시간에서 동일 HRF family를 적용하고 독립 정서 대비의 손실 차이를 leave-film-out으로 검정한다.

**부정 결과의 가치**

정밀한 영효과는 해당 상태모형의 추가 정보 필요성을 제한한다. 낮은 신뢰도는 기대 부재가 아닌 식별불가다. oracle만 이기면 retrospective 정보의 효과로 결론 범위를 줄인다.

**남은 이견**

관측 과거 기반 상태의 추가 예측이 기대 계산의 증거인지 일반 문맥 압축인지는 남는다. 새 인간 순서/기대 조작 없이 신경 인과로 판정하지 않는다.

근거: P013, P045, P046, P089, P002

### R3-05-C06-02 — 수정

대상: 06_frontier_ai / C06-02

| 검토 항목 | 구체적 판정 |
|---|---|
| 1. 선행문헌의 답과 남은 부분 | P049/P050은 환경 안정성·metadata 보존/억제를 다루며 어느 환경 정보가 정서 신경표상에 필수인지는 별도 질문이다. |
| 2. 모델/benchmark 교체 여부 | guide 종류×억제의 교차 대비는 독립 질문이다. C06-04와 달리 성능 향상 선택이 아니라 어떤 정보를 제거하는지가 조작임을 유지해야 한다. |
| 3. 독립 정서 대비 여부 | 동일 정서 라벨 안 신경 차이만 보면 정서와 무관한 내용 차이도 포함된다. 독립 정서 관련 대비에서 선택적 손실을 따로 검증해야 한다. |
| 4. 미확인 필드와 실제 필요조건 | 촬영 양식·사건 맥락의 독립 metadata, 내용×환경 교차, 실측 정서주석 및 반복 신뢰도, 적응 구현이 필요하다. |
| 5. 자극·motion·semantics·HRF 대안 | 촬영 양식도 의미·정서와 공변할 수 있다. probe 감소량·rank를 맞춰도 실제 제거 정보의 신경적 중요도와 분포 겹침은 맞춰지지 않는다. |
| 6. 예측·대응·기전·인과 수준 | 억제는 모델 내부 조작이며 인간에게 맥락을 제거한 결과가 아니다. nuisance라는 명칭을 근거로 신경적 무관성을 선언하지 않는다. |
| 7. 강한 baseline과 판별 대조 | 사전 정의된 촬영/사건 metadata를 중립적으로 명명하고 동일 삭제량 곡선·sham·내용 매칭을 적용한 difference-in-differences가 필요하다. |
| 8. 부정 결과의 과학적 가치 | 동일 손실 곡선이면 선택적 불변성은 지지되지 않는다. 두 종류 모두 정서 대비를 줄이면 보편적 nuisance 구분이 부적절할 수 있다. |

**가장 강한 반론**

촬영 정보를 nuisance로, 사건 정보를 필수 맥락으로 먼저 명명하면 결과의 방향을 사실상 가정한다. metadata probe 성능을 맞추는 것만으로 두 제거가 같은 정보량 또는 신경 영향력을 갖는다고 할 수 없다.

**필수 수정**

- 촬영/사건 정보라는 기술적 이름만 사용하고 무관성은 결과로 판단한다.
- 각 metadata의 train-only 제거 강도 곡선을 설정하고 임의 제거·sham·재구성 손실·다중 probe로 제거 및 잔존을 감사한다. probe 실패를 정보 부재의 증명으로 쓰지 않는다.
- 독립 정서 대비와 비정서 내용 대비를 같은 피험자·자극에서 평가하고 총/공유/조건부 손실을 분리한다.
- 공통 지지집합이 없는 환경 조합은 제외 이유와 적용 범위를 기록한다. 이를 데이터 보유 자체의 차단 사유로 확대하지 않는다.

**더 강한 판별 대조**

내용·현재 감각을 맞춘 strata에서 촬영정보 억제 대 사건정보 억제의 정서 대비 손실 차이를 비정서 대비 손실 차이로 다시 대조한다. 강도별 곡선과 label-permuted guide를 독립 환경에서 비교한다.

**부정 결과의 가치**

선택성 부재는 어떤 불변성도 정서 관련 정보만 남기지 않는다는 제한된 결과다. 일반 정확도 또는 QC만 남으면 adaptation 방법 후보로 분리한다.

**남은 이견**

정서와 공유되는 맥락을 nuisance와 분리할 유일한 조건화 집합은 없다. 총 설명과 조건부 설명 중 무엇을 주결과로 둘지는 다음 라운드에서 합의가 필요하다.

근거: P049, P050, P001, P007

### R3-05-C06-03 — 수정

대상: 06_frontier_ai / C06-03

| 검토 항목 | 구체적 판정 |
|---|---|
| 1. 선행문헌의 답과 남은 부분 | P083은 개념 경유 예측, P053은 분해 식별의 제약을 제공한다. SAE 안정성·신경 대응·계산 사용의 결합은 아직 이 자료에서 검증되지 않았다. |
| 2. 모델/benchmark 교체 여부 | 세 검증을 구분한 설계는 단순 SAE 적용을 넘는다. 단 안정성이 높다는 지표 하나만으로 신경 계산 단위를 이름 붙이면 기존 alignment 반복이다. |
| 3. 독립 정서 대비 여부 | 독립 정서 대비를 명시했으나 신경 대비에 유리한 성분 선택과 후속 모델 기능 평가를 독립 표본으로 분리해야 한다. |
| 4. 미확인 필드와 실제 필요조건 | activation 주입 지점, SAE 재구성 잔차 우회 경로, 영상모델 호환, 평가 목표·미래 사용 시점, 반복 신뢰도가 필요하다. |
| 5. 자극·motion·semantics·HRF 대안 | 고에너지·고빈도 움직임/장면 성분은 seed 안정성·BOLD 대응·후속 예측 기여를 동시에 높일 수 있다. 세 지표의 동시 양성만으로 정서 계산 성분은 아니다. |
| 6. 예측·대응·기전·인과 수준 | 모델 기능 제거는 모델 내부 필요성만 지지한다. 개별 feature가 실패하고 subspace가 안정적이면 신경 계산이 분산됐다고 확정할 수 없다. |
| 7. 강한 baseline과 판별 대조 | 재구성 잔차를 보존한 intervention, dense 방향 및 downstream 민감도가 맞는 대조, 개념/비개념 성분의 이중 분리를 추가한다. |
| 8. 부정 결과의 과학적 가치 | PCA나 무작위 subspace와 동등하면 희소 개념 단위 해석의 추가 가치를 제한한다. 잔차 우위면 해당 개념 사전의 불충분성을 말할 수 있다. |

**가장 강한 반론**

동일 에너지 제거는 동일한 downstream 손상을 뜻하지 않는다. SAE 재구성 잔차를 함께 제거하거나 주입 지점이 바뀌면 개념의 실제 사용과 off-manifold 손상을 혼동한다.

**필수 수정**

- activation = SAE 재구성 + 잔차로 기록하고 baseline·feature 제거 조건에서 잔차 경로를 동일하게 유지한다.
- 동일 에너지 외에 downstream 민감도·재구성 오차가 비슷한 dense 방향 대조와 의미가 맞는 donor activation patch를 둔다. patch 역시 분포 변화가 없는지 검사한다.
- 신경 대비 기반 성분 선택, seed 정렬, 모델 기능 평가는 nested train/validation/test를 분리한다.
- 후속 상태를 예측하는 경우 시점 t 이전 activation과 이후 도착한 평가 타깃을 구분한다. 영상 전체를 본 SAE feature를 온라인 상태로 명명하지 않는다.

**더 강한 판별 대조**

안정/불안정 × 정서 대비 관련/비관련 성분의 모델 기능 손실을 잔차 보존하에 비교한다. 같은 rank의 PCA와 dense 민감도 대조를 넣고, 신경 대비의 보존과 모델의 다음 사건 손실을 각각 보고한다. 둘의 곱을 단일 기전 점수로 만들지 않는다.

**부정 결과의 가치**

해석가능 이름·안정 좌표·모델 기능이 분리되는 결과도 유익하다. feature 이름만 남고 신경 대비 특이성이 없으면 일반 모델 해석 방법 후보로 이동한다.

**남은 이견**

안정된 subspace가 여러 분해에서 공통이라는 사실은 뇌가 그 단위로 계산한다는 주장보다 약하다. 신경 인과 결론을 유지할 근거는 현재 없다.

근거: P083, P053, P089, P101

### R3-05-C06-04 — 수정

대상: 06_frontier_ai / C06-04

| 검토 항목 | 구체적 판정 |
|---|---|
| 1. 선행문헌의 답과 남은 부분 | P050/P098/P099는 적응·분포 이동 평가를 뒷받침하지만 정서 신경정보 선택적 망각 여부를 이미 답한 근거는 아니다. |
| 2. 모델/benchmark 교체 여부 | 비정서 성능으로 고른 적응의 신경 비용을 평가하는 질문은 C06-02의 guide 조작과 구별된다. frozen 모델 순위 비교로 축소하지 않는다. |
| 3. 독립 정서 대비 여부 | 정서 대비와 일반 시각 대비의 변화 차이를 요구한 점은 적절하다. 두 대비를 서로 다른 데이터에서만 측정하면 선택성은 식별되지 않는다. |
| 4. 미확인 필드와 실제 필요조건 | 동일 자극/피험자에서 두 종류 대비, 적응 episode 경계, 독립 target 적응자료, 평가 readout 재적합 자료가 필요하다. |
| 5. 자극·motion·semantics·HRF 대안 | Horikawa와 NSD의 차이는 SNR·자극 modality·평정·획득 차이로도 생긴다. 서로 다른 자료의 손실량 비교를 정서 선택성 증거로 삼으면 안 된다. |
| 6. 예측·대응·기전·인과 수준 | 검사 자극으로 비지도 적응하는 transductive 설정과 새 미관측 자극 일반화를 명시적으로 구분해야 한다. neural target을 쓰지 않았다고 모든 평가 누수가 사라지는 것은 아니다. |
| 7. 강한 baseline과 판별 대조 | 같은 자극의 감각/정서 대비, reset된 적응 episode, held-out 환경, frozen/readapted readout 교차가 강한 대조다. |
| 8. 부정 결과의 과학적 가치 | readout 재적합 후 회복하면 정보 소실보다 좌표 변화 설명이 유력하다. 적응 이득 자체가 재현되지 않으면 신경 비용 가설의 전제를 확인하지 못한 것이다. |

**가장 강한 반론**

정서 신경 손실은 Horikawa에서, 일반 시각 보존은 NSD에서 확인하는 비교로는 선택성을 입증할 수 없다. 적응의 좌표 변경과 실제 정보 손실도 동일한 readout만 고정하면 섞인다.

**필수 수정**

- 정서 및 비정서 신경 대비를 동일 자극·참가자 안에서 주검정하고 NSD는 외부 범위 대조로 남긴다.
- 적응 train/validation/test와 신경 readout train/test를 별도 표로 명시한다. target 전체를 보는 적응은 transductive로 표시하고 순수 inductive 결과와 분리한다.
- 시간 순 적응에서는 영화 전체·미래 프레임으로 과거 상태를 갱신하지 않는다. episode reset·평가 순서를 고정한다.
- 동일 데이터량·용량의 readout 재적합과 fixed readout 결과를 함께 보고 비정서 성능의 측정오차도 joint uncertainty에 반영한다.

**더 강한 판별 대조**

동일 자극에서 adaptation strength × fixed/refit readout × 정서/비정서 대비를 교차한다. 별도의 환경에서 OOD 성능 상승을 확인한 뒤 정서 손실의 차이 대비를 평가한다. 미래 target batch 접근이 필요한 적응은 retrospective 보조 조건으로만 둔다.

**부정 결과의 가치**

회복 가능한 좌표 변화와 회복되지 않는 표현 손실을 구분한다. 모든 대비가 같은 만큼 손실되면 정서 선택적 망각 대신 일반 정보보존 문제로 결론을 줄인다.

**남은 이견**

검증 범위는 실제 선택된 domain과 적응 규칙에 한정된다. 소수 domain에서 보인 tradeoff를 모든 적응의 필연적 비용으로 일반화할 수 없다.

근거: P050, P098, P099, P001

### R3-05-C06-05 — 보류

대상: 06_frontier_ai / C06-05

| 검토 항목 | 구체적 판정 |
|---|---|
| 1. 선행문헌의 답과 남은 부분 | P001/P008/P009는 정서 표상·주석 구조의 배경이고 P083은 개념 모형을 제공한다. 관측하지 않은 조합 항의 학습 가능성을 직접 보장하지 않는다. |
| 2. 모델/benchmark 교체 여부 | 새 조합의 가산/비가산 신경 반응은 과학 질문이다. 다만 임의 상호작용 모형을 보지 않은 cell에 적용하는 설계는 모델 비교로도 식별되지 않는다. |
| 3. 독립 정서 대비 여부 | 독립 정서 대비를 포함하지만 test 조합을 정의한 주석과 검증 주석의 관계를 명시해야 한다. 집계 혼합을 개인 내 복합 정서로 해석하지 않는다. |
| 4. 미확인 필드와 실제 필요조건 | 성분별 빈도, 교차 조합 support, 평가자 수준 관측, 공유될 조합 구조, 실제 자극 사건 내용이 필요하다. |
| 5. 자극·motion·semantics·HRF 대안 | 보류한 조합은 객체 관계·길이·편집·motion에서도 새로울 수 있다. 성분 빈도만 맞춰서는 관계 의미의 외삽 난도를 맞추지 못한다. |
| 6. 예측·대응·기전·인과 수준 | 뇌 encoding의 상호작용 항은 신경회로 coupling이 아니다. 알려진 정서 라벨을 입력한 반응 예측을 정서 자체의 무감독 발견으로 서술하지 않는다. |
| 7. 강한 baseline과 판별 대조 | 관계 항을 조합별 자유계수 대신 학습된 성분 간 공유 저랭크 함수로 정의하고, synthetic recovery와 조합 support 조건을 먼저 고정해야 한다. |
| 8. 부정 결과의 과학적 가치 | 공유 구조가 복구 가능한 설계에서 가산 기준과 동등하면 관계 항 필요성을 제한한다. 관측하지 않은 자유계수의 실패는 가산 신경 코드의 증거가 아니다. |

**가장 강한 반론**

완전히 유보한 성분쌍의 자유 상호작용 계수는 학습에서 추정되지 않는다. low-rank라는 이름만으로 어느 조합에서 무엇을 공유해 외삽하는지 정하지 않으면, 음성 결과가 신경 가산성인지 추정 불가능성인지 구분되지 않는다.

**필수 수정**

- 보류는 데이터 부족 일반론 때문이 아니라 unseen-cell 추정량의 정의 부족 때문이다. 공유 성분 embedding·저랭크 tensor 등 상호작용의 구조적 가정과 예측식을 명시하면 발전시킬 수 있다.
- 각 성분이 여러 다른 partner와 train에서 연결되고 test pair가 그 연결구조 안에 놓이는 support 규칙을 정의한다. 전혀 새 성분과 새 조합은 별도 검정으로 나눈다.
- 같은 split에서 가산·공유 저랭크·성분 내 비선형 신호를 주입한 recovery를 하고 관측 연산/주석 잡음 뒤 구별 가능성을 확인한다.
- 조합 ontology는 외부 사전 정의 또는 훈련주석으로 고정하고 최종 정서 대비 평정은 독립 평가자 집합으로 검증한다. 개별 평정이 없으면 집계 주석의 조합이라고만 쓴다.

**더 강한 판별 대조**

동일 train에서 학습된 성분별 기여를 recombine한 가산 예측과 partner 간 공유를 명시한 관계 함수를 비교한다. 새 pair와 기존 pair의 별도 held-out 자극을 내용거리·duration·reliability에 맞춘다. recovery가 되는 최소 효과 범위에서 정서 관련 신경 대비의 차이를 평가한다.

**부정 결과의 가치**

지원되는 구조적 외삽에서만 관계 필요성의 영효과가 의미 있다. recovery 실패면 본 질문을 폐기하지 않고 해당 설계를 식별불가로 보류한다.

**남은 이견**

Agent02의 공동 후보와 병합해야 한다는 원안 판단에 동의한다. 생물학적으로 정당한 조합 구조를 저랭크 가정으로 대체해도 되는지는 미해결이다.

근거: P001, P008, P083, P101

### R3-05-C10-01 — 수정

대상: 10_llm_semantics / C10-01

| 검토 항목 | 구체적 판정 |
|---|---|
| 1. 선행문헌의 답과 남은 부분 | P081은 시각–언어 병목 구조를, P015는 신경 시각 정렬을 제공한다. 언어화가 정서 대비를 선택적으로 소실시키는지는 별도 검정이다. |
| 2. 모델/benchmark 교체 여부 | 용량별 보존 곡선은 단순 caption encoder 교체를 넘는다. 다만 Q-Former 단계 차이를 모두 언어화 원인으로 읽으면 구조·학습목표가 섞인다. |
| 3. 독립 정서 대비 여부 | 전체 신경 예측과 정서 대비를 나눈 점은 적절하다. 시각 식별을 한 종류로 맞추는 것만으로 사건 관계/시간 정보의 일반 손실까지 배제되지는 않는다. |
| 4. 미확인 필드와 실제 필요조건 | 동일 backbone 단계별 activation·caption seed/길이·시점, 실측 정서주석, 반복 신뢰도와 중립 사건 관계 주석이 필요하다. |
| 5. 자극·motion·semantics·HRF 대안 | 차원 또는 token 수는 정보량이 아니다. 캡션의 시간·음향 생략, 관계 누락, readout 비선형성으로 선택적 손실처럼 보일 수 있다. |
| 6. 예측·대응·기전·인과 수준 | 선형 readout에서 못 읽는 정보를 사라진 정보라고 단정하지 않는다. caption 단계의 재표현과 비가역 소실을 구분해야 한다. |
| 7. 강한 baseline과 판별 대조 | 선형/동일 용량 비선형 probe, 길이 맞춤 비언어 bottleneck, 관계·사건 대비, 생성 전/후 반복 seed 대조를 추가한다. |
| 8. 부정 결과의 과학적 가치 | 비선형 probe에서 회복되면 언어 압축의 정보 소실보다 접근성 변화다. 모든 대비가 함께 줄면 일반 압축 설명으로 충분하다. |

**가장 강한 반론**

동일 차원과 시각 식별 점수에서도 언어 latent의 정보는 다른 좌표나 비선형 형태로 남아 있을 수 있다. 선형 encoding 감소를 선택적 정보 소실로 부르면 근거보다 강한 결론이다.

**필수 수정**

- 주장을 선형 접근성 저하와 정보 소실 후보로 분리한다. 데이터량을 맞춘 선형·소형 비선형 readout의 학습곡선을 함께 보고한다.
- 동일 backbone의 비언어 bottleneck을 용량별 대조로 포함하고 객체뿐 아니라 비정서적 사건 관계 대비를 둔다.
- clip 캡션과 frame-prefix 캡션의 입력범위를 기록한다. 영화 전체 outcome을 본 caption을 이전 시점 신경 상태 설명에 사용하지 않는다.
- 캡션의 정서 단어를 독립 정서 정답으로 사용하지 않고 별도 실측 주석과 중립 사건 내용을 평가한다.

**더 강한 판별 대조**

병목 언어성 × 용량 × readout 유연성의 보존곡선을 동일 자극에서 비교한다. 정서 대비 손실이 시각·관계 대비 손실보다 크고 비선형 readout에서도 회복되지 않는 범위를 한정한다. 원자료 신뢰도가 없는 대비는 제외한다.

**부정 결과의 가치**

언어 병목이 정보를 없앤 것인지 읽기 어렵게 만든 것인지 구분한다. 모든 효과가 rank/관계 누락으로 설명되면 일반 압축 방법 후보로 남긴다.

**남은 이견**

유한 표본의 probe로 정보의 완전 부재를 증명할 수 없다. 가장 강한 표현도 평가한 readout family 내 비회복 손실이어야 한다.

근거: P081, P015, P079, P101

### R3-05-C10-02 — 수정

대상: 10_llm_semantics / C10-02

| 검토 항목 | 구체적 판정 |
|---|---|
| 1. 선행문헌의 답과 남은 부분 | P083/P084는 개념의 명시적 조건화, P066/P067은 사건/시간 구조 도구를 제공한다. 누락 관계와 신경 상호작용의 교차 검정은 아직 남아 있다. |
| 2. 모델/benchmark 교체 여부 | 관계 정보 × L/D/N 비교는 모델 교체 이상의 질문이다. C06-05의 자극 성분 상호작용과 달리 여기서는 영역 간 조합이 대상이다. |
| 3. 독립 정서 대비 여부 | 독립 정서주석 예측을 표적 삼는 점은 명료하다. 다만 관계 설명에 정서 결론이 들어가면 조건화가 타깃을 직접 대신하여 N-D를 줄일 수 있다. |
| 4. 미확인 필드와 실제 필요조건 | 독립 중립 관계 설명, 객체/사건 대응, 주석 코호트, ROI 신뢰도·정의, 설명 생성의 입력 provenance가 필요하다. |
| 5. 자극·motion·semantics·HRF 대안 | 공통 감각 입력·HRF 평활화·영역 SNR 차이로 비선형 N 이득이 생길 수 있다. 의미와 정서의 공선성 때문에 잔차 감소가 누락 confound 제거임을 보장하지 않는다. |
| 6. 예측·대응·기전·인과 수준 | 관계 추가 뒤 N-D 감소는 조건부 예측의 대체 관계다. 원래 신경 상호작용이 가짜였거나 의미가 인과적으로 매개했다는 결론은 나오지 않는다. |
| 7. 강한 baseline과 판별 대조 | 자극 관계를 뇌에서 독립적으로 만든 뒤 의미-only, 의미+지역 내 비선형 가산, 의미+영역 간 상호작용을 동일 held-out 자료에서 직접 비교한다. |
| 8. 부정 결과의 과학적 가치 | N-D가 원래 없으면 상호작용 필요성이 지지되지 않으며 감소 가설의 기준점이 없다. 관계 후 남아도 가능한 공통 입력과 미측정 의미가 남는다. |

**가장 강한 반론**

더 풍부한 사건 설명을 추가하면 주석을 직접 예측하기 쉬워져 어떤 신경 모델의 증분도 줄 수 있다. 이 감소만으로 원래 N-D 이득의 원인이 누락 사건이었다고 판정하면 과잉 해석이다.

**필수 수정**

- 서술 생성에는 뇌·정서 라벨을 입력하지 않고 객체·행위·관계 중심으로 검수한다. 정서 결론을 포함한 설명은 별도 민감도 조건으로 분리한다.
- N-D는 동일 의미 baseline 위에서 정의하고 의미-only 성능, 신경 총/공유/조건부 성능을 함께 보고한다.
- 관계 추가의 일반적 타깃 설명력 증가를 맞춘 비관계 설명 및 공통입력×HRF 모의 null을 둔다.
- 연속 자료로 확장하면 설명의 available time을 맞추고 Spacetop clip 평정은 clip 집계 분석에만 사용한다.

**더 강한 판별 대조**

객체-only/검수된 관계/정서결론 포함 설명을 교차하고 각 조건에서 의미-only 대비 D와 N의 추가 예측을 비교한다. 타깃 예측력을 맞춘 관계 없는 대조에서도 동일 감소가 나면 관계 특정 설명은 반증된다. 모든 잔차화는 cross-fitting한다.

**부정 결과의 가치**

관계의 특정성이 없으면 관심 정보가 의미와 통계적으로 공유됨을 보일 뿐이다. N이 남는 경우도 인과 통신이 아닌 선택한 모형계열의 비가산 필요성으로 제한한다.

**남은 이견**

정서와 사건 의미의 공유분을 nuisance로 지워야 하는지에 대한 이론적 선택은 남는다. 잔차만을 진짜 정서정보로 우선하지 않는다.

근거: P083, P084, P066, P067, P101

### R3-05-C10-03 — 수정

대상: 10_llm_semantics / C10-03

| 검토 항목 | 구체적 판정 |
|---|---|
| 1. 선행문헌의 답과 남은 부분 | P085/P086의 문맥 encoding과 P066의 사건 구조는 선행 틀이다. 동일 사건집합에서 순서만 필요한지와 정서 대비의 연결이 남은 차이다. |
| 2. 모델/benchmark 교체 여부 | 내용집합·순서·관측지연 분리는 실질 질문이다. 단순 긴 문맥 모델 승리로 돌아가면 기존 benchmark 교체가 된다. |
| 3. 독립 정서 대비 여부 | 시간별 독립 정서 대비가 주표적이다. Spacetop clip 평정을 매 시점 반복하면 핵심 질문을 검증한 것이 아니므로 데이터 계획을 명시적으로 분기해야 한다. |
| 4. 미확인 필드와 실제 필요조건 | event onset뿐 아니라 event completion/설명 생성 시점, prefix 입력, 주석 지연·코호트, 충분한 독립 영화가 필요하다. |
| 5. 자극·motion·semantics·HRF 대안 | 사건 집합을 고정해도 순서 교환은 recency와 의미적 인과관계 및 입력 자연스러움을 바꾼다. bag 대비만으로 순서 계산을 식별하기 어렵다. |
| 6. 예측·대응·기전·인과 수준 | 원래 순서를 본 뇌에 순서변형 모델 특징을 대응시키는 것은 모델 설명 비교다. 사람에게 실제로 순서를 바꿔 보여준 효과가 아니다. |
| 7. 강한 baseline과 판별 대조 | 마지막 k개 사건을 고정하고 먼 과거만 교환하는 조건, identity×lag 가산 모형, 순서 유지 paraphrase, 유효한 대체 순서를 추가한다. |
| 8. 부정 결과의 과학적 가치 | lag 가중 bag이 동등하면 최근 내용 기여로 충분한 범위다. 미래/완결 사건 설명에만 이득이면 온라인 순서 필요성은 지지되지 않는다. |

**가장 강한 반론**

같은 사건집합은 같은 시간정보가 아니다. 순서를 섞으면 어떤 사건이 가장 최근이었는지도 달라지므로 순서 의존 효과와 recency-weighted 내용 효과를 현재 대비로는 분리할 수 없다.

**필수 수정**

- 현재 구간과 마지막 k개 사건을 고정한 먼 과거 순서 교환을 추가하고 lag별 사건 identity를 허용하는 가산 baseline을 둔다.
- 각 시점까지 관찰된 부분만 caption/event description으로 만든다. 전체 영화를 본 사건 분절·후속 결말·완결된 사건 요약은 retrospective 조건으로 분리한다.
- 원순서 paraphrase와 그럴듯한 대체 순서를 검수해 문법·내용 길이·자연스러움 영향을 추정한다. 순서에서 생긴 의미 관계 변화는 관심효과로 명확히 정의한다.
- Emo-FilM은 연속 주석과 평정지연 모형으로, Spacetop은 clip-level 요약 대비로 나눈다. HRF는 원시간 좌표에서 동일 family로 적합하고 fold 경계 buffer를 적용한다.

**더 강한 판별 대조**

현재+최근 사건 고정 아래 원순서, 먼 과거 교환, lag 가중 bag, 순서 유지 paraphrase를 비교한다. 동일 past-only encoder의 원순서 이득이 recency·자연스러움 및 공통 HRF 통제 뒤 독립 영화의 정서 대비에서 남는지 검정한다. prefix-only와 full-film oracle의 성능은 별도로 보고한다.

**부정 결과의 가치**

recency로 충분하면 전체 순서 계산을 요구하지 않는 표현 범위를 얻는다. 낮은 시간 해상도에서 동등하면 신경 순서 부재가 아닌 관측상 비식별이다.

**남은 이견**

순서가 바뀌면 사건 관계의 의미도 바뀌므로 완전히 동일한 의미량을 보장할 수 없다. 질문을 시간순서 자체와 순서가 만드는 관계 구조 중 어느 것에 둘지 좁혀야 한다.

근거: P085, P086, P066, P002, P042

### R3-05-C10-04 — 유지

대상: 10_llm_semantics / C10-04

| 검토 항목 | 구체적 판정 |
|---|---|
| 1. 선행문헌의 답과 남은 부분 | P015/P021/P087은 조건부 생성과 prior 영향을 다룰 근거다. 정서 관련 내용의 생성 전후 출처 구분은 아직 확인할 부분이다. |
| 2. 모델/benchmark 교체 여부 | 생성 전 latent와 생성 후 내용, 의미 매칭 조건 교환을 교차해 단순 caption 품질 benchmark보다 강한 질문이다. |
| 3. 독립 정서 대비 여부 | 외부 참조·독립 주석을 평가하고 같은 뇌신호로 순환 encoding하지 않는 기준이 적절하다. 객체/장면과 구별되는 대비 타당성을 추가 명시하면 된다. |
| 4. 미확인 필드와 실제 필요조건 | Mind Captioning의 실제 식별·조건 경로, 생성 seed/프롬프트, 외부 참조, 동일 신뢰도 조건 교환 표본이 필요하다. 명칭만으로 가용성을 확정하지 않았다. |
| 5. 자극·motion·semantics·HRF 대안 | 의미 매칭은 실제 사건 관계·시간 단계까지 같다는 보장이 없다. 교환 조건의 피험자/세션/SNR 차이가 생성 차이를 만들 수 있다. |
| 6. 예측·대응·기전·인과 수준 | 주장을 신경 조건의 정보 기여에 한정한 점은 적절하다. 생성 실패로 원 뇌에 해당 정보가 없다는 결론을 내리지 않아야 한다. |
| 7. 강한 baseline과 판별 대조 | 동일 피험자·세션·신뢰도 strata 내 의미/사건 단계 매칭 교환과 생성 없는 latent retrieval을 주대조로 유지한다. |
| 8. 부정 결과의 과학적 가치 | 실제 조건 이득이 없고 latent 정보는 남으면 생성기의 사용 실패다. latent도 실패하면 decoder 한계·측정 신뢰도·정보 부재를 구분하지 못한다. |

**가장 강한 반론**

핵심 설계는 유지할 수 있다. 가장 남는 위험은 의미가 비슷한 신경 조건 교환이 감정 대비 외의 사건 단계·신호품질·피험자 좌표도 바꾸어 조건의 기여를 과대/과소평가한다는 점이다.

**필수 수정**

- 교환 후보는 뇌 출력이나 생성 품질을 보기 전 독립 자극 metadata로 정하고 피험자·세션·신뢰도·사건 단계의 공통 지지집합을 기록한다.
- 원 뇌→latent에서 판별되는지와 latent→caption에서 보존되는지를 나눠 실패 위치를 보고한다.
- 영상 기반 caption이면 full clip와 prefix의 가용시점을 표시한다. 전체 결말을 본 언어 출력은 이전 시점 기대를 읽었다는 근거로 쓰지 않는다.
- 해당 경로가 없으면 예정한 fallback대로 생성 없는 정보출처 비교로 줄이고 실제 수행하지 않은 생성 실험을 완료로 표시하지 않는다.

**더 강한 판별 대조**

같은 피험자 내 의미·사건 단계·SNR이 맞는 두 자극을 사전 선정해 실제/교환 조건을 비교한다. 원 뇌 readout, 생성 전 retrieval, 생성 후 독립 내용 판별의 세 단계에서 정서 대비 손실을 따로 계산하고 다수 seed 불확실성을 보고한다.

**부정 결과의 가치**

생성기 보충과 신경 조건 사용을 분리하는 음성 결과가 핵심 기여다. 단 원 뇌 정보의 부재를 입증하지는 않으며 정서 대비가 성립하지 않으면 일반 출처 감사로 축소한다.

**남은 이견**

의미 매칭을 얼마나 강하게 해야 정서 대비를 남기면서 자극 식별 효과를 억제할지는 남는다. 현 설계의 조건부 추정량으로 보고하면 핵심 질문은 유지 가능하다.

근거: P015, P021, P087, P101

### R3-05-C10-05 — 수정

대상: 10_llm_semantics / C10-05

| 검토 항목 | 구체적 판정 |
|---|---|
| 1. 선행문헌의 답과 남은 부분 | P015는 피험자 공유 decoder, P062는 지도 좌표 도구, P083/P079는 개념/시각언어 표상이다. 두 실패 원인을 직접 식별하는 설계는 별도다. |
| 2. 모델/benchmark 교체 여부 | 내용 조합×피험자×좌표 비교는 일반화 대상의 차이를 묻는다. 단 데이터셋만 바꾼 성능표와 구분하려면 각 축의 독립 support가 필요하다. |
| 3. 독립 정서 대비 여부 | 고정된 독립 정서 대비를 쓴 점은 적절하다. 내용과 피험자 신뢰도의 차이가 목표 대비를 바꾸지 않도록 맞춰야 한다. |
| 4. 미확인 필드와 실제 필요조건 | 새 피험자 정렬용 calibration 데이터, 공동 자극 여부, 반복 신뢰도, 의미 조합 support, 주석 단위·개인 차이가 필요하다. |
| 5. 자극·motion·semantics·HRF 대안 | 정렬 뒤 남는 의미 실패도 모델의 조합 실패 외에 신경 반응 자체의 내용 의존 변화·주석 차이·SNR로 생긴다. 언어모형 자체의 조합 성능을 별도 측정해야 한다. |
| 6. 예측·대응·기전·인과 수준 | 새 피험자 뇌로 adapter를 적합하면 zero-shot 새 피험자 일반화가 아니다. test 자극으로 정렬하면 의미/좌표 실패가 분리되지 않는다. |
| 7. 강한 baseline과 판별 대조 | 0-shot anatomy-only와 별도 calibration k-shot을 분리하고 각 단계에 동일 예산을 준다. 자극-only 관계 예측을 신경 일반화와 나란히 평가한다. |
| 8. 부정 결과의 과학적 가치 | calibration으로 회복되면 좌표/적응 제약, 자극-only도 실패하면 모델 조합 표현 문제가 후보가 된다. 둘을 모두 통제해도 남은 실패는 고유 정서 코드 부재를 뜻하지 않는다. |

**가장 강한 반론**

새 피험자의 개인 좌표를 얻는 데 필요한 보정 데이터와 평가 데이터가 명확하지 않다. 또한 좌표 정렬 뒤 실패가 남는다는 사실만으로 언어표현의 조합 실패로 원인을 특정할 수 없다.

**필수 수정**

- zero-shot, 독립 calibration k-shot, 피험자 내 기준을 분리하고 모든 calibration은 평가 내용군과 겹치지 않게 한다. 동일 보정 예산·readout 차원을 적용한다.
- 각각 새 성분/새 관계조합/새 ID를 구분하고 train에서 모든 test 성분이 나타나는지와 사건 역할 조합의 support를 감사한다.
- 동일 시험 자극에서 자극-only 관계/내용 판별을 평가하여 언어표현 자체 실패와 신경 mapping 실패를 구분한다.
- 정서 대비의 평가 방향은 train에서 고정하고 주석 코호트·개인 신뢰도 차이를 모델링한다. 영상을 쓰면 같은 장면/인접 구간이 calibration과 test에 섞이지 않게 한다.

**더 강한 판별 대조**

자극-only 조합 예측 × 개인/공유 좌표 × 0/k-shot calibration을 동일 내용군에서 비교한다. 자극-only는 성공하는데 공유 신경 공간만 실패하고 calibration으로 회복되는 경우와, 모든 좌표에서 자극-only부터 실패하는 경우를 판별적 결과로 사전 규정한다.

**부정 결과의 가치**

실패 원인을 표현·매핑·측정의 최소 세 층으로 제한할 수 있다. 다섯 보유 자료에 공통 자극/ontology가 없으면 자료 내 검정만 수행하고 pooling 성공·실패를 주장하지 않는다.

**남은 이견**

피험자마다 정서주석의 측정 대상이 다르면 의미와 좌표의 2축만으로 실패를 설명할 수 없다. 측정 불변성을 추가한 해석이 필요하다.

근거: P015, P062, P079, P083, P100

## 후보 간 중복과 구별

- C06-01, C10-03, C05-02, C05-03: 공통 대상은 시간별 정서 신경 대비지만 조작은 예측목표/상태, 사건순서, 모달리티별 창, 경계 reset으로 다르다. 동일 데이터·통제를 공유할 수 있으나 현재는 이름만 보고 병합하지 않는다.
- C06-02, C06-04: 정보종류의 보존/억제 대 적응 성능과 신경 손실의 tradeoff로 추정량이 다르다. 같은 guide 손실 곡선만 남으면 병합해야 한다.
- C06-05, C10-02: 자극 성분의 새 조합 상호작용 대 뇌 영역 간 조합의 조건부 증분으로 관측 단위·조작이 다르다. 둘 다 비가산성을 말하지만 같은 질문은 아니다.
- C10-01, C10-04: 언어 병목의 보존량 대 생성 내용의 신경/언어 prior 출처로 다르다. 생성 전후 비교를 공유해도 각각 손실과 정보 기원이 주추정량이다.

## 출처 검증 범위

출처 ID는 기존 canonical 레지스트리와 실제 대조했다. 아래 제목·링크는 신규 원문 검증을 뜻하지 않는다.

- [P001 · The neural representation of visually evoked emotion is high-dimensional, categorical, and distributed across transmodal brain regions](https://raw.githubusercontent.com/OpenNeuroDatasets/ds002425/3f94b2bf9a75ddb62637c529d30dc40dd4ab5ba1/dataset_description.json): E2
- [P002 · Emo-FilM: A multimodal dataset for affective neuroscience using naturalistic stimuli](https://raw.githubusercontent.com/OpenNeuroDatasets/ds004892/cdf68fe448ad180a476fa2371473a1a6ed063774/dataset_description.json): E2
- [P007 · Generalizable representations of pain, cognitive control, and negative emotion in medial frontal cortex](https://raw.githubusercontent.com/canlab/Neuroimaging_Pattern_Masks/master/Multivariate_signature_patterns/2018_Kragel_MFC_Generalizability/Kragel_2018_NatNeurosci_MFC_generalizability.pdf): E1
- [P008 · Emotion schemas are embedded in the human visual system](https://raw.githubusercontent.com/canlab/Neuroimaging_Pattern_Masks/master/Multivariate_signature_patterns/2019_Kragel_Emotion_Schemas/Kragel_2019_SciAdv_emotion_schemas.pdf): E1
- [P013 · V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning](https://raw.githubusercontent.com/facebookresearch/vjepa2/main/README.md): E1
- [P015 · MindEye2: Shared-Subject Models Enable fMRI-To-Image With 1 Hour of Data](https://github.com/MedARC-AI/MindEyeV2): E2
- [P021 · Brain-Diffuser: Natural scene reconstruction from fMRI signals using generative latent diffusion](https://github.com/ozcelikfu/brain-diffuser): E2
- [P042 · Temporal Cycle-Consistency Learning](https://github.com/google-research/google-research/tree/master/tcc): E1(공식코드·README 범위);논문본문 미검증;신경전이는E3
- [P045 · VideoMAE: Masked Autoencoders are Data-Efficient Learners for Self-Supervised Video Pre-Training](https://arxiv.org/abs/2203.12602): E1-공식 README/코드 한정; 논문 본문 E0; 전이 주장 E3
- [P046 · Revisiting Feature Prediction for Learning Visual Representations from Video](https://arxiv.org/abs/2404.08471): E1-공식 README/코드 한정; 논문 본문 E0; 전이 주장 E3
- [P049 · Invariant Risk Minimization](https://arxiv.org/abs/1907.02893): E1-공식 README/코드 한정; 논문 본문 E0; 전이 주장 E3
- [P050 · Who Needs Labels? Adapting Vision Foundation Models With the Metadata You Already Have](https://arxiv.org/abs/2606.05107): E1-공식 README/코드 한정; 논문 본문 E0; 전이 주장 E3
- [P053 · Challenging Common Assumptions in the Unsupervised Learning of Disentangled Representations](https://proceedings.mlr.press/v97/locatello19a.html): E1(본문); 정서·뇌 전이는 E3
- [P062 · neuromaps: structural and functional interpretation of brain maps](https://github.com/netneurolab/neuromaps/blob/main/markello2022natmethods.pdf): E1-논문 본문 및 Discussion 직접 확인
- [P066 · Discovering event structure in continuous narrative perception and memory](https://github.com/brainiak/brainiak/blob/master/src/brainiak/eventseg/event.py): E1-공식 코드 및 tutorial; 논문 본문·Discussion 미확인
- [P067 · Brain network dynamics are hierarchically organized in time](https://github.com/OHBA-analysis/HMM-MAR): E1-공식 코드/문서 범위; 논문 본문·Discussion 미확인
- [P079 · Learning Transferable Visual Models From Natural Language Supervision](https://raw.githubusercontent.com/mlresearch/v139/gh-pages/radford21a/radford21a.pdf): E1(선택 본문·공식 코드); 전이 E3
- [P081 · BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models](https://raw.githubusercontent.com/mlresearch/v202/gh-pages/li23q/li23q.pdf): E1(선택 본문·공식 코드); 전이 E3
- [P083 · Concept Bottleneck Models](https://raw.githubusercontent.com/mlresearch/v119/gh-pages/koh20a/koh20a.pdf): E1(선택 본문); 전이 E3
- [P084 · Label-free Concept Bottleneck Models](https://github.com/Trustworthy-ML-Lab/Label-free-CBM): E2(서지/공식 요약); E1은 별도 명시한 코드·문서만; 전이 E3
- [P085 · The neural architecture of language: Integrative modeling converges on predictive processing](https://github.com/mschrimpf/neural-nlp): E2(서지/공식 요약); E1은 별도 명시한 코드·문서만; 전이 E3
- [P086 · Scaling laws for language encoding models in fMRI](https://github.com/HuthLab/encoding-model-scaling-laws): E2(서지/공식 요약); E1은 별도 명시한 코드·문서만; 전이 E3
- [P087 · Semantic reconstruction of continuous language from non-invasive brain recordings](https://github.com/HuthLab/semantic-decoding): E2(서지/공식 요약); E1은 별도 명시한 코드·문서만; 전이 E3
- [P089 · Deep Predictive Coding Networks for Video Prediction and Unsupervised Learning](https://github.com/coxlab/prednet): E1: 직접 열람한 공식 코드/문서에 한정; E2: 서지·README 논문요약; E3: transfer_idea; 본문/Discussion 미확인
- [P098 · WILDS: A Benchmark of in-the-Wild Distribution Shifts](https://proceedings.mlr.press/v139/koh21a.html): E1
- [P099 · In Search of Lost Domain Generalization](https://github.com/facebookresearch/DomainBed): E1
- [P100 · Statistical inference on representational geometries](https://elifesciences.org/articles/82566): E1
- [P101 · Representational models: A common framework for understanding encoding, pattern-component, and representational-similarity analysis](https://github.com/rsagroup/rsaModelComparison): E1

## 한계

- Round3로 실제 수행한 범위는 자기 Round2 및 배정된 Agent06·Agent10의 JSON/Markdown 검토, 총 10후보에 대한 8항목 비판과 판정이다. 다른 역할과의 응답·합의 또는 Round4를 실행했다고 주장하지 않는다.
- 기존 canonical 문헌 레지스트리를 대조했다. 이 라운드에서 새 원문 열람·외부 신규성 역검색·실자료 분석·모델 실행은 하지 않았다. 인용은 기존 검증 범위의 방법/배경 근거이며 새로운 신경 실증을 뜻하지 않는다.
- 다섯 자료 보유를 유지하되 경로·버전·스키마 확인을 문헌 연구의 차단 조건으로 사용하지 않는다. C06-05 보류는 데이터 미확인 일반론이 아니라 unseen 조합 상호작용의 추정 구조가 미정이라는 구체적 식별 문제다.
- 시간 가설에는 관찰 가능한 과거, feature 가용시점, 원시간 HRF, 평정 지연, 영화/내용군 분할과 buffer를 요구했다. Spacetop clip 평정을 연속 주석으로 늘리지 않는다. Emo-FilM의 별도 평정 코호트를 개인 뇌 정답으로 동일시하지 않는다.
- Speech Features 및 기타 제외 주제를 새 연구축으로 도입하지 않았다. 텍스트 사건 의미는 caption 내용의 표현 문제로 다루며 음성 세부 특징 분석으로 확장하지 않는다.
- 유지 1개는 검증된 가설이라는 뜻이 아니라 핵심 설계의 논리적 유지다. 수정·보류 판정도 유망 질문의 폐기가 아니며 수정 후 재검토가 필요하다.
- 통계적 영효과는 사전 정한 최소 효과를 배제할 정밀도가 있을 때만 반증으로 해석한다. 불충분한 신뢰도·관측 연산 후 비식별은 별도 결과다.
- 작성 범위는 Agent05 round03_critique.json/md 두 파일이다. 타 Agent·공유 산출물·Git은 수정하지 않았다.
