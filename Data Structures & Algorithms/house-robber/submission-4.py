class Solution:
    def rob(self, nums: List[int]) -> int:

        dp = [-1] * len(nums)
        
        def backtrack(i):

            if i >= len(nums):
                return 0
            if dp[i] != -1:
                return dp[i]

            dp[i] = max(nums[i] + backtrack(i + 2), backtrack(i + 1))
            
            return dp[i]
        
        return max(backtrack(1), backtrack(0))