# Agent05 Round 2: 멀티모달 시간 계산의 교차 정보 교환

작성일: 2026-11-12. 실제 수행: Agent01·Agent11 원본 보고서 교차 읽기, 두 원리 수입, 구별되는 후보 다섯 개 생성. 신경 분석과 후속 라운드는 미실행. 모든 신경 가설은 E3이며 출처 검증 범위는 아래 별도 기록한다.

## 원리 수입

### 01_dataset → Agent05

- 읽은 파일: `agents/01_dataset/round1_independent_report.md`
- 원래 문제: 서로 다른 자극 ID·영화시간·스캐너시간·평정 시점을 안전하게 연결하는 metadata 및 관측 단위 문제
- 수입 원리: 잠재 과정과 관측 연산자 분리: 내용군 독립 분할, annotation 지연과 HRF의 별도 모형화, 연속 평정과 clip 평정의 타입 구분
- 새 질문: 멀티모달 시간창과 사건단계 효과가 관측 지연과 집계 단위에 의존하지 않고 독립 정서 대비를 설명하는가?
- 실제 수정: 시간모델 비교마다 공통 HRF 계열을 적용하고 Emo-FilM은 별도 평정 코호트라는 조건을 명시한다. Spacetop 사후 clip 평정을 시간별 정답으로 늘리지 않는다.
- 적용 후보: C05-01, C05-02, C05-03, C05-04, C05-05

### 11_brain_inspired → Agent05

- 읽은 파일: `agents/11_brain_inspired/report.md`
- 원래 문제: 영상 예측에서 상태/오차를 분리하고 조건부 계산에서 gate 선택과 전문가 내용을 구별하는 문제
- 수입 원리: 계산에 이용된 경로와 표현 내용의 구분, 상태 reset의 위치를 맞춘 대조, 관측 연산 후 판별 가능성 점검
- 새 질문: 공유·고유 모달리티 경로와 사건경계 상태 갱신이 내용 표현이나 단순 평활화 이상의 설명을 요구하는가?
- 실제 수정: 고유 경로의 추가 변수만 넣는 접근에 gate/content 통제를 추가하고, boundary reset은 matched-random reset과 비교한다. V-MoE의 시간 gate는 원 논문 기능이 아닌 새 확장임을 표시한다.
- 적용 후보: C05-01, C05-03, C05-05

## 후보 구분

| ID | 독립 조작 | 경쟁 설명 |
|---|---|---|
| C05-01 | 모델 내 고유 경로 포함/제거와 gate/content 분리 | 공유 충분성 대 고유 내용 대 계산용량 |
| C05-02 | Lv×La 조작과 공통 관측지연 모형 | 모달리티별 통합 대 자기상관·HRF 착시 |
| C05-03 | 동일 모델의 reset 위치·횟수와 유한창 | 사건 선택적 갱신 대 연속 기억·일반 drift |
| C05-04 | 사건 단계 좌표 대 elapsed/normalized time | 의미적 진행 대 위치암기·편집·HRF 정렬 |
| C05-05 | joint 대 additive 모델 및 독립 congruence 조건 | 조건부 비가산적 결합 대 감각 품질·의미량 |

## C05-01 · 공유 통로와 고유 경로의 필요성을 내용과 경로 선택에서 분리

연결 Axis: AS34, AS26, AS29, AS31

**핵심 질문**

공유 시청각 내용이 같은 수준으로 설명되는 조건에서도 고유 모달리티 경로가 독립 정서주석과 관련된 뇌패턴의 추가 정보를 제공하는가?

**신경 표적**

시각·청각 감각계와 transmodal parcel의 자극별 패턴; 독립 실측 주석 관련 총/공유/조건부 설명분을 별도 평가

**수입 원리**

Agent11의 gate–content 분해와 Agent01의 내용 중복군 분할을 FactorCL의 공유/고유 표현에 연결한다.

**1단계 모델 적용**

동일 인코더의 공유 latent S, 시각 고유 Vp, 비음성 음악·환경음 고유 Ap로 readout을 만들고, 고유 경로를 포함한 모델과 동차원 공유-only 및 고정 gate 모델을 비교한다.

**2단계 과학 질문**

모달리티 간에 교환되는 정보로 충분한지, 교환되지 않은 내용 또는 경로 선택도 정서 관련 신경표상에 필요한지 구분한다.

**3단계 가정 도전**

공통 검색공간이 좋아지면 신경적으로 중요한 정보도 충분히 보존된다는 가정을 시험한다. 부정 결과는 해당 분해·측정 단위에서 고유 경로의 필요성을 제한한다.

**주가설**

저수준·의미 통제 후에도 S+Vp+Ap의 검증자료 증분이 S-only보다 크고, 이 증분이 독립 정서 대비와 대응한다. gate 추가 이득은 별도로 추정한다.

**경쟁 설명**

추가 효과는 더 많은 파라미터·미측정 의미·감각 SNR 또는 gate가 재표현한 자극 내용으로 충분하다.

**측정 대비**

내용군 및 피험자 보류에서 ΔR²(S+Vp+Ap 대 S), ΔR²(gate+content 대 content)를 분리한다. 모델 예측 신경패턴의 독립 주석 대비 재현도를 총 BOLD 점수와 별도 평가한다. 모든 잔차화·차원선택은 훈련 fold 안에서 수행한다.

**반증·식별불가 기준**

차원/성능/의미 통제 뒤 private 증분의 사전 정한 최소 효과에 대한 상한이 충분히 작으면 필요성 가설을 기각한다. 신뢰도 부족이면 식별불가다. gate-only 이득으로 private 내용 필요성을 대체 주장하지 않는다.

**Baseline**

- 공유-only ridge
- 동일 차원 무작위 projection·정규화 강도 대조
- 시각+오디오 nonlinear additive readout
- 고정/균형/무작위 gate
- 객체·장면·움직임·음량·스펙트럼 baseline

**데이터 계획**

- primary: Horikawa의 실제 시청각 자극 가용성부터 확인하여 자극 단위 검정. 시각-only 보유본이면 이 데이터에서 멀티모달 검정을 하지 않는다.
- validation: Emo-FilM에서 영화 단위 분할 및 정렬 가능한 시간 집계로 재검증. Spacetop은 실제 task의 clip 수준 뇌·평정 대응으로만 재검증한다.
- auxiliary: NSD는 시각 경로의 내용·신뢰도 대조만. Mind Captioning은 정확한 자료 식별·모달리티·주석 확인 이후 의미 통제 후보다.
- fallback: 추가 학습 FactorCL을 실행하기 어렵다면 고정 시청각 특징의 cross-fitted 공유/잔차 투영을 쓴다. 이 잔차를 유일한 생물학적 private latent로 부르지 않는다.

**미확인 조건**

- 각 보유본의 실제 오디오·영상 제공 범위와 재생 조건
- 독립 정서주석·반복 신뢰도
- 분해의 seed/회전 안정성
- Horikawa dupidx와 내용군 매핑

**근거 canonical ID**

- P035
- P037
- P093
- P001

**가까운 기존 문헌**

- P035
- P037
- P093

**새 질문과 원래 문제의 차이**

정보 보존 목적과 조건부 경로 선택을 함께 대조하여 공유공간 충분성·고유 내용 필요성·gate 재표현을 분리한다. 원 논문들의 검색·분류 목표를 신경적 충분성 검정으로 바꾼다.

**신규성 위험**

기존 shared/private encoding의 재평가에 그칠 수 있다. 표상 분해가 비유일하며 gate 번호를 신경회로로 해석할 수 없다.

**개념적 서명**

- observation: 공유/고유 경로가 예측한 정서 관련 신경 대비
- manipulation: 모델 내 고유 경로 포함/제거와 gate/content 분리
- competing_explanations: 공유 충분성 대 고유 내용 대 계산용량

**필수 여덟 질문**

- q1: 관련 연구의 부재를 확인하지 않았다. 과거의 공유공간 성능과 고유정보 필요성 평가의 목적 차이가 공백 후보다.
- q2: 공개 shared/private 코드와 내부 gate 변수로 내용·선택을 별도 비교할 수 있다.
- q3: 공유 latent가 모든 정서 관련 신경정보를 보존한다는 가정.
- q4: 시청각의 고차원 공통·고유 구조를 기술할 수 있지만 신경적 우월성은 미검증이다.
- q5: 공유공간에서 제거된 채 원 뇌에 남는 정보가 후보이며 불완전한 감각 baseline과 경쟁한다.
- q6: 자원 배분용 gate 감사와 내용군 독립성 원리를 정보 보존 평가에 옮긴다.
- q7: 기존 자극을 공통 검색공간의 충분성을 반박할 수 있는 자료로 사용한다.
- q8: 양성 결과는 교환정보와 보유정보의 구분을 요구하고, 음성 결과는 고유 경로 필요성의 범위를 제한한다.

**상태**

발전: E3 새 가설; 실자료 분석·신규성 확정 전 조건부 준비


## C05-02 · 모달리티별 과거 창의 비대칭과 측정 지연의 분리

연결 Axis: AS35, AS32, AS17, AS34

**핵심 질문**

같은 시청각 사건에서 시각과 음악·환경음의 서로 다른 과거 창이 공통 시간창보다 정서 관련 뇌변동을 잘 구별하며, 그 차이가 HRF와 평정 지연으로 설명되지 않는가?

**신경 표적**

시간 정렬된 감각/transmodal parcel BOLD와 독립 주석 대비; 모달리티별 이력의 검증자료 예측 차이

**수입 원리**

Agent01의 잠재 시간과 관측지연 분리; Agent11의 관측 연산 후 모델 판별 원리.

**1단계 모델 적용**

동일 동결 특징에 시각 창 Lv와 오디오 창 La를 독립 적용한 작은 causal convolution/readout을 비교한다. 창은 t 이전 입력만 허용하며 최적화는 nested leave-film-out 안에서 한다.

**2단계 과학 질문**

신경적 통합에 공통 기억 길이가 충분한지, 모달리티별 과거 가용정보의 차이가 필요한지 시험한다.

**3단계 가정 도전**

더 긴 통합창을 더 느린 신경 계산으로 해석하는 가정을 시험한다. 단순 고정 지연으로 설명되면 모달리티별 기억 가설을 철회한다.

**주가설**

La≠Lv 모델이 공통창 모델보다 독립 정서 대비를 안정적으로 예측하고 공통 HRF/FIR 계열 및 평정지연 민감도에도 차이가 유지된다.

**경쟁 설명**

특징 자체의 자기상관, 컷/음향 onset 밀도, HRF 모형 부적합, 인코더의 숨은 미래 접근이 비대칭을 만든다.

**측정 대비**

사전 정한 소수 창 조합의 2차원 성능면에서 ΔR²(자유 La,Lv 대 La=Lv)를 평가한다. 같은 HRF 후보집합·복잡도 벌점·특징 차원을 사용하고 모달리티 자기상관을 맞춘 null 및 신호주입 복구를 비교한다.

**반증·식별불가 기준**

유연한 공통 관측모형에서 비대칭 이득이 사라지거나 관측 연산 후 창 차이를 복구하지 못하면 신경적 창 비대칭 주장을 중단한다. HRF 이하 시간차나 신경처리 순서를 추정하지 않는다.

**Baseline**

- 공통 시간창
- 현재 프레임/동일 길이 mean pooling
- 단일 지연만 다른 모델
- 차원·파라미터를 맞춘 causal convolution
- 자기상관을 보존한 블록 null

**데이터 계획**

- primary: Emo-FilM의 연속 주석·film onset·BOLD 타임베이스로 조건부 검정. 평정은 스캔 참가자 개인 궤적이 아니라 별도 코호트 관측이다.
- horikawa: 우선 보유본에서 원시 시간계열·자극 재생·주석 단위를 확인한다. clip 집계만 있으면 시간창의 clip-level 예측 비교로 줄이고 신경 시간상수 주장을 하지 않는다.
- validation: Spacetop은 자극 중 BOLD 시간계열은 사용할 수 있지만 clip 평정으로 연속 정서 궤적을 만들지 않는다. NSD는 본 시간 질문에 쓰지 않는다.
- fallback: 새 시간모델 학습 없이 고정 특징의 causal pooling으로 시작. Mind Captioning은 정체·시간 주석 확인 전 핵심 자료로 지정하지 않는다.

**미확인 조건**

- TR·run·자극 재생 시각과 음향 동기
- encoder receptive field와 t 이후 입력 차단 감사
- 평정 지연·신뢰도 및 충분한 영화 수
- HRF×창 식별 가능성 시뮬레이션

**근거 canonical ID**

- P002
- P038
- P043

**가까운 기존 문헌**

- P038
- P043
- P002

**새 질문과 원래 문제의 차이**

모델별 성능순위 대신 하나의 관측모형 아래 두 모달리티의 과거 가용창을 요인화한다. 비대칭 통합과 지연 착시를 직접 경쟁시킨다.

**신규성 위험**

기존 temporal receptive window 연구와 중복 가능성이 높다. 정서 관련 독립 대비와 모달리티별 창 상호작용이 없으면 일반 시간 encoding 방법론으로 낮춘다.

**개념적 서명**

- observation: 시청각별 이력에 따른 정서 관련 BOLD 예측
- manipulation: Lv×La 조작과 공통 관측지연 모형
- competing_explanations: 모달리티별 통합 대 자기상관·HRF 착시

**필수 여덟 질문**

- q1: 시간창 연구는 이미 있다. 모달리티 비대칭과 평정·HRF 지연의 동시 식별이 확인할 공백이다.
- q2: 공개 동결 인코더와 연속 영화 주석이 동일 자극의 모달리티별 과거 비교를 가능하게 한다.
- q3: 최적 창 길이가 곧 신경적 통합시간이라는 가정.
- q4: 여러 길이의 비언어적 시청각 맥락을 일정한 특징공간에서 기술할 수 있다.
- q5: 개인별 문맥 의존 신경분산은 평균 주석과 단일 인코더가 놓칠 수 있다.
- q6: 시스템 식별의 상태/관측 분리를 신경 시간창 검정으로 옮긴다.
- q7: Emo-FilM을 정서 예측 점수 자료가 아니라 통합창과 관측지연의 경쟁 실험으로 사용한다.
- q8: 양성 결과는 모달리티별 이력 필요성을, 음성 결과는 긴 문맥 이득의 관측적 설명을 좁힌다.

**상태**

발전: E3 새 가설; 실자료 분석·신규성 확정 전 조건부 준비


## C05-03 · 사건경계 상태 초기화와 연속 기억의 경쟁

연결 Axis: AS35, AS25, AS23, AS32

**핵심 질문**

독립적으로 정의한 사건경계에서 모델 상태를 초기화한 예측이 연속 상태 또는 동일 빈도 무작위 초기화보다 정서 관련 뇌전이를 잘 설명하는가?

**신경 표적**

사건경계 주변 parcel 패턴 변화와 독립 연속 정서주석 대비; 단순 BOLD 진폭과 별도 평가

**수입 원리**

Agent11의 상태/오차 분해와 reset 비교를 Agent01의 평정/HRF 지연 모형에 결합한다.

**1단계 모델 적용**

고정 시청각 특징과 작은 causal 상태모델에 never-reset, 사건경계-reset, 간격·횟수 맞춤 random-reset, 유한창 조건을 둔다. 경계는 독립 사건주석 또는 훈련 자료의 자극 특징으로 정의한다.

**2단계 과학 질문**

정서 관련 전이를 설명하는 과거 정보가 연속적으로 누적되는지, 사건 단위로 선택적으로 끊기는지 판별한다.

**3단계 가정 도전**

긴 문맥을 보존할수록 정서 관련 계산을 더 잘 포착한다는 가정을 시험한다. reset 이득이 일반 평활화로 설명되면 사건 단위 갱신 주장을 철회한다.

**주가설**

실제 경계 reset이 matched-random보다 독립 정서 전이 대비를 잘 예측하며, 컷·모션·의미 변화 및 상태/오차 baseline 뒤에도 이득을 보인다.

**경쟁 설명**

초기화가 단순 drift·평활화를 줄이거나 컷과 경계의 동시성이 이득을 만든다. 경계 후 입력량 차이가 모델 복구시간 차이를 만든다.

**측정 대비**

ΔR²(boundary reset 대 never/random/window)와 경계 전후 예측 패턴 거리 대비를 동일 HRF 아래 측정한다. 비경계 위치에 컷·음향 onset·이전 경과시간·입력량을 맞춘 대조를 둔다. 반대 방향인 연속 상태 우위도 같은 분석으로 판별한다.

**반증·식별불가 기준**

유한창 또는 matched-random이 같은 효과를 내거나 독립 정서 대비 없이 감각 컷만 설명하면 사건 선택적 갱신 가설을 기각한다. 경계 간격이 HRF보다 짧아 효과가 섞이면 시간기전 판단을 보류한다.

**Baseline**

- never-reset causal state
- 주기/횟수/간격을 맞춘 random-reset
- 동일 과거 길이 mean pooling
- 시각 컷+오디오 onset+의미 변화
- 상태와 예측오차를 분리한 readout

**데이터 계획**

- primary: Emo-FilM의 연속 자극과 주석으로 경계 효과 평가. 영화 단위 분할을 먼저 고정한다.
- horikawa: 원영상 및 시간계열이 확보되면 clip 내부 사건경계 분석; clip마다 상태를 리셋해야 하는 시행구조 자체와 자연 사건경계를 구분한다.
- validation: Spacetop clip 집계 평정은 경계 주변 정서 정답이 아니다. clip-level 요약 관련성만 확인한다. NSD에는 시간 reset 질문을 적용하지 않는다.
- fallback: 독립 경계주석이 없으면 비정서적 자극 변화 경계로 제한하고 사건경계로 확정하지 않는다. Mind Captioning 식별 전에는 서사 경계 자료로 간주하지 않는다.

**미확인 조건**

- 독립 사건경계와 컷 구분
- run/clip 경계와 초기 상태 처리
- 연속 정서주석·평정 lag
- reset 모델의 분포 이탈 및 창 길이 대조

**근거 canonical ID**

- P044
- P089
- P002

**가까운 기존 문헌**

- P089
- P044

**새 질문과 원래 문제의 차이**

원래 영상 예측의 재귀 상태와 장기영상 한계를 사건선택적 기억 유지 대 완전 연속 기억이라는 신경 경쟁 설명으로 변환한다.

**신규성 위험**

Agent11 BI-RQ08과 개념 중복군이다. 본 후보는 경계 위치 특이성과 matched reset에 초점을 두며 최종 RQ 수에서는 동일 조작이면 병합해야 한다. 모델 reset은 뇌 인과개입이 아니다.

**개념적 서명**

- observation: 경계 전후 정서 관련 신경패턴 변화
- manipulation: 동일 모델의 reset 위치·횟수와 유한창
- competing_explanations: 사건 선택적 갱신 대 연속 기억·일반 drift

**필수 여덟 질문**

- q1: 재귀 reset 연구의 부재는 미검증이다. 사건경계 위치 특이성과 독립 정서 대비를 묶은 차이가 공백 후보다.
- q2: 상태를 읽고 초기화할 수 있는 공개 영상 모델과 독립 영화 주석이 있다.
- q3: 장기 문맥 보존이 항상 신경적으로 유익하다는 가정.
- q4: 재귀 상태 유지·소거가 만든 복구 궤적을 명시적으로 예측한다.
- q5: 관객의 유연한 사건 분할은 고정 모델의 경계와 다를 수 있다.
- q6: 모델 내부 개입을 신경 인과성 대신 경쟁 예측 생성에 사용한다.
- q7: 같은 영화 자료를 누적 기억과 사건별 갱신을 가르는 자료로 재사용한다.
- q8: 양성 결과는 기억 유지의 경계 의존성을 제한하고 음성 결과는 일반 평활화 설명의 충분성을 보여준다.

**상태**

발전: E3 새 가설; 실자료 분석·신규성 확정 전 조건부 준비


## C05-04 · 사건 진행 단계와 시계시간에 따른 정서 신경전이의 분리

연결 Axis: AS36, AS32, AS31

**핵심 질문**

내용 계열이 유사하지만 지속시간이 다른 자연 사건에서 정서 관련 신경전이는 경과초보다 사건 진행 단계에 맞출 때 더 안정적으로 일반화하는가?

**신경 표적**

다른 영화/내용군 사이의 정서 관련 parcel 패턴 및 전이 대비; 정렬 전 원 시간좌표의 검증자료 예측

**수입 원리**

Agent01의 타입이 다른 시간좌표와 내용군 독립성; TCC의 cycle correspondence를 위치암기 null과 경쟁시킨다.

**1단계 모델 적용**

비신경 자극 자료에서 학습한 TCC류 단계 좌표와 elapsed-time·normalized-time·DTW를 동일 readout으로 비교한다. 테스트 신경신호나 정서 라벨로 warp를 맞추지 않는다.

**2단계 과학 질문**

정서 관련 코드의 변화가 사건의 의미적 진행을 따르는지, 단순 시간경과·편집리듬에 의해 정렬되는지 묻는다.

**3단계 가정 도전**

서로 다른 시퀀스가 정렬되면 의미적 단계가 발견됐다는 가정을 도전한다. normalized-time과 동등하면 복잡한 사건 좌표의 필요성을 철회한다.

**주가설**

독립 영화와 duration stratum에서 단계 좌표의 추가 설명이 경과초·정규화 시간·컷 밀도를 넘고 실측 정서 대비의 신경전이를 재현한다.

**경쟁 설명**

TCC가 프레임 위치를 세거나 내용 유사성이 정렬을 만들며, HRF와 annotation delay가 이동시킨 곡선을 warping이 강제로 맞춘다.

**측정 대비**

단계 기반 예상 신경변화를 원시간축에 되돌린 다음 HRF를 적용하여 평가한다. 물리시간에서 먼저 HRF를 적용하는 기준을 보존하며 HRF 전후 임의 warping을 섞지 않는다. 내용군×duration holdout에서 단계 모델과 normalized-time 모델의 ΔR² 및 대비 재현도 차이를 측정한다.

**반증·식별불가 기준**

위치-only/normalized-time/DTW가 동일하거나 단계 효과가 같은 영화 내에서만 남으면 사건 진행 가설을 기각한다. 사건군 대응과 duration 변이가 부족하면 식별불가로 보류한다.

**Baseline**

- elapsed seconds
- normalized clip position
- position-only network
- 비신경 특징 DTW
- 컷·음향 onset·motion·semantic-change baseline

**데이터 계획**

- primary: Horikawa의 원영상에서 반복 가능한 사건 계열과 지속시간 변이 여부를 우선 감사한다. 주석이 clip 집계면 clip 수준 단계 요약에 한정한다.
- continuous_test: Emo-FilM에서 독립 사건 매칭을 정의할 수 있을 때 연속 신경전이를 검정한다. 의미가 다른 장면을 속도만 다른 같은 사건으로 간주하지 않는다.
- validation: Spacetop은 clip 평정의 집계 검정만 가능하다. 보유 자료에 없는 재생속도 조작의 뇌반응을 합성하지 않는다.
- fallback: 사건 계열 매칭이 불충분하면 TCC 적용을 보류하고 경과시간 null 감사만 수행한다. NSD는 부적합; Mind Captioning은 정확한 자료·시간정보 확인 후 별도 판단.

**미확인 조건**

- 독립 사건계열 정의와 시간 변이
- 시간 라벨/position shortcut 감사
- 물리시간 기준 HRF·annotation delay
- 내용군 독립 분할과 원시간에서의 평가

**근거 canonical ID**

- P042
- P041
- P002

**가까운 기존 문헌**

- P042
- P041

**새 질문과 원래 문제의 차이**

영상의 동일 동작 정렬 원리를 정서 신경전이의 좌표 선택 문제로 바꾸고, 원시간 관측 연산과 사건시간 표현을 명시적으로 분리한다.

**신규성 위험**

시간 정렬된 뇌 궤적 연구와 중복 가능. 자연 사건은 속도 조작이 아니므로 속도 불변성의 인과 검정이라고 부르지 않는다. TCC 단계 자체의 타당성이 선결 조건이다.

**개념적 서명**

- observation: 내용군 간 정서 관련 패턴 전이의 일반화
- manipulation: 사건 단계 좌표 대 elapsed/normalized time
- competing_explanations: 의미적 진행 대 위치암기·편집·HRF 정렬

**필수 여덟 질문**

- q1: 시간정렬 연구는 존재한다. 정렬 좌표와 신경 관측좌표를 분리한 정서 대비의 추가 가치를 검토한다.
- q2: 공개 cycle-consistency 특징과 시간 주석 자료로 위치 shortcut을 직접 대조할 수 있다.
- q3: 정렬 성공은 의미적 진행의 증거라는 가정.
- q4: 자연 영상의 비선형 진행 대응을 유연하게 기술할 수 있다.
- q5: 뇌의 사건 해석이 모델이 학습한 동작 단계와 일치하지 않을 수 있다.
- q6: 행동영상 정렬 문제를 신경전이의 좌표 선택 검정으로 바꾼다.
- q7: 영상 지속시간의 자연 변이를 사용하지만 조작된 속도의 인과효과로 해석하지 않는다.
- q8: 양성 결과는 단순 시계시간 이상의 사건 좌표를 요구하고 음성 결과는 위치·시간 설명의 충분성을 좁힌다.

**상태**

발전: E3 새 가설; 실자료 분석·신규성 확정 전 조건부 준비


## C05-05 · 감각 불일치 조건에서만 필요한 비가산적 시청각 결합

연결 Axis: AS34, AS29, AS26

**핵심 질문**

독립적으로 확인된 시청각 일치·불일치 조건에 따라 정서 관련 신경 대비를 설명하는 joint 결합의 이득이 달라지며, 각 감각의 독립 효과 합으로 충분한가?

**신경 표적**

일치도 조건별 감각/transmodal 패턴 및 실제 정서주석 관련 신경 대비; 단순 전체 BOLD 이득과 구분

**수입 원리**

Agent11의 경로선택/내용 경쟁을 Agent01의 관측값 타입·독립 평정 원리에 연결한다.

**1단계 모델 적용**

CAV-MAE/MBT의 joint 특징, 같은 인코더의 nonlinear additive 특징, 공유/고유 경로를 비교한다. congruence는 별도 관찰자 평정 또는 정서와 독립된 사건 대응 검증으로 정의한다.

**2단계 과학 질문**

정보 두 개를 함께 사용해서 좋아지는 것인지, 특정 감각 불일치 조건에서 결합 규칙 자체가 달라져야 하는지 시험한다.

**3단계 가정 도전**

joint 모델이 unimodal보다 좋으면 통합 또는 synergy라는 가정을 시험한다. additive 모형이 충분하면 해당 조건의 비가산적 결합 필요성을 철회한다.

**주가설**

불일치 조건에서 ΔR²(joint 대 nonlinear additive)의 정서 관련 대비 이득이 일치 조건보다 크며, 의미·음량·모션·각 모달리티 난도와 신뢰도 통제 뒤에도 유지된다.

**경쟁 설명**

불일치 조건은 희귀 장면·음악 유무·감각 SNR·편집 방식이 달라 joint 모델이 부족한 baseline을 보완할 뿐이다.

**측정 대비**

held-out 영화에서 [joint−additive]불일치−[joint−additive]일치의 사전 지정 상호작용을 평가한다. 층/용량/특징 수를 맞추고 독립 정서주석에 관련된 패턴 대비와 전체 BOLD 증분을 나란히 보고한다. 조건별 표본수와 신뢰도를 맞추거나 불확실성을 계층 모형으로 추정한다.

**반증·식별불가 기준**

비선형 additive 또는 의미·감각 통제 뒤 조건 상호작용의 최소 효과 상한이 작으면 조건부 비가산성 가설을 기각한다. 상호작용이 있어도 정보이론적 PID synergy나 뇌의 인과 통합으로 단정하지 않는다.

**Baseline**

- 각 감각 단독
- 동일 용량 nonlinear additive
- 동일 용량 late fusion
- static gate·조건 비의존 joint
- 감각 품질·음악 유무·장면 의미·컷 통제

**데이터 계획**

- primary: Horikawa 보유 자극에 실제 동시 시청각 입력과 조건 다양성이 있는지 확인. 없다면 Emo-FilM의 자연 일치/불일치 구간을 대상으로 한다.
- annotation: 감각 일치도는 독립 추가 평정이 필요할 수 있다. 정서 평가와 일치도 평가의 주체·시간 단위를 기록하고 AI 일치도 점수를 인간 정답으로 간주하지 않는다.
- validation: Spacetop은 실제 clip-level 조건 및 평정 대응만 사용. NSD는 시청각 불일치 연구에 쓰지 않는다. Mind Captioning은 이름만으로 audiovisual 데이터라고 추정하지 않는다.
- fallback: 자연 불일치 표본이 충분하지 않으면 추가 자극·실측 fMRI 연구의 제안으로 보류. 오디오를 바꾼 합성 자극에 원래 뇌반응을 붙이지 않는다.

**미확인 조건**

- 독립 감각 일치도·정서주석
- 불일치와 저수준/의미 변수의 충분한 겹침
- 각 조건의 효과 식별 가능한 표본수
- Speech Features 제외: 비음성 음악·환경음 구간 선별, 음성 포함 여부는 범위/QC 용도만 사용

**근거 canonical ID**

- P036
- P038
- P041
- P093

**가까운 기존 문헌**

- P036
- P038
- P041

**새 질문과 원래 문제의 차이**

원래 correspondence·event localization·계산량 절감 목적을 감각 불일치에 따라 결합 규칙 필요성이 달라지는지 검정하는 질문으로 바꾼다.

**신규성 위험**

audiovisual congruence 신경연구와 가장 직접적으로 중복할 수 있다. 조건부 정서 대비·강한 additive 대조가 기여를 만들지 못하면 범용 감각 통합 재현으로 낮춘다.

**개념적 서명**

- observation: 일치/불일치 조건의 정서 관련 신경 대비
- manipulation: joint 대 additive 모델 및 독립 congruence 조건
- competing_explanations: 조건부 비가산적 결합 대 감각 품질·의미량

**필수 여덟 질문**

- q1: 시청각 불일치 연구 자체는 기존 분야다. 정서 관련 대비와 강한 nonlinear additive 경쟁이 확인할 차별점이다.
- q2: 공개 융합 모델에서 각 경로와 통합층을 분리할 수 있고 독립 일치도 평정을 추가할 수 있다.
- q3: 두 감각을 결합한 성능 이득이 곧 synergy라는 가정.
- q4: 고차원 시청각 대응 및 불일치를 기술하지만 인간 감각 일치도를 대체하지 못한다.
- q5: 뇌의 맥락 의존 불일치 해석은 모델의 단순 correspondence 점수 밖에 있을 수 있다.
- q6: 조건부 계산의 gate/content 분해를 감각 불일치별 결합 규칙 검정에 적용한다.
- q7: 기존 자연영상의 이질성을 조건부 결합 규칙의 판별 자료로 재사용한다.
- q8: 양성 결과는 언제 가산적 설명이 부족한지 제한하고 음성 결과는 감각 독립 정보 합의 충분성을 지지한다.

**상태**

발전: E3 새 가설; 실자료 분석·신규성 확정 전 조건부 준비

## 출처와 검증 범위

아래 링크는 기존 canonical 문헌 레지스트리에서 대조했다. 이 라운드에서 원문/코드 재접속이나 모델 실행을 하지 않았다.

- [P001 · The neural representation of visually evoked emotion is high-dimensional, categorical, and distributed across transmodal brain regions](https://raw.githubusercontent.com/OpenNeuroDatasets/ds002425/3f94b2bf9a75ddb62637c529d30dc40dd4ab5ba1/dataset_description.json): E2
- [P002 · Emo-FilM: A multimodal dataset for affective neuroscience using naturalistic stimuli](https://raw.githubusercontent.com/OpenNeuroDatasets/ds004892/cdf68fe448ad180a476fa2371473a1a6ed063774/dataset_description.json): E2
- [P035 · ImageBind: One Embedding Space To Bind Them All](https://github.com/facebookresearch/ImageBind): E1(공식코드·README 범위);논문본문 미검증;신경전이는E3
- [P036 · Contrastive Audio-Visual Masked Autoencoder](https://github.com/YuanGongND/cav-mae/tree/master): E1(공식코드·README 범위);논문본문 미검증;신경전이는E3
- [P037 · Factorized Contrastive Learning: Going Beyond Multi-view Redundancy](https://github.com/pliang279/FactorCL): E1(공식코드·README 범위);논문본문 미검증;신경전이는E3
- [P038 · Attention Bottlenecks for Multimodal Fusion](https://github.com/google-research/scenic/tree/main/scenic/projects/mbt): E1(공식코드·README 범위);논문본문 미검증;신경전이는E3
- [P041 · Audio-Visual Event Localization in Unconstrained Videos](https://github.com/YapengTian/AVE-ECCV18): E1(공식코드·README 범위);논문본문 미검증;신경전이는E3
- [P042 · Temporal Cycle-Consistency Learning](https://github.com/google-research/google-research/tree/master/tcc): E1(공식코드·README 범위);논문본문 미검증;신경전이는E3
- [P043 · VideoMamba: State Space Model for Efficient Video Understanding](https://github.com/OpenGVLab/VideoMamba): E1(공식코드·README 범위);논문본문 미검증;신경전이는E3
- [P044 · VideoPrism: A Foundational Visual Encoder for Video Understanding](https://github.com/google-deepmind/videoprism): E1(논문 방법·Limitations 직접+공식코드);신경전이는E3
- [P089 · Deep Predictive Coding Networks for Video Prediction and Unsupervised Learning](https://github.com/coxlab/prednet): E1: 직접 열람한 공식 코드/문서에 한정; E2: 서지·README 논문요약; E3: transfer_idea; 본문/Discussion 미확인
- [P093 · Scaling Vision with Sparse Mixture of Experts](https://github.com/google-research/vmoe): E1: 직접 열람한 공식 코드/문서에 한정; E2: 서지·README 논문요약; E3: transfer_idea; 본문/Discussion 미확인

## 한계와 다음 단계

- 실행 범위는 지정된 원본 보고서 두 역할의 실제 교차 읽기와 후보 생성이다. Round3–5 토론, 원자료 분석, 모델 추론, 신규 외부 검색은 실행하지 않았다.
- 5종 데이터 보유는 사용자 진술로 유지한다. 현재 환경의 실제 경로·버전·모달리티·스키마 검증 완료를 의미하지 않는다. 미확인 스키마는 문헌 연구의 차단 사유가 아닌 후보별 준비 조건이다.
- 모든 신경전이·주가설은 새 가설 E3. 원 보고서의 E1은 읽은 공식 코드/선택 본문에 한정하며 본 후속 Agent가 원문을 새로 검증했다는 뜻이 아니다. 원문 미열람 Discussion을 저자 미래 과제로 인용하지 않았다.
- Speech Features는 연구 축에서 제외한다. 음악/환경음 분석은 실제 자극 범위를 확인하며 음성 세부 특징·음성 정서 분석을 도입하지 않는다.
- 모든 시간 특징은 관찰 시점 t 이후의 입력을 추출 단계에서 차단한다. 양방향 모델 출력은 원형 그대로 causal 예측으로 해석하지 않는다. full-clip 특징은 retrospective 조건으로만 표시한다.
- 평정지연·HRF·sampling을 분리하고 공통 관측모형으로 경쟁한다. 동일 영화의 겹치는 창이 분할을 넘지 않게 하고 훈련/검증 경계에 최대 특징창+관측지연에 맞는 buffer를 둔다.
- Emo-FilM의 별도 평정 코호트와 Spacetop의 clip 평정 단위를 유지한다. Spacetop 평정을 시간축으로 반복하여 연속 정서주석처럼 사용하지 않는다. NSD에 정서 정답을 있다고 가정하지 않는다.
- 검정은 영화/내용군 및 피험자 수준 불확실성, 다중 비교와 신뢰도 상한을 포함한다. 시간점 수를 독립 표본수로 사용하지 않는다. 표본 분할 단위·효과 기준은 실자료 감사 뒤 결과를 보기 전에 고정한다.
- 정서 관련 잔차는 조건화한 특징에 상대적인 추정량이다. 감각/의미와 공유된 정서 정보를 제거할 수 있으므로 총/공유/조건부 설명을 함께 보고한다. 잔차를 정서 고유 기전이라고 명명하지 않는다.
- 모델 내 경로 제거·초기화·합성 입력은 모델 비교용이다. 실제 관측하지 않은 인간 뇌반응·인과효과를 만들지 않는다.
- canonical 문헌을 기존 catalog와 대조했지만 포괄적 신규성 역검색은 미실행이다. 특히 C05-03은 Agent11 BI-RQ08과 병합 검토가 필요하며 C05-02/04/05는 기존 시간창/정렬/시청각 문헌과 겹칠 수 있다.
