class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in sums:
                return [sums[diff], i]
            sums[nums[i]] = i
            
        