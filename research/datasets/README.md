# 데이터 검증 보고서

기준일 2026-11-12. 사용자는 **Horikawa·Emo-FilM·Mind Captioning·NSD·Spacetop을 보유**한다. [보유 상태와 Axis 연결](ownership_and_readiness.md)을 우선 확인한다. 에이전트는 이번 작업에서 본체를 내려받거나 뇌 분석을 실행하지 않았다. 아래 네 자료는 공식 메타데이터·코드·텍스트 이벤트를 확인한 기존 감사다.

- [Horikawa](horikawa/verified_spec.md): 우선 데이터. 305개 이벤트 파일을 전수 검산했다.
- [Emo-FilM](emofilm/verified_spec.md): 뇌 측정·평정 코호트와 시간 좌표 구분.
- [Spacetop](spacetop/verified_spec.md): 릴리스별 참여자 수와 실제 분석 코호트 구분.
- [NSD](nsd/verified_spec.md): 공식 코드의 데이터 경로·ID 대응과 실제 확보 상태 구분.
- [Mind Captioning](mind_captioning/verified_spec.md): 사용자 보유 확인; 정확한 버전·스키마는 분석 시 확인. 조건부 Axis 연결 등록.
- [교차 데이터 비교](cross_dataset_matrix.md): 공유 변수와 직접 비교가 불가능한 항목.

기존 네 감사 폴더에 metadata_inventory.csv, annotation_dictionary.csv, modeling_opportunities.md를 포함한다. Mind Captioning의 미확인 필드를 임의로 채우지 않았다. 확인 불가능한 라벨·척도·실물 접근은 미확인으로 남겼으며 Axis 진행의 선행 차단 조건은 아니다. 원증거는 agents/01_dataset/evidence/와 다운로드 로그·해시에 보존했다.
