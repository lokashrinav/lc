class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = 0
        emptyBottles = 0
        while numBottles:
            print(numBottles, emptyBottles)
            total += numBottles
            emptyBottles += numBottles
            newBottles = emptyBottles // numExchange
            emptyBottles = emptyBottles % numExchange
            numBottles = newBottles
        return total