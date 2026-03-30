class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}
        
        def dfs(amount):
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            
            res = 1e9

            for coin in coins:
                if amount - coin >= 0:
                    res = min(1 + dfs(amount - coin), res)
            memo[amount]  = res
            return res
        
        min_coin = dfs(amount)
        return min_coin if min_coin != 1e9 else -1