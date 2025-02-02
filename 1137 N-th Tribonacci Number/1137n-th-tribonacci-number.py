class Solution:
    def tribonacci(self, n: int) -> int:
        p1, p2, p3, = 0, 1, 1
        if n <= 1:
            return n
        elif n == 2:
            return 1
        
        for i in range(3, n + 1):
            calc = p1 + p2 + p3
            p1 = p2
            p2 = p3
            p3 = calc
        
        return calc
            
        
