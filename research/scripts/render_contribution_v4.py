#!/usr/bin/env python3
"""v4 실제 원안·동료 비판·저자 응답과 Coordinator 선정을 함께 게시한다."""
from pathlib import Path
import csv
import json

ROOT = Path(__file__).resolve().parents[1]


def read(name):
    return json.loads((ROOT / name).read_text())


def write(name, value):
    p = ROOT / name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(value.rstrip() + '\n')


def dump(name, value):
    write(name, json.dumps(value, ensure_ascii=False, indent=2))


def prose(value):
    if isinstance(value, list):
        return '\n\n'.join(prose(v) for v in value)
    if isinstance(value, dict):
        return '\n\n'.join(f'{k}: {prose(v)}' for k, v in value.items())
    return str(value)


def table(headers, rows):
    def cell(v):
        return str(v).replace('|', '\\|').replace('\n', ' ')
    return '\n'.join(['| ' + ' | '.join(headers) + ' |',
                      '| ' + ' | '.join(['---'] * len(headers)) + ' |'] +
                     ['| ' + ' | '.join(cell(v) for v in row) + ' |' for row in rows])


def main():
    catalog = read('revision_v4/catalog.json')
    curation = read('revision_v4/curation.json')
    by_id = {c['candidate_id']: c for c in catalog}
    refs = read('revision_v4/REFERENCES.json')
    papers = {p['canonical_id']: p for p in csv.DictReader((ROOT / 'literature/papers.csv').open())}
    for c in catalog:
        cid = c['candidate_id']
        parts = [f"# {c['question']}",
                 f"{cid} · {c['contribution_type']} · 저자 수정본",
                 '현재 선정은 [선정·보류 기록](../revision_v4/DECISIONS.md)을 따른다. 아래 결론은 가설이 지지될 때의 주장이다. 뇌 분석 결과가 아니다.',
                 '## 왜 필요한가', prose(c['why_needed']),
                 '## 중요한 비교와 결과', prose(c['decisive_comparison']),
                 table(['경쟁 설명', '서로 다른 예측'],
                       [[a['account'], a.get('distinguishing_result', a.get('distinguishing_observation', ''))]
                        for a in c['competing_accounts']]), prose(c['decisive_result']),
                 '## 결과에 따른 Conclusion', prose(c['conclusion_if_supported']),
                 '다른 결과가 나온다면: ' + prose(c['conclusion_if_alternative']),
                 '## 정서신경과학에 대한 기여', prose(c['field_impact']),
                 '기여가 부족한 결과: ' + prose(c['noncontribution_result']),
                 '## 보유 자료로 어떻게 검정하는가', prose(c['primary_data']),
                 table(['자료', '기존 관측', '검정에서의 역할', '실행 전 확인'],
                       [[b['dataset'], b['existing_observation'], b['use_in_test'], b['still_to_verify']]
                        for b in c['data_binding']]),
                 prose(c['analysis_plan']), 'AI의 역할: ' + prose(c['ai_enables']),
                 '선택적 확장: ' + prose(c['secondary_data']),
                 '## 가장 강한 반론', prose(c['strongest_objection']), prose(c['response_to_objection']),
                 '## 가장 가까운 선행연구']
        for ref in c['nearest_prior']:
            pid = ref['paper_id']
            p = refs.get(pid, papers.get(pid, {}))
            title = p.get('title', pid)
            url = p.get('url', p.get('official_url', ''))
            link = f'[{pid} · {title}]({url})' if url else pid
            parts += [link, '알려진 부분: ' + prose(ref.get('known', '')),
                      '제안에서 추가로 구별할 부분: ' + prose(ref.get('proposed_difference', '')),
                      '실제 확인 범위: ' + prose(ref.get('access_scope', ''))]
        parts += ['## 파일럿과 중단 기준', prose(c['minimum_pilot']), prose(c['abandon_if']),
                  '## 결론의 범위와 남은 불확실성', prose(c['claim_limit']), prose(c['uncertainty']),
                  '## 실제 비판에 대한 저자 응답', prose(c.get('response_log', [])),
                  '[질문 목록](README.md) · [데이터 연결 근거](../agents/01_dataset/revision_v4_data_bridge.md) · [토론 기록](../discussions/revision_v4/SYNTHESIS.md)']
        write(f'proposals/{cid}.md', '\n\n'.join(parts))

    parts = ['# 보유 데이터에서 출발한 연구 질문', curation['overview'],
             '각 질문의 필요성, 중요한 관찰, 조건부 Conclusion, 분야 기여를 먼저 적었다. 공개 메타데이터 검산과 실제 뇌 분석의 실행 상태는 구별한다.']
    for g in curation['directions']:
        parts += [f"## {g['question']}", f"{g['direction_id']} · {g['decision']}",
                  '**왜 필요한가.** ' + g['why_short'],
                  '**어떤 결과가 중요한가.** ' + g['result_short'],
                  '**그 결과가 나온다면.** ' + g['conclusion_short'],
                  '**분야 기여.** ' + g['impact_short'],
                  '**쓸 자료.** ' + g['data_short'],
                  '**채택 전 확인.** ' + g['gate_short'],
                  ' · '.join(f'[{cid} 상세 원고]({cid}.md)' for cid in g['candidate_ids'])]
    parts += ['## 보류한 방향', table(['질문', '보류 이유'],
                 [[h['question'], h['reason']] for h in curation['held']]),
              '[선정·통합·보류 근거](../revision_v4/DECISIONS.md) · [최근 논문과의 차이](../revision_v4/PRIOR_COMPARISON.md) · [파일럿 계획](../pilots/README.md) · [실제 에이전트 토론](../discussions/revision_v4/SYNTHESIS.md)',
              'v1·v2·v3 제안은 [이전 기록](../archive/v3/README.md)에 보존했다. 이전 질문 수와 순위를 유지하려고 이번 후보를 늘리지 않았다.']
    write('proposals/README.md', '\n\n'.join(parts))
    dump('proposals/cards.json', catalog)

    dec = ['# 선정·통합·보류 기록', curation['overview']]
    for g in curation['directions']:
        dec += [f"## {g['direction_id']}: {g['question']}", g['decision'], g['rationale'],
                '원안: ' + ', '.join(g['candidate_ids']), '남은 확인: ' + g['gate_short']]
    for h in curation['held']:
        dec += [f"## {h['question']}", h['reason'], h.get('reopen_if', ''),
                '원안: ' + ', '.join(h.get('candidate_ids', []))]
    write('revision_v4/DECISIONS.md', '\n\n'.join(dec))

    decisions = {}
    for g in curation['directions']:
        for cid in g['candidate_ids']:
            decisions[cid] = g['decision']
    for h in curation['held']:
        for cid in h.get('candidate_ids', []):
            decisions[cid] = '보류: ' + h['reason']
    landscape = [{'version': 4, 'candidate_id': c['candidate_id'], 'question': c['question'],
                  'contribution_type': c['contribution_type'], 'decision': decisions.get(c['candidate_id'], c['revision_decision']),
                  'existing_data_only': c['existing_data_only']} for c in catalog]
    short = [{'version': 4, **g} for g in curation['directions']]
    for name, records in [('landscape', landscape), ('shortlist', short)]:
        dump(f'research_questions/{name}.json', records)
        with (ROOT / f'research_questions/{name}.csv').open('w', newline='') as f:
            w = csv.DictWriter(f, fieldnames=list(records[0]) if records else ['version', 'question'])
            w.writeheader()
            for r in records:
                w.writerow({k: json.dumps(v, ensure_ascii=False) if isinstance(v, (dict, list)) else v for k, v in r.items()})
    write('research_questions/LANDSCAPE.md', '# 연구 질문의 전체 검토 결과\n\n' +
          table(['원안', '질문', '현재 판단'], [[r['candidate_id'], f"[{r['question']}](../proposals/{r['candidate_id']}.md)", r['decision']] for r in landscape]) +
          '\n\n원안 수는 독립 연구 수가 아니다. [현재 방향과 기여](../proposals/README.md) · [실제 통합·보류 기록](../revision_v4/DECISIONS.md).')
    write('research_questions/README.md', '# 현재 연구 질문\n\n[질문과 기여](../proposals/README.md)부터 읽는다. [원안 전체](LANDSCAPE.md)에는 통합·보류한 제안도 포함한다.')
    print(json.dumps({'rendered_cards': len(catalog), 'directions': len(short), 'held_families': len(curation['held'])}))


if __name__ == '__main__':
    main()
