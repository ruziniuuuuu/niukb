# Transformer

## 李沐论文带读 - Transformer

### Attention

An attention function can be described as mapping a query and a set of key-value pairs to an output, where the query, keys, values, and output are all vectors. The output is computed as a weighted sum of the values, where the weight assigned to each value is computed by a compatibility function of the query with the corresponding key.

### Scaled Dot-Product Attention

共包含两个主要步骤：

- 计算注意力权重：使用某种相似度函数度量每一个query向量和所有key向量之间的关联程度，对于长度为m的query向量和长度为n的key向量，计算得到一个m×n的矩阵，每一行代表一个query向量对所有key向量的注意力权重。
  - 特别地，scaled dot-product attention使用query向量和key向量的内积作为相似度函数，这样相似的queries和keys会具有较大的点积。
  - 由于点积可以产生任意大的数字，这会破坏训练过程的稳定性，因此注意力分数还需要乘以一个缩放因子来标准化它们的方差，然后使用一个softmax标准化。
  - 最终的注意力权重$w_{ij}$表示第i个query向量和第j个query向量之间的关联程度。
- 更新token embeddings：将注意力权重与value向量相乘，然后对结果求和，得到最终的输出向量。
  - 形式化表示为：$Attention(Q, K, V) = softmax(\frac{QK^T}{\sqrt{d_k}})V$
  - 这一步可以看作是对value向量的加权求和，其中权重由注意力权重决定。

## 详解Transformer （Attention Is All You Need）

> [详解Transformer （Attention Is All You Need）](https://zhuanlan.zhihu.com/p/48508221)

RNN的计算限制是顺序的，这意味着RNN相关算法只能从左到右依次计算或者从右到左依次计算，这种机制带来了两个问题：

1. t以来t-1时刻的计算结果，这样限制了模型的并行能力。
2. 顺序计算的过程中信息会丢失，尽管LSTM等门机制的结构一定程度上缓解了长期依赖的问题，但是对于特别长期的依赖现象，LSTM依旧无能为力。

Transformer解决了上述问题

1. 使用Attention机制，将序列中任意两个位置之间的距离缩小为一个常量
2. 它不是RNN的顺序结构，因此具有更好的并行性，符合现有的GPU框架

### Transformer详解

#### Transformer主要框架

Transformer的本质上是一个Encoder-Decoder的结构，encoder和decoder均由6个block组成，编码器的输出会作为解码器的输入。

Encoder的结构：

1. self-attention
2. feed-forward neural network
   1. 第一层的激活函数的ReLU
   2. 第二层是一个线性激活函数

Decoder的结构：

1. Self-attention：当前翻译和已经翻译的前文之间的关系
2. Encoder—Decoder Attention：当前翻译和编码的特征向量之间的关系

#### 输入编码

通过Word2Vec等词嵌入方法将输入语料转化为特征向量，论文中的词嵌入维度为d_model = 512

#### Self-Attention

核心内容是为输入向量的每个单词学习一个权重。

在self-attantion中，每个单词有3个不同的向量，他们分别是Query，Key和Value向量，长度均是64。它们是通过3个不同的权值矩阵由嵌入向量X乘以三个不同的权重矩阵W_Q, W_K, W_V得到的，其中三个矩阵的尺寸也是相同的，均是512*64。

Attention的计算方法如下：

1. 将输入单词转化为嵌入向量
2. 根据嵌入向量得到q, k, v三个向量
3. 为每个向量计算一个score: $score = q * k^T$
4. 为了梯度的稳定，使用score归一化，即除以sqrt(d_k)
5. 对score施以softmax激活函数
6. softmax点乘Value值v，得到加权的每个输入向量的评分v
7. 相加之后得到最终的输出结果z

在self-attention中采用了残差网络中的short-cut结构，目的是解决深度学习中的退化问题。

Query，Key，Value的概念取自信息检索系统，当你在电商平台搜索某件商品时，搜索引擎上输入的内容便是Query，然后搜索引擎根据Query为你匹配Key（例如商品的种类，颜色，描述等），然后根据Query和Key的相似度得到匹配的内容（Value）。

self-attention中的Q，K，V也起着相似的作用，在矩阵计算中，点积是计算两个矩阵相似度的方法之一，之后根据相似度进行输出的匹配，这里使用了加权匹配的方式，而权值就是query和key的相似度。

> 加权匹配：
>
> 1. 加权：每个值都被赋予了一个权重（注意力分数）。这个权重决定了该值在最终输出中的重要性。
> 2. 匹配：通过将查询向量与键向量进行比较（点积），我们在寻找与当前位置最“匹配”或最相关的其他位置。
> 3. 综合效果：通过讲权值与值向量相乘并求和，这是一种“软”匹配。我们不是选择单一的最佳匹配，而是考虑所有位置，但给予更相关的位置更高的权重。
>
> 这个过程可以被视为在多有可能的匹配中进行加权平均，其中权重反映了匹配的强度或相关性。

#### Multi-Head Attention

Multi-Head Attention相当于h个不同的self-attention的集成，以h=8为例，分三步：

1. 将数据X输入8个self-attention中，得到8个加权后的特征矩阵Z_i
2. 将8个Z_i按列拼成一个大的特征矩阵
3. 特征矩阵经过一层全连接后得到输出Z

Multi-Head attention中也加入了short-cut机制。

#### Encoder-Decoder Attention

在解码器中，Transformer Block比编码器多了一个encoder-decoder attention。在encoder-decoder attention中，Q来自于解码器的上一个输出，K和V则来自于编码器的输出。

在机器翻译中，解码过程是一个顺序操作的过程，也就是当解码第k个特征向量时，我们只能看到第k-1及其之前的解码结果，论文中把这种情况下的multi-head attention叫做masked multi-head attention。

#### 损失层

解码器解码之后，解码的特征向量经过一层激活函数为softmax的全连接层之后得到得到每个单词概率的输出向量。此时我们便可以通过CTC等损失函数训练模型了。

一个完整可训练的网络结果便是encoder和decoder的堆叠（各N个，N=6）。

### 位置编码

位置编码会在词向量中加入单词的位置信息，这样Transformer就能区分不同位置的单词了。

常见的位置编码模式有：

1. 根据数据学习
2. 自己设计编码规则

作者的位置编码是一个长度为d_model的特征向量，这样便于和词向量进行单位加的操作。

如此设计的原因是，单词的绝对位置和相对位置都很重要。

#### 为什么能表达相对位置

1. 周期性：不同频率的正弦和余弦函数的组合可以唯一地编码每个位置。
2. 线性关系：对于任意固定的偏移k，PE(pos+k)可以表示为PE(pos)的线性函数。这意味着模型可以容易地学习关注相对位置而不是绝对位置

#### 为什么这种设计优于其它方案

1. 无界性：与直接使用位置索引相比，正弦函数是无界的，这允许模型处理比训练时更长的序列。
2. 确定性：与学习嵌入相比，这种方法是确定性的，不需要额外的训练。
3. 插值能力：对于没见过的位置，这种编码方式可以平滑地插值。
4. 相对位置信息
