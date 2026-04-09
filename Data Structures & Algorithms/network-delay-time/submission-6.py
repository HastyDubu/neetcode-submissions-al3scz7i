class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for src, dst, t in times:
            adj[src].append([dst, t])
        
        minHeap = [(0, k)]
        visit = set()
        time = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            time = w1
            visit.add(n1)
            for n2, w2 in adj[n1]:
                heapq.heappush(minHeap, [w1 + w2, n2])
        
        return time if len(visit) == n else -1