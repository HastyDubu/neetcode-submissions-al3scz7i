class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        coins.sort()
        memo = [[-1] * (amount + 1) for _ in range(len(coins))]
        
        def dfs(i, amount):
            if amount == 0:
                return 1
            if i == len(coins):
                return 0
            if memo[i][amount] != -1:
                return memo[i][amount]
            
            memo[i][amount] = dfs(i + 1, amount)
            if amount - coins[i] >= 0:
                memo[i][amount] = dfs(i, amount - coins[i]) + memo[i][amount]

            return memo[i][amount]
        
        return dfs(0, amount)