class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)
        
        if len(self.large) > 1 + len(self.small):
            val = heapq.heappop(self.large) * -1
            heapq.heappush(self.small, val)
        if len(self.large) + 1 < len(self.small):
            val = heapq.heappop(self.small) * -1
            heapq.heappush(self.large, val)

    def findMedian(self) -> float:
        if len(self.small) < len(self.large):
            return self.large[0]
        elif len(self.large) < len(self.small):
            return self.small[0] * -1
        else:
            return ((self.small[0] * -1) + (self.large[0])) / 2
        