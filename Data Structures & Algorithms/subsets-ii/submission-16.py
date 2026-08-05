class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets, curSet = [], []
        self.helper(nums, subsets, curSet, 0)
        return subsets
    
    def helper(self, nums, subsets, curSet, i):
        if i == len(nums):
            subsets.append(curSet.copy())
            return
        
        curSet.append(nums[i])
        self.helper(nums, subsets, curSet, i + 1)
        curSet.pop()

        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        self.helper(nums, subsets, curSet, i + 1)
        return