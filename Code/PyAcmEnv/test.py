"""
使用最少的背包

有一定的数量N个物品，重量分别为W1、W2、W3….Wn（0<W<=10）,每个背包最大容量为10，请问如何合理的放置物品才能达到使用最少背包数量的目的。

实例1：
输入：
N = 5
W1=3，W2=8，W3=6, W4 =2, W5 = 2
输出：
[3,6],[2, 8],[2]或者[2,6]，[2,8],[3]  //  凡是背包数量为3的任意答案都是符合要求的
"""

def func(W):
    # sort
    W.sort()
    n = len(W)

    MAX_CAP = 10
    
    # filter bags
    selected = set()
    result = 0
    for i in range(n - 1, -1, -1):
        if i in selected:
            continue
        selected.add(i)
        count = W[i]
        for j in range(i - 1, -1, -1):
            if j in selected:
                continue
            if count + W[j] > MAX_CAP:
                break
            else:
                count += W[j]
                selected.add(j)
        result += 1

    return result

if __name__ == "__main__":
    W = [3, 8, 6, 4, 2]
    print(func(W))