# Planning-oriented Autonomous Driving

## My TODO

我还需要了解深入的概念：

- [ ] BEVFormer，各种Former是什么意思，什么原理
- [ ] Occupancy

## 端到端自动驾驶Uniad详细讲解

> [端到端自动驾驶Uniad详细讲解 - 求求你们别学了的文章 - 知乎](https://zhuanlan.zhihu.com/p/642373931)

### Abstract

- 现代自动驾驶通常模块化。感知、预测和规划。可能有累积误差或任务协调不足的困扰。
- UniAD整合全栈
- nuScenes爆杀

## 核心

- 多组查询向量的Transformer模型
- 基于最终“规划”为目标

## Introduction

- 大多数工业解决方案针对不同的任务部单独的模型
- 多任务学习方案会共享骨干网络
- 端到端范式将感知和预测模块结合在一起

UniAD是以规划为导向进行设计的。一个关键组件是连接所有节点的基于查询的设计。与经典的bbox相比，查询收益于更大的感受域，以软化上游预测的复合误差。此外，查询可以灵活地对各种交互进行建模和编码，例如多个物体之间的关系。UniAD是第一个全面研究自动驾驶领域感知、预测和规划等多种任务联合的作品。

## Methodology

UniAD面向规划设计。研究每个模块在感知和预测中的影响，利用联合优化从前面的节点到最终规划。所有感知和预测模块都在transformer解码器中设计，任务查询作为连接节点的接口。

- UniAD包含四个基于transformer解码器的感知和预测模块，以及最后的规划器。查询Q起到连接pipeline的作用。
- 多视角图像通过BEVFormer特征提取，获得BEV特征B。（可用其他BEV方案）
- TrackFormer中，通过track queries的可学习嵌入，在B中查询物体的信息来进行检测和跟踪。
- MapFormer中，使用map queries从B中查询道路元素（例如车道和分割线）的信息，并执行地图的全景分割。
- MotionFormer捕获B+物体+地图之间的交互信息（作为k和v），并预测每个物体的未来轨迹，由于场景中每个物体的行动可能会对其他物体产生影响，该模块为所有考虑的物体做出联合预测。
- 同时，我们设计了一个自车查询来预测规划结果，并将其自身原理OccFormer预测的占用区域，避免碰撞。

### TrackFormer & MapFormer

### Prediction: Occupancy Prediction

### Plannning

## Experiments

### 消融研究

## Limitations

- 大量算力，尤其是使用历史帧
- 部署难度大
- 端到端模型出现bad case不好修复
