import gc
import json
from dataclasses import dataclass
from typing import Optional, Union

import streamlit as st
import torch
from diffusers import (
    AltDiffusionImg2ImgPipeline,
    AltDiffusionPipeline,
    DiffusionPipeline,
    StableDiffusionImg2ImgPipeline,
    StableDiffusionPipeline,
)
from loguru import logger
from PIL import Image
from PIL.PngImagePlugin import PngInfo

from diffuzers import utils


@dataclass
class Img2Img:
    model: Optional[str] = None
    device: Optional[str] = None
    text2img_model: Optional[Union[StableDiffusionPipeline, AltDiffusionPipeline]] = None

    def __post_init__(self):
        if self.model is not None:
            self.text2img_model = DiffusionPipeline.from_pretrained(
                self.model,
                torch_dtype=torch.float16 if self.device == "cuda" else torch.float32,
            )
        components = self.text2img_model.components

        if isinstance(self.text2img_model, StableDiffusionPipeline):
            self.pipeline = StableDiffusionImg2ImgPipeline(**components)
        elif isinstance(self.text2img_model, AltDiffusionPipeline):
            self.pipeline = AltDiffusionImg2ImgPipeline(**components)
        else:
            raise ValueError("Model type not supported")

        self.pipeline.to(self.device)
        self.pipeline.safety_checker = utils.no_safety_checker
        self._compatible_schedulers = self.pipeline.scheduler.compatibles
        self.scheduler_config = self.pipeline.scheduler.config
        self.compatible_schedulers = {scheduler.__name__: scheduler for scheduler in self._compatible_schedulers}

    def _set_scheduler(self, scheduler_name):
        scheduler = self.compatible_schedulers[scheduler_name].from_config(self.scheduler_config)
        self.pipeline.scheduler = scheduler

    def generate_image(
        self, prompt, image, strength, negative_prompt, scheduler, image_size, num_images, guidance_scale, steps, seed
    ):
        self._set_scheduler(scheduler)
        logger.info(self.pipeline.scheduler)
        generator = torch.Generator(device=self.device).manual_seed(seed)
        num_images = int(num_images)
        output_images = self.pipeline(
            prompt=prompt,
            image=image,
            strength=strength,
            negative_prompt=negative_prompt,
            num_inference_steps=steps,
            guidance_scale=guidance_scale,
            num_images_per_prompt=num_images,
            generator=generator,
        ).images
        torch.cuda.empty_cache()
        gc.collect()
        metadata = {
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "scheduler": scheduler,
            "image_size": image_size,
            "num_images": num_images,
            "guidance_scale": guidance_scale,
            "steps": steps,
            "seed": seed,
        }
        metadata = json.dumps(metadata)
        _metadata = PngInfo()
        _metadata.add_text("img2img", metadata)
        return output_images, _metadata

    def app(self):
        input_image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
        if input_image is not None:
            input_image = Image.open(input_image)
            st.image(input_image, use_column_width=True)
        col1, col2 = st.columns(2)
        with col1:
            prompt = st.text_area("Prompt", "Blue elephant")
        with col2:
            negative_prompt = st.text_area("Negative Prompt", "")
        submit = st.button("Generate")

        # sidebar options
        available_schedulers = list(self.compatible_schedulers.keys())
        scheduler = st.sidebar.selectbox("Scheduler", available_schedulers, index=0)
        image_size = st.sidebar.slider("Image size", 256, 1024, 512, 256)
        guidance_scale = st.sidebar.slider("Guidance scale", 1.0, 40.0, 7.5, 0.5)
        strength = st.sidebar.slider("Strength", 0.0, 1.0, 0.8, 0.05)
        num_images = st.sidebar.slider("Number of images per prompt", 1, 30, 1, 1)
        steps = st.sidebar.slider("Steps", 1, 150, 50, 1)
        seed = st.sidebar.slider("Seed", 1, 999999, 1, 1)

        if submit:
            with st.spinner("Generating images..."):
                output_images, metadata = self.generate_image(
                    prompt=prompt,
                    image=input_image,
                    negative_prompt=negative_prompt,
                    scheduler=scheduler,
                    image_size=image_size,
                    num_images=num_images,
                    guidance_scale=guidance_scale,
                    steps=steps,
                    seed=seed,
                    strength=strength,
                )

            utils.display_and_download_images(output_images, metadata)
