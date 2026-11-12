# 단계별 원격 저장·복구

연구는 클라우드에서 수행하고 GitHub 비공개 저장소에 보존한다. 사용자 컴퓨터의 디스크를 사용하지 않는다.

## 단계 저장

현재 세션의 명령:

```bash
python /workspace/Affective-Research-Exploration/scripts/checkpoint_backup.py \
  --source /workspace/Affective-Research-Exploration \
  --repo /workspace/affective_research_backup \
  --stage stage02-independent-discovery \
  --push
```

각 Wave 종료, 문헌 병합, 토론 라운드, 조합, 제안, 파일럿 계획, 중단 지점에 stage 이름을 바꿔 실행한다. 별도의 자동 실행 서비스나 cron은 설치하지 않는다. 작업을 수행하는 Coordinator가 이 규칙을 실행한다.

`--push`를 빼면 로컬 준비만 한다. `--commit-only`는 원격 업로드 없이 로컬 커밋까지만 만든다. 업로드 시 비공개 여부를 확인하고 작은 묶음의 커밋을 차례대로 푸시한다. 중단됐다가 다시 실행하면 원격에 도착한 커밋 다음부터 재개한다. 원격 브랜치 HEAD를 다시 읽어 로컬과 일치하는지 검증한다. `backup/LAST_SUCCESS.json`은 검증된 데이터 커밋을 가리키며, 그 확인서 자체도 후속 커밋으로 저장한다.

## 새 클라우드 세션 복구

```bash
git clone --single-branch --branch research/independent-exploration-20261112 \
  https://github.com/SeokJin-Moon14/affective_neuroscience_exploratory.git \
  /workspace/affective_research_backup
python /workspace/affective_research_backup/research/scripts/restore_backup.py \
  --repo /workspace/affective_research_backup \
  --output /workspace/Affective-Research-Exploration
```

비어 있는 복원 폴더를 사용한다. 복구 스크립트는 LAST_SUCCESS.json이 가리키는 검증된 데이터 커밋에서 파일을 읽는다. 다음 단계 업로드가 중간에 끊겼어도 마지막 성공 지점으로 복구한다. 모든 파일과 큰 파일 조각의 SHA-256을 검증한다. 성공한 뒤 RESEARCH_STATUS.md부터 읽고 새 Agent에게 해당 역할 보고서를 전달한다. 이전 세션의 Agent ID는 재사용 가능하다고 가정하지 않는다. 원격 저장 전 로컬 시험에만 --allow-unverified 옵션을 사용한다.

## 저장 범위

보고서·문헌 CSV·코드·원문 PDF·HTML·다운로드 증거·원본 메타데이터를 포함한다. 큰 파일은16MiB 조각으로 분리해 Git에 보존하며 원본 경로로 재구성한다. .git 내부정보, 실행 캐시, 가상환경, 자격증명 폴더는 제외한다. 증거 자료의 저작권·라이선스는 원출처에 있으며 저장소의 LICENSE가 이를 재허가하는 것은 아니다.

ChatGPT 프로젝트는 별도의 대화 관리 공간이다. 비공개 저장소 접근 권한 없이 링크만으로 증거를 읽을 수 없고, 채팅 종료 후 연구가 자동으로 계속되는 것도 아니다.
