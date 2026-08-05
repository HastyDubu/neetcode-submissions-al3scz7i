class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets, curSet = [], []
        self.helper(nums, subsets, curSet, 0)
        return subsets
    
    def helper(self, nums, subsets, curSet, i):
        if i >= len(nums):
            subsets.append(curSet.copy())
            return
        
        curSet.append(nums[i])
        self.helper(nums, subsets, curSet, i + 1)
        curSet.pop()
        self.helper(nums, subsets, curSet, i + 1)
        return
