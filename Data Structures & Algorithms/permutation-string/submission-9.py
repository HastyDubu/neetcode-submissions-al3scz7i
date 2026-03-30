class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count_1, count_2 = [0] * 26, [0] * 26
        for i in range(len(s1)):
            count_1[ord(s1[i]) - ord('a')] += 1
            count_2[ord(s2[i]) - ord('a')] += 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            if count_1 == count_2:
                return True
            
            index = ord(s2[r]) - ord('a')
            count_2[index] += 1
            
            index = ord(s2[l]) - ord('a')
            count_2[index] -= 1

            l += 1
        return count_1 == count_2