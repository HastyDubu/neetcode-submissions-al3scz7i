class Solution:
    def isPalindrome(self, s: str) -> bool:
        w = ""
        for c in s:
            if c.isalnum():
                w += c.lower()
        
        return w == w[::-1]