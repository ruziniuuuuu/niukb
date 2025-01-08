"""python
a_1, a_2, ..., a_n为玩具需求电量
可选择区间[L, R], 若L<=i<=R, sum(a_i) <= m，则ok
希望只使用一次充电器，让尽可能多的玩具充满电。

输入描述：
第一行两个整数为n和m
第二行n个整数为a_1, ..., a_n

输出描述：
输出一个整数表示最多能让多少个玩具充满电
"""

def f(n, m, a: list) -> int:
    current_sum = 0
    result = 0

    L = 0

    for R in range(n):
        current_sum += a[R]

        while current_sum > m:
            L += 1
            current_sum -= a[L]

        result = max(result, R - L + 1)

    return result
    


if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    print(f(n, m, a))

