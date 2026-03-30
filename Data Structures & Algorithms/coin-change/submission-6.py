class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}

        def dfs(total):
            if total == 0:
                return 0
            if total in memo:
                return memo[total]

            res = float("INF")

            for c in coins:
                if total - c >= 0:
                    res = min(res, 1 + dfs(total - c))
            
            memo[total] = res
            return res
        
        res = dfs(amount)
        return res if res != float("inf") else -1