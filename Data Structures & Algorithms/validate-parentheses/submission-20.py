class Solution:
    def isValid(self, s: str) -> bool:
        charDict = {
            "}": "{",
            ")": "(",
            "]": "["
        }

        stack = []
        for c in s:
            if c in charDict:
                if stack and charDict[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return False if stack else True