class Solution:
    def isPalindrome(self, s: str) -> bool:
        check = ""
        for c in s:
            if c.isalnum():
                check += c.lower()
        
        if check == check[::-1]:
            return True
        
        return False