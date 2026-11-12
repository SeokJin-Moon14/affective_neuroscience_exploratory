# Agent06 Frontier AI 독립 탐색 보고서

확인일: 2026-11-12. 작성: Agent06 Frontier AI.

`source`: evidence_index.md / papers.csv; `verified_on`: 2026-11-12; `confidence`: 공식 서지·문서 높음, 정서/신경 전이 및 신규성 미검증; `needs_followup`: 본문·Discussion·데이터 가용성·선행 반례 확인; `origin_agent`: 06_frontier_ai.

 상태: Round 1 독립 조사 완료, 본문·Discussion 및 신규성 반례 검색은 후속 과제. 기존 EmoBrain 및 타 Agent 결과를 검색·열람하지 않았다. 작성 범위는 `agents/06_frontier_ai/`로 제한했다. Horikawa의 현재 자료·라벨에 맞춰 발상을 선별하지 않았다.

가장 유망한 전이는 특정 모델을 정서 분류기에 넣는 일이 아니다. **학습이 보존하도록 강제한 정보의 종류를 바꾸어, 정서 관련 신경표상이 현재 장면, 예측 가능한 상태, 맥락에 의존하는 관계 중 무엇을 필요로 하는지 구별하는 것**이다. 예측 목표, 희소 분해, 환경 불변성은 서로 다른 판별 도구다.

## 1. 검증 범위와 증거 수준

- `papers.csv`: 공식 저장소에서 제목·저자·연도·arXiv 식별자를 확인한 고유 논문 9편. 미션의 30필드에 `source`, `needs_followup`을 추가한 32열이다. DreamerV3 2023 preprint와 2025 Nature 표기는 한 연구로 집계했다.
- 실제 다운로드한 공식 저장소 README·코드·HTML 19개, 실패한 URL 6개를 `evidence/sources.json`과 `evidence_index.md`에 기록했다. URL·확인일·HTTP 상태·SHA-256을 보존했다. 일부 GitHub HTML은 별도 서지 정보를 얻지 못했어도 실패 이력을 숨기지 않기 위해 보존했다.
- **논문 본문 직접 확인 0편, Discussion 직접 확인 0편**이다. 공식 README/BibTeX/코드 확인은 미션의 E1 중 공식 문서 범주에 해당한다. 이를 논문 본문 검증으로 계산하지 않는다. 성능 언급은 문서의 주장이고 독립 재현 결과가 아니다.
- 아래 연구 연결·한계 해석·반증 조건은 모두 Agent의 **E3 새 가설 또는 근거 기반 추론**이다. 저자의 Discussion 미래 제안으로 제시하지 않는다. E0는 본문·정서 전이·신규성 미검증 부분에 적용한다.
- 네트워크 정책이 허용한 GitHub/raw GitHub를 사용했다. arXiv/Crossref 차단에 관한 상위 작업 지시를 준수했으며 차단을 우회하거나 접근 성공을 주장하지 않았다. 본 Agent는 해당 도메인에 새 접근 시도를 하지 않았다. 공식 GitHub에 이미 공개된 README와 코드를 독립적인 원출처로 확인했다.
- 체크포인트 다운로드, 모델 추론·학습, 뇌 자료 분석, 논문 성과 재현은 수행하지 않았다. 현재 문헌 목록은 최신 AI의 전수 조사나 정서 분야 최초성 입증이 아니다.

### 1.1. 확인한 논문과 원래의 계산 원리

| ID | 논문·연도 | 실제 확인 위치 | 원래 원리와 전이 경계 |
|---|---|---|---|
| FAI01 | *Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture* (2023) | [I-JEPA](https://github.com/facebookresearch/ijepa), 로컬 `ijepa_README.md` 3–35, 149–154행 | 이미지의 다른 부분에서 가려진 부분의 **잠재표상** 예측. 정적 이미지의 부분 관측 모델이며, 이 사실만으로 시간적 미래예측을 주장할 수 없다. |
| FAI02 | *VideoMAE: Masked Autoencoders are Data-Efficient Learners for Self-Supervised Video Pre-Training* (2022) | [VideoMAE](https://github.com/MCG-NJU/VideoMAE), `videomae_README.md` 12–13, 34–44, 133–145행 | 90–95% tube masking과 masked autoencoding. 비디오 시간 중복성을 학습 과제에 활용한다. 마스킹 복원 난도와 실제 사건의 예상 밖 정도는 다르다. |
| FAI03 | *Revisiting Feature Prediction for Learning Visual Representations from Video* (2024) | [V-JEPA](https://github.com/facebookresearch/jepa), `vjepa_README.md` 14–30, 402–407행 | 텍스트·negative examples·pixel reconstruction 없이 feature prediction. 마스킹의 문맥이 미래 프레임을 포함할 수 있으므로 시간 방향성은 별도 실험 조건이다. |
| FAI04 | *V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning* (2025) | [V-JEPA 2](https://github.com/facebookresearch/vjepa2), `vjepa2_README.md` 7–24, 64, 530–540행 | 비디오 자기지도 모델과 로봇 상호작용으로 후학습한 action-conditioned 2-AC를 구분한다. 수동 관람 자료에 action/reward가 있다고 가정하지 않는다. |
| FAI05 | *V-JEPA 2.1: Unlocking Dense Features in Video Self-Supervised Learning* (2026) | 같은 저장소 `vjepa2_README.md` 32–49, 544–550행 | 보이는 토큰과 가려진 토큰 모두의 dense predictive loss, 중간층의 deep self-supervision, 이미지/비디오 tokenizers. 공간 정보와 전역 의미의 경쟁을 탐구할 도구다. README paper 버튼은 `TODO`지만 BibTeX에는 `2603.14482`가 있다. 서지 교차 확인 필요. |
| FAI06 | *DINOv3* (2025) | [DINOv3](https://github.com/facebookresearch/dinov3), `dinov3_README.md` 18–43, 875–883행; `dinov3_ssl_meta_arch.py` | dense features; 공식 훈련 구현의 DINO·iBOT·KoLeo 및 조건부 Gram loss, README의 Gram anchoring 단계 확인. 단계별 원인 효과와 정서 관련성은 미검증이다. |
| FAI07 | *Mastering diverse control tasks through world models* (2025) | [DreamerV3 저자 저장소](https://github.com/danijar/dreamerv3), `dreamerv3_README.md` 12–19, 28–45, Disclaimer | 행동 조건부 범주형 잠재 전이·보상 예측, imagined trajectory로 actor–critic 학습. 저장소는 reimplementation임을 명시한다. Nature DOI·최종 쪽수는 재확인 필요. |
| FAI08 | *Invariant Risk Minimization* (2019) | [IRM](https://github.com/facebookresearch/InvariantRiskMinimization), `irm_README.md` 3–10; `irm_main.py` 107–111, 128–150행 | 환경별 risk와 scalar classifier의 gradient penalty를 결합한 예제. predictor 불변성은 단순 feature 동일성이나 인과 발견과 같지 않다. |
| FAI09 | *Who Needs Labels? Adapting Vision Foundation Models With the Metadata You Already Have* (2026) | [DINOv3 FINO branch](https://github.com/facebookresearch/dinov3/tree/FINO), `finO_README.md` 715–739, 921–930행 | metadata를 auxiliary 또는 adversarial guide로 사용해 CLS를 보존·억제하는 적응. FMoW 예시는 sub-region 보존, year 억제다. 무엇을 nuisance로 지정했는지가 과학적 가정이다. |

### 1.2. 서지 확정 수에 포함하지 않은 방법 증거

이 항목들을 논문 9편에 더하지 않는다. 실제 기술을 조사했지만 불완전한 논문 서지를 채워 넣지 않았다.

| 도구·공식 출처 | 직접 확인 | 정서·뇌 전이의 의미와 제한 |
|---|---|---|
| [OpenAI sparse_autoencoder](https://github.com/openai/sparse_autoencoder) | `sae_openai_README.md`의 GPT2-small activation encoder/decoder; `sae_model.py` 162–174행의 TopK 선택, 나머지 0 처리 | 밀집 활성의 재구성과 희소 특징의 선택을 분리할 수 있다. 이 저장소의 README에는 목표 논문 *Scaling and evaluating sparse autoencoders*의 완전한 서지가 없어 해당 논문을 검증 목록에 넣지 않았다. 특징 하나가 정서 개념 하나라는 결론은 성립하지 않는다. |
| [transcoder_circuits](https://github.com/jacobdunefsky/transcoder_circuits) | `transcoder_README.md`: MLP를 희소 특징의 선형 조합으로 대체, GPT2/Pythia 비교 notebook과 해석 실패 사례를 함께 제공 | 단순 activation 재구성과 layer 간 계산 대체를 구별한다. 정서 관련 encoder에 그대로 호환된다는 증거는 없다. 논문 제목·연도·저자 완전 서지 미확인. |
| [circuit-tracer](https://github.com/safety-research/circuit-tracer) | `circuit_tracer_README.md` 3–6행: feature·error node·입력 token·output logit 간 직접 효과 계산; 20행: 모델 feature intervention 가능 | 오류 노드를 남겨 근사 모델의 설명 잔차를 명시하는 것이 핵심이다. README의 Ameisen/Lindsey 2025 링크는 확인했지만 원 논문을 읽지 않았다. model circuit은 brain circuit이 아니다. |
| [DomainBed](https://github.com/facebookresearch/DomainBed) | `domainbed_README.md` 3행에서 *In Search of Lost Domain Generalization*과 `2007.01434` 연결; model selection 절에서 IID·held-out domain·oracle 기준 구별 | test-domain 선택은 비교용 oracle 상한이며 일반화 주평가에 사용하면 안 된다. 논문 저자·출판연도 전체 서지 재검증이 남아 확정 수에서 제외했다. |

`google-deepmind/jumprelu` 및 `gemma_scope`로 추정한 URL은 404였으므로 JumpReLU의 공식 코드·논문 확인 성공으로 기록하지 않았다. 최초 `transcoder_circuits/main`은 404였고 저장소의 `master`에서 README를 확인했다. 404를 연구의 부재로 해석하지 않는다.

## 2. 네 종류의 주장을 분리한다

| 주장 | 필요한 증거 | 본 조사에서 가능한 범위 |
|---|---|---|
| 예측력 | 독립 자극·피험자·런에서 정서 주석 또는 신경 신호를 예측 | 제안만 작성. 아직 결과 없음. |
| 신경 정렬 | 신뢰도·noise ceiling을 고려한 encoding/RSA 및 통제 특징 대비 고유 설명분산 | 모델 후보·대조군 제안. 정렬이 같은 알고리즘의 증거는 아니다. |
| 계산 설명 | 두 경쟁 목표/전이 규칙이 서로 다른 예측을 하고 적절히 통제한 실험에서 한쪽이 반박됨 | 픽셀 복원 대 상태 예측, 희소 basis 대 분산 계산, 맥락 제거 대 필요 맥락을 비교하도록 설계. |
| 인과 증거 | 검증한 자극 조작 후 새로운 인간 신경 측정, 또는 별도 인과 설계 | 모델 feature ablation은 모델 인과만 검증. 뇌 인과는 주장하지 않음. |

## 3. 미해결 문제 5개

1. **학습 목적의 효과가 데이터/용량/읽기 방식과 식별되는가?** V-JEPA 대 VideoMAE 대 DINO 비교는 architecture·학습 영상·데이터 규모가 동시에 변한다. 예측력이 높아도 잠재 예측 원리가 원인인지는 미해결이다. matched-budget 소형 재학습 또는 같은 backbone/objective ablation이 후속 핵심이다. 출처: FAI01–06, E3.
2. **추상화가 버린 정보 중 무엇이 신경 계산에 필수인가?** global semantic embedding이 버린 색·움직임·지역 관계는 nuisance일 수도, 정서 관련 신경정보일 수도 있다. 차원 감소가 아니라 동일한 현재 의미 아래의 상태 전이 정보 보존 여부를 시험해야 한다. 출처: FAI02,05,06, E3.
3. **희소 특징은 안정된 계산 단위인가, 임의 basis의 편리한 이름인가?** seed·dictionary width·sparsity·layer에 따라 feature가 쪼개지고 합쳐질 수 있다. 성능이 같은 분해가 다른 ‘정서 특징’을 내면 일대일 해석을 포기해야 한다. 출처: SAE/transcoder 공식 구현, E3.
4. **어느 환경 변화에 대해 불변이어야 하는가?** 촬영 장비를 지우는 일과 사건 맥락을 지우는 일은 다르다. context가 정서 관련 표상의 원인이라면 광범위한 불변성은 목표 신호를 지울 수 있다. 출처: FAI08–09, E3.
5. **관찰 비디오의 숨은 상태는 미래 정보와 실제로 구별되는가?** 양방향 masked prediction은 이미 본 전후 문맥을 채우는 과제일 수 있다. prefix-only 입력, 미래 masking, 시간 역전/순서 섞기 비교가 없으면 미래 기대를 검증했다고 할 수 없다. 출처: FAI03–04,07, E3.

## 4. 모델·방법 기회 5개

| 기회 | 새로 가능한 측정 | 경쟁 설명·최소 대조군 | 핵심 실패 조건 |
|---|---|---|---|
| O1 잠재 예측과 픽셀 복원의 분리 | 같은 자극에서 복원오차·잠재 예측오차·현재 특징을 별도 산출 | 현재 시각 특징으로 충분하다는 설명; 차원수·성능·시간 창 통제 | 오차의 고유 신경분산이 독립 자료에서 사라짐 |
| O2 dense 관계 정보의 보존 | 패치 관계/지역 특징과 global pooled 표현의 이중 비교 | 많은 특징 수 때문에 좋아졌다는 설명; 동일 rank·regularization·표본 수 | rank를 맞추면 차이가 없어짐 |
| O3 희소 특징 안정성 감사 | 여러 SAE seed·width에서 공통 subspace와 개별 feature를 구분 | 해석 가능한 이름이 임의 분해라는 설명; PCA·random sparse dictionary·원래 dense feature | 대응 feature가 재현되지 않고 subspace만 안정적이면 개별 단위 가설 기각 |
| O4 metadata를 보존/억제하는 대칭 비교 | nuisance guide와 context guide에 대한 표상 손실 지도 | 모든 환경 변화를 지우면 좋다는 설명; frozen baseline·ERM·sham guide | context 제거와 nuisance 제거가 통제 후 구별되지 않음 |
| O5 모델 계산의 필요성과 신경 정렬을 교차 검사 | 모델 내 intervention 효과 × 독립 신경 설명력의 2×2 표 | decodable feature가 실제 계산에 쓰이지 않는다는 설명; 동에너지 무작위 perturbation·재구성 잔차 | 신경 정렬은 있어도 해당 feature 제거가 모델 예측을 바꾸지 않음 |

O5의 ‘필요성’은 선택한 모델·과제·개입에서의 필요성이다. 인간 신경 계산의 필요성으로 일반화하지 않는다.

## 5. 타 분야 전이 아이디어 5개

1. **비디오 학습 → 정서 관련 예측 상태.** FAI03–04의 predictor를 현재 장면 encoder와 분리한다. 동일한 현재 프레임인데 이전 사건 순서가 다른 자극에서 후속 상태 예측과 신경반응이 함께 달라지는지 묻는다. 신경반응은 visual·motion·semantic baseline과 함께 비교한다. 새로운 실측이 필요한 발견 경로이며 Horikawa에 그 조작이 있다는 가정은 하지 않는다.
2. **강화학습 상태 추상화 → 정서 범주 내부의 전이 구별.** FAI07의 원래 목표는 제어에 유용한 잠재 상태다. 이를 ‘같은 정서 주석을 가진 사건도 가능한 후속 사건이 다르면 다른 신경 상태인가?’로 전이한다. 관람 자료에는 행동 정책 대신 관찰 가능한 전이 예측만 사용한다. action/reward 자료가 없다면 정책 설명을 보류한다.
3. **기계적 해석 → 안정된 계산 방향 검증.** SAE와 transcoder를 이용해 정서 관련 신경정보에 정렬된 방향이 단순 readout 가능한 방향인지 모델 내 다음 상태 예측에 쓰이는 방향인지 분리한다. 랜덤 basis, dense feature, matched reconstruction을 대조한다. 관측 fMRI에서 circuit 복원을 주장하지 않는다.
4. **도메인 일반화 → 맥락 필요성의 경계.** FAI08–09를 이용해 nuisance 지우기와 context 지우기를 대칭 비교한다. 정서 주석과 뇌의 대응이 환경에 대해 완전히 불변이라는 가정을 반박할 수 있다. 환경 정의는 외부 metadata로 사전 결정하고 정서/뇌 신호를 보고 최적 환경을 선택하지 않는다.
5. **위성·현미경 metadata 적응 → 기존 신경 자료의 획득 차이 감사.** FAI09의 auxiliary/adversarial guide를 촬영/획득 특징이 시각 embedding에 남는 정도를 분석하는 도구로 옮긴다. 그러나 scanner metadata는 자극 이미지의 속성이 아니므로 무비판적으로 이미지 encoder 학습 guide로 쓰지 않는다. 자극 metadata와 신경 획득 metadata를 다른 모형에서 처리하고 shared/private 성분의 전이를 평가한다.

## 6. 예상 밖의 연결 3개

| 연결 | 원래 목적 → 새 질문 | 가정·검증 | 연계할 역할 |
|---|---|---|---|
| C1 비디오 masking × 부분 관측 상태 식별 | 빠른 표현학습을 위한 가림이 ‘같은 관측, 다른 숨은 상태’ 자극 설계로 전환 | 이전 문맥만 다르게 제시; 현재 프레임·장면 의미·후속 확률을 구분. 모델의 uncertainty와 HRF 지연을 혼동하지 않음 | Agent05 시간 역학, Agent08 분산 신경 계산 |
| C2 transcoder error node × 신경 설명의 누락 성분 | 근사 회로의 오류 노드를 명시하는 원리를 encoding의 미설명 성분 감사로 전환 | SAE 재구성 잔차도 별도 신경 설명 변수로 사용. 잔차가 중요하면 희소 특징의 포괄성 주장을 반박. 잔차의 중요성이 독립 brain mechanism을 증명하지는 않음 | Agent07 식별성, Agent08 시스템 신경과학 |
| C3 위성 metadata debiasing × 맥락 선택성 | 센서/연도 제거 원리를 ‘버려도 되는 맥락’과 ‘유지해야 하는 맥락’ 구별에 전환 | nuisance로 정한 변수가 실제 신호일 가능성을 대칭적 guide ablation으로 검증 | Agent01 metadata, Agent10 의미표상 |

위 역할 연결은 후속 교차 검토의 제안이며 실제 에이전트 간 토론을 했다는 뜻이 아니다.

## 7. 숨겨진 가정 3개와 뒤집는 실험

| 가정 | 어느 연구 흐름에서 생기는가 | 왜 그대로 믿을 수 없는가 | 최근 기술로 판별하는 방법 |
|---|---|---|---|
| A1 의미적으로 추상적인 표현일수록 정서 신경표상에 적합하다 | I-JEPA/JEPA의 의미적 feature 장점에 대한 신경학적 확장 | 원 논문이 정서에 대해 이 가정을 입증한 것은 아님. 정보 제거가 신경 신호도 지울 수 있음 | V-JEPA 2.1 dense supervision·DINOv3 관계 특징·global pooling을 동일 rank로 비교하고 제거한 잔차의 신경정보 측정 |
| A2 이름 붙이기 쉬운 희소 feature는 실제 신경 계산 단위다 | SAE 기반 해석을 신경 축으로 번역할 때 | dictionary의 비유일성과 분할/병합; 언어 이름은 독립 측정이 아님 | seed/width 안정성, 무작위 basis, held-out stimulus, 모델 내부 개입과 뇌 정렬의 이중 검사 |
| A3 정서와 관련 없는 환경 정보는 모두 제거해야 한다 | IRM·domain-adversarial 적응의 쉬운 전이 | context는 nuisance일 수도, 상태 식별에 필요한 정보일 수도 있음 | FINO식 보존/억제 guide를 대칭 적용. 외부 정의 nuisance/context group에서 효과 방향과 외부 일반화를 비교 |

세 가정은 해당 AI 저자들이 정서에 관해 직접 주장했다는 뜻이 아니라, 정서·뇌 연구로 전이할 때 연구자가 덧붙이기 쉬운 가정이다.

## 8. 신규 Sub-axis 3개

상세 등록 필드는 `subaxes.csv`에 보존한다. 새 문자 Axis를 억지로 늘리기보다 기존 축의 계산적 차이를 명확히 하는 하위축으로 제안한다.

| axis_id | 이름·정의 | 유형 태그 | 대표 근거 | 열린 질문 |
|---|---|---|---|---|
| V.FAI1 | **예측에 충분한 상태와 복원 정보의 분리**: 현재 관측을 설명하는 정보와 가능한 상태 전이를 구별하는 정보를 분리 | Construct / Stimulus; Model / Method; Structure / Dynamics; Inference / Measurement | FAI01–04,07 | 정서 관련 신경정보는 현재 장면 동일성을 넘는 상태 전이 구별을 보존하는가? |
| R.FAI2 | **분해 안정성과 계산 사용의 이중 식별**: 해석 가능한 방향의 재현성, 모델 내 필요성, 신경 정렬을 서로 다른 축으로 측정 | Neural; Model / Method; Structure / Dynamics; Inference / Measurement | SAE·transcoder·circuit-tracer 기술 문서 | 안정된 희소 특징이 없는 경우에도 안정된 분산 subspace가 정서 관련 신경정보를 설명하는가? |
| S.FAI3 | **선택적 맥락 불변성**: 어떤 환경 변화는 지우고 어떤 변화는 보존해야 하는지 실험으로 정의 | Construct / Stimulus; Model / Method; Inference / Measurement | FAI08–09; DomainBed 방법 문서 | nuisance 제거는 전이를 높이면서 필요 맥락 제거는 신경 설명력을 낮추는 이중 분리가 존재하는가? |

## 9. 강한 후보 질문: 모델 적용 → 과학 질문 → 가정 반박

### RQ-FAI1: 현재 장면이 같아도 가능한 미래가 다르면 정서 관련 신경표상이 달라지는가?

1차 적용은 JEPA의 현재 특징·prefix-only 예측 상태·예측오차로 신경반응을 예측하는 것이다. 2차 과학 질문은 정서 관련 신경표상이 입력의 의미적 목록을 넘어 가능한 후속 상태를 구별하는가이다. 3차 도전은 정서 표상이 현재 장면 의미의 readout이면 충분하다는 설명과 상태 전이 표현이 추가로 필요하다는 설명을 분리한다.

**판별 설계:** 현재 장면은 맞추고 이전 사건 순서/후속 전이 확률을 달리한다. 미래 정보 없는 prefix-only predictor와 bidirectional reconstruction을 분리한다. optical flow·객체/장면·caption semantics·시간 경과·사건 경계·반복 효과를 통제하고 실제 정서 주석의 측정 단위를 확인한다. 영상 단위 held-out split과 피험자 일반화, HRF를 고려한 지연 모형을 사용한다.

**반증:** 적절한 reliability 범위에서 상태 정보의 고유 분산이 없으면 현재 장면 설명으로 충분하다는 결과다. 전이 정보가 설명하되 정서 주석과의 관련이 독립 검증되지 않으면 일반 사건 예측 연구로 남고 정서 특이성을 주장하지 않는다. 예측 차이가 low-level motion에 환원되면 질문을 재설계한다.

**강한 반론과 수정:** 모델군마다 학습자료가 달라 이득 원인을 식별하기 어렵다. 먼저 fixed representations의 판별적 관측을 탐색하되 계산 원리의 인과적 우위를 주장하지 않는다. 유망하면 같은 architecture/data의 목적함수 비교와 새로운 통제 자극 실험으로 강화한다. predictive coding/temporal encoding 기존 연구와 중복 위험이 크므로 최종 신규성 판정은 보류한다.

### RQ-FAI2: 정서 관련 신경정보는 개별 희소 특징에 고정되는가, 여러 분해에서 유지되는 분산 방향에 고정되는가?

1차 적용은 신경 정렬이 높은 모델 층에 SAE를 학습하는 것이다. 2차 질문은 개별 feature와 안정된 subspace 중 어느 수준이 자료를 지지하는가이다. 3차 도전은 해석 가능한 이름을 붙인 feature를 신경 계산 단위로 취급하는 관행이다.

**판별 설계:** 모든 feature 학습·선택을 training fold에서 수행한다. 여러 seed·dictionary width·활성 개수에서 feature correspondence와 subspace correspondence를 따로 측정한다. original dense, PCA, random sparse dictionary, 재구성 잔차와 비교한다. 신경 정렬을 본 뒤 같은 자료로 feature를 설명/검증하지 않는다. 모델에서 feature를 제거할 때 norm·재구성 오차·무작위 개입 크기를 맞춘다.

**반증:** feature 단위 대응은 무너지지만 subspace와 신경 설명력은 유지되면 일대일 ‘정서 특징’ 주장을 기각하고 분산 코드로 수정한다. 어떤 방법도 원래 feature보다 유용하지 않으면 SAE는 시각화/압축 도구로 남는다. model ablation이 성공해도 인간 뇌 회로의 인과 결론은 낼 수 없다.

**강한 반론과 수정:** 비정서 LLM의 SAE 기법이 video encoder에 직접 맞지 않을 수 있다. 먼저 작은 공개 vision backbone의 activation에서 재구성·stability 기준을 통과시키고, 실패하면 neural circuit 이름을 붙이지 않는다. feature의 정서 명칭은 AI-generated label이 아니라 독립 자극/주석 검증으로만 평가한다.

### RQ-FAI3: 정서 관련 신경정보는 어느 맥락 변화에 불변이고 어느 변화에 선택적으로 민감한가?

1차 적용은 metadata-guided/IRM 특징으로 데이터셋 전이를 개선하는 것이다. 2차 질문은 nuisance와 필요한 context의 경계다. 3차 도전은 가장 불변인 표현이 가장 좋은 신경 설명이라는 가정이다.

**판별 설계:** 확보된 metadata만으로 nuisance 후보와 context 후보를 사전 정의한다. frozen·ERM·nuisance-guided·context-guided·sham-guided 모델을 비교한다. 본문 미확인 FINO recipe를 곧바로 신경자료에 적용하기보다 guide의 정보량·모형 복잡도·학습 예산을 맞춘 소형 대조부터 한다. outer held-out domain과 inner train/validation selection을 분리한다. test-domain oracle은 주결과에서 제외한다.

**반증:** nuisance 제거와 context 제거의 차이가 완전히 사라지면 선택적 불변성 가설을 지지하지 않는다. 신경 설명력이 높아도 정서 주석과의 구별 가능한 관련이 없다면 정서 특이성은 보류한다. 한 데이터셋에서만 성립하면 dataset shortcut을 우선 검토한다.

**강한 반론과 수정:** 자연 자료에서 context와 정서 주석이 얽혀 있으면 정보 제거 효과를 해석하기 어렵다. 새로운 crossed-context stimulus가 필요할 수 있다. 이 조건을 만족하지 못하면 발견 과제로 유지하고 Horikawa 즉시 파일럿이라고 선언하지 않는다.

## 10. 여덟 탐색 질문에 대한 명시적 답

1. **왜 아직 시도되지 않았는가?** ‘아직’이라는 최초성은 미검증이다. 기존에는 목적함수별 공개 video encoder, 대규모 sparse feature, metadata guide가 분리된 연구 흐름이었다. 실제 선행 시도가 없다고 주장하지 않고, 모델/data confound와 fMRI 시간 해상도의 어려움을 검증 장벽으로 제시한다.
2. **최근에야 가능해진 것은 무엇인가?** V-JEPA 2.1의 dense/deep predictive supervision, DINOv3 dense feature와 공식 훈련 경로, FINO의 명시적 guide/debias interface, 공개 SAE/circuit 도구가 목표 정보의 보존·삭제를 실제 비교 가능한 조작으로 만든다. 현재 환경에서 모든 weight를 쓸 수 있다는 뜻은 아니다.
3. **기존 가정 중 무엇이 틀렸을 수 있는가?** 의미 추상화가 항상 정서 신경정보를 강화한다, 희소 feature가 고유한 신경 단위다, 모든 환경 불변성이 유익하다는 세 가정이다. §7의 실험으로 반박 가능하다.
4. **AI가 기존 뇌과학 모델보다 잘 포착할 수 있는 것은 무엇인가?** 고차원 장면 조건부 상태, 국소 관계 구조, 여러 가능한 상태 전이를 계량하는 능력이다. 실제 우위는 아직 측정하지 않았으며 정적 시각/의미 baseline을 이겨야 한다.
5. **뇌가 표상하지만 AI가 놓칠 수 있는 것은 무엇인가?** 긴 문맥 누적, 피험자별 경험에 따른 사건 상태 구별, 현재 학습 목표가 압축해 버린 정서 관련 미세한 차이다. 이를 모형 잔차로 발견하더라도 먼저 측정 잡음·시간 정렬·모델의 관측창 부족을 배제한다. 제외 연구 주제를 재도입하지 않는다.
6. **전혀 다른 분야의 방법이 무엇을 밝히는가?** world-model state abstraction은 현재 범주와 미래 전이의 구별, mechanistic interpretability는 readout과 계산 사용의 구별, domain generalization은 nuisance와 필요 맥락의 구별을 제공한다.
7. **기존 데이터셋이 다른 질문에 답할 수 있는가?** 원자극 접근·반복/순서·metadata·시간 정렬이 실제 있으면 새 특징을 추출해 그 가능성을 탐색할 수 있다. 본 Agent는 Horikawa/Emo-FilM/Spacetop/NSD의 해당 필드를 확인하지 않았으므로 자료 이름만으로 가능하다고 선언하지 않는다. 조건부 경로는 아래에 제시한다.
8. **결과가 신경 계산 이해를 바꾸는가?** 긍정 결과는 어떤 정보 보존 제약이 정서 관련 분산 신호에 필요한지 좁힌다. 부정 결과도 상태 예측 필요성, 개별 희소 단위, 광범위 불변성 중 특정 설명을 기각한다. 단순 정확도 우위만 얻으면 방법 연구로 분류한다.

## 11. 자료 제약을 소급 적용하지 않는 후속 경로

| 경로 | 필요한 실제 정보 | 조건부 자료 매핑 | 현재 판정 |
|---|---|---|---|
| 고정 자극의 목적함수·dense/global 비교 | 원자극, 독립 반복/자극 구분, fMRI와 정서 주석의 정확한 대응 | Horikawa 우선 검토; 다른 시각 자료도 비교 가능 | Agent01 확인 전 실현성 미확정 |
| 상태 전이·prefix-only 예측 | 자극 프레임 순서, 제시 timing, 충분한 연속 문맥, 주석 시간 단위 | Emo-FilM/Spacetop은 확인 후보이며 실제 가용성 주장 아님 | 발견 경로 유지; 시간 metadata 확인 필요 |
| sparse dictionary 안정성 | model activation, 독립 자극 split, 신경 reliability | Horikawa 혹은 시각 신경자료; NSD의 정서 주석 존재는 가정하지 않음 | AI 단계만 먼저 검증 가능; 실제 실행 미수행 |
| 선택적 불변성 | 정서 주석과 독립적으로 정의한 환경·맥락 metadata, 여러 환경 | 데이터셋 이름보다 외부 metadata의 식별력이 우선 | 관찰자료에서 식별 불가하면 새 crossed-context 실험 필요 |

## 12. 완료·미완료와 우선 판단

완료: 독립 지침 확인, 공식 서지 9편과 방법 출처 수집, 미해결 문제/기회/전이 각 5개, 연결/가정/Sub-axis 각 3개, 8질문 검토, 판별적 후보 3개. 모델 수행과 문헌 Discussion Mining은 완료하지 않았다. 다른 Agent와의 연구 토론은 아직 실시하지 않았다.

**과학적 잠재력:** RQ-FAI1은 현재 장면 코드와 상태 전이 코드를 구별하므로 높다. **개념적 독창성 후보:** RQ-FAI2의 feature 안정성·계산 사용·신경 정렬 분리는 개별 feature 명명 관행에 직접 반증 조건을 건다. **단기 실현성 후보:** 실제 자극 접근이 확인되면 O2 dense/global 동일-rank 비교와 SAE 안정성 감사가 먼저 가능하다. **종합 순위는 보류:** 세 후보의 자료·원문·가까운 선행연구가 검증되기 전 점수 합산으로 우선순위를 확정하지 않는다.

다음 작업은 논문 본문/Discussion 및 최종 서지 확인, 직접 가까운 신경/정서 선행연구 반례 검색, Agent01의 실제 metadata 검증, Agent07/08의 식별성·신경 해석 비판이다. 저자 미래 제안이 없는 현재 상태에서 본 보고서는 ‘Discussion 기반 기회 발굴 완료’로 집계하면 안 된다.
