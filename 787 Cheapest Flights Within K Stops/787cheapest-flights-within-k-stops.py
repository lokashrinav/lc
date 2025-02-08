class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        idk = [float('inf')] * n
        idk[src] = 0

        for i in range(k + 1):
            tmp = idk[:]
            for fro, yo, price in flights:
                if idk[fro] != float('inf') and idk[fro] + price < tmp[yo]:
                    tmp[yo] = idk[fro] + price
            idk = tmp

        return idk[dst] if idk[dst] != float('inf') else -1



