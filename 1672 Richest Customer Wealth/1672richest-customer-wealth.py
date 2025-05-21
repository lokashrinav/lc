class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        total = 0
        for i in range(len(accounts)):
            total = max(total, sum(accounts[i]))
        
        return total
        

        