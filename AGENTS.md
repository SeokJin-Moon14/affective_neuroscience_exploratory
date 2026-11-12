# 연구 백업 저장소 운영

사용자는 기존 GitHub 저장소를 비공개로 전환해 연구 결과와 원문 증거를 원격 백업하도록 요청했다.

연구 지침은 `research/RESEARCH_MISSION.md`부터 읽고 `research/AGENTS.md`를 따른다. 현재 상태는 `research/RESEARCH_STATUS.md`, 마지막으로 검증한 원격 데이터 커밋은 `backup/LAST_SUCCESS.json`에 있다.

이 저장소의 `research/`는 보기 쉬운 복사본이다. 전체 연구 작업은 `research/scripts/restore_backup.py`로 별도 클라우드 폴더에 복원한 뒤 수행한다. 큰 증거 파일은 `backup/large_files/`의 조각과 `backup/current_snapshot.json`으로 복원한다.

각 연구 단계·토론 라운드·중단 지점에서 Coordinator가 `research/scripts/checkpoint_backup.py`를 실행하여 저장한다. 원격 HEAD 검증 없이 백업 완료를 주장하지 않는다. force push, 기본 브랜치 덮어쓰기, 기존 사용자 변경 삭제를 하지 않는다. 사용자 컴퓨터에 전체 자료를 내려받을 필요가 없다.
