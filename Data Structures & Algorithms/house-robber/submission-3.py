class Solution:
    def rob(self, nums: List[int]) -> int:

        dp = [-1] * len(nums)
        
        def dfs(i):
            if i >= len(nums):
                return 0

            if dp[i] == -1:
                dp[i] = nums[i] + dfs(i + 2)
            
            return max(dp[i], dfs(i + 1))
        
        return dfs(0)
            
