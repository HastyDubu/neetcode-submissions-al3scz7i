class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = l + ((r - l) // 2)
            totalHours = 0
            for p in piles:
                totalHours += math.ceil(float(p) / k)
            if totalHours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res