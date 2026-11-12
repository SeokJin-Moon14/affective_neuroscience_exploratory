# ChatGPT 프로젝트용 연구 안내

프로젝트 이름 제안: **Brain × Emotion × AI — 독립 연구 탐색**

## 현재 앱에서 설정하기

사용자가 왼쪽 사이드바에 프로젝트 메뉴가 보인다고 확인했다. 일반적인 ChatGPT 프로젝트 흐름은 다음과 같다. 세부 메뉴 위치는 앱 버전에 따라 다를 수 있다.

1. 왼쪽 **새 프로젝트**에서 위 이름으로 프로젝트를 만든다. 생성 시 메모리 선택이 제공되면 기존 연구와의 독립성을 위해 **프로젝트 전용 메모리**를 선택한다.
2. 프로젝트 메뉴(대개 `⋯`)의 **프로젝트 지침**에 아래 내용을 붙여 넣는다.
3. 현재 채팅의 `⋯` 메뉴에 **프로젝트로 이동**이 있으면 만든 프로젝트를 선택한다. 이동 메뉴가 없으면 프로젝트 안에서 새 채팅을 열고 이 안내와 GitHub 링크를 넣는다.
4. 웹 화면이라면 만든 프로젝트를 새 탭으로 열 수 있다. 앱 자체의 별도 탭 제공 여부는 현재 도구로 확인하지 못했다.

GitHub 보고서를 컴퓨터에 다운로드해서 프로젝트에 다시 올릴 필요는 없다. 지침에 저장소·브랜치를 기록하고, 새 대화에서 파일을 실제로 읽을 수 있는 도구/연결이 있는지 확인한다. 링크를 붙이는 것만으로 파일 전체가 자동 읽히거나 GitHub와 자동 동기화되지는 않는다.

## 프로젝트 지침에 붙여 넣을 내용

이 프로젝트는 Brain × Emotion × AI의 문헌 기반 독립 연구 탐색이다. 모든 사용자 설명과 연구 산출물은 한국어로 작성한다. 논문명·DOI·모델명·코드 표기는 원문을 허용한다.

정본은 GitHub `SeokJin-Moon14/affective_neuroscience_exploratory`의 `research/independent-exploration-20261112` 브랜치다. 저장소의 `research/RESEARCH_MISSION.md`를 과학 지침으로, `research/AGENTS.md`를 운영 지침으로 사용한다. 새 작업을 시작하기 전에 `research/RESEARCH_STATUS.md`와 `backup/LAST_SUCCESS.json`을 확인한다. 채팅 기억보다 파일에 기록된 근거·상태를 우선한다.

기존 EmoBrain의 가설·분석을 기본값으로 상속하지 않는다. 측정된 정서 주석, AI가 만든 특징, 신경반응을 구별한다. 공식 코드 확인과 논문 본문 확인, 서지 확인과 Discussion 확인을 구별한다. 확인하지 못한 자료·실험·토론·무작위 추출·백업을 완료했다고 주장하지 않는다.

사용자는 Horikawa, Emo-FilM, Mind Captioning, NSD, Spacetop을 이미 보유한다. 정확한 버전·스키마 확인은 분석 착수 조건으로 기록하고 Axis·개념 조합을 중단하는 이유로 사용하지 않는다. Mind Captioning의 태스크·텍스트 생성 출처·정서 주석을 이름으로 추정하지 않는다.

현재 연구 상태는 Stage3 Axis 통합 v1 완료다. A–X24축, 12역할36개 제안, 8묶음, 수동 교차연결8개를 등록했다. 36개는 고유 RQ 수가 아니다. 고유 문헌100편은 서지·출처 확인이며 그중27편만 본문 또는 지정 절 확인이다. 다음은 실제 Round2–5 토론과 조합·RQ 구성이다. 최종30개 RQ·10개 제안·3개 파일럿은 미완료다. 최신 상태는 항상 RESEARCH_STATUS.md를 다시 읽는다.

연구 단계가 끝나거나 중단되기 전에 상태 파일을 갱신하고, 실행 도구와 GitHub 쓰기 권한이 있는 에이전트가 단계별 커밋·푸시·원격 HEAD 검증을 수행한다. 일반 ChatGPT 대화나 프로젝트 지침만으로 GitHub 파일이 자동 저장되거나 백그라운드 연구가 계속되는 것은 아니다.

## 관리 방식

- ChatGPT 프로젝트: 대화·목표·검토 결과를 모으는 공간.
- GitHub 연구 저장소: 보고서·문헌 표·코드·원문 증거·복구 상태의 정본.
- 클라우드 실행 환경: 실제 조사·파일 작성·Git 작업을 수행하는 공간.

현재 사용자는 공개 저장소에서 작업하도록 선택했다. 공개 링크는 열람할 수 있지만, ChatGPT의 GitHub 쓰기 기능과 실행 도구는 별도 연결이 필요하다. 나중에 비공개로 전환하면 읽기 권한도 별도로 확인한다.

브랜치: https://github.com/SeokJin-Moon14/affective_neuroscience_exploratory/tree/research/independent-exploration-20261112

Axis: https://github.com/SeokJin-Moon14/affective_neuroscience_exploratory/blob/research/independent-exploration-20261112/research/axis_map/AXIS_ENCYCLOPEDIA.md

## 이 채팅을 옮길 때

현재 ChatGPT 채팅 메뉴에 '프로젝트로 이동'이 제공되면 생성한 프로젝트를 선택한다. 이 대화가 별도 Codex 화면에 있어 이동 메뉴가 없다면, ChatGPT 프로젝트에 새 채팅을 만들고 위 안내를 붙여 넣어 연결한다. 현재 도구에는 ChatGPT 프로젝트 생성·채팅 이동 기능이 없으므로 이동 완료를 자동으로 확인할 수 없다.
