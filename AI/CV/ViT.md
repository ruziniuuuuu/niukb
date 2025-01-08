# Vision Transformer

## ViT论文逐段带读【论文精读】

> bilibili李沐 2021-11-30

ViT开启了CV的新时代，效果炸裂，在paperswithcode上疯狂屠榜。

ViT的有趣特性，相比CNN的优势，以下四种情况均能表现良好：

- Occlusion
- Distribution Shift
- Adversarial Patch
- Permutation

An Image is Worth 16*16 Words

### Abstract

Transformer在NLP很好，但在CV领域仍是一些小范围应用，还依赖CNN，其实并不必要，Transformer有更好的训练效率。

### Introduction

NLP任务的主流手段是大数据集上训练，特定数据集上微调。得益于Transformer的架构，未出现性能饱和。

Transformer在视觉领域的难点：如何将2D图像变为1D序列，最简单的是直接拉直但序列太长计算复杂度太高，所以CNN仍然主导。已有一些工作将自注意力机制应用于CV，但大规模应用效果太差，都不如残差网络。

ViT希望用标准的Transformer直接扩展到CV领域，尽量不做修改。将原始图像分割为多个16*16的patch，每个patch做linear embedding，可以直接当成NLP中的单词。训练ViT使用有监督训练的方式。

已有一些类似的工作，比如ICLR2020中取了2*2的patch，ViT的区别在于可以应用在大规模的数据集。

在中规模数据集上弱于ResNet，但是可以预料，因为Transformer没有归纳偏置（因为CNN有locality、平移等变性的归纳偏置），只能自己学特征。在大规模数据集中，果然效果拔群。

### Conclusioon

与之前用自注意力机制的工作不一样的是，直接用Transformer效果出奇的好，且训练相对便宜。

挖坑：

- ViT不仅用于分类，还能用来检测、分割。
- 如何进行自监督的预训练方式
- 如果将ViT规模不变的很大（半年后出了个ViT-G）
- 多模态？

### Related Work

之前没有工作直接将Transformer应用到视觉领域。

NLP领域的SOTA：

- BERT：denoising自监督预训练任务
- GPT：语言模型预训练

CV里的自注意力：

- 如何处理pixel？
  - local neighborhood
  - Sparse Transformer
  - 轴注意力

虽然表现不错，但需要复杂工程建立算子。

很相近的工作：

- Cordonnier：2*2 patch
- image GPT

其他相关的工作：

- 在更大的数据集上做预训练，但是是残差网络

## Method

尽可能保持Transformer在NLP的结构。

### ViT

image -> Patch + Position Embedding (+ Extra learnable {class} embedding) -> (Trainable) Linear Projection of Flatten Patches -> Transformer Encoder -> MLP Encoder -> Class

- 输入：224*224*3
- 经过Patch：196 * 768
- 经过linear（768*768的全连接层）：196*768/768*768 + 1*768 = 197*768
  - 其中1*768代表cls embedding，借鉴于Bert
  - position embedding为直接加，而不是拼接，这不改变维度
  - cls token可以用global average pooling替换，效果差不多。
- Transformer叠加L层，不改变特征维度

归纳偏置Inductive bias：ViT基本没怎么用，除了位置编码用了一下，其他信息都得从头学。

混合结构：图片给CNN代替patch embedding，后面是ViT

### Fine-tuning和更高的分辨率

在更大尺寸上微调时，提前预训练好的position embedding可能失效，解决方案是使用一个2D插值，但会让效果掉点，是一种临时的解决方案。

## Experiment

主要对比ResNet和ViT，最后做了个自监督的实验。

### SETUP

- Datasets：ImageNet-21k
- Model Variants
  - ViT-Base
  - ViT-Large
  - ViT-Huge

Analysis：数据集越大ViT效果越好
