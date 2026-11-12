#!/usr/bin/env python3
"""기존 독립 제안과 Coordinator의 명시적 통합 판정을 재현한다. 새 문헌 검색 없음."""
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'axis_map'
DATE = '2026-11-12'
TYPES = ['Construct / Stimulus', 'Neural', 'Model / Method', 'Structure / Dynamics', 'Inference / Measurement']

def rows(path):
    with path.open(newline='') as f:
        return list(csv.DictReader(f))

def write_csv(path, data):
    with path.open('w', newline='') as f:
        fields = list(dict.fromkeys(k for row in data for k in row))
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for row in data:
            w.writerow({k: json.dumps(v, ensure_ascii=False) if isinstance(v, (list, dict)) else v for k, v in row.items()})

def write_json(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')

def sequence(value):
    return value if isinstance(value, list) else [x.strip() for x in value.split(';') if x.strip()]

def tags(value):
    return [next(t for t in TYPES if t.replace(' ', '') == x.replace(' ', '')) for x in sequence(value)]

sources = json.loads((OUT / 'candidate_subaxes.json').read_text())

def extra(origin, axis_id, name, definition, type_tags, papers, models, question, transfer, feasibility):
    sources.append({'origin_file': origin, 'review_state': '보고서 표에서 Coordinator가 구조화; 원문 보고서 보존', 'record': {
        'axis_id': axis_id, 'name': name, 'definition': definition, 'type_tags': type_tags,
        'representative_papers': papers, 'models': models, 'open_questions': question,
        'transfer_opportunities': transfer, 'dataset_feasibility': feasibility,
        'confidence': 'E3 조건부 제안; 신규성 미확인', 'origin_agent': origin.split('/')[1], 'last_verified': DATE}})

d = 'agents/01_dataset/round1_independent_report.md'
extra(d, 'P-A01', '자극 독립성의 의미적 단위', '자극 ID·파일·내용의 독립성을 구별하여 일반화 모집단을 정의한다.',
      [TYPES[0], TYPES[4], TYPES[3]], ['A01-HORIKAWA2020'], ['perceptual fingerprint', 'group CV'],
      'ID가 다른 자극의 내용 중복을 제거하면 정서 관련 신경정보의 일반화는 유지되는가?',
      '데이터 중복 감사와 의미적 그룹 분할', 'Horikawa 보유 자극의 ID·파일·내용 대응 확인')
extra(d, 'Q-A01', '시간 좌표와 관측지연', '영화 시간의 주석과 clip 평정 구간을 관측 단위로 구별하고 scanner onset·HRF에 정렬한다.',
      [TYPES[1], TYPES[3], TYPES[4]], ['A01-EMOFILM2025'], ['상태공간 관측모형', 'FIR/HRF'],
      '주석 집계와 관측지연을 분리한 뒤에도 신경적 시간 통합의 설명이 필요한가?',
      '시계열 관측모형과 타임베이스 감사', 'Emo-FilM 보유본의 주석·이벤트·BOLD 대응 확인')
extra(d, 'X-A01', '주석 불확실성과 공유 표상', '평정자·타깃·척도 차이를 측정모형으로 분리하여 자료 간 공유 표상 주장의 범위를 정한다.',
      [TYPES[0], TYPES[2], TYPES[4]], ['A01-EMOFILM2025', 'A01-SPACETOP2024'], ['계층 측정모형', 'measurement invariance'],
      '공유 요인의 차이가 신경표상 차이인가 평정자·척도의 차이인가?',
      '측정 불변성과 공통 anchor 기반 비교', '공통 anchor·평정자 자료 확인; 없으면 공동 평정 추가 조건')
d = 'agents/05_multimodal_dynamics/report.md'
extra(d, 'M-X-05a', '공유 통로의 충분성과 고유정보의 필요성', '동일 자극의 공유 성분과 뇌 예측에 추가로 필요한 모달리티 고유 성분을 구별한다.',
      [TYPES[2], TYPES[3], TYPES[4], TYPES[1]], [f'MD05-P{i:02}' for i in range(1,5)], ['ImageBind', 'CAV-MAE', 'FactorCL', 'MBT'],
      '공통 잠재만으로 충분한가, 공유·고유 정보의 결합이 필요한가?',
      '멀티뷰 분해와 정보 교환량 제약', '실제 자극의 영상·음악/환경음 및 신경 정렬 확인')
extra(d, 'D-V-05b', '관찰 가능한 과거와 잠재 예측오류', '입력 가용시간을 제한한 상태와 예측 잔차를 신경 전이에 비교한다.',
      [TYPES[3], TYPES[2], TYPES[4], TYPES[1]], [f'MD05-P{i:02}' for i in range(9,12)], ['VideoMamba', 'V-JEPA2', 'VideoPrism'],
      '장기 문맥 이득은 과거 상태의 필요성인가 미래 입력의 유출인가?',
      '과거 입력 제한과 사건경계 reset', '연속 자극·BOLD·시간주석 확인; 모델별 미래 프레임 접근 검사')
extra(d, 'C-D-05c', '사건 단계와 경과시간의 분리', '사건 진행 좌표를 시계시간·편집 리듬과 경쟁시키는 정렬을 평가한다.',
      [TYPES[0], TYPES[3], TYPES[2], TYPES[4]], ['MD05-P07', 'MD05-P08', 'MD05-P11'], ['AVE', 'TCC', 'VideoPrism'],
      '신경 전이는 사건 단계에 정렬되는가 단순 경과시간에 정렬되는가?',
      '비신경 감독 사건 정렬과 시간왜곡 통제', '독립 사건 주석 및 사건 길이·내용의 다양성 확인')

# 순서: 기존 JSON 30개 + 보고서 내 6개. 각 행은 별개의 판별 질문을 유지한다.
# family, parent axes, 핵심 경쟁 설명, 기각/축소를 요구하는 관측, 주요 대조, 분석 착수 조건
design = [
 ('F04','A F K Q S','환경을 넘는 정서 차원 vs 객체·장면 구성비','내용군 보류에서 효과가 사라지고 신뢰도 보정으로도 회복되지 않으면 보편 차원 주장을 축소한다.','내용군별 분할; 평정 신뢰도; 저수준·의미 기준모형','Horikawa: 실제 주석·내용 ID 대응. Emo-FilM: 영화 단위 외적 평가.'),
 ('F02','A C D H V','이력 의존 신경 상태 vs 현재 자극 설명','입력 정보량·HRF를 맞추면 이력 이득이 사라지는 경우 지속 상태 필요성은 지지되지 않는다.','동일 현재 입력; 문맥 길이 일치; HRF 계열; run 경계','Emo-FilM 연속 자극·BOLD·주석 정렬. Horikawa는 이용 가능한 시간 단위에 맞춤.'),
 ('F03','A E F K X','영역 간 정보 결합 vs 중복·가산 정보','복잡도를 맞춘 가산 모델이 joint 모델과 같으면 결합 계산의 필요성은 약해진다.','ROI 선택 독립성; nonlinear additive; 신뢰도·복잡도 일치','Horikawa 시행별 신경값·주석·ROI. 정보이론적 synergy는 별도 추정 정의 필요.'),
 ('F05','G I L X T','뇌 조건이 제공한 정보 vs 생성 prior가 채운 정보','뇌 조건을 교환하거나 제거해도 평가가 같으면 해당 정서 내용의 신경 근거를 주장하지 않는다.','생성 전 latent; prior-only; 조건 교환; 생성기 교체','Horikawa 자극–신경–주석 정렬. NSD는 시각 대조; 측정 정서 주석은 별도 확인.'),
 ('F01','F G O X Q','공유 latent의 충분성 vs 정렬이 지운 개인 신경정보','잔차가 독립 반복에 재현되지 않거나 조건부 표적을 설명하지 못하면 정보 소실 주장을 축소한다.','정렬 전후 정보; 자극·피험자 보류; 반복 신뢰도','Horikawa/NSD 공유 자극·반복 대응. 정서 검정에는 독립 측정 주석 필요.'),
 ('F07','D G L Q','생성 영상의 세밀한 변화 vs fMRI가 식별한 시간 정보','시간 평활 prior만으로 같은 출력을 설명하면 영상 프레임 속도를 신경 시간 해상도로 해석하지 않는다.','시간 평활 null; HRF; 입력 지연; 생성 prior 제거','Emo-FilM 시간주석·연속 BOLD 우선. Spacetop clip 평정은 연속 정서 궤적을 대신하지 않음.'),
 ('F01','F I J Q X','학습 목표가 보존한 정보 vs 용량·입출력 차이','모델 용량·공간 표현·관측 시간을 맞추면 차이가 없어질 때 목적함수 효과를 기각한다.','공간 지지집합·시간격자 일치; 학습량; readout 복잡도','Horikawa/Emo-FilM/NSD 중 입력 형식이 맞는 보유본; checkpoint 호환은 후속 확인.'),
 ('F08','F H I X Q','자극으로 설명되는 변동 vs 신경 문맥으로 설명되는 변동','두 모델의 고유 잔차가 신뢰 가능한 신경변동과 연결되지 않으면 계산적 상보성을 주장하지 않는다.','동일 test; 공통자극 통제; 잔차 신뢰도; 외부 주석','Emo-FilM 연속 자극·신경자료 우선; Mind Captioning은 신경–자극 쌍과 시간구조 존재 시 조건부.'),
 ('F02','D H N Q V','잠재 상태 통합 vs TR·HRF·재표본화 효과','관측모형을 맞춘 짧은 문맥 모델이 같으면 장기 상태의 신경적 필요성을 축소한다.','원 시간격자; HRF 계열; 자기상관 null; 재표본화 민감도','Emo-FilM 연속 BOLD. beta-map을 임의로 나열해 시계열로 사용하지 않음.'),
 ('F02','B C J V X','전이를 구별하는 예측 상태 vs 현재 장면 복원 정보','장면 동일성 기준모형이 상태 전이 대비까지 설명하면 예측 상태의 추가 필요성은 약해진다.','동일 과거 창; 복원 목표 대조; 상태 전이 보류','Emo-FilM 연속 자극·전이 단위. 신경 실험 없이 상태전이의 인간 인과를 주장하지 않음.'),
 ('F08','I J R F X','해석 특징의 안정성 vs 모델 계산에서의 실제 사용','특징 개입이 held-out 계산을 바꾸지 않거나 seed에 따라 의미가 바뀌면 단일 특징 설명을 축소한다.','seed·기저 변환; feature/subspace 대비; ablation; 오류 노드','Horikawa/NSD 모델 activation·신경 대비. Mind Captioning은 텍스트/표현 연결이 실제 있는 경우 조건부.'),
 ('F04','A C J S X','제거할 환경 변화 vs 보존할 필요 맥락','필요 맥락과 nuisance를 지워도 결과가 같으면 선택적 불변성의 이중 분리가 성립하지 않는다.','짝지은 맥락·환경 변화; 외적 split; 대칭 ablation','Horikawa 내용군·맥락 메타데이터; 없으면 주석 생성·검증 조건. 조작의 뇌효과는 새 측정 필요.'),
 ('F01','F K O X Q','좌표상 동등성 vs 변환이 제거한 신뢰 가능한 정보','기하 정렬이 좋아져도 잔차가 반복되지 않으면 제거된 정서 정보의 존재를 주장하지 않는다.','가역 좌표변환; rank 일치; 잔차 반복; 독립 표적','Horikawa/NSD 반복 또는 독립 평가; 정서 관련성은 실제 주석과 별도 검정.'),
 ('F06','D F K Q T','신경 기하 구조 vs 표본밀도·거리·잡음 산물','거리·밀도·시간창의 합리적 변화에 구조가 붕괴하면 기하의 신경 일반성을 축소한다.','잡음 일치 합성 null; 거리·표본수·임베딩 민감도','Horikawa/Emo-FilM 신뢰도와 충분한 표본; 보유만으로 반복 측정 존재를 가정하지 않음.'),
 ('F04','K M O Q X','의미가 식별된 대응 vs 여러 등가 정렬','동등한 적합의 수송 결합들이 독립 anchor에서 반대 의미를 주면 특정 의미 대응 주장을 보류한다.','여러 초기화·결합; 독립 anchor; 공통 측정모형','다섯 보유 데이터셋 사이 공통 anchor 실제 확인 후. Mind Captioning 이름만으로 공통 ontology를 가정하지 않음.'),
 ('F03','A E F H X','지역 모델 vs 분산 가산 모델 vs 상호작용 모델','평균활성·공통자극·모델복잡도로 이득이 설명되면 네트워크 상호작용 필요성을 축소한다.','ROI 크기·신뢰도; additive; 공통자극; 외적 검정','Horikawa 시행 단위 우선; 동적 네트워크는 연속 신호 확인 후 별도 검정.'),
 ('F02','C D E H Q','gradient 위치의 통합시간 vs HRF·사건 길이','공간·HRF·의미 길이를 통제하면 위치–시간 관계가 없어지는 경우 신경 통합 해석을 축소한다.','공간 null; HRF; 제한 문맥; 의미 사건 길이','Emo-FilM 연속 자료·공간 대응. Spacetop 정서 궤적에는 별도 시간 주석 필요.'),
 ('F07','D E K Q T','정서 네트워크 효과 vs 공간·시간 구조가 만든 유의성','공간 비정상성·자기상관을 보존하는 null에서 효과가 같으면 네트워크 특이 주장을 기각한다.','여러 구조 보존 null; 공통자극; parcellation 민감도','각 보유본의 공간 표현·시간 단위 확인; 데이터 형식에 맞는 null 선택.'),
 ('F05','B C L P T','의미 보존 개입의 표적 효과 vs 편집된 감각·사건 혼입','독립 검증에서 의미 보존이 실패하거나 생성기 교체에 소실되면 선택적 개입 주장을 기각한다.','편집 타당성 평정; 비표적 특징; 생성기 변경; sham edit','Horikawa 원본으로 후보 선정 가능. 편집 자극의 인간 신경효과는 새 주석·뇌 측정 필요.'),
 ('F05','G L Q X','관측이 결정한 특징 vs prior에 따라 달라지는 후보','같은 관측 적합도에서 정서 특징이 prior별로 달라지면 해당 특징은 관측만으로 식별되지 않는다.','관측 적합도 일치; 다중 생성 prior; 독립 encoding 검증','Horikawa 자극–뇌–주석 및 held-out encoding. NSD는 시각 검증; 정서 측정은 별도.'),
 ('F05','L P Q T V','가설을 가르는 정보 이득 vs 불확실한 편집의 극단 선택','무작위·전형성 기준보다 실제 가설 구분이 좋아지지 않으면 설계 이득을 기각한다.','편집·관측·모델 불확실성 분리; 무작위 대조; 외삽 검사','기존 보유본으로 모형 보정·후보 평가. 실제 순차 검증은 새 자극의 신경 측정 필요.'),
 ('F01','C F G I X','언어 압축이 보존한 신경 대비 vs 생략된 비언어 정보','캡션의 정보량·유연성을 늘리면 차이가 사라질 때 언어 고유 한계 주장을 축소한다.','직접 시각·캡션·bottleneck 비교; 길이 일치; readout 용량','Horikawa/NSD 자극–뇌 대응. Mind Captioning은 자극·신경·캡션 대응과 캡션 생성 주체 확인 시 우선 연결.'),
 ('F02','C D I V Q','사건 순서 효과 vs 의미량·시간 거리 효과','내용량·거리·경계를 맞추면 순서 효과가 사라지는 경우 순서 의존 계산 주장을 축소한다.','bag-of-events; 순서 교환; 동일 길이; 거리·경계 통제','Emo-FilM 연속 자극·BOLD. Mind Captioning은 연속 순서·시간 대응이 실제 있을 때만 후보.'),
 ('F04','A C H R X','정서 관련 신경 잔차 vs 누락된 의미·개념','개념 집합을 확장하면 잔차–주석 관계가 사라지는 경우 정서 고유 잔차 주장을 철회한다.','다른 표현 가족; 개념 확장; nested CV; 독립 주석','Horikawa 주석·feature 대응. Mind Captioning에 독립 캡션이 있으면 의미 통제에 사용; AI 캡션은 측정 정서 주석이 아님.'),
 ('F02','C D N V X','예측 오차 vs 상태·예측 내용','상태·내용·양음 오차를 맞춘 경쟁에서 오차의 추가 설명이 없으면 오차 코드 주장을 축소한다.','오차·상태 모델 용량 일치; 과거 제한; HRF; 부호 대비','Emo-FilM 연속 자료 우선. Horikawa에 시간 정보가 없으면 정적 대비로 범위를 제한.'),
 ('F03','E I N R X','경로 선택의 기여 vs 전문가가 담은 내용','gate 교환 효과가 내용·부하 차이로 설명되면 독립 경로 선택 계산을 주장하지 않는다.','gate/expert 교차 ablation; 부하·용량 일치; 재현성','Horikawa 자극별 신경 대비. MoE expert와 뇌영역의 일대일 대응은 가정하지 않음.'),
 ('F06','F I N Q T','생물학적 제약의 관측 가능한 차이 vs 집계 후 등가성','HRF와 공간 집계 후 경쟁 모델이 구별되지 않으면 fMRI로 spike 규칙을 식별한다는 주장을 기각한다.','집계 전후 식별성; 동일 입력·용량; synthetic recovery','보유 fMRI는 집계 표상 비교. spike timing·학습 규칙의 직접 식별에는 추가 측정 필요.'),
 ('F07','A F O Q S T','일반화 가능한 신경 코드 vs 특정 자극·사람의 효과','자극·사람 이중 보류에서 효과가 없으면 그 모집단을 넘는 주장을 축소한다.','자극/참가자 분리 분산; 이중 보류; 신뢰도; 계층 bootstrap','다섯 보유본 각각 실제 반복·참가자·자극 ID를 확인한 뒤 split 구성.'),
 ('F04','A B C P X Q','조건부 추가 정보 vs 조건화가 바꾼 추정 대상','조건화 집합·overlap에 따라 효과가 역전되면 보편적 정서 고유 정보 주장을 보류한다.','total/shared/conditional 구별; fold 내 적합; 측정오차·overlap','Horikawa 실제 주석·시각·의미 특징. 측정되지 않은 원인은 관찰자료만으로 제거할 수 없음.'),
 ('F07','A H K R T','계산 가설의 예측 차이 vs 분석 선택의 자유도','독립 test와 선택 자유도 통제 뒤 모델 순위가 불안정하면 계산 설명 우위를 주장하지 않는다.','layer·ROI·거리·readout nested 선택; 독립 대비; 단순 baseline','모든 보유본에서 해당 분석의 독립 test 확보; 반복 신뢰도와 탐색 이력 기록.'),
 ('F07','B C Q S T','새 내용에 대한 일반화 vs ID만 다른 반복 내용','중복 내용 그룹 분할에서 이득이 사라지면 내용 일반화 주장을 기각한다.','파일 해시+지각 중복; content-group split; provenance','Horikawa 영상·ID·dupidx 우선; NSD 자극 ID; 다른 자료는 사용 단위별 적용.'),
 ('F07','D H Q X','신경 통합 지연 vs 주석 집계·scanner·HRF 정렬','관측 시계 정정만으로 장기 통합 이득이 사라지면 신경 시간상수 주장을 축소한다.','영화시간–scanner onset; 관측 단위; HRF; clip 경계','Emo-FilM 주석과 clip 검증은 같은 영화 시간의 다른 단위; scanner onset은 별도 대응.'),
 ('F04','A O Q S X','자료 간 공유 표상 vs 평정 척도·주체 차이','공통 anchor에서 측정 불변성이 실패하면 직접적인 표상 크기 비교를 보류한다.','평정자·타깃·척도 명시; hierarchical error; 공동 anchor','Emo-FilM/Spacetop 평정 자료 우선. 다섯 보유본 공통 척도 존재는 가정하지 않음.'),
 ('F03','B H J M X','공유 통로의 충분성 vs 모달리티 고유 정보 필요성','강한 가산 모델이 joint 모델과 같으면 상호작용 필요성을 축소한다.','동일 용량 nonlinear additive; 공통원인 null; 합성 양성대조','Emo-FilM 또는 Horikawa 실제 영상·음악/환경음 존재 확인. 음성 특징을 연구 축으로 확장하지 않음.'),
 ('F02','C D J M V','과거 상태의 예측력 vs 미래 프레임·bidirectional 정보','미래 접근을 차단하면 효과가 사라질 때 과거 예측 상태 주장을 철회한다.','원 입력 t에서 절단; bidirectional 경로 검사; reset 대조','Emo-FilM 연속 자료. 모델명만으로 causal 입력을 가정하지 않음; Spacetop 시간 정서 주석은 추가 조건.'),
 ('F02','C D K M V','사건 진행 좌표 vs 경과시간·편집 리듬','position-only 또는 DTW가 같거나, 타깃을 이용한 정렬에만 의존하거나 비신경 감독 정렬의 효과가 보류 사건에 일반화하지 않으면 사건 단계 계산 주장을 축소한다.','정서·신경 타깃 없는 정렬; position-only; DTW; 보류 사건','Emo-FilM 사건 경계·다양성 확인. Mind Captioning은 사건 순서/주석 존재 확인 시에만 연결.'),
]
assert len(sources) == len(design) == 36

families = {
 'F01': ('표상 변환의 정보 보존', '변환·정렬·학습·언어 압축이 무엇을 유지하고 무엇을 제거하는가.'),
 'F02': ('문맥·상태·시간 계산', '현재 내용, 이력, 예측 상태, 사건 좌표와 관측 시간을 어떻게 구별하는가.'),
 'F03': ('분산·경로·멀티모달 결합', '여러 부품의 사용이 중복·가산·상호작용 중 어느 설명을 요구하는가.'),
 'F04': ('정서·의미·측정의 식별', '정서 관련 추가 정보라는 주장이 내용·정렬·평정 조건에 얼마나 의존하는가.'),
 'F05': ('생성·역문제·실험 설계', '생성물의 특징을 관측 정보와 prior로 나누고 유효한 자극 개입을 설계하는가.'),
 'F06': ('관측 가능한 기하와 생물학적 제약', '계산 차이가 측정 척도·집계를 통과하여 실제 구별 가능한가.'),
 'F07': ('일반화·시간·검정의 기준', '신경 주장에 필요한 독립 표본·관측 단위·검정 기준을 명시하는가.'),
 'F08': ('모델 설명과 계산적 사용', '표현의 대응, 정보의 상보성, 모델에서의 필요성을 구분하는가.'),
}
papers = rows(ROOT / 'literature/papers.csv')
aliases = {alias.strip(): r for r in papers for alias in r['origin_ids'].split(';')}
pending_extra = {r['paper_id']: r for r in rows(ROOT / 'agents/12_adversarial_review/pending_papers.csv')}
doc_refs = {
 'DOC-SAE': ('OpenAI sparse_autoencoder 공식 코드', 'https://github.com/openai/sparse_autoencoder'),
 'DOC-TRANSCODER': ('transcoder_circuits 공식 코드', 'https://github.com/jacobdunefsky/transcoder_circuits'),
 'DOC-CIRCUIT': ('circuit-tracer 공식 코드', 'https://github.com/safety-research/circuit-tracer'),
 'DOC-DOMAINBED': ('DomainBed 공식 코드', 'https://github.com/facebookresearch/DomainBed'),
}
catalog = {}

def resolve(ref):
    if ref in doc_refs:
        title, url = doc_refs[ref]
        catalog[ref] = {'reference_id': ref, 'title': title, 'official_url': url,
                        'status': '공식 코드·문서 확인; 논문 서지 확정 수 제외', 'source_aliases': ref,
                        'source_scope': 'agents/06_frontier_ai/report.md §공식 도구; 본문 확인과 구분'}
        return ref
    if ref in aliases:
        p = aliases[ref]; key = p['canonical_id']
        catalog[key] = {'reference_id': key, 'title': p['title'], 'official_url': p['official_url'],
                        'status': p['verification_gate'], 'source_aliases': p['origin_ids'],
                        'source_scope': f"본문: {p['full_text_access']}; Discussion: {p['discussion_access']}; 근거: {p['evidence_level']}"}
        return key
    if ref in pending_extra:
        p = pending_extra[ref]; key = 'PENDING-' + ref
        catalog[key] = {'reference_id': key, 'title': p['title'], 'official_url': p['official_url'],
                        'status': '보류: 완전 서지 미확인; 고유103편 집계 밖의 보조 코드 출처',
                        'source_aliases': ref, 'source_scope': p['source_verified']}
        return key
    raise ValueError(f'해결되지 않은 출처: {ref}')

registry = []
for i, (source, spec) in enumerate(zip(sources, design), 1):
    r = dict(source['record'])
    original_id = r['axis_id']
    refs = sequence(r['representative_papers'])
    if i == 11: refs = ['DOC-SAE', 'DOC-TRANSCODER', 'DOC-CIRCUIT']
    if i == 12: refs = ['FAI08', 'FAI09', 'DOC-DOMAINBED']
    canonical = list(dict.fromkeys(resolve(x) for x in refs))
    family, parents, contrast, falsify, controls, feasible = spec
    r.update(axis_id=f'AS{i:02}', source_axis_id=original_id, source_file=source['origin_file'],
             type_tags=tags(r['type_tags']), representative_papers=canonical,
             models=sequence(r['models']), open_questions=sequence(r['open_questions']),
             transfer_opportunities=sequence(r['transfer_opportunities']),
             source_confidence=r['confidence'], source_dataset_feasibility=r['dataset_feasibility'],
             confidence='E3 통합 제안; 문헌·코드 근거 범위는 출처별 표시; 신규성·실험 결과 미확정',
             dataset_feasibility=feasible, family_id=family, parent_axes=parents.split(),
             competing_explanations=contrast, falsification_test=falsify, critical_controls=controls,
             review_date=DATE, last_verified=source['record']['last_verified'])
    r['source_definition'] = source['record']['definition']
    r['deduplication_group'] = 'DG05' if i in (5,13) else f'DG{i:02}'
    r['role'] = ('측정·평가 조건' if i in (6,18,28,30,31,32,33) else
                 '개입·실험 설계' if i in (19,21) else '경쟁 계산·표상 가설')
    r['verified_bibliography_refs'] = [k for k in canonical if k.startswith('P') and '보류' not in catalog[k]['status']]
    r['pending_bibliography_refs'] = [k for k in canonical if '보류' in catalog[k]['status']]
    r['supporting_document_refs'] = [k for k in canonical if k.startswith('DOC-')]
    if i == 2: r['models'] = [m.replace('인과적 접근제한', '미래 입력 차단') for m in r['models']]
    if i == 13: r['open_questions'] = ['공통 기하 밖의 신경정보는 잡음인가 독립 재현 가능한 정서 관련 정보인가?']
    if i == 14: r['open_questions'] = ['내재차원·연결 구조가 측정 척도와 표본밀도를 넘어 재현되는가?']
    if i == 15:
        r['name'] = '잠재요인·공간 대응의 비유일성'
        r['definition'] = 'shared/private 요인·수송 결합의 여러 해가 독립 표적에서 동일한 의미를 갖는지 검증한다. PID의 결합정보 질문은 AS03·AS34와 별도 연결한다.'
        r['open_questions'] = ['서로 동등한 shared/private 분해·수송 결합이 독립 표적에서도 동일한 의미를 갖는가?']
        r['transfer_opportunities'] = ['잠재요인 식별과 수송 결합 불확실성; PID는 별도 결합정보 경로로 연결']
    if i == 25: r['open_questions'] = ['예측 내용·상태를 조건화한 뒤 부호별 예측오차의 추가 신경 설명이 남는가?']
    if i == 26: r['open_questions'] = ['전문가 내용과 용량을 맞춰도 입력 의존 경로 선택이 독립 신경 대비를 설명하는가?']
    if i == 27: r['open_questions'] = ['생물학적 계산 제약의 차이가 fMRI 집계 후에도 경쟁 모델과 구별되는가?']
    if i in (8,11,22,23,24,36):
        r['dataset_feasibility'] += ' Mind Captioning의 텍스트 출처를 구분하며, 같은 신경반응으로 생성한 캡션을 독립 입력으로 되넣지 않음.'
    r['reference_caveats'] = [f"{key}: {catalog[key]['status']}" for key in canonical if '보류' in catalog[key]['status'] or key.startswith('DOC-')]
    registry.append(r)

write_json(OUT / 'source_proposals.json', sources)
write_json(OUT / 'integrated_subaxes.json', registry)
write_csv(OUT / 'integrated_subaxes.csv', registry)
write_csv(OUT / 'reference_catalog.csv', sorted(catalog.values(), key=lambda x:x['reference_id']))
write_csv(OUT / 'source_crosswalk.csv', [{k:r[k] for k in ['axis_id','source_axis_id','source_file','origin_agent','family_id']} for r in registry])
write_csv(OUT / 'families.csv', [{'family_id':k,'name':v[0],'definition':v[1], 'subaxes':[r['axis_id'] for r in registry if r['family_id']==k]} for k,v in families.items()])

parent_types = {
 'A':[0,4], 'B':[0,2], 'C':[0,3], 'D':[0,3,4], 'E':[1], 'F':[1,3],
 'G':[2,4], 'H':[2,1], 'I':[2], 'J':[2], 'K':[3,4], 'L':[2,4],
 'M':[2,3], 'N':[2,1], 'O':[1,4], 'P':[4,2], 'Q':[4], 'R':[2,3,4],
 'S':[4], 'T':[4], 'U':[0,3], 'V':[2,3], 'W':[0,3], 'X':[3,4],
}
taxonomy = []
for row in rows(OUT/'seed_taxonomy.csv'):
    key = row['axis_id']; children = [r['axis_id'] for r in registry if key in r['parent_axes']]
    taxonomy.append(dict(axis_id=key, name=row['name'], type_tags=[TYPES[i] for i in parent_types[key]],
                         active_subaxes=children, status='하위축 연결' if children else 'seed 보존; 이번 통합의 근거 공백',
                         boundary='보유 데이터 이름만으로 기억·심상 조건을 추정하지 않음' if key=='U' else
                         '독립적인 가치·salience 조작과 경쟁 설명이 없어 정서 평정으로 대신 채우지 않음' if key=='W' else
                         '유형은 다중 태그이며 단일 계층으로 제한하지 않음'))
write_csv(OUT/'taxonomy.csv', taxonomy)

lines = ['# Axis Encyclopedia v1', '', f'통합일: {DATE}. **A–X 24개 상위축, 36개 출처 추적 가능한 하위축, 8개 탐색 묶음**이다. 12개 역할의 원본 제안을 모두 수록했다. 서로 다른 판별 질문을 유지하고, 겹치는 방법은 묶음·교차연결로 관리한다.', '',
         '36개는 원본 제안 등록 수이며 고유 RQ 수가 아니다. AS05·AS13은 공통 중복군 DG05로 묶고 피험자 정렬과 일반 변환이라는 세부 비교를 보존했다. 이후 동일 조작·표적·반증이면 하나의 RQ로 집계한다.', '',
         '사용자는 Horikawa, Emo-FilM, Mind Captioning, NSD, Spacetop 보유를 확인했다. 데이터 상세 검증은 Axis 진행을 막지 않는다. 이 문서는 연구 가설 지도이며 분석 결과·신규성 확정·최종 제안이 아니다. 기존 문헌 근거를 통합했으며 이번 단계에서 새 원문을 확인하거나 신경 분석을 실행하지 않았다.', '',
         '`last_verified`는 원 제안의 기록일이고 `review_date`는 이번 통합 검토일이다. 스키마·실험 검증 날짜를 뜻하지 않는다. 하위축 가설은 E3이며 인용 문헌의 서지·본문·코드 확인 범위는 각각 다르다.', '',
         '## 탐색 묶음', '', '| 묶음 | 판별하는 질문 | 하위축 |', '|---|---|---|']
for fid,(name,definition) in families.items():
    children = ', '.join(f"[{r['axis_id']}](#{r['axis_id'].lower()})" for r in registry if r['family_id']==fid)
    lines.append(f'| {fid} {name} | {definition} | {children} |')
lines += ['', '## A–X 연결과 공백', '', '| 상위축 | 유형 | 연결 하위축 | 상태 |', '|---|---|---|---|']
for t in taxonomy:
    lines.append(f"| {t['axis_id']} {t['name']} | {'; '.join(t['type_tags'])} | {', '.join(t['active_subaxes']) or '없음'} | {t['status']} |")
lines += ['', '**U와 W는 미션의 seed로 보존하고 미확인 공백으로 표시한다.** Mind Captioning이라는 이름만으로 심상·기억 실험을 가정하지 않는다. 정서 관련 평정을 곧바로 계산적 가치·salience의 측정으로 치환하지 않는다. 새 최상위 Y/Z 축은 이번 36개 제안의 질문을 기존 다중 태그로 수용할 수 있어 신설하지 않았다.', '',
          '## 하위축 상세', '', '모든 항목의 관측 판정은 충분한 신뢰도·검정력을 전제로 한다. 비유의성만으로 정보 부재를 단정하지 않는다. 관찰적 추가 설명, 모델 내부 개입, 인간 신경 인과는 다른 주장이다.', '']
for r in registry:
    lines += [f"<a id=\"{r['axis_id'].lower()}\"></a>", f"### {r['axis_id']}. {r['name']}", '',
              f"{r['definition']}", '',
              f"- **연결:** {' × '.join(r['parent_axes'])}; {r['family_id']}. 유형: {'; '.join(r['type_tags'])}.",
              f"- **질문:** {' / '.join(r['open_questions'])}",
              f"- **경쟁 설명:** {r['competing_explanations']}",
              f"- **기각·축소 관측:** {r['falsification_test']}",
              f"- **필수 대조:** {r['critical_controls']}",
              f"- **모델·방법:** {'; '.join(r['models'])}",
              f"- **전이 기회:** {'; '.join(r['transfer_opportunities'])}",
              f"- **보유 데이터 경로·분석 조건:** {r['dataset_feasibility']}",
              '- **근거:** ' + '; '.join(f"[{key} {catalog[key]['title']}]({catalog[key]['official_url']})" for key in r['representative_papers']),
              f"- **추적:** [{r['origin_agent']} / {r['source_axis_id']}](../{r['source_file']}); 원 제안 {r['last_verified']}, 통합 {r['review_date']}. 가설 E3; 역할: {r['role']}; 중복군: {r['deduplication_group']}."]
    if r['reference_caveats']: lines.append('- **근거 한계:** ' + '; '.join(r['reference_caveats']))
    lines += ['']
lines += ['## 다음 단계', '', '이 지도에서 경쟁 설명을 실제로 교환·수정하는 Round2–5를 수행하고, 문헌 연결 및 실제 무작위 조합을 거쳐 RQ 후보를 만든다. 세부 데이터·모델 검증은 후보의 분석 조건을 확인할 때 진행한다. Axis 통합 검토를 미실행 토론 라운드로 계산하지 않는다.', '',
          '기계 판독본: [통합 하위축](integrated_subaxes.json), [전체 출처 목록](reference_catalog.csv), [원본 대응표](source_crosswalk.csv), [상위축](taxonomy.csv), [교차연결](cross_connections.csv), [검토 판정](integration_review.md).', '']
(OUT/'AXIS_ENCYCLOPEDIA.md').write_text('\n'.join(lines))

required = ['axis_id','name','definition','type_tags','representative_papers','models','open_questions','transfer_opportunities','dataset_feasibility','confidence','origin_agent','last_verified']
assert len({r['axis_id'] for r in registry}) == 36
assert len({r['origin_agent'] for r in registry}) == 12
assert all(all(r.get(k) for k in required) for r in registry)
assert all(set(r['type_tags']) <= set(TYPES) for r in registry)
assert all(set(r['parent_axes']) <= set(parent_types) for r in registry)
assert all((ROOT/r['source_file']).is_file() for r in registry)
validation = {'date':DATE, 'source_proposals':len(sources), 'integrated_subaxes':len(registry),
              'origin_roles':12, 'parent_axes':len(taxonomy), 'active_parent_axes':sum(bool(t['active_subaxes']) for t in taxonomy),
              'families':len(families), 'unique_references_used':len(catalog),
              'verified_bibliography_references_used':sum(k.startswith('P') and '보류' not in v['status'] for k,v in catalog.items()),
              'pending_references_used':[k for k,v in catalog.items() if '보류' in v['status']],
              'document_only_references':[k for k in catalog if k.startswith('DOC-')],
              'checks':'필수12필드·고유ID·12역할·모든 원본 경로·문헌ID 대응·유형·상위축 참조 통과',
              'not_verified':['실제 데이터 스키마','모델 실행','신규성 역검색','Round2–5','최종 RQ 수량 목표']}
write_json(OUT/'validation.json', validation)
print(json.dumps(validation, ensure_ascii=False))
