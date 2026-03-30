class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        com = {}
        for i in range(len(nums)):
            if nums[i] in com:
                return [com[nums[i]], i]
            diff = target - nums[i]
            com[diff] = i
            