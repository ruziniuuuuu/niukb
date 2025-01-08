"""
猜数游戏。小 A 随机选择一个整数 K 并给出 Q 个提示，小 B 猜数。
提示含 M，D表示 M 和 K 的差的绝对值不超过 D。
现在，小 B 想根据小 A 的 Q 条提示找出满足提示的最大的 K。

输入描述：
Q
Q 行，每行两个整数 M，D
输出描述：
满足提示的最大的 K；若没有这样的数，输出-1

示例输入 1：
3
3 3
2 5
5 3
示例输出 1：
6

示例输入 2：
3
1 1
2 2
3 3
示例输出 2：
2 
"""


def func(Q, mes):
    # TODO: more elegant max and min value?
    K_max = 10**100
    K_min = -10**100
    for i in range(Q):
        M = mes[i][0]
        D = mes[i][1]
        K_min = max(K_min, M - D)
        K_max = min(K_max, M + D)
        if K_min > K_max:
            return -1
        
    return K_max
        

if __name__ == '__main__':
    Q = int(input())
    mes = []
    for _ in range(Q):
        M, D = map(int, input().split())
        mes.append((M, D))
    print(func(Q, mes))
