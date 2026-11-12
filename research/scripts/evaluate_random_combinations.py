#!/usr/bin/env python3
"""Coordinator의 조합별 과학 판정. 난수 결과를 바꾸거나 재추첨하지 않는다."""
import csv,json
from pathlib import Path
root=Path(__file__).resolve().parents[1]; out=root/'combinations'
draw=json.loads((out/'random_draws.json').read_text())
axes={r['axis_id']:r for r in json.loads((root/'axis_map/integrated_subaxes.json').read_text())}
# 구성개념 / 계산원리 / 신경대상 / 대비 / 반증 / baseline / 자료·조건 / 연결하위축 / 판정 / 이유
design=[
('내용 밖으로 일반화하는 정서 전이','도메인 밖 잠재동역학','시간별 분산 신경표상','영화 내부·외부에서 같은 전이모형의 정서 대비 설명력','외부 영화에서 현재내용 기준을 넘지 못하면 공유 전이법칙을 축소','현재 프레임+HRF; 동일 문맥 길이','Emo-FilM 연속자료·외부 consensus; 독립 영화 split','AS02 AS10 AS28','발전','시간상태와 일반화 단위를 결합한 판별 가능 질문'),
('예측에 쓰이는 잠재 특징','희소 분해와 예측상태의 기능적 사용','예측상태와 대응되는 신경 부분공간','seed가 다른 개별 feature와 부분공간의 상태전이 예측 보존','feature 편집이 모델 계산을 바꾸지 않으면 해당 feature의 기능 주장 약화','무작위 방향·rank 일치·동일 readout','Horikawa 또는 Emo-FilM; 모델 activation 접근·독립 정서 대비','AS10 AS11 AS15','수정 필요','모델 내 기능 검정을 인간 신경 필요조건으로 확대하지 않도록 범위를 제한'),
('사건 순서에 따른 경로 선택','MoE gate와 내용의 교차 개입','맥락별 정서 관련 뇌 대비','같은 사건집합의 순서를 바꾸고 gate 교환 대 expert 교환 비교','gate 효과가 expert 내용이나 계산량으로 모두 설명되면 독립 routing 필요성 약화','고정 gate·부하 일치·bag of events','Emo-FilM 관찰비교; 실제 순서개입의 뇌효과는 새 측정','AS23 AS26 AS29','수정 필요','관찰자료에서는 조건부 계산 비교만 유지'),
('계산적 salience의 희소 특징','SAE로 salience 축 발견','독립 salience 대비에 반응하는 신경표상','정서 관련 특징과 독립 salience 조작의 일반화 분리','정서 평정만 설명하고 독립 salience 조작을 설명하지 못하면 salience 가설 기각','감각 대비·예측오차·정서 주석 별도모형','다섯 보유자료에서 독립 salience 조작·측정 존재 미확인','AS11 AS24','보류','W축을 정서 점수나 주의라는 이름으로 대체하지 않음; 필수 측정 근거 공백'),
('외부 영상과 내부 재현의 시간 구조','지각–심상 전이모형','지각과 내부 재현의 신경 궤적','같은 내용의 외부지각·내부재현에서 전이 좌표 보존','행동·시간 일치 뒤 교차조건 일반화가 없으면 공통 동역학 축소','내용·시간·지시 차이 통제','Mind Captioning 포함 보유자료의 실제 심상·기억 조건 미확인','AS02 AS14','보류','U 조건을 데이터 이름이나 긴 문맥에서 추정하지 않음'),
('멀티모달 맥락 변화의 추가 정보','공유/고유 분해와 반사실','정서 관련 비가산 신경 대비','영상·비음성음향의 의미 일치 대 불일치에서 joint 이득','같은 의미량의 nonlinear additive가 충분하면 상호작용 필요성 약화','영상만·음향만·가산·공통원인 null','Emo-FilM 실제 제시 스트림; 진짜 불일치 자극 뇌효과는 새 측정','AS34 AS19 AS29','수정 필요','기존자료 재조합의 계산 결과와 실제 재조합 자극의 뇌결과를 구별'),
('보상가치의 정서 encoding','가치 회귀와 외적 검증','가치와 관계된 신경반응','독립 보상가치가 정서 평정을 넘어 신경반응을 설명하는지','가치 변수 없이는 이 대비를 구성할 수 없음','정서·감각·의미 baseline','보유자료에 확인된 가치 조작·보상변수 없음','AS29 AS30','기각','현재 조합을 정서 회귀로 치환하면 W가 사라지므로 별도 가치자료 없이 성립하지 않음'),
('정서 차원과 salience 차원의 분리','측정 불변성과 잠재요인 경쟁','독립 구성개념에 대응되는 분산표상','공통 척도에서 정서와 salience가 분리되는지','독립 측정 없이 두 latent에 이름만 붙이면 식별되지 않음','한 요인·두 요인·측정오차 모형','독립 salience 측정은 현재 미확인','AS01 AS33','보류','고각성 주석을 salience ground truth로 대신하지 않음'),
('공유 공간 밖 모달리티 정보','공유/고유 통로','지역·분산 신경정보','공유-only 대 공유+고유; joint 대 복잡도 일치 가산','고유 성분 이득이 용량·저수준 정보로 소실되면 필요성 축소','단일모달·비선형 가산·공통원인 null','Emo-FilM 실제 영상·음악/환경음 및 정서주석 대응','AS34 AS03','발전','입력원 분해와 뇌표상 비교를 연결; 정확한 PID 주장은 별도'),
('개인별 내부 재현의 공통 기하','정렬과 내부재현 교차일반화','개인별 기억·심상 표상','지각 정렬을 내부재현에 적용했을 때 독립 의미·정서 대비 보존','조건부 신뢰도를 넘는 교차조건 정보가 없으면 공유 기하 축소','비정렬·가역변환·독립 신뢰도','실제 내부재현 태스크·측정은 보유명만으로 확인되지 않음','AS05 AS13','보류','U 측정이 확인될 때 열리는 미래 경로로 남김'),
('맥락의 예측오차와 관측 지연','predictive coding의 관측모형','부호별 오차와 신경변동','상태·내용·HRF를 맞춘 뒤 양음 오차 추가설명 비교','관측모형이나 상태만으로 설명되면 오차 코드 필요성 축소','현재내용·상태·signed/unsigned error·HRF','Emo-FilM 연속 자극·BOLD·주석 정렬','AS25 AS09 AS32','발전','오차와 BOLD 지연의 대안설명을 분리'),
('네트워크 전이의 인과 방향','동적 연결성에서 방향 추론','정서 관련 네트워크 switching','관찰적 BOLD 선후관계만으로 영역 간 원인방향 결정','서로 다른 HRF·공통입력이 같은 선후관계를 만들면 식별 불가','HRF 계열·공통입력 null','관찰 fMRI만으로 개입 방향성 확인 불가','AS17 AS18 AS29','기각','현재 조합의 인과방향 주장은 관찰 등가를 깨지 못함; 기술적 선후관계로 낮추면 별도 질문'),
('지역·분산 코드의 복원 충분성','영역 제한 decoding 경쟁','ROI와 분산표상','ROI-only·분산가산·분산joint에서 독립 정서 대비 보존','ROI 크기·신뢰도·용량 통제 뒤 차이가 사라지면 분산 계산 필요성 축소','일치 voxel수·비선형 가산·prior-only','Horikawa 시행 단위; NSD는 시각 대조','AS16 AS03 AS04','발전','단순 위치분류보다 정보원 충분성을 검정'),
('의미 확장에 따른 정서 기하 잔차','개념 집합 확장과 기하 경쟁','신경 거리·조건부 잔차','객체→관계→사건 특징을 추가할 때 신뢰 가능한 정서 대비 변화','개념 추가로 효과가 사라지면 정서 독립성을 주장하지 않음','여러 의미모형·용량 일치·noise ceiling','Horikawa 주석·자극; Mind Captioning은 독립 설명 출처 확인','AS24 AS14 AS22','발전','개념 누락과 새로운 신경정보의 구별'),
('디코딩되는 영역의 신경적 필요성','decoder 성능으로 causal localization','ROI별 정서정보','어떤 ROI에서 잘 복원된다는 사실로 그 ROI의 필요성을 판정','중복 코드·공통입력만으로도 decoding 가능','ROI ablation은 모델 내부 제거로만 해석','기존 관찰자료에는 실제 영역 개입 없음','AS16 AS04','기각','decodability를 인간 신경 필요조건으로 바꾸는 논리 도약'),
('시간 특징의 기능적 사용','시간 SAE와 모델 feature intervention','정서 관련 시간창 신경정보','feature의 시간적 안정성·모델 필요성·신경 대응을 따로 평가','안정된 신경 대응이 있으나 모델 개입 효과가 없으면 단일 mechanism 해석 축소','임의 방향·동일 과거 창·오류 노드','Emo-FilM; 모델 activation과 시간 정렬 필요','AS11 AS02 AS30','수정 필요','세 증거를 하나의 인과 점수로 합산하지 않음'),
('모달리티별 정서 통합시간','공유/고유 상태공간','시간별 분산표상','영상과 비음성음향의 과거 창을 독립 변화해 추가 정서정보 곡선 비교','신뢰도·HRF 일치 후 창 차이가 사라지면 통합시간 차이 축소','단일모달·동일 창·FIR·future mask','Emo-FilM 연속자료·실제 스트림 동기화','AS34 AS35 AS09','발전','고유 경로 필요성과 시간 통합을 교차 비교'),
('생성된 사건 의미의 정보 출처','brain-to-text와 다중 prior','신경 조건이 제한하는 의미 대비','뇌 조건 교환·prior 교체에도 외부 참조의 사건 의미가 보존되는지','자연스러움만 유지되고 독립 내용 일치가 늘지 않으면 신경 정보 주장 축소','prior-only·교환조건 OOD·직접latent','Mind Captioning이 실제 신경 조건 생성이면 적용; Horikawa 원자극 설명으로 대조','AS04 AS20 AS22','발전','출력의 유창함과 관측이 제한한 내용을 구별'),
('개인 정렬에서 축과 부분공간의 안정성','basis non-identifiability','개인·공유 신경표상','사람·seed별로 개별 축은 바뀌어도 정서 부분공간의 외적 예측은 유지되는지','독립 자극·개인에서 부분공간도 재현되지 않으면 안정 코드 축소','가역 회전·rank 일치·개인별 신뢰도','Horikawa/NSD 공유 자극; NSD는 정서 ground truth 별도','AS05 AS13 AS11','발전','축 해석과 예측정보 불변성을 분리'),
('재귀 상태의 의미 기하','재귀 계산과 사건 좌표','맥락별 신경 기하','같은 유효 과거 범위의 재귀·비재귀모델이 사건 대비를 다르게 설명하는지','유효깊이·문맥량 일치 후 차이 없으면 재귀 구현 필요성 축소','feedforward unroll·같은 input horizon·HRF','Emo-FilM 연속자료; 내부 상태 관측은 모델 수준','AS25 AS14 AS36','수정 필요','재귀 구조 이름 자체를 신경 계산 증거로 쓰지 않음'),
('개인 encoding의 설명 가능한 차이','공유 readout와 개인 residual','개인별 반복 가능한 신경 차이','공유모형에 개인 residual을 더할 때 독립 정서 대비가 유지되는지','개인차가 신뢰도·처리공간·자극 빈도로 소실되면 개인 코드 축소','공유/개인 용량 일치·두 수준 보류','Horikawa 반복·공유 자극; 각 보유 처리본의 신뢰도 조건','AS08 AS05 AS30','발전','개인차를 정렬 실패와 분리'),
('희소 특징 편집의 선택성','생성 편집과 mechanistic probe','선택적 정서 관련 신경 대비의 예측','같은 feature 개입을 다른 생성기로 옮겨 비표적 의미 보존을 평가','생성기별로 의미가 달라지면 공통 선택적 개입 주장 축소','sham edit·비표적 특징·외부 평정','기존자료로 후보 검증; 실제 편집 뇌효과는 새 주석·측정','AS19 AS11 AS21','수정 필요','모델 내부 편집과 실제 자극 개입의 두 검증 단계 분리'),
('개인 공통 정서 전이법칙','subject alignment와 state dynamics','개인별 신경 상태 전이','정적 표상 정렬이 전이법칙도 정렬하는지 별도 검정','정적 정렬은 좋아도 전이 일반화가 없으면 공통 동역학 충분성 기각','정적현재·개인별상태·HRF·공통자극','Emo-FilM 공통 자극·개인 시계열; 외부 consensus는 개인 정답 아님','AS02 AS05 AS10','발전','정적 대응과 계산 법칙의 공유를 구별'),
('네트워크 기하의 원인 구조','기하와 인과 그래프','네트워크 간 거리·경로','낮은 geodesic 거리를 직접 신경정보 흐름 원인으로 해석','공간·공통입력 null이 같은 기하를 만들면 인과구조 식별 불가','공간구조 보존 null','관찰자료에 직접 경로 개입 근거 없음','AS14 AS18','기각','기하학적 이웃과 신경적 인과 경로를 혼동하는 조합'),
('신경 궤적 차원의 관측척도 안정성','multiscale geometry','정서 관련 신경 궤적','표본수·시간창·잡음을 바꿀 때 차원·연결과 정서 대비가 유지되는지','같은 관측왜곡을 준 null에서 재현되면 신경 특이 구조 주장 축소','noise matched null·거리계열·독립 자극','Emo-FilM/시간자료 있는 Horikawa; 반복·시간주석 조건','AS14 AS09 AS18','발전','새 그림이 아닌 관측척도에 대한 반증 질문'),
('정서 상태 발견의 독립 검증','label-free latent state discovery','독립 정서 대비를 예측하는 상태','정서 라벨 없이 학습한 상태가 보류 자극의 주석 관련 신경변동을 설명하는지','현재 내용·사건 경계만으로 같으면 정서 상태 필요성 축소','현재프레임·사건segmentation·상태수 일치','Emo-FilM 연속자료; 상태수 선택은 training 내부','AS10 AS01 AS30','발전','사후 이름 붙이기를 피하고 발견과 검증을 분리'),
('정서 예측오차의 시간 비대칭','signed predictive coding','정서 주석과 관련된 부호별 오차 신경반응','내용·상태·오차크기를 맞춘 양음오차의 시간 반응 차이','HRF·크기·주석불확실성 조정 후 동일하면 부호 비대칭 축소','unsigned error·matched magnitude·FIR','Emo-FilM 연속주석·신경 정렬; AI 예측오차는 측정 주석과 별개','AS25 AS32 AS33','수정 필요','오차 부호의 구성법·모델 교체 안정성 명시 필요'),
('감각계층의 예측상태 충분성','prediction vs reconstruction','sensory–transmodal 위치별 신경표상','동일 과거·용량에서 복원과 예측 목표의 정서 대비 설명 차이','HRF·사건길이·공간null 조정 후 차이 없으면 계층별 목적 분화 축소','matched objectives·동일readout·공간null','Emo-FilM 및 호환 보유 신경공간; Horikawa는 가능한 시간단위','AS07 AS10 AS17','수정 필요','서로 다른 공개모델 비교만으로 학습목표 원인을 식별하지 않도록 설계 강화'),
('신경 관측과 양립하는 정서 자극 집합','inverse problem uncertainty','관측이 제한하는 정서 특징','같은 신경 적합도 후보들의 정서 주석 관련 특징이 prior별로 변하는지','동등 적합 후보가 반대 특징을 가지면 단일 정서 복원 주장을 축소','prior 교체·held-out encoding·후보폭 보정','Horikawa 원자극·주석·신경; 새 후보의 실제 정서는 외부 검증 조건','AS20 AS04 AS21','발전','관측등가의 정의·모형오차를 사전에 명시'),
('최신 모델의 정서 예측 순위','모델 family benchmark','분산 신경표상','같은 타깃에서 여러 최신 모델의 최고 정확도 순위 비교','순위만으로 어떤 신경 계산 가정도 구별하지 못함','동일 readout·튜닝 예산','보유자료에서 기술 benchmark는 가능','AS07 AS30','기각','현재 형태는 단순 모델 교체. 목표/정보접근/구조를 조작하는 다른 발전 후보로 흡수')]
assert len(design)==30
records=[]
for raw,spec in zip(draw['accepted'],design):
    construct,principle,target,contrast,falsify,baseline,data,sids,decision,reason=spec
    support=sids.split();refs=list(dict.fromkeys(p for sid in support for p in axes[sid]['representative_papers']))
    records.append(dict(**raw,scientific_construct=construct,external_field_concept=principle,
      ai_model_or_method=list(dict.fromkeys(m for sid in support for m in axes[sid]['models'])),neural_target=target,
      available_dataset=data,measurable_contrast=contrast,falsifiable_prediction=falsify,baseline=baseline,
      source_papers=refs,missing_assumptions=data,novelty_risk='E3 연결; 기존 질문과 의미 중복 여부를 최종 RQ 대응표에서 병합; 세계 최초 미확정',
      decision=decision,rejection_reason=reason if decision in ['기각','보류'] else '',review_reason=reason,
      supporting_subaxes=support,evidence_boundary='인용은 계산 원리·주변 근거이며 이 새 조합의 실증 결과가 아님; U/W 직접 근거는 미확인'))
(out/'random_evaluated.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
with (out/'random_evaluated.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(records[0]));w.writeheader()
    for r in records:w.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,list) else v for k,v in r.items()})
from collections import Counter
print(json.dumps({'reviewed':len(records),'decisions':Counter(r['decision'] for r in records)},ensure_ascii=False))
