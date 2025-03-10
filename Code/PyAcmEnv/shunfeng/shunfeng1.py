"""
小明最近学习了相反数，在研究一个有趣的数学问题。
老师给他一个任务：给定长度为N的数组a[], 小明需要选择K个数并反转他们的符号（即求相反数，a[i]置为-a[i]）。他的目标是通过这种操作来最大化数组的总和。小明的任务是找到在进行K次反转后能够得到的最大和。
形式化地，给定长度为N的数组a[]，以及一个整数K，表示必须反转K个元素的符号（选择K不同的下标i_1, i_2, ..., i_k，令a[i_j] = -a[i_j], i<=j <= K）。求最优选择后得到的数组的最大和。

输入描述：
第一行1个整数T，表示数据组数。
对于每组数据：
第一行包含两个整数N和K，分别表示数组的长度和需要反转的元素数量。
第二行包含N个整数a[i]，...，a[N]，表示数组的元素。

输出描述：
输出T行分别表述每组数据答案。
对每组数据，输出一行一个整数，表示经过K次反转后的最大和。

样例输入：
2
5 3
1 -2 3 -4 5
1 1
1

样例输出：
13
-1

提示：
初始数组为[1, -2, 3, -4, 5], 初始总和为3。
如果反转-4, -2和1的符号，可以得到[-1, 2, 3, 4, 5], 最大和为13.
在反转这三个元素后，最佳选择下的最大和是13.
"""

def f(N: int, K: int, nums: list) -> int:
    nums.sort()
    for i in range(K):
        nums[i] = -nums[i]

    return sum(nums)
    

if __name__ == '__main__':
    T = int(input())
    results = []
    for _ in range(T):
        N, K = map(int, input().split())
        nums = list(map(int, input().split()))
        results.append(f(N, K, nums))

    for result in results:
        print(result)
    
