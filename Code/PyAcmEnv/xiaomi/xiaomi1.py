"""
装箱问题:
容量 N 的箱子，a[i]的玩具，c 个大小为 1的填充物。
任务：是否可以完全装满限制，不留任何空隙。（也可以全部为填充物）

第一行输入三个整数N n c
第二行输入a[1], a[2], ..., a[n]

样例输入：
2
10 4 1
2 3 5 7
10 1 3
6

样例输出：
YES
NO
"""

def f(N, n, c, a, i):
    if N == 0:
        return True
    if N < 0 or i == n:
        return False
    return f(N - a[i], n, c, a, i + 1) or f(N, n, c, a, i + 1)

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N, n, c = map(int, input().split())
        a = list(map(int, input().split()))
        a.append(1)  # 添加填充物
        n += 1  # 更新玩具数量
        if f(N, n, c, a, 0):
            print("YES")
        else:
            print("NO")