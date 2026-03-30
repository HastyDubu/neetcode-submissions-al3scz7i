class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets, curSet = [], []
        self.subset(0, nums, subsets, curSet)
        return subsets
    
    def subset(self, i, nums, subsets, curSet):
        if i >= len(nums):
            subsets.append(curSet.copy())
            return
        
        curSet.append(nums[i])
        self.subset(i + 1, nums, subsets, curSet)
        curSet.pop()

        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        self.subset(i + 1, nums, subsets,curSet)
        return