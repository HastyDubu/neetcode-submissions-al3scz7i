class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        maxHeap = [-v for v in counter.values()]
        heapq.heapify(maxHeap)

        q = deque()
        time = 0
        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]

            if maxHeap:
                val = heapq.heappop(maxHeap) + 1
                if val != 0:
                    q.append([val, time + n])

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time