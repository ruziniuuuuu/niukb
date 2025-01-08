# VAD

## 地平线VAD又又又上新了！VADv2比v1强在哪里？一起来听

> [地平线VAD又又又上新了！VADv2比v1强在哪里？一起来听](https://www.bilibili.com/video/BV1XT421k7q3/?spm_id_from=333.337.search-card.all.click&vd_source=3a95aabe2a51de1b59af9b31eb6f51fd)

### End-to-End

端到端自驾比如Tesla和comma.ai在业界有落地。定位为：感知输入，完全可微，输出轨迹/signal。优势在于，完全由数据驱动，从数据中学习到驾驶的行为模式，并且没有信息的损失，打通了梯度流，以及不需要人工设计的启发式算法，所以性能上限更高。

为什么端到端现在能火？算力+数据。

E2E perception -> prediction -> planning

### MapTRv1

之前是高精地图，标注成本过高，在线的地图预测方案是必不可缺的一环。

输入环式图像，输出vector序列，实际上道路是无序的

### Lane Graph as Path (LaneGAP)

### MapTRv2

### Long-range Mapping

120米的超大范围地图感知范围。

相比于启发式方案，表现更好。

#### PIP (Perceive, Interact, Predict)

之前的轨迹预测依赖于高精地图。无图，在线建图。利用BEVFormer。提出了模态和agent的query形成motion query。

### VAD v1: extending to e2e planning straightforwardly

#### Uncertainty of Planning and Probabilistic Modeling

Uncertainty comes from

- Scenarios
- Human behaviors

Affected by latent factors that cannot be modeled

Two methods:

- Deterministic Planning
- Probabilistic Planning

### VAD v2

最大的特点：提出了Planning Vocabulary

额外加入场景约束。

感知的模型是否真的需要？

- 90% + problems are with elements in whitelist (traffic element, map element, traffic participant)

Vectorized token, Rasterized token

#### Action Space Discretization and Planning Vocabulary

Why to output trajectory rather than control signal?

- The mapping from trajectory to control signal is almost deterministic (MPC, PID)
- For system simplicity, difference in kinamatics/dynamics model
- Explicit, easier to add scene constraints

利用Nerf的方式做信息编码

Continuity: action -> token memedding -> probability

#### Fitting the Distribution

$L = L_{distribution} + L_{conflict} + L_{token}$

#### Inference and Deployment

- Sample top 1 action
- Select TopK, randomly sample one with probability (like LLM)
- Filter actions with ego state, smoothness, perception results
- Output multi-modal trajectories, easy to combine with rule-based and optimization-based PnC (as post-solver)

#### CARLA Closed-Loop Simulation

#### CARLA Benchmark-Town05

#### Ablation

#### Scaling Law

关于因果倒置的问题，结论是：当数据量和数据分布比较好的时候，就不会出现这些问题。

#### VADv2 vs. GPT

#### VADv2 vs. Diffusion Policy

#### Future Work

VADv3 = VADv2 + RL

## 端到端自动驾驶-VAD

> [端到端自动驾驶-VAD - 锤子的文章 - 知乎](https://zhuanlan.zhihu.com/p/715181935)

以前的自动驾驶规划依赖场景的密集栅格表达；其计算密集，容易错过实例级结构信息

VAD完全向量化，优点：

1. 利用矢量化的代理运动和地图元素作为显式实例级规划约束，有效地提高了规划的安全性；
2. 对算力要求低，推理速度快，因为不适用于计算密集型栅格化和大量设计的后处理步骤；

向量化map：提供道路结构信息， 如交通流量、可行驶边界和车道方向。优点：可以降低轨迹搜索空间，规划更可靠轨迹。

向量化agent运动信息：可为避免碰撞提供实例级限制

VAD通过查询交互和矢量化规划约束，隐式和显式地利用矢量化场景信息来提高规划安全性；矢量化规划约束主要包括：

1. 自车碰撞约束，保持自车和其他动态车辆见在横向和纵向的安全距离；
2. 自车边界约束，保证规划轨迹远离边界；
3. 自车道路方向约束，用矢量化车道方向正则化车辆的未来运动方向

### 算法实现

1. Backbone -> BEV features：输入多角度、多帧的图片输入，通过BEVEncoder得到相应的BEV features
2. Vectorized Scene Learning ==> Vectorized Map & Vectorized Agent Motion：表达场景信息
