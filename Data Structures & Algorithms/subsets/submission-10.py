class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset, curSet = [], []
        self.create_subsets(0, nums, subset, curSet)
        return subset
    
    def create_subsets(self, i, nums, subset, curSet):
        if i >= len(nums):
            subset.append(curSet.copy())
            return
        
        curSet.append(nums[i])
        self.create_subsets(i + 1, nums, subset, curSet)
        curSet.pop()

        self.create_subsets(i + 1, nums, subset, curSet)
        return