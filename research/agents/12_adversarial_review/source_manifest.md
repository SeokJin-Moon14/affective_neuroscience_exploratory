# 출처 접근·검증 범위

검증일: 2026-11-12. 담당: Agent12. 자세한 URL·로컬 파일·SHA-256·검토 위치·실패 사유는 `source_manifest.csv`에 있다.

## 논문 집계

| 구분 | 수 | ID |
|---|---:|---|
| 공식 논문 본문 직접 확인 | 5 | A12-P03, P05, P08, P09, P10 |
| 저자 공식 코드/문서 직접 확인; 논문 본문 미확인 | 3 | A12-P04, P06, P07 |
| 공식 구현팀 인용 서지만 확인(E2) | 1 | A12-P01 |
| 서지 보완 필요, 위 9편에서 제외 | 1 | A12-P02 |

E1은 확인한 내용에만 적용한다. 공식 코드의 존재는 논문 실험 성능이나 Discussion의 확인을 뜻하지 않는다. 공식 구현팀의 서지는 원저자 직접 출처와 구별한다. P02의 코드 동작은 E1 보조 근거로 사용할 수 있지만 논문 저자 순서가 미확인인 상태에서 검증 논문 수를 늘리지 않는다.

PMLR 4편은 출판사 `mlresearch`의 권별 공식 GitHub에서 metadata와 PDF를 받았다. Schütt2023은 출판사 `elifesciences/elife-article-xml`의 정식 XML을 받았다. 본문·Discussion 검토 위치는 `papers.csv`의 `source_location`, `future_direction_source_location`을 참조한다.

## 접근 기록

53개 URL 취득 시도를 보존했다. 성공 42건은 논문 수가 아니라 문서·코드·metadata·탐색 페이지를 포함한 URL 수다. 나머지 11건에는 추정 경로 404와 JMLR 출판사 PDF의 프록시 CONNECT 403이 포함된다. 404는 해당 문헌이 존재하지 않는다는 증거가 아니다. 차단된 출처를 허용된 출처로 가장하거나 프록시를 우회하지 않았다.

원문 내려받기와 `pdftotext` 변환, XML 텍스트 추출을 수행했다. 다운로드한 코드·Matlab 분석·신경모델은 실행하지 않았다. 저장소 전체를 복제하지 않고 필요한 파일을 개별 취득했다. mutable branch 파일은 확인일과 파일 해시를 남겼으며, 모든 저장소에 대해 commit pinning을 완료한 것은 아니다. DomainBed의 2020 README는 명시된 commit을 사용했다.

## 확정 집계에 사용하지 않은 자료

- MVCA: 공식 코드와 2018 preprint 링크는 확인했지만 저자 순서·최종 논문 서지는 보완이 필요하다. `pending_papers.csv`에 있다.
- Diedrichsen 등의 whitened RDM 논문: 공식 README의 2021 표기와 Schütt 참고문헌의 2020 표기가 달라 추가 확인이 필요하다. 이번 확정 문헌에 넣지 않았다.
- Varoquaux small-sample CV 저장소: 공식 코드는 확보했지만 논문 서지를 직접 충분히 확인하지 못하여 확정 목록에 넣지 않았다.
- 기타 GitHub 조직·저자 페이지: 출처 경로 탐색에만 사용했고 논문 내용 증거로 세지 않았다.

## 남은 검증

1. P01 원문과 P02 정식 서지·논문 본문 확인.
2. P04/P06/P07의 논문 본문·Discussion을 공식 코드와 대조.
3. 후보별 가장 가까운 정서 선행연구 역검색. 현재 E3 제안을 독창성이 입증된 결과로 볼 수 없다.
4. Horikawa 우선으로 실제 stimulus/run/subject/repetition 단위, annotation, 신뢰도 자료와 평가 설계를 대조. 이 Agent는 dataset metadata를 직접 조사하지 않았다.
5. Coordinator 지시 후 실제 교차 검토. 현재 타 Agent 결과·EmoBrain 미열람 상태다.
