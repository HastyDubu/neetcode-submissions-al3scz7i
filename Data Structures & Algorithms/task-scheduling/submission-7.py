class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = []
        for t, num in count.items():
            heapq.heappush(maxHeap, -num)
        
        time = 0
        q = deque()
        while maxHeap or q:
            
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                val = 1 + heapq.heappop(maxHeap)
                if val:
                    q.append([val, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time
