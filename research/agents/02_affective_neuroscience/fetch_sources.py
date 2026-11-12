"""허용된 공개 URL 응답과 접근 증거 보존. 프록시/정책 설정 변경 없음."""
import sys,urllib.request,urllib.error,json,pathlib,hashlib,concurrent.futures,datetime
base=pathlib.Path(__file__).parent/'evidence'
def fetch(item):
 k,u=item
 m={'url':u,'verified_on':datetime.datetime.now(datetime.timezone.utc).isoformat(),'origin_agent':'02_affective_neuroscience'}
 try:
  try:r=urllib.request.urlopen(u,timeout=30)
  except urllib.error.HTTPError as e:r=e
  b=r.read(); (base/(k+'.source')).write_bytes(b)
  m.update(status=r.status,final_url=r.url,bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),content_type=r.headers.get('Content-Type'),source_file=k+'.source')
 except Exception as e:m.update(status='요청실패',error=repr(e))
 (base/(k+'.json')).write_text(json.dumps(m,ensure_ascii=False,indent=2)); print(k,json.dumps(m,ensure_ascii=False))
items=json.loads(sys.argv[1])
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as p:list(p.map(fetch,items.items()))
