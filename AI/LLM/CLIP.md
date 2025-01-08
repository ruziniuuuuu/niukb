# Clip

## TODO

- [ ] cosine similarity

## CLIP 论文逐段精读【论文精读】笔记

大量实验，多模态工作，对比学习，zero-shot，prompt template做推理

- "A photo of a {object}." -> text encoder -> text feature
- image -> image encoder -> image feature

通过cosine similarity做相似度计算

其他有意思的工作：

- StyleClip：通过改变文字输入改变图片风格
- ClipDraw：通过gradient descent生成简笔画
- Open-Vocabulary Object Detection: 利用clip做物体检测
  - Clip一个半月后Google的工作
  - 摆脱了基础类的限制，检测出新的类（蓝色的玩具，玩具鳄鱼等等）
- Constrastive Language-Image Forensic Search: Clip视频检索

Clip论文总共48页，正文30多页，大部分都是实验

目的：搞一个迁移性很好的特征。

图像文本的配对数据集，用自监督的方式训练一个模型。ImageNet上Clip和有监督训练的ResNet50打平手。

### 引言

与2017的某工作相似，但当时规模较小。

还有其他利用自然语言的工作，但规模不够所以效果不好（VirTex，ICMLM，ConvIRT）

Clip是ConvIRT的简化版本

迁移学习的效果与模型的规模正相关

### Approch

#### Natural Language Supervision

之前的工作很多，但是比较乱，规模不大，我们来做个大的！

好处很多，自监督而且不用标注很方便，输入输出的自由度打了很多，多模态的特征很容易做zero-shot的迁移学习，MOCO或MAE都学到视觉特征。

#### 创建一个足够大的数据集

#### 预训练的方法

视觉方法训练非常大非常贵，1000类的数据集都这么大了，更多类别的更吓人。

图像用CNN，文本用Transformer训练，利用对比学习的方式只需要判断图片和文本的配对即可，使任务简单很多，且监督信号更加合理。

### Training

5个Resnet和3个ViT，使用Adam优化器，Batch Size有3w多

混精度训练（大部分时候不掉点），还有很多工程上的优化

一篇推荐的blog: How to Train Really Large Models on Many GPUs?

在更大尺寸上Fine-Tune

### Experiments

#### Zero-Shot Transfer

为什么这么做？之前的自监督/无监督模型主要是学习一种泛化性比较好的特征，但很难以用到下游任务，因为还是需要用有标签的数据去做微调。如何能够训练哪一个模型而不用微调了呢？

#### Prompt Engineering And Ensembling

- 因为Polysemy多义性
- distribution gap

A photo of a {label}, a type of pet.

#### Analysis of Zero-Shot CLIP

#### 特征学习Representation Learning

- linear probe
- fine-tune

我就是要用linear probe，不用fine-tune

- 网络是冻住，可学习的空间比较小，能更准确地反映出预训练模型的好坏

#### 泛化性

### Comparison to Human Performance

给实验者做one-shot，two-shot分类，别人类要好得多，因为有37个品种的猫狗

### Limitation

- Clip性能但并非不可一世，不如最大的ViT，还差十几个点，扩大Clip规模的硬件资源消耗太大
- 在某些细分类任务上效果不太好
- 更复杂的任务：数物体、异常检测
- 虽然泛化好，但是MNIST只有88%的准确率，因为out of distribution
- 虽然能分类，但是还不能生成图像标题
- 数据利用不高效
- 如果有一个数据集准备做迁移学习，那就更好了
- 爬出来的图片文本对没有清洗和审查，可能会有偏见和歧视

### Conclusion

nlp用大规模数据预训练模型有革命性的成果，但是视觉领域还没有，尝试了一下效果确实不错。
