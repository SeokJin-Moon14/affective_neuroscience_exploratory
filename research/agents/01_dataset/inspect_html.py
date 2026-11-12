import re,json,sys
from pathlib import Path
for arg in sys.argv[1:]:
 p=Path(arg);print(p.name)
 for x in re.findall(r'<script type="application/json"[^>]*>(.*?)</script>',p.read_text()):
  j=json.loads(x).get('payload',{})
  for k in ['codeViewRepoRoute','codeViewTreeRoute']:
   if k in j: print(j[k].get('refInfo',{}));print([v['path'] for v in j[k].get('tree',{}).get('items',[])])
 print(sorted(set(re.findall(r'href="/((?:cvnlab|spatialtopology)/[^/"?#]+)',p.read_text()))))
