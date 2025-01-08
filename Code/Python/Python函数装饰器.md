# Python函数装饰器

> [Runoob: Python 函数装饰器](https://www.runoob.com/w3cnote/python-func-decorators.html)
> [【python】装饰器超详细教学](https://www.bilibili.com/video/BV1Gu411Q7JV/?spm_id_from=333.337.search-card.all.click&vd_source=3a95aabe2a51de1b59af9b31eb6f51fd)

## 什么是装饰器

装饰器（Decorators）是修改其他函数的功能的函数，使代码更简洁。

## 一切皆对象

```python
def hi(name="yasoob"):
    return "hi " + name

print(hi())

# 我们可以将一个函数赋值给一个变量
greet = hi

print(greet()) # 输出：hi yasoob

# 如果我们删掉旧的hi函数
del hi
print(hi()) # NameError
print(greet()) # 输出：hi yasoob

# 甚至可以将函数作为参数传给另一个函数
print(greet) # 输出：<function hi at 0x7f2143c01500>

```

## 将函数作为参数传给另一个函数

```python
def hi():
    return "hi yassob!"

def doSomethingBeforeHi(func):
    print("I am doing some boring work before executing hi()")
    print(func())
```

## A Simple Case

```python
import time

def timeit(f):
    
    def wrapper(*args, **kwargs):
        start = time.time()
        ret = f(*args, **kwargs)
        print(time.time() - start)
        return ret

    return wrapper

@timeit
def my_func(x):
    time.sleep(x)
```

## 带参数的decorator

```python
import time

def timeit(iteration):
    
    def inner(f):

        def wrapper(*args, **kwargs):
            start = time.time()
            for i in range(iteration):
                ret = f(*args, **kwargs)
            print(time.time() - start)
            return ret
    
    return wrapper

@timeit(1000)
def double(x):
    return x * 2

inner = timeit(1000)
double = inner(double)

```

## @cache

```python
def cache(user_function, /):
    'Simple lightweight unbounded cache.  Sometimes called "memoize".'
    return lru_cache(maxsize=None)(user_function)
```

`@cache`是`@lru_cache`的改进版
