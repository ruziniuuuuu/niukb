# 跟知乎大V一起来学BEV！视觉BEV感知和跟踪算法详解

> [【跟知乎大V一起来学BEV！视觉BEV感知和跟踪算法详解】](https://www.bilibili.com/video/BV1NM4y1a7V3/?share_source=copy_web&vd_source=724ca2fcd803a56b1646d6d28e65b820)

## My TODO

经过学习过后，我需要进一步了解的概念：

- [ ] 稠密与稀疏的区别，优缺点
- [ ] 深入理解Transformer的query过程
- [ ] NMS，匈牙利匹配
- [ ] cross-attention
- [ ] Stereo双目
- [ ] 时空对齐
- [ ] 内外参投影
- [ ] 深度估计（单目/双目）

## 主要内容

1. BEV感知的优势
2. BEV目标检测的常见范式
3. BEV时序融合的方法BEV端到端目标跟踪初探
4. Q&A

## BEV感知的优势

- 早期视觉感知：2D检测 + 测距
  - 视觉几何测距：假设地面平坦，目标接地，已知目标真实高度，2D像素高度，内参
  - IPM（逆透视变换）测距：假设地面平坦，目标接地，对标定要求严格
  - 双目测距：基线长度、共视区域限制测距范围，立体匹配和cost volume计算复杂度高
- 基于CNN的深度学习的方法
  - 视觉3D检测：需要复杂的后处理做多视角拼接，之前实车都这么做，非常复杂
  - 伪点云方法（稠密深度估计 + 点云检测）：依赖于深度估计准确性，深度估计结果当做点云处理
- 基于CNN/Transformer的BEV感知：
  - 不依赖于先验知识，如接地假设、地平面假设
  - 直接融合多视角特征，无需复杂的后处理

## BEV目标检测的常见范式

- 自底向上
  - 先在每个相机透视视角估计像素的深度，再通过内外参投影到BEV空间，通过多视角的融合生成BEV特征，支持下游的任务。
  - 代表工作：LSS（NVidia，2020），BEVDet（鉴智机器人，2022）等
- 自顶向下
  - 先在BEV空间初始化特征（稀疏或稠密），再通过多层Transformer（self-attention和cross-attention）与每个相机特征进行交互融合，最终得到BEV特征
  - 代表工作：DETR3D（清华等，2021）为稀疏的代表，BEVFormer（上海AI Lab，2022）为稠密的代表等

### LSS（Lift，Splat，Shoot）

Lift：

- 对于每个视角，每个像素点，预测多个离散深度值的概率（文中是1-50米），得到深度分布特征alpha
- 将深度分布特征alpha和图像特征c做外积，得到视锥特征

Splat：

- 将多视角的视锥特征通过外参投影到bev平面
- bev平面下具有无限高度的体素称为pillar，将每个视锥的每个点分配给最近的pillar，执行sum-pooling，得到BEV特征

Shoot：

- 用BEV特征可以很方便地进行3D检测、语义分割、预测和规划等一系列任务

### BEVDet

- BEVDet使用LSS方法得到稠密的bev特征，经过bev encoder进行编码，再使用检测头执行目标检测
- 训练的真值匹配和推理后处理采用scale-NMS，将不同的size考虑在内

### DETR3D

自底向上的问题：lift过程多视角冗余计算，splat过程复杂度高，且稠密bev特征不一定是必要的

有了Transformer，使得自顶向下的稀疏BEV成为可能

Deformable DETR发现原始DETR的Transformer的query的全局交互没有必要，收敛慢。可以联想到可变卷积的思想，计算量小了很多，效果可能更好。

前置知识：Transformer，ViT，DETR，Deformable DETR

DETR3D比2D多了个BEV空间到多视角图像空间的交互。

1. transformer阶段：在BEV空间初始化多个object-queries，并映射出对应的3D reference_points，在cross-sttention阶段经过内外惨投影到多个2D视角，并经过双线性插值找到的最近的2D特征进行交互
2. 匹配阶段：使用匈牙利匹配得到**一对一**的匹配结果，后处理不需要NMS（NMS是一对多的，复杂度很高）

DETR系列的扩展：

1. DAB-DETR：使用更有意义且动态更新的位置编码
2. DN-DETR：训练阶段加入了去噪（denoise）分支，缓解匈牙利匹配的不稳定性，帮助模型更快收敛

### 自顶向下 BEVFormer （稠密范式）

与DETR3D的区别：

1. 加入了transformer encoder，定义N*N的稠密pillar网格，每一个pillar对应一个query，在self-attention阶段，每个query对应一个2D的reference_points，在cross-attention阶段采样K个高度值，分别做内外参投影和特征交互，再将所有的高度的结果进行相加，最中得到稠密的BEV特征
2. decoder在encoder的基础上使用2D的DETR decoder
3. 在encoder阶段加入时序融合，即保留前一帧的bev feature在self-attention模块进行融合

## BEV时序融合的方法

### 时序融合简介

单帧检测的问题在于不稳定，拼接起来会抖动地很严重。

时序融合是提高感知算法准确性和连续性的关键，可以弥补单帧感知的局限性，增加感受野，改善目标检测（Object Detection）帧间跳变和目标遮挡问题，更加准确地判断目标运行速度，同时也对目标检测（Prediction）和跟踪（Tracking）有重要作用。

- 传统方法：RNN、卡尔曼滤波。缺点：后融合，依赖检测结果，对单帧地准确性帮助不大，且增加额外的开销。
- 推荐方法：特征级融合。优化：中融合，节省内润，跨模态，跨时空。

BEV时序融合方法：

- 图像域（自车camera图像坐标系）特征融合
  - 优点：可融合区域大，自适应调节前序帧权重，可用的时序区间长
  - 缺点：保留多视角图像特征占用显存大，重新做特征融合时延较长
- BEV域（自车lidar坐标系）特征融合（区别于传统感知算法）
  - 优点：简单直接，占用显存小
  - 缺点：可融合区域小，无法自适应调节前序帧权重，可用的时序区间短

具体融合手段：CNN，Transformer，Stereo

融合关键点：训练的前序帧选择，融合分辨率，时空对齐（alignment）（特征warp或转换reference_points）

### 基于Transformer的BEV特征融合

- BEVFormer（上海AI Lab）
  - 保留前序帧encoder输出的BEV feature，时空对齐后在Temporal Self-Attention模块与当前帧的BEV feature分别做Deformable-self-attention，再做平均操作
  - 训练前4帧随机选择3帧，**两两迭代融合**，推理出前一帧（关键帧），提升很大
- PolarDETR（华中科大，地平线）
  - 极坐标：避免笛卡尔坐标矩形的距离范围不一致引起歧义
  - 保留多个前序帧的object query，时空对齐后与当前帧拼接后做self-attention再降，非迭代融合

### 基于CNN的BEV特征融合

- BEVDet4D/BEVdepth4d（鉴智机器人）
- PolarFormer（复旦大学，达摩院）

### 基于Transformer的图像特征融合

- PETRv2（旷视科技）
- Uniformer（浙大，大疆，上海AI Lab）
  - 提出“虚拟视角（virtual views）”的概念，融合更长的时序
  - 使用self-regression自回归模块融合多层transformer结果，达到加强效果
- Uniformer（商汤）
  - 2D时序，如视频识别相关任务
  - 使用3D卷积在图像域进行时序融合
  - 浅层使用3D卷积提取局部特征，深层结合transformer学习全局特征

### 基于Stereo的图像特征融合

基于stereo的方法：将带有pose信息的时序帧作为双目视图进行深度估计，再做LSS投影

- BEVStereo（中科院，旷视科技）
  - 将多视图分两个warp方向输入共享权重的两个子网络，同时进行单目和双目深度估计（双目需要匹配点对，无法覆盖所有点）并融合
  - 对每个像素点预测$\mu$和$\sigma$，用$\mu+k*\sigma$决定深度候选值，而不是所有像素使用同样的深度候选值
- SoloFusion
  - 提出影响时序融合效果的主要因素有两个：时序融合区间和融合分辨率
  - BEV特征融合只适用于较短时间，而对于Stereo方法来说，间隔时间长的两帧的匹配点对距离较远，深度估计更准确
  - 融合时间长可以弥补低分辨率带来的指标下降，不增加显存占用
  - 该方法相比单帧的提升明显

## BEV目标跟踪初探

有了检测和时序，可以挖掘一下BEV的跟踪。

目标检测的三个发展阶段：

- Tracking by Detection：完全独立的二阶段检测和跟踪
- Tracking by Regression：隐式数据关联，即一定程度上融合了检测和跟踪
- Tracking by Attention：基于transformer的端到端检测+跟踪

训练阶段：Label Assignment

核心思想：每帧新初始化N个query（new-born query），与标签做匈牙利匹配后，匹配成功的query（task query）迭代进入下一帧，与下一帧的new-born query拼接后参与transformer更新，但绑定标签不再参与匹配。

推理阶段：score_thresh & filter_score_thresh & miss_tolerance

核心思想：每帧score大于score_thresh（0.4）作为新目标加入，连续miss_tolerance（5）帧低于filter_score_thresh（0.35）作为消失目标舍弃。
