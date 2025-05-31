class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:

        minNum1 = min(prices)
        prices.remove(minNum1)
        minNum2 = min(prices)
        
        if minNum1 + minNum2 > money:
            return money
        
        return money - (minNum1 + minNum2)
