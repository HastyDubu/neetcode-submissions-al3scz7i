class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for c in s:
            if c.isalnum():
                string += c.lower()
        
        if string == string[::-1]:
            return True
        
        return False
        