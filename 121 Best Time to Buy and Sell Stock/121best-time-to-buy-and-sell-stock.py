class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minSoFar = float('inf')

        maxProf = 0
        for i in range(len(prices)):
            if prices[i] < minSoFar:
                minSoFar = prices[i]
            else:
                maxProf = max(maxProf, prices[i] - minSoFar)
        
        return maxProf
        