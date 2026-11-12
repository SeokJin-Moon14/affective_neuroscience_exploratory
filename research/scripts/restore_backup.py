#!/usr/bin/env python3
"""Git에서 받은 보고서와 분할 증거를 새 클라우드 폴더로 복원·해시 검산한다."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import re
import subprocess
from contextlib import contextmanager

def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()

def safe(root, value):
    path = (root / value).resolve()
    if not path.is_relative_to(root) or Path(value).is_absolute():
        raise ValueError('저장소/복원 경로를 벗어난 항목입니다.')
    return path

@contextmanager
def member(repo, commit, name):
    path = safe(repo, name)
    if commit is None:
        with path.open('rb') as f:
            yield f
    else:
        proc = subprocess.Popen(['git', '-C', str(repo), 'show', f'{commit}:{name}'],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            yield proc.stdout
        finally:
            proc.stdout.close()
            error = proc.stderr.read().decode(errors='replace')
            proc.stderr.close()
            if proc.wait() != 0:
                raise ValueError(f'검증된 커밋의 파일 읽기 실패: {name}: {error}')

def copy_member(repo, commit, name, target, size, expected):
    h, actual = hashlib.sha256(), 0
    with member(repo, commit, name) as f:
        for block in iter(lambda: f.read(1024 * 1024), b''):
            h.update(block); actual += len(block); target.write(block)
    if actual != size or h.hexdigest() != expected:
        raise ValueError(f'원격 복원 자료 검산 실패: {name}')

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    ap.add_argument('--allow-unverified', action='store_true',
                    help='원격 저장 전 로컬 복구 시험에만 사용')
    args = ap.parse_args()
    repo, out = args.repo.resolve(), args.output.resolve()
    if out.exists() and any(out.iterdir()):
        ap.error('기존 작업을 덮어쓰지 않도록 비어 있는 복원 폴더를 사용하세요.')
    out.mkdir(parents=True, exist_ok=True)
    receipt_path = repo / 'backup/LAST_SUCCESS.json'
    commit = None
    if args.allow_unverified:
        manifest = json.loads((repo / 'backup/current_snapshot.json').read_text())
    else:
        if not receipt_path.is_file():
            ap.error('검증된 원격 저장 확인서가 없습니다. 로컬 시험은 --allow-unverified를 사용하세요.')
        receipt = json.loads(receipt_path.read_text())
        commit = receipt['data_commit']
        if not re.fullmatch(r'[0-9a-f]{40,64}', commit):
            ap.error('확인서의 커밋 식별자가 올바르지 않습니다.')
        result = subprocess.run(['git', '-C', str(repo), 'show', f'{commit}:backup/current_snapshot.json'],
                                capture_output=True, check=True)
        manifest = json.loads(result.stdout)
        if manifest['snapshot_id'] != receipt['snapshot_id']:
            ap.error('확인서와 검증된 커밋의 스냅샷이 다릅니다.')
    for rec in manifest['files']:
        dest = safe(out, rec['path']); dest.parent.mkdir(parents=True, exist_ok=True)
        with dest.open('wb') as target:
            if 'stored_path' in rec:
                copy_member(repo, commit, rec['stored_path'], target, rec['size'], rec['sha256'])
            else:
                for part in rec['parts']:
                    copy_member(repo, commit, part['path'], target, part['size'], part['sha256'])
        if dest.stat().st_size != rec['size'] or digest(dest) != rec['sha256']:
            raise ValueError(f"복원 검산 실패: {rec['path']}")
    print(json.dumps({'restored_files': len(manifest['files']),
                      'snapshot_id': manifest['snapshot_id'], 'all_hashes_verified': True,
                      'verified_data_commit': commit}, ensure_ascii=False))

if __name__ == '__main__':
    main()
