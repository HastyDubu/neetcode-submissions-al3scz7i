class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            if n not in count:
                count[n] = 0
            count[n] += 1
        for key, n in count.items():
            freq[n].append(key)
        res = []
        for i in range(len(freq) -1, -1, -1):
            for n in freq[i]:
                if len(res) != k:
                    res.append(n) 
        return res
        