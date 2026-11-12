#!/usr/bin/env python3
"""최종 문서 감사의 실제 원본·해시를 묶는다. 실험 성공을 인증하지 않는다."""
import json,hashlib
from pathlib import Path
from datetime import datetime,timezone
r=Path(__file__).resolve().parents[1]
closure=json.loads((r/'agents/01_dataset/final_pilot_audit_closure.json').read_text())
assert closure['overall']['document_audit_closed'] and closure['overall']['pending_count']==0
science=json.loads((r/'agents/12_adversarial_review/final_audit_round2.json').read_text())
files=sorted((r/'agents').glob('*/proposal_RP*.json'))+sorted((r/'agents').glob('*/pilot_PILOT*.json'))
record={'assembled_at':datetime.now(timezone.utc).isoformat(),'status':'문서 감사 지적의 수정 확인 완료','scope':'원문 확인 범위·과학 질문 중복/주장·자료/통계/자원 실행 계약. 실제 신경효과·모델 실행·전역 신규성 인증 아님','scientific_audit_source':'agents/12_adversarial_review/final_audit_round2.json','scientific_audit_judgment':science['overall_judgment'],'pilot_closure_source':'agents/01_dataset/final_pilot_audit_closure.json','pilot_closure':closure['overall'],'final_question_curation':'research_questions/final_curation.json','artifact_hashes':{p.relative_to(r).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}}
(r/'synthesis/final_audit_resolution.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'final_cards':10,'pilot_plans':3,'pilot_contract_findings_resolved':closure['overall']['resolved_count']},ensure_ascii=False))
