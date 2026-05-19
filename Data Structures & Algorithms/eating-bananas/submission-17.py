class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r 

        while l <= r:
            k = l + ((r - l) // 2) 
            maxSum = 0
            for p in piles:
                maxSum += math.ceil(p / k)
            if maxSum <= h:
                res = min(k, res)
                r = k - 1
            else:
                l = k + 1
        
        return res