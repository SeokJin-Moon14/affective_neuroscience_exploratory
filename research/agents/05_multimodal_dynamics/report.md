# Agent05 독립 탐색: 멀티모달 표현과 시간적 계산

작성·검증일: 2026-11-12. 담당: Agent05 Multimodal Dynamics. 상태: Round 1 독립조사 완료, 신경 데이터 실현성·신규성 최종검증은 보류. source: `papers.csv`, `evidence_manifest.csv`. confidence: 공식 서지·읽은 문서와 코드 높음, 신경전이 가설 낮음~중간. needs_followup: 원문 추가확인·실제 데이터 metadata·체크포인트·반례검색. origin_agent: Agent05.

이 조사의 핵심은 **공유표상으로 압축하면서 버린 정보와 시간순서를 처리하면서 만들어낸 정보가 정서 관련 뇌표상에 각각 필요한가**이다. 최신 영상모델의 encoding 점수 순위를 연구목표로 삼지 않는다. 공유정보·고유정보·상호작용 정보의 필요성, 사건 단계와 경과시간의 차이, 과거 입력만으로 성립하는 예측과 미래입력에 의존하는 정렬을 경쟁 설명으로 놓는다.

## 1. 독립성과 증거 범위

- 프로젝트 `AGENTS.md`·`RESEARCH_MISSION.md`를 읽고 자기 폴더 안에서만 작성했다. EmoBrain과 다른 Agent 결과는 읽거나 수정하지 않았다. 연구범위 제외 주제를 새 축으로 도입하지 않았다. Speech Features는 분석대상이 아니며 오디오에서는 환경음·음악의 표현 원리를 다룬다.
- **11편의 제목·저자·연도·공식 출처를 직접 확인했다.** MERT와 VideoMamba는 읽은 공식 README가 제공하는 preprint 판으로 기록했다. 기억에 근거해 정식학회 서지를 보충하지 않았다.
- **VideoPrism 1편**의 출판사 공식 PDF를 받아 방법 §2.3, ablation §3.5, Limitations §3.6(p8), Conclusion §5(p9) 등을 직접 읽었다. 전체 27쪽을 모두 정독했다는 뜻은 아니다. 다른 10편은 공식 README·모델카드·구현의 E1 범위이다. 이들에게 논문 본문 또는 Discussion을 읽었다고 표시하지 않는다.
- arXiv·OpenReview·공식 github.io 페이지는 실제 HTTP tunnel 403을 확인했다. 허용된 공식 GitHub/raw 출처를 사용했다. 원문 접근 실패와 대체 경로를 retrieval JSON에 남겼다. PDF는 출판사 `mlresearch/v235`의 공식 링크를 통해 확보했다.
- `papers.csv`는 미션의 실제 30필수 필드에 `confidence`, `needs_followup`을 추가한 32필드이다. `evidence_manifest.csv`는 URL·현지 사본·SHA256·검증일을 연결한다. 공식문서의 성능은 저자 보고이며 독립 재현이 아니다. 모델·체크포인트·신경분석을 실행하지 않았다.

증거 표기: **검증됨/E1**은 읽은 문서·코드·해당 본문에 한정한다. **문헌 기반 추론/E3**은 문헌들을 연결한 해석이다. **새 가설/E3**은 앞으로 검증할 주장이다. **미확인/E0**은 사실로 사용하지 않는다.

## 2. AI 분야의 원래 계산 문제에서 출발한 11편

전체 저자·연도·식별자·브랜치 SHA는 `papers.csv`에 보존했다.

| ID | 논문/모델과 원래 계산 원리 | 실제 확인한 범위 | 신경전이에 필요한 구별 |
|---|---|---|---|
| MD05-P01 | [ImageBind](https://github.com/facebookresearch/ImageBind): 이미지와 짝지은 여러 모달리티를 공통 좌표에 정렬 | README·모델카드·모델 구현; huge 출력1024차원, 기본 영상2프레임 | 공통 좌표를 가진다는 사실과 모달리티 고유정보가 필요 없다는 주장을 구별 |
| MD05-P02 | [CAV-MAE](https://github.com/YuanGongND/cav-mae/tree/master): cross-modal correspondence와 각 입력 복원을 결합 | 공동/개별 latent, 모달리티별 masking, MSE+NCE 코드 | 대응성에 유리한 정보와 복원에 유리한 정보 중 무엇이 신경목표에 필요한가 |
| MD05-P03 | [FactorCL](https://github.com/pliang279/FactorCL): 다중 view의 공유·고유 task-relevant 정보를 함께 보존 | 공식 방법설명, NCE-CLUB critic, 합성자료 생성기 | shared/private 분해와 신경적 synergy는 동일하지 않음 |
| MD05-P04 | [MBT](https://github.com/google-research/scenic/tree/main/scenic/projects/mbt): 좁은 latent 통로를 통해 모달리티 정보를 교환 | fusion_layer, bottleneck, 공유 encoder 설정과 갱신 코드 | 통합의 시작 시점·용량·모델크기 효과 분리 |
| MD05-P05 | [MERT](https://github.com/yizhilll/MERT): 음악을 위한 acoustic teacher와 musical teacher 결합 | RVQ-VAE/K-means·CQT, CQT MSE 구현,95M/330M 문서 | 텍스트에 정렬되지 않은 음악정보가 정서 관련 신경변동을 설명하는가 |
| MD05-P06 | [CLAP](https://github.com/LAION-AI/CLAP): 오디오-텍스트 정렬과 길이 대응 feature fusion | 공식 API·대조 손실;48kHz 입력 예제 | 언어와 공유하는 소리정보와 음악/환경음의 고유정보 분리 |
| MD05-P07 | [AVE](https://github.com/YapengTian/AVE-ECCV18): 시청각 사건의 시간적 위치 추정 | audio-guided attention,10구간,양방향 LSTM | 사건 동시출현·의미적 일치·뇌 사건경계를 구별 |
| MD05-P08 | [TCC](https://github.com/google-research/google-research/tree/master/tcc): 다른 속도의 시퀀스에서 왕복 대응 학습 | soft nearest-neighbor 왕복정렬·공식 위치암기 경고 | 사건 진행 단계와 단순 경과시간을 구별 |
| MD05-P09 | [VideoMamba](https://github.com/OpenGVLab/VideoMamba): 국소 중복과 전역 의존성의 효율적 처리 | 상태공간 기반 구현, 기본 bimamba=True | 계산적으로 긴 문맥을 보는 것과 신경적인 미래 예측을 구별 |
| MD05-P10 | [V-JEPA 2](https://github.com/facebookresearch/vjepa2): masked latent 예측과 별도 행동조건 계획 | encoder/predictor 설명·마스크/위치 token 구현 | 마스킹 복원, 과거→미래 예측, 로봇 행동조건화를 분리 |
| MD05-P11 | [VideoPrism](https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhao24f/zhao24f.pdf): 언어로 얻은 전역 의미와 영상의 동작정보를 함께 보존 | 정식 ICML2024 원문§2.3·§3.5·§3.6·§5+공식코드 | appearance/motion의 균형이 좋아져도 정서 신경통합 설명이 된 것은 아님 |

### 재현성에 영향을 주는 실제 발견

1. CAV-MAE의 `main` README는 코드가 아직 공개되지 않았다는 오래된 안내이다. `master`에는 실제 구현과 모델이 있다. 코드 부재로 오판하지 않도록 두 사본을 남겼다. `Scale++`는 README가 원논문 외 후속이라고 명시하므로 원논문 결과와 분리했다.
2. ImageBind README의 CC-BY-NC 표기와 모델카드·실제 LICENSE의 CC-BY-NC-SA4.0 표기가 다르다. 사용 시 실제 LICENSE를 재검토해야 한다.
3. VideoMamba 기본 `bimamba=True`, AVE의 `bidirectional=True`를 직접 확인했다. 이 모델의 좋은 시간 예측력을 관찰자의 미래 예측 메커니즘으로 해석하면 미래 자극 접근이 혼입된다.
4. TCC README는 LSTM/positional embedding이 프레임 위치를 세는 trivial solution에 도달할 수 있다고 명시한다. 이는 저자의 **공식 코드문서 경고**이지 논문 Discussion에서 가져온 인용은 아니다.
5. V-JEPA2 README에는 2025 원논문과 2026 V-JEPA2.1이 함께 있다. 2.1의 dense predictive loss·deep supervision 및 arXiv2603.14482 서지는 README에서 확인했지만 본 11편에는 별도 집계하지 않았다. 2.1 부분의 Paper 링크가 TODO로 남은 점도 후속 확인 대상이다.
6. VideoPrism 공개 base/large checkpoint는 원논문 base/giant와 구별한다. 원문은16프레임 짧은 클립을 명시하며 공개 README는 2025 공개 및2026 갱신을 포함한다. 공개판 성능을2024 논문 수치와 동일시하지 않는다.

## 3. 직접 읽은 저자 한계와 Agent의 전이 추론

**VideoPrism 저자 직접 서술 — §3.6 Limitations, p8.** 잡음 텍스트는 불완전하고 편향될 수 있다. 현재는 짧은 영상에서16프레임을 표본화하므로 장기영상 이해가 어렵다. 인코더를 장기영상 이해 시스템의 구성요소로 쓰는 것을 future work로 제시한다. 고정 backbone 평가를 지향하지만 일부 상황에서는 전체 fine-tuning 또는 효율적 adaptation이 유리할 수 있다고 인정한다. 원문 `evidence/videoprism_paper.pdf`, 텍스트 변환본529–543행과568행 부근에 해당한다. 2단 편집으로 추출 텍스트의 문단 순서가 섞여 있어 페이지·절을 기준으로 읽었다.

**본문 방법과 결과 — §2.3,p3–4; §3.5 Figure4,p8.** 두 번째 단계에서 token-wise 예측만 하면 첫 단계의 외형 지식이 손실될 수 있어 global distillation을 추가한다. token shuffling은 보이는 token을 decoder가 그대로 복사하는 shortcut을 방지하려는 장치이다. ablation은 motion-rich SSv2와 appearance-driven K400의 개선 양상이 다름을 보인다.

**Agent의 새 연결/E3.** 전역 의미를 보존하는 학습과 국소 변화에 민감한 학습이 정서 관련 신경정보를 다르게 남길 수 있다. 장기 문맥 모듈을 붙이는 것 자체보다, 동일한 관찰 과거를 주고 사건경계에서 상태를 초기화했을 때 추가 신경설명력이 어떻게 바뀌는지 비교하는 편이 판별적이다. 이는 저자가 제안한 뇌-정서 연구가 아니다.

나머지10편에서는 저자의 논문 Discussion 미래과제를 추출하지 않았다. 아래 모든 미해결 문제·기회·질문은 읽은 방법에 근거한 Agent의 E3이다.

## 4. 미해결 문제 5개

| 문제 | 문헌 근거 | 경쟁 설명과 필요한 검정 |
|---|---|---|
| U1. 공통 공간이 정서 관련 뇌정보에 충분한가? | P01 ImageBind+P03 FactorCL | 공통 요인이 충분함 vs 압축에서 버린 음악/시각 고유정보도 필요함. 공유+고유 모델의 held-out 추가 기여가 저수준·의미 통제 후 남는지 검정 |
| U2. 모달리티 융합 이득은 상호작용 정보인가? | P02 CAV-MAE+P04 MBT | 진짜 비가산적 의존 vs 독립적 감각 정보 두 개를 합친 효과. nonlinear additive 모델과 joint 모델을 용량·샘플 수에 맞춰 비교 |
| U3. 정서 관련 신경전이는 사건 단계에 묶이는가, 경과시간에 묶이는가? | P07 AVE+P08 TCC | 사건 단계 표상 vs 시간·편집리듬·HRF가 만든 정렬. position-only·DTW·시각 cut·음향 onset baseline과 분리 |
| U4. 장기문맥 이득은 관찰 과거의 지속상태인가, 미래영상 접근의 효과인가? | P09 VideoMamba+P10 V-JEPA2+P11 VideoPrism | 과거 누적 상태 vs 양방향 접근/넓은 창의 더 많은 정보. 입력 horizon을 고정하고 미래차단·reset·순서교란 비교 |
| U5. 음악의 신경적 관련 정보는 언어공통 공간 밖에 남는가? | P05 MERT+P06 CLAP+P03 FactorCL | 텍스트 의미로 충분함 vs 음악 특이 구조가 추가로 필요함. 음량·스펙트럼·음악 유무·시각의미 통제와 독립 정서주석 필요 |

## 5. 모델·방법 기회 5개

1. **O1: 두 목표의 제거 효과를 대조한다.** CAV-MAE의 contrastive-only·MAE-only·결합을 비교하고 FactorCL의 공유/고유 합성자료로 무엇이 소실되는지 먼저 보정한다. 목표에 따라 빠진 신경정보의 종류가 다르면 단순 모델 우열 이상의 관찰이다. 근거 P02+P03, E3.
2. **O2: 통합 통로의 충분성 곡선을 만든다.** MBT의 융합 시작층·bottleneck 용량을 조절하되 parameter-matched late fusion와 감각특징은 고정한다. 좁은 통로가 전체 감각정보에는 부족하지만 정서 관련 잔여에는 충분한지 비교한다. 근거 P01+P04, E3. token 수를 신경정보의 bit 수로 해석하지 않는다.
3. **O3: 관찰 과거를 제한한 시간모델을 비교한다.** VideoMamba/V-JEPA2/VideoPrism에서 t 이후 프레임을 feature 추출 단계부터 차단한다. 같은 과거 창의 mean pooling·causal convolution·상태모델을 비교하고 창 크기와 HRF 모형을 별도로 튜닝한다. 근거 P09+P10+P11, E3.
4. **O4: 사건 경계 후보를 독립적으로 정의한다.** 오디오 onset, 시각 cut, AVE의 교차모달 사건 변화, TCC의 단계 진행을 다른 회귀항으로 둔다. 정서 주석으로 경계를 고르고 같은 주석에 다시 적합하는 순환을 피한다. 근거 P07+P08, E3.
5. **O5: 모델 불일치를 목적변수 대신 실험 선택자로 쓴다.** MERT·CLAP·ImageBind가 서로 다르게 판단하는 음악/환경음 구간을 train 데이터에서 정의하고, 독립 자극에서 신경반응·실측 주석의 관계를 확인한다. 근거 P01+P05+P06, E3. AI 점수는 독립 정서 정답이 아니다.

## 6. 다른 분야에서의 전이 5개

| 전이 | 원래 문제 → 새 계산 능력 → 신경과학 질문 | 관찰·반증·주요 한계 |
|---|---|---|
| T1 | FactorCL의 다중 view 정보손실 → 공유/고유 보존 → 정서 관련 신경정보가 공통 좌표로 충분한가? | 고유정보의 추가 기여가 자극·피험자 분리 후 없으면 해당 해상도에서 필요성 가설 약화. 정보 부재 자체를 증명하지는 않음. P01+P03 |
| T2 | MBT의 계산량·교환량 제약 → 통로 용량 조절 → 정서 관련 표현은 감각보다 낮은 차원의 교환에 충분한가? | 감각/정서 관련 목표 모두 같은 용량곡선이면 정서 선택적 압축 설명 약화. 모델 구조를 뇌 구조로 직접 동일시하지 않음. P02+P04 |
| T3 | TCC의 속도 변화 대응 → 의미적 단계 정렬 → 신경 정서전이는 물리시간보다 사건진행에 안정적인가? | 위치-only나 DTW와 동일하면 새 계산 원리 필요성 약화. 실제 속도 조작 fMRI가 없으면 자연자료의 관찰적 비교에 한정. P07+P08 |
| T4 | 영상 사전학습의 shortcut 제거·지식보존 → 의미와 동작의 분리된 손실 → 정서 관련 전이는 움직임 변화인가, 의미 상태의 변경인가? | 전역 의미·모션 통제 후 추가 정보가 없으면 정서 특이 전이 설명 축소. teacher 차이를 단일요인 조작처럼 취급 불가. P10+P11 |
| T5 | 음악 self-supervision과 audio-text retrieval → 서로 다른 불변성 비교 → 언어화되지 않는 음악정보의 신경적 기여가 있는가? | 음량·스펙트럼·시각 의미·장르/음악유무 통제로 사라지면 음악 고유 계산 주장 약화. 음악 주석과 신경 정서주석의 의미를 섞지 않음. P05+P06 |

## 7. 예상 밖의 연결 3개

1. **시간 정렬의 shortcut과 신경적 정서 궤적.** TCC는 같은 위치에 돌아오는 손실만으로 의미가 생기지 않는다고 경고한다. VideoPrism 역시 token 복사 shortcut을 막는 장치를 쓴다. 따라서 신경 궤적을 정렬한 아름다운 그림보다 먼저 **시간·위치만으로도 같은 효과가 나오는지** 물어야 한다. 새 가설은 사건 단계 정렬이 위치-only null을 넘을 때만 검토한다(P08+P11,E3).
2. **지식보존과 감각 통합의 선택성.** VideoPrism의 global distillation은 새 학습 중 전역 정보를 잊지 않게 한다. CAV-MAE의 복원은 대응성 외의 입력정보를 남기는 방향이다. 이 두 목적이 뇌와 대응하는 잔여를 다르게 보존한다면, 높은 정렬 점수가 정보를 많이 보유해서인지 특정 정보를 선택해서인지 구별할 수 있다(P02+P11,E3).
3. **압축 통로와 모달리티 고유정보의 공존.** 좁은 MBT 통로가 융합을 돕는다고 해서 모든 정보가 공유공간으로 가야 하는 것은 아니다. FactorCL은 고유정보 보존을 목표로 한다. **교환에는 좁은 공통 정보만 필요하지만 정서 관련 뇌표상에는 교환되지 않은 정보도 필요하다**는 설명을 공통 공간 충분성 가설과 비교할 수 있다(P03+P04,E3).

## 8. 숨겨진 가정 3개와 시험법

| 가정 | 문헌과의 정확한 관계 | 과거의 제약/최근 도구 | 반증 방법 |
|---|---|---|---|
| H1. modality-invariant 공간이 필요한 정보를 모두 보존한다 | ImageBind는 공통 검색공간을 제공한다. 이것이 뇌정보에 충분하다는 것은 원논문 주장이 아니라 응용자가 덧붙이기 쉬운 가정 | 서로 다른 모달리티 인코더·FactorCL·CAV-MAE 개별 경로를 공개 구현에서 대조 가능 | 조건부 고유표현의 held-out 기여가 반복되면 충분성 반박. 학습·feature선택은 fold 내부 |
| H2. 큰 문맥창·상태공간 모델은 관찰자의 예측을 더 잘 나타낸다 | VideoMamba/AVE의 실제 양방향 구현이 이 해석을 보증하지 않는다. V-JEPA masking도 방향성을 자동 보증하지 않음 | 공개 dense latent와 창 크기 조절·미래차단을 시행할 수 있음 | 동일 과거 조건에서는 이득이 사라지고 미래프레임 허용 시만 커지면 관찰자 예측 설명 기각 |
| H3. joint 모델이 unimodal 모델보다 좋으면 synergy다 | MBT·CAV-MAE의 융합 성능을 신경정보량 분해로 읽는 데 생기는 가정; 저자가 정확한 neural PID를 입증했다는 뜻 아님 | 공유/고유 합성자료·additive nonlinear baseline·반복 샘플링 | 독립 정보의 합으로 joint gain이 재현되면 synergy 증거 아님. nonlinear additive와의 차이도 선택한 모델계열 내 비가산성만 뜻함 |

## 9. 신규 Sub-axis 3개

각 항목의 origin_agent=Agent05, last_verified=2026-11-12. 새로운 최상위 축을 임의로 늘리지 않고 기존 축을 판별력 있게 세분화한다.

| axis_id/name | definition/type_tags | representative_papers/models | open_questions/transfer_opportunities | dataset_feasibility/confidence |
|---|---|---|---|---|
| M-X-05a 공유 통로의 충분성과 고유정보의 필요성 | 동일 자극의 정보 중 통합에 필요한 공유 성분과 뇌 예측에 추가로 필요한 고유 성분을 구별; Model/Method,Structure/Dynamics,Inference/Measurement,Neural | P01–P04;ImageBind,CAV-MAE,FactorCL,MBT | 공통 공간 충분성 vs 공유+고유 필요성; 분해와 교환량 제약 결합 | 영상·음악/환경음 자극과 신경 정렬 필요. 실제 modalities 미확인. 원리 높음/신경전이 낮음~중간 |
| D-V-05b 관찰 가능한 과거와 잠재 예측오류 | 입력 가용시간을 명시한 상태·예측 잔차와 뇌 전이를 비교; Structure/Dynamics,Model/Method,Inference/Measurement,Neural | P09–P11;VideoMamba,V-JEPA2,VideoPrism | 장기문맥 필요성 vs 미래입력 leakage; boundary reset의 영향 | 연속 자극·BOLD·시간주석 필요. HRF 해상도 이하 주장 금지. 원리 높음/실현성 미확인 |
| C-D-05c 사건 단계와 경과시간의 분리 | 사건진행 좌표와 시계시간·편집리듬을 경쟁시키는 정렬; Construct/Stimulus,Structure/Dynamics,Model/Method,Inference/Measurement | P07–P08+P11;AVE,TCC,VideoPrism | 정서 관련 전이의 위치 불변성 vs 위치암기; 비신경 감독으로 정렬 학습 | 독립 사건주석과 충분한 사건 다양성 필요; 기존 자료의 시간 annotation 미확인. 원리 중간/신경전이 낮음 |

## 10. 후보 질문의 3단계 재구성과 강한 반론

### RQ05-1: 공통 표상 밖의 정보는 정서 관련 신경정보에 필요한가?

1차 모델 적용: ImageBind/CAV-MAE/FactorCL 표현으로 신경신호를 예측한다.

2차 과학 질문: 감각·의미의 공유 성분을 조건화한 뒤 모달리티 고유 성분이 **독립 정서주석과 관계되는 신경변동**을 추가 설명하는가?

3차 가정 도전: 공통 잠재가 충분하다는 설명과 공유·고유 성분의 공존 설명을 구별한다. 부정 결과는 해당 자극·측정 신뢰도에서 고유정보 필요성의 상한을 제한한다.

가장 강한 반론: 고유 성분은 단지 model capacity·저수준 소리·의미 누락이며, supervised factorization은 타깃을 미리 주입할 수 있다. 수정: 외부 데이터/비정서 목적의 표현을 우선 사용하고, fold 내부 정규화·분해·회귀, 같거나 더 강한 nonlinear additive baseline, 자극·피험자 전이, reliability ceiling을 포함한다. 검증 전에는 성립한 신규성으로 보고하지 않는다.

### RQ05-2: 정서 관련 신경전이의 문맥 의존성은 사건경계에서 재설정되는가?

1차 모델 적용: 긴 문맥의 video latent와 예측 잔차로 BOLD를 예측한다.

2차 과학 질문: 동일한 과거 입력 범위에서 감각·의미 변화 이상의 정서 관련 신경정보가 사건경계를 넘어 유지되는 상태에 의존하는가?

3차 가정 도전: 모든 시점의 정서를 독립적인 자극 속성으로 근사하는 설명과 지속상태가 필요한 설명을 비교한다. 경계 reset과 길이 일치 무작위 reset이 같다면 사건 특이 재설정 가설이 약화된다.

가장 강한 반론: HRF·시간 자기상관·미래프레임 때문에 긴 문맥 이득이 생긴다. 수정: 원본 시각/음향 입력을 t에서 절단하고, run 경계를 넘는 convolution을 막으며 HRF 지연·창 길이를 train fold에서 추정한다. 비연속 시간점 무작위 split을 쓰지 않는다. 정서 시간주석이 없다면 “정서 궤적” 주장을 보류한다.

### RQ05-3: 정서 관련 전이는 사건의 시계시간인가, 진행 단계인가?

1차 모델 적용: TCC로 사건 시퀀스를 정렬하고 신경전이를 비교한다.

2차 과학 질문: 서로 다른 자극의 속도·길이가 달라도 독립적으로 정의된 사건 단계에서 정서 관련 신경전이가 안정적인가?

3차 가정 도전: 물리적 시간상수와 사건 단계 중심 전이를 구별한다. position-only나 DTW로 동일하게 설명되면 TCC 필요성을 기각하고 단순 baseline을 유지한다.

가장 강한 반론: 정렬 자체가 원래 다른 궤적을 강제로 같게 만든다. 수정: 신경자료/정서주석 없이 정렬을 학습하고 보류 자극에서 검정한다. 정렬 전후 신호보존·시간왜곡량을 함께 평가한다. 속도 조작 신경실험이 없으면 속도 불변성의 인과 주장을 하지 않는다.

## 11. 과학적 보호 장치와 실현성 경계

**Synergy 용어.** joint 모델이 가장 좋은 단일모달 모델을 넘는다는 사실은 두 독립정보를 더한 효과로도 생긴다. `y=f(A)+g(V)` 합성 null, 공유 공통원인 null, XOR형 상호작용 합성 양성대조를 사용해 분석을 보정한다. 동일 복잡도의 nonlinear additive와 joint 모델 차이는 해당 함수계열 내 상호작용 증거이다. 정확한 정보이론적 synergy는 별도 추정 대상·PID 정의·가정 없이는 주장하지 않는다. FactorCL을 완전한 PID 분해로 부르지 않는다.

**정서 관련성.** 자극 feature, 모델 score, 실제 정서주석, BOLD를 별개의 관측변수로 둔다. 신경신호 전체의 예측성 개선만으로 정서 계산을 주장하지 않는다. 사전에 정한 정서주석 관련 contrast 또는 독립 평가가 필요하다. 정서 관련 신경잔여를 ROI 선정과 동일 데이터에서 이중 사용하지 않는다.

**시간과 통계.** HRF·자기상관·자극 반복·run 경계·미래 token을 함께 점검한다. 시간 셔플은 자기상관을 파괴하므로 가능하면 사건/블록 단위, circular shift 등 구조 보존 null을 비교한다. 주석 빈도와 BOLD 해상도가 허용하는 시간범위 안에서만 주장한다. 자극/film·run·subject를 독립 단위로 분할하고 bootstrap·통계도 계층을 반영한다. 여러 창·층·ROI 선택은 내부 validation과 다중비교 통제가 필요하다.

**데이터.** Horikawa→Emo-FilM→Spacetop→NSD 우선순위는 후속 실현성 단계에 유지한다. 본 조사는 공개 AI 자료에서 먼저 질문을 만들었으며 네 데이터셋의 자극 오디오 유무·원본 접근·시간주석을 직접 확인하지 않았다. 정적 이미지 자극만 있는 자료는 시청각 통합과 연속 사건전이를 직접 검증할 수 없으며, 실제 metadata 감사 후 정적 대조군 활용 가능성만 판단한다. 특정 데이터셋에 없는 주석을 있다고 가정하지 않는다.

**인과와 해석.** 관찰 fMRI의 모델 대응은 구현 알고리즘 동일성이나 인과 증거가 아니다. 오디오 교체·시간압축 같은 model-only 조작은 모델의 예측 비교에 한정된다. 그 자극을 실제 참가자에게 제시한 신경측정 없이 뇌의 조작 효과를 주장하지 않는다.

## 12. 미션의 8가지 탐색 질문에 대한 답

1. **왜 아직 시도되지 않았는가?** 공유/고유 요인을 분해하는 표현, 조절 가능한 통합 구조, dense video latent의 공개가 서로 다른 분야에 흩어져 있었다는 E3 설명이 가능하다. 다만 선행연구 부재를 아직 입증하지 않았다. 신경문헌의 역방향 신규성 검색이 다음 단계이다.
2. **최근에야 가능해진 것은?** FactorCL·CAV-MAE의 분해/손실 대조와 MERT·CLAP의 다른 불변성, VideoPrism 공개 encoder·V-JEPA2 latent predictor의 실제 코드가 비교를 구체화한다. 2026 V-JEPA2.1도 README에서 발견했지만 본 결과에 미검증 기능을 추가하지 않는다.
3. **틀렸을 수 있는 가정은?** 공통 공간 충분성, 긴 문맥=관찰자 예측, joint gain=synergy의 세 가정이다. 모두 원저자의 신경과학 주장을 허구로 귀속하지 않고 응용 단계의 가정으로 표시했다.
4. **AI가 기존 뇌모델보다 잘 포착할 후보는?** 복합 시청각 관계, 음악 구조, 위치 변화에도 대응되는 사건 단계, 장기 영상 문맥이다. “더 잘 포착한다”는 신경실험 결과는 아직 없다. 실제 추가 설명력은 대조군을 통해 평가해야 한다.
5. **뇌가 가지지만 AI가 놓칠 후보는?** 분포 밖 시청각 불일치와 모달리티 고유정보, 과제·개인별 시간통합 차이이다. 이는 신경표상으로 확인된 사실이 아니라 잔여를 찾을 가설이며 개인차와 잡음을 구별해야 한다.
6. **다른 분야 원리로 새 사실을 밝힐 수 있는가?** 압축 통로, 왕복정렬, 지식보존, 공유/고유 MI 목표를 전이한다. 각 원리를 쓰지 않은 강한 baseline보다 더 판별적인 경우에만 채택한다.
7. **기존 데이터의 다른 질문 활용은?** 사건 annotation을 학습타깃이 아니라 독립 alignment 검증으로, 반복 자극을 신뢰도와 미래입력 통제의 대조로 재해석할 수 있다. 실제 필드 존재 여부는 확인 전이다.
8. **결과가 계산 이해를 바꾸는가?** 공통 공간 충분성의 반박, 사건경계에서 통합상태 유지/재설정의 구별, 물리시간과 사건단계의 구별은 계산적 제약을 준다. 단순 encoding 점수 상승만 나오면 방법론 결과로 낮춰 보고한다.

## 13. 다음 교차검토로 넘길 사항

- **Agent07 Geometry & Information**와 연결할 질문: 공유/고유 표상의 비유일성, 모델 기반 interaction과 정보이론 synergy의 구별, 합성 null의 타당성. 아직 해당 Agent 결과를 읽거나 실제 토론하지 않았다.
- **Agent08 Systems Neuroscience**와 연결할 질문: 감각·transmodal 분포에서 통로 충분성/시간 상태가 구별되는지와 ROI 선택 독립성. 아직 교환하지 않았다.
- **Agent01 Dataset**에 필요한 사실: 실제 원본 영상·오디오 접근, 시간별 정서주석/사건주석, run/반복 구조, HRF를 적용할 원시 시간축. 이러한 사실이 없으면 해당 질문을 실현 가능하다고 표시하지 않는다.
- 원문 후속: FactorCL의 식별성·MI 가정, MERT/VideoMamba 정식출판 서지, MBT 통합층 ablation, V-JEPA2.1 논문 링크와2026 dense feature 검증. 체크포인트 license·다운로드·추론 비용과2024–2026 신경 선행연구 반례검색도 남아 있다.

초기 과학적 잠재력은 RQ05-1과 RQ05-2가 높지만, 단기 실현성 순위는 metadata를 확인하기 전에는 매기지 않는다. Round2–5 토론·실제 무작위조합·신경 파일럿은 수행하지 않았다.
