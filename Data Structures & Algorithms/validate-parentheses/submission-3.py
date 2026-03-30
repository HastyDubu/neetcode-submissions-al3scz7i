class Solution:
    def isValid(self, s: str) -> bool:
        mp = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        arr = []
        for c in s:
            if c in mp:
                if arr and arr[-1] == mp[c]:
                     arr.pop()
                else:
                    return False                   
            else:
                arr.append(c)
        return True if not arr else False
