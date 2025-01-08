# Controllable Generation with Text-to-Image Diffusion Models: A Survey

## Introduction

Diffusion模型作为参数化Markov链，在将随机噪声转为高分辨率视觉表征上有强大的作用，在图像生成和相关下游任务中展现出巨大的潜力。

随着生成图像质量越来越高，一个关键挑战逐渐明显：针对人类需求实现精准的图像控制。这不急涉及到分辨率，还涉及到将输出与用户具体的需求进行仔细的调整。随着大量多模态文本-图像数据集的发展，T2I扩散模型已经成为了可控视觉生产的基石。这些模型可以在保证图像质量的同时更加准确地反映用户描述和需求。

T2I虽然在图像可控生成中有重要作用，但天然地无法满足某些需求，比如描述某个不存在的人或者一种特定的风格，用Text Prompts的方式就会很难表达，这些局限性为T2I的生成带来了挑战。基于这一gap，现有的大量研究转向了将超出文本描述的心条件整合进T2R扩散模型中，近两年基于diffusion的T2R的大量研究和开源工作加速了这种探索过程，丰富了条件生成的可能性范围，并解决了各种应用中用于更加复杂细致的需求。

在AIGC领域已有大量的综述，包括diffusion的原理和架构，高效的diffusion模型，多模态图像合成和编辑，视觉扩散模型以及text-to-3D的应用，但仍没有关于可控图像生成的。

本篇工作聚焦于diffusion T2I。

## Preliminaries

### Denoising Diffusion Probabilistic Model

- Forward Process
- Reverse Process

### Text-to-Image Diffusion Models

- GLIDE：
  - 第一个T2R模型
  - 基于类别引导的扩散模型，核心思路是在逆向过程的每一步都用一个分类网络对生成的图片进行分类，再基于分类分数和目标类别之间的交叉熵计算梯度，用梯度引导下一步的生成采样。
- Imagen：
  - 应用classifier-free guidance，即一个pre-trained和frozen的LLM作为text encoder，为了减少计算资源。
  - 全面的研究了多种LLMs，包括了CLIP和Bert等，发现提升语言模型的规模作用更大。
  - 揭示了cross attention的重要性
- DALL-E 2：
  - 为了从CLIP等对比模型中提取robust的语义和风格表征，DALL-E2也叫unCLIP，训了一个decoder去翻转CLIP的图像encoder
  - 生成步骤如下：
    - 首先，给定一个图像标题y和它的文本嵌入z_t，一个先验p(z_i|z_t)桥接了CLIP文本和图像隐空间之间的鸿沟，其中z_i是图像嵌入。
    - 其次，解码器p(x|z_i)从图像嵌入中生成图像x。解码器是一个从GLIDE中修改的diffusion模型，其中CLIP嵌入式投影并添加在现有的时间步嵌入中。
- Latent Diffusion Model (LDM):
  - 为了能够在有限的计算资源上进行扩散模型的训练和推理，生成高质量和灵活性的高分辨率图像，LDM在预训练的自编码器的潜在空间中应用了去噪过程。
- Satble Diffusion
  - 基于LDM构建，Stability AI开源，在T2I生成中展现出强大的实力。

### 分类Taxonomy

从condition的角度，我们可以将可控图像生成分为三个子任务：

- T2I Diffusion可控图像生成
  - Generation with specific condition
  - Generation with multiple conditions
  - Universal Controllable Generation

大多数工作研究的是在特定条件下如何生成图像，比如说基于图像引导的生成，还有sketch-to-image的生成，进一步地，我们可以根据条件的类型后进行再次分类。

- 主要挑战在于如何利用预训练的T2I diffusion模型学习建模新类型的条件，并在确保生成图像具有高质量的同时结合文本条件进行生成。
- 一些方法研究了如何使用多种条件来生成图像，比如一个字符的identity和pose。该任务的挑战在于多个条件的集成，这就需要在生成结果中拥有同时表达多个条件的能力。
- 此外，一些工作试图开发一种条件不可知（condition-agnostic）的生成方法。

## 如何控制具有Novel conditions的T2I diffusion模型

一种基于得分角度（score-based）的扩散模型控制机制
