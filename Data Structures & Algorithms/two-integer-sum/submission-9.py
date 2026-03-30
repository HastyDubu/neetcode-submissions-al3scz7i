class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = defaultdict(int)
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in count:
                return [count[diff], i]
            count[nums[i]] = i