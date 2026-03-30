class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = {}

        for w in strs:
            c_count = [0] * 26
            for c in w:
                index = ord(c) - ord('a')
                c_count[index] += 1
            tup = tuple(c_count) 
            if tup not in count:
                count[tup] = []
            count[tup].append(w)

        res = []
        for item in count.values():
            res.append(item)
        
        return res
