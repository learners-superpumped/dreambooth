import os
import torch
from diffusers import StableDiffusionPipeline
from diffusers import (
    AutoencoderKL,
    DDIMScheduler,
    DDPMScheduler,
    StableDiffusionPipeline,
    UNet2DConditionModel,
)

from transformers import CLIPTextModel, CLIPTokenizer

token = "***"

cache_dir = "stable-diffusion-v1-5-cache"
vae_cache_dir = "sd-vae-ft-mse-cache"
os.makedirs(cache_dir, exist_ok=True)
os.makedirs(vae_cache_dir, exist_ok=True)

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    cache_dir=cache_dir,
    revision="fp16",
    torch_dtype=torch.float16,
    use_auth_token=token,
)

tokenizer = CLIPTokenizer.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    subfolder="tokenizer",
    cache_dir=cache_dir,
    revision="fp16",
    use_auth_token=token,
)

text_encoder = CLIPTextModel.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    subfolder="text_encoder",
    cache_dir=cache_dir,
    revision="fp16",
    use_auth_token=token,
)
vae = AutoencoderKL.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    subfolder="vae",
    cache_dir=cache_dir,
    revision="fp16",
    use_auth_token=token,
)
unet = UNet2DConditionModel.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    subfolder="unet",
    cache_dir=cache_dir,
    revision="fp16",
    use_auth_token=token,
)

noise_scheduler = DDPMScheduler.from_config(
    "runwayml/stable-diffusion-v1-5",
    subfolder="scheduler",
    cache_dir=cache_dir,
    use_auth_token=token,
)
