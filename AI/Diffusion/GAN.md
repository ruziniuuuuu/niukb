# GAN (Generative Adversarial Nets)

## GAN论文逐段精读

> 李沐 2021-11-10

## Abstract

写的很精简，可以直接写入wiki的那种。

提出了一个framework，通过对抗的方式估计生成模型，同时训练两个模型：

- 生成模型G：捕获数据分布
- 辨别模型D：估计样本是训练的还是生成的

G的目的是想让D犯错，对应的是博弈论中的two-player game。

如果G和D都是MLP的话，整个系统可以通过误差反传来训练。

整个系统不需要用Markov链，相比其他工作比较简单。实验效果很好。

## Introduction

深度学习是对数据分布的一种表示，它在辨别模型上效果很好，但在生成模型上进展不多。

一个例子：

- G：造假者，造假币
- D：警察

目的是让G赢，这样的话生成的图像可以和原始图像无法分辨。

## Related Work

之前的函数总想构造一个分布函数，但计算上比较难。相比之下，我们构造一个模来实现近似。

相关工作有VAEs，predicability minimization

## Adversarial Nets

为了学习关于输入数据x的分布p_g，我们定义一个先验$p_z(z)
$和一个映射$G(z;\theta_g)$，其中$G$是可微分的MLP，$\theta_g$是可学习的参数。

- 辨别器D：maximize 辨别成功率
- 生成器G：minimize $log(1-D(G(z)))$

定义一个value function，最优时为0，不最优为负数。在博弈论为是一个min max游戏，达到纳什均衡。

Figure 1很形象，目的是G的生成和原始数据分布相同，使D无能为力。

每次迭代中，先更新辨别器，再更新生成器。GAN的收敛不容易判定。

## Theoretical Results

(理论有点晦涩，先跳过)

### 全局最优 $p_g = p_{data}$

### Convergence of Algo 1

## Experiments

效果不是很好，相信后人的智慧

## 优点 & 缺点

## Future Work

1. conditional GAN
2. ......

---

## 问题 & 八股

### 什么是KL散度？

> wiki

KL散度（Kullback-Leibler divergence，简称KLD），在消息系统中称为相对熵（relative entropy），在连续时间序列中称为随机性（randomness），在统计模型推断中称为消息增益（information gain）。也称消息散度（information divergence）。

KL散度是两个概率分布P和Q差别的非对称性的度量。 KL散度是用来度量使用基于Q的分布来编码服从P的分布的样本所需的额外的平均比特数。典型情况下，P表示数据的真实分布，Q表示数据的理论分布、估计的模型分布、或P的近似分布。
