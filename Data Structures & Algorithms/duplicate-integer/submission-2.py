class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr = []
        for n in nums:
            if n not in arr:
                arr.append(n)
            else:
                return True
        return False