class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2:
            return False
        
        target = sum(nums) // 2
        dp = set()
        dp.add(0)

        for n in nums:
            nextDP = set()
            for t in dp:
                if t + n == target:
                    return True
                nextDP.add(t + n)
                nextDP.add(t)
            dp = nextDP

        return False