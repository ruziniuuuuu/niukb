"""
将世界简化为一条数轴。牛牛在位置 1 上，而牛牛的目的地在n。
牛牛每分钟走一米，向左或者向右。
存在 m 个传送装置，连接数轴上的两个点 (u, v)，当牛牛走到 u 时，可以传送到 v（v -> u同理）且耗时为 0.
牛牛希望规划路线到达目的地时间最少。

输入描述：
第一行 n 和 m 表示目的地坐标和装置个数。
接下来 m 行表示装置连接的两个点 u 和 v。
输出描述：
输出为一行，表示牛牛所需要的最少时间。

示例输入：
10 2
1 5
4 10
示例输出：
1
说明：
牛牛首先在1依靠装置传送到位置5。然后牛牛再向左走一米花费一分钟，达到4，再利用传送装置到达10。所以牛牛所需的时间为1分钟。
"""

def func(n, m, trans):
    trans_dict = {}
    for u, v in trans:
        trans_dict[u] = v
        trans_dict[v] = u
    
    dp = [n] * (n + 1)
    dp[1] = 0

    for i in range(2, n + 1):
        dp[i]

    


if __name__ == '__main__':
    n, m = map(int, input().split())
    trans = []
    for _ in range(m):
        u, v = map(int, input().split())
        trans.append((u, v))
    print(func(n, m, trans))
