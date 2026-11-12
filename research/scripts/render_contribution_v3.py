#!/usr/bin/env python3
"""실제 독립 제안·교차 토론 뒤 정리한 연구 기여 원고를 렌더링한다."""
from pathlib import Path
import csv
import json
import re

R = Path(__file__).resolve().parents[1]
catalog = json.loads((R / 'revision_v3/catalog.json').read_text())
curation = json.loads((R / 'revision_v3/curation.json').read_text())
papers = {p['canonical_id']: p for p in csv.DictReader((R / 'literature/papers.csv').open())}
by_id = {c['candidate_id']: c for c in catalog}


def write(name, text):
    p = R / name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text.rstrip() + '\n')


def dump(name, obj):
    write(name, json.dumps(obj, ensure_ascii=False, indent=2))


def table(headers, rows):
    def cell(s):
        return str(s).replace('|', '\\|').replace('\n', ' ')
    return '\n'.join(['| ' + ' | '.join(headers) + ' |', '| ' + ' | '.join(['---'] * len(headers)) + ' |'] +
                     ['| ' + ' | '.join(cell(x) for x in row) + ' |' for row in rows])


def para(value):
    if isinstance(value, list):
        return '\n\n'.join(str(v) for v in value)
    return str(value)


def paper_url(p):
    s = p['doi_or_arxiv'].strip()
    if re.fullmatch(r'10\.\d{4,9}/[^\s]+', s):
        return 'https://doi.org/' + s
    m = re.fullmatch(r'(?:arXiv:)?(\d{4}\.\d{4,5})', s)
    return 'https://arxiv.org/abs/' + m[1] if m else p['official_url']


for c in catalog:
    cid = c['candidate_id']
    parts = [f"# {c['question']}", f"{cid} · 기여 유형: {c['contribution_type']} · 현재 판단: {c['revision_decision']}",
             c['premise'], '## 왜 이 연구가 필요한가', c['why_needed'],
             '## 어떤 결과가 나와야 중요한가',
             table(['경쟁하는 설명', '설명을 구별할 관찰'], [[x['account'], x['distinguishing_observation']] for x in c['competing_accounts']]),
             c['decisive_result'], '## 그 결과를 얻었을 때 논문의 결론',
             '아래 문장은 아직 얻지 않은 결과에 대한 조건부 결론이다.', c['conclusion_if_supported'],
             '다른 설명이 지지된다면: ' + c['conclusion_if_alternative'],
             '## 정서신경과학에서 무엇이 달라지는가', c['field_impact'],
             '## 무엇을 측정하고, AI는 어디에 쓰나', para(c['minimum_design']), c['ai_enables'], c['data_scope'],
             '## 어떤 결과라면 기여가 부족한가', c['noncontribution_result'],
             '## 가장 강한 반론과 수정', c['strongest_objection'], c['response_to_objection'],
             '## 가까운 선행연구와 남은 확인']
    for ref in c['nearest_prior']:
        p = papers[ref['paper_id']]
        parts += [f"[{ref['paper_id']} · {p['title']}]({paper_url(p)})\n\n알려진 부분: {ref['what_is_known']}\n\n추가로 검토할 부분: {ref['actual_difference']}"]
    missing = c.get('missing_prior', [])
    if missing:
        parts.append('\n'.join('- ' + str(x) for x in missing))
    parts += [c['uncertainty'], '[문헌의 실제 확인 범위](../literature/REVISION_V3_SOURCES.md)',
              '## 이번 토론에서의 위치', c['relation_to_v2'],
              f"[선정·통합·보류 판단](../revision_v3/DECISIONS.md) · [실제 교차 토론](../discussions/revision_v3/SYNTHESIS.md) · [질문 목록](README.md)"]
    write('proposals/' + cid + '.md', '\n\n'.join(parts))

groups = curation['groups']
rows = []
for g in groups:
    links = ' · '.join(f"[{cid}]({cid}.md)" for cid in g['candidate_ids'])
    rows.append([g['question'], g['why_short'], g['conclusion_short'], g['impact_short'], links])
write('proposals/README.md', '# 왜 필요한지, 어떤 결론을 낼지에서 출발한 연구 질문\n\n'
      '특정 RP를 중심으로 선택하지 않고 다섯 역할이 독립적으로 제안한 뒤 서로 비판하고 수정했다. 아래 질문들은 정서신경과학의 설명을 바꾸는 연구와 측정 방법을 개선하는 연구를 함께 포함한다.\n\n'
      '각 상세 원고에는 연구의 필요성, 중요한 예상 관찰, 조건부 Conclusion, 분야에서 달라질 점을 먼저 적었다. 실제 실험 결과나 신규성이 확인된 제안이라는 뜻은 아니다.\n\n' +
      table(['연구 질문', '왜 필요한가', '중요한 결과를 얻었을 때의 결론', '분야 기여', '상세 원고'], rows) +
      '\n\n' + curation['overview'] + '\n\n'
      '[기여와 한계 비교](../revision_v3/CONTRIBUTIONS.md) · [선정·통합·보류 이유](../revision_v3/DECISIONS.md) · [실제 토론 기록](../discussions/revision_v3/SYNTHESIS.md)\n\n'
      'v2의 RP06·RP07과 첫 파일럿 순위는 자동으로 이어받지 않았다. [이전 v2](../archive/v2/README.md)와 [이전 v1](../archive/v1/README.md)은 기록으로 보존한다.')
dump('proposals/cards.json', catalog)

contrib = ['# 후보별 기여와 판단',
           '결론은 가설이 지지될 때의 주장이다. 원하는 결과에 맞춰 분석하겠다는 뜻이 아니며, 반대 결과와 판단 불가능한 결과는 상세 원고에서 구분한다.']
decisions = ['# 선정·통합·보류 판단', curation['overview']]
for g in groups:
    contrib += [f"## {g['question']}", '필요성: ' + g['why_short'], '조건부 결론: ' + g['conclusion_short'],
                '분야 기여: ' + g['impact_short'], '현재 판단: ' + g['decision'],
                ' · '.join(f"[{cid}](../proposals/{cid}.md)" for cid in g['candidate_ids'])]
    decisions += [f"## {g['question']}", g['decision'], g['rationale'],
                  ' · '.join(f"[{cid}](../proposals/{cid}.md)" for cid in g['candidate_ids'])]
for held in curation.get('not_advanced', []):
    decisions += [f"## {held['candidate_id']}: {by_id[held['candidate_id']]['question']}", held['decision'], held['reason']]
write('revision_v3/CONTRIBUTIONS.md', '\n\n'.join(contrib))
write('revision_v3/DECISIONS.md', '\n\n'.join(decisions))

write('research_questions/LANDSCAPE.md', '# 연구 질문과 기여\n\n'
      '현재 질문은 [v3 제안 목록](../proposals/README.md)과 [기여 비교](../revision_v3/CONTRIBUTIONS.md)를 따른다. 관련 후보를 묶어 정리했으며, 아래 원안 수를 모두 독립적인 연구 수로 세지 않는다.\n\n' +
      table(['독립 제안 ID', '질문', '기여 유형', '현재 판단'], [[c['candidate_id'], f"[{c['question']}](../proposals/{c['candidate_id']}.md)", c['contribution_type'], c['revision_decision']] for c in catalog]) +
      '\n\n[선정·통합·보류 이유](../revision_v3/DECISIONS.md). 이전 30개 또는 10개 질문과 합산하지 않는다.')
write('research_questions/README.md', '# 현재 연구 질문\n\n[다양한 질문과 기여](LANDSCAPE.md)를 따른다. 현재는 논문 기여를 검토하는 탐색이며, 특정 기존 RP나 파일럿 순위로 좁히지 않는다.')
write('research_questions/RANKINGS.md', '# 현재 선정 판단\n\nv2의 순위와 첫 파일럿 순위는 해제했다. 이번에는 [각 질문의 기여와 판단](../revision_v3/CONTRIBUTIONS.md), [통합·보류 이유](../revision_v3/DECISIONS.md)를 함께 본다. 신규성 미확인과 실험 부담은 과학적 잠재력과 구별한다.')
short = [{'version': 3, 'candidate_id': c['candidate_id'], 'question': c['question'], 'why_needed': c['why_needed'],
          'contribution_type': c['contribution_type'], 'conclusion_if_supported': c['conclusion_if_supported'], 'field_impact': c['field_impact'], 'decision': c['revision_decision']} for c in catalog]
active_ids = {cid for g in groups for cid in g['candidate_ids']}
for name in ['landscape', 'shortlist']:
    selected = short if name == 'landscape' else [c for c in short if c['candidate_id'] in active_ids]
    dump('research_questions/' + name + '.json', selected)
    with (R / 'research_questions' / (name + '.csv')).open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(short[0])); w.writeheader(); w.writerows(selected)

used = sorted({ref['paper_id'] for c in catalog for ref in c['nearest_prior']})
write('literature/REVISION_V3_SOURCES.md', '# v3의 문헌과 실제 확인 범위\n\n'
      '기존 문헌 장부를 사용하고 일부 지정 원문을 다시 읽었다. 각 후보가 아직 확인하지 못한 가장 가까운 선행은 별도로 적었다. 이 목록은 새 포괄 검색이나 최초성 검증의 완료를 뜻하지 않는다.\n\n' +
      table(['문헌', '본문 확인', 'Discussion 확인', '접근한 출처'],
            [[f"[{pid} · {papers[pid]['title']}]({paper_url(papers[pid])})", papers[pid]['full_text_access'], papers[pid]['discussion_access'],
              f"[출처]({papers[pid]['official_url']})"] for pid in used]) +
      '\n\n[다시 읽은 핵심 선행과 기여의 경계](../revision_v3/EVIDENCE_NOTES.md) · [전체 문헌 장부](papers.csv)')
print(f'Rendered {len(catalog)} candidate manuscripts in {len(groups)} directions')
