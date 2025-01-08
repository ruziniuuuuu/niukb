"""
n 棵苹果树，共 n 个苹果，每个苹果有两个参数（pos_i, h_i），表示苹果所在的苹果树编号和高度。
对于每一棵苹果树，可选择一个长度为 k 的区间，得到高度在这个区间的所有苹果。
问：该如何操作才能得到最多的苹果，输出最多的苹果个数。

输入描述：
第一行为三个证书n, m, k，分别代表苹果树个数、苹果个数、可选择区间的长度。
接下来有 m 行，每行两个整数（pos_i, h_i），代表每个苹果的位置参数。

输出描述：
输出一个整数，代表可以得到的最多的苹果个数。

示例输入：
2 5 3
1 12
1 4
2 9
2 7
2 44

示例输出：
3
"""

def func(n, m, k, apples):
    apple_infos = dict()
    for i in range(m):
        pos, h = apples[i]
        if pos not in apple_infos:
            apple_infos[pos] = []
        apple_infos[pos].append(h)

    max_get = 0
    for _, apple_hs in apple_infos.items():
        apple_hs.sort()
        left = 0
        current_max = 0
        for right in range(len(apple_hs)):
            while apple_hs[right] - apple_hs[left] > k:
                left += 1
            current_max = max(current_max, right - left + 1)
        max_get += current_max

    return max_get


if __name__ == "__main__":
    n, m, k = map(int, input().split())
    apples = []
    for i in range(m):
        pos, h = map(int, input().split())
        apples.append((pos, h))

    print(func(n, m, k, apples))