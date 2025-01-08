# Faster RCNN

> [一文读懂Faster RCNN（大白话，超详细解析）](https://blog.csdn.net/weixin_42310154/article/details/119889682)

## Faster RCNN模型详解

Faster RCNN检测部分主要分为四个模块：

- conv layers：特征提取网络
- RPN：区域候选网络
- ROI pooling：兴趣域池化
- Classification and Regression

### 1. conv layers
