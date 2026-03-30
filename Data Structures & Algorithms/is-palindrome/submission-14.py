class Solution:
    def isPalindrome(self, s: str) -> bool:
        w = ""
        for c in s:
            if c.isalnum():
                w += c.lower()
        
        if w == w[::-1]:
            return True
        
        return False