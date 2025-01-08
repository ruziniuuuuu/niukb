"""python
歌单排名，三种意见：

1. 1 x 第x名排名高了，应该低点
2. -1 x 第x名排名低了，应该高点
3. 0 x 第x名合理，别动

每首歌一个意见，调整歌单。

输入描述：
T 数据组数
每组数据n+1行，第一行为榜单歌数。之后n行输入两个空格分割的整数op, x

输出描述：
输出T行字符串YES或者NO表示对于每组数据 是否有满足所有条件的榜单。如果满足输出YES，否则No。

样例输入：
2
2
1 1
-1 2
5
0 2
-1 3
-1 4
0 1
-1 5

样例输出：
YES
NO

"""

def f(n, opinions):
    lower_bounds = [0] * n
    upper_bounds = [n - 1] * n

    for op, x in opinions:
        x = x - 1
        if op == 1:
            upper_bounds[x] = min(upper_bounds[x], x)
        elif op == -1:
            lower_bounds[x] = max(lower_bounds[x], x)
        elif op == 0:
            lower_bounds[x] = max(lower_bounds[x], x)
            upper_bounds[x] = min(upper_bounds[x], x)
        else:
            return ValueError

    rank_range = [[lower_bounds[i], upper_bounds[i]] for i in range(n)]

    # Brute Force
    ranks = [1] * n

    for x in range(n):
        l_x = lower_bounds(x)
        u_x = upper_bounds(x)

        flag = 0
        for x_av in range(l_x, u_x + 1):
            if ranks[x_av] == 1:
                ranks[x_av] = 0
                x_
            else:
                continue


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        opinions = list(tuple(map(int, input().split())) for _ in range(n))
        f(n, opinions)