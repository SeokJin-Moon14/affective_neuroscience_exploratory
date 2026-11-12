import csv,json,hashlib
from pathlib import Path
P=Path(__file__).parent
fields='axis_id name definition type_tags representative_papers models open_questions transfer_opportunities dataset_feasibility confidence origin_agent last_verified'.split()
rows=[dict(zip(fields,['G/X-VD1','생성 prior와 신경정보의 기여 분리','생성 전 latent·prior 출력·생성 후 영상에서 뇌 조건의 추가 정보를 각각 검증','Model / Method; Neural; Inference / Measurement; Construct / Stimulus','VD01;VD02;VD05;VD07','MindEye2;MindEye;Brain-Diffuser;ridge latent decoding','정서 관련 내용이 신경 조건의 정보인가 생성 prior의 보충인가?','hard-negative retrieval; 조건 교환; latent와 출력 이중 평가','Horikawa 우선이나 실제 주석/반복/정합 확인 필요; NSD는 시각 대조군','방법 코드 범위 E1; 과학 가설 E3; 신규성 미확정','03_vision_decoding','2026-11-12'])),dict(zip(fields,['O/X-VD2','정렬 과정의 정서 관련 정보 보존','공유 시각 latent 정렬이 유지하는 정보와 버리는 반복 가능한 신경 잔차를 분리','Neural; Structure / Dynamics; Inference / Measurement; Construct / Stimulus','VD01;VD03;VD08;VD09','MindEye2;Brain-IT;MinD-Vis;MindBridge','영상 검색이 유지되는 동안 정서 관련 신경정보는 소실될 수 있는가?','domain adaptation; masked 대 contrastive 학습; cycle consistency 감사','피험자/자극 이중 보류와 반복 신뢰도 자료가 필요; 대상 데이터의 실제 가용성 미확인','방법 코드/문서 E1; 가설 E3; 반복 가능성 전제 미검증','03_vision_decoding','2026-11-12'])),dict(zip(fields,['D/Q-VD3','생성 시간 해상도와 신경 식별 시간의 분리','영상 출력의 시간적 매끄러움과 fMRI가 식별한 정서 관련 시간 정보의 차이를 측정','Structure / Dynamics; Neural; Model / Method; Inference / Measurement','VD10;VD01','MinD-Video;시간적 hard-negative retrieval','장면·움직임·HRF 통제 후 정서 관련 변화가 추가 신경정보를 갖는가?','temporal negative sampling; 자기상관 보존 교환; prior-only 대조','Emo-FilM/Spacetop 영상 onset·연속 주석·원신호 정합 확인 전 보류','공식 README E1; 시간적 전이 가설 E3; 데이터 조건 미확인','03_vision_decoding','2026-11-12']))]
with (P/'subaxes.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
manifest=json.loads((P/'sources/fetch_manifest.json').read_text())
lines=['# 다운로드 출처 및 확인 위치','', '공식 URL별 요청 결과와 SHA256은 `fetch_manifest.json`에 보존했다. 직접 성공한 파일이 있다는 것과 그 파일의 모든 문장을 해석·검증했다는 것은 구분한다. README는 논문 본문으로 집계하지 않는다.','', '| 키 | 요청 결과 | 공식 URL | 로컬 파일 |','|---|---|---|---|']
for x in manifest:
 key=x['key'];status=str(x.get('status',x.get('error','미확인')))
 local=f'[{key}.txt]({key}.txt)' if (P/'sources'/f'{key}.txt').exists() else '없음'
 lines.append(f'| {key} | {status} | {x["url"]} | {local} |')
lines+=['','## 읽은 범위','', '- 주요 README 8개와 Brain-IT transfer README의 서지·입출력·학습/추론 안내를 읽었다. Takagi README는 두 연구, Brain-IT README는 두 연구를 포함하므로 고유 연구10건이다.', '- MindEye2 Train/final_evaluations 노트북은 `*_cells.txt`로 code/markdown만 추출해 입력층·출력 target·손실·retrieval cell을 검토했다. 노트북의 저장 출력은 새 실행 결과가 아니다.', '- MindEye2 models/utils의 대조 손실·prior MSE·cosine/topk; Brain-IT encoder/decoder 훈련·transfer 및 모델 정의의 관련 부분을 확인했다. 전체 프로그램 감사·실행은 하지 않았다.', '- `brainit_page.txt`, `mindbridge_page.txt`는 root tree와 commit 식별에만 사용했다.', '- GitHub 검색 결과는 공식 저장소를 찾는 탐색 자료이며 자체로 논문 내용의 근거가 아니다.', '- 실패한 BrainCLIP 추정 URL을 존재 부정이나 다른 저장소의 공식성 확인으로 사용하지 않는다. BrainCLIP은 이번 문헌 집계에서 제외했다.', '- arXiv/Hugging Face403으로 본문/Discussion/가중치 실물 미확인. 논문 또는 checkpoint가 없다는 뜻이 아니다.']
(P/'sources/README.md').write_text('\n'.join(lines)+'\n')
# 수집 원문 변조 여부 및 CSV 구조 점검만 수행한다.
checks=[]
for x in manifest:
 if x.get('status')==200:
  f=P/'sources'/f'{x["key"]}.txt'
  assert hashlib.sha256(f.read_bytes()).hexdigest()==x['sha256'],f
  checks.append(x['key'])
with (P/'papers.csv').open(encoding='utf-8-sig') as f:
 reader=csv.DictReader(f); papers=list(reader); assert len(reader.fieldnames)==32
assert len(papers)==10 and len({p['paper_id'] for p in papers})==10
assert all(len(p)==32 and all(v is not None and v!='' for v in p.values()) for p in papers)
assert all(p['discussion_access']=='아니오' and p['evidence_level']=='E2' for p in papers)
(P/'VALIDATION.md').write_text(f'''# 산출물 검증\n\n- `papers.csv`: 고유 연구 {len(papers)}행, 32열. 미션30필드와 추가 확인범위/위치2필드. 누락값 없음.\n- 문헌수준 E2 {len(papers)}건; 논문 본문/Discussion 직접 확인0건. 코드/README 근거만 E1로 별도 표기.\n- 성공 다운로드 {len(checks)}개 파일 SHA256 일치. 실패 요청도 manifest에 보존.\n- Sub-axis3건, 미해결문제5/방법기회5/분야전이5/예상밖연결3/숨겨진가정3/필수탐색질문8을 보고서에 명시.\n- 모델 설치·학습·추론, checkpoint 다운로드, 데이터셋 실물 분석, 신규성 전수 검색은 실행하지 않음.\n- 다른 Agent 결과와 EmoBrain 미열람; 산출물은 이 Agent 폴더에만 작성.\n''')
print({'papers':len(papers),'columns':32,'successful_source_hash_checks':len(checks),'subaxes':len(rows)})
