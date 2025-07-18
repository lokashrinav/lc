class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        '''
        [7, 1, 5, 3, 6, 4]
        '''
        curr = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < curr:
                curr = prices[i]
            maxProf = max(prices[i] - curr, maxProf)
        
        return maxProf


        