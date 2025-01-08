# Python库collections

> [https://zhuanlan.zhihu.com/p/343747724](Python库collections)
> [https://docs.python.org/zh-cn/3/library/collections.html#module-collections](中文文档)

collections模块实现了特定目标的容器，提供了额外的高性能数据类型，比如collections模块的OrderedDict类构建的字典可以支持顺序

## 模块子类

```python
import collections
print(collections.__all__)
['deque', 'defaultdict', 'namedtuple', 'UserDict', 'UserList', 
'UserString', 'Counter', 'OrderedDict', 'ChainMap']
```

## 计数器-Counter

计数可哈希对象

```python
from collections import Counter
import re
```
