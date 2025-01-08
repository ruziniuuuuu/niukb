# ComfyUI

This ui willlet you design and execute advanced stable diffusion pipelines using a graph/nodes/flowchart based interface.

## ComfyUI Basic Tutorial VN

The big files downloaded from HuggingFAce or Civitai. The contains the weights for 3 different models: CLIP, the main MODEL and the VAE. In the default workflow this is represented by the CheckpointLoader.

- CLIPTextEncode: The CLIP is used in Stable Diffusion to encode the text to a format that the main MODEL can understand.
- KSampler: Image Generator.
  - Inputs
    - Diffusion Model used
    - pos. and neg. prompts encoded by the CLIP model
    - Latent Image
      - for txt2img, pass it an empty image.
  - Process
    - The Sampler takes this input latent image, adds noise to it and then denoises it.
    - The pos. and neg. prompts are passed to the MODEL at each sampling step and are used to guide the denoising. The denoising is how Stable Diffusion generates images.
    - The final model used by stable diffusion is the VAE
      - VAE is used to translate an image from latent space to pixel space. Latent space is the format the main MODEL understands while pixel space is the format that your viewer understands. VAEDecoder takes the latent image (coming from ssampler) as input and outputs a regular image.
    - The image is then saved to a PNG file with the SaveImage node.

## ComfyUI入门教程

> [【ComfyUI全球爆红，AI绘画进入“工作流时代”？做最好懂的Comfy UI入门教程：Stable Diffusion专业节点式界面新手教学】](https://www.bilibili.com/video/BV1D7421N7xN/?share_source=copy_web&vd_source=724ca2fcd803a56b1646d6d28e65b820)

视频做的很用心，好评！

一些推荐的custom nodes：

- ComfyUI Manager
- CumfyUI-Custom-Scripts：提示词补全，还有其他功能
- Tagger：字符串生成prompt，Convert text to prompt，自动负面提示词

点左上角的小圆点，可以折叠node。

多个节点可以组成一个节点包，最著名的是impact pack节点包，很全能，比如ToBasicPipe等等。

Efficiency nodes：为高效而设计。

- Efficient Sampler
- Efficient Loader

可以用四个节点实现一个T2I。

### 高清放大

Example：2Pass2Image

操作潜空间：

- Upscale Latent：增大latent的分辨率
- Upscale Latent By：放缩图片
- 多加一个KSampler，这里的denoise表示重绘幅度，最重要，0.5以下比较好是安全线

操作图像：ESRGAN update四倍放大

latent放大效果比较好。

后期处理：Upscale Iamge （using Image）。

放大容易爆显存，有一些脚本用来分区域放大会省显存。

### 局部重绘

Inpaint文件里有一些基本的工作流。

Open in MaskEditor选mask，后接一个VAE Encode专门用来重绘，目的就是只在mask里做重绘。

Denoise不能太低，0.8即可，否则会被视为white latent。

多数情况下需要对mask进行二次处理，因为mask边缘生硬或精度不足。

通过mask invert节点可以选择重绘mask里面的还是外面的。

可以通过Convert mask to Image进行preview处理完的mask长什么样子。

也可以Convet Image to mask。

### 附加网络

三类主要的：

- Embeddings
- LoRA
  - 可以堆叠lora，通过efficient loader可以一个nodes堆叠好几个lora
- ControlNet
  - 官方文件夹里有默认workflow，会输出一个conditioning传递给KSampler
  - 一个问题是ComfyUI只加载ControlNet的模型，额需要手动加入预处理器
  - 或者多下载一个包含预处理器功能的节点，ControlNet Aux
  - 多个ControlNet直接火车头

### 综合应用

对照片做批量的风格迁移

可以忽略节点：Bypass
