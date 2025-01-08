"""
2*2网格，共四个格子（左上，右上，左下，右下），每个格子修个炮塔。假设某个炮塔战斗力为x，那么可以使其所在格子的防御力增加x，并且还可以使得它相邻的格子的防御力增加x/2向下取整，使其斜对角格子的防御力增加x/4向下去整。

你修建炮塔时可以任意指定这个炮塔的战斗力，现在给出每个格子所需要的最低防御力，你的任务是使得所有格子的防御力都大于等于给定的最低防御力，且所有炮塔的战斗力之和最小。请问所有炮塔战斗力之和的最小值是多少？

输入描述：
在一行中输入四个整数a, b, c, d (0 <= a, b, c, d <= 400)代表左上，右上，左下，右下要求的最低防御力。

输出描述：
在一行中输出一个整数，代表四个炮塔的最低战斗力之和。

示例1:

输入：
100 50 48 24

输出：
100

"""

# def calc_min_zd(a, b, c, d):
#     fy = [a, b, c, d]
#     # 初始化战斗力为最低防御力
#     zd = [a, b, c, d]

#     # 计算最大防御力
#     def calc_max_fy(zd: list) -> list:
#         max_fy = [0] * 4
#         max_fy[0] = zd[0] + zd[1] // 2 + zd[2] // 2 + zd[3] // 4
#         max_fy[1] = zd[1] + zd[0] // 2 + zd[3] // 2 + zd[2] // 4
#         max_fy[2] = zd[2] + zd[0] // 2 + zd[3] // 2 + zd[3] // 4
#         max_fy[3] = zd[3] + zd[1] // 2 + zd[2] // 2 + zd[0] // 4
#         return max_fy
    
#     # 计算所需的最小战斗力
#     max_fy = calc_max_fy(zd)

#     # 循环直到所有格子的防御力满足要求
#     while True:
#         print(1)
# import numpy as np
# import math

# def solution(a, b, c, d):
#     matrix = np.array([[1, 1/2, 1/2, 1/4],
#                       [1/2, 1, 1/4, 1/2],
#                       [1/2, 1/4, 1, 1/2],
#                       [1/4, 1/2, 1/2, 1]])
#     fy = np.array([a, b, c, d])
#     gj = np.linalg.inv(matrix) @ fy
#     math.ceil(gj[0])
#     return [math.ceil(gj[0]),
#             math.ceil(gj[1]),
#             math.ceil(gj[2]),
#             math.ceil(gj[3])]


# if __name__ == '__main__':
#     a, b, c, d = map(int, input().split())
#     print(sum(solution(a, b, c, d)))

# import math

# def matrix_multiply(matrix, vector):
#     result = []
#     for i in range(len(matrix)):
#         sum = 0
#         for j in range(len(matrix[i])):
#             sum += matrix[i][j] * vector[j]
#         result.append(sum)
#     return result

# def solution(a, b, c, d):
#     # matrix = [
#     #     [1, 1/2, 1/2, 1/4],
#     #     [1/2, 1, 1/4, 1/2],
#     #     [1/2, 1/4, 1, 1/2],
#     #     [1/4, 1/2, 1/2, 1]
#     # ]
#     inverse_matrix = [
#         [1.515625, -0.546875, -0.546875, 0.125],
#         [-0.546875, 1.140625, 0.140625, -0.375],
#         [-0.546875, 0.140625, 1.140625, -0.375],
#         [0.125, -0.375, -0.375, 1.0]
#     ]
#     fy = [a, b, c, d]
#     gj = matrix_multiply(inverse_matrix, fy)
#     return [max(0, math.ceil(gj[0])),
#             max(0, math.ceil(gj[1])),
#             max(0, math.ceil(gj[2])),
#             max(0, math.ceil(gj[3]))]

# if __name__ == '__main__':
#     a, b, c, d = map(int, input().split())
#     # 计算所有炮塔的战斗力之和
#     total_power = sum(solution(a, b, c, d))
#     print(total_power)

def min_total_power(a, b, c, d):
    def check(x1, x2, x3, x4):
        return (
            x1 + x2//2 + x3//2 + x4//4 >= a and
            x2 + x1//2 + x3//4 + x4//2 >= b and
            x3 + x1//2 + x4//2 + x2//4 >= c and
            x4 + x2//2 + x3//2 + x1//4 >= d
        )

    for total in range(max(a, b, c, d), 1601):
        for x1 in range(total + 1):
            for x2 in range(total - x1 + 1):
                for x3 in range(total - x1 - x2 + 1):
                    x4 = total - x1 - x2 - x3
                    if check(x1, x2, x3, x4):
                        return total
    
    return -1  # 如果没有找到解

# 读取输入
a, b, c, d = map(int, input().split())

# 计算并输出结果
result = min_total_power(a, b, c, d)
print(result)