#!/usr/bin/env python3
"""후보별 기존103편 전수 역대조와 접근 가능한 공개 저장소 검색을 기록한다."""
import csv,json,math,re,collections,urllib.request,urllib.parse,urllib.error,time
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
root=Path(__file__).resolve().parents[1]
papers=list(csv.DictReader((root/'literature/papers.csv').open()))
questions=json.loads((root/'research_questions/landscape.json').read_text())
out=root/'literature/novelty';out.mkdir(exist_ok=True)
def tokens(s):return re.findall(r'[a-z][a-z0-9_-]{2,}|[가-힣]{2,}',s.lower())
texts=[' '.join(p.get(k,'') for k in ['title','original_rq','main_findings','limitations','transfer_idea','axis_tags','model_method']) for p in papers]
bags=[collections.Counter(tokens(t)) for t in texts]
df=collections.Counter(t for b in bags for t in b)
N=len(papers)
records=[]
for q in questions:
    query=q['reverse_search_query_en'];qs=set(tokens(query+' '+q['research_question']+' '+q['assumption_challenge']))
    scores=[]
    for p,b in zip(papers,bags):
        score=sum((1+math.log(b[t]))*math.log(1+(N-df[t]+0.5)/(df[t]+0.5)) for t in qs if b[t])/(1+0.002*sum(b.values()))
        scores.append((score,p['canonical_id'],p['title']))
    ranked=sorted(scores,reverse=True)[:5]
    url='https://github.com/search?'+urllib.parse.urlencode({'q':query,'type':'repositories'})
    response={'url':url,'status':'미실행'}
    # GitHub는 접근 가능한 보조 코드 인덱스다. 논문 전체 검색이나 부재 증명으로 쓰지 않는다.
    try:
        with urllib.request.urlopen(url,timeout=15) as r:
            html=r.read().decode(errors='replace');response['http_status']=r.status
        target=out/f"{q['rq_id']}_github_search.html";target.write_text(html)
        response['evidence_file']=target.relative_to(root).as_posix()
        match=re.search(r'<script[^>]+data-target="react-app.embeddedData"[^>]*>(.*?)</script>',html,re.S)
        payload=json.loads(match.group(1)).get('payload',{}) if match else {}
        found=payload.get('results',[])
        response['result_count_reported']=payload.get('result_count')
        response['status']='페이지 조회; 검색 인덱스 범위만 확인'
        response['candidate_repository_names']=[x.get('hl_name',x.get('name','')) for x in found[:5] if isinstance(x,dict)]
    except Exception as e:response={'url':url,'status':'접근 실패','error_type':type(e).__name__}
    records.append({'rq_id':q['rq_id'],'query_en':query,'executed_at':datetime.now(ZoneInfo('Asia/Seoul')).isoformat(),
                    'local_corpus_size':N,'local_method':'제목·원질문·발견·한계·전이·모델 필드의 문서빈도 가중 토큰 겹침; 전수103편 점수화',
                    'local_top5':[{'canonical_id':x[1],'title':x[2],'retrieval_score':round(x[0],4)} for x in ranked],
                    'expert_closest_prior_ids':q['closest_prior_ids'],'difference_claim':q['what_is_new'],
                    'github_supplement':response,'verdict':'제한된 근접 선행연구 대조 완료; 차별 가설 E3; 전체 문헌의 부재·세계 최초 미확정',
                    'external_limits':'Crossref/arXiv CONNECT403; 현재 검색 범위로 최신 문헌 전체의 비중복을 확정하지 않음'})
    time.sleep(0.1)
(out/'reverse_search_records.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
lines=['# 후보별 신규성 역대조','',
       f'{len(records)}개 RQ마다 기존 고유103편을 실제 전수 검색하고, 역할 연구자가 지정한 근접 문헌과 비교했다. 공개 GitHub 저장소 검색은 보조 코드 인덱스다. Crossref·arXiv 접근 제한으로 전 세계 최신 문헌에 대한 완전한 신규성을 확정하지 않는다. 검색결과가 없다는 사실은 선행연구가 없다는 증거가 아니다.','',
       '| RQ | 실제 검색어 | 전문가 근접 문헌 | 전수검색 상위3 | 보조 검색 |','|---|---|---|---|---|']
for r in records:
    lines.append(f"| {r['rq_id']} | {r['query_en']} | {', '.join(r['expert_closest_prior_ids'])} | {', '.join(p['canonical_id'] for p in r['local_top5'][:3])} | {r['github_supplement']['status']} |")
lines+=['','각 차별점·중복 반론은 [질문 지도](../../research_questions/LANDSCAPE.md)와 Top10 카드에 기록했다. 원 질의·시각·점수·응답 파일은 reverse_search_records.json에 보존한다.','']
(out/'README.md').write_text('\n'.join(lines))
print(json.dumps({'rq_queries':len(records),'local_corpus':N,'github_success':sum(r['github_supplement'].get('http_status')==200 for r in records)},ensure_ascii=False))
