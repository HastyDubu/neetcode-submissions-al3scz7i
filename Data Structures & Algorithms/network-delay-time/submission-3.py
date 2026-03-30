class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for src, dst, wei in times:
            adj[src].append([dst, wei])
        
        minHeap = [[0, k]]
        time = 0
        visit = set()
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            
            if n1 in visit:
                continue
            visit.add(n1)
            time = w1

            for n2, w2 in adj[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, [w1 + w2, n2])

        return time if len(visit) == n else -1
        