class Solution:
    def isValid(self, s: str) -> bool:
        outChar = {
            ")": "(",
            "}": "{",
            "]": '['
        }
        stack = []
        for c in s:
            if c in outChar:
                if stack and stack[-1] == outChar[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False