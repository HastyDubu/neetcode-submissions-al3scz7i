class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for n in nums:
            if n not in count:
                count[n] = 0
            else:
                return True
        return False