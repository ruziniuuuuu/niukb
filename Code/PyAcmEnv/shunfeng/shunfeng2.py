"""
对于一个3*3的矩阵，小明可以在每一个格子中填上0到3之间的任何一个数。
给数6个约束。
前三个数a_1, a_2, a_3代表每一行异或和为a_1, 第二行异或和为a_2, 第三行异或和为a_3。
后三个数a_4, a_5, a_6代表每一列异或和a_4, 第二列异或和a_5, 第三列异或和a_6。
求有多少种填法使得以上约束至少满足k个。

输入描述：
一行给出6个数a_i(0 <= a_i <= 7)。
第二行给出一个数k(1 <= k <= 6)

输出描述：
输出一行一个数代表答案。

样例输入：
3 2 1 0 1 1 
6

样例输出：
256
"""

# brute-force
def solution(a: list, k: int) -> int:
    def is_valid(matrix, a, k):
        count = 0
        # row constraint
        for i in range(3):
            if cal_xor(matrix[i]) == a[i]:
                count += 1
        # col constraint
        for j in range(3):
            if cal_xor([matrix[i][j] for i in range(3)]) == a[j]:
                count += 1
        if count >= k:
            return True
        else:
            return False
    
    def cal_xor(values: list) -> int:
        result = 0
        for value in values:
            result ^= value
        return result
    
    def enum_matrices(a, k, row, col, matrix, count):
        if col == 3:
            if row == 2:
                if is_valid(matrix, a, k):
                    count += 1
            else:
                for x in range(4):
                    matrix[row + 1][col] = x
                    enum_matrices(a, k, row + 1, 0, matrix, count)
            return
        for x in range(4):
            matrix[row][col] = x
            if is_valid(matrix, a, k):
                count += 1
        count = enum_matrices(a, k, row, col + 1, matrix, count)
        return count

    count = [0]
    matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    enum_matrices(a, k, 0, 0, matrix, count)
    return count[0]

if __name__ == '__main__':
    a = list(map(int, input().split()))
    k = int(input())


    print(solution(a, k))