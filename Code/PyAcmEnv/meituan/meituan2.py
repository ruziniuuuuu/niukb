"""
长度为n的数组，每次操作执行如下：

选定一个a_i, 该数加上一个任意的x(x > 0), 花费代价为a_i + x。

请问小美想把整个数组变成全部奇数或者全部偶数的最小代价是多少？

输入描述：
第一行一个整数，表示数组长度。
第二行n个整数，第i个数a_i表示数组元素。

输出描述：
最小代价。

示例：
输入
3
1 2 3
输出
3
"""

def min_cost(n, a):
    even_count = 0
    odd_count = 0
    even_cost = 0
    odd_cost = 0

    for i in range(n):
        if a[i] % 2:
            even_count += 1
            odd_cost += a[i] + 1
        else:
            odd_count += 1
            even_cost += a[i] + 1
    
    return min(odd_cost, even_cost)



if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(min_cost(n, a))