class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        charOut = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        for c in s:
            if c in charOut and stack:
                if charOut[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False