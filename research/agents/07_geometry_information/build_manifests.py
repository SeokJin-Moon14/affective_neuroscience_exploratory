from pathlib import Path
import csv,hashlib,json
P=Path(__file__).resolve().parent;S=P/'sources';D='2026-11-12'
# 실제 내려받은 파일만 기록한다. PDF에서 파생된 텍스트는 별도 행으로 연결한다.
items=[]
def src(file,url,paper,kind,scope):
 f=S/file
 assert f.is_file(),file
 items.append(dict(source_id='G07-S'+str(len(items)+1).zfill(2),paper_id=paper,source=url,local_path='sources/'+file,source_type=kind,http_status='200',verified_on=D,sha256=hashlib.sha256(f.read_bytes()).hexdigest(),bytes=f.stat().st_size,confidence='높음: 해당 파일의 직접 확인 범위',evidence_scope=scope,needs_followup='논문 외 공식 코드이면 본문 주장 별도 검증; 미래 학술 신규성 별도 검색',origin_agent='Agent07'))
for paper,stem,v,date in [('G07-P01','kornblith19a','97','2019-05-24'),('G07-P02','huh24a','235','2024-07-08'),('G07-P03','locatello19a','97','2019-05-24'),('G07-P04','hyvarinen19a','89','2019-04-11'),('G07-P05','khemakhem20a','108','2020-06-03'),('G07-P06','moor20a','119','2020-11-21'),('G07-P07','peyre16','48','2016-06-11')]:
 meta=f'https://raw.githubusercontent.com/mlresearch/v{v}/gh-pages/_posts/{date}-{stem}.md'
 pdf=(f'https://raw.githubusercontent.com/mlresearch/v{v}/main/assets/{stem}/{stem}.pdf' if stem=='huh24a' else f'https://raw.githubusercontent.com/mlresearch/v{v}/gh-pages/'+(f'{stem}/{stem}.pdf' if stem!='peyre16' else f'{stem}.pdf'))
 src(stem+'_meta.txt',meta,paper,'공식 출판사 서지','E2: 제목·저자·권호·초록')
 src(stem+'.pdf',pdf,paper,'공식 출판 PDF','E1: 보고서에 지정한 본문·정리·결론/한계 직접 확인; 전 페이지 정밀검토 아님')
 src(stem+'.txt',pdf,paper,'로컬 파생 텍스트','공식 PDF를 pdftotext -layout으로 추출; source PDF와 같은 근거 범위')
for file,url,paper,scope in [
 ('pid_readme.txt','https://raw.githubusercontent.com/pliang279/PID/main/README.md','G07-P08','E2 서지; E1 사용문서; 저자명 불일치 기록'),
 ('pid_rus.txt','https://raw.githubusercontent.com/pliang279/PID/main/synthetic/rus.py','G07-P08','E1 코드: solve_Q_new 및 get_measure; 실행하지 않음'),
 ('skdim_readme.txt','https://raw.githubusercontent.com/scikit-learn-contrib/scikit-dimension/master/README.md','G07-P09','E1 사용문서; E2 서지'),
 ('skdim_cite.txt','https://raw.githubusercontent.com/scikit-learn-contrib/scikit-dimension/master/CITATION.cff','G07-P09','E2: 공식 선호 인용정보'),
 ('skdim_twonn.txt','https://raw.githubusercontent.com/scikit-learn-contrib/scikit-dimension/master/skdim/id/_TwoNN.py','G07-P09','E1: 현재 TWO-NN 구현; 현재 기능을 2021 논문으로 소급하지 않음'),
 ('rsareadme.txt','https://raw.githubusercontent.com/rsagroup/rsatoolbox/main/README.md','G07-P10','E1 공식 도구 소개'),
 ('rsa_cite.txt','https://raw.githubusercontent.com/rsagroup/rsatoolbox/main/CITATION.cff','G07-P10','E2: 2025 preprint 선호 인용정보; 최종 출판 미확인'),
 ('rsa_calc.txt','https://raw.githubusercontent.com/rsagroup/rsatoolbox/main/src/rsatoolbox/rdm/calc.py','G07-P10','E1: crossnobis와 fold descriptor docstring·구현'),
 ('rsa_noise.txt','https://raw.githubusercontent.com/rsagroup/rsatoolbox/main/src/rsatoolbox/inference/noise_ceiling.py','G07-P10','E1: noise ceiling 상·하한 코드'),
 ('rsa_inference.txt','https://raw.githubusercontent.com/rsagroup/rsatoolbox/main/src/rsatoolbox/inference/evaluate.py','G07-P10','공식 추론 구현 파일 확보; 개별 함수 전체 정밀검토 안 함'),
 ('toporeadme.txt','https://raw.githubusercontent.com/BorgwardtLab/topological-autoencoders/master/README.md','G07-P06','E1 공식 구현 문서; E2 논문 서지'),
 ('facco_readme.txt','https://raw.githubusercontent.com/efacco/TWO-NN/master/README.md','미집계 보조자료','E1 저자 도구 문서; 별도 논문 행에 집계하지 않음'),
 ('facco_code.txt','https://raw.githubusercontent.com/efacco/TWO-NN/master/TWO-NN_userfriendly.cc','미집계 보조자료','저자 코드 파일 확보; 논문 전체 서지/Discussion 검증으로 대체하지 않음')]:src(file,url,paper,'공식 코드/문서',scope)
with (P/'sources_manifest.csv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(items[0]));w.writeheader();w.writerows(items)
fields=['axis_id','name','definition','type_tags','representative_papers','models','open_questions','transfer_opportunities','dataset_feasibility','confidence','origin_agent','last_verified','source','needs_followup']
axes=[
 ['K07.1','불변성에 따른 정보 보존과 소실','좌표변환·차원축소·정렬이 보존하거나 제거하는 정서 관련 신경정보를 독립 재현성으로 구별','Structure / Dynamics; Neural; Inference / Measurement; Model / Method','G07-P01;G07-P02;G07-P10','CKA; crossnobis RSA; 공유 저차원 정렬','U1: 공통기하 밖 신경정보는 잡음인가?','T1: 표현 수렴을 정보 손실 감사로 전환','Horikawa 우선 조건부: 실제 정서 주석·자극 ID·독립 반복/런 검증 필요','계산 원리 높음; 뇌 전이 E3','Agent07',D,'papers.csv G07-P01/P02/P10; report.md §5–7','라벨·반복·최신 중복 검증'],
 ['K07.2','관측척도를 건너는 기하 재현성','잡음·표본밀도·시간창·거리·임베딩을 바꾸어도 남는 내재차원과 연결 구조','Structure / Dynamics; Neural; Inference / Measurement','G07-P06;G07-P09;G07-P10','H0 persistent homology; TWO-NN 및 대안 ID; noise ceiling','U2/U3: 차원·연결의 신경 기원과 관측 효과 구분','T2: 위상보존 압축을 관측척도 시험으로 전환','Horikawa/Emo-FilM 조건부: 반복 또는 시간별 자료와 정서 주석 정렬 확인 필요','방법 원리 높음; H1/attractor 해석 낮음','Agent07',D,'papers.csv G07-P06/P09/P10; report.md §5–7','표본수·HRF·거리 추정·독립성 확인'],
 ['X07.1','의미 대응의 식별성과 결합 불확실성','shared/private 요인·수송 결합의 여러 해가 독립 표적에 동일한 의미를 갖는지 검증','Structure / Dynamics; Model / Method; Inference / Measurement','G07-P03;G07-P04;G07-P05;G07-P07;G07-P08','보조변수 nonlinear ICA; iVAE; GW; PID','U4/U5: 시너지와 의미 대응은 어느 조건에서 식별되는가?','T3/T4/T5: 생성원 복원·정보분해·형상 정합의 전이','4개 후보자료 모두 측정/ontology/anchor 확인 전 직접 결합 보류','이론 조건 높음; 실제 신경 식별·cross-dataset 전이 낮음','Agent07',D,'papers.csv G07-P03/P04/P05/P07/P08; report.md §5–8','PID 본문·유한표본·독립 anchor·최신 중복 검증']]
with (P/'subaxes.csv').open('w',newline='') as f:w=csv.writer(f);w.writerow(fields);w.writerows(axes)
# 탐색용 웹 목록은 서지/본문 근거가 아니므로 자신이 만든 캐시만 제거한다.
for name in ['v97_tree.html','pid_page.html','v119_tree.html','v108_tree.html','v89_tree.html','v235_root.txt','v97root.txt','huh235.txt','facco_repo.txt','v48_tree.txt','skdim_repo.txt']:
 f=S/name
 if f.exists():f.unlink()
print(len(items),'출처 파일;',len(axes),'subaxes')
