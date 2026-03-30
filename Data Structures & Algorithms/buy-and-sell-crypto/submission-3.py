class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy = prices[0]
        for sale in prices:
            max_profit = max(max_profit, sale - min_buy)
            min_buy = min(min_buy, sale)
        return max_profit