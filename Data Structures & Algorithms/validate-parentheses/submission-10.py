class Solution:
    def isValid(self, s: str) -> bool:
        charOut = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []

        for c in s:
            if c in charOut:
                if stack and stack[-1] == charOut[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
        