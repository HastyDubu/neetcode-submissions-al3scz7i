class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = {}

        def dfs(i, a):
            if i >= len(nums):
                return 1 if a == target else 0
            if (i, a) in dp:
                return dp[(i, a)]
            
            res = dfs(i + 1, a + nums[i])
            res += dfs(i + 1, a - nums[i])

            dp[(i, a)] = res

            return res
        
        return dfs(0, 0)