"""
对于给定的由n个结点构成，根节点为1的由根数中，定义节点u和v是相似的节点，当切进党节点u的子节点数量son_u与节点v的子节点数量son_u相等。
输出“相似的节点”的对数。

输入描述：
每个测试文件包含多组测试数据，每一行输入一个整数T代表数据组数。

每组测试数据描述如下：
第一行n为节点数量。
此后每一行代表两个整数u_i和v_i

示例输入：
1
7
1 2
1 3
3 5
3 7
2 4
2 6

示例输出：
9

解释：
在第一组测试数据中，节点 1,2,3 均有两个子节点，所以 1,2 、1,3 和 2,3 都是”相似的节点“。并且有 4 个叶子节点，也会贡献 6 个"相似的节点"。
"""

from collections import defaultdict

def count_similar_nodes(n, edges):
    # Build a tree
    children = defaultdict(list)
    for u, v in edges:
        children[u].append(v)

    # count child nodes for every node
    node_counts = defaultdict(int)
    for node, child_list in children.items():
        node_counts[len(child_list)] += 1

    # count leaf nodes
    for node in range(1, n + 1):
        if node not in children:
            node_counts[0] += 1

    similar_node_counts = 0
    for count in node_counts.values():
        similar_node_counts += count * (count - 1) // 2

    return similar_node_counts

if __name__ == '__main__':
    T = int(input())
    results = []
    for i in range(T):
        n = int(input())     
        edges = [list(map(int, input().split())) for _ in range(n - 1)]
        results.append(count_similar_nodes(n, edges))

    for result in results:
        print(result)
    
    print(' '.join(map(str, results)))