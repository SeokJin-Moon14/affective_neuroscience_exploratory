# 출처 기록 읽는 법

`source_manifest.csv`가 파일별 원본 기록이다. `sources/fetch_log.json`은 요청 URL·성공/실패·바이트 수를 보존한다. 공식 저자 저장소, 출판사 mlresearch의 권별 저장소, OpenNeuro 공식 데이터 저장소만 근거로 채택했다. 네트워크 프록시·CA 설정은 변경하지 않았다.

원본은 변동 가능한 main/master/gh-pages에서 받은 확인일 저장본이며 SHA256으로 고정했다. 원본 저장소의 현재 HEAD와 논문 당시 실험 버전이 동일하다는 주장은 하지 않는다. 특히 LLaVA 현행 README·코드는 후속 버전 설정을 포함한다.

PDF4편은 접근 가능했지만 선택 절만 직접 검토했다. 본문 확인 범위는 manifest의 `reviewed_location`에 있다. 다운로드만 한 부분을 검토했다고 세지 않는다. 공식 코드 E1과 논문 결과 E1을 분리한다. 논문 본문 미열람 6편의 Discussion 미래 과제를 저자에게 귀속하지 않는다.

`*_paper.txt`는 pdftotext로 생성한 검색용 텍스트, `*_methods_excerpt.txt`는 PDF의 선택 페이지 추출, `scaling_notebook_text.txt`는 notebook의 코드/markdown 셀을 추출한 파생 파일이다. 원본 파일의 해시는 CSV에 있으며 파생 파일은 논문별 원본으로 역추적할 수 있다. scaling notebook의 audio/stacked 분기는 연구 근거·제안에 채택하지 않았으며 별도의 speech feature 추출 파일은 열람·실행하지 않았다.

공식 자료의 긴 본문과 코드 사본은 검증 재현용 `sources/`에만 보존했다. 최종 보고서는 짧은 한국어 요약·위치·링크를 제공한다. 모델·노트북·원저자 스크립트는 실행하지 않았다. `build_tables.py`는 기록을 CSV로 직렬화하는 로컬 산출물 생성 스크립트다.
