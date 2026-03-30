class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2:
            return False
        

        target = sum(nums) // 2
        dp = set()
        dp.add(0)

        for i in range(len(nums) - 1, -1, -1):
            nextDp = set()
            for n in dp:
                if (n + nums[i]) == target:
                    return True
                nextDp.add(n + nums[i])
                nextDp.add(n)
            dp = nextDp
        return False