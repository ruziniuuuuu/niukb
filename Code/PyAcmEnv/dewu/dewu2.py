"""
给定一个大小为 N 的数组，仅由1～N 组成，且没有重复的元素。你可以选择相邻两个数进行交换，前提是，每个数最多只能被交换两次。
经交换后，所能形成的最大字典顺序的数组是多少？

从第一个数字开始，逐个元素比较直到找到第一个不同的数字，通过比较这个数字的大小决定序列的大小，称为字典顺序。

输入描述：
输入的第一行给出数组的大小 N。随后N 个数x_i。

输出描述：
输出所能形成的最大字典顺序的数组（每个数用空格分隔）。

示例输入：
8
3 7 2 1 6 5 4 8

示例输出：
7 3 6 5 2 1 8 4
"""

def func(N, x):
    # 记录每个数字被交换的次数
    swap_count = [0] * N
    
    for i in range(N):
        for j in range(N - 1):
            # 尝试交换相邻的两个数
            if x[j] < x[j + 1] and swap_count[j] < 2 and swap_count[j + 1] < 2:
                # 交换两个数字
                x[j], x[j + 1] = x[j + 1], x[j]
                # 更新交换次数
                swap_count[j] += 1
                swap_count[j + 1] += 1
    
    return x

if __name__ == '__main__':
    N = int(input())
    x = list(map(int, input().split()))
    y = func(N, x)
    print(' '.join(map(str, y)))