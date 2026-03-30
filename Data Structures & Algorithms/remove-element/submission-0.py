class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
            n = len(nums)
            l = r = 0
            while r < n:
                while r < n and nums[r] == val:
                    r += 1
                if r < n:
                    nums[l] = nums[r]
                    l += 1
                    r += 1
            return l