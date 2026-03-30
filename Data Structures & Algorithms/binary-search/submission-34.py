import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = bisect.bisect_left(nums, target)
        return res if res < len(nums) and nums[res] == target else -1
        