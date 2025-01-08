# Diffusion Model-Based Image Editing: A survey笔记

## Introduction

基于learning策略的分类：

- training-based approches
- testing-time fine-tuning approches
- training and finetuing free approches

十种不同的input conditions：text, mask, reference image, class, layout, pose, pose, sketch, segmentation map, audio and dragging point.

一种新的分类方式：

- segmentic editing
- stylistic editing
- structural editing

此外，特别关注了inpainting和outpainting两种编辑类型

## Background

### Diffusion Models

### Related Tasks

#### Conditional Image Generation

#### Image Restoration and Enhancement

## Categorization of Image Editing

based on their learning strategies:

- training-based approaches testing-time
- finetuning approaches
- training and finetuning free approaches

12 most common editing types:

- segmentic editing
- stylistic editing
- structural editing

## Training-Based Approches

### Domain-Specific Editing with Weak Supervision

CLIP Guidance: DiffusionCLIP, which allows for image manipulation in both trained and new domains using CLIP.

1. first converts a real image into latent noise using DDIM inversion.
2. then finetunes the pretrained diffusion model during the reverse diffusion process to adjust the image's attributes constrained by a CLIP loss between the source and target text prompts+

Asyrp: focuses on a finetuning on a semantic latent space internally.

Diffstyler and StyleDiffusion: target artistic style transfer.

Some useful techniques:

1. Cycling Regularization
2. Projection and Interpolation: projecting two real images into the GAN latent space and then interpolating between them for smooth image manipulation
3. Classifier Guidance

### Reference and Attribute Guidance via Self-Supervision

extracts attributes or other information from single images to serve as conditions for training diffusion-based image editing models in a self-supervised manner. Two types:

- Reference-Based Image Composition
  - PbE: using contents in bbox as ref, outside as source
    - strong augmentations to ref to prevent the trivial copy-paste solution: create an arbitrarily shaped mask, and employts the CLIP image nncoder to compress info of the ref image as condition
  - RIC: incorporates sketches of the masked areas as control conditions for training, allowing users to finely tune the effects of reference image synthesis through sketches.
- Attribute-Controlled Image Editing
  - augment pretained diffusion models with specific image features as control conditions to learn the generation of corressponding images.

### Instructional Editing via Full Supervision
