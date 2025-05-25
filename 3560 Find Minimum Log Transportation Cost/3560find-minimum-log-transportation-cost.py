class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:

        cost1 = 0
        if n > k:
            cost1 = (n - k) * k
        cost2 = 0
        if m > k:
            cost2 = (m - k) * k

        return cost1 + cost2
            

            
                
                

        

        

        
        