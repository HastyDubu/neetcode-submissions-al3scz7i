class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        results = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in results:
                return [results[diff], i]
            results[nums[i]] = i