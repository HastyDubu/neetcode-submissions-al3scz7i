class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2 != 0:
            return False
        
        half = sum(nums) / 2
        visit = set([0])

        for n in nums:
            nextVisit = set()
            for t in visit:
                if n + t == half:
                    return True
                nextVisit.add(t)
                nextVisit.add(n)
                nextVisit.add(t + n)
            visit = nextVisit
        
        return False
        