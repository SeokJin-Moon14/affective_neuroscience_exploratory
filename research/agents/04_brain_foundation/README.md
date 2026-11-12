# Agent04 1차 독립조사 산출물

담당: Brain Encoding & Brain Foundation Models. 확인일: 2026-11-12. 독립조사 완료 범위는 아래와 같으며 후속 검증이 남아 있다.

- `round1_report.md`: 계산 원리, 숨은 가정 3개, 미해결 문제 5개, 기회 5개, 전이 5개, 예상 밖 연결 3개, 새 Sub-axis 3개, 필수 8질문 및 강한 반론.
- `papers.csv`: 고유 서지 10편, 미션 필수30열 + source/needs_followup 총32열. E1의 확인 범위를 각 행에 명시.
- `model_cards.md`: 주요 모델의 정확한 실체·코드·가중치·학습자료·입출력·해상도·라이선스·컴퓨팅 확인과 부족분. BrainLM은 코드 확인만 하고 서지 집계에서 제외.
- `discussion_mining.csv`: Brain-Mamba Appendix E에서 직접 확인한 저자 후속 방향5개와 Agent 전이를 분리.
- `subaxes.csv`: 12개 등록필드가 있는 독립 후보3개.
- `source_manifest.csv`, `sources/`: 원본 URL·접근 상태·다운로드 원본·SHA256·관측 Git commit. 실패도 보존.
- `validation.json`: 실제 CSV 구조 검증 결과. 설치·추론·학습은 실행하지 않았다.

원문·부록 확인은 Brain-Mamba 1편이다. 나머지9편은 공식 README/일부 코드의 서지·구현 범위를 검증했으며 논문 결과·Discussion을 읽었다고 간주하지 않는다. arXiv/HuggingFace 접근403, Brain-Mamba 공식 코드404, 일부 GitHub 검색429를 확인했다. 후속 작업은 나머지 본문/Discussion, BrainLM 1차서지, checkpoint 다운로드 및 실행, 실제 데이터 입력 적합성·사전학습 중복·신규성 역검색이다.

EmoBrain과 다른 Agent 결과를 읽지 않았고 공통 통합파일을 수정하지 않았다. 모든 작성 범위는 `agents/04_brain_foundation/`이다.
