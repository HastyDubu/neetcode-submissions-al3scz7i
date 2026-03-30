class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append([t, v])
        
        minHeap = [[0, k]]
        time = 0
        visit = set()
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)

            if n1 in visit:
                continue
            
            visit.add(n1)
            t = w1

            for w2, n2 in adj[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, [w2 + t, n2])
        
        return t if len(visit) == n else -1