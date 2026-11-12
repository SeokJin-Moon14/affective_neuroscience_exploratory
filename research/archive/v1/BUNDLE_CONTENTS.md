# 보고서 묶음과 전체 백업의 차이

이 문서의 초기 경량 압축 묶음은 당시 보고서·CSV·JSON·검증 스크립트만 포함하고 큰 PDF·HTML·원 이벤트 증거를 제외했다. 그 초기 묶음의 범위를 최신 전체 백업과 혼동하지 않는다.

현재 정본은 GitHub 연구 브랜치다. 보고서와 공개 원문 증거·원 이벤트·코드 snapshot을 포함하고 큰 파일은 해시가 있는 조각으로 보존한다. scripts/restore_backup.py로 전체를 새 클라우드에 복원할 수 있다. 사용자 컴퓨터에 다운로드할 필요는 없다.

최신 시작점은 [START_HERE.md](https://github.com/SeokJin-Moon14/affective_neuroscience_exploratory/blob/bee5c041fca8ff8a6dcf99c9c8906252c2cbe2a6/research/START_HERE.md)와 [최종 종합 보고서](https://github.com/SeokJin-Moon14/affective_neuroscience_exploratory/blob/bee5c041fca8ff8a6dcf99c9c8906252c2cbe2a6/research/synthesis/FINAL_REPORT.md)다. 실제 사용자 데이터 본체·모델 가중치가 이 저장소에 새로 포함됐다고 뜻하지 않는다. 파일별 범위는 backup/current_snapshot.json, 원격 저장 성공은 backup/LAST_SUCCESS.json을 확인한다.
