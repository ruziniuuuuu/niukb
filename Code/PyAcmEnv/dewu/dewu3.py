"""
小红有一个 n 个点 m 条边的无向图，每条边有一个权值w_i。
小红计划修 k 条双向道路，起点是 1 号点，终点是其他定点。
假设修了这 k 条路后，从 1 号点到其他点的距离为 d_i，小红想知道，可以少修多少条路，使得从 1 号点到其他点的距离仍然为d_i。

输入描述：
第一行三个整数n, m, k, 表示点数、边数、以及小红计划修的路数。
接下来 m 行，每行三个整数 u_i, v_i, w_i，表示一条边的两个端点以及权值。
接下来 k 行，每行两个整数p_i, s_i，表示计划修从 1 号点到p_i号点的一条路，长度为 s_i。

输入：
2 2 2
1 2 2
2 1 3
2 2
2 3

输出：
2
"""

import heapq

def dijkstra(n, graph, start):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    return dist

def func():
    n, m, k = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    planned_roads = []
    for _ in range(k):
        p, s = map(int, input().split())
        planned_roads.append((p, s))
    
    original_dist = dijkstra(n, graph, 1)
    
    # Debug: 输出原始的最短距离
    print("Original distances from node 1:", original_dist)
    
    reduced_count = 0
    for p, s in planned_roads:
        # Debug: 输出每条计划修的路的情况
        print(f"Planned road to {p} with distance {s}, original distance {original_dist[p]}")
        if original_dist[p] <= s:
            reduced_count += 1
    
    print(k - reduced_count)

if __name__ == '__main__':
    func()