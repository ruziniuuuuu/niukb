# DETR

## DETR论文精度

> [【DETR 论文精读【论文精读】】 2022-06-10](https://www.bilibili.com/video/BV1GB4y1X72R/?share_source=copy_web&vd_source=724ca2fcd803a56b1646d6d28e65b820)

很火，star很多，端到端的里程碑，NMS的调参比较复杂，体现出端到端的优越性，既不需要proposal也不需要anchor，模型的训练和部署简单了不少。

作者团队来自Facebook AI，作者是实习期搞的。

总共26页，相关工作写的很好。

反复强调，DETR是一个非常简单的框架。

### Abstract

把目标检测看成集合预测问题，做成端到端框架，把anchor和NMS去掉网络就变得非常简单。

提出两个东西：

- 目标函数
- Transformer encoder-decoder架构的引入
  - decoder部分有改进：加了个输入为learned object queris与全局图像信息结合，直接出框，而且in parallel
    - 为何in parallel：时效性，出检测框不互相依赖

框架简单，性能和占用内存等都与Faster RCNN差不多，在全景分割的任务上效果非常不错，代表着扩展性好（只需要加一个分割头就行了）

### Introduction

目标检测其实就是bbox和种类出框，是个集合预测问题，但以往的工作并不直接（要么回归要么分类），而且很多工作都会涉及到NMS，使得难以优化难以调参。

端到端在其他任务都有工作，但目标检测还没用过。

image -> CNN -> features -> Transformer encoder-decoder + object queries -> set of box predictions (100个) -> 二分图匹配bipartite matching loss -> bbox and categories

1. CNN抽特征
2. Transformer encoder抽全局特征
3. Transformer decoder生成预测框
4. 将生成的预测框与gt的预测框作匹配，去计算loss
5. training loop

COCO上，无论ap还是性能都差不多，对大物体的效果尤其好，小物体不怎么样，后来半年有deformable DETR出现解决了该问题。

### Related Work

#### Object Detection

之前的目标检测方法大多依赖于某种初始猜测，比如Two-stage依赖proposals然而single-stage依赖anchors或物体的中心点。有一些工作已经证明，这些方法极大地依赖于这种初始猜测。

以前也有set-based loss，比如有可学习的NMS，但是这些方法的性能都比较差。

之前也有recurrent detectors，但以前主要都是用RNN。

说到底，DETR的成功还是Transformer的成功。

### DETR模型

1. set prediction loss
2. an architecture

#### Set Prediction Loss

由于DETR的输出是恒定的N个predictions，而在一般情况下N是远远大于一张图片中的物体数量的，所以一个难点就是这些检测框与gt的匹配。

一种任务就是abc三个工人去完成xyz三项工作，会形成一个cost matrix，优化目标是分配最优工作使得总体的cost最小，这种问题用遍历的方法就可以解决，但是复杂度太高，在scipy里有一个linear-sum-assignment专门解决这个问题（用的就是匈牙利算法），输入一个cost matrix即可，会算出一个最优的排列，在DETR的实现里就用的这个方法。

那么cost matrix放的是什么呢，放的是loss（Hungarian Loss），这个loss包含两个部分，一个表示分类对不对，一个表示出框的准确性。

一个工程技巧是，让这两个部分的数量级相似，所以把log去掉了。其次L1 Loss在DETR里有点问题，所以作者还用了generalized IoU loss去算bbox的loss。

与普通的目标检测loss计算相比，DETR是先计算一个匹配，然后在这个匹配的基础上去计算loss的。

#### Architecture

### Experiments

### Conclusion
