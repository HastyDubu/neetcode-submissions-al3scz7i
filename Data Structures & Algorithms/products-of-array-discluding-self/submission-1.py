class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        pre = 1
        for n in range(len(nums)):
            res[n] = pre
            pre *= nums[n]
        
        suf = 1
        for n in range(len(nums) -1, -1, -1):
            res[n] *= suf
            suf *= nums[n]

        return res