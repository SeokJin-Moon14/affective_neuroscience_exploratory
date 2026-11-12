#!/usr/bin/env python3
"""실제 역할 파일의 수집·출처 검증. 없는 토론을 생성하지 않는다."""
import csv,json,sys
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
root=Path(__file__).resolve().parents[1]
role_dirs=sorted(p for p in (root/'agents').iterdir() if p.is_dir() and p.name[:2].isdigit())
round_number=int(sys.argv[1])
kind={2:'exchange',3:'critique',4:'revision',5:'debate'}[round_number]
files=[p/f'round{round_number:02}_{kind}.json' for p in role_dirs]
assert all(f.exists() for f in files),[str(f) for f in files if not f.exists()]
docs=[json.loads(f.read_text()) for f in files]
out=root/'discussions'/f'round_{round_number:02}';out.mkdir(exist_ok=True)
papers={r['canonical_id'] for r in csv.DictReader((root/'literature/papers.csv').open())}
papers |= {r['reference_id'] for r in csv.DictReader((root/'axis_map/reference_catalog.csv').open())}
axes={r['axis_id'] for r in json.loads((root/'axis_map/integrated_subaxes.json').read_text())}
records=[]
for f,d in zip(files,docs):
    if round_number==2:
        assert len(d['imports'])>=2
        for c in d['candidates']:
            assert len(c['eight_questions'])==8,(f,c['candidate_id'])
            assert len(c['source_papers'])>=2
            assert set(c['source_papers'])<=papers,(c['candidate_id'],set(c['source_papers'])-papers)
            assert set(c['axis_ids'])<=axes
            records.append(dict(c,role_folder=f.parent.name,source_file=f.relative_to(root).as_posix()))
    elif round_number==3:
        records.extend(dict(r,review_source=f.relative_to(root).as_posix(),reviewer_folder=f.parent.name) for r in d['reviews'])
    elif round_number==4:
        records.extend(dict(r,role_folder=f.parent.name,source_file=f.relative_to(root).as_posix()) for r in d['revised_candidates'])
    else:
        records.extend(dict(r,review_source=f.relative_to(root).as_posix(),reviewer_folder=f.parent.name) for r in d['positions'])
(out/'collected.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
lines=[f'# 실제 Round {round_number} 수집 기록','',
       f'수집시각: {datetime.now(ZoneInfo("Asia/Seoul")).isoformat()}. 역할 파일 {len(files)}개, 실제 항목 {len(records)}개. 각 보고서는 아래 원본에서 확인한다. Coordinator가 역할의 발언을 지어내지 않았다.','',
       '| 역할 | 실제 보고서 | 구조화 기록 |','|---|---|---|']
for f in files:
    rel='../../'+f.relative_to(root).as_posix()
    lines.append(f'| {f.parent.name} | [보고서]({rel[:-5]}.md) | [JSON]({rel}) |')
(out/'index.md').write_text('\n'.join(lines)+'\n')
print(json.dumps({'round':round_number,'roles':len(files),'records':len(records)},ensure_ascii=False))
