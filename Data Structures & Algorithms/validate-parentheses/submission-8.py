class Solution:
    def isValid(self, s: str) -> bool:
        closed = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        stack = []
        for c in s:
            if c in closed:
                if stack and stack[-1] == closed[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False