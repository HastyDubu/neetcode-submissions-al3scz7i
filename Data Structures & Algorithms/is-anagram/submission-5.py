class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        count_s = [0] * 26
        for c in s:
            count_s[ord(c) - ord('a')] += 1

        count_t = [0] * 26
        for c in t:
            count_t[ord(c) - ord('a')] += 1
        
        for c in s:
            if c not in t or count_s[ord(c) - ord('a')] != count_t[ord(c) - ord('a')]:
                return False
        
        for c in t:
            if c not in s or count_s[ord(c) - ord('a')] != count_t[ord(c) - ord('a')]:
                return False
        
        return True
