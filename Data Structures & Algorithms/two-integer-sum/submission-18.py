class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i in range(len(nums)):
            if nums[i] in res:
                return [res[nums[i]], i]
            diff = target - nums[i]
            res[diff] = i
