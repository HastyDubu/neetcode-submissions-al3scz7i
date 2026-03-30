class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums.sort()
        for n in nums:
            if n - 1 not in nums:
                length = 0
                while n + length in nums:
                    length += 1
                res = max(res, length)
        return res