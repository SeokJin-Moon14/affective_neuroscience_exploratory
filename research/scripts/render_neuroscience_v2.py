#!/usr/bin/env python3
"""검토한 v2 원고를 독자용 문서와 표로 저장한다. 과거 토론을 재생성하지 않는다."""
from pathlib import Path
import csv
import json
import re

ROOT = Path(__file__).resolve().parents[1]
if (ROOT / 'revision_v3/version.json').exists():
    raise SystemExit('v3 작업이 시작되어 v2 생성기의 현재 문서 덮어쓰기를 중단합니다. 과거 결과는 archive/v2를 읽으세요.')
CARDS = json.loads((ROOT / 'revision_v2/cards.json').read_text())
PILOTS = json.loads((ROOT / 'revision_v2/pilots.json').read_text())
PAPERS = {p['canonical_id']: p for p in csv.DictReader((ROOT / 'literature/papers.csv').open())}


def write(path, text):
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text.rstrip() + '\n')


def dump(path, value):
    write(path, json.dumps(value, ensure_ascii=False, indent=2))


def table(headers, rows):
    clean = lambda x: str(x).replace('|', '\\|').replace('\n', ' ')
    return '\n'.join(['| ' + ' | '.join(headers) + ' |', '| ' + ' | '.join(['---'] * len(headers)) + ' |'] +
                     ['| ' + ' | '.join(clean(x) for x in row) + ' |' for row in rows])


def bullets(items):
    return '\n'.join('- ' + str(x) for x in items)


def paper_url(p):
    ident = p['doi_or_arxiv'].strip()
    if re.fullmatch(r'10\.\d{4,9}/[^\s]+', ident):
        return 'https://doi.org/' + ident
    match = re.fullmatch(r'(?:arXiv:)?(\d{4}\.\d{4,5})', ident)
    if match:
        return 'https://arxiv.org/abs/' + match[1]
    return p['official_url']


for c in CARDS:
    sections = [f"# {c['title']}", f"{c['proposal_id']} · {c['rq_id']} · 연구 기획 v2",
                c['summary'], '## 이 질문으로 알아내려는 것', c['why'],
                '## 어떤 설명을 비교하나',
                table(['설명', '맞다면 관찰할 결과'], [[h['explanation'], h['prediction']] for h in c['hypotheses']]),
                '## 뇌에서 무엇을 보고, AI를 어떻게 쓰나', c['neural_targets'],
                '\n\n'.join(f'{i}. {step}' for i, step in enumerate(c['approach'], 1)),
                '## 결과를 어떻게 해석하나',
                table(['관찰 결과', '과학적 의미'], [[o['result'], o['meaning']] for o in c['outcomes']]),
                '## 기존 연구에서 더 나아갈 부분', c['novelty']['known'], c['novelty']['proposed'], c['novelty']['unresolved'],
                '## 보유 자료로 시작할 범위', c['data'], '먼저 할 일: ' + c['first_step'],
                '## 해석할 때 남는 한계', bullets(c['limits']),
                '## 관련 문헌']
    if c['proposal_id'] == 'RP01':
        diagram = """```mermaid
flowchart LR
    B[뇌 활동] --> D[vision decoder]
    D --> V[예측한 시각 특징]
    V --> H[emotion head]
    H --> E[인간 정서 평정 예측]
    B --> Q[뇌에서 정서 직접 예측]
    Q --> E
    I[실제 영상] --> M[시각 모델]
    M --> A[실제 영상의 시각 특징]
    A --> H
```"""
        at = sections.index('## 뇌에서 무엇을 보고, AI를 어떻게 쓰나') + 1
        sections.insert(at, diagram)
    refs = []
    for ref in c['literature']:
        p = PAPERS[ref['id']]
        refs.append(f"- [{ref['id']} · {p['title']}]({paper_url(p)}): {ref['role']}")
    sections += ['\n'.join(refs), '[문헌별 실제 확인 범위](../literature/REVISION_V2_SOURCES.md). 이 제안의 분석 결과는 아직 없다.',
                 '[제안 목록](README.md) · [새 질문과 이전 제안의 관계](../revision_v2/CHANGELOG.md)']
    write(f"proposals/{c['proposal_id']}.md", '\n\n'.join(sections))

brief_scope = {
    'RP01': 'Horikawa에서 시작',
    'RP02': '기존 영상과 추가 주석. 직접 조작은 새 실험',
    'RP03': 'Horikawa의 내용 간 비교',
    'RP04': '여러 정서 항목의 분포를 확인한 뒤 탐색',
    'RP05': 'Emo-FilM과 맥락 주석. 같은 장면 비교는 새 실험',
    'RP06': 'Emo-FilM과 장면 연결 주석. 지속 시간 해석에 주의',
    'RP07': '사건의 예상 가능성에 관한 추가 평가 필요',
    'RP08': '소리 제시 확인과 감각별 주석. 직접 비교는 새 실험',
    'RP09': '기존 자료 탐색. 선행연구와 차별화가 더 필요',
    'RP10': '소수 참가자 탐색. 확증은 더 많은 참가자·세션 필요'
}
rows = [[f"[{c['proposal_id']}](" + c['proposal_id'] + '.md)', c['title'], brief_scope[c['proposal_id']]] for c in CARDS]
write('proposals/README.md', '# 정서를 처리하는 뇌에 관한 연구 제안\n\n'
      '시각 정보, 장면의 맥락, 시간에 따른 변화가 뇌의 정서 표현과 어떻게 관계되는지 묻는다. 각 제안에서 먼저 과학적 질문과 경쟁하는 설명을 제시하고, 이를 구별할 AI 모델과 실험을 설명한다.\n\n'
      '첫 분석 후보는 [RP01 시각과 정서가 공유하는 정보](RP01.md), [RP03 내용이 바뀌어도 유지되는 정서 패턴](RP03.md), [RP05 장면의 맥락](RP05.md)이다.\n\n' +
      table(['제안', '연구 질문', '자료와 실행 범위'], rows) + '\n\n'
      '[파일럿 3개](../pilots/README.md) · [종합 보고서](../synthesis/FINAL_REPORT.md) · [질문 비교](../research_questions/LANDSCAPE.md)\n\n'
      '이 목록은 사용자 피드백을 반영해 새로 구성한 v2다. 이전 30개 질문과 방법 검토는 [v1 기록](../archive/v1/README.md)에 보존했다. RP 번호가 같아도 이전과 같은 제안이라는 뜻은 아니다.')
dump('proposals/cards.json', CARDS)
write('proposals/AUTHORING_PROTOCOL.md', '# 제안 작성 기준\n\n현재 기준은 [최신 작성 지침](../revision_v2/AUTHORING.md)과 [AGENTS.md §11](../AGENTS.md)이다. 검토한 원고는 revision_v2/cards.json에 저장하고 scripts/render_neuroscience_v2.py로 문서를 갱신한다. v1의 역할별 proposal_RP 파일을 렌더링하면 이전 기획으로 돌아가므로 사용하지 않는다.')

for p in PILOTS:
    parts = [f"# {p['title']}", f"{p['pilot_id']} · [{p['proposal_id']}](../proposals/{p['proposal_id']}.md) · {p['rq_id']}",
             p['purpose'], '## 예상하는 차이', p['hypothesis'], '## 첫 분석',
             '\n\n'.join(f'{i}. {step}' for i, step in enumerate(p['steps'], 1)),
             '## 결과에 따른 판단', table(['관찰 결과', '판단'], [[d['observation'], d['decision']] for d in p['decisions']]),
             '## 자료와 준비', p['scope'], bullets(p['requirements']), p['resource'],
             '## 남길 결과', p['output'], p['status'],
             '[공통 방법과 데이터 조건](METHODS.md) · [파일럿 목록](README.md)']
    write(f"pilots/{p['pilot_id']}.md", '\n\n'.join(parts))
dump('pilots/plans.json', PILOTS)
write('pilots/README.md', '# 먼저 검토할 세 가지 분석\n\n'
      '시각 정보와 정서의 관계에서 시작해, 장면의 내용이 바뀌는 경우와 맥락이 달라지는 경우로 확장한다. 아래 문서는 실행 계획이며, 실제 사용자 자료를 분석한 결과는 아직 없다.\n\n' +
      table(['계획', '질문', '주요 자료'], [[f"[{p['pilot_id']}]({p['pilot_id']}.md)", p['title'], 'Horikawa' if i < 2 else 'Emo-FilM'] for i, p in enumerate(PILOTS)]) +
      '\n\n첫 두 분석은 데이터 정리와 영상 특징을 공유한다. 서로 다른 질문을 검토하지만 독립적인 반복 실험 두 건으로 세지 않는다.\n\n'
      '[선정 이유](SELECTION.md) · [공통 방법](METHODS.md) · [실행 자원](RESOURCE_AND_MODEL_PLAN.md)')
write('pilots/SELECTION.md', '# 파일럿 선정 이유\n\n'
      'RP01은 사용자가 제시한 vision decoder와 emotion head를 구체적인 신경과학 질문에 연결한다. 장면을 설명하는 뇌 정보가 정서 설명에도 충분한지 비교할 수 있어 첫 번째로 둔다.\n\n'
      'RP03은 특정 장면과 정서의 연관을 넘어서는 뇌 패턴이 있는지 묻는다. RP01과 데이터 준비를 공유하지만, 평가할 핵심은 시각 모델의 충분성이 아니라 새로운 내용으로의 일반화다.\n\n'
      'RP05는 영화의 앞선 맥락이 현재의 정서 관련 뇌 반응을 설명하는지 묻는다. 시간 정보를 포함해 앞선 두 질문에서 다루지 못하는 문제를 검토한다.\n\n'
      '생성형 모델로 자극을 바꾸는 RP02와 시청각 조건을 직접 바꾸는 RP08은 신경과학적 잠재력이 있지만 새로운 평정과 뇌 측정이 필요하다. 개인차를 다루는 RP10은 참가자 수와 개인별 신뢰도를 먼저 확보해야 한다.\n\n'
      '이전의 학습목표 비교와 parcel 평균 비교는 필요한 경우 쓰는 방법 점검으로 옮겼다. [이전 계획](../archive/v1/pilots/README.md)은 새 파일럿의 실행 기록이 아니다.')

land = [{'version': 2, 'rq_id': c['rq_id'], 'proposal_id': c['proposal_id'], 'question': c['title'], 'scientific_contribution': c['why'], 'feasibility': c['feasibility']} for c in CARDS]
dump('research_questions/landscape.json', land)
dump('research_questions/shortlist.json', land)
for name in ['landscape.csv', 'shortlist.csv']:
    with (ROOT / 'research_questions' / name).open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(land[0])); w.writeheader(); w.writerows(land)
map_rows = [[c['rq_id'], f"[{c['title']}](../proposals/{c['proposal_id']}.md)", c['why']] for c in CARDS]
write('research_questions/LANDSCAPE.md', '# 핵심 연구 질문 10개\n\n'
      '새 질문은 NQ01–NQ10으로 표시한다. 이전 RQ 30개를 새 질문과 더해 세지 않는다. 질문을 이해한 뒤 필요한 분석 방법을 찾을 수 있도록 구성했다.\n\n' +
      table(['질문', '무엇을 묻나', '답이 알려주는 것'], map_rows) +
      '\n\n[상세 제안](../proposals/README.md) · [우선순위와 판단 근거](RANKINGS.md) · [이전 질문 30개](../archive/v1/research_questions/LANDSCAPE.md)')
write('research_questions/README.md', '# 연구 질문\n\n현재는 [핵심 질문 10개](LANDSCAPE.md)를 기준으로 작업한다. 질문 수를 유지하려고 비슷한 질문을 여러 개로 나누지 않았다. 이전 질문·방향·순위·토론 대응표는 [v1 기록](../archive/v1/README.md)에 있다.')

refs = sorted({ref['id'] for c in CARDS for ref in c['literature']})
source_rows = []
for pid in refs:
    p = PAPERS[pid]
    source_rows.append([f"[{pid} · {p['title']}]({paper_url(p)})", p['full_text_access'] or '기록 없음', p['discussion_access'] or '기록 없음', f"[확인 출처]({p['official_url']})"])
write('literature/REVISION_V2_SOURCES.md', '# 새 제안의 근거 문헌과 확인 범위\n\n'
      '기존 문헌 조사에서 확보한 자료를 사용했다. 코드·서지만 확인한 문헌과 논문 본문을 읽은 문헌을 구별한다. 아래 표는 원래 문헌 장부의 확인 범위를 유지한다. 새 질문의 세계 최초 여부를 확인한 목록은 아니다.\n\n' +
      table(['문헌', '본문 확인', 'Discussion 확인', '실제 접근 출처'], source_rows) +
      '\n\n전체 장부: [papers.csv](papers.csv). 이번에 새로 구성한 가설과 선행 결과는 [제안별 설명](../proposals/README.md)에서 구별한다.')
write('literature/novelty/REVISION_V2_REVIEW.md', '# 새 제안과 가까운 기존 연구\n\n'
      '이 검토는 기존 문헌 장부와 담당자의 확인 자료를 이용했다. 포괄적인 신규 학술 검색은 수행하지 않았으며, 새로운 모델을 쓴다는 이유만으로 독창성을 인정하지 않는다.\n\n' +
      '\n\n'.join(f"## {c['proposal_id']}: {c['title']}\n\n이미 알려진 부분: {c['novelty']['known']}\n\n이번에 검토할 부분: {c['novelty']['proposed']}\n\n추가 확인: {c['novelty']['unresolved']}" for c in CARDS))

write('revision_v2/CHANGELOG.md', '# 사용자 피드백에 따른 재구성\n\n'
      '사용자는 이전 제안이 어려운 표현으로 분석 절차를 연구 질문처럼 제시했고, 정서신경과학의 질문이 보이지 않는다고 지적했다. 이에 질문·가설·실험·파일럿 선정을 다시 구성했다.\n\n'
      '현재는 NQ01–NQ10을 사용한다. RP01–RP10은 읽기 경로를 유지하기 위해 같은 파일명을 썼지만 내용은 새 기획이다. 이전 제안은 [v1 보존본](../archive/v1/README.md)에서 확인할 수 있다.\n\n'
      '“사전 고정한 내용모형”은 정식 학술 용어로 쓰기 부적절한 임의 표현이었다. 필요한 곳에는 영상의 색·움직임·사물·장면을 설명하는 모델이라고 구체적으로 적었다. “정서관련편집”은 무엇을 바꿀지 숨기는 표현이므로, 밝기·거리·장면 속 사건 등 실제 조작 대상을 적도록 바꿨다.\n\n'
      '학습목표 비교, 데이터셋 정렬, parcel 평균과 공간 패턴 비교, 생성 영상의 해석 한계는 방법으로 남겼다. 이 점검만으로 신경과학 연구의 기여를 주장하지 않는다.\n\n' +
      '\n\n'.join(f"## {c['proposal_id']} / {c['rq_id']}\n\n{c['title']}\n\n{bullets(c['previous_links'])}" for c in CARDS) +
      '\n\n문장 편집에는 [humanizer](../skills/humanizer/SKILL.md)를 참고했다. 프로젝트 안에 지침 파일을 저장해 적용했으며, ChatGPT 앱 전역에 명령을 설치한 것은 아니다. v1의 5라운드 토론과 감사는 v2에 수행한 검토로 계산하지 않는다.')
print(f"Rendered {len(CARDS)} proposals, {len(PILOTS)} pilot plans and {len(refs)} source entries")
