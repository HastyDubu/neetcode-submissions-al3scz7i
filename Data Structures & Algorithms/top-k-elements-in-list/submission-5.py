class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = {}
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            if n not in buckets:
                buckets[n] = 0
            buckets[n] += 1
        
        for n, f in buckets.items():
            freq[f].append(n)
        
        res = []
        for i in range(len(freq) -1 , -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res