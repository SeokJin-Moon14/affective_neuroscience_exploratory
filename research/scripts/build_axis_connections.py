#!/usr/bin/env python3
"""실제 교차 검토에서 채택한 수동 문헌 연결. 무작위 조합 생성기가 아니다."""
import csv
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
out = root/'axis_map'
registry = {r['axis_id']:r for r in json.loads((out/'integrated_subaxes.json').read_text())}
types = ['Construct / Stimulus','Neural','Model / Method','Structure / Dynamics','Inference / Measurement']
# 이름 / 연결 / 경쟁 설명 / 판별 관측 / 데이터 경로 / 원 제안
design = [
 ('공통 정렬의 성공과 정서 관련 정보 손실의 공존', 'AS05 AS13 AS07 AS22 AS34 AS31',
  '공통 잠재가 충분함 / 정렬·압축이 신뢰 가능한 정보를 제거함 / 차원·용량·잡음 효과',
  'rank·readout·평가 예산을 맞춘 뒤 정렬 성능은 늘고 독립 정서 대비는 줄어드는지 평가한다. 신뢰도·내용 통제로 감소가 소실되면 선택적 손실 설명을 축소한다.',
  'Horikawa 주석–자극–뇌 대응 우선; NSD는 시각 정렬 대조; Mind Captioning은 실제 텍스트–자극–신경 대응과 출처가 있을 때 언어 병목 가지.',
  'Agent07 C1; Agent10 V1; Coordinator 중복군 DG05'),
 ('사건 단계의 기하와 시계시간·HRF의 구별', 'AS14 AS36 AS35 AS02 AS32 AS17',
  '독립 사건 단계에 신경 전이가 정렬됨 / 경과시간·편집·HRF / 학습 정렬의 강제 일치',
  '정서·BOLD 없이 학습한 사건 정렬을 보류 영화에 적용한다. position-only·DTW·같은 과거 창·HRF null이 같으면 사건 단계의 추가 설명을 기각한다.',
  'Emo-FilM 영화시간 주석·scanner onset·연속 BOLD; Spacetop은 확인된 clip 평정 단위만; Mind Captioning의 시간 구조는 확인 시 별도 가지.',
  'Agent07 C2; Agent10 V2/V3'),
 ('좁은 공유 통로와 정보원 결합의 필요성', 'AS34 AS03 AS16 AS15',
  '독립 기여의 합으로 충분함 / 고유 경로·비가산 결합 필요 / 공통원인·용량·잡음 평균화',
  '동일 복잡도의 nonlinear additive 대 joint, 공유-only 대 공유+고유, 정보원 가림을 비교한다. 가산 null에서 이득이 재현되면 결합 필요성을 축소한다. PID는 별도 표적·정의·추정 가정을 요구한다.',
  'Horikawa ROI 결합과 Emo-FilM 영상·음악/환경음 결합을 별도 분석; Spacetop은 유효 clip 평정과 결측 조건을 명시.',
  'Agent07 C3; Agent12 결합정보 감사'),
 ('거리구조 정렬이 정서 의미를 운반하는 조건', 'AS15 AS33 AS01 AS29 AS28',
  '공통 정서 관계구조 / 시각·의미 대응만 유지 / 대칭에 따른 비유일성 / 측정 척도 차이',
  '근접 최적 수송 결합들을 정렬에 쓰지 않은 anchor로 평가한다. 동등 비용의 결합이 반대 정서 대응을 만들거나 측정 불변성이 실패하면 공통 정서 코드 해석을 보류한다.',
  'Horikawa–Emo-FilM–Spacetop은 관측 단위를 따로 모델링. NSD는 시각 참조. Mind Captioning은 스키마 확인 뒤 독립 의미 노드. 공통 anchor가 없으면 추가 평정 조건.',
  'Agent07 C4; Agent10 MC-4'),
 ('개별 잠재축과 안정적인 신경 부분공간의 구별', 'AS15 AS11 AS24 AS29 AS08',
  '단일 정서 축 / 좌표는 비유일하나 부분공간 정보는 안정 / 감독·누락 의미·공통자극의 산물',
  'seed·dictionary 크기·표현 가족·개념 집합을 바꾸어 축과 부분공간을 따로 평가한다. 개념 추가로 효과가 사라지면 정서 고유성을 주장하지 않는다. 모델 feature 개입은 뇌 개입과 구별한다.',
  'Horikawa 내용 보류; Mind Captioning의 텍스트 출처·독립 신경 타깃이 있을 때 개념 확장; NSD는 시각·의미 대조.',
  'Agent07 C5; Agent10 V4; Agent12 식별성 감사'),
 ('복원 특징의 관측 정보와 생성 prior 기여', 'AS04 AS20 AS05 AS21 AS22',
  '뇌 관측이 특징을 제한함 / prior가 관측 등가 후보를 선택 / 정렬이 잃은 정보를 prior가 보충',
  '생성 전 latent·prior-only·뇌 조건 교환·다중 prior를 독립 참조에 평가한다. 신경 적합도가 같은 후보 사이 특징이 달라지면 단일 출력의 식별 주장을 축소한다. 조건 교환의 OOD도 통제한다.',
  'NSD의 시각 관측 대조와 Horikawa의 측정 정서 대비를 구별. Mind Captioning이 실제 신경 조건 생성 태스크라면 텍스트 출력의 별도 평가. 새 편집 자극의 뇌효과는 새 측정 필요.',
  'Agent07 C6; Agent10 V5'),
 ('언어 의미 누락과 신경 신호의 순환 재사용', 'AS22 AS24 AS08 AS31 AS30',
  '독립 자극 설명이 신경 대비를 보존 / 개념이 빠져 잔차 발생 / 신경 조건 텍스트가 타깃을 되돌려 전달',
  '인간 설명·자극 기반 AI 설명·신경 조건 출력의 출처를 나눈다. 같은 Y로 만든 캡션을 독립 encoding 입력으로 사용하지 않는다. 개념 확장과 독립 반복/외부 참조 평가로 순환 없이 남는 대비를 확인한다.',
  'Mind Captioning의 실제 출처·대응이 확인될 때 우선 경로; Horikawa와 NSD는 자극 기반 설명 대조. 독립 정서 주석 없으면 의미 결과까지만 해석.',
  'Agent10 MC-1/MC-2·V4; Coordinator 연결'),
 ('뇌영감 계산 차이의 fMRI 관측 가능성', 'AS25 AS26 AS27 AS09 AS30',
  '오차·경로·생물학적 제약이 구별 가능한 계산을 구현 / 모델 용량 차이 / HRF·공간 집계 후 관측 등가',
  '동일 입력·용량에서 오차/상태, gate/expert, 계산 제약을 별도 요인으로 비교하고 합성 관측 회복을 검사한다. 집계 후 차이가 없으면 해당 측정의 식별 한계로 보고한다. 생물학적 기전 자체를 반박했다고 해석하지 않는다.',
  'Horikawa 자극 단위와 Emo-FilM 연속 자료에 맞는 관측모형; NSD 시각 대조 가능. spike timing·학습규칙의 직접 판별은 추가 측정 조건.',
  'Agent11 원 제안; Agent12 경로·구현 감사; Coordinator 연결'),
]
connections=[]
for i,(name,ids,alternatives,test,data,origin) in enumerate(design,1):
    members=ids.split()
    refs=list(dict.fromkeys(ref for sid in members for ref in registry[sid]['representative_papers']))
    used=[t for t in types if any(t in registry[sid]['type_tags'] for sid in members)]
    assert len(used)>=3
    connections.append(dict(connection_id=f'CC{i:02}',name=name,subaxes=members,type_tags=used,
                            competing_explanations=alternatives,discriminating_observation=test,
                            dataset_path=data,reference_ids=refs,origin=origin,
                            evidence='E3 수동 문헌 기반 연결; 무작위 추출 아님; 신경 결과·신규성 미확정'))
with (out/'cross_connections.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(connections[0]));w.writeheader()
    for row in connections:
        w.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,list) else v for k,v in row.items()})
lines=['# 핵심 교차연결 8개','',
       '2026-11-12 실제 Axis 검토를 바탕으로 Coordinator가 선택한 수동 문헌 연결이다. 실제 무작위 조합 30개와 구별하며 그 목표에 포함하지 않는다. 최종 고유 RQ로 확정한 목록도 아니다. 충분한 신뢰도·검정력에서 경쟁 예측을 평가한다.','',
       '유형은 현상·자극, 신경, 모델·방법, 구조·동역학, 추론·측정이다. 유형 수 자체를 과학적 우선순위로 사용하지 않는다.','']
for c in connections:
    lines += [f"## {c['connection_id']}. {c['name']}",'',
              '- **연결:** '+', '.join(f"[{sid}](AXIS_ENCYCLOPEDIA.md#{sid.lower()})" for sid in c['subaxes']),
              '- **유형:** '+'; '.join(c['type_tags']),
              '- **경쟁 설명:** '+c['competing_explanations'],
              '- **판별 관측:** '+c['discriminating_observation'],
              '- **보유 데이터 경로:** '+c['dataset_path'],
              '- **출처 추적:** '+c['origin']+'. 인용별 원문·문서 범위는 연결된 하위축과 [출처 목록](reference_catalog.csv)에 기록.','']
lines += ['## 다음 토론의 출발점','',
          '정보 보존(CC01/05/07), 현재 내용 대 과거 상태(CC02), 영역·모달리티 결합(CC03)을 먼저 서로 다른 경쟁 설명으로 토론할 수 있다. 이는 과학적 비교를 위한 잠정 작업 순서이며 최종 제안 순위나 데이터 실현성 승인으로 간주하지 않는다.','']
(out/'cross_connections.md').write_text('\n'.join(lines))
v=json.loads((out/'validation.json').read_text())
v['manual_cross_connections']=len(connections)
v['connection_checks']='모든 하위축 ID 참조, 연결별 3개 이상 유형, 근거 ID 연결 확인'
(out/'validation.json').write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'manual_connections':len(connections),'random_combinations_executed':0},ensure_ascii=False))
