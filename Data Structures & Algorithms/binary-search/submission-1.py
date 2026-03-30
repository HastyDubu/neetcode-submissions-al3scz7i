class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) 

        while l < r:
            middle = l + ((r - l) // 2)

            if nums[middle] > target:
                r = middle
            elif nums[middle] <= target:
                l = middle + 1
        
        return l - 1 if (l and nums[l - 1] == target) else  - 1