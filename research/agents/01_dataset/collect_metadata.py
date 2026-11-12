from pathlib import Path
from fetch import fetch
import subprocess,concurrent.futures,json
root=Path(__file__).parent/'evidence/repos'
selected={}
for repo,owner in [('ds002425','OpenNeuroDatasets'),('ds004872','OpenNeuroDatasets'),('ds004892','OpenNeuroDatasets'),('ds005256','spatialtopology'),('nsdexamples','cvnlab'),('nsddatapaper','cvnlab')]:
 files=(root/(repo+'_tree.txt')).read_text().splitlines();sha=subprocess.check_output(['git','-C',str(root/repo),'rev-parse','HEAD'],text=True).strip()
 take=[x for x in files if x in ['README','README.md','dataset_description.json','participants.json','participants.tsv']]
 if repo=='ds002425':take += [x for x in files if x.endswith('_events.tsv')]+[x for x in files if x.endswith('_bold.json')][:1]
 if repo=='ds004872':take += [x for x in files if x in ['derivatives/Annot_AfterTheRain_stim.json','sub-area/beh/sub-area_task-AfterTheRain_recording-Anxiety_stim.json']]
 if repo=='ds004892':take += [x for x in files if x.startswith('sub-S01/ses-1/') and ('BigBuckBunny' in x and x.endswith(('.tsv','.json')))]+['code/FilmInfo.txt']
 if repo=='ds005256':
  take += [x for x in files if '/' not in x and x.endswith('.json')]
  for task in ['alignvideo','shortvideo','fractional','narratives','faces','social']:
   take += [x for x in files if x.endswith('_events.tsv') and ('task-'+task+'_') in x][:1]
 if repo=='nsdexamples':take += [x for x in files if x.startswith('matlab/example') and x.endswith('.m')]
 if repo=='nsddatapaper':take += [x for x in files if x in ['main/nsd_setup.m','main/export_noiseceiling.m','main/autoqc_acquisition.m','main/preprocess_nsd.m','main/analysis.m']]
 for p in take:selected[repo+'/'+p]='https://raw.githubusercontent.com/'+owner+'/'+repo+'/'+sha+'/'+p
(Path(__file__).parent/'evidence/metadata_selection.json').write_text(json.dumps(selected,indent=2))
res=list(concurrent.futures.ThreadPoolExecutor(max_workers=6).map(lambda x:fetch(*x),selected.items()))
from collections import Counter
print('선택 파일:',len(res),'상태:',dict(Counter(str(x['status']) for x in res)))
