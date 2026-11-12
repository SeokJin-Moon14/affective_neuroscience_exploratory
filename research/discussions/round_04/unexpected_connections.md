# Round4의 실제 새 연결27개

각 역할이 Round3 비판을 읽은 후 추가한 연결이다. 외부 분야의 원래 계산 목적과 전이 구조를 구별한다. 새 신경 질문은 E3이며 원 논문 저자의 후속 제안으로 돌리지 않는다.

## UC10-1 — 순차 Bayesian 실험설계와 개념 질의

**원래 계산 목적:** P077은 설계–관측 history에서 다음 실험을 고르는 정책으로 반복 설계 비용을 줄인다. P083 §8은 인간 질의로 개념을 학습·정제할 가능성을 논의한다.

**옮긴 구조:** 다음 자극을 생성하는 대신 어떤 독립 중립 관계 주석을 다음에 수집할지 선택한다. 후보 관계 질의의 기대 정보가 관계특이 중복 가설과 일반 타깃설명력 가설을 얼마나 구별하는지 훈련 자료에서 평가한다.

**새 신경 질문:** 제한된 추가 의미 주석 예산에서 어떤 관계를 확인해야 정서 관련 N-D 감소의 두 설명을 가장 잘 구분하는가?

**Round2와 다른 점:** Round2는 미리 정한 객체/관계 특징을 비교했다. 여기서는 미측정 의미 중 다음 관측을 적응적으로 선택하는 측정 정책 자체를 새로 도입한다. 단순 모델·데이터명 교체가 아니다.

**assumptions:** 관계 주석은 뇌·정서라벨을 보지 않는 별도 주석자가 제공 / 주석 likelihood와 불확실성을 정의할 수 있어야 정확한 Bayesian 설계 명칭 사용 가능 / P077의 연속 설계·조건부 독립·명시적 likelihood 가정이 이산·상관 주석에 자동 성립하지 않음 / 불충족 시 이산 enumeration 또는 disagreement 휴리스틱으로 명칭을 낮추고 exact EIG를 주장하지 않음

근거: [P077](https://proceedings.mlr.press/v139/foster21a.html); [P083](https://raw.githubusercontent.com/mlresearch/v119/gh-pages/koh20a/koh20a.pdf); [P100](https://elifesciences.org/articles/82566)

## UC10-2 — 잡음 역문제의 복수 해와 신경 지도 정렬

**원래 계산 목적:** P076은 잡음 관측과 diffusion prior를 결합해 신호를 근사 복원한다. P062는 좌표가 다른 뇌 지도의 변환·비교를 다루며 개인/집단 변환의 한계를 밝힌다.

**옮긴 구조:** 관측과 양립하는 자극 후보의 복수성이라는 구조를 자극 대신 신경 mapping의 복수성으로 옮긴다. 독립 calibration에서 비슷한 손실을 갖는 mapping family를 사전에 허용하고 이후 의미 일반화 결론이 모든 허용 mapping에서 유지되는지 본다.

**새 신경 질문:** 특정 정렬 하나에서 보이는 새 의미조합의 정서 신경 예측 실패는 calibration으로 구별할 수 없는 다른 mapping에서도 유지되는가?

**Round2와 다른 점:** Round2는 개인/공유 mapping 중 선택한 모형의 요인 비교였다. 여기서는 선택을 하나로 고정하지 않고 허용 mapping 전체에서의 결론 범위를 주타깃으로 바꾸었다. P076의 원신호 생성과도 다른 추정 대상이다.

**assumptions:** 독립 calibration 관측과 noise/reliability 기반 사전 허용오차 / 후보 mapping family의 유한 coverage 한계를 명시 / 같은 test 성능으로 허용 mapping을 선택하지 않음 / 허용집합을 posterior 또는 진짜 신경 등가군으로 해석하지 않음

근거: [P076](https://github.com/DPS2022/diffusion-posterior-sampling); [P062](https://github.com/netneurolab/neuromaps/blob/main/markello2022natmethods.pdf); [P100](https://elifesciences.org/articles/82566)

## UC05-01 — 통계적 식별성과 표현 유사도

**원래 계산 목적:** P053은 무감독 latent disentanglement의 식별 한계를, P051은 신경망 표현 비교의 적절한 불변성을 다룬다. P037은 shared/private task 정보를 보존한다.

**옮긴 구조:** 좌표 재표현과 정보원 접근을 분리한다. 같은 정보를 보유한 직교 좌표 변환은 대조이고, 정보원 가림과 병목 크기는 실질 조작이다.

**새 신경 질문:** private 축 이름이 달라도 추가 모달리티 접근의 정서 신경 대비 이득이 공유 병목 용량에 걸쳐 유지되는가?

**Round2와 다른 점:** Round2는 gate와 특정 private latent의 필요성을 동시에 물었다. 새 연결은 gate를 제거하고 좌표별 특수성 대신 정보원 접근의 충분성 곡선을 추정한다.

**assumptions:** 가역 직교 변환은 정보원을 추가하지 않는 대조이며 새로운 신경기전 검정은 아님 / 유한 readout family에서의 충분성만 추정 / 원문 이론을 정서 신경표상 식별 정리로 확장한 주장은 E3

근거: [P053](https://proceedings.mlr.press/v97/locatello19a.html); [P051](https://proceedings.mlr.press/v97/kornblith19a.html); [P037](https://github.com/pliang279/FactorCL)

## UC05-02 — 시스템 식별·표현모형 선택

**원래 계산 목적:** P034/P089의 상태 갱신은 효율적 시퀀스 계산/영상 예측을 위한 구조이며 P101은 encoding·PCM·RSA를 표현모형 비교 틀로 연결한다.

**옮긴 구조:** 서로 다른 잠재 기전의 합성 데이터를 같은 관측 family에 통과시키고 각 대립모형이 nuisance 파라미터를 train에서 최적으로 적합하도록 허용한 뒤 복구 혼동을 검사한다.

**새 신경 질문:** 모달리티 기억 차이나 경계 forgetting의 필요성이 encoder filter·HRF·초기상태 prior가 조정된 경쟁 설명에서도 관측상 남는가?

**Round2와 다른 점:** Round2의 공통 HRF와 matched reset만으로 충분하다고 두지 않는다. 실제 자기상관을 유지한 대립 생성세계와 모형별 nuisance 재적합을 포함해 설명 가능한 동등성을 먼저 찾아낸다.

**assumptions:** 합성 세계는 실제 뇌를 확정하는 모델이 아님 / 개발 자료로 정한 노이즈·효과마진과 실제 자극 구조를 사용 / 공통 family가 동일 nuisance 값 강제를 뜻하지 않음

근거: [P034](https://github.com/state-spaces/mamba); [P089](https://github.com/coxlab/prednet); [P101](https://github.com/rsagroup/rsaModelComparison); [P100](https://elifesciences.org/articles/82566)

## UC05-03 — 비선형 ICA의 보조변수 식별·시퀀스 대응

**원래 계산 목적:** P054는 auxiliary variables를 사용한 nonlinear ICA 식별을, P042는 속도가 다른 시퀀스의 cycle correspondence를 다룬다.

**옮긴 구조:** 외부 landmark를 좌표의 방향/상대 진행을 제한하는 보조 앵커로 두고 완료된 미래 시퀀스가 아닌 현재까지 관찰된 landmark 이력으로 진행을 표현한다.

**새 신경 질문:** 미래 종료점을 모르는 상황에서도 독립 landmark 이력이 시계시간 이상의 정서 신경 대비를 설명하는가?

**Round2와 다른 점:** 단순 full-sequence TCC 정렬이 아니라 prefix state와 retrospective 좌표를 분리하고 외부 앵커의 측정 타당성부터 검증한다. C01-02 병합 설계의 새 식별 조건이다.

**assumptions:** landmark는 정서/BOLD를 보지 않고 정의 / 독립 landmark의 인과적 관찰 시점을 기록 / nonlinear ICA 정리의 조건이 뇌 사건 상태에 만족된다고 주장하지 않음

근거: [P054](https://proceedings.mlr.press/v89/hyvarinen19a.html); [P042](https://github.com/google-research/google-research/tree/master/tcc); [P053](https://proceedings.mlr.press/v97/locatello19a.html)

## UC01-01 — 조건부 계산·도메인 일반화

**원래 계산 목적:** P093은 입력별 일부 전문가를 활성화하여 계산량과 전체 용량을 분리하고 P098은 환경 밖 일반화를 평가한다.

**옮긴 구조:** 입력descriptor가 공유 파라미터를 조절하는 구조를 미관측 내용군의 관측변환 예측으로 전이한다.

**새 신경 질문:** 고정 정서 방향이 실패해도 내용descriptor에 의해 조절되는 같은 연산은 새 내용군으로 전이하는가?

**Round2와 다른 점:** 내용 그룹/검색 후보 정의를 넘어 held-out 내용군에 존재하지 않는 dummy 계수 문제를 해결하는 함수 구조를 도입했다.

**assumptions:** descriptor 공통 지지 / 조건부 함수는 train에서만 적합 / MoE 성능은 신경 routing 근거가 아님

근거: [P093](https://github.com/google-research/vmoe); [P098](https://proceedings.mlr.press/v139/koh21a.html); [P051](https://proceedings.mlr.press/v97/kornblith19a.html)

## UC01-02 — 순차 영상 예측·시간 대응 학습

**원래 계산 목적:** P089은 과거 영상에서 다음 입력을 예측하고 P042는 비디오 단계의 순환 일관적 대응을 학습한다.

**옮긴 구조:** 현재 입력집합을 과거 prefix로 제한하는 예측 구조와 전체 시퀀스 대응을 분리하여 실제 종료를 아는 oracle를 독립 대조로 둔다.

**새 신경 질문:** 정서 신경 대비의 사건단계 이득은 현재에 계산 가능한 상태에서 오나 사후 정렬에서만 오나?

**Round2와 다른 점:** 기하 재매개화의 평가에서 입력 정보의 시간 방향을 검정하는 반사실 비교로 바뀌었다.

**assumptions:** prefix 경계 감사 / 예상 duration은 train에서 추정 / 실제 종료는 oracle만 사용

근거: [P089](https://github.com/coxlab/prednet); [P042](https://github.com/google-research/google-research/tree/master/tcc); [P066](https://github.com/brainiak/brainiak/blob/master/src/brainiak/eventseg/event.py)

## UC01-03 — Bayesian experimental design·비대응 형상 정합

**원래 계산 목적:** P077은 관측 이력에서 다음 설계를 골라 정보 획득을 높이고 P057은 서로 다른 거리행렬을 수송으로 정렬한다.

**옮긴 구조:** 비슷한 수송비용인데 다른 정서/신경 대비를 예측하는 해들을 구별할 bridge를 고른다. likelihood/posterior가 없으면 heuristic disagreement임을 명시한다.

**새 신경 질문:** 어떤 외부 측정이 공통 모양에서 정서 관계와 실제 신경 전이를 분리하는 데 필요한가?

**Round2와 다른 점:** 불확실성을 보고하는 데서 끝나지 않고 그 불확실성을 줄일 새 측정의 종류와 독립 검증 단계를 설계한다.

**assumptions:** 후보 결합과 측정 noise model 명시 / 선택용 bridge와 최종평가 bridge 분리 / 신경 주장에는 양쪽 실제 neural anchor 필요

근거: [P077](https://proceedings.mlr.press/v139/foster21a.html); [P057](https://proceedings.mlr.press/v48/peyre16.html); [P100](https://elifesciences.org/articles/82566)

## UC09-01 — 역문제의 제약충족 탐색 × Bayesian 실험설계

**원래 계산 목적:** P076은 잡음 관측에 양립하는 신호의 근사 복원, P077은 순차 설계 전체의 정보 이득을 효율적으로 선택하는 것이 원 목표다.

**옮긴 구조:** 전체 해집합을 추정한다는 요구를 버리고 서로 다른 두 유효해라는 witness를 고정한 뒤 추가 관측으로 배제하는 반복 구조를 도입한다. 반례를 이용한 정제라는 연결은 E3이며 별도 형식검증 논문을 확인했다고 하지 않는다.

**새 신경 질문:** 어떤 독립 반복/사전지정 contrast 관측이 정서에 관해 상반된 모델조건부 자극 설명을 처음으로 배제하는가?

**Round2와 다른 점:** Round2의 후보 최소–최대 범위는 탐색 완전성을 암묵적으로 요구했다. 새 연결은 이미 찾은 witness의 생존/탈락으로 추정량을 바꾸고 추가 측정의 가치를 구체적 양자 설명의 구별로 한정한다.

**assumptions:** witness의 인간 주석 차이·자연성 검증 / 별도 forward와 독립 관측의 calibration / 새 관측을 보기 전에 witness 고정 / 유한 sampler의 미발견을 증명으로 쓰지 않음

근거: [P076](https://github.com/DPS2022/diffusion-posterior-sampling); [P077](https://proceedings.mlr.press/v139/foster21a.html); [P053](https://proceedings.mlr.press/v97/locatello19a.html); [P100](https://elifesciences.org/articles/82566)

## UC09-02 — 분포 이동 학습 × 표상 통계의 모집단 추론 × 생성 편집

**원래 계산 목적:** P098은 서로 다른 domain·subpopulation에 대한 일반화 평가, P100은 참가자·자극 모집단의 표상 추론, P070은 구조를 보존하는 텍스트 편집이 원 목표다.

**옮긴 구조:** 편집 허용 필터를 품질검사만이 아니라 평가 대상 모집단을 바꾸는 선택 연산자로 취급한다. 조건부 효과·coverage·domain별 누락을 함께 정의한다.

**새 신경 질문:** 의미 보존을 엄격하게 요구할수록 어떤 원본 내용·정서 강도 영역이 관측 가능한 신경대비 모집단에서 빠지며, 남은 허용영역의 대비는 두 구현에서 유지되는가?

**Round2와 다른 점:** Round2는 타당성 필터로 실패를 제거하면 평가가 개선된다는 구상이었다. 새 연결은 필터 자체가 결과의 적용 범위를 바꾼다는 질문으로 전환하며 pass/fail 효과와 원모집단 외삽을 철회한다.

**assumptions:** 모든 편집 시도·실패·선별 규칙 기록 / 개발에서 허용영역과 target population 고정 / A/내용/자연성 공통 support / 선택확률 0인 영역에 가중치로 일반화하지 않음

근거: [P098](https://proceedings.mlr.press/v139/koh21a.html); [P100](https://elifesciences.org/articles/82566); [P070](https://raw.githubusercontent.com/prompt-to-prompt/prompt-to-prompt.github.io/main/ptp_files/Prompt-to-Prompt_preprint.pdf)

## UC06-01 — 표현 불변성과 서로 다른 학습 계산의 기능 등가성

**원래 계산 목적:** P051은 표현 유사성 지표의 불변성을, P096의 확인된 코드/서지는 다른 학습 계산과 역전파 비교를 다룬다. 프로그램 동등성 일반이론을 새로 검증했다고 주장하지 않는다.

**옮긴 구조:** 입출력 함수를 보존하는 재매개화를 음성 대조로 삼아, 같은 예측을 구현하는 여러 내부 좌표에서 개별 feature 중요도가 얼마나 달라지는지 시험한다.

**새 신경 질문:** 동일 모델 함수가 정서 신경 대비를 똑같이 예측하면서 다른 개념 중요도를 부여하면 어떤 수준의 개념–신경 대응만 식별되는가?

**Round2와 다른 점:** Round2는 SAE seed/width의 경험적 안정성과 제거 효과를 병렬 측정했다. 새 연결은 함수 보존을 수학적으로 정의한 control과 decoder 역변환을 넣어 좌표 변화만으로 해석이 바뀌는지를 직접 반박한다.

**assumptions:** 허용 재매개화가 모델 후속 출력·복원 함수를 실제로 보존하는지 수치 확인 / 임의 회전이 sparse 분포를 보존한다고 가정하지 않음 / 동등성은 고정 입력·readout·오차허용폭에 한정

근거: [P051](https://proceedings.mlr.press/v97/kornblith19a.html); [P096](https://github.com/BerenMillidge/PredictiveCodingBackprop); [P101](https://github.com/rsagroup/rsaModelComparison)

## UC06-02 — 잠재요인 역문제의 식별성·생성모형 회복과 실험 지지 설계

**원래 계산 목적:** P055는 보조 정보 아래 잠재요인의 식별 조건을 다루고 P101은 공통 생성모형·잡음 조건에서 표현모형 비교를 구현한다. 두 문헌이 본 bilinear 조합의 식별 정리를 제공한다는 뜻은 아니다.

**옮긴 구조:** 데이터를 나눈 뒤 예측을 보는 순서에 앞서, 알려진 생성 신호가 관측 연산자와 train 조합 설계를 통과해 회복되는지 검사하고 지지가 있는 pair 유보만 신경 가설 검정으로 삼는다.

**새 신경 질문:** 정서 조합의 실패가 실제 가산 코드 때문인지 훈련 조합에서 공유 관계 연산을 추정할 수 없었기 때문인지 구별할 수 있는가?

**Round2와 다른 점:** Round2의 low-rank라는 방법명만으로는 미관측 pair의 예측식을 정하지 못했다. 새 연결은 공유 함수·gauge·설계조건수·positive recovery를 정의하여 음성 결과의 의미를 바꾼다.

**assumptions:** 연결 그래프만으로 식별성을 보장하지 않음 / synthetic recovery는 지정한 생성모형 범위의 검증일 뿐 뇌가 그 모형이라는 증거가 아님 / 관측 HRF·주석 잡음·표집 구조가 simulation에 반영되어야 함

근거: [P055](https://proceedings.mlr.press/v108/khemakhem20a.html); [P101](https://github.com/rsagroup/rsaModelComparison); [P100](https://elifesciences.org/articles/82566)

## UC12-01 — 식별 가능한 표현학습·비선형 ICA

**원래 계산 목적:** P055는 보조변수로 조건화한 latent prior와 명시적 모형 가정 아래 비선형 잠재요인의 식별성을 연구한다. P053는 무감독 disentanglement의 식별 한계를 다룬다.

**옮긴 구조:** 목표 출력에 맞춘 잠재축 대신 독립 보조 anchor와 공유 제약을 먼저 정하고 여러 미사용 표적이 동일 구조를 만족하는지 검정한다. 맥락 합성규칙은 이 문헌이 입증한 뇌 결과가 아니라 새 E3 확장이다.

**새 신경 질문:** 정서 독립 anchor가 고정한 맥락 변환은 학습하지 않은 맥락 조합에서 여러 정서 신경 대비를 동시에 예측하는가?

**Round2와 다른 점:** Round2의 단일 조건부 readout 비교는 재매개화로 동등할 수 있었다. 독립 anchor 고정·다중 표적·미관측 요소 합성이라는 추가 예측을 도입하며 제목과 주장을 실질적으로 좁혔다.

**assumptions:** anchor는 정서 test target과 독립적으로 정의한다. / 변환군·기준좌표·복잡도·합성규칙은 train 내부에서 사전 고정한다. / iVAE의 생성모형·보조변수 가정을 뇌자료가 충족한다고 가정하지 않는다. / 맥락 조합의 공통 지지와 독립 다중 대비가 필요하다.

근거: [P055](https://proceedings.mlr.press/v108/khemakhem20a.html); [P053](https://proceedings.mlr.press/v97/locatello19a.html); [P051](https://proceedings.mlr.press/v97/kornblith19a.html)

## UC12-02 — 부분 관측 제어의 world model·잠재 rollout 재사용

**원래 계산 목적:** P048의 공식 DreamerV3 코드/문서는 환경 상호작용의 world model 및 상상 rollout을 통한 제어 학습을 다룬다. P013 공식 V-JEPA2 문서는 영상 이해·예측·계획을 위한 잠재 모델을 제공한다. 논문 본문·Discussion은 이번 작업에서 확인하지 않았다.

**옮긴 구조:** 하나의 상태가 한 출력만 맞추는 것이 아니라 복수 후속 경로에 재사용되는 제약을 가져온다. 수동 관람자에게 action/reward를 부여하지 않고, 실험자가 교차 배치한 후속 사건군에 대해 동일 prefix 상태의 다중 예측을 고정한다.

**새 신경 질문:** 같은 현재 장면에서 과거 이력이 남긴 상태는 단순 HRF 잔류 이상으로 여러 후속 사건군의 정서 관련 신경 상호작용을 공통 규칙으로 예측하는가?

**Round2와 다른 점:** Round2는 동일현재/상이과거의 단일 현재 대비였다. 이제 이력×후속사건군을 교차해 한 상태가 독립 후속 분기들에 동시에 적용되는지 검정한다. 별도 RQ 수를 늘리지 않고 C12-03의 발견 확장으로 포함한다.

**assumptions:** 후속 사건은 이력 조건과 counterbalance하며 같은 현재 probe와 지연을 유지한다. / 과거/후속 자극의 정서 주석은 모델에서 생성하지 않고 독립 측정한다. / 모든 비교 상태는 현재까지의 prefix만 보고, 후속 실제 입력을 허용하는 진단과 분리한다. / 일반 적응·의미상태와 HRF/FIR family가 같은 상호작용을 설명하는지 비교한다.

근거: [P048](https://arxiv.org/abs/2301.04104); [P013](https://raw.githubusercontent.com/facebookresearch/vjepa2/main/README.md); [P089](https://github.com/coxlab/prednet); [P100](https://elifesciences.org/articles/82566)

## UC04-01 — 역문제·관측 영공간 감사

**원래 계산 목적:** P076은 잡음 있는 역문제에서 관측 제약과 생성 prior를 결합해 가능한 해를 찾는다. 정확한 posterior 보장이나 fMRI 적용 결과는 확인되지 않았다.

**옮긴 구조:** 관측 연산이 같은 값을 내는 방향을 직접 구성하고 그 방향이 외부 표적을 바꾸는 witness인지 검사한다. 여기서는 생성기 대신 알려진 parcel 평균 행렬의 null space를 정확히 구성한다.

**새 신경 질문:** 동일한 parcel 평균을 유지하면서 바뀌는 재현 공간 대비가 A 관련 예측을 바꾸는가?

**Round2와 다른 점:** 단순 표현 유사도/병목 전후 성능이 아니라 Gr=0인 소거 성분을 정의해 재추가하는 판별 조작이 새로 생겼다. 일반 평균화와 atlas 특수성을 별도 가설로 분해한다.

**assumptions:** 알려진 비중첩 평균 행렬과 동일 dense 관측 / 독립 반복에서 r의 신뢰도를 검증 / 신경 측정공간 밖 숨은 신호나 실제 뇌 압축 연산으로 일반화하지 않음

근거: [P076](https://github.com/DPS2022/diffusion-posterior-sampling); [P026](https://github.com/MedARC-AI/CortexMAE); [P060](https://github.com/rsagroup/rsatoolbox)

## UC04-02 — 알고리즘 비교의 관측 동치 통제·가역 좌표군

**원래 계산 목적:** P051은 어떤 변환을 허용해야 표현 비교가 구별력을 가지는지, P096은 predictive coding과 backprop 계산을 비교하는 문제를 다룬다. P096의 원문 등가 정리 전체는 미확인이다.

**옮긴 구조:** 표현의 좌표/관측 map만 다른 모형과 추가 상태가 필요한 모형을 분리하고, 알려진 동치 생성자료를 음성대조로 사용한다.

**새 신경 질문:** 안정된 개인 잔차는 공통 latent의 gain/rotation/affine 관측 차이로 설명되는가, 그 지정군을 넘어서는 개인 성분이 필요한가?

**Round2와 다른 점:** shared/private 잔차의 재현성만 검사했던 질문에 명시적 허용 좌표군과 coordinate-only recovery 대조를 도입해 새 경쟁모형을 만든다.

**assumptions:** 가역군은 동일 차원에서 명시하고 condition number 제약을 고정 / 관측 head와 공유 latent 학습은 training-only / 선택한 군의 실패를 모든 nonlinear 가역군 실패로 확장하지 않음

근거: [P051](https://proceedings.mlr.press/v97/kornblith19a.html); [P055](https://proceedings.mlr.press/v108/khemakhem20a.html); [P096](https://github.com/BerenMillidge/PredictiveCodingBackprop)

## UC04-03 — 계산 구조의 동치/비동치와 recurrence 대 depth 비교

**원래 계산 목적:** P090은 얕은 재귀 시각모형의 계산 성능을, P096은 다른 학습 계산의 대응을, P034는 입력 의존 selective sequence 계산을 다룬다.

**옮긴 구조:** 최종 예측 성능이 다른 경우 비선형성의 존재와 위치를 별도 요인으로 고정하여 어느 계산 경로가 필요한지 반례를 찾는다.

**새 신경 질문:** A 관련 이력 예측의 이득은 nonlinear observation만으로 충분한가, 고정 전이의 gated input 또는 입력 의존 전이가 추가로 필요한가?

**Round2와 다른 점:** 관측격자×fixed/selective 이분법에 input gate와 transition gate를 분리하는 세 함수족 대조를 추가해 용량 혼동을 직접 겨냥한다.

**assumptions:** 공통 nonlinear input/output 및 같은 real-time context / 고정 수렴/예산 결과 구분 / gate shuffle OOD와 재학습 제어 구분

근거: [P090](https://github.com/dicarlolab/CORnet); [P096](https://github.com/BerenMillidge/PredictiveCodingBackprop); [P034](https://github.com/state-spaces/mamba)

## UC02-01 — 표현학습의 식별성 이론·비선형 ICA

**원래 계산 목적:** P053은 가정 없는 분리표현의 비유일성을, P055는 보조변수와 명시적 분포·혼합 가정 아래 식별 조건을 연구한다.

**옮긴 구조:** 좌표 수가 남는 것과 같은 요인이 남는 것을 구분하고, 복수 조건화 설명 아래 동일 외부 대비의 기능적 전이라는 과잉 제약을 둔다.

**새 신경 질문:** 내용모형별 잔차 rank가 아니라 같은 정서 관련 neural contrast가 공통 좌표에서 교차 설명에 살아남는가?

**Round2와 다른 점:** Round2의 generative inverse 후보집합을 반복하지 않는다. 서로 직교한 양의 rank라는 반례로 원 하한 주장을 철회하고 고정 방향의 전이행렬을 새 추정량으로 삼는다.

**assumptions:** 신경 좌표 고정·평가 중 정렬 금지 / 독립 정서 대비와 조건화 모델의 사전정의 / 식별 정리의 fMRI 적용은 주장하지 않음

근거: [P053](https://proceedings.mlr.press/v97/locatello19a.html); [P055](https://proceedings.mlr.press/v108/khemakhem20a.html); [P001](https://raw.githubusercontent.com/OpenNeuroDatasets/ds002425/3f94b2bf9a75ddb62637c529d30dc40dd4ab5ba1/dataset_description.json); [P007](https://raw.githubusercontent.com/canlab/Neuroimaging_Pattern_Masks/master/Multivariate_signature_patterns/2018_Kragel_MFC_Generalizability/Kragel_2018_NatNeurosci_MFC_generalizability.pdf)

## UC02-02 — 비모수 조건부독립 검정과 국소 순열

**원래 계산 목적:** P102는 조건부 mutual information의 추정과 국소 permutation을 이용한 검정 calibration을 다룬다. 고차원 조건집합과 표본수 제약이 있다.

**옮긴 구조:** 무조건 교란 대신 사전정의 내용·SNR 지지 안에서 신경 입력의 조건부 관계만 깨는 null을 만들어 라벨 우회와 실제 brain 경로를 구별한다.

**새 신경 질문:** 조건부 지역 readout의 이득은 C가 주어졌을 때 신경 패턴 B와 독립 정서주석 A의 추가 관계를 필요로 하는가?

**Round2와 다른 점:** Round2는 V-MoE의 gate 구조를 수입했다. 이번에는 통계 검정의 교환가능성 구조를 가져와 gate 성능이 content→A 우회인지 진짜 B 의존인지 반박하며 A를 조건으로 고정하지 않는 이유까지 명시한다.

**assumptions:** B|C의 근사 교환·support가 사전 calibration되어야 함 / run·참가자 의존성을 보존하고 train/test 분리 / 정확한 CMI나 조건부독립 검정이 검증되었다고 주장하지 않음

근거: [P102](https://proceedings.mlr.press/v84/runge18a.html); [P093](https://github.com/google-research/vmoe); [P005](https://raw.githubusercontent.com/canlab/Neuroimaging_Pattern_Masks/master/Multivariate_signature_patterns/2015_Chang_PLoSBiology_PINES/Chang_2015_PLoSBiol_PINES.pdf)

## UC07-01 — 순차 Bayesian experimental design

**원래 계산 목적:** 비싼 posterior 재계산 없이 과거 설계·관측에 따라 정보획득을 높이는 다음 실험을 선택한다(P077).

**옮긴 구조:** 정렬결합을 확정해야 할 미지 가설로 두고 다음 비정서 anchor를 선택하는 순차 측정정책; 적합도 최대화 대신 보류 대비의 식별가능성 증가를 목표로 한다.

**새 신경 질문:** 감각/의미 관계의 어떤 관측을 추가하면 독립 정서 신경대응이 결정되며 정서 감독은 불필요해지는가?

**Round2와 다른 점:** Round2는 수송해 비유일성과 anchor 수 증가를 비교했다. 이제 동일 개수의 anchor 선택 목적·종류를 바꾸고 비정서 감독으로 미사용 정서 대비가 전이하는지를 주표적으로 삼는다.

**assumptions:** E1은 기존 P077 선택본문과 P057 본문 범위이며 현재 신경전이는 E3. / Bayesian EIG를 쓰려면 명시 likelihood/prior·설계 조건 가정 필요; 단순 다중시작해를 posterior라 하지 않음. / 미사용 정서평가를 anchor 선택에 노출하지 않는다.

근거: [P077](https://proceedings.mlr.press/v139/foster21a.html); [P057](https://proceedings.mlr.press/v48/peyre16.html); [P052](https://proceedings.mlr.press/v235/huh24a.html)

## UC07-02 — 비모수 조건부독립 검정과 변수집합 충분성

**원래 계산 목적:** 연속 변수의 비선형 의존이 조건변수에 의해 설명되는지 local permutation/CMI로 검정한다(P102).

**옮긴 구조:** 특정 predictor의 개선과 정보원의 조건부 추가의존을 별개로 평가하는 두 단계; 본인 신경이력을 타참가자 공통자극 관측으로 치환하여 조건집합을 강화한다.

**새 신경 질문:** 미래 정서 관련 신경대비에 본인 과거 관측이 필요한가, 풍부한 자극·다른 참가자·nuisance 이력으로 충분한가?

**Round2와 다른 점:** Round2의 joint 대 additive 모델위험 비교만으로는 누락입력과 함수표현의 효과가 섞였다. 새로운 연결은 조건부 의존과 함수계열 내 비가산성을 다른 estimand로 두고 본인/타인 정보원 치환을 도입한다.

**assumptions:** P102의 기존 본문 검토는 일반 조건부검정의 범위이며 fMRI 특수조건은 E3. / TR을 i.i.d.로 취급하지 않는다. 독립 영화/블록의 유효표본과 local permutation 타당성을 별도 검증한다. / 고차원 BOLD 직접 CMI는 계획하지 않고 사전 정의 저차원 투영이 충분할 때만 보조 검정한다.

근거: [P102](https://proceedings.mlr.press/v84/runge18a.html); [P027](https://github.com/facebookresearch/tribev2); [P037](https://github.com/pliang279/FactorCL)

## UC08-01 — 표현학습의 비식별성·불변성 및 시스템 식별

**원래 계산 목적:** P053은 관측만으로 잠재 요인 분해가 유일하지 않은 문제를, P051은 표현 비교에서 허용 변환에 따라 동등성이 달라지는 문제를 다룬다. P028은 상태공간의 예측 표현을 제공한다.

**옮긴 구조:** 예측이 같은 두 생성설명을 먼저 명시하고 그 동치류를 깨는 독립 측정을 요구한다. 예: 같은 합성커널을 만드는 HRF/신경필터 두 분해, 같은 목적함수를 만드는 graph 공동 재색인.

**새 신경 질문:** 어떤 정서 문맥·관계 효과가 관측 동치류를 넘어 식별되며 어떤 생리적 해석은 추가 정보 없이는 불가능한가?

**Round2와 다른 점:** Round2는 대체모형의 성능 비교였다. 이번 연결은 정확히 같은 관측을 만드는 모의쌍/공동 재색인을 음성대조로 고정하고 원래 신경시간상수·경로 주장을 축소한다.

**assumptions:** convolution 분해는 E3 예시이며 문헌이 정서 HRF 실험을 수행했다는 뜻이 아니다. / 모의 동치쌍의 동일성이 수학적으로 또는 수치적으로 확인되어야 한다. / 생리적 분해는 독립 HRF 제약 등 추가 자료가 있어야 한다.

근거: [P051](https://proceedings.mlr.press/v97/kornblith19a.html); [P053](https://proceedings.mlr.press/v97/locatello19a.html); [P028](https://proceedings.mlr.press/v248/behrouz24a.html)

## UC08-02 — 정적 표현기하 비교와 확률과정의 시간전이 식별

**원래 계산 목적:** P051은 표현간 기하 비교를, P067은 잠재 관측상태의 시간 조직을, P066은 사건분절을 다룬다.

**옮긴 구조:** 같은 emissions·점유분포 또는 같은 정적 공간기하를 가진 과정도 iid/연속/이산 전이가 다를 수 있다는 구조를 사용한다. 정적 분포를 고정하고 시간정보만 남는 예측을 검사한다.

**새 신경 질문:** 정서 주석 예측에 필요한 것은 비정규 공간분포의 압축인가, 비대각 시간구조 또는 전이가 제공하는 추가 정보인가?

**Round2와 다른 점:** Round2의 mean/covariance HMM 비교는 진폭·분포·전이를 함께 바꿨다. 새 연결은 같은 공간관측을 만드는 동등 emissions와 시간변화를 분리하고 이산 HMM 실재 주장을 검증 대상으로 낮춘다.

**assumptions:** 동일 emissions mixture와 HMM 비교는 점유분포·model capacity를 맞춘다. / 연속 null의 주변분포·자기상관 적합성이 확인되어야 한다. / state label 순열에 불변인 예측통계만 해석한다.

근거: [P051](https://proceedings.mlr.press/v97/kornblith19a.html); [P066](https://github.com/brainiak/brainiak/blob/master/src/brainiak/eventseg/event.py); [P067](https://github.com/OHBA-analysis/HMM-MAR)

## UC11-01 — 표현 비교의 불변성·계산 그래프 검증

**원래 계산 목적:** P051은 신경망 표현 유사성 비교를, P096은 예측부호화와 역전파 계산 관계를 다룬다. P090의 반복 블록은 유한 계산 그래프로 펼칠 수 있는 구현이다.

**옮긴 구조:** 같은 정보·함수에 대한 재매개화와 정확한 계산 경로 변환을 검정의 등가 통제로 삼는다.

**새 신경 질문:** 표현 좌표의 효율과 인간 신경 계산 구현의 식별을 나눴을 때, 독립 정서 대비가 실제로 제약하는 것은 어느 수준인가?

**Round2와 다른 점:** Round2의 모델 변수 분해를 넘어, 동일 함수이면 같아야 하는 검정 불변성 조건을 도입하고 그 조건을 통과한 뒤 학습 효율만 비교한다.

**assumptions:** exact-unroll은 모든 상태갱신·정규화·초기상태를 보존해야 함 / readout family가 변환을 흡수하는 조건과 제한 예산의 조건을 분리 / P096의 근사 정리를 모든 구현의 exact equivalence로 일반화하지 않음

근거: [P051](https://proceedings.mlr.press/v97/kornblith19a.html); [P096](https://github.com/BerenMillidge/PredictiveCodingBackprop); [P090](https://github.com/dicarlolab/CORnet)

## UC11-02 — 자극 기반 대체 측정과 교사 신호 검증

**원래 계산 목적:** P027은 자극에서 집단 피질반응을 예측하고 P050은 metadata로 표현의 보존/억제를 지도한다. P100은 표현 추론의 일반화 단위를 다룬다.

**옮긴 구조:** 비용이 큰 실제 신경 교사와 자극만으로 예측한 대체 신경 교사를 cross-fit해 동일 adapter에서 비교한다.

**새 신경 질문:** 신경 측정이 제공하는 감독의 효용은 풍부한 의미로 예측 가능한 교사 정보로 충분한가, 지정된 대체 교사를 넘는 안정된 추가 효용이 있는가?

**Round2와 다른 점:** Round2의 neural/semantic/random guide 비교를 대체 신경 교사와 실제 교사의 같은 target 형식 비교로 바꾸고 교사 생성과 평가의 cross-fitting을 명시했다.

**assumptions:** 자극 predictor와 guide는 outer 평가 신경 데이터를 보지 않음 / 잔차는 순수 정서 또는 완전한 신경 고유정보가 아님 / 교사 신뢰도·공분산·예측되는 자극정보를 보고하되 완전 정보량 매칭을 주장하지 않음

근거: [P027](https://github.com/facebookresearch/tribev2); [P050](https://arxiv.org/abs/2606.05107); [P100](https://elifesciences.org/articles/82566)

## UC03-01 — 표현 기하의 불변성 분석 × 변환 기반 소프트웨어 검증

**원래 계산 목적:** P051은 표현 유사도의 불변성과 구별력을 분석하고 P100은 유연 표현모형의 보류 조건·참가자 평가를 다룬다. 아래 신경 검사를 원논문의 결과로 주장하지 않는다.

**옮긴 구조:** 구성상 정보보존이 알려진 가역 혼합과 일부 입력을 제거한 비가역 절단을 만들고 probe ladder의 오판을 측정하는 양성·음성 대조(E3). CKA가 일반 가역 변환에 불변이라고 가정하지 않는다.

**새 신경 질문:** 정서 대비의 판독 저하는 정렬 목표의 효과인가, 좌표 재표현을 정보삭제로 오판하는 probe의 한계인가?

**Round2와 다른 점:** Round2의 내용 일반화에는 정보보존의 정답이 없었다. 새 연결은 알려진 가역성을 이용해 측정 절차 자체의 실패를 대조한다. 새 정리나 완전한 정보손실 검증은 아니다.

**assumptions:** 가역 변환의 차원·수치 조건을 기록하고 train/test에서 동일 적용한다. / probe 튜닝은 평가 fold 밖에서 한다. / 대조 통과는 모든 비선형 재부호화에 대한 충분성 보증이 아니다.

근거: [P051](https://proceedings.mlr.press/v97/kornblith19a.html); [P100](https://elifesciences.org/articles/82566); [P015](https://github.com/MedARC-AI/MindEyeV2)

## UC03-02 — 통계적 모형 선택 편향 × 비유일 역문제

**원래 계산 목적:** P097은 선택 이후 평가 편향의 서지 근거(E2)이고 P100의 확인 보고서는 유연 모형과 참가자·조건 일반화를 구분한다. P076의 역문제 후보 생성에 이를 옮긴다.

**옮긴 구조:** 후보 universe 구성·거리문턱 보정·최종 신경 판별을 분리하고 정답을 포함한 중첩 자연 후보군 U1⊂U2⊂U3에서 고정 문턱 허용집합을 감사한다(E3).

**새 신경 질문:** 정서 대비의 배제는 같은 신경자료를 후보 선택에 재사용하지 않고도 유지되며 의미 일치 반례를 늘려도 유지되는가?

**Round2와 다른 점:** Round2는 prior와 후보 다양성을 비교했다. 새 연결은 선택 후 평가 편향을 명시적 경쟁 원인으로 만들고 중첩 후보군의 집합 단조성과 독립 참조 유지율을 검사한다. 단순 sampler 교체가 아니다.

**assumptions:** 중첩 비교에서 거리함수·문턱·encoder를 고정한다. / 후보별 점수 정규화를 universe마다 바꾸지 않는다. / U가 전체 자극공간을 덮는다는 보장은 없고 경험적 calibration을 test에서 확인한다.

근거: [P097](https://jmlr.org/papers/v11/cawley10a.html); [P100](https://elifesciences.org/articles/82566); [P076](https://github.com/DPS2022/diffusion-posterior-sampling)

