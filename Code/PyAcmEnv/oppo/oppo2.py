"""
小欧有一个长度为n的数组{a_1, a_2, ..., a_n}，他可以进行任意次操作：

- 选择1 <= i, j <= n, i != j, 执行a_i = a_i + 1同时a_j = a_j - 1。（前提是a_j > 1，也就是说操作后数组的所有元素都必须还是正整数。）

他想从数组中选择一个子序列，使得子序列是一个排列，请问在可以进行任意次操作的前提下，这个“排列子序列”的长度最长是多少？

定义子序列为从原数组中删除任意数量（可以为零、可以为全部）的元素得到的新数组。

长度为n的排列是有1～n这n个整数，按任意顺序组成的数组，每个整数恰好出现一次。例如，{2, 3, 1, 5, 4}是一个排列，但{1, 2, 2}不是一个排列（数组中的2出现了2次），{1, 3, 4}也不是一个排列（长度为3单数组中有4）。

输入描述：

第一行输入一个正整数n代表数组中的元素数量。
第二行输入n个正整数代表数组元素。

输出描述：
在一行中输出一个整数，代表最长的“排列子序列”长度。

示例1：

输入：
4
1 2 5 5

输出：
3

说明：
可以选择i = 3, j = 4。操作两次，数组a变成[1, 2, 7, 3]，可以选择的最长排列子序列为[1, 2, 3]，长度为3。
"""

def max_permutation_subsequence(n, arr):
    # 统计每个数字出现的次数
    count = {}
    for num in arr:
        count[num] = count.get(num, 0) + 1
    
    # 计算可以形成的最长排列长度
    max_length = 0
    extra = 0
    for i in range(1, n + 1):
        if i in count:
            max_length += 1
            extra += count[i] - 1
        elif extra > 0:
            max_length += 1
            extra -= 1
        else:
            break
    
    return max_length

if __name__ == '__main__':
    # 读取输入
    n = int(input())
    arr = list(map(int, input().split()))

    # 计算并输出结果
    result = max_permutation_subsequence(n, arr)
    print(result)
