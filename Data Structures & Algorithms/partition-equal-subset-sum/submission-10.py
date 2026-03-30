class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2:
            return False
        
        half = sum(nums) / 2
        visit = set([0])

        for n in nums:
            curSums = visit.copy()
            for t in curSums:
                if n + t == half:
                    return True
                visit.add(n)
                visit.add(t + n)
        
        return False

