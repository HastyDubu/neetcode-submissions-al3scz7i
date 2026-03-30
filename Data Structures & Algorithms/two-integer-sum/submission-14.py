class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        for i in range(len(nums)):
            if nums[i] in count:
                return [count[nums[i]], i]
            diff = target - nums[i]
            count[diff] = i
