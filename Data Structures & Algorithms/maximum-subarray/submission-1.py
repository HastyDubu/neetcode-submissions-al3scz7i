class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0
        for r in range(len(nums)):
            if curSum < 0:
                curSum = 0
            curSum += nums[r]
            maxSum = max(maxSum, curSum)
        return maxSum