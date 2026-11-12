# 외부 접근 기록

기준일 2026-11-12. 기존 proxy 및 CA를 그대로 사용했다. 정책 우회나 자격증명 출력 없음.

| 요청 | 결과 | 해석 |
|---|---|---|
| https://api.crossref.org/works?query.title=Horikawa%20emotion&rows=1 | Tunnel connection failed: 403 Forbidden | 환경 정책에 목적지 미허용 |
| https://arxiv.org/abs/2305.08790 | Tunnel connection failed: 403 Forbidden | 환경 정책에 목적지 미허용 |
| https://raw.githubusercontent.com/MedARC-AI/MindEyeV2/main/README.md | HTTP 200 | 공식 README 접근 가능 |
| https://github.com/search?q=Horikawa+emotion&type=repositories | HTTP 200 | 저장소 검색 페이지 접근 가능; 결과 부재는 논문 부재 증거가 아님 |

환경 상태: observations_current=true, network_policy.state=enforced, restricted. 학술출처 허용 초안 저장 응답 status=saved, requires_publish=true. 이 초안은 적용/게시 전이며 접근 가능해졌다고 간주하지 않는다.
