<div align="center">

<h2>Exploring The Visual Feature Space for Multimodal Neural Decoding (ICCV 2025)</h2>

<div>
    <a href='https://weihaox.github.io/' target='_blank'>Weihao Xia</a>&emsp;
    <a href='https://sites.google.com/view/cengiz-oztireli-intro/home' target='_blank'>Cengiz Öztireli</a>
</div>
<div>
    University of Cambridge
</div>

<br/>

<p align="center">
<!-- <a href="https://pytorch.org/get-started/locally/"><img alt="PyTorch" src="https://img.shields.io/badge/PyTorch-ee4c2c?logo=pytorch&logoColor=white"></a> -->
<!-- <a href="https://arxiv.org/abs/2505.15755" target="_blank" rel="noopener noreferrer"><img src="https://img.shields.io/badge/Paper-VINDEX" alt="Paper PDF"></a> -->
<a href="https://iccv.thecvf.com/" target="_blank"><img src="https://img.shields.io/badge/ICCV-2025-4b96dc" alt="ICCV 2025"></a>
<a href="https://arxiv.org/abs/2505.15755" target="_blank"><img src="https://img.shields.io/badge/arXiv-2505.15755-b31b1b" alt="arXiv"></a>
<a href="https://weihaox.github.io/VINDEX" target="_blank"><img src="https://img.shields.io/badge/Project_Page-green" alt="Project Page"></a>
<a href="https://huggingface.co/datasets/weihaox/vindex/tree/main" target="_blank"><img src="https://img.shields.io/badge/Hugging%20Face-blue" alt="Hugging Face"></a>
</p>

</div>

<p>UMBRAE aligns brain activations with image features for zero-shot captioning and grounding. We further explore the impact of different image feature spaces on fine-grained multimodal decoding, drawing inspiration from prior MLLM research that uses diverse features. We also introduce a metric to effectively evaluate detailed open-vocabulary brain-based descriptions.</p>

## News :triangular_flag_on_post:
- [2025/07/10] Codes and pretrained models are released.
- [2025/06/26] VINDEX is accepted to [ICCV 2025](https://iccv.thecvf.com) at Hawaii.
- [2025/05/21] Both <a href="https://weihaox.github.io/VINDEX">project</a> and <a href="https://arxiv.org/abs/2505.15755">preprint</a> are available.

## Method

We investigate four types of image feature spaces: (a) **Single Encoder** (SE): uses features from a single pre-trained vision encoder (e.g., CLIP) for brain alignment—commonly used in MLLMs.; (b) **Mixture of Encoders** (ME): integrates features from multiple task-specific vision experts such as CLIP and DINO; (c) **Aggregated Feature** (AF): combines dense features from various layers (shallow, middle, and deep) to capture different image characteristics.; (d) **Nested Features** (NF): uses a variable-length set of visual tokens, downscaled using multiple downsampling factors to produce a hierarchical, nested representation—encoding visual content from coarse to fine-grained details.

<div align="center"><tr>
    <img src="docs/images/feature_space.png" width="90%"/>
</tr></div>

## Installation 

### Environment

Same environment as UMBRAE. Please use it directly if already set up; otherwise, install with following commands:

```bash
conda create -n vindex python=3.10
conda activate vindex
pip install -r requirements.txt
```

### Download Data and Checkpoints

The training and inference scripts support automatically downloading the dataset if the designated path is empty. However, this process can be quite slow. You can try the following script to download all data in advance if this happens. Please fill out the NSD [Data Access form](https://forms.gle/xue2bCdM9LaFNMeb7) and agree to the [Terms and Conditions](https://cvnlab.slite.page/p/IB6BSeW_7o/Terms-and-Conditions). 

Download Checkpoints from [Hugging Face](https://huggingface.co/datasets/weihaox/vindex).

```bash
bash download_data.sh
bash download_checkpoint.sh
```

## Code Structure

```
src
├── llava // Single Encoder (SE)
│   ├── inference_nsd_image.py // image inference
│   ├── inference.py // brain inference
│   └── model_weights // model weights
├── mmvp // Mixture of Encoders (ME)
│   ├── inference_nsd_image.py
│   ├── inference.py
│   └── model_weights
├── denseconnector // Aggregated Feature (AF)
│   ├── inference_nsd_image.py
│   ├── inference.py
│   └── model_weights
├── matryoshka-mm // Nested Features (NF)
│   ├── inference_nsd_image.py
│   ├── inference.py
│   └── model_weights
├── model
│   ├── mm_utils.py
│   ├── model.py
│   ├── multimodal_projector
│   ├── perceiver.py
│   └── utils.py
├── shikra
│   ├── inference.py
│   └── model_weights
├── train_brainx.py // cross-subject training and adaptation
└── train.py //single-subject training
```

## Inference

Inference requires a connection to the backend MLLM. Please ensure that configuration parameters such as `model_name`, `hidden_size`, and `mm_projector_type` are correctly matched. If no errors occur, the system should function properly.

For SE,
```bash
ckpt_name='clip_224' model_name='llava-v1.5-7b' # 'llava-v1.5-13b', 'llava-next-7b', 'llava-next-13b'
hidden_size=4096 # 5120
python src/llava/inference.py --fmri_encoder 'brainxs' --subj 1 \
    --data_path 'nsd_data' --prompt 'Describe this image in detail.' \
    --img_size 224 --feat_dim 1024 --hidden_size ${hidden_size} --mm_projector_type 'mlp2x_gelu' \
    --mllm_path "src/llava/model_weights/${model_name}" \
    --brainx_path "train_logs/specific_sub/sub01_dim1024/${ckpt_name}/last.pth" \
    --save_path "train_logs/evaluation/specific_sub/sub01_${ckpt_name}_dim1024_${model_name}"
```

For ME,
```bash
python src/llava/mmvp/inference.py --fmri_encoder 'brainxs' --subj 1 \
    --data_path 'nsd_data' --prompt 'Describe this image in detail.' \
    --brainx_path 'train_logs/specific_sub/sub01_dim1024' \
    --img_size 224 --feat_dim 1024 \
    --save_path 'train_logs/evaluation/specific_sub/sub01_dim1024/sub01_clip_dino224_dim1024_mmvp'
```

For AF,
```bash
vision_tower='siglip' img_size=384  feat_dim=3456 mm_hidden_size=3456 ckpt_name='siglip_384/epoch500'
mllm_name='dc-llava-v1.5-7b' hidden_size=4096 # mllm_name='dc-llava-v1.5-13b' hidden_size=5120
python src/denseconnector/inference.py  --subj 1 --fmri_encoder 'brainxs' --img_size $img_size  \
    --data_path 'nsd_data' --feat_dim $feat_dim --hidden_size $hidden_size \
    --prompt 'Describe this image in detail.' --mm_hidden_size=$mm_hidden_size \
    --mllm_path "/home/wx258/project/vindex/src/denseconnector/model_weights/${mllm_name}" \
    --brainx_path "train_logs/specific_sub/sub01_dim${feat_dim}/${ckpt_name}/last.pth" \
    --save_path "train_logs/evaluation/specific_sub/sub01_${vision_tower}_${img_size}_dim${feat_dim}_${mllm_name}"
```

For NF,
```bash
# mllm_name: [m3-llava-v1.5-7b, m3-llava-next-7b, llava-next-vicuna-7b-m3, llava-v1.5-vicuna-7b-m3]
# matryoshka_vis_token_scale: [1, 9, 36, 144, 576]
img_size=224 feat_dim=1024 hidden_size=4096 matryoshka_vis_token_scale=1
ckpt_name='clip_224' model_name='m3-llava-next-7b'
python src/matryoshka-mm/inference.py  --subj 1 --img_size $img_size --feat_dim $feat_dim \
    --data_path 'nsd_data' --hidden_size $hidden_size --fmri_encoder 'brainxs' \
    --prompt 'Describe this image in detail.' \
    --brainx_path "train_logs/specific_sub/sub01_dim1024/${ckpt_name}/last.pth" \
    --mllm_path "src/matryoshka-mm/model_weights/${model_name}" --matryoshka_vis_token_scale=$matryoshka_vis_token_scale \
    --save_path "train_logs/evaluation/specific_sub/sub01_${ckpt_name}_dim${feat_dim}_${model_name}_ts${matryoshka_vis_token_scale}"
```

> [!NOTE]
> `<image>` should be included in the prompt if using Shikra, but must be excluded if using LLaVA variants.

## Training

VINDEX is model-agnostic so the training procedure is independent of base MLLMs and only related to encoders (e.g., CLIP, DINO, and SigLIP). The training process basically follows [UMBRAE](https://github.com/weihaox/UMBRAE). Due to the architectural consistency among LLaVA variants, the trained brain encoders can be directly integrated into different MLLMs without requiring additional modifications. 

For cross-subject training using CLIP or DINO as the vision encoder:
```bash
# cross-subject training and adaptation
vison_tower='clip' img_size=224 # clip/dino_224/336
accelerate launch --num_processes=1 --num_machines=1 --gpu_ids='0' src/train_brainx.py \
    --data_path 'nsd_data' --fmri_encoder 'brainx2' --batch_size 128 --num_epochs 300 \
    --vision_tower $vison_tower --img_size $img_size  --subj 1 2 5 7 \
    --model_save_path "train_logs/cross_sub/${vison_tower}_${img_size}/epoch${num_epochs}"    
```

For single-subject training using CLIP or DINO as the vision encoder:
```bash
# single-subject training 
vision_tower='clip' img_size=224
accelerate launch --num_processes=1 --num_machines=1 --gpu_ids='0' src/train.py \
    --data_path 'nsd_data' --fmri_encoder 'brainxs' --img_size $img_size \
    --vision_tower $vision_tower --subj 1 --feat_dim 1024 --batch_size 64 --num_epochs 300 \
    --model_save_path "train_logs/specific_sub/sub01_dim1024/${vision_tower}_${img_size}/epoch${num_epochs}"
```

For single-subject training using SigLIP as the vision encoder:
```bash
vision_tower='siglip' img_size=384 feat_dim=3456 batch_size=32 num_epochs=500
accelerate launch --num_processes=1 --num_machines=1 --gpu_ids='0' src/train_dc.py \
    --data_path 'nsd_data' --fmri_encoder 'brainxs' --img_size $img_size \
    --vision_tower $vision_tower --subj 1 --feat_dim $feat_dim --batch_size $batch_size --num_epochs $num_epochs \
    --model_save_path "train_logs/specific_sub/sub01_dim${feat_dim}/${vision_tower}_${img_size}/epoch${num_epochs}"
```

> [!CAUTION]
> Training AF (Dense SigLIP feature alignment) is not recommended — it is resource-intensive and typically leads to poor results, with the brain encoder often producing garbled or empty outputs.
<!-- > It is not recommended to run the training of AF (SigLIP feature alignment), as it is time-consuming, GPU-intensive, and often results in unreliable outputs. In most cases, the trained brain encoder produces nonsensical results, such as garbled text or blank responses. -->

## TODO
- [x] Release inference scripts and pretrained checkpoints.
- [x] Update training scripts.
- [x] Update benchmark and evaluation scripts.

## Acknowledgements

The codes are built upon [UMBRAE](https://github.com/weihaox/UMBRAE). The processed data are from [MindEye](https://medarc-ai.github.io/mindeye/). We use pretrained models [LLaVA](https://llava-vl.github.io), [MMVP](https://github.com/tsb0601/MMVP), [M3](https://github.com/mu-cai/matryoshka-mm), and [DC](https://github.com/HJYao00/DenseConnector) as the MLLMs. Thanks for the awesome research works.

The following highlights a series of our works on multimodal brain decoding and benchmarking:

- **[DREAM](https://github.com/weihaox/DREAM)**: mirrors pathways in the human visual system for stimulus reconstruction.
- **[UMBRAE](https://github.com/weihaox/UMBRAE)**: interprets brain activations into multimodal explanations with task-specific MLLM prompting.
- **[BASIC](https://github.com/weihaox/BASIC)**: provides interpretable and multigranular benchmarking for brain visual decoding.

## Citation

```bibtex
@inproceedings{xia2025vindex,
  title     = {Exploring The Visual Feature Space for Multimodal Neural Decoding},
  author    = {Xia, Weihao and Öztireli, Cengiz},
  booktitle = {International Conference on Computer Vision (ICCV)},
  year      = {2025},
}
```