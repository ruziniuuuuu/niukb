"""
给定一个矩阵，矩阵中的每个数字表示这个位置上叠放的小正方体数量。小正方体边长为 1。
请问：题目所描述的几何体的三视图（从正面、左面和上方看的投影）各自的面积为多少？

输入描述：
一行两个整数 n，m 表示矩阵的行数和列数
之后 n 行 m 列表示a_{i, j}
输出描述：
一行三个整数，依次代表从正面、左面和上方看过去的投影面积。

示例输入：
2 3
3 3 2
3 2 1
示例输出：
8 6 6
"""

def func(n, m, a):
    front = [0] * m
    left = [0] * n
    up = [0] * m * n

    for i in range(n):
        for j in range(m):
            ele = a[i][j]
            # up
            if ele == 0:
                up[i * m + j] = 0
            else:
                up[i * m + j] = 1
            # front
            front[j] = max(front[j], ele)
            # left
            left[i] = max(left[i], ele)

    sum_front = sum(front)
    sum_left = sum(left)
    sum_up = sum(up)

    return [sum_front, sum_left, sum_up]

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = [[0] * m for _ in range(n)]

    for i in range(n):
        b = list(map(int, input().split()))
        a[i] = b
    
    result = func(n, m, a)
    print(' '.join(str(item) for item in result))