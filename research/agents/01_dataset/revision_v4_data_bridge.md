# v4 지원: Horikawa–MC 연결의 실제 근거와 한계

최신 사용자 우선순위는 1순위 Horikawa·MC·NSD, 2순위 Emo-FilM, 3순위 Spacetop이다. 이번 확인은 새 RQ를 만드는 작업이 아니라, 같은 원영상 ID로 무엇을 연결할 수 있는지 좁혀 확인한 자료다. 공개 GitHub의 작은 코드·메타데이터만 추가로 받았으며 뇌 데이터·영상·큰 모델은 받지 않았다.

## 확인된 연결

| 연결 | 이번에 직접 확인한 결과 | 그 결과가 보장하지 않는 것 |
|---|---|---|
| Horikawa events ↔ MC 사람 캡션 | Horikawa 5명 각각의 2,196개 `stim_index` 모두 MC CSV의 `video_id`에 연결된다. Horikawa의 숫자로 읽은 `stimulus_name`도 `stim_index`와 모두 같다. CSV는 2,196 ID마다 사람 캡션20개, 총43,920행이다. | 원영상 파일의 byte/hash 동일성, 정서 라벨 본체의 행 순서·개별 항목명, 캡션이 정서 정답이라는 주장 |
| MC perception ↔ 원영상·캡션 | 공식 실제 events의 `stimID`가 원영상 ID다. 예: trainPerception 첫 런에 `stimID=1300`, `stimLabel=1298`; testPerception 첫 런에는 `stimID=71`, `stimLabel=4`가 있다. | `stimLabel`을 원영상 ID처럼 직접 조인하면 안 된다. 시험 자료의 `stimLabel`은 확인 범위에서1–72, train에서는1–2180이다. |
| MC imagery ↔ perception | sub-01 testImagery 첫 세션의72개 `imageryID` 집합이 testPerception의72개 `stimID`와 정확히 같다. `cueID=71` 준비 뒤 `imageryID=71`인 심상 블록과 뒤따르는 실제 영상 블록을 실제 행에서 확인했다. | 모든 참가자의 파일 대응·전처리된 MATLAB 행 순서, 과제 간 동일 SNR, 개인의 경험 정서, 객관적인 세부 기억 오류 |
| MC 반복 | sub-01 testPerception의10개 events 파일에서72개 영상이 각각5회 제시된360개 블록을 확인했다. imagery 첫 세션은72개가각1회다. | imagery 전체5회 반복은 공식 README가 설명하지만 이번 실물 검산은 첫 세션까지만 했다. 전체6명 모두의 반복·QC를 검증한 것은 아니다. |

[캡션–Horikawa 조인 검산](evidence/revision_v4/caption_horikawa_join.json) · [MC sub-01 원영상 ID 검산과 전체 ID 목록](evidence/revision_v4/mc_sub01_id_checks.json).

MC 캡션은 공식 data README가 crowdsourcing으로 수집했다고 명시하는 **자극에 대한 사람 설명**이다. 뇌로 생성한 caption과는 다른 입력이다. 같은 뇌 반응에서 생성한 텍스트를 그 뇌 반응의 독립적인 원인 특징처럼 다시 넣어서는 안 된다.

## raw task 이름만으로 MC의 학습·평가 구분을 하면 안 된다

sub-01의 raw `trainPerception`에는60런·2,180개 원영상 ID가 각1회 있다. 그런데 그 안에 testPerception의72개 ID가 전부 들어 있다. 마지막 세션의 run-06과run-07이 바로 그72개 시험영상이며, 두 런을 제외한58런·2,108개 영상은 시험영상과 겹치지 않는다. 공식 처리본 README의 train2108과 공식 코드 `mcap_setParams.m`의 CV범위1–58이 이 구분과 맞는다. **이 대응을 확인한 것이지, 배포된 .mat의 실제 행을 열어 확인한 것은 아니다.**

따라서 모든 raw trainPerception 행을 학습에 넣고 testPerception을 ‘새 영상 평가’라고 부르면 같은 영상이 들어간다. 실제 분석에서는 공식 처리본의 ID mapping을 확인하거나 위 원영상 ID로 시험영상72개를 명시적으로 제외해야 한다. Horikawa 자료로 학습해 MC를 평가할 때도, MC시험 영상이 Horikawa에도 있다는 사실을 반영해야 한다. 같은 영상을 새 참가자·새 과제에서 읽는 검정과 처음 보는 내용으로 일반화하는 검정을 구별한다.

근거: [공식 MC data README](../../datasets/mind_captioning/evidence/data_README.md), [직접 받은 설정 코드](evidence/revision_v4/mcap_setParams.m), [sub-01 events 목록](evidence/revision_v4/mc_sub01_event_manifest.json), [다운로드 기록](evidence/revision_v4/mc_sub01_event_fetch.json). 추가 events76개는 합계288,331바이트다.

## 제외 ID는 두 연구에서 같지 않다

MC sub-01에서 확인한 전체 perception ID는1–2196 중 다음16개가 빠진2,180개다.

`859, 866, 1363, 1673, 2184, 2186, 2187, 2188, 2189, 2190, 2191, 2192, 2193, 2194, 2195, 2196`

이는 실제 이벤트 집합에서 없는 ID를 계산한 결과이며, 이번에 그16개를 제외한 이유까지 확인한 것은 아니다. Horikawa 원분석의15개 제외 목록과 다르다. [Horikawa 원 코드](evidence/horikawa_batch.m)의 제외를 적용한 ID집합과 MC perception의 교집합은2,172개다. MC시험72개 중 Horikawa의 해당 제외에 걸리는 것은 원ID1이어서, 이 제외 기준을 그대로 적용하면71개가 남는다.

Horikawa의2,185 소개·2,196 이벤트·2,181 원분석 ID를 MC의2,180과 같은 숫자로 맞추거나 한쪽의 행 번호를 다른 쪽에 그대로 복사하면 안 된다. 두 데이터 모두 실제 원영상 ID를 기준으로 대응표를 만들고, 어떤 제외를 적용한 결과인지 남겨야 한다. 같은 ID여도 원영상의 편집·제시 길이가 같은지는 별도 확인 대상이다.

## 지금 설계할 수 있는 것과 주장하면 안 되는 것

기존 관측에 근거한 출발점은 원영상 ID로 연결한 영상·사람 캡션·공개 정서 주석과, 기존 perception/imagery 신경 반응 사이의 관계다. 이 연결을 분석에 쓰려면 Horikawa 정서 feature의 실제 값을 열어 원영상 ID와 항목을 대조하고 MC 처리본의 row-to-ID 대응을 확인하면 된다. 이 확인은 새 뇌 실험을 전제로 하지 않는다.

반면 동일한 사람의 실제 경험 정서가 Horikawa와 MC 사이에 전달됐다고 주장할 근거는 없다. 두 자료의 `sub-01` 같은 이름이 같은 사람이라는 근거도 확인하지 않았다. 외부 정서 주석은 자극에 대한 측정이며, MC의 심상 accuracy/vividness 평정은 정서 평정이나 객관적인 세부 기억 오류가 아니다. 이 때문에 기존 C06-C의 ‘정서적 방향의 구체적인 기억 오류 예측’은 여전히 이 자료만으로 검증할 수 없다.

새로 합성한 변형 영상에 대응하는 실제 BOLD, 시선 조작, 변형 유인자극 선택 자료도 이 연결로 생기지 않는다. 데이터에 없는 관측을 결론에 필요한 조건으로 남긴 질문은 v4의 실행 가능한 주력 후보로 통과시키지 않는다.

## 근거의 확인 수준

이번에 MC의 공식 분석 진입 코드, 설정 코드, 원자료 이벤트를 직접 읽었다. 원 논문 전체·각 피험자 처리본·원영상 본체·Horikawa 정서 feature의 개별 값은 읽지 않았다. 그림이나 feature 차원 수에서 정서 항목 이름을 추정하지 않았다. 새 자료는 모두 `agents/01_dataset/evidence/revision_v4/`에 있으며, 공통 문서와 Git은 수정하지 않았다.
