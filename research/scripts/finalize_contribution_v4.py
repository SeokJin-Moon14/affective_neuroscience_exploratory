#!/usr/bin/env python3
"""실제 v4 저자 수정이 모두 끝난 뒤 현재 연구 목록과 운영 문서를 갱신한다."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
if (ROOT / 'interest_review/USER_FEEDBACK.json').exists():
    raise SystemExit('사용자 평가 이후 v4를 현재 선정으로 다시 게시·검사하지 않습니다. interest_review를 확인하세요.')


def write(name, value):
    p = ROOT / name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(value.rstrip() + '\n')


def dump(name, value):
    write(name, json.dumps(value, ensure_ascii=False, indent=2))


def main():
    paths = sorted(ROOT.glob('agents/0[2-8]_*/revision_v4_revised.json'))
    if len(paths) != 7:
        raise SystemExit('7개 제안 역할의 실제 저자 수정본이 모두 필요합니다.')
    catalog, sources = [], []
    for p in paths:
        cards = json.loads(p.read_text())
        catalog.extend(cards)
        sources.append({'path': str(p.relative_to(ROOT)), 'sha256': hashlib.sha256(p.read_bytes()).hexdigest(),
                        'candidate_ids': [c['candidate_id'] for c in cards]})
    if len(catalog) != 10:
        raise SystemExit('이번 실제 원안10개와 수정본 수가 다릅니다. 수동 확인이 필요합니다.')
    by_id = {c['candidate_id']: c for c in catalog}
    if 'U002' not in [p['paper_id'] for p in by_id['D02-A']['nearest_prior']]:
        by_id['D02-A']['nearest_prior'].append({
            'paper_id': 'U002',
            'known': '같은 MC 지각·심상 자료에서 시각·의미 특징 및 내용 captioning을 연구한 직접 선행이다.',
            'proposed_difference': '심상에서도 내용을 판독할 수 있다는 사실을 넘어 정서 관계와 풍부한 내용 관계의 상대적 변화가 다른 예측을 하는지 검정한다. 원문에서 같은 비교를 이미 했는지는 확인 전이다.',
            'access_scope': '공식 README·코드·데이터 문서·공개 캡션과 일부 이벤트 확인. 원문 전체·Discussion 직접 확인 아님.'})
        by_id['D02-A']['coordinator_edit'] = 'U002를 공통 문헌 목록에 명시적으로 연결했다. 저자 원본 파일은 변경하지 않았다.'
    dump('revision_v4/FINAL_AUTHOR_SOURCES.json', sources)
    dump('revision_v4/catalog.json', catalog)

    directions = [
        {
            'direction_id': 'V4-01', 'candidate_ids': ['D07-A'],
            'question': '비슷한 정서라도 범주가 달라지면 뇌에서 더 다르게 표현될까?',
            'decision': '파일럿 후보로 선정. 주석의 척도와 경계 주변 영상이 실제 검정을 지원해야 한다.',
            'why_short': '뇌 활동으로 정서 이름을 잘 맞힌다고 해서 뇌가 정서를 범주별로 나눈다고 말할 수는 없다. 연속적인 차이에도 이름을 붙여 분류할 수 있기 때문이다. 정서 범주가 실제 뇌 표현의 구조와 연결되는지 묻는다.',
            'result_short': '정서 평정과 장면 내용의 차이가 비슷한 영상들을 비교한다. 그중 두 정서의 점수 우열이 바뀌는 지점에서 뇌 반응의 차이가 더 커지고, 다른 종류의 장면에서도 같은 양상이 나타나야 한다.',
            'conclusion_short': '그 결과가 나온다면, 검사한 정서 범주는 단순한 분류 이름을 넘어 가까운 장면들을 구별하는 뇌 표현의 구조와 연결된다고 말할 수 있다. 그 구조를 연속 모델이 잘 설명하는지는 별도의 질문이다.',
            'impact_short': '정서의 범주가 뇌에 어떻게 나타나는지에 대해, 분류 정확도나 군집 그림보다 직접적인 근거를 제시한다. 반대로 충분한 감도에서도 이런 구조가 없다면 범주 예측 성공의 해석 범위를 좁힌다.',
            'data_short': 'Horikawa의 기존 영상별 fMRI·category/dimension 평정. 기존 영상 특징과 MC의 영상별 20개 사람 캡션으로 내용 차이를 비교한다. 새 측정은 필수가 아니다.',
            'gate_short': '범주 점수의 비교 가능한 척도, 실제 전환 부근의 영상·내용 겹침을 먼저 확인한다. 집계 점수의 전환을 개인이 느끼는 감정의 경계로 해석하지 않는다. P001과 범주지각 직접 선행의 중복 확인은 남아 있다.',
            'rationale': 'D07-A의 두 동료 비판과 데이터 심사 뒤 저자가 수정했다. 국소 구조의 관찰과 연속/범주 모델의 승패를 분리한 점이 핵심이다. 기존 자료로 관찰할 대상과 그 결과가 바꿀 해석이 구체적이므로 파일럿 후보로 남긴다. 신규성과 실제 검정력을 확정한 채택은 아니다.'
        },
        {
            'direction_id': 'V4-02', 'candidate_ids': ['D08-A'],
            'question': '장면이 달라도 같은 정서를 나타내는 뇌 패턴은, 비슷한 정서도 잘 구별할까?',
            'decision': '파일럿 후보로 선정. 기존 주석·내용의 겹침을 확인한 뒤 첫 분석 대상으로 권고한다.',
            'why_short': '장면이 바뀌어도 같은 정서를 나타내는 능력과, 비슷한 정서들의 차이를 남기는 능력은 다르다. 장면 변화에 잘 견디는 뇌 패턴이 정서를 더 세밀하게 구별하는지, 여러 뇌 영역이 서로 다른 정서 차이를 보존하는지 묻는다.',
            'result_short': '같은 평가 영상과 같은 정서 대비를 사용했을 때, 어느 영역은 장면이 비슷할 때 세밀한 차이를 잘 구별하고 다른 영역은 새로운 장면에서 그 차이를 더 잘 유지할 수 있다. 중요한 것은 평균 성능의 역전뿐 아니라 어떤 정서 차이가 남고 줄어드는지를 새 영상에서 맞히는 것이다.',
            'conclusion_short': '영역별 전체 감도와 내용 민감도만으로 설명되지 않는 관계 차이가 나온다면, 장면을 넘어 일반화하는 능력과 세밀한 정서 구별이 하나의 순서로 좋아지지는 않는다고 결론내린다. 검사한 뇌 표현들이 서로 다른 정서 차이를 보존한다는 조직상의 발견이다.',
            'impact_short': '내용에 민감한 시각 영역의 정서 표현을 단순히 덜 완성된 표현으로 보지 않게 한다. 정서 모델도 평균 정확도뿐 아니라 어떤 구별을 일반화하고 어떤 차이를 보존하는지 뇌와 함께 설명해야 한다.',
            'data_short': 'Horikawa의 영상 시청 fMRI와 기존 연속 정서 평정. 기존 semantic·시각 특징과 MC 사람 캡션으로 내용군을 정한다. MC 반복은 선택적 보조이며 핵심 검정은 Horikawa에서 한다.',
            'gate_short': '여러 정서 대비가 서로 다른 내용군에도 있어야 한다. 동일 평가 영상을 고정하고 학습 내용군만 바꾼다. 한 대비의 성능 차이만 남거나 내용·감도 차이로 충분하면 표현의 분업을 주장하지 않는다. P001 및 직접 후속 선행과의 중복은 확인해야 한다.',
            'rationale': 'D08-A는 동료 두 명과 데이터 담당의 비판을 반영해 동일 평가 영상·여러 대비의 상대적 보존·공통/영역별 모형의 차이를 명시했다. D07-A의 범주 전환 경계가 없어도 성립하는 별도 질문이며, 공통 정서 패턴 존재를 확인하는 데서 끝나지 않는다.'
        },
        {
            'direction_id': 'V4-03', 'candidate_ids': ['D02-A', 'D03-A', 'D04-A', 'D05-A', 'D06-A'],
            'question': '장면을 떠올릴 때, 정서와 관련된 차이는 다른 장면 정보보다 더 잘 남을까?',
            'decision': '다섯 원안을 한 파일럿 후보로 통합. 기존 MC 시험영상과 심상 구간이 비교를 지원하는지 먼저 확인한다.',
            'why_short': '머릿속에 떠올린 장면에서 물체와 사건을 읽어냈다고 해서, 장면들 사이의 정서적 차이도 그대로 남았다고 볼 수는 없다. 장면을 떠올리면 모든 정보가 비슷하게 약해지는지, 정서와 관련된 차이는 더 남거나 더 줄어드는지 묻는다.',
            'result_short': '같은 영상을 볼 때와 떠올릴 때의 뇌 반응을 비교한다. 물체·행동·사건의 정보를 자세히 나타낸 AI 모델로 예상한 것과 달리, 정서가 다른 장면들의 구별이 더 남거나 줄어드는 양상이 반복돼야 한다. 전체 신호가 약해지는 설명과 장면의 의미가 남는 설명도 함께 검토한다.',
            'conclusion_short': '그 결과가 나오면, 검사한 심상 과제에서 장면의 정서 관련 관계는 다른 내용과 같은 비율로 유지되지 않았다고 말할 수 있다. 정서 차이가 더 잘 남는 결과와 더 크게 줄어드는 결과 모두 장면 재구성의 성격을 알려 준다.',
            'impact_short': '뇌가 장면을 되살릴 때 무엇을 보존하는지 설명하고, 물체·사건의 복원만으로 정서 관련 관계의 복원까지 평가할 수 있는지 밝힌다. 단순한 지각→심상 정서 판독의 성공은 기여로 세지 않는다.',
            'data_short': 'MC의 같은 원영상에 대한 testPerception·testImagery, 기존 사람 캡션과 Horikawa 원영상의 정서 주석. 공식 제외를 적용하면 시험 대상은 추가 QC 전 최대 71개다.',
            'gate_short': '기존 71개 안에서 정서와 내용 설명이 실제로 다른 예측을 내야 한다. cue·심상·후속 실제영상의 신호와 처리 window를 확인한다. 개인의 심상 중 감정이나 객관적 기억 오류를 측정한 것으로 해석하지 않는다. U002와 직접 심상 선행의 동일 분석 여부도 남은 확인이다.',
            'rationale': '다섯 저자가 실제 토론으로 같은 핵심 관찰·결론임을 인정하고 통합했다. 시각 ROI와 visual latent 분석은 보조 분석이다. 특정 과제의 표현 변화를 검정하는 후보로 남기되, 적은 시험영상과 시점 분리가 가장 큰 실현성 조건이다.'
        }
    ]
    held = [
        {'candidate_ids': ['D02-B'], 'question': '정서가 달라도 좋고 나쁨을 같은 뇌 신호로 읽을 수 있을까?',
         'reason': '범주 내부 순서와 공정한 적응 비교로 개선했지만, 기존의 공통·유형별 표현과 맥락 의존성 결론을 넘어설 기여가 아직 약하다. 저자와 최종 검토자가 주력 미채택·조건부 보존에 동의했다.',
         'reopen_if': '일반적인 domain shift를 보여 주는 데서 끝나지 않고, 구체적인 공통 valence 해석을 수정할 반례와 직접 선행의 차이가 명확해질 때 재검토한다.'},
        {'candidate_ids': ['D03-B'], 'question': '시각 디코더를 거치며 정서 정보가 사라지는가?',
         'reason': '기존 자료로 계산할 수는 있지만 일반적인 압축·대리측정 손실 이상의 연구 필요성이 부족하다. 실제 분석은 생성 영상이 아니라 시각 특징 판독이다.',
         'reopen_if': '그 변환을 사용하는 구체적인 정서 연구에서 어떤 중요한 설명 선택이 달라지는지 정해질 때 검토한다. 단순 ROI 점수 역전으로 구제하지 않는다.'},
        {'candidate_ids': ['D04-B'], 'question': '내용 설명에 맞춘 AI 학습이 정서 관련 뇌 차이를 놓치는가?',
         'reason': '캡션 자체의 범위와 학습 과정의 손실을 구별하도록 개선했지만, 모델의 정보 손실이 바꿀 구체적인 신경과학 설명이 부족하다. D03-B와 합쳐 새 연구로 세지 않는다.',
         'reopen_if': '특정 시각·의미 계산 설명을 선택하는 실제 과학 질문에서 모델 목표 때문에 결론이 달라지는 경우가 명확해질 때 재검토한다.'},
        {'candidate_ids': [], 'question': '여러 정서가 함께 드러나는 장면은 각 정서 표현의 합으로 설명될까?',
         'reason': 'Coordinator의 추가 발상을 정서·데이터 담당이 검토했다. 완전히 제외한 조합의 전용 interaction 계수는 학습할 수 없고, 기존 조합 분포도 미확인이다. 독립 원안10개에 포함하지 않는다.',
         'reopen_if': '다른 조합에서 배운 공유 구조가 실제 보류 조합의 뇌 반응을 예측할 수 있는 관측 범위가 있고, 단순 비선형 encoding 개선 이상의 결론이 분명할 때 재검토한다.'}
    ]
    curation = {'version': 4,
                'overview': '7개 제안 역할이 만든 10개 원안을 데이터 담당과 동료들이 검토하고 저자가 수정했다. 서로 같은 MC 원안 5개는 1개로 합쳤고, 기여가 부족한 3개는 주력에서 보류했다. 현재 남긴 것은 아래 3개 파일럿 후보다. 모두 기존 관측으로 설계했지만 실제 주석·뇌 배열의 지원 범위와 직접 선행의 중복을 확인해야 하며, 검증된 발견이나 최초성이 확정된 주제라는 뜻은 아니다.',
                'directions': directions, 'held': held,
                'practical_order': ['V4-02', 'V4-01', 'V4-03'],
                'experiments_run': False}
    dump('revision_v4/curation.json', curation)
    now = datetime.now(timezone.utc).isoformat()
    dump('revision_v4/version.json', {'version': 4, 'status': 'planning_complete_with_explicit_conditions',
         'updated_at_utc': now, 'raw_candidates': 10, 'proposal_roles': 7, 'data_review_count': 10,
         'active_rqs': [g['direction_id'] for g in directions], 'held_full_candidates': ['D02-B', 'D03-B', 'D04-B'],
         'priority': {'1': ['Horikawa', 'MC', 'NSD'], '2': ['Emo-FilM'], '3': ['Spacetop']},
         'experiments_run': False, 'public_metadata_checks_run': True,
         'novelty_fully_verified': False,
         'reason': '기존 관측에 맞춘 제안·실제 토론·저자 수정·선정·파일럿 계획을 완료했다. 실제 BOLD 분석과 직접 선행 전체 확인은 수행 완료로 표시하지 않는다.'})
    plans = [
        {'pilot_id': 'P4-01', 'direction_id': 'V4-02', 'path': 'pilots/v4/GENERALIZATION_AND_DETAIL.md', 'status': '계획 완료·뇌 분석 미실행', 'existing_data_only': True},
        {'pilot_id': 'P4-02', 'direction_id': 'V4-01', 'path': 'pilots/v4/EMOTION_BOUNDARIES.md', 'status': '계획 완료·뇌 분석 미실행', 'existing_data_only': True},
        {'pilot_id': 'P4-03', 'direction_id': 'V4-03', 'path': 'pilots/v4/MC_IMAGERY.md', 'status': '계획 완료·공개 ID 검산 일부 실행·뇌 분석 미실행', 'existing_data_only': True}]
    dump('pilots/plans.json', {'version': 4, 'pilots': plans, 'metadata_check': 'pilots/v4/metadata_check.json', 'brain_experiments_run': False})
    write('pilots/README.md', '''# 기존 자료로 실행할 파일럿

세 파일럿의 입력·비교·결과 해석·중단 조건을 작성했다. 현재 실행한 것은 공개 이벤트와 캡션의 ID·학습/시험 분할 검산이다. 사용자의 BOLD·정서 feature 본체를 분석한 결과는 아직 없다.

| 순서 | 질문 | 먼저 확인할 조건 | 계획 |
|---|---|---|---|
| 1 | 장면 일반화와 세밀한 정서 구별은 함께 좋아지는가 | 같은 정서 대비가 여러 내용군에 있어야 한다. 동일 평가 영상에서 학습 내용군을 바꾼다. | [P4-01](v4/GENERALIZATION_AND_DETAIL.md) |
| 2 | 정서 범주가 바뀌는 부근에서 뇌의 구별이 커지는가 | 범주 점수의 척도가 비교 가능하고 전환 부근 영상이 있어야 한다. | [P4-02](v4/EMOTION_BOUNDARIES.md) |
| 3 | 심상에서 정서 차이는 다른 내용보다 더 남는가 | 최대 71개 영상의 실제 대비와 cue·심상·후속영상의 구간 분리가 필요하다. | [P4-03](v4/MC_IMAGERY.md) |

이 순서는 첫 검정의 실현성 판단이다. 과학적 잠재력의 순위나 원하는 결과의 우선순위가 아니다. 새 뇌 촬영·새 기억 과제·새 인간 평정을 필수 단계로 넣지 않았다.

[실제 입력 조건](v4/INPUTS.md) · [실행한 메타데이터 검산](v4/metadata_check.json) · [연구 질문과 기여](../proposals/README.md)
''')
    write('research_questions/RANKINGS.md', '''# 잠재력과 실행 순서를 구분한 판단

| 방향 | 과학적 잠재력 | 독창성의 남은 조건 | 단기 실현성 | 현재 판단 |
|---|---|---|---|---|
| V4-01 정서 범주와 국소 신경 구별 | 범주 이름과 실제 신경 구조의 관계를 가르는 이론적 기여 | Horikawa 원문·범주지각 직접 선행에서 같은 국소 관찰을 했는지 확인 | 척도의 비교 가능성과 전환 부근 표본이 핵심 | 자료 확인 뒤 파일럿2 |
| V4-02 일반화와 세밀한 정서 구별 | 어떤 정서 차이를 뇌 시스템들이 나누어 보존하는지 설명 | 단순 영역별 decoding·일반 불변성 효과와 다른 관계 예측 필요 | Horikawa 안에서 비교 가능. 내용군·정서 대비의 중첩 확인 필요 | 첫 파일럿 권고 |
| V4-03 지각에서 심상으로의 관계 변화 | 장면 재구성에서 정서와 내용의 상대적 보존을 설명 | 단순 지각→심상 판독과 기존 MC 분석을 넘어야 함 | 최대 71개, 심상 window·후속영상 분리가 큰 조건 | 조건 확인 뒤 파일럿3 |

현재 근거로 수치 점수나 확정적인 신규성 순위를 만들지 않았다. 위 세 후보의 중요한 결과가 나오지 않을 수 있다. 판단 불가능한 결과와 대안 설명이 지지되는 결과는 각 파일럿에서 구분한다.
''')
    write('proposals/AUTHORING_PROTOCOL.md', '# 제안 작성 기준\n\n현재는 [v4 기준](../revision_v4/PROTOCOL.md)을 따른다. 필요성·결정적 관찰·조건부 Conclusion·분야 기여와 기존 관측의 연결을 함께 작성한다. 원안·실제 비판·저자 응답·Coordinator 선정을 구별한다.')
    write('pilots/AUTHORING_PROTOCOL.md', '# 파일럿 작성 기준\n\n[현재 세 계획](README.md)과 [기존 입력 조건](v4/INPUTS.md)을 따른다. 기존 자료에서 답할 수 있는 비교·학습/평가·관측의 뜻·중단 조건을 명시한다. 공개 메타데이터 검산을 실제 fMRI 분석으로 보고하지 않는다.')
    print(json.dumps({'catalog': len(catalog), 'directions': len(directions), 'pilots': len(plans)}))


if __name__ == '__main__':
    main()
