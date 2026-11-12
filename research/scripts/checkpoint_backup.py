#!/usr/bin/env python3
"""연구 파일·증거를 전용 Git 브랜치에 저장하고 원격 HEAD를 검증한다.

기본 동작은 로컬 준비만 수행한다. --push는 사용자가 정한 공개 범위 확인 후 실행한다.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import urllib.error
import urllib.request
from datetime import datetime, timezone

CHUNK = 16 * 1024 * 1024
SKIP = {'.git', '__pycache__', '.pytest_cache', '.venv', '.aws', '.codex', '.agents'}

def run(repo, *args):
    r = subprocess.run(['git', '-C', str(repo), *args], text=True, capture_output=True)
    if r.returncode:
        raise RuntimeError(f'git {args[0]} 실패: {r.stderr.strip()}')
    return r.stdout.strip()

def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()

def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

def verify_remote(repo, config):
    owner_repo = config['github_repository']
    actual = run(repo, 'remote', 'get-url', 'origin')
    expected = f'https://github.com/{owner_repo}.git'
    if actual.rstrip('/') not in [expected, expected[:-4]]:
        raise RuntimeError('설정한 GitHub 원격과 origin이 다릅니다.')
    if config.get('expected_visibility') == 'public':
        if not config.get('public_backup_authorized_by_user'):
            raise RuntimeError('공개 백업에 대한 사용자 지시가 설정되지 않았습니다.')
        with urllib.request.urlopen(f'https://github.com/{owner_repo}', timeout=25) as r:
            body = r.read().decode(errors='replace')
        if not re.search(r'>Public</span>', body):
            raise RuntimeError('설정된 공개 저장소를 확인하지 못했습니다.')
        return '사용자가 원문 증거 포함 Public 백업 지시; GitHub 웹 Public 확인'
    if shutil.which('gh'):
        r = subprocess.run(['gh', 'api', f'repos/{owner_repo}', '--jq', '.private'],
                           text=True, capture_output=True, timeout=30)
        if r.returncode == 0:
            if r.stdout.strip() != 'true':
                raise RuntimeError('원격 저장소가 비공개가 아닙니다. 업로드 중단.')
            return 'GitHub API private=true'
    # API 제한 시 사용자 확인 + 공개 웹에서 비노출 + 인증 Git 접근을 함께 확인.
    if not config.get('private_confirmed_by_user'):
        raise RuntimeError('비공개 전환 확인이 필요합니다. 로컬 파일은 준비됐습니다.')
    try:
        with urllib.request.urlopen(f'https://github.com/{owner_repo}', timeout=25) as r:
            body = r.read().decode(errors='replace')
        if re.search(r'>Public</span>', body):
            raise RuntimeError('GitHub 웹에서 Public 확인. 업로드 중단.')
        if re.search(r'>Private</span>', body):
            return 'GitHub 웹 Private 표시'
        raise RuntimeError('GitHub 공개 여부를 확인할 수 없어 업로드 중단.')
    except urllib.error.HTTPError as exc:
        if exc.code != 404:
            raise RuntimeError(f'GitHub 공개 여부 검사 HTTP {exc.code}') from exc
    if not run(repo, 'ls-remote', 'origin', 'HEAD'):
        raise RuntimeError('인증 Git으로도 원격을 확인하지 못했습니다.')
    return '사용자 Private 확인 + 일반 웹404 + 인증 Git 접근 성공(API 직접 확인은 아님)'

def prepare(source, repo, stage):
    if source == repo or repo.is_relative_to(source) or source.is_relative_to(repo / 'research'):
        raise RuntimeError('원본과 백업 경로가 겹칩니다. 별도 작업 폴더에서 저장하세요.')
    dest = repo / 'research'
    dest.mkdir(exist_ok=True)
    records = []
    keep = set()
    for base, dirs, files in os.walk(source):
        dirs[:] = sorted(d for d in dirs if d not in SKIP)
        for name in dirs:
            if (Path(base) / name).is_symlink():
                raise RuntimeError(f'심볼릭 링크 폴더는 별도 검토가 필요합니다: {name}')
        for name in sorted(files):
            path = Path(base) / name
            rel = path.relative_to(source).as_posix()
            if path.is_symlink():
                raise RuntimeError(f'심볼릭 링크는 별도 검토가 필요합니다: {rel}')
            if name in {'.env', '.netrc', 'credentials', 'id_rsa', 'id_ed25519'}:
                raise RuntimeError(f'자격증명 가능 파일을 자동 백업하지 않습니다: {rel}')
            size, digest = path.stat().st_size, sha(path)
            rec = {'path': rel, 'size': size, 'sha256': digest}
            target = dest / rel
            if size > CHUNK:
                parts = []
                with path.open('rb') as f:
                    for n, block in enumerate(iter(lambda: f.read(CHUNK), b'')):
                        part = repo / 'backup/large_files' / digest / f'part-{n:04d}.bin'
                        part.parent.mkdir(parents=True, exist_ok=True)
                        part_hash = hashlib.sha256(block).hexdigest()
                        if not part.exists() or sha(part) != part_hash:
                            part.write_bytes(block)
                        parts.append({'path': part.relative_to(repo).as_posix(),
                                      'size': len(block), 'sha256': part_hash})
                rec['parts'] = parts
                if target.exists():
                    target.unlink()
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                if not target.exists() or sha(target) != digest:
                    shutil.copy2(path, target)
                if sha(target) != digest:
                    raise RuntimeError(f'복사 중 원본 변경 감지: {rel}')
                rec['stored_path'] = target.relative_to(repo).as_posix()
                keep.add(target.relative_to(dest).as_posix())
            if path.stat().st_size != size or sha(path) != digest:
                raise RuntimeError(f'백업 중 원본 변경 감지: {rel}')
            records.append(rec)
    # 전용 research 복사본만 동기화한다. 사용자 원본에는 손대지 않는다.
    for path in dest.rglob('*'):
        if path.is_file() and path.relative_to(dest).as_posix() not in keep:
            path.unlink()
    records.sort(key=lambda r: r['path'])
    sid = hashlib.sha256(json.dumps(records, sort_keys=True).encode()).hexdigest()
    manifest = {'format': 1, 'stage': stage, 'snapshot_id': sid,
                'prepared_at_utc': datetime.now(timezone.utc).isoformat(),
                'file_count': len(records), 'total_bytes': sum(r['size'] for r in records),
                'files': records, 'excluded_components': sorted(SKIP)}
    write_json(repo / 'backup/current_snapshot.json', manifest)
    write_json(repo / 'backup/checkpoints' / f'{stage}-{sid[:12]}.json',
               {k: v for k, v in manifest.items() if k != 'files'})
    return manifest

def commit_pending(repo, config, manifest):
    branch = run(repo, 'branch', '--show-current')
    if branch != config['branch'] or branch in {'main', 'master'}:
        raise RuntimeError('백업 전용 브랜치가 아닙니다.')
    if run(repo, 'diff', '--cached', '--name-only'):
        raise RuntimeError('기존 staged 변경을 먼저 검토해야 합니다.')
    tracked = subprocess.run(['git', '-C', str(repo), 'ls-files', '-z', '--modified',
                              '--deleted', '--others', '--exclude-standard'],
                             capture_output=True, check=True).stdout
    paths = sorted(set(p.decode() for p in tracked.split(b'\0') if p))
    allowed = lambda p: p.startswith(('research/', 'backup/')) or p in {
        'README.md', 'AGENTS.md', 'BACKUP_OPERATIONS.md', '.gitignore'}
    if any(not allowed(p) for p in paths):
        raise RuntimeError('백업 범위 밖의 변경이 있습니다. 자동으로 포함하지 않습니다.')
    # 최초 증거 업로드도 작은 Git 요청으로 나눠 중간 중단에서 복구한다.
    batches, batch, size = [], [], 0
    for name in paths:
        n = (repo / name).stat().st_size if (repo / name).is_file() else 0
        if batch and size + n > CHUNK:
            batches.append(batch); batch, size = [], 0
        batch.append(name); size += n
    if batch:
        batches.append(batch)
    for i, batch in enumerate(batches, 1):
        run(repo, 'add', '--', *batch)
        run(repo, 'commit', '-m', f"backup: {manifest['stage']} ({i}/{len(batches)})")
        print(f'로컬 커밋 {i}/{len(batches)}', flush=True)

def push_pending(repo, config, manifest):
    privacy = verify_remote(repo, config)
    commit_pending(repo, config, manifest)
    branch = config['branch']
    remote_line = run(repo, 'ls-remote', 'origin', f'refs/heads/{branch}')
    base = remote_line.split()[0] if remote_line else config['base_commit']
    if remote_line:
        run(repo, 'fetch', 'origin', f'refs/heads/{branch}')
    run(repo, 'merge-base', '--is-ancestor', base, 'HEAD')
    commits = run(repo, 'rev-list', '--reverse', f'{base}..HEAD').splitlines()
    for i, commit in enumerate(commits, 1):
        run(repo, 'push', 'origin', f'{commit}:refs/heads/{branch}')
        print(f'원격 저장 {i}/{len(commits)}', flush=True)
    # 앞선 실행이 로컬 commit 뒤 push에서 끊겨도 위 원격 HEAD부터 재개한다.
    run(repo, 'push', '-u', 'origin', branch)
    local = run(repo, 'rev-parse', 'HEAD')
    remote = run(repo, 'ls-remote', 'origin', f'refs/heads/{branch}').split()[0]
    if local != remote:
        raise RuntimeError('로컬과 원격 HEAD 불일치. 원격 백업 완료로 보고하지 않습니다.')
    receipt = {'stage': manifest['stage'], 'snapshot_id': manifest['snapshot_id'],
               'data_commit': local, 'remote_head_verified': remote,
               'verified_at_utc': datetime.now(timezone.utc).isoformat(),
               'privacy_check': privacy, 'file_count': manifest['file_count'],
               'total_bytes': manifest['total_bytes'], 'github_repository': config['github_repository'],
               'branch': branch}
    write_json(repo / 'backup/LAST_SUCCESS.json', receipt)
    run(repo, 'add', '--', 'backup/LAST_SUCCESS.json')
    run(repo, 'commit', '-m', f"backup: verify {manifest['stage']} remote snapshot")
    run(repo, 'push', 'origin', branch)
    final = run(repo, 'rev-parse', 'HEAD')
    if run(repo, 'ls-remote', 'origin', f'refs/heads/{branch}').split()[0] != final:
        raise RuntimeError('백업 확인서의 원격 저장 검증 실패.')
    print(json.dumps({'remote_verified': True, 'head': final,
                      'file_count': manifest['file_count'], 'snapshot_id': manifest['snapshot_id']}, ensure_ascii=False))

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--source', type=Path, required=True)
    ap.add_argument('--repo', type=Path, required=True)
    ap.add_argument('--stage', required=True)
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument('--push', action='store_true')
    mode.add_argument('--commit-only', action='store_true', help='로컬 커밋까지 준비; 원격 업로드 없음')
    args = ap.parse_args()
    if not re.fullmatch(r'[A-Za-z0-9_-]+', args.stage):
        ap.error('stage는 영문·숫자·밑줄·하이픈만 허용합니다.')
    source, repo = args.source.resolve(), args.repo.resolve()
    if not source.is_dir():
        ap.error('원본 폴더가 없습니다.')
    run(repo, 'rev-parse', '--show-toplevel')
    manifest = prepare(source, repo, args.stage)
    print(json.dumps({'prepared': True, 'file_count': manifest['file_count'],
                      'bytes': manifest['total_bytes'], 'snapshot_id': manifest['snapshot_id']}, ensure_ascii=False), flush=True)
    if args.push or args.commit_only:
        config = json.loads((repo / 'backup/config.json').read_text())
        if args.push:
            push_pending(repo, config, manifest)
        else:
            commit_pending(repo, config, manifest)

if __name__ == '__main__':
    main()
