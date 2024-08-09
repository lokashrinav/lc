class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        '''
        a = 11, b = 01
        a = 10, b = 10
        a = 000, b = 100 
        c = 100, b = 0000
        '''
        while b != 0:
            carry = a & b
            a = a ^ b
            b = carry << 1
        
        return a
