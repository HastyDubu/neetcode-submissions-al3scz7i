class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr = {}
        for n in nums:
            if n not in arr:
                arr[n] = 0
            else:
                return True
        return False