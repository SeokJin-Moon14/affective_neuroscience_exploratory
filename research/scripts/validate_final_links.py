#!/usr/bin/env python3
"""현재 사용자 진입점과 최종 산출물의 내부 파일 링크 확인."""
from pathlib import Path
import re,json,urllib.parse
from datetime import datetime,timezone
r=Path(__file__).resolve().parents[1]
relative=['START_HERE.md','RESEARCH_STATUS.md','CHATGPT_PROJECT_BRIEF.md','BUNDLE_CONTENTS.md','proposals/README.md','pilots/README.md','research_questions/LANDSCAPE.md','research_questions/RANKINGS.md','datasets/DATASET_INTELLIGENCE_REPORT.md','axis_map/AXIS_ENCYCLOPEDIA.md','synthesis/OPPORTUNITY_MAP.md','synthesis/DIVERSITY_AUDIT.md','synthesis/FINAL_REPORT.md','synthesis/FINAL_AUDIT.md','discussions/round_05/SYNTHESIS.md']
files=[r/x for x in relative]+sorted((r/'proposals').glob('RP*.md'))+sorted((r/'pilots').glob('PILOT*.md'))
missing=[];checked=0
for f in files:
 assert f.is_file(),f
 for raw in re.findall(r'\]\(([^)]+)\)',f.read_text()):
  if raw.startswith(('http:','https:','mailto:','#')):continue
  target=urllib.parse.unquote(raw.split('#')[0].strip('<>'))
  if not target:continue
  checked+=1;p=(f.parent/target).resolve()
  if not p.exists():missing.append({'source':f.relative_to(r).as_posix(),'target':target})
report={'checked_at':datetime.now(timezone.utc).isoformat(),'files_checked':len(files),'local_file_links_checked':checked,'missing':missing,'scope':'현재 진입점 및 최종 보고/제안/계획의 내부 파일 경로. 외부URL 응답·HTML anchor 동작 검증은 아님'}
(r/'synthesis/link_check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
assert not missing,missing
print(json.dumps(report,ensure_ascii=False))
