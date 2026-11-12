# 데이터 우선순위 재확인

2026-11-12 · 담당 `/root/dataset_priority`. 이번에는 기존에 저장한 공식 README·코드·실제 이벤트/주석 메타데이터를 다시 읽었다. 새 네트워크 검색, fMRI 분석, 모델 실행, 보유 원자료 다운로드는 하지 않았다. 사용자가 데이터를 보유한다는 사실과, 여기서 그 데이터 본체를 실제로 열었다는 사실은 구별한다.

## 우선순위

최신 사용자 지시가 원래 미션 문서의 순서를 대체한다. **1순위 Horikawa·MC·NSD → 2순위 Emo-FilM → 3순위 Spacetop.** 이 보고서의 담당 범위는 Horikawa와 보조 두 자료다. MC·NSD는 다른 역할이 주로 확인한다. 마지막에 Coordinator가 확보한 MC 공식 BIDS README를 직접 읽어, 심상 과제와 v3 기억 정확성 검정의 차이만 추가 확인했다.

## 확인한 관측과 연구에 쓸 수 있는 범위

| 자료 | 이번에 직접 확인한 공식 자료 | 보유 자료로 다룰 수 있는 관측 | 아직 확인하지 못한 것 |
|---|---|---|---|
| **Horikawa, 1순위** | [공식 BIDS README](evidence/horikawa_bids_README), [공식 Python README](evidence/horikawa_python_README.md), [튜토리얼](evidence/horikawa_Tutorials.txt), [설정](evidence/horikawa_config.yaml), 305개 실제 events.tsv | 다섯 참가자가 같은 자극 ID/name 집합의 짧은 영상을 보는 fMRI. 공식 분석은 영상별 정서 category 34·dimension 14, semantic 73·vision 1000 특징을 사용한다. 영상 내용·정서 주석·신경 표현의 관계와 내용이 다른 자극으로의 일반화를 기존 관측에서 연구할 근거가 있다. | 실제 feature 값·항목명·척도·평정자별 데이터·사용자 보유 처리본·BOLD·영상 본체는 이번에 열지 않았다. 영상마다 해당 fMRI 참가자의 정서 평정이 있다고 확인하지 않았다. |
| **Emo-FilM, 2순위** | [뇌 참여자 명단](evidence/ds004892/participants.tsv), [주석 참여자 명단](evidence/ds004872/participants.tsv), [consensus sidecar](evidence/ds004872/derivatives/Annot_AfterTheRain_stim.json), [공식 처리 코드 설명](evidence/emofilm_README.md), [상수](evidence/emofilm_constants.py), 실제 scan/beh events | 뇌 자료 30명과 주석 자료 44명의 명단을 각각 확인했다. consensus는 50열·1Hz·영화시간 0부터 시작한다. 자연 영화의 시각/사건 변화와 외부 정서 주석에 대응하는 뇌 반응을 연구하는 확장 자료다. fMRI 참가자의 별도 clip validation 평정도 실제 TSV로 확인했다. | 외부 consensus를 스캔 참가자의 연속 개인 정서로 볼 수 없다. 숫자 annotation `.tsv.gz` 두 파일은 gzip 본체가 아니라 git-annex 포인터다. 개인별 영화 전체 정서 궤적·주석 신뢰도 수치·사용자 보유본의 처리/QC는 확인하지 않았다. |
| **Spacetop, 3순위** | [공식 README](evidence/ds005256/README), [참여자 명단](evidence/ds005256/participants.tsv), [alignvideo events 설명](evidence/ds005256/task-alignvideo_events.json), [실제 예시 events](evidence/ds005256/sub-0001/ses-01/func/sub-0001_ses-01_task-alignvideo_acq-mb8_run-01_events.tsv) | 자연 영상과 해당 참가자의 clip 후 happy/sad/afraid/disgusted 등 0–100 평정을 연결할 수 있는 구조를 확인했다. 우선 자료에서 얻은 관계가 다른 자료·측정 단위에서도 나타나는지 살펴볼 후순위 확장 자료다. | README101명과 참여자 파일117행의 차이가 남아 있고, 분석 가능한 표본 수는 확정하지 않았다. 영상 중 연속 정서 평정이 아니다. 원래 PINES 문항·척도·자극 방식과 같다고 볼 수 없다. |

위의 ‘가능’은 관측 구조가 있는 연구 범위를 뜻한다. 구체적인 새 RQ의 최초성이나 보유본의 실제 파일 연결까지 검증했다는 뜻은 아니다. 추가 인간 주석이 필요한 질문은 기존 주석만으로 되는 질문과 별도로 표시해야 한다.

## Horikawa 재확인 결과

이번에 실제 TSV를 다시 파싱했다. 다섯 참가자 각각 61개 events 파일, 2,196개 자극 행, 2,196개 서로 다른 `stim_index`가 있다. 다섯 참가자의 `(stim_index, stimulus_name)` 집합은 동일하다. 이 메타데이터에서는 같은 자극 ID를 한 참가자에게 독립 반복한 구조가 확인되지 않는다. ID가 다른데 영상 내용이 겹치는 문제와 참가자 안의 반복 측정은 다르다.

실제 헤더는 `onset,duration,trial_type,stimulus_name,stim_index`다. README의 `stimulus_index`라는 설명과 다르므로 데이터 연결에는 실제 헤더를 사용한다. [원 MATLAB 설정](evidence/horikawa_batch.m) 85행의 `dupidx`는 15개 제외 인덱스이며 2,196−15=2,181이다. Python README의 2,185개 소개와 차이는 이 확인으로 해결되지 않았다. 따라서 ‘2,185개 영상의 실물을 모두 확인했다’고 말하지 않는다.

[튜토리얼](evidence/horikawa_Tutorials.txt) 220행이 category34/dimension14/semantic73/vision1000의 근거다. 공식 설정의 `amt/mean_score_concat` 경로와 feature group은 확인했으나 HDF5 안의 개별 이름·값·신뢰도를 연 것은 아니다. 설정은 다섯 피험자의 HDF5와 `stimulus_name` 연결, Run을 사용한 6분할을 명시한다. Python README는 nested cross-validation이 생략됐다고 명시하므로 단순 실행을 원논문의 엄밀한 재현으로 부르지 않는다.

## v3 네 방향은 현재 자료로 가능한 연구로 선정됐는가

**그렇게 볼 수 없다. 특히 C06-C의 핵심 결론은 현재 확인한 보유 자료로 검증할 수 없다.** MC에 심상 자료가 있다는 사실만으로 이 결론이 달라지지 않는다. 필요 관측을 아래처럼 구별해야 한다.

| v3 방향 | 핵심적으로 필요한 관측 | 이번 담당 자료에서의 판정 |
|---|---|---|
| C04-C 시선·정보 선택 | 첫 관측 조작, 다음 시선, 동일 부분을 다른 이력 뒤 보여 준 뇌 반응 | 새 조작 조건과 시선 측정을 확인하지 못했다. 기존 완전 영상 BOLD에 부분 영상을 만든 뒤 같은 반응을 붙여 대체할 수 없다. |
| C06-C 정서 기억의 오류 방향 | 처음 세부 지각 확인, 선택지 전 회상 BOLD, 이후 유인 자극 선택 오류 | 이 조합의 관측을 확인하지 못했다. MC에는 실제 testImagery와 참가자가 평가한 accuracy/vividness 0–5점이 있지만, 이는 원본 세부의 객관적 지각 확인·변형 유인자극 선택·오류 방향 자료가 아니다. 따라서 C06-C를 보유 자료로 검증 가능한 주력 후보에서 제외해야 한다. |
| C06-A 편집에 공통된 신경 변화 | 원 장면·단일 편집·두 편집 결합·대조 장면에 대한 실제 뇌 반응 | 새로 만든 편집 장면의 뇌 반응은 없다. 기존 자연 장면의 유사한 비교로 재설계할 가능성과, 동일한 조작 실험을 이미 할 수 있다는 주장은 구별해야 한다. |
| C02-A/C03-A 등 PINES 비교 | 원 PINES 목표 문항·척도·제시 조건의 개인 평정, 해당 뇌 반응, 시각 조건과 평정의 교차 비교 | Horikawa의 평균 feature나 Emo-FilM consensus를 원 PINES 목표로 대체할 수 없다. Spacetop은 개인 clip 후 평정이 있지만 문항·척도·자극 형식이 다르므로 원 지표 눈금 검증과 동일하지 않다. |

따라서 이 방향들을 **현재 보유 자료로 우선 실행할 연구**로 제시한 것은 자료 확인의 결과와 맞지 않는다. 장기 새 실험 후보로 보존할 수는 있으나, 1순위 자료에서 실제 가능한 질문을 제치고 앞에 놓을 근거는 없다.

## MC에 심상 자료가 있어도 C06-C가 가능한 것은 아니다

Coordinator가 새로 확보한 [공식 MC BIDS README](../../datasets/mind_captioning/evidence/bids_README)를 직접 읽었다. 여섯 참가자, `trainPerception`, `testPerception`, `testImagery`를 명시한다. `testImagery`에는 `cueID`, `imageryID`, `stimID`, 참가자가 평가한 `accuracy`와 `vividness` 0–5점이 있다.

따라서 ‘보유 데이터에는 심상이 없다’는 말은 틀리다. 그러나 **심상 정확성에 대한 본인 평정은 특정 세부가 어느 방향으로 잘못 기억됐는지를 측정한 행동 자료가 아니다.** C06-C가 요구한 초기 세부 지각 확인, 선택지 제시 전 회상 신경표현, 이후 정서 전형적 변형을 고르는 구체적인 오류를 이 점수로 대체할 수 없다. MC의 실제 관측에 맞춰 다른 결론을 검토할 수는 있어도, C06-C의 결론을 그대로 유지한 채 실행 가능이라고 표시하면 안 된다.

## 접근 상태를 과장하지 않기 위한 기록

이번에 확인한 `agents/01_dataset/evidence/` 아래에는 `.h5`, `.nii`, `.nii.gz` 본체가 없었다. 이것은 사용자에게 데이터가 없다는 뜻이 아니다. 이 작업의 근거 파일은 공개 문서·코드·TSV/JSON 메타데이터다. 새 분석을 시작할 때만 사용자 보유본의 경로·버전·스키마를 대조하면 된다. 그 전에도 공식적으로 확인된 관측을 토대로 RQ를 설계할 수 있다.

일부 과거 다운로드 파일 이름이 README여도 내용은 `404: Not Found`였다. `emofilm_brain_README`, `emofilm_annotation_README`, `emofilm_annotation_README.md`를 내용 근거로 사용하지 않았다. 성공한 Emo-FilM 공식 코드 README, constants, participant TSV, 실제 이벤트·annotation JSON으로 위 사실을 재확인했다. 뇌 자료의 `ds004892/README.md`도 논문 URL 한 줄이므로 원문을 읽은 것으로 세지 않았다.

원본 파일과 확인 시점의 해시는 [검토 근거 기록](priority_recheck_sources.json)에 남겼다. 공통 데이터 명세·연구 제안·Git은 수정하지 않았다.
