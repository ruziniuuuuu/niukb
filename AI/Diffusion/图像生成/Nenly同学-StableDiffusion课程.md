# Stable Diffusion

> [【B站第一套系统的AI绘画课！零基础学会Stable Diffusion，这绝对是你看过的最容易上手的AI绘画教程 | SD WebUI 保姆级攻略】](https://www.bilibili.com/video/BV1As4y127HW/?share_source=copy_web&vd_source=724ca2fcd803a56b1646d6d28e65b820)

## 1. 快速入门

- Stable Diffusion
- WebUI
- 正向提示词
- 反向提示词

## 1. Prompts与参数

- prompts: user -> (prompts) -> AI -> Image
- "多多益善"，英文书写，以词组为单位
- 提示词的权重分配：权重过高（比如2以上）容易崩
- 反向提示词
- 采样迭代步数：理论上越高越精确，实际上20以上提升就不大了
- 采样方法Sampler：很多种，推荐用带加号的，很多模型有推荐使用的Sampler
- 分辨率：512\*512越会模糊，1024\*1024会清晰，但显存也会大。
  - 同时，如果分辨率太大的话，会有奇怪的东西出现，原因是AI的训练集分辨率比较小，如果太大则会认为是多张图片的拼接
  - 一种辅助处理手段是：高清修复增大分辨率
- 生成批次
