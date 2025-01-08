# ControlNet

## My TODO

经过学习之后，我还需要了解的概念：

- [ ] zero convolution是什么，为什么work

## 深入浅出完整解析ControlNet核心基础知识

> [深入浅出完整解析ControlNet核心基础知识 - Rocky Ding的文章 - 知乎](https://zhuanlan.zhihu.com/p/660924126)

## 全网最详细controlnet论文逐段精读

> [【AI论文精读】【图像生成】全网最详细controlnet论文逐段精读](https://www.bilibili.com/video/BV1fs4y177nu/?share_source=copy_web&vd_source=724ca2fcd803a56b1646d6d28e65b820)

Adding Conditional Control to Text-to-Image Dffusion Models

加入Canny、分割图、深度图等等十几种去控制生成

### Abstract

针对当前的T2I生成方法，我们提出三个问题：

- 这种prompt-based的方法能满足要求吗？
- 什么样的框架能处理不同的条件
- 如何保留大模型的能力，不用从头训练

作者的发现：

- 在特定领域，其实数据并不多
- 资源不多，大的计算资源并非随处可得。对一般人而言，这需要对于预训练模型进行微调或者迁移学习
- 模型是端到端的，更加灵活，非常必要

### Introduction

提出了ControlNet去控制大型Diffusion模型。clone了模型权重为trainable copy和locked copy

- locked copy：训练中参数不调整
- trainable copy：在小样本中学习如何去控制生成

回答了之前的问题：如何保留大模型的能力呢？通过locked copy。

通过zero convolution将locked copy和trainable copy相连。zero convolution就是1*1的权值为0的卷积（训练开始的时候），目的是在开始训练的时候保证模型的输入和不加controlnet时模型的输入是相同的。

训练了各种各样的数据集，在小样本和大样本上都能进行训练，而且能在消费级显卡上训练，说明足够轻量化。

### Related Work

- HyperNetwork：对模型微调的方式，在原来模型中新加层进行微调。
- zero convolution的由来
- DPM模型：DDPM，LDM
- Text-to-Image生成：CLIP方式处理文本，Disco Diffusion，Stable Diffusion
- 其他控制方式：color-level，img2img，inpainting，textual inversion或者DreamBooth去控制图像风格
- 图生图的控制方式：Pix2Pix，Taming Transformer

### Method
