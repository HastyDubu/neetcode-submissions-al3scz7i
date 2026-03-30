class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        res = 0
        for sell in prices:
            buy = min(buy, sell)
            res = max(sell - buy, res)
        return res