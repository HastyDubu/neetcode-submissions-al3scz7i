class Solution:
    def isPalindrome(self, s: str) -> bool:
        w = ""
        for c in s:
            if c.isalnum():
                w += c.lower()
        
        l, r = 0, len(w) - 1
        while l < r:
            if w[l] != w[r]:
                return False
            l += 1
            r -= 1
        return True
        