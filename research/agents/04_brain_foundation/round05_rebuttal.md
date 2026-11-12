# Agent04 Round5 실제 비판에 대한 응답

RP05/RP08의 실제 비판·통계 원본과 수집본을 읽고 작성했다. 새 신경 결과나 만장일치 기록이 아니다.

## RP05 · 10_llm_semantics / 회의적비판자

**비판:** 추가 신경 관측은 원 자극의 풍부한 proxy이므로 S 밖의 이득을 자극 밖 내부 정서 기전으로 해석할 수 없다.

**수용:** 수용한다. 제목과 주장은 지정 S에 대한 독립 관측 문맥의 조건부 예측가치로 제한한다. 객체→관계→사건/맥락→유연한 raw stimulus 모형의 S 강화와 A/비정서 대비를 같이 보고한다. 같은 뇌에서 생성한 caption을 그 뇌 예측 입력으로 되넣지 않는다.

**남은 이견:** 유한 S 강화로 의미 완전성은 입증되지 않는다. 양성 결과도 내부 상태와 미모형화 자극을 구별하지 않는다.

## RP05 · 10_llm_semantics / 회의적비판자

**비판:** 반복 입력의 추가 측정 비용, target 포함 여부, 동시 완성과 미래 예측의 차이를 선언해야 한다.

**수용:** 수용한다. RP05-A는 test 자극에서 target 밖 N_a를 추가로 측정한 공간완성 계약이다. S-only와 같은 입력예산이라고 하지 않으며 동일 N을 쓰는 raw-context ridge를 따로 비교한다. target 자체의 다른 반복을 제공하는 것은 신뢰도 benchmark로 분리한다. RP05-B 과거→미래는 별도 관측 가지로 유지한다.

**남은 이견:** A/B를 한 점수로 합치지 않는다. 독립 반복 존재 미확인으로 A의 신경 실증 착수는 보류한다.

## RP05 · 01_dataset / 데이터통계검토자

**비판:** 전처리 전파로 context에 target이 섞일 수 있어 단순 masking 순서 기술만으로 target-free가 성립하지 않는다.

**수용:** 수용한다. 원입력에서 target와 buffer를 변경해도 고정 전처리 경로의 context feature가 허용 수치오차 안에서 불변인지 직접 확인하는 게이트를 둔다. affine H를 명시할 수 있으면 context←target block이 0인지도 확인한다. 이미 비가역 혼합된 처리본밖에 없어 이를 입증할 수 없으면 독립 문맥 가설을 착수하지 않는다.

**남은 이견:** 유한 perturbation 검사는 일반 nonlinear 경로의 수학적 독립성 증명이 아니다. 구현 구조 감사와 함께 사용하고 검증 범위를 명시한다.

## RP05 · 01_dataset / 데이터통계검토자

**비판:** 반복 a/b가 실제 독립 측정인지, 적응·nuisance와 N 신뢰도 차이를 별도로 확인해야 한다.

**수용:** 수용한다. 참가자·동일 원자극 hash·run/session·노출순서·측정일의 mapping을 요구한다. Horikawa 2,196개 고유 ID와 dupidx는 그 증거가 아니다. 같은 run 다른 자극뿐 아니라 A/내용/context 신뢰도 일치 다른 자극 N을 대조하며 Q·w·mask는 train에서 고정한다.

**남은 이견:** 반복 적응과 안정 nuisance는 완전히 제거되지 않을 수 있다. 음성 결과를 독립 문맥 정보 부재로 단정하지 않는다.

## RP08 · 08_systems_neuroscience / 회의적비판자

**비판:** 영공간의 존재는 자명하며 강한 nonlinear mean-only가 잔차 이득을 회수할 수 있다.

**수용:** 수용한다. H1 주비교에 tuned ridge와 kernel ridge 또는 작은 MLP의 m-only를 넣고 같은 정보입력·선택예산·nested tuning을 유지한다. 잔차 k곡선을 train-selected primary k와 함께 전체 보고한다. 일반 MVPA 우위만 확인되면 공간 QC 모듈로 낮춘다.

**남은 이견:** 제안자는 제한된 접근성 검정도 첫 파일럿 가치가 있다고 보지만 비판자는 정서 선택성과 반복 없이는 독립 과학 RQ의 신규성이 약하다고 본다. 이 소수 의견을 보존한다.

## RP08 · 08_systems_neuroscience / 회의적비판자

**비판:** 면적가중 G/P, 타깃 척도, k와 신뢰도 선택을 명확히 해야 한다.

**수용:** 수용한다. C를 비중첩 parcel membership, W를 고정 양의 voxel-volume/vertex-area 가중으로 두고 G=(CᵀWC)⁻¹CᵀW, P=CG를 정의한다. H3는 train 표준화한 A와 비교가능한 비정서 B의 paired-risk interaction으로 고정한다. 원효과와 신뢰도/공간대역 matching 후 효과를 모두 보존한다.

**남은 이견:** 면적 정보가 없으면 W=I인 명시적 무가중 관측만 수행한다. 동일 rank는 동일 정보량이 아니며 모든 타깃의 난도/신뢰도를 완전히 맞출 수 없다.

## RP08 · 11_brain_inspired / 데이터통계검토자

**비판:** Horikawa 5명과 고유 이벤트 ID는 반복 신뢰도나 강한 사람 모집단 추론을 보장하지 않는다.

**수용:** 수용한다. 첫 PILOT03은 다섯 명 각각과 그 참가자들에 조건부인 새 자극 일반화만 평가한다. 독립 반복이 실제 없으면 반복 noise ceiling과 반복 재현 witness를 계산하지 않는다. 내용 중복·복사본·다른 사람의 같은 자극을 개인 내 반복으로 바꾸지 않는다. 양측 exact sign-flip 최소 p=.0625와 집단 CI의 불안정성을 명시한다.

**남은 이견:** 새 자극에서의 접근성 이득은 반복 신호의 안정성과 다른 증거다. 참가자 모집단 일반화/반복 주장은 별도 자료를 요구한다.

## RP08 · 11_brain_inspired / 데이터통계검토자

**비판:** H1/H2/H3·k·atlas 탐색과 잘못된 label permutation이 conditional null을 흐릴 수 있다.

**수용:** 수용한다. H1을 일차, H2/H3를 사전 순서가 있는 별도 이차 가족으로 둔다. k/alpha/basis/atlas 선택은 내부훈련에만 두고 primary k와 고정 k곡선을 같이 보고한다. A 무조건 permutation은 평균의 실제 신호도 제거하므로 H1 정확 null로 부르지 않는다. known m-only 생성 null과 reduced-model 적합·exchangeability를 점검한 residual resampling을 별도로 사용한다.

**남은 이견:** 조건부 null의 오지정 위험이 남는다. 대조가 실패하거나 precision이 부족하면 확증이 아니라 방법 점검으로 제한한다.

