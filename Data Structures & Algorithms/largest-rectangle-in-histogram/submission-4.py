class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][0]:
                stackH, stackI = stack.pop()
                res = max(res, stackH * (i - stackI))
                start = stackI
            stack.append((h, start))
        
        for h, i in stack:
            res = max(res, h * (len(heights) - i))
        
        return res