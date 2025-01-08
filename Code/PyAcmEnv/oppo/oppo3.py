"""
在S城，一共有n个地点，其中一些地点通过双向道路连接起来，每条道路连接着不同的两个地点，且保证任意两个地点之间能相互到达。

双向道路一共有m条，第i条可以使用u_i, v_i, w_i表示：地点u_i和v_i相连，打车路程话费w_i元。

小欧和小皮一开始都在s地点玩，玩完之后他们打算一起坐计程车回家，但是他们的家不在同一个地点。为了节省金钱，他们决定先一起坐同一辆车，中途小欧再做另一辆计程车回家。

在本题中，我们默认司机走最优路线，即打车从u到v的花费为最少话费。

已知小欧的家在t_1地点，小皮的家在t_2地点。求最少需要花费多少钱才能让小欧和小皮全部都到家。

输入描述：

第一行输入五个正整数n, m, s, t_1, t_2代表地点的个数、边数、最开始两人玩的位置、小欧的家和小皮的家。保证s, t_1, t_2两两不同。
此后m行，第i行输入三个整数u_i, v_i和w_i表示图上第i条道路连接地点u_i和v——i，这一段的打车话费为w_i元。保证图联通，没有重边。

输出描述：
在一行上输出一个整数，代表最少需要花费多少钱才能让两人都到家。

示例1:

输入：
7 7 1 5 7
1 2 1
2 3 1
3 4 1
4 5 1
3 6 1
6 7 1
1 3 5

输出：
6

说明：
小欧和小皮先同时坐到 3 ，再分别坐车到 5 和 7，总共需要花费 6 元。注意，司机走最优路线，在本题中，会走 1 \to 2 \to 3 而不是 1 \to 3 。
"""

import heapq
from collections import defaultdict

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

def min_cost(n, m, s, t1, t2, edges):
    graph = defaultdict(dict)
    for u, v, w in edges:
        graph[u][v] = graph[v][u] = w
    
    # 计算从起点s到所有点的最短距离
    dist_s = dijkstra(graph, s)
    # 计算从t1到所有点的最短距离
    dist_t1 = dijkstra(graph, t1)
    # 计算从t2到所有点的最短距离
    dist_t2 = dijkstra(graph, t2)
    
    min_total_cost = float('inf')
    for mid in range(1, n+1):
        # 计算总花费：s到mid的距离 + mid到t1的距离 + mid到t2的距离
        total_cost = dist_s[mid] + dist_t1[mid] + dist_t2[mid]
        min_total_cost = min(min_total_cost, total_cost)
    
    return min_total_cost

# 读取输入
n, m, s, t1, t2 = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

# 计算并输出结果
result = min_cost(n, m, s, t1, t2, edges)
print(result)