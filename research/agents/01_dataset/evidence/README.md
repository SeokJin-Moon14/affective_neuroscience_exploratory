# 근거 보존 안내

검증일 2026-11-12. 공식 원본은 원어 그대로 보존했다. fetch_log.jsonl에는 URL·최종 URL·HTTP/프록시 상태·확인시간·SHA256을 기록한다. 200 응답이어도 git-annex 포인터일 수 있으며 원자료 다운로드 성공으로 해석하지 않는다.

repository_snapshots.json에 저장소 URL/commit을 기록했다. repository_snapshots.tar.gz는 다운로드 당시 Git metadata와 공식 코드 snapshot을 보존한다. 중첩 Git 저장소가 프로젝트 Git 추적을 방해하지 않도록 .git 디렉터리는 archive에 넣고 작업 경로에서는 제거했다. 필요하면 별도 임시 디렉터리에 압축을 풀어 참조한다. repos/horikawa_code의 공식 소스와 repos/*_tree.txt는 그대로 열람 가능하다. collect_metadata.py 재실행에는 archive의 저장소 metadata 복원이 필요하다.

audit_counts.py는 보관한 텍스트 이벤트만 사용한다. derived_audit_counts.json은 해당 실제 검산 결과다. selection metadata는 metadata_selection.json을 참조한다.

원본 다운로드 기록의 local_path는 당시 저장 위치이다. 원본 일부가 archive로 이동한 경우 repository_snapshots.tar.gz를 참조한다. 다른 Agent 또는 기존 EmoBrain 자료는 포함하지 않았다.
