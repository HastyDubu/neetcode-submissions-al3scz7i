class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        visited = {}
        for n in nums:
            if n not in visited:
                visited[n] = 0
            visited[n] += 1
        
        buckets = {}
        for i in visited:
            if visited[i] not in buckets:
                buckets[visited[i]] = []
            buckets[visited[i]].append(i)
        
        res = []
        n = len(nums)
        while len(res) < k:
            if n in buckets:
                for i in buckets[n]:
                    if len(res) < k:
                        res.append(i)
            n -= 1

        return res


            