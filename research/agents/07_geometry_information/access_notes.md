# 접근 및 검증 기록

- 작성/확인: Agent07, 2026-11-12. 출처: 실제 도구 응답, 공식 파일들. 신뢰도: 직접 관찰 높음. 후속: 학술 도메인 접근이 확대되면 미확인 본문/최신 선행검증.
- 실행 환경 정책을 확인했다. 공식 GitHub 및 raw.githubusercontent.com에 대한 일반 HTTPS 요청을 사용했다. 정책 우회, 외부 검색 프록시, 전체 출판사 저장소 다운로드는 하지 않았다.
- Python `requests`는 설치되어 있지 않아 첫 조회가 ModuleNotFoundError로 실패했다. 이후 Python 표준 `urllib.request`를 사용했다. 별도 패키지 설치 없음.
- 공식 PMLR 저장소의 이전 권은 `gh-pages/{논문ID}/{논문ID}.pdf`, v48은 `gh-pages/peyre16.pdf`, v235는 metadata가 지정한 `main/assets/huh24a/huh24a.pdf`를 사용했다. DOI/arXiv를 기억으로 채워 넣지 않았다. DOI가 없는 PMLR 행은 공식 URL로 식별했다.
- 실제 404: v97 `gh-pages/assets/kornblith19a/kornblith19a.pdf`, v97 `main/assets/kornblith19a/kornblith19a.pdf`, v97 `tree/gh-pages/assets`; v235 `tree/main/_posts`; GitHub `rubenrubenruben/Intrinsic-Dimension-of-DNNs`, `ansuini/IntrinsicDimension`, `dmelis/gromov-wasserstein`; scikit-dimension `master/README.rst`, `master/doc/references.bib`. 이는 URL 추정 실패이며 논문 부존재의 증거가 아니다. 공식 트리/실재 파일에서 후속 경로를 검증했다.
- 상위 작업자가 보고한 arXiv/Crossref 403은 이 Agent가 재시험하지 않았다. 따라서 이 폴더의 직접 검증 접근실패로 새 집계하지 않는다.
- 성공 다운로드의 URL·로컬경로·바이트수·SHA256·근거범위는 `sources_manifest.csv`에 있다. HTML 탐색 캐시는 최종 근거가 아니므로 제거했다. PDF 텍스트는 `pdftotext -layout`으로 추출했다.
- 본문 7편: 관련 본문/정리/결론/한계를 직접 읽었다. 모든 부록·증명을 전수 정밀검토한 것은 아니다. 텍스트의 수식 추출 오류가 있어 정리의 조건과 주장을 제한적으로 요약했다.
- 코드/문서 3편: PID·scikit-dimension·RSA 도구. 현 코드 검토를 논문 본문 확인이나 결과 재현으로 주장하지 않는다. 어떤 모델·분석도 실행하지 않았다.
- PID README의 상단 저자 목록에는 Nicholas Allen/Randy Auerbach가 있으나 BibTeX에는 없다. 전체 저자명 확정은 보류했다. 제목·연도·venue·arXiv 식별자는 공식 README에 있다.
- RSA CITATION.cff의 소프트웨어 release 정보와 preferred-citation 논문 날짜는 다르다. 논문은 preferred-citation의 2025 preprint로 기록했고 최종 출판본 존재는 확인하지 않았다.
- Facco TWO-NN 저자 코드도 확보했지만 별도 논문 전체 검증 행으로 추가하지 않았다. ID 축은 공식 scikit-dimension 문서/코드를 근거로 삼았다. 현재 코드의 후속 MLE 기능을 2021 논문 주장으로 소급하지 않았다.
