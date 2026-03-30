class Solution:
    def isPalindrome(self, s: str) -> bool:
        compare = ""
        for c in s:
            if c.isalnum():
                compare += c.lower()
        if compare == compare[::-1]:
            return True
        return False