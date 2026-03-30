class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = {}
        for n in nums:
            if n in duplicate:
                return True
            duplicate[n] = 0
        return False