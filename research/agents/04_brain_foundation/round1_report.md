# Agent04 Brain Encoding & Foundation Models — 독립조사 Round1

2026-11-12. origin_agent=04_brain_foundation. EmoBrain과 다른 Agent 결과를 열람하지 않았고 정서 데이터셋의 현재 라벨에 사전학습 목표를 맞추지 않았다. 프로젝트 AGENTS.md·RESEARCH_MISSION.md를 적용했다. 환경접근에는 cloud-environment-runtime 지침을 적용했으며 연구데이터나 모델을 실행하지 않았다.

**핵심 발견은 ‘범용 뇌표현’의 정보 보존 자체를 과학적 검증 대상으로 삼을 수 있다는 점이다.** fMRI→표현 모형과 자극→fMRI 모형을 대조하면 같은 정서 관련 변동이 공간집계, 목표함수, 시간 예측, 개인간 평균에서 어느 단계에 보존되거나 소실되는지 물을 수 있다. 이 결론은 연구팀의 E3 제안이며 입증된 신경기제가 아니다.

## 검증 범위

`papers.csv`는 고유 10편, 미션30개 필드+source/needs_followup의32열이다. **논문 본문·부록까지 읽은 논문은 Brain-Mamba 1편**, 나머지 9편은 공식 저장소의서지·README·일부코드를 확인했다. 이9편의E1은 코드/문서에만 해당하며 성능·Discussion 원문 확인을 뜻하지 않는다. BrainLM은 공식 코드확인과 논문서지 확인을 분리해 문헌집계에서 제외했다. Brainmarks는CortexMAE동일논문의평가도구여서 추가 문헌으로 세지 않았다. Mamba2/3도후속 코드 식별만기록하고10편에 추가하지 않았다.

arXiv와HuggingFace는proxy403, 일부GitHub검색은429였다. 출판사PMLR공식GitHub가Brain-MambaPDF를 제공해 본문 접근이 가능했다. 공식Brain-Mamba software주소는404였다. 실패와로컬원본의해시는`source_manifest.csv`에남겼다. 저자의future direction은직접 읽은AppendixE만인용했고 나머지는미확인으로표시했다.

## 모델군을 나누면 드러나는 질문

| 계산 방향 | 실제 모델/근거 | 무엇을 학습하는가 | 무엇을 아직 말할 수 없는가 |
|---|---|---|---|
| fMRI→표현/복원 | SwiFT BF01, CortexMAE BF02, Brain-JEPA BF05, TFF BF07 | 신경신호에서 재사용할 통계적 구조 | 표형 성능이 정서 관련 transient 보존을 뜻하지 않음 |
| 자극→뇌반응 | TRIBE v2 BF03 | 자극 조건부 피질반응 | 평균 피험자 예측이 개인별 반응·인과모의실험의정답이라는주장 |
| 신호+그래프→표현 | Brain-Mamba BF04 | 시계열과연결망의상호정보,입력 의존선택 | 합성corruption성공이OOD검증이라는주장 |
| 구조+기능→공통token | Brain Harmony BF06 | 형태·기능의결합 | 구조정보추가효과가정서기제라는주장 |
| 원리적 비교 | MAE BF08, I-JEPA BF09, Mamba BF10 | 복원/잠재예측/상태 선택 | 최신원리의적용자체가새로운뇌과학질문이라는주장 |

## 숨겨진 가정 3개와 판별 실험

1. **자기지도에서 좋은 표현은 정서 관련 신호도 보존한다.** E3 의심: MAE는 큰분산·자기상관을,JEPA는예측가능구조를,contrastive목표는변환불변성을 선호하므로 신뢰 가능한 작은 transient를 제거할 수 있다(BF01/02/05/08/09). 같은 원자료와공간 표현에서frozen/미학습network/rawridge/동일budgetfrom-scratch를 비교한다. 신뢰도있는 정서 관련잔여정보가pretrained에서만소실되면가정을반박한다.
2. **공통atlas·flatmap·평균 피험자는 계산질문에중립적이다.** E3 의심: 공간집계와subject평균은정보를단순히정렬하기도하지만사라지게할수있다(BF02/03/06). dense→parcel결정적변환,개인별→평균예측을분리하고 동일probe용량·SNR·피험자수·측정신뢰도를맞춘다. 피질 전용모형의실패를전체 뇌의부재로해석하지않는다.
3. **긴문맥을이용한성능은긴신경적통합을입증한다.** E3 의심: HRF·공통사건구조·시간보간·저주파드리프트가대신설명할수있다(BF03/04/05/10). FIR/HRF기반baseline,자기상관보존surrogate,run간독립,과거전용예측과양방향복원구분으로검사한다. 동일스펙트럼대조에서효과가사라지면신경적장기상태주장을기각한다.

## 미해결 문제 5개

| ID | 문제 | 근거상태와출처 | 답을가를관측 |
|---|---|---|---|
| U1 | 어떤사전학습 목표가신뢰가능하지만희소한정서 관련변동을지우는가? | E3; BF01/02/05/08/09의상이한목적함수 | 고정 자료·공간·probe에서conditional성능과noiseceiling차이 |
| U2 | spatial pooling과subject pooling중무엇이재현 가능한개인별정보를소실하는가? | E3; BF02/03/06구현 | 피험자 내반복신뢰도가높은잔차가평균에서선택적으로감소 |
| U3 | 자극조건부 모형과신경내재조건부 모형이놓치는정보는겹치는가? | E3; BF02/03/05 | cross-fitted residual의조건부추가설명력과외부자료재현 |
| U4 | Pearson고정연결망을학습형으로바꾸면보존되는정보가달라지는가? | **저자 E1**: BF04AppendixE pp249–250; 정서전이는E3 | 동일시간신호에서정적graph/학습graph/graphshuffle대조 |
| U5 | 입력 의존상태 선택은subject·자극·site이동에서견고한가? | **저자 E1**: BF04AppendixE는distribution-shift평가를미완으로명시; 구체 분할전이는E3 | source내성능과holdout일반화의교호작용; 부정 결과도허용 |

## 방법론적 기회 5개

1. **목적함수를 과학적 개입변수로 삼기**(BF02/05/08/09,E3): 같은ROI·data·encoder budget에서MAE/JEPA를비교한다. 표현 고유 정보와noise예측의구분이목표다.
2. **동일계열 공간 표현 비교**(BF02,E1도구/E3질문): CortexMAE-P/F/V와dense→parcel변환을이용해공간평균의정보손실을측정한다. pretrainedvariant의data/seed차이를먼저통제해야한다.
3. **이중조건부 예측**(BF02/03/05,E3): stimulus→brain과held-out brain-block→brain을별도학습하여두모형에서회수되는정보를분리한다. 잔차에정서라는이름을먼저붙이지않는다.
4. **선택적 SSM의입력 의존성제거 실험**(BF04/10,E3): selective/고정SSM/시간순서 교란을matched capacity로비교한다. 긴문맥성능을불변시간상수와구분한다.
5. **probe계층을분리한평가**(BF02와Brainmarks,E1도구/E3질문): frozen linear/attention/MLP/finetune을나누어표현에이미있는정보와head가새로학습한정보를분리한다. 성능이높은head를곧바로좋은foundation표현으로판정하지않는다.

## 분야 간 전이 5개

| 원분야→새 질문 | 새계산능력 | 검증/반론 | 연결가능Agent |
|---|---|---|---|
| 시각masked복원→정서 관련뇌정보의조건부예측단위 | BF08→BF02의tube/blockmask | 시간보간으로풀리는과제이면신경 질문이약함; HRF대조 | 07Geometry,08Systems |
| 이미지latent예측→원값과추상정보의소실차이 | BF09→BF05 | rawbaseline과용량일치가없으면압축효과일뿐 | 06Frontier,07Geometry |
| selectiveSSM→사건맥락별신경정보유지 | BF10→BF04 | 양방향scan을미래예측이라부를수없음; 과거전용마스킹필요 | 05Dynamics,11Brain-inspired |
| 멀티모달encoding→모형이설명하지못하는재현가능뇌정보 | BF03+BF02 | 영상저수준·의미·motion·HRF통제가없으면정서고유성결론불가 | 03Vision,05Dynamics |
| 구조·기능token통합→기능정보에서형태기여분리 | BF06+BF05 | 구조가subject/site식별자일수있음; T1shuffle·leave-site검증 | 07Geometry,08Systems |

다섯항목은모두연구팀 E3이며저자가정서연구를제안했다는뜻이아니다. 다른 Agent내용을읽지않은독립연계후보다.

## 예상 밖의 연결 3개

1. **재표본화 코드가 temporal theory의 숨은 가정이다.** CortexMAE의1초보간(BF02)과TRIBE의5초offset(BF03)은같은timeline을만드는단순편의가아니다. 이를통일하는과정자체가사건경계정보를지울수있다는E3질문. 제안: 원TR와native-sampling baseline,HRF지연민감도곡선에서효과가유지되는지검사.
2. **압축된평균 피험자와평균ROI는서로다른정보병목이다.** BF03평균 subject와BF02parcel은서로다른축의평균이다. 두평균을교차시켜어떤변동이개인공유이고공간적으로희소한지검사하는E3연결. 주의: noiseceiling차이로설명되는경우는표상결론을보류.
3. **그래프순서와gradient좌표는뇌의가까움을정의하는경쟁prior다.** BF04functionalordering과BF05gradientpositioning은동일한해부적거리보다기능유사성을우선할수있다. 학습fold내gradient생성,무작위/해부/기능 순서를대조해정서 관련정보의전이에서어떤관계가필요한지묻는E3연결. 구현성능만으로해당prior가뇌의알고리즘임을증명할수없다.

## 신규 Sub-axis 3개

세부등록은`subaxes.csv`. 제안축은기존A–X를덮어쓰지않는다.

- **J–X–Q: 사전학습 목표별 정보 보존/소실** — 어떤신뢰가능성분이재구성·잠재예측·불변성목표에선택적으로남는가. Neural/Model/Structure/Measurement태그.
- **H–F–X: 자극조건부와신경조건부표현의불일치** — 두조건부 모형의예측가능집합을비교하되잔차를정서와동일시하지않음. Construct/Neural/Model/Inference태그.
- **D–N–Q: 관측시간격자와잠재상태 선택의분리** — TR·HRF·재표본화와모델state-timescale의기여를구별. Structure/Model/Measurement태그.

## 강한 반론과개정

- **반론: 기존모델정보를probe하는것은새 benchmark일뿐이다.** 개정: 성능순위를목표로삼지않고상반가설(예측가능한공통구조 vs 신뢰 가능한희소transient)을먼저정의한다. 같은 데이터·해상도·목표/구조한요인씩변화한효과만해석한다.
- **반론: 정서 관련잔차는다른자극특성일뿐이다.** 개정: fold내low-level/semantic/motion특성추출·residualization과새자극외삽; 안정된정서annotation의추가설명력을요구한다. 미측정공변량때문에고유성최종입증은아니라고명시한다.
- **반론: 데이터크기가작아모형 효과와noise를구별못한다.** 개정: 반복신뢰도·계층bootstrap·run/stimulusholdout을우선; 신뢰가능잔차없으면기각/중단한다. window수는독립표본수가아니다.
- **반론: cortical모델로전체정서회로를논할수없다.** 개정: 피질에서검증할질문으로범위를한정하거나검증된subcortical입력을별도사용한다. 공개TRIBEgrid나Cortexreader옵션을실제pretrained가중치의 지원과혼동하지않는다.
- **반론: 시뮬레이션편집이인과증거인가?** 개정: 모형반응은검증대상예측이며생물학적인과효과가아니다. 향후새 실측 자극반응을필요로한다.

## 여덟 가지 탐색 질문에 대한 답

1. **왜아직시도되지않았는가?** E3: 사전학습 목표·입력공간·평가 head를동일 자료에서분리비교할공개도구가분산돼있었다. 정확선행연구역검색은다음라운드에서필요하다. “아무도하지않았다”는단정은하지않는다.
2. **최근가능해진것은?** E1: CortexMAE다중입력/variant와Brainmarks,TRIBEv2자극→피질API,JEPA가중치 링크가있다. 이 환경의실행 가용성은미확인.
3. **틀렸을수있는기존가정은?** E3: 범용 표현의보편적정보보존,공통공간변환의중립성,긴문맥성능의신경시간상수해석.
4. **AI가더잘포착할수있는것은?** E3: 비선형자극결합과분산된공간·시간상관. 실제정서정보우월성은보이지않았다.
5. **뇌가표상하나AI가놓칠수있는것은?** E3: 신뢰 가능한개인별 변동,표현학습에서억제된짧은transient,피질 모델밖의신호. 존재여부부터실측 신뢰도로검증해야한다.
6. **다른분야방법의전이는?** E3: 마스크예측의조건부정보,latentprediction의추상화,SSM의입력 의존상태 선택,공통token에서의조건부분해.
7. **기존자료의새 질문은?** E3: 원자료가충분하면분류가아닌사전학습정보소실·시간 변환민감도·조건부 모형불일치를검사할수있다. 네우선데이터셋의원시시계열·반복·정렬·annotation실재는미확인이다.
8. **결과가신경계산이해를바꾸는가?** E3: 선택적정보소실이반복재현되면정서 관련신경성분을예측가능한공유구조와희소변동중어디에놓아야하는지제약한다. 순위차이만나오면benchmark이며해석적기여가약하다.

## 다음 단계의 구체적 후보와중단조건

1. **정보보존후보**: 같은 신경자료에서rawridge·미학습encoder·CortexMAE-P/F/V·JEPA를고정 probe로비교. 일차질문은신뢰도 높은정서 관련잔여분산의소실여부. MRI공간·시간축과사전학습 중복을먼저감사한다. 유효신호/noiseceiling없으면중단.
2. **조건부불일치후보**: TRIBE자극예측과brainblock예측을cross-fit하고잔차를새 피험자·자극으로검증. semantic/low-level/motion/FIR통제후차이없으면“정서고유잔차”가설기각. encoding상관을인과성으로확대하지않음.
3. **상태 선택후보**: Brain-Mamba원리를고정SSM·selectiveSSM으로독립비교. 공식 코드404로즉시실행우선순위는낮음. 순서·HRF·신호 품질대조로설명되면장기통합가설기각.

이 단계에서는Horikawa/Emo-FilM/Spacetop/NSD에위후보를확정배정하지않았다. continuous시계열이없는자료에는temporalfoundation입력을인위적으로만들지않는다. beta-map의trial순서를연속BOLD처럼취급하는전이는금지한다. 데이터 감사후각자료의가능/추가annotation/외부자료/불가능을판정해야한다.

완료: 독립서지 10편, 공식 코드범위검증,원문 1편Discussion검증,모델카드,필수5/5/5/3/3/3/8항목. 미완료: 나머지 9편본문,BrainLM서지,가중치 실행,정확GPU견적,fullcorpus오염감사,새 질문역선행검색,교차Agent토론. 이보고서는Round1이며후속토론을실행했다고주장하지않는다.
