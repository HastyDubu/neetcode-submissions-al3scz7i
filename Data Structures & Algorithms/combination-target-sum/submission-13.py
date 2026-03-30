class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, total, cur):
            if total == target:
                res.append(cur.copy())
                return
            
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    break
                cur.append(nums[j])
                dfs(j, total + nums[j], cur)
                cur.pop()
            
            return
        
        dfs(0, 0, [])
        return res