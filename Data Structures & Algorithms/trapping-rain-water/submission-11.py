class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxLeft, maxRight = height[l], height[r]
        res = 0
        while l < r:
            if height[l] < height[r]:
                maxLeft = max(maxLeft, height[l])
                res += maxLeft - height[l]
                l += 1
            else:
                maxRight = max(maxRight, height[r])
                res += maxRight - height[r]
                r -= 1
        return res