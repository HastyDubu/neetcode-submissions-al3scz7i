class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = float('inf')
        while l <= r:
            k = l + ((r - l) // 2)
            totalHours = 0
            for i in range(len(piles)):
                totalHours += math.ceil(piles[i] / k)
            if totalHours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res