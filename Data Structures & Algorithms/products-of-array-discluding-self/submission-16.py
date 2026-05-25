class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        pre = 1
        for n in nums:
            res.append(pre)
            pre *= n

        suf = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suf
            suf *= nums[i]
        return res