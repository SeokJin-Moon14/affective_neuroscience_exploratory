# 원격 백업 구성 상태

기준일: 2026-11-12. 현재 사용자는 기존 **공개 저장소에서 우선 백업하고 작업**하도록 명시했다. 이전 비공개 전환 대기는 해제했다.

- 저장소: SeokJin-Moon14/affective_neuroscience_exploratory
- 브랜치: research/independent-exploration-20261112
- 원본 연구 폴더: /workspace/Affective-Research-Exploration
- Git 작업 폴더: /workspace/affective_research_backup
- 원문 PDF·HTML·메타데이터·보고서·코드를 포함한다. 현재 파일 수·정확한 바이트 수는 저장소 backup/current_snapshot.json에 있다. 사용자 컴퓨터에는 다운로드하지 않는다.
- 큰 파일 분할 저장과 전체 복원·SHA-256 검사를 수행했고, 중단된 다음 업로드가 있어도 이전 성공 커밋에서 복구하는 시험을 통과했다.

**실제 원격 저장 성공의 정본은 백업 브랜치 backup/LAST_SUCCESS.json이다.** 그 파일의 data_commit·snapshot_id·원격 HEAD 검증 기록을 확인한다. 로컬 커밋만으로 원격 보존을 주장하지 않는다. 단계별 저장 및 복구는 저장소의 BACKUP_OPERATIONS.md를 따른다.

ChatGPT 프로젝트 안내는 CHATGPT_PROJECT_BRIEF.md다. 현재 도구에 프로젝트 생성·채팅 이동 기능이 없어 이동 자체를 수행했다고 주장하지 않는다.
