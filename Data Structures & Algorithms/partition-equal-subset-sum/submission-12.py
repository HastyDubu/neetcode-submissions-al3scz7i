class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2:
            return False
        
        half = sum(nums) / 2
        visit = set([0])

        for n in nums:
            nextDP = set()
            for t in visit:
                if n + t == half:
                    return True
                nextDP.add(t)
                nextDP.add(t + n)
            visit = nextDP
        
        return False

