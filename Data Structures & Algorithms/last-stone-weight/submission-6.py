class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones) 
            if x != y:
                heapq.heappush(stones, x - y)
        
        heapq.heappush(stones, 0)
        return stones[0] * -1