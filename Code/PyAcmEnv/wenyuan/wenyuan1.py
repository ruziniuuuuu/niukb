"""
给定一个大小为n的数组。有一个K大小的滑动窗口，它从数组的最左边移动到最右边。你只能在窗口中看到K个数字。每次滑动窗口向右移动一个位置。你的任务是确定滑动窗口中每个位置的最大值和最小值。

输入描述：
输入由两行组成。第一行包含两个整数n和k（n不超过10000，k小于n），它们是数组和滑动窗口的长度。第二行有n个整数，为数组的值（均在int范围内）。

输出描述：
输出中有两行。第一行分别给出窗口中每个位置从左到右的最小值。第二行给出最大值。

示例1：

输入：
8 3
1 3 -1 -3 5 3 6 7

输出：
-1 -3 -3 -3 3 3
3 3 5 5 6 7
"""

from collections import deque

def min_max_sliding_window(n, k, arr):
    min_deque = deque()
    max_deque = deque()
    min_values = []
    max_values = []

    for i in range(n):
        # remove index outside the window
        while min_deque and min_deque[0] < i - k + 1:
            min_deque.popleft()
        while max_deque and max_deque[0] < i - k + 1:
            max_deque.popleft()

        # update min deque
        while min_deque and arr[min_deque[-1]] >= arr[i]:
            min_deque.pop()
        min_deque.append(i)

        # update max deque
        while max_deque and arr[max_deque[-1]] <= arr[i]:
            max_deque.pop()
        max_deque.append(i)

        # record min and max
        if i >= k - 1:
            min_values.append(arr[min_deque[0]])
            max_values.append(arr[max_deque[0]])
    
    return min_values, max_values

if __name__ == "__main__":
    n, k = map(int, input().split())
    arr =  list(map(int, input().split()))
    min_values, max_values = min_max_sliding_window(n, k, arr)
    print(" ".join(map(str, min_values)))
    print(" ".join(map(str, max_values)))