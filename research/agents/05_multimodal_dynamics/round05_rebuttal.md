# Agent05 Round 5 실제 검토 응답

RP03의 Agent11·08, RP04의 Agent06·04 입장을 수집본에서 직접 읽고 답했다. 수용8건이며 남은 식별 한계는 별도로 보존한다. 검토자들이 이 수정안에 다시 동의했다고 주장하지 않는다.

## 응답 1: RP03 / 11_brain_inspired

출처: `agents/11_brain_inspired/round05_debate.json`

**실제 비판**

readout의 같은 boundary indicator만으로 state update의 정보 접근이 같아지지 않는다. 명시적 forgetting은 비명시 상태함수에 정확히 흡수될 수 있다.

**응답 — 수용**

모든 주대조의 state update와 readout에 같은 b_t를 같은 available time에 제공한다. h_t=F((1−rho_t)h_prev+rho_t h0,x_t)와 F_tilde(h,x,b)=F((1−rho(b))h+rho(b)h0,x)의 exact functional control을 같은 가중치로 만들고 동일 출력을 확인하도록 계획했다. 이 둘은 하나의 함수 동치류이며 독립 기전으로 비교하지 않는다. 제목·결론도 제한된 parameterization의 예측 효용으로 축소했다.

**남은 이견**

유연한 상태함수가 같은 연산을 구현할 수 있으므로 미시적 기억 소거는 식별 불가능하다. 유한 예산에서의 효용은 남을 수 있다.

## 응답 2: RP03 / 11_brain_inspired

출처: `agents/11_brain_inspired/round05_debate.json`

**실제 비판**

random forgetting의 norm/예상오차 matching은 처리 이후 상태에 조건화할 수 있고, 사후 경계·미래 smoothing이 online 검정에 섞일 위험이 있다.

**응답 — 수용**

위치 매칭은 forgetting을 적용하지 않은 공통 reference head의 사전 상태·과거에 도착한 오차·컷/음향 onset으로만 한다. boundary time_available, zero-phase 필터 금지, prefix feature 범위를 명시한다. 사후 인간 경계는 retrospective 분기로 격리하고 위치 대조를 실험적 무작위배정 null로 부르지 않는다.

**남은 이견**

자연 사건경계와 내용 변화의 완전한 분리는 보장되지 않는다. 위치특이 효용은 관찰 범위의 주장이다.

## 응답 3: RP03 / 08_systems_neuroscience

출처: `agents/08_systems_neuroscience/round05_debate.json`

**실제 비판**

한 A 대비와 loss를 고정하고 외부 consensus를 개인 정답으로 취급하지 않아야 한다. 반복 신경자료를 가정하면 안 된다.

**응답 — 수용**

PILOT02의 주석은 실제 annotation dictionary에서 확인한 Fear 한 항목으로 고정한다. 개발에서 동일 target projection u_A와 lag를 정하고 모든 head에 같은 z_A를 사용한다. 현재 개인 내 동일 영화 독립 반복은 확인되지 않았으며 test–retest noise ceiling을 계산 가능하다고 가정하지 않는다. 외부 A와 held-out z_A 관계, 참가자/영화별 효과와 측정오차 민감도를 분리한다.

**남은 이견**

반복이 없으면 개인 신경 대비의 반복 신뢰도와 잡음상한을 직접 추정할 수 없다. 참가자 간 일치는 그 대체가 아니다.

## 응답 4: RP03 / 08_systems_neuroscience

출처: `agents/08_systems_neuroscience/round05_debate.json`

**실제 비판**

reset·연속 gate·유한창이 HRF 이후 같은 예측을 만들 수 있다. 영화14개를 다수 독립 경계창으로 세면 안 된다.

**응답 — 수용**

state기전×경계오차×HRF폭 합성 복구에 상대모형의 nuisance 재적합을 포함한다. exact controls는 동일해야 하며 다른 생성세계도 구분되지 않으면 신경기전 판정을 중단한다. 계획 하위집합은 최대6영화×8명이고 영화 전체 outer split을 사용한다. 작은 영화 수에서는 영화별 손실과 CI를 우선하고 유의성·동등성 확증을 보장하지 않는다.

**남은 이견**

BOLD 관측동등성 내부의 기전 선택은 남긴다. 복구 시뮬레이션의 성공도 가정한 생성세계 밖의 식별을 보증하지 않는다.

## 응답 5: RP04 / 06_frontier_ai

출처: `agents/06_frontier_ai/round05_debate.json`

**실제 비판**

큰 k의 잔차 이득은 유한 shared/readout family의 한계이며 잔차는 독립 또는 biological private 정보가 아니다.

**응답 — 수용**

카드 제목에 사전 지정 병목·판독 범위를 명시했다. R_k=X−g_train(S_k)는 해당 predictor의 operational residual이며 통계 독립을 뜻하지 않는다. S_k+R_k가 원정보의 가역 재표현인 설정은 full X와 같은 정보 접근 대조로 표기한다. 모든 조건에 같은 ridge/제한 nonlinear family·탐색·seed·학습량 곡선을 적용한다.

**남은 이견**

유한 k와 자료량에서 shared 표현이 충분히 강하다는 보편 기준은 없다. 결과는 명시한 family의 예측 충분성으로만 보고한다.

## 응답 6: RP04 / 06_frontier_ai

출처: `agents/06_frontier_ai/round05_debate.json`

**실제 비판**

정서 특수성은 같은 자극의 신뢰도·난도를 맞춘 비정서 대비와 비교해야 한다. 좌표 난도와 정보 절단을 구분해야 한다.

**응답 — 수용**

동일 자극·참가자에서 z_A와 사전 정의 z_C의 D_k를 공통 train 표준화로 비교하는 선택성 검정을 부차 분기로 추가한다. 이것이 없거나 효과가 동등하면 정서 관련 대비에서도 나타나는 일반 압축/접근성 결과라고 명명한다. 알려진 가역변환·rank 절단 신호주입과 학습량 회복을 먼저 검사한다.

**남은 이견**

z_A와 z_C의 측정 신뢰도·난도가 완전히 같다고 보장할 수 없다. 정서 선택성은 추가 조건을 통과한 범위에서만 쓴다.

## 응답 7: RP04 / 04_brain_foundation

출처: `agents/04_brain_foundation/round05_debate.json`

**실제 비판**

파일의 오디오와 실제 스캐너 내 오디오 재생을 구분하고 독립 대비·내용군·FactorCL 감독 경로를 확인해야 한다.

**응답 — 수용**

실제 presentation 로그/공식 프로토콜과 원음원 매핑을 착수 계약에 둔다. Horikawa 재생이 확인되지 않으면 해당 시청각 분기를 실행하지 않고 재생조건이 확인된 Emo-FilM으로 전환한다. u_A·분해·readout·표준화는 모두 outer train 안에서 적합하고 독립 test A/BOLD로 재선택하지 않는다. FactorCL 감독이 미확인일 때는 frozen cache+train-only 투영으로 좁힌다.

**남은 이견**

현재 실제 보유본의 AV 재생·숫자주석·체크포인트 load는 확인되지 않았다. 데이터 보유와 실행 준비를 구분한다.

## 응답 8: RP04 / 04_brain_foundation

출처: `agents/04_brain_foundation/round05_debate.json`

**실제 비판**

이벤트 수와 독립 표본수를 구분하고 반복을 가정하지 않아야 한다. Horikawa 5명 exact 양측 sign-flip은 최소 p=0.0625다.

**응답 — 수용**

내용 중복은 같은 fold에 묶고 2,196행을 독립 자극 수로 세지 않는다. 개인 내 반복은 현재 미확인이라고 명시했다. 5명만의 모든 부호반전 32개에서 양측 최소 p=2/32임을 카드에 기록하고 p<0.05 보장을 제거한다. 참가자별 효과와 내용군 조건부 불확실성을 병기하며 정밀도 부족은 충분성 입증이 아니다.

**남은 이견**

새 참가자 모집단 추론은 5명 표본으로 제한된다. 자극 수·voxel 수 증가는 참가자 수를 대체하지 않는다.

## 상세계획 반영

- RP03: 동일 경계 접근·exact absorbed-function 대조·HRF 후 복구·개인 내 반복 미확인·Fear 단일 대비를 카드와 PILOT02에 반영했다.
- RP04: 운영적 잔차의 비독립성·동일 함수족·학습곡선·실제 오디오 제시·5명 통계 한계를 반영했다.
- 상세 카드와 파일럿은 계획 완료 상태이며 실제 파일·모델 load·신경 분석을 완료했다고 표시하지 않는다.
- 공유 파일·타 Agent·Git을 수정하지 않았다.
