# Agent01 Round4: 실제 비판 응답과 수정

2026-11-12. 두 검토자 Agent08·12의 실제 비판 10개에 응답했다. 과학RQ후보 4개와 현재 방법후보 1개를 보존하며, 공동 후보는 중복 집계하지 않는다. 실측 결과가 아니다.

## 비판 응답

### C01-01 — 수정

비판: R3-08-C01-01, R3-12-C01-01

- 수용: 고정방향과 제한적 관측변환 아래 공통 코드의 불변성을 분리한다.
- 수용: unseen-content dummy interaction을 폐기하고 독립 외부 내용descriptor로 예측되는 저차원 조건부 readout을 사용한다.
- 수용: total/conditional 정서 대비와 참가자×내용군 독립 단위를 함께 보고한다.
- 남은 쟁점/정정: 내용별 방향 회전만으로 코드 자체가 변한다고 보았던 원안은 철회한다. 허용 관측변환 밖의 효과도 관측모형 의존적임을 유지한다.
- 남은 쟁점/정정: C12-01과 하나의 내용조건부 전이 RQ로 통합하되 C01의 내용 중복/descriptor 검증을 하위 설계로 남긴다.

불변성의 정의와 미관측 내용군의 예측경로를 구체화하여 QC를 넘는 경쟁 설명을 유지한다.

### C01-02 — 수정

비판: R3-08-C01-02, R3-12-C01-02

- 수용: 실제 종료시점 기반 normalized position은 offline oracle로 제한한다.
- 수용: 경과초·train 예상 duration·prefix-only 의미 진행·actual-duration oracle를 분리한다.
- 수용: C05-04와 한 사건좌표 RQ로 병합하며 원 scanner 시간에서 HRF 적용을 고정한다.
- 남은 쟁점/정정: P068은 cortical micro-architecture/MEG 시계열 특징 논문이므로 사건분절의 직접 선행으로 추가하지 않는다. P066/P042를 가까운 근거로 사용한다.
- 남은 쟁점/정정: 뇌가 종료를 예측할 수 있다는 가능성은 인정하지만 실제 종료를 입력받는 분석과 동일하지 않다.

미래 종료정보 누수와 의미 진행/시간 정규화의 혼동을 제거하고 온라인 주장과 사후 정렬의 성공을 구분한다.

### C01-03 — 수정

비판: R3-08-C01-03, R3-12-C01-03

- 수용: 다중성 코드라는 강한 명명을 외부 평정분포와 연관된 신경 대비로 변경한다.
- 수용: 평정자별 lag·ordinal/유계 척도·결측·유효 N의 측정모형을 독립 개발자료에서 추정한다.
- 수용: 고차 분포는 평균/분산 일치와 원평정 support가 있는 경우의 확장으로 제한한다.
- 남은 쟁점/정정: 분포 관련 신경 대비는 제한된 과학 질문으로 유지한다. 분포가 뇌 안에서 확률적으로 표현된다는 주장은 철회한다.
- 남은 쟁점/정정: 평균이 높거나 분포가 두 봉우리인 사실을 시간적 또는 동일 평정자의 동시성으로 해석하지 않는다.

측정 혼합을 명시적인 대안으로 두고 분포 추정 QC와 독립 신경 설명 증분을 별도 성공조건으로 둔다.

### C01-04 — 수정: 현재 방법후보; 신경 전이 주장은 조건부 discovery

비판: R3-08-C01-04, R3-12-C01-04

- 수용: 당장 가능한 기하 비유일성 검토는 방법후보로 분리한다.
- 수용: 공통 코드 대신 사전 지정 정서 관계와 신경 대비의 전이라는 제한된 추정대상을 둔다.
- 수용: train-only coupling에서 외부 자극 feature→표적 기하의 inductive extension을 명시하고 test neural geometry를 사용하지 않는다.
- 수용: 평정-only anchor와 양쪽 실제 신경 anchor의 역할을 분리하고 fitting/선택/최종검증 bridge를 나눈다.
- 남은 쟁점/정정: R3-08의 보류 판정은 신경 주검정 착수에는 수용한다. 문헌·방법 설계를 멈추는 뜻으로는 적용하지 않는다.
- 남은 쟁점/정정: 유한 해 탐색의 일치가 모든 최적해의 유일성은 아니며 성공도 공통 알고리즘을 확정하지 않는다.

핵심 신경 anchor가 특정되지 않았으므로 고유 신경과학 RQ 수에는 현재 포함하지 않는다. 측정 계획은 계속 구체화한다.

### C01-05 — 수정

비판: R3-08-C01-05, R3-12-C01-05

- 수용: 직교회전+등방 gain, 일반 선형 관측변환, 자극의존 관계변형을 nested 모형으로 분리한다.
- 수용: 개인 noise covariance와 whitening은 train 반복에서만 추정하며 원 정서 대비와 상호작용의 재현성을 따로 측정한다.
- 수용: 참가자별 CI/사전 최소효과 기준·동일 데이터량·새 자극×독립 반복 평가를 포함한다.
- 수용: C12-05/공유공간 정보보존군과 통합하고 참가자×자극의 하위 대비로 남긴다.
- 남은 쟁점/정정: R3-12의 유지를 감사하지만 R3-08이 지적한 일반 선형변환과 관계 변화의 중첩은 실질적 결함이므로 수정한다.
- 남은 쟁점/정정: 참가자 고유 신경정보와 개인의 주관적 정서 상태를 동일시하지 않는다. 본 후보는 개인 식별이나 개인정보 추론 연구가 아니다.

허용 좌표군을 고정해야 정보 복원과 좌표 보정의 경쟁이 반증 가능해진다.

## 새로운 구조 전이

### UC01-01 — 조건부 계산·도메인 일반화

P093은 입력별 일부 전문가를 활성화하여 계산량과 전체 용량을 분리하고 P098은 환경 밖 일반화를 평가한다.

입력descriptor가 공유 파라미터를 조절하는 구조를 미관측 내용군의 관측변환 예측으로 전이한다.

새 질문: 고정 정서 방향이 실패해도 내용descriptor에 의해 조절되는 같은 연산은 새 내용군으로 전이하는가?

Round2와 차이: 내용 그룹/검색 후보 정의를 넘어 held-out 내용군에 존재하지 않는 dummy 계수 문제를 해결하는 함수 구조를 도입했다.

판별: 고정·제한 관측변환·관계변형의 새 내용/자극 대비 예측을 동일 자료량으로 비교한다.

실패 해석: descriptor 조건부 일반화가 실패하면 특정 함수와 관측모형의 한계이며 공통 뇌 코드 전체의 부재는 아니다.

근거: P093, P098, P051. 원 계산문제는 기존 문헌/공식 코드 기록, 신경 전이는 E3

### UC01-02 — 순차 영상 예측·시간 대응 학습

P089은 과거 영상에서 다음 입력을 예측하고 P042는 비디오 단계의 순환 일관적 대응을 학습한다.

현재 입력집합을 과거 prefix로 제한하는 예측 구조와 전체 시퀀스 대응을 분리하여 실제 종료를 아는 oracle를 독립 대조로 둔다.

새 질문: 정서 신경 대비의 사건단계 이득은 현재에 계산 가능한 상태에서 오나 사후 정렬에서만 오나?

Round2와 차이: 기하 재매개화의 평가에서 입력 정보의 시간 방향을 검정하는 반사실 비교로 바뀌었다.

판별: elapsed·expected duration·prefix semantics·actual-end oracle를 새 영화의 같은 neural contrast에서 평가한다.

실패 해석: oracle만 성공하면 offline 표현 방법의 이득으로 낮춘다.

근거: P089, P042, P066. 공식 코드 수준의 원리 기록에 근거한 E3 신경 전이; 새 신경결과 없음

### UC01-03 — Bayesian experimental design·비대응 형상 정합

P077은 관측 이력에서 다음 설계를 골라 정보 획득을 높이고 P057은 서로 다른 거리행렬을 수송으로 정렬한다.

비슷한 수송비용인데 다른 정서/신경 대비를 예측하는 해들을 구별할 bridge를 고른다. likelihood/posterior가 없으면 heuristic disagreement임을 명시한다.

새 질문: 어떤 외부 측정이 공통 모양에서 정서 관계와 실제 신경 전이를 분리하는 데 필요한가?

Round2와 차이: 불확실성을 보고하는 데서 끝나지 않고 그 불확실성을 줄일 새 측정의 종류와 독립 검증 단계를 설계한다.

판별: 동일 예산의 disagreement 대 무작위 bridge 선택 후 완전히 보류한 의미 및 신경 대비의 예측을 각각 비교한다.

실패 해석: bridge가 의미만 개선하면 신경 전이 주장을 보류하고 mapping/측정 설계의 한계를 밝힌다.

근거: P077, P057, P100. 원문/공식 자료의 기존 검증기록을 사용; 신경 bridge 설계는 E3

## C01-01 — 새 내용군에서 고정 정서 대비와 조건부 관측변환의 경쟁

새로운 내용군에서 정서 관련 신경 대비는 고정 방향으로 전이되는가, 외부 내용descriptor가 예측하는 제한적 좌표/gain 변환이 필요한가?

분류: 과학RQ후보; 최상위 추천: True. 내용조건부 관측변환의 실질적 판별; C12-01과 하나로 통합

**1차 모델 적용:** 독립 자극 descriptor z로 M0 고정 readout, M1 descriptor가 예측하는 등방 gain/제한적 직교변환, M2 제한된 일반 선형 관측, M3 저차원 bilinear 관계항을 train 내용군에서만 적합한다. 미관측 내용 dummy 계수는 두지 않는다.

**2차 과학 질문:** 내용 변화에도 유지되는 것은 신경공간의 같은 방향인지, 제한된 관측변환 아래 재사용되는 관계 연산인지 구분한다.

**3차 가정 도전:** 고정 방향의 실패가 곧 공통 계산의 부재라는 가정을 철회하고 관측동치의 허용범위를 검정한다.

**주가설:** 고정 방향보다 내용descriptor 기반 제한적 관측변환이 새 내용군의 독립 정서 대비를 더 잘 예측하며, 자유로운 관계변형은 추가로 필요하지 않을 수 있다.

**대안:** 모든 이득이 감각 gain/측정오차 또는 미측정 의미 차이이며, 어떤 조건부 연산도 독립 정서 대비로 전이되지 않는다.

**주 대비:** 같은 test 내용군의 정서 대비 방향·크기에 대해 M0→M1→M2→M3의 사전 지정 증분을 평가한다. 각 유효 자유도/정규화·원 대비 신뢰도를 맞추고 total 및 content-conditional 대비를 병기한다.

**반증:** 신뢰도와 공통 지지가 충분한데 M1/M2가 M0를 개선하지 않으면 제한적 관측변환의 필요성을 축소한다. M3만 성공해도 해당 모형집합 밖 모든 공통 코드의 부재라고 하지 않는다. 모두 실패하면 지지와 모형 부적합을 분리한다.

**실질 변경:** 관측단위 QC에서 더 나아가 조건부 계산의 공유 파라미터 구조를 도입해 미관측 내용군에서도 경쟁모형이 정의되도록 바꿨다. C12-01과 통합할 대비다.

**신규성 위험:** 조건부 cross-decoding·domain generalization과 가깝다. 하나의 병합 RQ이며 세계 최초 미확정.

**기준선:** 고정 readout; descriptor 기반 scalar gain/제한 직교변환; descriptor 기반 동일 rank 일반 선형 관측변환; 동일 자유도 저차원 bilinear 관계항; 내용군별 독립 모형은 관측군 내 상한으로만 사용

**자료 계획:**

- primary: Horikawa: 기존 감사에서 확인한 stim_index와 공식 dupidx를 시작점으로 실제 영상 내용 그룹을 재확인. 자극 집계 정서 주석을 개인 상태로 해석하지 않는다.
- secondary: NSD는 영상 내용 전이·중복 검출 기준선만 담당. 정서 ground truth를 있다고 가정하지 않는다.
- split: 중복 원본 그룹→내용군→자극→참가자 의존성을 보존한다. descriptor 및 내용 주석은 정서/BOLD와 독립 정의. test 뇌로 변환을 재적합하지 않으며 자극쌍은 독립 N으로 세지 않는다.
- fallback: 영상 미접근 시 공식 dupidx로 제한된 독립성 검사는 가능하나 내용 불변 코드 주장은 보류.

**분석조건:** 실제 영상과 fMRI·정서 주석의 ID join; 정서 대비를 공유하는 독립 내용 집합의 충분한 수; 영역별 신뢰도 및 반복/런 분할 가능성; 외부 연속 descriptor의 train/test 공통 지지; 내용별 정서 대비 신뢰도; 조건부 변환의 파라미터 식별성과 동일 자유도 비교

**영어 역검색:** Emotion neural representations unseen content domains conditional observation transformations invariant decoding

실제 결과: {"query_en": "Emotion neural representations unseen content domains conditional observation transformations invariant decoding", "provider": "Crossref works API", "url": "https://api.crossref.org/works?query.bibliographic=Emotion+neural+representations+unseen+content+domains+conditional+observation+transformations+invariant+decoding&rows=3", "attempted_on": "2026-11-12", "execution": "실제 HTTP 요청", "status": "접근 실패; 검색결과 0건을 선행 부재로 해석하지 않음", "error": "<urlopen error Tunnel connection failed: 403 Forbidden>", "results": []}

| 평가 | 점수 | 근거 | 불확실성 |
|---|---:|---|---|
| novelty | 3 | 새 내용에서 관측변환과 고정 코드를 분리하지만 cross-decoding과 가깝다. (P001, P015) | 외부 신규성 검색 접근 실패 시 중복 검토 미완료; 기존 문헌 범위의 잠정 점수 |
| neuro_importance | 4 | 추상 코드의 의미를 제한된 관측동치로 구체화한다. (P001, P015) | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| ai_necessity | 3 | 조건부 descriptor가 유용하지만 선형/bilinear 기준선으로 첫 검정이 가능하다. (P001, P015) | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| data_feasibility | 3 | Horikawa 보유와 감사가 있지만 내용×정서 지지·실제 경로는 미확인이다. (P001, P015) | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| rigor | 4 | train-only 변환과 내용군/참가자 의존성을 명시했다. (P001, P015) | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| falsifiability | 4 | 고정/관측변환/관계항의 단계별 실패 결과가 다르다. (P001, P015) | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| interpretability | 4 | 어느 변환군까지 필요한지 제한된 해석이 가능하다. (P001, P015) | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| generalization | 4 | 새 내용군의 외부 descriptor만으로 예측한다. (P001, P015) | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| technical_feasibility | 4 | 고정 특징과 저차원 모형으로 시작할 수 있다. (P001, P015) | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| exploration_value | 4 | 고정 방향 실패와 공통 연산 부재를 분리한다. (P001, P015) | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |

**여덟 탐색 답변:**

1. 정확한 미시도 여부는 확인하지 못했다. 실제 영어 역검색 시도 결과와 접근 제한을 함께 보존한다.
2. Agent03의 hard-negative retrieval과 Agent07의 표현 불변성을 결합하여 ID가 아닌 내용 관계를 비교 단위로 삼는다.
3. 고정 방향의 실패가 곧 공통 계산의 부재라는 가정을 철회하고 관측동치의 허용범위를 검정한다.
4. 독립 자극 descriptor z로 M0 고정 readout, M1 descriptor가 예측하는 등방 gain/제한적 직교변환, M2 제한된 일반 선형 관측, M3 저차원 bilinear 관계항을 train 내용군에서만 적합한다. 미관측 내용 dummy 계수는 두지 않는다.
5. 고정 방향보다 내용descriptor 기반 제한적 관측변환이 새 내용군의 독립 정서 대비를 더 잘 예측하며, 자유로운 관계변형은 추가로 필요하지 않을 수 있다. 아직 뇌에서 확인된 사실이 아니다.
6. 입력descriptor가 공유 파라미터를 조절하는 구조를 미관측 내용군의 관측변환 예측으로 전이한다.
7. 내용 변화에도 유지되는 것은 신경공간의 같은 방향인지, 제한된 관측변환 아래 재사용되는 관계 연산인지 구분한다.
8. 신뢰도와 공통 지지가 충분한데 M1/M2가 M0를 개선하지 않으면 제한적 관측변환의 필요성을 축소한다. M3만 성공해도 해당 모형집합 밖 모든 공통 코드의 부재라고 하지 않는다. 모두 실패하면 지지와 모형 부적합을 분리한다.

근거: P001, P015, P051, P093, P098, P100

## C01-02 — 미래 종료를 모르는 사건 진행 상태는 고정 시간창을 넘는가

과거 입력만으로 추정한 사건 진행 상태가 경과초·예상길이·일반 사건 내용을 넘어 정서 관련 신경 대비를 설명하는가?

분류: 과학RQ후보; 최상위 추천: False. 사건좌표 공동 RQ C05-04와 병합하되 자기 최상위 2개에는 추가하지 않음

**1차 모델 적용:** M0 elapsed time/FIR, M1 train 영화에서 예측한 expected-duration 위치, M2 prefix-only semantic landmarks/state, M3 실제 전체 duration을 아는 offline oracle를 만든다. 의미 상태도 이벤트 전체를 인코딩한 교사에 test 미래를 입력하지 않는다.

**2차 과학 질문:** 사후 시간 정렬의 유용성과 관찰 시점에 계산 가능한 사건 상태의 추가 신경 설명을 구분한다.

**3차 가정 도전:** 실제 종료로 나눈 0–1 진행률을 온라인 신경 계산의 입력으로 간주한 원안을 철회한다. 사후 oracle만 좋아지면 방법적 정렬 이득으로 낮춘다.

**주가설:** M2가 새로운 영화×duration 구간의 독립 정서 대비에서 M0/M1과 일반 사건 상태 기준을 개선하며, actual-end oracle의 이득과 구별된다.

**대안:** 정규화 위치·경계·HRF·일반 의미 기억이 전부 설명하거나 미래 종료를 아는 M3에서만 효과가 나타난다.

**주 대비:** native scanner 시간에서 각 상태 특징을 생성한 뒤 동일 HRF/FIR 관측모형을 적용한다. prefix 상태 대 elapsed/expected-duration/일반 사건 baseline의 정서 대비 오차 차이와 offline oracle 이득을 별도 추정한다.

**반증:** M3만 개선하면 온라인 사건상태 가설의 증거가 없다. M2가 일반 사건·의미기억 기준을 넘지 못하면 정서 관련 추가 상태 해석을 축소한다. event boundary·주석 lag 선택은 train 내부로 제한한다.

**실질 변경:** Round2의 사후 시간 재매개화를 폐기하지 않고 offline 대조로 분리하며, 입력 시점의 정보 제한을 충족하는 온라인 상태의 충분성으로 질문을 좁혔다. C05-04와 병합한다.

**신규성 위험:** 사건분절/시간창·TCC와 밀접하다. 사건좌표 하나의 공동 RQ로만 계산하며 단순 시간정렬이면 방법후보다.

**기준선:** elapsed time/FIR; train 예상 duration 위치; prefix-only 비신경 semantic progress; 일반 사건경계/과거 의미기억; actual-duration offline oracle; 자기상관·길이·경계 수 보존 null

**자료 계획:**

- primary: Emo-FilM: 공식 1Hz consensus와 fMRI는 별도 코호트임을 유지하며 film-relative time과 실제 onset을 연결한다.
- secondary: Horikawa는 clip 평균 대비의 외부 기준선; 연속 사건 분석을 자동 가정하지 않는다. Spacetop은 실제 연속 주석/타이밍 확인 때만 추가.
- split: leave-film-out 및 duration 층 보류. run별 시작/끝·평정 lag·사건 경계 선택은 train에서만 고정. Spacetop clip 평정을 연속 주석으로 확장하지 않는다.
- fallback: 사건 길이 다양성이나 연속 신경신호가 없으면 시간창 관측 민감도 연구로 축소하고 단계 코드 RQ는 보류.

**분석조건:** 원시 연속 주석·BOLD·영상 timebase; 독립적으로 정의할 사건 경계와 사건 길이 변이; 충분한 영화 수와 HRF 불확실성 평가; prefix 시점에 접근한 frame/token의 감사; 예상 종료시점 예측의 독립 검증; 일반 사건 상태와 정서 대비를 분리할 공통 지지

**영어 역검색:** Emotion brain event progress duration normalization online prediction future boundary leakage

실제 결과: {"query_en": "Emotion brain event progress duration normalization online prediction future boundary leakage", "provider": "Crossref works API", "url": "https://api.crossref.org/works?query.bibliographic=Emotion+brain+event+progress+duration+normalization+online+prediction+future+boundary+leakage&rows=3", "attempted_on": "2026-11-12", "execution": "실제 HTTP 요청", "status": "접근 실패; 검색결과 0건을 선행 부재로 해석하지 않음", "error": "<urlopen error Tunnel connection failed: 403 Forbidden>", "results": []}

| 평가 | 점수 | 근거 | 불확실성 |
|---|---:|---|---|
| novelty | 3 | 온라인/사후 구분은 중요하지만 사건분절 선행과 중복 가능하다. (P002, P042) | 외부 신규성 검색 접근 실패 시 중복 검토 미완료; 기존 문헌 범위의 잠정 점수 |
| neuro_importance | 4 | 정서 관련 시간상태의 계산 가능 정보 범위를 검정한다. (P002, P042) | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| ai_necessity | 3 | 의미 진행 모델은 유용하나 고정시간 기준이 핵심이다. (P002, P042) | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| data_feasibility | 3 | Emo-FilM의 개념 적합성은 있으나 prefix/주석/실제 타임베이스 미확인이다. (P002, P042) | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| rigor | 4 | 미래종료 oracle와 train-only lag를 분리했다. (P002, P042) | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| falsifiability | 4 | oracle만 성공하는 반증 결과가 명확하다. (P002, P042) | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| interpretability | 4 | 온라인 상태와 사후 좌표의 성공을 혼동하지 않는다. (P002, P042) | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| generalization | 4 | 영화×duration 보류가 명시되어 있다. (P002, P042) | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| technical_feasibility | 3 | prefix-only 영상표현 추출과 시간정렬 구현 확인이 필요하다. (P002, P042) | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| exploration_value | 4 | 사건단계라는 자연스러운 설명의 정보 누수를 드러낸다. (P002, P042) | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |

**여덟 탐색 답변:**

1. 정확한 미시도 여부는 확인하지 못했다. 실제 영어 역검색 시도 결과와 접근 제한을 함께 보존한다.
2. 영상의 순차 예측과 cycle-consistent 대응을 결합하되 현재 계산에 미래 endpoint를 주지 않는 입력 제약을 추가한다. 이는 E3 전이이며 P042/P089가 이 신경 결론을 검증했다는 뜻이 아니다.
3. 실제 종료로 나눈 0–1 진행률을 온라인 신경 계산의 입력으로 간주한 원안을 철회한다. 사후 oracle만 좋아지면 방법적 정렬 이득으로 낮춘다.
4. M0 elapsed time/FIR, M1 train 영화에서 예측한 expected-duration 위치, M2 prefix-only semantic landmarks/state, M3 실제 전체 duration을 아는 offline oracle를 만든다. 의미 상태도 이벤트 전체를 인코딩한 교사에 test 미래를 입력하지 않는다.
5. M2가 새로운 영화×duration 구간의 독립 정서 대비에서 M0/M1과 일반 사건 상태 기준을 개선하며, actual-end oracle의 이득과 구별된다. 아직 뇌에서 확인된 사실이 아니다.
6. 현재 입력집합을 과거 prefix로 제한하는 예측 구조와 전체 시퀀스 대응을 분리하여 실제 종료를 아는 oracle를 독립 대조로 둔다.
7. 사후 시간 정렬의 유용성과 관찰 시점에 계산 가능한 사건 상태의 추가 신경 설명을 구분한다.
8. M3만 개선하면 온라인 사건상태 가설의 증거가 없다. M2가 일반 사건·의미기억 기준을 넘지 못하면 정서 관련 추가 상태 해석을 축소한다. event boundary·주석 lag 선택은 train 내부로 제한한다.

근거: P002, P042, P066, P089, P100

## C01-03 — 평균을 넘는 외부 평정분포는 독립 신경 대비와 연관되는가

평정자 척도·지연·표본수를 모형화한 뒤에도 평균으로 소실되는 외부 주석분포 특징이 보류 영화의 신경 대비와 연관되는가?

분류: 과학RQ후보; 최상위 추천: False. 원평정 support와 제한된 신경기여 확인 전 후순위

**1차 모델 적용:** 개별 평정 identity·ordinal 또는 유계 척도·시점별 유효 N·lag/결측을 계층 관측모형으로 적합한다. 이 모형의 예측 분포와 실제 rater-split 분포가 신경 대비에 주는 증분을 독립 영화에서 비교한다.

**2차 과학 질문:** 합의 평균이라는 자극 기술이 정서 관련 신경 연관을 설명하기에 충분한지, 측정 혼합을 넘는 분포 특징이 추가되는지 판별한다.

**3차 가정 도전:** 평균 충분성을 시험하되 외부 사람 사이의 분포를 개인 뇌 내부의 혼합·불확실성·동시 상태로 해석하지 않는다.

**주가설:** 척도/lag/유효표본수만의 분포 null과 평균을 넘는 재현 가능한 외부 분포 특징이 독립 신경 대비를 예측한다.

**대안:** 유계 척도의 평균–분산 결합, 평정자별 지연, 사건 전환·의미 복잡성·결측만으로 분포와 신경 연관이 생긴다.

**주 대비:** 평균+측정모형 예측분포 대 평균+측정모형+독립 재현 분포특징의 held-out neural contrast 증분. 평균·분산 일치 고차분포는 표본지지 게이트를 통과한 별도 탐색이다.

**반증:** 분포가 rater split에서 불안정하면 측정 한계다. 분포는 안정하지만 사전 최소효과보다 신경 증분 CI가 작으면 해당 범위의 평균 충분성을 지지한다. 두 조건이 확인되지 않으면 분포 코드 부재라고 하지 않는다.

**실질 변경:** 평정분포의 추가 신경 연관은 유지하되 다중해석 코드라는 인과·표현 명명을 철회했다. 원평정 관측모형을 경쟁 설명으로 명시했다.

**신규성 위험:** 분포적 annotation·측정오차 연구와 가까우며 신경 증분이 없으면 방법후보다. iVAE 식별 정리가 이 평정모형을 보증하지 않는다.

**기준선:** 평균 정서 벡터; 평정자 ordinal/scale+lag+결측 모형의 예측분포; 동일 평균·유효 N·척도·lag 모의 null; motion·사건경계·의미복잡성; 평균/분산 일치 고차분포 확장

**자료 계획:**

- primary: Emo-FilM: 44명 평정과 30명 fMRI가 별도 집단이라는 기존 공식 감사 사실을 유지. 원평정이 현재 보유본에 있는지 확인 후 수행.
- secondary: Horikawa 원평정 가용성이 확인되면 같은 측정 질문을 외부 검증. 합의 값만 있으면 사용하지 않는다.
- split: 평정자와 영화/자극을 다른 일반화 축으로 둔다. rater별 지연·척도는 개발자료에서만 추정; 시간점과 RDM쌍을 독립 표본으로 세지 않는다.
- fallback: 원평정 부재 시 독립 추가 평정 설계만 남기며 분석 가능이라 표시하지 않는다.

**분석조건:** 개별 평정 원자료와 문항/척도 정의; 같은 시점 또는 같은 clip에 충분한 독립 평정자; 평균이 유사한데 분포가 다른 자극의 공통 지지; 시점별 실제 유효 평정자 수와 missingness; 평정자별 시간 지연/척도 식별; 같은 평정자의 동시 다범주 응답은 별도 자료이며 존재를 가정하지 않음

**영어 역검색:** Affective ratings distribution neural representations rater delays ordinal scales consensus mean

실제 결과: {"query_en": "Affective ratings distribution neural representations rater delays ordinal scales consensus mean", "provider": "Crossref works API", "url": "https://api.crossref.org/works?query.bibliographic=Affective+ratings+distribution+neural+representations+rater+delays+ordinal+scales+consensus+mean&rows=3", "attempted_on": "2026-11-12", "execution": "실제 HTTP 요청", "status": "접근 실패; 검색결과 0건을 선행 부재로 해석하지 않음", "error": "<urlopen error Tunnel connection failed: 403 Forbidden>", "results": []}

| 평가 | 점수 | 근거 | 불확실성 |
|---|---:|---|---|
| novelty | 3 | 평균의 불충분성 원리는 알려져 있으나 독립 신경 증분 질문은 남는다. (P002, P051) | 외부 신규성 검색 접근 실패 시 중복 검토 미완료; 기존 문헌 범위의 잠정 점수 |
| neuro_importance | 3 | 신경 표현기전보다 주석관련 신경 설명의 범위를 바꾼다. (P002, P051) | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| ai_necessity | 2 | 계층 측정모형·단순 encoding으로 검정 가능해 최신 AI가 필수는 아니다. (P002, P051) | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| data_feasibility | 2 | 개별 평정·시점별 N·lag를 사용할 수 있는지 미확인이다. (P002, P051) | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| rigor | 4 | 측정혼합 null과 영화/평정자 이중 검증을 둔다. (P002, P051) | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| falsifiability | 4 | 분포 비신뢰성과 신경 증분 부재를 분리한다. (P002, P051) | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| interpretability | 3 | 외부 분포의 신경 연관 이상은 해석할 수 없다. (P002, P051) | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| generalization | 3 | 보류 영화 전이는 가능하지만 척도 차이에 취약하다. (P002, P051) | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| technical_feasibility | 3 | 원평정이 있으면 통계모형은 작으나 고차분포 support가 제한될 수 있다. (P002, P051) | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| exploration_value | 4 | 평균 집계가 잃는 정보를 독립 신경목표에 질문한다. (P002, P051) | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |

**여덟 탐색 답변:**

1. 정확한 미시도 여부는 확인하지 못했다. 실제 영어 역검색 시도 결과와 접근 제한을 함께 보존한다.
2. Agent07의 관측표현 비식별성: 같은 평균은 여러 다른 분포를 대표한다. 평균 기반 정렬의 성공은 분포 수준의 정보 보존을 보장하지 않는다.
3. 평균 충분성을 시험하되 외부 사람 사이의 분포를 개인 뇌 내부의 혼합·불확실성·동시 상태로 해석하지 않는다.
4. 개별 평정 identity·ordinal 또는 유계 척도·시점별 유효 N·lag/결측을 계층 관측모형으로 적합한다. 이 모형의 예측 분포와 실제 rater-split 분포가 신경 대비에 주는 증분을 독립 영화에서 비교한다.
5. 척도/lag/유효표본수만의 분포 null과 평균을 넘는 재현 가능한 외부 분포 특징이 독립 신경 대비를 예측한다. 아직 뇌에서 확인된 사실이 아니다.
6. 측정모형의 예측분포를 독립 신경 대비의 경쟁 설명으로 전이한다.
7. 합의 평균이라는 자극 기술이 정서 관련 신경 연관을 설명하기에 충분한지, 측정 혼합을 넘는 분포 특징이 추가되는지 판별한다.
8. 분포가 rater split에서 불안정하면 측정 한계다. 분포는 안정하지만 사전 최소효과보다 신경 증분 CI가 작으면 해당 범위의 평균 충분성을 지지한다. 두 조건이 확인되지 않으면 분포 코드 부재라고 하지 않는다.

근거: P002, P051, P055, P100

## C01-04 — 관계 정렬의 모호성을 줄이는 bridge 설계와 독립 신경 전이 조건

기하적으로 동등한 여러 정렬을 구별하도록 선택한 bridge가 완전히 보류한 정서 관계와 양쪽 실제 신경 대비의 전이를 식별하는가?

분류: 방법후보; 최상위 추천: False. 현재 방법후보; neural bridge 조건 전 최상위 신경 RQ로 제안하지 않음

**1차 모델 적용:** train-only GW coupling T로 target 훈련 신경거리 D_B를 공통 좌표 E_B로 임베딩하고, source 훈련 stimulus descriptor z_A에서 T E_B를 예측하는 정규화 함수 f를 fit한다. 새 자극은 f(z_test)만으로 예측하며 target test neural geometry는 학습/튜닝/bridge 선택에 쓰지 않는다. 해당 단순 barycentric map의 왜곡은 별도 검증한다.

**2차 과학 질문:** 공통 기하에서 정서 의미 관계, 다시 실제 신경 대비로 넘어가는 어느 연결이 추가 측정 없이는 결정되지 않는지 판별한다.

**3차 가정 도전:** 유한한 근접 최적 결합의 합의를 공통 신경 코드의 식별로 간주하지 않는다. 현 transport+inductive 모형의 전이 범위만 검정한다.

**주가설:** 훈련·선택 bridge로 고정한 mapping이 최종 미사용 bridge의 정서 관계와 양쪽 측정 신경 대비를 각각 예측하고 의미순열/감각-only 대응보다 낫다.

**대안:** bridge가 의미 대응만 고정하며 신경 전이는 관측/도메인 차이로 실패하거나 유한 최적해 탐색이 대칭 반례를 놓친다.

**주 대비:** 최종 bridge에서 의미 관계 오차와 신경 대비 오차를 별도로 측정한다. 비슷한 train GW비용의 adversarial 의미순열 결합·감각-only map·무작위 bridge 선택과 비교한다. mapping uncertainty는 탐색한 해집합에 조건부인 값으로 표기한다.

**반증:** 의미는 맞아도 실제 neural anchor 예측이 실패하면 신경 전이를 기각한다. 둘 다 실패하면 현 transport/extension의 의미 전이부터 실패한 것이다. 공통 뇌 코드의 부재는 결론내리지 않는다.

**실질 변경:** Round2는 정렬 불확실성을 평가했다. Round4는 어떤 새 bridge 측정이 모호한 대응들을 실제 구별하는지 설계하는 질문으로 전환했다. 지금은 방법후보이며 neural bridge가 특정되어야 신경 RQ가 된다.

**신규성 위험:** active alignment/optimal experimental design과 겹칠 수 있다. 두 집단의 실제 신경 전이 검정 없이 독립 신경과학 RQ로 세지 않는다.

**기준선:** 감각-only inductive map; 비슷한 비용의 의미순열/adversarial coupling; Procrustes+동일 inductive regression; 무작위/균등 bridge 선택; 평정-only 대 의미+양쪽 실측 신경 anchor

**자료 계획:**

- 현재: 사용자 보유 5종을 전제하되 현재 bridge의 양쪽 신경관측 실재는 미확인이다. 현재 산출물은 모형 및 bridge 설계 방법후보다.
- bridge: fitting용·설계 선택용·최종검증용 bridge를 별도 분리한다. 평정-only는 의미 단계만 검증하며 양쪽 fMRI 또는 사전 지정 대응 신경 대비의 실측이 있어야 신경단계 검정이 가능하다.
- inductive: 신규자극의 비신경 descriptor만 f에 입력한다. test neural distance는 최종 평가값이다. source/target modality가 다르면 공통 descriptor의 범위를 먼저 명시한다.
- fallback: neural bridge 부재 시 기하/의미 정렬 방법으로만 남는다. MindCaptioning의 ID·모달리티·주석을 추정하지 않는다.

**분석조건:** 실제 양쪽 neural bridge 및 공통 대비 정의; 평정/신경 bridge의 세 분할; descriptor 기반 inductive map 검증; 의미순열/대칭 반례의 탐색범위; 신규 bridge 선택의 비용과 실제 측정 계획

**영어 역검색:** Gromov Wasserstein affective brain alignment inductive transport independent neural bridge anchors

실제 결과: {"query_en": "Gromov Wasserstein affective brain alignment inductive transport independent neural bridge anchors", "provider": "Crossref works API", "url": "https://api.crossref.org/works?query.bibliographic=Gromov+Wasserstein+affective+brain+alignment+inductive+transport+independent+neural+bridge+anchors&rows=3", "attempted_on": "2026-11-12", "execution": "실제 HTTP 요청", "status": "접근 실패; 검색결과 0건을 선행 부재로 해석하지 않음", "error": "<urlopen error Tunnel connection failed: 403 Forbidden>", "results": []}

| 평가 | 점수 | 근거 | 불확실성 |
|---|---:|---|---|
| novelty | 3 | active alignment와 실험설계의 결합으로 중복 위험이 있다. (P001, P002) | 외부 신규성 검색 접근 실패 시 중복 검토 미완료; 기존 문헌 범위의 잠정 점수 |
| neuro_importance | 3 | 신경 bridge가 마련되면 기하/의미/신경 전이 경계를 설명한다. (P001, P002) | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| ai_necessity | 3 | inductive map과 설계점수는 단순 통계모형으로도 가능하다. (P001, P002) | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| data_feasibility | 1 | 양쪽 실제 neural bridge가 특정되지 않았다. (P001, P002) | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| rigor | 4 | fitting/선택/최종검증 anchor와 inductive extension을 분리했다. (P001, P002) | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| falsifiability | 3 | 신경 단계의 반증에는 실제 bridge 측정이 필요하다. (P001, P002) | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| interpretability | 3 | 각 단계의 전이는 해석 가능하지만 공통 알고리즘은 식별하지 못한다. (P001, P002) | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| generalization | 3 | 새 자극 map을 정의했으나 domain shift가 크다. (P001, P002) | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| technical_feasibility | 2 | GW와 mapping은 가능하나 bridge 측정은 별도 비용이다. (P001, P002) | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| exploration_value | 4 | 어떤 새 관측이 주장을 가능하게 하는지 찾는 설계 가치가 있다. (P001, P002) | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |

**여덟 탐색 답변:**

1. 정확한 미시도 여부는 확인하지 못했다. 실제 영어 역검색 시도 결과와 접근 제한을 함께 보존한다.
2. GW 대응의 비유일성에 Bayesian experimental design의 모형 간 불일치 기반 측정 선택을 추가한다. 실제 Bayesian posterior가 없으면 기대정보이득이라고 명명하지 않고 사전 지정 disagreement score를 사용한다.
3. 유한한 근접 최적 결합의 합의를 공통 신경 코드의 식별로 간주하지 않는다. 현 transport+inductive 모형의 전이 범위만 검정한다.
4. train-only GW coupling T로 target 훈련 신경거리 D_B를 공통 좌표 E_B로 임베딩하고, source 훈련 stimulus descriptor z_A에서 T E_B를 예측하는 정규화 함수 f를 fit한다. 새 자극은 f(z_test)만으로 예측하며 target test neural geometry는 학습/튜닝/bridge 선택에 쓰지 않는다. 해당 단순 barycentric map의 왜곡은 별도 검증한다.
5. 훈련·선택 bridge로 고정한 mapping이 최종 미사용 bridge의 정서 관계와 양쪽 측정 신경 대비를 각각 예측하고 의미순열/감각-only 대응보다 낫다. 아직 뇌에서 확인된 사실이 아니다.
6. 비슷한 수송비용인데 다른 정서/신경 대비를 예측하는 해들을 구별할 bridge를 고른다. likelihood/posterior가 없으면 heuristic disagreement임을 명시한다.
7. 공통 기하에서 정서 의미 관계, 다시 실제 신경 대비로 넘어가는 어느 연결이 추가 측정 없이는 결정되지 않는지 판별한다.
8. 의미는 맞아도 실제 neural anchor 예측이 실패하면 신경 전이를 기각한다. 둘 다 실패하면 현 transport/extension의 의미 전이부터 실패한 것이다. 공통 뇌 코드의 부재는 결론내리지 않는다.

근거: P001, P002, P057, P077, P100

## C01-05 — 개인별 정서 신경 관계의 차이는 어느 관측변환까지로 설명되는가

참가자×자극의 정서 관련 신경 차이는 직교+등방 gain, 일반 선형 관측변환, 자극의존 관계변형 중 어느 수준까지 요구하는가?

분류: 과학RQ후보; 최상위 추천: True. 반복 기반 허용좌표군의 판별; C12-05와 하나로 통합

**1차 모델 적용:** 공통 저차원 신호에서 M0 직교회전+등방 gain, M1 제한된 일반 선형 관측변환, M2 공유 비신경 자극descriptor에 대한 개인별 저차원 관계변형을 nested 적합한다. 개인 noise covariance/whitening과 모든 적응은 train 자극/반복에서만 추정한다.

**2차 과학 질문:** 개인화의 이득이 공통 신호의 측정좌표 차이로 충분한지, 지정한 관측군을 넘는 반복 가능한 자극관계 정보가 필요한지 구분한다.

**3차 가정 도전:** 일반 선형변환은 Euclidean 거리를 보존하지 않으므로 좌표보정과 관계변형을 단순 이분법으로 두었던 원안을 수정한다. 참가자 고유정보는 개인의 내적 정서 또는 개인 식별정보와 다르다.

**주가설:** 일부 참가자에서 M1을 넘는 M2가 새 자극×독립 반복의 정서 대비를 추가 예측하며 그 증분은 독립 반복에서 재현된다.

**대안:** M0/M1과 개인별 신뢰도·HRF·시각민감도 차이로 충분하거나 M2의 이득이 capacity/overfit에만 의존한다.

**주 대비:** 같은 test 자극의 두 독립 반복에서 M0→M1→M2의 contrast 예측증분 CI와 상호작용 RDM 재현성을 별도로 추정한다. raw Euclidean 기하와 noise-whitened crossvalidated 기하는 같은 수치로 혼합하지 않는다.

**반증:** 원 대비 신뢰도가 충분하고 M2 증분 CI의 상한이 개발자료에서 정한 최소 의미 효과보다 작으면 해당 참가자/허용모형에서 관계변형의 필요성을 줄인다. M1 충분성은 잠재 신경 코드의 보편 동일성을 증명하지 않는다.

**실질 변경:** Round2의 선형 보정 대 관계변형 구분을 관측모형의 엄밀한 단계 비교로 바꿨다. C12-05와 한 정보보존 RQ로 병합하고 개인×자극 하위 대비를 남긴다.

**신규성 위험:** hyperalignment/shared-private·표상모형 비교와 가깝다. 전체 BOLD 개인화만 좋아지면 정서 RQ가 아니다.

**기준선:** 직교회전+등방 gain; 동일 rank 일반 선형 관측변환; 동일 자료량·유효자유도 자극의존 저차원 변형; 개인별 noise covariance와 HRF 보정; test 자극 독립 반복 및 참가자내 자극 교환

**자료 계획:**

- primary: Horikawa 우선. 5명이라는 기존 감사의 범위를 유지하며 실제 반복/세션 독립성 확인 후 수행. 참가자를 대규모 모집단 표본처럼 해석하지 않는다.
- secondary: NSD는 반복 기반 시각 상호작용과 정렬 손실의 방법 대조이며 정서 주석은 새 독립 측정이 없으면 사용하지 않는다. Emo-FilM은 반복이 없으면 이 목적의 대체 자료라고 가정하지 않는다.
- split: few-shot 개인 적응과 새 참가자 zero-shot은 다른 추정대상이다. 적응 train 자극과 test 자극의 두 독립 반복을 분리하고 참가자별 CI를 우선한다. 5명 결과를 모집단 유병/부재로 확대하지 않는다.
- fallback: 반복 부재이면 신뢰로운 상호작용과 잡음을 분리할 수 없어 보류. 평균모형 비교만으로 개인 고유 코드라고 주장하지 않는다.

**분석조건:** 참가자×자극의 충분한 공통 관측과 독립 반복; 반복별 BOLD 및 개인별 신뢰도; 실제 정서 대비와 감각 특징의 공통 지지; train 반복에서 안정적인 개인 noise covariance 추정; 최소효과 기준과 대비 신뢰도 CI; 허용 관측변환군별 모형 식별성과 동일 유효 자유도

**영어 역검색:** Individual affective neural geometry orthogonal alignment linear observation stimulus interaction reliability

실제 결과: {"query_en": "Individual affective neural geometry orthogonal alignment linear observation stimulus interaction reliability", "provider": "Crossref works API", "url": "https://api.crossref.org/works?query.bibliographic=Individual+affective+neural+geometry+orthogonal+alignment+linear+observation+stimulus+interaction+reliability&rows=3", "attempted_on": "2026-11-12", "execution": "실제 HTTP 요청", "status": "접근 실패; 검색결과 0건을 선행 부재로 해석하지 않음", "error": "<urlopen error Tunnel connection failed: 403 Forbidden>", "results": []}

| 평가 | 점수 | 근거 | 불확실성 |
|---|---:|---|---|
| novelty | 3 | shared/private와 hyperalignment 선행에 가까워 독창성은 잠정적이다. (P001, P015) | 외부 신규성 검색 접근 실패 시 중복 검토 미완료; 기존 문헌 범위의 잠정 점수 |
| neuro_importance | 4 | 개인별 차이를 관측좌표와 관계정보로 분리한다. (P001, P015) | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| ai_necessity | 2 | 고정 시각 특징과 선형/저차원 모형으로 핵심 검정이 가능하다. (P001, P015) | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| data_feasibility | 3 | Horikawa 보유이나 실제 반복·교차 coverage·개인 noise 추정은 조건이다. (P001, P015) | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| rigor | 4 | 허용변환과 train-only whitening·새 자극 반복을 명시했다. (P001, P015) | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| falsifiability | 4 | M1 충분성과 M2 필요성을 최소효과 CI로 구별한다. (P001, P015) | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| interpretability | 4 | 참가자 고유 정보와 주관 상태를 구분한다. (P001, P015) | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| generalization | 3 | 5명 내부 재현과 모집단 일반화는 별개다. (P001, P015) | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| technical_feasibility | 4 | 소규모 nested 표상모형 비교로 첫 검정이 가능하다. (P001, P015) | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |
| exploration_value | 4 | 개인화 성능이 어디서 생기는지 관측단위 수준으로 분해한다. (P001, P015) | 스키마·checkpoint·효과크기 또는 모형 적합성 실측 전의 조건부 평가 |

**여덟 탐색 답변:**

1. 정확한 미시도 여부는 확인하지 못했다. 실제 영어 역검색 시도 결과와 접근 제한을 함께 보존한다.
2. Agent03의 shared trunk/private residual 평가와 Agent07의 불변성 비교를 결합한다. 참가자 평균을 기본 단위로 놓지 않고 상호작용을 별도 관측량으로 삼는다.
3. 일반 선형변환은 Euclidean 거리를 보존하지 않으므로 좌표보정과 관계변형을 단순 이분법으로 두었던 원안을 수정한다. 참가자 고유정보는 개인의 내적 정서 또는 개인 식별정보와 다르다.
4. 공통 저차원 신호에서 M0 직교회전+등방 gain, M1 제한된 일반 선형 관측변환, M2 공유 비신경 자극descriptor에 대한 개인별 저차원 관계변형을 nested 적합한다. 개인 noise covariance/whitening과 모든 적응은 train 자극/반복에서만 추정한다.
5. 일부 참가자에서 M1을 넘는 M2가 새 자극×독립 반복의 정서 대비를 추가 예측하며 그 증분은 독립 반복에서 재현된다. 아직 뇌에서 확인된 사실이 아니다.
6. 입력descriptor가 공유 파라미터를 조절하는 구조를 미관측 내용군의 관측변환 예측으로 전이한다.
7. 개인화의 이득이 공통 신호의 측정좌표 차이로 충분한지, 지정한 관측군을 넘는 반복 가능한 자극관계 정보가 필요한지 구분한다.
8. 원 대비 신뢰도가 충분하고 M2 증분 CI의 상한이 개발자료에서 정한 최소 의미 효과보다 작으면 해당 참가자/허용모형에서 관계변형의 필요성을 줄인다. M1 충분성은 잠재 신경 코드의 보편 동일성을 증명하지 않는다.

근거: P001, P015, P051, P060, P100, P101

## 한계

- 5종 데이터 보유는 인정한다. 미확인 경로·버전·스키마는 실제 분석 착수 조건이며 문헌·Axis 진행의 차단 조건이 아니다.
- MindCaptioning의 정확한 ID·버전·모달리티·주석을 이름으로 추정하지 않았다.
- 모든 신경 분석·모델 실행·모의실험·신규 bridge 측정은 계획이며 실제 수행하지 않았다.
- Crossref 영어 질의 5개를 실제 요청했다. 접근 결과는 후보별 execution에 보존하며 실패를 검색결과 부재나 세계 최초의 근거로 사용하지 않는다.
- 기존 canonical 원문/코드 검증 범위를 승계했으며 이번에 새 본문 검증을 했다고 집계하지 않는다.
- P068을 사건분절 직접 선행으로 추천한 비판의 출처 대응은 수용하지 않았다. 실제 catalog의 micro-architecture/MEG 논문을 다른 주장으로 인용하지 않는다.
- C01-01/C12-01, C01-02/C05-04, C01-05/C12-05는 병합 권고하며 독립 RQ를 중복 집계하지 않는다.
- C01-04는 현재 방법후보로 분류하고 neural bridge 조건의 discovery 계획만 보존한다.
- 점수는 근거와 불확실성을 가진 Coordinator 입력이며 가중합 순위로 사용하지 않았다.

자기 round04_revision.json/md만 작성했다. 공유 파일과 Git은 수정하지 않았다.
