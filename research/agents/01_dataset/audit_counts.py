from pathlib import Path
import json,csv,collections,re
r=Path(__file__).parent/'evidence';out={}
for name in ['ds002425','ds004892','ds005256']:
 tree=(r/'repos'/f'{name}_tree.txt').read_text().splitlines();raw=[p for p in tree if p.startswith('sub-')]
 subjects=sorted(set(p.split('/')[0] for p in raw));tasks=collections.Counter(re.search(r'_task-([^_]+)',p).group(1) for p in raw if '_task-' in p and p.endswith('_bold.nii.gz'))
 out[name]={'subject_count_tree':len(subjects),'subjects':subjects,'bold_paths_per_task':dict(tasks)}
 print(name,len(subjects),dict(tasks))
for subj in sorted((r/'ds002425').glob('sub-*')):
 fs=list(subj.rglob('*events.tsv'));rows=[row for f in fs for row in csv.DictReader(f.open(),delimiter='\t')];st=[x for x in rows if x['trial_type']=='1'];ids=[x['stim_index'] for x in st];names=[x['stimulus_name'] for x in st]
 data={'event_files':len(fs),'stimulus_rows':len(st),'unique_stim_index':len(set(ids)),'unique_stimulus_name':len(set(names)),'duration_counts':dict(collections.Counter(x['duration'] for x in st)),'sessions':dict(collections.Counter(f.parts[-3] for f in fs)),'repeated_stim_index':{k:v for k,v in collections.Counter(ids).items() if v>1},'fields':list(rows[0])}
 out[subj.name]=data;print(subj.name,json.dumps(data))
for n in ['ds004872','ds004892','ds005256']:
 p=r/n/'participants.tsv';rows=list(csv.DictReader(p.open(),delimiter='\t'));print(n,'participants',len(rows),'fields',list(rows[0]));out.setdefault(n,{}).update(participant_rows=len(rows),participant_fields=list(rows[0]))
(r/'derived_audit_counts.json').write_text(json.dumps(out,indent=2))
for p in [*list((r/'ds002425').rglob('*bold.json')),*list((r/'ds004892').rglob('*bold.json')),r/'ds005256/task-alignvideo_acq-mb8_bold.json']:
 j=json.loads(p.read_text());print(str(p),{k:v for k,v in j.items() if k in ['RepetitionTime','EchoTime','Manufacturer','ManufacturersModelName','MagneticFieldStrength','SliceThickness','SpacingBetweenSlices','MultibandAccelerationFactor','TaskName','TaskDescription']})
