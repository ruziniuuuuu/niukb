# RL Basics

## Markov Decision Process

五个核心元素：

1. 状态空间S
2. 动作空间A
3. 状态转移概率P(s'|s,a)
4. 奖励函数R(s,a,s')
5. 折扣因子γ

MDP的目标是找到最优策略π*，使得期望累计折扣奖励最大。

关键性质：

- 马尔可夫性：转移概率只依赖于当前状态和动作。
- 时间独立性：转移概率和奖励与时间无关。

## Bellman Equation

Bellman方程是MDP的核心，描述了状态价值函数V(s)和状态转移概率P(s'|s,a)之间的关系。

Bellman方程分为两部分：

1. 状态价值函数V(s)：表示从状态s开始，遵循策略π的期望累计折扣奖励。
2. 状态转移概率P(s'|s,a)：表示从状态s开始，执行动作a后转移到状态s'的概率。

$$
V(s) = \sum_{a \in A} \pi(a|s) \sum_{s' \in S} P(s'|s,a) [R(s,a,s') + \gamma V(s')]
$$

## Policy Iteration

分为两个步骤：

1. Policy Evaluation：给定策略π，迭代计算状态价值函数V直至收敛
2. Policy Improvement：基于当前的V更新策略

算法会不断重复这两个步骤直到策略收敛。Policy Iteration能保证找到最优策略，但计算开销较大。

## Value Iteration

算法步骤：

1. 初始化V(s) = 0
2. 迭代更新V(s)直至收敛
3. 提取最优策略

特点：

- 比Policy Iteration更高效，每次迭代只需一次更新
- 收敛速度和折扣因子gamma有关
- 最终收敛到最优价值函数和最优策略

## Model-Free vs. Model-Based

- Model-Free
  - 直接从经验学习
  - 不需要知道环境模型（状态转移概率和奖励函数）
  - 样本效率低
  - 需要大量交互
  - 难以快速适应环境变化
- Model-Based
  - 通过环境模型（状态转移概率和奖励函数）学习
  - 需要知道环境模型
  - 可以快速适应环境变化
  - 计算成本高
  - 模型误差会影响性能

## On-Policy vs. Off-Policy

- On-Policy
  - 使用当前策略收集数据并学习
  - 必须使用新数据
  - 代表算法：SARSA
- Off-Policy
  - 可以使用任意策略收集的数据来学习
  - 可以使用历史数据
  - 代表算法：Q-Learning

## Q-Learning

- Model-Free
  - 不需要知道环境模型（状态转移概率和奖励函数）
  - 直接从与环境的交互中学习
  - 适用于复杂的现实世界问题，因为现实中很难获得准确的环境模型
- off-policy
  - 可以使用任意策略收集数据
  - 同时学习最优策略
  - 更有效地利用历史数据
  - exporation和exploitation的平衡

## MCTS
  
- [ ] TODO

## Policy Gradient

策略梯度直接对策略进行优化，不同于value iteration方法，它直接学习一个从状态到动作的映射策略 $\pi(a|s)$ 。

目标是最大化期望回报：

$$
J(\theta) = \mathbb{E}_{\tau \sim \pi\theta}[\sum_{t=0}^T R(s_t,a_t)]
$$

其中$\tau$表示轨迹。

### 策略梯度定理

通过对目标函数求导，可以得到策略梯度定理：

$$
\nabla_\theta J(\theta) = \mathbb{E}_{\tau \sim \pi_\theta}[\sum_{t=0}^T \nabla_\theta \log \pi_\theta(a_t|s_t)Q^{\pi_\theta}(s_t,a_t)]
$$

简化形式为：

$$
\nabla_\theta J(\theta) = \mathbb{E}_{s,a}[\nabla\theta \log \pi_\theta(a|s)Q^{\pi}(s,a)]
$$

### 优缺点

- 优点：
  - 直接优化策略函数，不需要通过值函数间接优化
  - 对连续动作空间更友好
  - 理论上保证收敛到局部最优
  - 可以学习随机策略，有助于探索和处理部分可观察环境
- 缺点：
  - 高方差，样本效率低，需要大量数据
  - 容易陷入局部最优，难以跳出局部最优解
  - 超参数敏感

## Actor-Critic
