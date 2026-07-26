class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for n in nums:
            if n - 1 in nums:
                continue
            else:
                length = 0
                while n + length in nums:
                    length += 1
                res = max(res, length)
        return res