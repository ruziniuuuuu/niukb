# Python3 数据结构

> [Runoob: Python3 数据结构](https://www.runoob.com/python3/python3-data-structure.html)
> [Python3数据结构：力扣Leetcode预备知识【已完结】](https://www.bilibili.com/video/BV1Lk4y117Cb?p=3&vd_source=3a95aabe2a51de1b59af9b31eb6f51fd)

## Number

- Number
  - int
  - float
  - complex

- Bool
  - True
  - False

```python
# + - * / // % **

3 / 2 = 1.5
3 // 2 = 1
3 % 3 = 0

abs(-3) = 3

max(1, 2, 3) = 3
min(1, 2, 3) = 1

pow(x, y) = x ** y
sqrt(x) = x ** 0.5
```

## 列表list

### 基础操作

```python

a =  [1, 1.5, "abc"]
b = [1, 2, 3, 4, 5]
c = ["a", "b", "c"]

# 查找
a[0]

# 增加
a.append(b)

# 更新
a[0] = 9

# 删除
a.pop() # 默认删除最后一个元素
a.pop(i) # 将index为i的元素删除

# 切片
a[1: 5]
a[-1]
a[2: -1]
a[:]
```

### 常用函数

```python
len(a), max(a), min(a)

a.reverse()
a.clear()
a.count(x)
a.sort()
i = a.index(x) # 返回第一个x的index，若无匹配则报错
b = a.copy() # 浅拷贝
```

### list可用作堆栈

list可用于堆栈，LIFO

```python
stack = [3, 4, 5]
stack.append(6)
stack.pop() # 6
```

### list可用于队列

可将list用于队列，FIFO，但效率不高，因为其他元素需要一一移动

```python
# 使用deque
from collections import deque

q = deque(["a", "b", "c"])
q.append("d")
q.popleft() # 'a'
```

### 迭代

```python
for x in a:
    print(x)

for index in range(len(a)):
    print(a[index])
```

### list推导式

```python

a: [1, 2, 3, 4, 5]

[expression for item in a if condition]
b = [i * i for i in a if i % 2 == 0]

[expression if condition else else_expression for item in a]

b = [i * i if i % 2 == 0 else i for i in a]

```

### 嵌套list

```python

a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

# 将3*4的矩阵转换为4*3的矩阵
b = [[row[i] for row in a] for i in range(len(a[0]))]
```

### del语句

```python
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0] # [1, 66.25, 333, 333, 1234.5]
del a[2:4] # [1, 66.25, 1234.5]
del a[:] # []
```

### 常用操作符

```python
[1, 2, 3] + [4, 5, 6] # [1, 2, 3, 4, 5, 6]
[1, 2, 3] * 3 # [1, 2, 3, 1, 2, 3, 1, 2, 3]
```

## 元组tuple

tuple用于存储不可变的数据

```python
list: [1, 1,5, "abc"]
tuple: (1, 1.5, "abc")
# 区别： tuple不可修改、增加、删除

a = (1, 1.5, "abc")
a[0] # 查找

# 常用函数
len(a), max(a), min(a)
```

## 集合Set

- 所有元素唯一，无序
- 用于关系测试和消除重复元素
- 若要创建空集合，必须使用set()，而不是{}，后者会创建一个空字典

```python
a = {1, 1.5, "abc"}

a.add(1) # 不变
a.add(2) # 加个2
a.update(1)

a.pop()
a.remove(2)

len(a), max(a), min(a)
```

逻辑运算

```python
a: {1, 2, 3}
b: {2, 5, 9}

a - b: {1, 3}
a | b: {1, 2, 3, 5, 9}
a & b: {2}
a ^ b: {1, 3, 5, 9} # ^表示两个集合的对称差集，即只在一个集合中，不同时在两个集合中
```

## 字典dict

- 无序的键值对集合 `key: value`

```python
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127 # 增加
tel # {'jack': 4098, 'sape': 4139, 'guido': 4127}
tel{'jack'} # 4098
tel{'jack'} = 4099 # 更改

# 删除
del tel['sape']

# 查找
list(tel.keys()) # ['jack', 'guido']

# 排序
sorted(tel.keys())

# 判断是否存在
'guido' in tel # True
'jack' not in tel # False

# 字典遍历
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
```

## String字符串

```python
var1 = 'Hello World!'
var2 = "Runoob"
 
print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5])

# python三引号允许字符串跨多行
para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print (para_str)

# 常用函数
s.count("H")
s.upper(), s.isupper()
s.lower(), s.islower()
s.lstrip(), s.rstrip(), s.strip()
```

## 数组Array

用list表示，其中每一个元素数据类型相同即可

- 优点：读很快
- 缺点：查询、插入、删除很慢

## 链表LinkedList

数组和链表的优缺点

链表：

- 优点：插入、删除很快
- 缺点：查询、访问很慢

```python
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
```

## 哈希表HashTable

由dict实现

## Queue队列

```python
# 使用deque，为双端队列
from collections import deque

q = deque(["a", "b", "c"])
q.append("d")
q.popleft() # 'a'
q.appendleft("e")
q.pop()
```

## 栈Stack

使用list实现

```python
# 使用list
stack = [3, 4, 5]
stack.append(6)
stack.pop() # 6
```

也可使用deque实现（双端队列）

## 堆Heap

- 大堆：pop当前最大值
- 小堆：pop当前最小值

```python
from heapq import heapify, heappush, heappop

a = [1, 2, 3]
heapify(1) # 将a变为小堆
nlargest(2, a) # 返回最大的两个数
nsmallest(2, a) # 返回最小的两个数

heappush(a, 4)
heappop(a) # 1

# 大堆
a = [-1, -2, -3] # 先取反
heapify(a)
heappush(a, -1 * 4)
heapop(a) # -4
```

## 树Tree

节点 ｜ 父节点 ｜ 叶子节点 ｜ 高度 ｜ 深度

- 二叉树
  - 普通二叉树
  - 满二叉树：除了叶子节点，每个节点都有两个子节点
  - 完全二叉树：除了最后一层，每一层都是满的，且最后一层的叶子节点都靠左排列
- 二叉树的遍历
  - 前序遍历
  - 中序遍历
  - 后序遍历
- BFS、DFS  # 广度优先搜索、深度优先搜索
