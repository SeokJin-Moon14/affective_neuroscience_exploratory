<div align="center">
  <h1><strong>Multigranular Evaluation for Brain Visual Decoding</strong></h1>
  <p>
    <a href="https://www.cst.cam.ac.uk/people/wx258" target="_blank">Weihao Xia</a>&emsp;
    <a href="https://sites.google.com/view/cengiz-oztireli-intro/home" target="_blank">Cengiz Oztireli</a>
    <br>
    University of Cambridge
    <br>
    <strong>AAAI 2026</strong>
  </p>
</div>

<div id="top" align="center">
<p>
  <a href="https://aaai.org/conference/aaai/aaai-26/" target="_blank"><img src="https://img.shields.io/badge/AAAI-2026-4B96DC?style=flat&logo=aiqfome&logoColor=white" alt="AAAI 2026"></a>
  <a href='https://arxiv.org/abs/2507.07993' style='padding-left: 0.5rem;'><img src='https://img.shields.io/badge/arXiv-2507.07993-A42C25?style=flat&logo=arXiv&logoColor=white'></a>
  <img src="https://visitor-badge.laobi.icu/badge?page_id=weihaox/BASIC" style="padding-left: 0.5rem; height: 20px;" alt="visitor badge"/>
  <a href="https://opensource.org/licenses/Apache-2.0" style="padding-left: 0.5rem;">
    <img src="https://img.shields.io/badge/License-Apache_2.0-7B61FF?style=flat&logo=apache&logoColor=white" alt="Apache License 2.0">
  </a>
</p>

</div>

## 📰 News
- **`2025/11/15`** 🌟 **Codes** are released.
- **`2025/11/08`** 🚀 **BASIC** is accepted to [AAAI 2026](https://aaai.org/conference/aaai/aaai-26/) in Singapore.

------------------------------------------------------------------------

## 🎯 Introduction

### Why Existing Evaluation Protocols Fall Short

Current evaluation protocols are limited in:

1. **Discriminative power**:  metrics often saturate and fail to reveal meaningful differences.
2. **Neuroscientific grounding**: they poorly capture perceptual plausibility or human-like alignment.
3. **Visual cognition coverage**: they overlook the multi-level nature of visual understanding.

### Our Method: BASIC

We introduce **BASIC** (**B**rain-**A**ligned **S**tructural, **I**nferential, and **C**ontextual similarity), a discriminative, interpretable, and comprehensive framework designed to fill key gaps in brain visual decoding evaluation. BASIC combines semantic reasoning and structural matching to measure how closely decoded outputs align with reference stimuli across multiple levels.

<div align="center"><tr>
    <img src="docs/overview.png" width="100%"/>
</tr></div>

BASIC evaluates decoding from three complementary perspectives:
1. **Structural**: measures spatial organization and category boundaries using granularity-aware correspondence.
2. **Inferential**: assesses semantic accuracy via object categories, attributes, and relations from MLLM captions.
3. **Contextual**: evaluates global plausibility via MLLM-based scene reasoning, quantifying narrative coherence.

------------------------------------------------------------------------

## ⚙️ Usage

The visual decoding results should be structured as follows:

```text
res_decoding
├── cc2017
│   ├── decofuse
│   ├── mind-video
│   └── neuroclips
├── eeg-neuro3d
│   └── neuro3d
├── eeg-things
│   ├── atm
│   ├── cognitioncapturer
│   └── images
├── fmri-shape
│   ├── images
│   ├── mind3d
│   └── mind3d++
├── nsd
│   ├── braindiffuser
│   ├── brainguard
│   ├── dream
│   ├── images
│   ├── mindbridge
│   ├── mindeye
│   ├── mindeye2
│   ├── mindtuner
│   ├── neuropictor
│   ├── sdrecon
│   ├── sepbrain
│   ├── sttm
│   ├── test_images
│   ├── umbrae
│   ├── unibrain
│   └── neurovla
└── seed-dv
```

Download [LLaVA](https://github.com/haotian-liu/LLaVA) checkpoints into `detailcap/llava/model_weights`.

```python
# git lfs install
ckpt = 'llava-v1.5-7b' # 'llava-v1.5-13b', 'llava-next-vicuna-7b', 'llava-next-vicuna-13b'
from huggingface_hub import snapshot_download
snapshot_download(repo_id=f"liuhaotian/{ckpt}", local_dir=ckpt)
```

------------------------------------------------------------------------

### BASIC-H: Semantic Reasoning

#### 1. Generate Detailed Captions

```bash
# Step 1: Generate detailed captions for GT images and decoded images
models=("llava-v1.5-7b") # "llava-v1.5-13b" "llava-next-vicuna-7b", "llava-next-vicuna-13b", "llava-next-34b")

methods=(
    "nsd/images"
    "nsd/sdrecon/sub01"
    "nsd/braindiffuser/sub01"
    "nsd/mindeye/sub01"
    "nsd/umbrae/sub01"
    "nsd/dream/sub01"
    "nsd/mindbridge/sub01"
    "nsd/mindeye2/sub01"
    "nsd/neurovla/sub01"
    "nsd/sepbrain/sub01"
    "nsd/unibrain/sub01"
    "nsd/brainguard/sub01"
    "nsd/neuropictor/sub01"
)

for model in "${models[@]}"; do
    for method in "${methods[@]}"; do
  echo "Processing model: $model, data: $method"
  python detailcap/generate_detailed_image_caption.py --model_path "detailcap/llava/model_weights/${model}"  --prompt detailcap/prompts/basic.txt \
      --data_path "res_decoding/${method}" --save_path "res_decoding/captions/${model}/${method}" \
  done
done
```

#### 2. Evaluate Detailed Captions

```bash
# Step 2: Evaluate the detailed captions
for model in "${models[@]}"; do
    refs="res_decoding/captions/${model}/nsd/images/fmricap.json"
    for method in "${methods[@]}"; do
    if [ "$method" == "nsd/images" ]; then
        echo "Skipping evaluation for GT data: $method"
        continue
    fi
    echo "Evaluating model: $model, data: $method"
    preds="res_decoding/captions/${model}/${method}/fmricap.json"
    python capture/eval_detailcap.py "${refs}" "${preds}" --is_strict True
    done
done
```

> [!NOTE]
> Set `is_strict = False` when performing [VINDEX](https://github.com/weihaox/VINDEX) evaluation.


### BASIC-L: Structural Matching 

#### 0. Environment & Code

Download codes and pretrained models from [IDEA-Research/Grounded-SAM-2](https://github.com/IDEA-Research/Grounded-SAM-2), and follow the official instructions for environment setup.

```bash
cd basic/grounded-sam2
git clone https://github.com/IDEA-Research/Grounded-SAM-2
```
#### 1. (Optional) Generate Hierarchical Class Captions

We provide processed hierarchical categories in `grounded-sam2/hierarchical_classes`.

```bash
# Step 1: Generate hierarchical class captions for images
model="llava-next-vicuna-13b"
for data in "nsd/images"
do
python detailcap/generate_detailed_image_caption.py --model_path "detailcap/llava/model_weights/${model}" \
    --data_path "res_decoding/${data}" --save_path "res_decoding/captions/${model}/${data}/hierarchical_classes" \
    --prompt detailcap/prompts/hierarchical_class.txt
done
```

#### 2. Generate Multigranular Segmentation Masks

```bash
# Step 2: Generate multigranular segmentation masks based on the hierarchical classes
prompt_path='basic/grounded-sam2/hierarchical_classes/nsd/class_dict.json'

methods=(
    "nsd/images"
    "nsd/sdrecon/sub01"
    "nsd/braindiffuser/sub01"
    "nsd/mindeye/sub01"
    "nsd/umbrae/sub01"
    "nsd/dream/sub01"
    "nsd/mindbridge/sub01"
    "nsd/mindeye2/sub01"
    "nsd/neurovla/sub01"
    "nsd/sepbrain/sub01"
    "nsd/unibrain/sub01"
    "nsd/brainguard/sub01"
    "nsd/neuropictor/sub01"
)

tth=0.3 
bth=0.25

for data in "${methods[@]}"; do
    echo "Processing $data with box threshold $bth and text threshold $tth"
    python batch_process_grounded_sam2_hierclass.py --text-prompt-path $prompt_path \
        --img-path "res_decoding/${data}" --output-dir "res_decoding/${data}_b${bth}_t${tth}_hierarchical_llava" \
        --box-threshold $bth --text-threshold $tth --img-size 512
done
```

#### 3. Evaluate Segmentation Masks

```bash
# Step 3: Evaluate the segmentation masks
methods=("sdrecon" "braindiffuser"  "mindeye" "umbrae" "dream" "mindbridge" "mindeye2" "neurovla" "sepbrain" "unibrain" "brainguard" "neuropictor")

for method in "${methods[@]}"; do
    echo "Calculating matching ratio for method: $method (bth=$bth, tth=$tth)"
    python cal_hierarchical_matching_ratio_ap.py --dataset nsd --method "$method" --thbox "$bth" --thtxt "$tth"
done
```

------------------------------------------------------------------------

## 📚 Acknowledgements

The codebase is built upon the following excellent projects: [LLaVA](https://github.com/haotian-liu/LLaVA), [CAPTURE](https://github.com/foundation-multimodal-models/CAPTURE) and [Grounded SAM](https://github.com/IDEA-Research/Grounded-Segment-Anything).

We also highlight a series of our works on multimodal brain decoding and benchmarking:
- **[DREAM](https://github.com/weihaox/DREAM)**: mirrors pathways in the human visual system for stimulus reconstruction.
- **[UMBRAE](https://github.com/weihaox/UMBRAE)**: interprets brain activations into multimodal explanations with task-specific MLLM prompting.
- **[VINDEX](https://github.com/weihaox/VINDEX)**: explores the impact of different image feature spaces on fine-grained multimodal decoding.
- **[MEVOX](https://cvpr25-advml.github.io/short_paper/21_Multi_Task_Vision_Experts_.pdf)**:  introduces Multi-Expert Vision systems for Omni-contextual eXplanations.
- **[BASIC](https://github.com/weihaox/BASIC)**: provides interpretable and multigranular benchmarking for brain visual decoding.

## 📖 Citation

```bibtex
@inproceedings{xia2026basic,
  title     = {Multigranular Evaluation for Brain Visual Decoding},
  author    = {Xia, Weihao and Öztireli, Cengiz},
  booktitle = {AAAI Conference on Artificial Intelligence (AAAI)},
  year      = {2026},
}
```