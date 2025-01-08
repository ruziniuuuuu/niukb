"""
文远知行的工程师小明要测试最新版本的自动驾驶程序。这个自动驾驶程序包含n个算法模块，我们用0~n-1来表示不同的算法模块（modules）。算法模块之间存在一定的依赖关系，我们用一个一维数组dependencies来表示这种依赖关系，其中dependencies[j] = [prevModule, nextModule]，表示算法模块nextModule必须在算法模块prevModule之后执行。我们给定一组critical_modules，表示必须被执行的算法模块。与此同时，给定一个下标以0开始的一维数组latencies，其中latencies[i]表示算法模块i执行所需要的时间。

请根据以下规则，计算出执行该程序所需要的最短时间：
1. 在critical_modules中算法模块都需要执行一次，每个算法模块可以在满足依赖条件后任意时间开始执行。
2. 没有直接或间接依赖关系的算法模块，可以并行执行，且不影响各自的运行时间。

注意：
1. 测试数据可以保证执行所有算法模块（即所有算法模块可根据依赖关系构成有向无环图）；
2. dependencies和critical_modules均可能为空，times由非负整数组成。

示例1:
输入：
5,[[0,1],[0,2],[1,3],[2,3],[2,4]],[1,2,3,4,1],[2,3]
输出：
8
说明：
critical_nodes 为 2，3。根据依赖关系可得，必须执行的node为[0,1,2,3]，其中关键路径为[0,2,3]，则最小运行时间为1 + 3 + 4 = 8
"""

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 找到最小执行时间
# @param n int整型 算法模块的个数
# @param dependences int整型二维数组 算法模块的依赖关系，[i, j] 表示算法模块j依赖算法模块i
# @param latencies int整型一维数组 每个算法模块的延迟
# @param critical_modules int整型一维数组 必须执行的算法模块
# @return int整型
#

from typing import List
from collections import defaultdict, deque

class Solution:
    def minimumCriticalTime(self , n: int, dependences: List[List[int]], latencies: List[int], critical_modules: List[int]) -> int:
        # 构建反向图
        reverse_graph = defaultdict(list)
        for prev, next in dependences:
            reverse_graph[next].append(prev)
        
        # 找到所有必须执行的模块
        must_execute = set(critical_modules)
        queue = deque(critical_modules)
        while queue:
            node = queue.popleft()
            for prev in reverse_graph[node]:
                must_execute.add(prev)
                queue.append(prev)

        # 构建子图和入度
        subgraph = defaultdict(list)
        in_degree = [0] * n
        for prev, next in dependences:
            if prev in must_execute and next in must_execute:
                subgraph[prev].append(next)
                in_degree[next] += 1
        
        # 拓扑排序且考虑并行执行
        queue = deque([node for node in must_execute if in_degree[node] == 0])
        max_time = {node: 0 for node in must_execute}
        current_time = 0
        while queue:
            level_size = len(queue)
            max_level_time = 0
            for _ in range(level_size):
                node = queue.popleft()
                execution_time = current_time + latencies[node]
                max_time[node] = execution_time
                max_level_time = max(max_level_time, execution_time)
                for next in subgraph[node]:
                    in_degree[next] -= 1
                    if in_degree[next] == 0:
                        queue.append(next)
            current_time = max_level_time
        return current_time


if __name__ == '__main__':
    solution = Solution()
    n = 5
    dependencies = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 4]]
    latencies = [1, 2, 3, 4, 1]
    critical_modules = [2, 3]
    print(solution.minimumCriticalTime(
        n,
        dependencies,
        latencies,
        critical_modules
    ))