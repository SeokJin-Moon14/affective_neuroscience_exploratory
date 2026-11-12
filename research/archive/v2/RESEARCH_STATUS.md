# 연구 진행 상태

2026-11-12. 사용자 피드백에 따라 정서신경과학 질문을 중심으로 기획을 다시 구성했다. 현재 원고는 핵심 질문 NQ01–NQ10, 상세 제안 RP01–RP10, 파일럿 계획 3개다. 실제 사용자 데이터의 뇌 분석·모델 학습·추론은 수행하지 않았다.

## 현재 기획

첫 분석은 시각 정보를 읽는 뇌 모델에 emotion head를 붙여 시각과 정서가 공유하는 정보를 조사하는 RP01이다. RP03은 내용이 바뀌어도 유지되는 정서 패턴을, RP05는 앞선 맥락이 정서 관련 반응을 설명하는지 다룬다. [제안 목록](https://github.com/SeokJin-Moon14/affective_neuroscience_exploratory/blob/bd56335c91f309620fd37ed2c30b2767c7f98e20/research/proposals/README.md)과 [파일럿](https://github.com/SeokJin-Moon14/affective_neuroscience_exploratory/blob/bd56335c91f309620fd37ed2c30b2767c7f98e20/research/pilots/README.md).

이번 수정에서는 vision, affective neuroscience, dynamics 담당자가 새 카드 원고를 작성하고 Coordinator가 기획·문장·파일럿을 통합했다. 별도 검토자는 질문의 과학적 논리와 데이터 해석을 검토했다. 실제 검토 내용과 반영 여부는 [검토 기록](https://github.com/SeokJin-Moon14/affective_neuroscience_exploratory/blob/bd56335c91f309620fd37ed2c30b2767c7f98e20/research/synthesis/FINAL_AUDIT.md)에 남긴다.

## 이전 작업의 보존

v1에서 수행한 12개 역할의 조사, 문헌 100편의 서지·출처 확인, 5라운드 토론, 실제 무작위 조합, 질문 30개와 방법 감사는 [이전 기록](https://github.com/SeokJin-Moon14/affective_neuroscience_exploratory/blob/bd56335c91f309620fd37ed2c30b2767c7f98e20/research/archive/v1/README.md)에 있다. 이 숫자와 검토 이력을 새 기획의 검증 완료로 사용하지 않는다. 지정 본문·한계 부분을 직접 확인한 문헌은 27편이며, 100편을 모두 원문 완독한 것은 아니다.

새 제안은 기존 문헌을 바탕으로 구성했다. 새로운 포괄적 학술 검색은 수행하지 않았다. 제안별 신규성은 아직 확인이 필요하며, RP03·RP09처럼 선행연구와 특히 가까운 질문을 명시했다.

## 실행 전에 확인할 것

사용자는 Horikawa, Emo-FilM, Mind Captioning, NSD, Spacetop을 보유한다. 이 클라우드에서 보유본의 실제 경로·버전·배열을 확인하거나 모델 가중치를 로드한 상태는 아니다. 확인할 항목은 각 파일럿에 적었으며 기획 작업을 중단하는 이유로 쓰지 않았다.

## 저장과 재개

정본은 GitHub `SeokJin-Moon14/affective_neuroscience_exploratory`의 `research/independent-exploration-20261112` 브랜치다. 마지막 원격 저장 성공은 저장소 `backup/LAST_SUCCESS.json`에서 확인한다. 현재 소스는 `/workspace/Affective-Research-Exploration`, Git 작업 폴더는 `/workspace/affective_research_backup`이다.

현재 문서 원고는 `revision_v2/cards.json`과 `revision_v2/pilots.json`이다. `scripts/render_neuroscience_v2.py`로 다시 만들고 `scripts/validate_neuroscience_v2.py`로 형식·문헌·링크를 확인한다. v1 작성 스크립트로 현재 문서를 덮어쓰지 않는다.

새 세션은 이 파일과 원격 성공 기록을 읽고 이어간다. ChatGPT 프로젝트는 GitHub와 자동 동기화되지 않으며, 채팅을 닫은 뒤 무기한 작업이 계속된다고 보장하지 않는다. [프로젝트 설정 안내](https://github.com/SeokJin-Moon14/affective_neuroscience_exploratory/blob/bd56335c91f309620fd37ed2c30b2767c7f98e20/research/CHATGPT_PROJECT_BRIEF.md).
