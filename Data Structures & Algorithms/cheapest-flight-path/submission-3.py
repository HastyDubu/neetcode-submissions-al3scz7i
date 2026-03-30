class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf") for _ in range(n)]
        prices[src] = 0

        for i in range(k + 1):  
            tmpPrices = prices.copy()
            for s, d, cost in flights:
                if prices[s] == float("inf"):
                    continue
                tmpPrices[d] = min(tmpPrices[d], prices[s] + cost)
            prices = tmpPrices
        
        return prices[dst] if prices[dst] != float("inf") else -1
