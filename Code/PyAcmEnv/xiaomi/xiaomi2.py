"""
排序任务。
两个长度为n的数组a[]和 b[]。
可以在两数组对应位置做交换。可以进行任意次交换。
想知道是否可以达到，至少让一个有序。

样例输入：
2
5
1 3 5 2 4
5 2 3 4 1
7
1 2 3 4 3 2 1
4 3 2 1 2 3 4

样例输出：
YES
NO
"""

def f(n, a, b):

    c = [0] * n

    c[0] = min(a[0], b[0])

    for i in range(1, n):
        max_curr = max(a[i], b[i])
        min_curr = min(a[i], b[i])

        if i + 1 == n:
            if c[i - 1] <= min_curr:
                c[i] = min_curr
        else:
            if c[i - 1] <= min_curr:
                c[i] = min_curr
            else:
                c[i] = max_curr
                max_next = max(a[i + 1], b[i + 1])
                min_next = min(a[i + 1], b[i + 1])
                if c[i] > max_next or c[i] < min_next:
                    return False
                else:
                    c[i] = min_next
                
    return True

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        if f(n, a, b):
            print("YES")
        else:
            print("NO")
    