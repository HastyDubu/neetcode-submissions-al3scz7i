class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = {}
        
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                res = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                res = max(sell, cooldown)
            
            dp[(i, buying)] = res
            
            return res
        
        return dfs(0, True)