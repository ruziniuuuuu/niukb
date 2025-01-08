class Solution:
    def candy_partition(self, nums) :
        # write code here
        tot_sum = sum(nums)

        if tot_sum % 2 == 1:
            return False
        
        target = tot_sum // 2

        visited = [False] * (target + 1)
        visited[0] = True

        for num in nums:
            for i in range(target, num - 1, -1):
                if visited[i - num]:
                    visited[i] = True
        
        return visited[-1]


if __name__ == '__main__':
    nums = [1, 6, 12, 5]
    solution = Solution()
    print(solution.candy_partition(nums))
