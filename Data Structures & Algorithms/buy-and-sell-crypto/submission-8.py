class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        res = 0
        for sale in prices:
            buy = min(buy, sale)
            res = max(res, sale - buy)
        return res