"""
小美有个无限长的正整数序列[1, 2, 3, ...]，现在q次询问，每次询问给出两个数字x和y。
对于每一次询问，小美执行y次删除，然后输出最后一个被删除的数字。
删除指的是，找到第一个大于等于x的数字，然后将其从序列中永久删除。

输入描述：
    第一行输入一个整数q代表询问次数。
    接下来q行，每行输入两个整数x，y

输出描述：对于每一个询问，在一行上输出一个整数，代表在这次操作中最后被删除的那个数字。

示例1:
输入：
3
3 3
3 3
2 1
输出：
5
8
2
说明：
\,\,\,\,\,\,\,\,\,\,序列初始为 [1,2,3,4,5,6,7,8,9,\dots] 。
\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,● 对于第 1 次询问，依此删除 3,4,5 ，序列变为 [1,2,6,7,8,9,\dots] 。
\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,● 对于第 2 次询问，依此删除 6,7,8 ，序列变为 [1,2,9,\dots] 。
\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,● 对于第 3 次询问，删除 2 ，序列变为 [1,9,\dots] 。
"""

def find_last_deleted_number(q, queries):
    results = []
    deleted_set = set()
    for x, y in queries:
        d_x = x
        while y:
            if d_x not in deleted_set:
                deleted_set.add(d_x)
                y -= 1
            d_x += 1
        results.append(d_x - 1)

    return results

if __name__ == '__main__':
    # 读取输入
    q = int(input())
    queries = [list(map(int, input().split())) for _ in range(q)]

    # 计算并输出每个询问的结果
    results = find_last_deleted_number(q, queries)
    for result in results:
        print(result)