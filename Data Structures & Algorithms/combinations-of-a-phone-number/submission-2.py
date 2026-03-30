class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        path = []

        def dfs(i):
            if i >= len(digits):
                res.append("".join(path))
                return
            
            s = digitToChar[digits[i]]
            for c in s:
                path.append(c)
                dfs(i + 1)
                path.pop()
            return
        
        if digits:
            dfs(0)
        
        return res
