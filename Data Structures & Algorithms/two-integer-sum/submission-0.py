class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in count:
                count[nums[i]] = i
            else:
                return [count[diff], i]