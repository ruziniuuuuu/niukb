# SmartEdit: Exploring Complex Instruction-based Image Editing with Multimodal Large Language Models

## Overview

<!-- ![smartedit-overview](assets/smartedit-overview.png) -->

- Text2Image，但利用多模态大语言模型来增强了图像编辑的理解和推理能力
- 先前的工作有Instruct-Pix2Pix和InstructPix2Pix，在此基础上提升复指令场景能力
- 能够处理复杂的理解（包含各种对象属性的指令，如指令、相对位置、相对大小）和推理场景
- 解决的问题：
  - 现有的方案比如InstructPix2Pix，由于依赖简单的文本编码器二难以应付复杂的环境
- 主要贡献：
  - 复杂指令场景
  - 利用多模态LLMs来更好地理解指令
  - 新的数据集Reason-Edit评估复杂图像编辑任务

## Framework

<!-- ![smartedit-framework](assets/smartedit-framework.png) -->
