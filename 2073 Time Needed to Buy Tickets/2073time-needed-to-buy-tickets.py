class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:

        '''
        1, 1, 1, 4
        '''

        total = 0
        if k != len(tickets) - 1:
            total = k+1

            for i in range(k+1):
                tickets[i] -= 1

            if tickets[k] == 0:
                return total
        
        print(tickets, total)
        
        for i in range(k+1, k + len(tickets)+1):
            total += min(tickets[k], tickets[i % len(tickets)])
        
        print(tickets)
        
        return total

        


        