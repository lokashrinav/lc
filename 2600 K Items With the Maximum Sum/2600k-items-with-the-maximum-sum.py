class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        
        total = 0
        if k > numOnes:
            k -= numOnes
            total += numOnes
        else:
            return k
        
        if k > numZeros:
            k -= numZeros
        else:
            return total
        
        return total - k

        
