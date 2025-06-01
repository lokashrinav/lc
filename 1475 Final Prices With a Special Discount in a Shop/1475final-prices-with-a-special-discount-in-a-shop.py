class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        '''



        '''

        stack = []

        for i in range(len(prices) - 1, -1, -1):
            while stack and stack[-1] > prices[i]:
                stack.pop()
            
            minNum = stack[-1] if stack else 0

            stack.append(prices[i])

            prices[i] -= minNum
        
        return prices
        



        