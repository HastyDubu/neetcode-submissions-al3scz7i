class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            leftMax, rightMax = row[0], row[-1]
            if leftMax <= target <= rightMax:
                l, r = 0, len(row)
                while l < r:
                    m = l + ((r - l) // 2)
                    if row[m] > target:
                        r = m 
                    elif row[m] < target:
                        l = m + 1
                    else:
                        return True
        return False