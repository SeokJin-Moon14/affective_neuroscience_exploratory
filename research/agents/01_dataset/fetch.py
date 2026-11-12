from pathlib import Path
import urllib.request, urllib.error, concurrent.futures, json, datetime, hashlib, sys
root=Path(__file__).parent/'evidence'; root.mkdir(exist_ok=True)
def fetch(k,u):
 try:
  with urllib.request.urlopen(u,timeout=25) as r: data=r.read();status=r.status;final=r.url
 except urllib.error.HTTPError as e:data=e.read();status=e.code;final=e.url
 except Exception as e:data=str(e).encode();status='ERROR';final=u
 p=root/k;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
 row={'name':k,'url':u,'final_url':final,'status':status,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'local_path':str(p),'verified_on':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 with (root/'fetch_log.jsonl').open('a') as f:f.write(json.dumps(row,ensure_ascii=False)+'\n')
 return row
if __name__=='__main__':
 pairs=[line.rstrip('\n').split('\t',1) for line in sys.stdin if line.strip()]
 for x in concurrent.futures.ThreadPoolExecutor(max_workers=4).map(lambda p:fetch(*p),pairs): print(json.dumps(x,ensure_ascii=False))
