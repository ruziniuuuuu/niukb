# VAE

## 变分自编码器Vairational Autoencoder

> [【15分钟】了解变分自编码器】](https://www.bilibili.com/video/BV1Ns4y1J7tK/?share_source=copy_web&vd_source=724ca2fcd803a56b1646d6d28e65b820)

## auto-encoder自编码器笔记

> 李宏毅

- SSL：data经过self-supervised learning（Pre-train）之后的model，可用于下游任务。
- 06年就有了auto-encoder，可以认为是self-supervised learning的一种方法。
- example:
  - inputs: unlabeled images
  - images -> (NN Encoder) -> Vector -> (NN Decoder) -> images
  - outputs: images
  - reconstruction: make the inputs and outputs as close as possible
