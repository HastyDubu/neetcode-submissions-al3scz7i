class Solution:
    def isValid(self, s: str) -> bool:
        closed = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        pSet = []

        for c in s:
            if c in closed:
                if pSet and pSet[-1] == closed[c]:
                    pSet.pop()
                else:
                    return False
            else:
                pSet.append(c)
        
        return True if not pSet else False