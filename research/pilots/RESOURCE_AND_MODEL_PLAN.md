# 실행 환경과 공통 모델 경로

2026-11-12 실제 환경 관측은 environment_observation.json에 기록했다. CPU 노출5개이나 cgroup quota는4 CPU분량이고 memory.max는32GiB다. nvidia-smi는 없으며 GPU 추론을 실행하지 않았다. 이 사실은 사용자의 다른 장비·클라우드 자원까지 없다는 뜻은 아니다.

## 첫 검정의 비용을 분리

첫 단계는 보유 자료의 작은 부분과 **이미 추출된 특징**으로 split·관측정렬·baseline·반증 대비를 점검한다. 특징 추출과 신경모형 적합 비용을 분리한다. 원본 영상·fMRI·전체 checkpoint를 사용자 컴퓨터에 받도록 요구하지 않는다.

N개 관측, K개 float32 특징의 저장량은 `4*N*K`바이트다. 예를 들어 N=2,196,K=1,024는 약8.58MiB이고, N=20,000,K=1,024는 약78.13MiB다. 이는 특징행렬 한 개의 산술 견적이며 원본 영상·voxel 행렬·교차검증 복사본·모델 activation 메모리는 포함하지 않는다. 실제 array shape를 확인하여 총량을 다시 계산한다. voxel/시간 블록 단위 처리와 feature cache를 사용한다.

## 구체적으로 식별한 가벼운 시각 기준모형

- 모델: OpenAI CLIP **ViT-B/32**. [공식 loader](https://github.com/openai/CLIP/blob/main/clip/clip.py), [구조](https://github.com/openai/CLIP/blob/main/clip/model.py), [LICENSE](https://github.com/openai/CLIP/blob/main/LICENSE).
- 공식 loader의 체크포인트: `https://openaipublic.azureedge.net/clip/models/40d365715913c9da98579312b702a82c18be219cc2a73407c4526f58eba950af/ViT-B-32.pt`.
- loader가 요구하는 SHA256: `40d365715913c9da98579312b702a82c18be219cc2a73407c4526f58eba950af`. 링크·해시 규칙·MIT 코드 라이선스를 직접 확인했고, 소스 해시를 model_evidence/manifest.json에 저장했다. **가중치 다운로드·load·추론 성공은 미확인**이다.
- 가중치가 보유 캐시에 있으면 실제 해시를 검증하고 작은 입력1개로 shape·수치·peak memory를 측정한다. 없으면 허용된 실행 환경에서 해당 공식 checkpoint를 준비한다. GPU 최소 VRAM·벽시계시간을 측정 전 확정하지 않는다. CPU에서도 실행 경로는 가능하지만 전체 영상 처리의 실용 속도를 보장하지 않는다.

CLIP의 의미/정서 점수는 측정 정서 주석이 아니다. pretraining corpus의 자극 중복을 완전히 배제했다고 주장하지 않는다. 모델 identity와 체크포인트를 고정한 후 특징 추출 버전·frame sampling·normalization을 기록한다.

## 고비용 확장은 첫 baseline 이후 판단

V-JEPA2·ImageBind·CortexMAE·TRIBE v2·MindEye2의 공식 코드·checkpoint 연결과 입출력·라이선스 범위는 각 역할 모델 카드에 있다. 공개 링크가 있다고 바로 Horikawa 입력과 호환되는 것은 아니다. 서로 다른 backbone을 비교한 결과만으로 학습목표의 인과 효과를 주장하지 않는다.

첫 baseline이 충분하거나 신뢰도가 낮아 경쟁모형을 구분할 수 없으면 더 큰 모델 학습을 중단한다. frozen feature·작은 readout으로 판별 가능성을 확인한 뒤, 동일 입력·용량·선택 예산의 비교가 필요한 후보에만 확장한다. 인용된 GPU 구성은 원 연구의 실행 예시이며 본 환경의 최소 요구량으로 치환하지 않는다.
