class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal = ""
        for c in s:
            if c.isalnum():
                pal += c.lower()
        if pal == pal[::-1]:
            return True
        return False
        