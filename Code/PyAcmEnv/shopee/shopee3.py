class Solution:
    def lengthOfLIS(self, nums) :
        # write code here
        if not nums:
            return 0
        
        n = len(nums)
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
    

if __name__ == '__main__':
    nums = [8,4,7,4,4,4,8,4]
    solution = Solution()
    print(solution.lengthOfLIS(nums))