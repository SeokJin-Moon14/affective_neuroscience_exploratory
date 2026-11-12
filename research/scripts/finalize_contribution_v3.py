#!/usr/bin/env python3
"""실제 저자 수정본을 모은다. 선정 판단은 Coordinator가 작성한 curation.json을 따른다."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

R = Path(__file__).resolve().parents[1]
if (R / 'revision_v4/version.json').exists():
    raise SystemExit('v3 주력 제안은 데이터 적합성 문제로 철회됐습니다. revision_v4의 최신 제약을 따르세요.')
roles = ['02_affective_neuroscience', '03_vision_decoding', '04_brain_foundation',
         '05_multimodal_dynamics', '06_frontier_ai']

def read(name):
    return json.loads((R / name).read_text())

def write(name, value):
    (R / name).parent.mkdir(parents=True, exist_ok=True)
    (R / name).write_text(value.rstrip() + '\n')

def dump(name, value):
    write(name, json.dumps(value, ensure_ascii=False, indent=2))

source_paths = [f'agents/{r}/revision_v3_revised.json' for r in roles]
source_paths += [f'agents/{r}/revision_v3_additional_revised.json'
                 for r in ['04_brain_foundation', '06_frontier_ai']]
catalog, source_records = [], []
for path in source_paths:
    cards = read(path)
    catalog.extend(cards)
    source_records.append({'path': path, 'sha256': hashlib.sha256((R/path).read_bytes()).hexdigest(),
                           'candidate_ids': [c['candidate_id'] for c in cards]})

# 과학적 판정과 원저자 원고는 보존하며 독자용 사본에서만 표현을 다듬는다.
replacements = {
    '자연 사진 가족': '실제 사진 묶음', '사진 가족': '사진 묶음',
    '측정 계약': '문항·자극 제시·측정 조건', '사진의 교차 지지': '두 사진 비교의 실현성',
    '실측 지원 검증': '실제 측정 자료와 지표 적용 범위의 확인',
    '원 목표 평정': '원 논문이 예측하려던 평정', '원 목표 문항': '원 논문의 평정 문항',
    '재적합': '재학습',
}
titles = {
    'C03-A': '정서 뇌 지표는 언제 사진의 차이를 정서의 차이로 잘못 읽을까?',
    'C04-B': '정서 뇌 지표가 잘못 해석되는 사진 조건을 미리 찾을 수 있을까?',
    'C05-B': '정서 뇌 지표의 해석을 시험할 사진을 어떻게 고를까?',
    'C06-A': '위협의 원인이 달라도 뇌 반응이 바뀌는 방식은 같을까?',
    'C06-B': '뇌 자료로 새로운 상황 주석을 찾으면 어떤 정서 연구에 도움이 될까?',
}

def natural(value):
    if isinstance(value, str):
        for a, b in replacements.items():
            value = value.replace(a, b)
        return value
    if isinstance(value, list):
        return [natural(x) for x in value]
    if isinstance(value, dict):
        return {k: natural(v) for k, v in value.items()}
    return value

edited, edits = [], []
for original in catalog:
    c = natural(original)
    if c['candidate_id'] in titles:
        c['question'] = titles[c['candidate_id']]
    if isinstance(c.get('missing_prior'), str):
        c['missing_prior'] = [c['missing_prior']]
    # 원래 응답은 검토 이력이므로 원문 그대로 둔다.
    c['response_log'] = original['response_log']
    edits.append({'candidate_id': c['candidate_id'], 'changed_fields': [k for k in c if c[k] != original.get(k)],
                  'original_question': original['question'], 'reader_question': c['question']})
    edited.append(c)
catalog = sorted(edited, key=lambda c: c['candidate_id'])
dump('revision_v3/catalog.json', catalog)
dump('revision_v3/AUTHOR_SOURCES.json', source_records)
dump('revision_v3/EDITORIAL_CHANGES.json', {'scope': '독자용 사본의 표현 정리. 저자 원본·검토 응답은 보존.',
                                         'replacements': replacements, 'cards': edits})

peers = []
for role in roles:
    p = f'agents/{role}/revision_v3_peer_review.json'
    peers.extend({'source': p, 'review': r} for r in read(p))
for role in ['02_affective_neuroscience', '05_multimodal_dynamics']:
    p = f'agents/{role}/revision_v3_additional_review.json'
    peers.extend({'source': p, 'review': r} for r in read(p))
dump('revision_v3/peer_reviews.json', peers)

curation = read('revision_v3/curation.json')
for g in curation['groups']:
    if g['direction_id'] in ['D01', 'D02']:
        g['decision'] = '조건부 설계 발전. 실제 동료 비판과 원저자 수정을 거쳤으며, 직접 선행과 핵심 자극 비교의 실현성 확인 전 최종 채택은 유보한다.'
curation['groups'][0]['question'] = '정서적인 장면에서 시선은 눈에 띄는 곳과 판단에 필요한 곳 중 어디로 향할까?'
dump('revision_v3/curation.json', curation)

version = read('revision_v3/version.json')
version.update(status='planning_revision_complete', independent_candidate_count=10,
               additional_candidate_count=2, peer_review_count=len(peers),
               initial_contribution_review_count=10, response_check_count=2,
               research_direction_count=len(curation['groups']),
               experiments_run=False, novelty_verified=False,
               updated_at_utc=datetime.now(timezone.utc).isoformat())
dump('revision_v3/version.json', version)

discussion = ['# v3 실제 교차 토론과 수정',
    '다섯 역할이 독립 원안 10개를 작성하고, 서로 다른 역할의 후보에 동료 비판 10건을 보냈다. 별도 기여 검토자는 10개를 모두 검토했다. 원저자들은 실제 메시지로 응답하고 발전·통합·보류를 기록했다. 첫 통합 뒤 지표·위협에 치우친 구성을 보완하려고 두 역할이 서로의 추가 원안을 읽기 전에 후보를 하나씩 더 썼고, 다른 두 역할이 각각 비판한 뒤 저자가 수정했다.',
    '추가 검토에서도 정서 전용 회로나 일반 사건 표상과의 완전한 독립을 요구하지 않았다. 기존 설명과 구별되는 예측이 있고 그 결과가 정서 연구의 판단을 바꾸는지를 기준으로 삼았다. C06-A에서 이 기준을 과도하게 좁혔던 부분은 감사자가 다시 지적했고 실제 수정까지 확인했다.',
    '[처음 원안과 배정](../../revision_v3/PEER_ASSIGNMENTS.json) · [추가 원안과 배정](../../revision_v3/ADDITIONAL_ASSIGNMENTS.json) · [동료 비판 12건](../../revision_v3/peer_reviews.json) · [기여 검토 10건](../../agents/12_adversarial_review/revision_v3_contribution_review.json) · [두 후보 후속 검토](../../agents/12_adversarial_review/revision_v3_response_check.json)',
    '## 실제로 통합한 부분',
    'C03-A·C04-B·C05-B 저자들은 고정된 정서 지표의 적용 범위를 확인하는 하나의 연구로 통합하기로 실제 메시지를 주고받았다. C03-A의 시각 조건, C04-B의 지표 적용 조건, C05-B의 자극 선택을 같은 실험에 배치했다. C02-A의 보조 측정은 추가 성공 조건이 있어야 독립적인 성과가 되므로, Coordinator는 독자용 목록에서 이 네 원안을 한 방법론 방향으로 묶었다. 이 마지막 목록 편집을 네 저자의 새 합의라고 쓰지 않는다.',
    'C02-B와 C04-A 저자들은 정서 범주 성분과 사건 요소를 비교하는 하나의 질문으로 합쳤다. 다만 두 설명을 실제로 가를 장면과 직접 선행 차이가 불명확해 채택은 보류했다. C06-B는 이 연구의 특정 실패가 확인될 때만 쓸 수 있는 선택적 후속 도구로 낮췄다.',
    '## 원저자 응답에서 달라진 점']
source_by_id = {cid: r['path'] for r in source_records for cid in r['candidate_ids']}
for c in catalog:
    discussion += [f"### {c['candidate_id']} · {c['revision_decision']}", c['question']]
    for response in c['response_log']:
        discussion += [f"**{response['review_id']} — {response['position']}**\n\n{response['substantive_change']}\n\n남은 점: {response['remaining']}"]
    discussion += [f"[원저자 수정본](../../{source_by_id[c['candidate_id']]})"]
discussion += ['## 확인 범위',
    '위 기록은 실제 제안·비판·응답이다. 검토자들이 모든 과학적 쟁점에 동의했다는 뜻은 아니다. 특히 보류 후보의 핵심 비교와 모든 새 후보의 직접 선행 확인이 남아 있다. 원고의 필요 항목과 내부 링크를 검사한 결과를 연구 가치나 최초성의 승인으로 쓰지 않는다.',
    '[선정·통합·보류 판단](../../revision_v3/DECISIONS.md) · [연구 질문과 기여](../../proposals/README.md)']
write('discussions/revision_v3/SYNTHESIS.md', '\n\n'.join(discussion))

report = ['# 정서신경과학에서 어떤 새 결론을 얻을 것인가',
    '이번 재검토는 네 연구 방향으로 정리했다. 정서 관련 정보의 선택, 기억 내용의 보존과 왜곡, 여러 상황에서 재사용되는 뇌 반응의 변화 방식, 정서 뇌 지표의 비교 가능성이다. RP03을 중심으로 주제를 좁히지 않았다. 각 질문에서 왜 연구가 필요한지와 어떤 결과가 나와야 중요한지를 먼저 정하고, 그 결과에 맞는 조건부 Conclusion과 분야 기여를 썼다.',
    '[질문별 필요성·핵심 결과·Conclusion·기여를 한 번에 읽기](../proposals/README.md)',
    '## 네 방향의 핵심 주장']
for g in curation['groups']:
    report += [f"### {g['question']}", g['why_short'], '중요한 예상 관찰: ' + g['result_short'],
               '그 관찰이 지지할 결론: ' + g['conclusion_short'], '분야 기여: ' + g['impact_short']]
report += ['## 토론으로 바뀐 선택',
    '같은 지표의 반례를 찾는 세 원안을 독립 연구처럼 세지 않았다. 자극 정보로 점수를 보정하는 후보도 뇌 정보가 실제로 필요한 판단을 남길 때만 별도의 방법 기여가 된다고 제한했다. 반대로 일반적인 사건 표상 안에서 정서와 관련된 관계를 설명할 수 있다는 이유만으로 연구를 탈락시키지 않았다.',
    '미래 내용을 예상하는 뇌 반응, 피해가 생기는 경로, 뇌 자료로 새 주석을 찾는 절차는 현재의 관찰만으로 중요한 새 결론을 정하기 어려워 보류했다. 범주 성분과 사건 요소의 조합 질문은 두 저자가 합쳤지만 결정적 비교가 아직 불명확하다. [각 원안의 처리 이유](../revision_v3/DECISIONS.md)와 [실제 비판·수정 기록](../discussions/revision_v3/SYNTHESIS.md)을 함께 남겼다.',
    '## 현재 완료한 것과 남은 것',
    '완료한 것은 질문 발굴, 실제 교차 토론, 원저자 수정, 통합·보류 판단, 읽기용 원고다. 실제 뇌 분석·모델 실험·새 데이터 수집을 완료한 것이 아니다. 모든 Conclusion은 예상 관찰을 얻었을 때 가능한 주장이다. 반대 결과의 의미와 기여가 남지 않는 결과도 각 원고에 적었다.',
    '기존 문헌 장부와 확보한 원문 일부를 다시 읽었고, 모델 대립 자극의 선행은 저자의 공식 코드 README에서 확인했다. 기억·시선·표상 변환·지표 보정의 가장 가까운 선행을 모두 원문 대조한 상태는 아니다. 따라서 네 방향은 논문으로 검토할 후보이며 최초성이 검증된 확정 주제가 아니다. [실제 문헌 확인 범위](../literature/REVISION_V3_SOURCES.md).',
    '사용자가 보유한 Horikawa, Emo-FilM, Mind Captioning, NSD, Spacetop의 원자료는 현재 환경에서 직접 분석하지 않았다. 기존 자료는 후보 장면과 모델 예측을 탐색하는 데 활용할 수 있으나, 추가 정보 제시·회상·편집 장면에 필요한 뇌 반응이 이미 있다고 가정하지 않았다. [자료별 시작 범위](../pilots/README.md).']
write('synthesis/FINAL_REPORT.md', '\n\n'.join(report))

write('pilots/README.md', '''# 기존 자료에서 시작할 부분과 새로 필요한 관측

이번에는 첫 파일럿을 하나로 선택하지 않았다. 네 방향의 최소 설계는 각각의 원고에 있고, 이전 세 파일럿의 순위와 설계는 [v2 기록](../archive/v2/pilots/README.md)에 보존했다. 아래는 실행 결과가 아니라 자료 사용 범위다.

| 방향 | 기존 자료에서 시작할 부분 | 핵심 주장에 추가로 필요한 관측 |
|---|---|---|
| 시선과 정보 선택 | 장면 전체와 부분 정보가 서로 다른 정서 예측을 만드는 자극 후보 탐색 | 첫 관측을 달리한 시선 기록, 정보 순서를 조작한 실제 신경 측정 |
| 정서와 기억 내용 | 원본과 가까우면서 정서 전형성과 일반 의미가 다른 변형 후보 탐색 | 초기 지각 확인, 선택지 제시 전 회상 신경 반응, 이후 세부 기억 선택 |
| 공통된 변화 방식 | 위협 원인이 다른 장면과 정서 주석의 범위 조사 | 단일 편집·결합 편집·대조 장면에 대한 새 주석과 실제 뇌 반응 |
| 정서 뇌 지표의 해석 | 원 지표의 가중치·공간·대상 변수와 보유 자료의 대응 확인 | 원래 평정 문항과 같은 제시 조건에서의 뇌 측정; 새 사진 묶음의 조건 비교 |

Horikawa와 Emo-FilM의 외부 정서 주석을 스캔 참가자의 개인별 평정으로 대신하지 않는다. Spacetop의 자극 후 평정을 연속 정답으로 보지 않는다. NSD의 정서 정답과 Mind Captioning의 정확한 과제·텍스트 출처는 확인 전이다. 이 자료들에 새로 편집한 장면의 뇌 반응이나 필요한 회상 기록이 있다고 가정하지 않는다.

이 단계에서 원자료 파일을 마운트하거나 모델 가중치를 실행하지 않았다. 기존 자료만으로 할 수 있는 탐색과 새 관측이 필요한 핵심 검정을 구별해 계획했다. [연구 질문과 기여](../proposals/README.md).
''')

write('synthesis/FINAL_AUDIT.md', '''# v3 검토 범위

다섯 역할의 첫 제안 10개와 추가 제안 2개를 대상으로 실제 동료 비판 12건, 첫 제안 전체에 대한 별도 기여 검토 10건, 두 수정안에 대한 후속 검토를 수행했다. 원저자 응답과 실제 전달 기록은 [토론 문서](../discussions/revision_v3/SYNTHESIS.md) 및 연결된 역할 파일에서 확인한다.

검토는 연구의 필요성, 결론을 바꿀 관찰, 분야 기여에 집중했다. 일반 표상과 정서가 완전히 분리되어야 한다는 요구는 적용하지 않는다. 최초성·실현성·실험 성공을 승인한 기록이 아니다. 네 방향은 조건부 설계 발전 단계이며 나머지 원안의 보류·통합을 보존했다.

[문서 구조·참조·원본 보존 검사](../revision_v3/VALIDATION.json)는 기술적인 파일 검사다. 내부 링크가 맞거나 필수 항목이 있다는 이유로 연구 가치가 입증되지는 않는다. 이전 v2의 검토 결과는 [역사적 기록](../archive/v2/synthesis/FINAL_AUDIT.md)이며 새 질문의 검증으로 쓰지 않는다.
''')
write('synthesis/DIVERSITY_AUDIT.md', '''# 연구 방향의 범위

현재 네 방향은 시각 정보 선택, 정서적 기억의 내용, 여러 사건에서의 신경 변화, 정서 신경 측정의 해석을 다룬다. 세 방향은 정서와 뇌표상의 관계를 밝히는 발견 후보이고 한 방향은 방법론이다. 독립 원안 12개를 논문 12편이나 확정 기여 12개로 세지 않는다.

첫 제안들은 지표 검증과 위협에 치우쳤다. 그래서 별도 추가 탐색에서 시선과 기억을 검토했다. RP03을 중심으로 전체를 묶지 않았고, v2 RP06·RP07과 이전 파일럿 순위를 유지하지 않았다. 범위를 늘린 것만으로 깊이가 확보됐다는 뜻은 아니며, 각 질문의 중요한 관찰과 가장 가까운 선행 차이를 함께 읽어야 한다.

[현재 질문](../proposals/README.md) · [통합·보류 이유](../revision_v3/DECISIONS.md).
''')
write('synthesis/OPPORTUNITY_MAP.md', '''# 현재 검토할 연구 기회

현재 판단은 [네 연구 방향의 필요성·조건부 결론·기여](../proposals/README.md)를 따른다. AI의 역할은 각각 관측할 정보 선택을 모델링하기, 기억을 구별할 변형 장면 만들기, 새로운 조작 조합의 신경 변화를 예측하기, 지표가 잘못 해석되는 조건을 찾기다.

새 모델을 적용했다는 사실만으로 신규성을 인정하지 않는다. 직접 선행 대조와 핵심 장면 비교의 실현성이 남아 있다. 이전 기회 지도는 [v2 기록](../archive/v2/synthesis/OPPORTUNITY_MAP.md)에 보존했다.
''')
write('RESEARCH_STATUS.md', '''# 연구 진행 상태

최신 작업은 v3 연구 기획 재검토다. 다양한 질문의 필요성·중요한 예상 결과·조건부 Conclusion·Affective Neuroscience 기여를 다시 작성했다. RP03을 중심으로 선정하지 않았다.

다섯 역할의 첫 원안 10개와 추가 원안 2개에 대해 실제 동료 비판과 원저자 수정을 마쳤다. 현재는 [네 연구 방향](proposals/README.md)으로 정리하며, 겹친 원안의 통합과 핵심 비교가 부족한 원안의 보류는 [판단 기록](revision_v3/DECISIONS.md)에 남겼다. 현재의 설계 발전은 최초성이나 실험 가능성의 확정이 아니다.

이번에 완료한 범위는 질문 발굴·토론·수정·문서화다. 실제 뇌 분석·모델 실험·새 측정은 수행하지 않았다. 직접 근접 선행과 핵심 자극 비교의 실현성 확인은 남아 있다. 보유 데이터의 추가 확인을 Axis·질문 탐색의 선행 조건으로 삼지는 않았다.

사용자는 Horikawa, Emo-FilM, Mind Captioning, NSD, Spacetop을 보유한다. 현재 환경에 원자료가 마운트되었거나 필요한 개인별 평정·시선·회상·편집 자극의 뇌 반응이 있다고 가정하지 않는다. [보유 자료에서 시작할 범위](pilots/README.md).

v1·v2의 제안과 토론은 [이전 기록](archive/v2/README.md)에 보존했다. 그 결과를 현재 질문의 검증 완료로 인용하지 않는다. 현재 기준은 [AGENTS.md의 최신 사용자 지시](AGENTS.md)와 [v3 작업 기준](revision_v3/PROTOCOL.md)을 따른다.

원격 정본은 GitHub SeokJin-Moon14/affective_neuroscience_exploratory의 research/independent-exploration-20261112 브랜치다. 마지막 원격 저장 성공은 저장소 backup/LAST_SUCCESS.json을 따른다. 사용자 컴퓨터에 전체 자료를 내려받을 필요는 없다. 이 기록은 세션 종료 후의 상시 실행이나 ChatGPT 프로젝트 자동 동기화를 뜻하지 않는다.
''')
dump('synthesis/validation_report.json', {'version': 3, 'current_report': '../revision_v3/VALIDATION.json',
                                        'scope': '기술적 문서 검사. 과학적 유효성 판정 아님.'})
dump('synthesis/link_check.json', {'version': 3, 'current_report': '../revision_v3/VALIDATION.json'})
dump('synthesis/deliverables_manifest.json', {'version': 3, 'catalog': '../revision_v3/catalog.json',
     'curation': '../revision_v3/curation.json', 'author_sources': '../revision_v3/AUTHOR_SOURCES.json',
     'main': '../proposals/README.md', 'report': 'FINAL_REPORT.md', 'experiments_run': False})
print('Prepared v3 catalog, actual discussion record, and current entry documents')
