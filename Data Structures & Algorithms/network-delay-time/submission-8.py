class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for src, dst, w in times:
            adj[src].append([dst, w])
        
        minHeap = [[0, k]]
        visit = set()
        time = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            time = w1
            for n2, w2 in adj[n1]:
                heapq.heappush(minHeap, [w2 + w1, n2])
        return time if len(visit) == n else -1
            