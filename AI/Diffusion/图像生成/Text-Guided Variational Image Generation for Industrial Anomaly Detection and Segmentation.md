# Text-Guided Variational Image Generation for Industrial Anomaly Detection and Segmentation

## Abstract

- 一种文本引导的变分图像生成方法，以解决工业正造中异常检测获取clean data的挑战。
- 利用大量文本库文档中学习道德关于目标对象的文本信息，来生成与输入图像相似的合格品数据图像。
- 该框架可以确保生成的非缺陷图像与基于文本和图像知识的预期分布保持一致。

## Introduction

异常检测（anomaly detection）一直具有挑战性。

- 传统方法：通过训练非缺陷数据集的分布
- 最近方法：使用概率方法训练图像为高斯分布的可逆函数，不需要适应目标分布

异常检测的有效性取决于可用的非缺陷数据的数量和质量，大多数情况难对工业缺陷进行视觉分类，因为defects有很多种，这带来out-of-distribution的问题。因此，获取大量的非缺陷数据能够有效地表示数据分布，并且更好地与缺陷数据进行区分。

然而，工业场景下数据获取困难：

- 正常/缺陷数据集分布不均
- 数据敏感性：因机器和捕获条件而存在差异
- 在过度收集非缺陷数据的过程中，可能会错误地将缺陷数据标记为非缺陷数据

我们的方法：基于文本引导的变分图像生成方法。为了解决提供的无缺陷数据缺乏多样性的问题，我们广泛利用通过综合文本库文档学习到的关于目标对象的文本信息，以生成与输入图像最相似的无缺陷数据图像。

贡献如下：

- 变分图像生成器生成，保证非缺陷图像的方差
- 为了解决好的产品数据缺乏多样性的问题，我们开发了一个关键字到提示的生成器，该生成器通过比较关于目标对象的文本信息，通过综合文本库文档广泛学习，与输入图像生成最佳提示。
- 为了弥合不同模态之间的语义鸿沟，我们开发了一种文本引导的知识集成方法，其中潜在的图像特征与目标对象的文本信息对齐。
- 真实工业场景下的测试

## Related Work

### Text-based Anomaly Detection

大多数方法是representation-based的，并使用GAN计算分布提取patches的判别特征和计算基于reconstruction的方法的距离。最近的研究采用了不同的设置和方法，比如WinCLIP等。

我们的方法侧重于根据输入输出的相似性和基于文本的先验知识来生成合格品图像。它通过将新生成的不同属性的图像输入到通用的异常检测方法中来提高性能。

### Text-to-Image Generation

- DALL-E
- GAN
- VQGAN-CLIP: Through VQGAN-CLIP, where VQGAN creates an image, CLIP checks whether the generated image from VQGAN matches the text.

先前的T2I方法忽略了给定图像数据的表示方差的重要性，我们旨在预测合格品图像分布的方法，利该方差来避免生成有缺陷的图像，同时扩大非缺陷图像中外观的多样性。

## Preliminary Analysis
