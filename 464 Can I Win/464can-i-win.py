class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        gaus = (maxChoosableInteger * (maxChoosableInteger + 1)) / 2
        memo = {}
        if gaus < desiredTotal:
            return False
        if gaus == desiredTotal:
            return maxChoosableInteger % 2 == 1
        
        def canWin(choices, remainder):
            if choices[-1] >= remainder:
                return True

            tup = tuple(choices)

            if tup in memo:
                return memo[tup]
            
            for i in range(len(choices)):
                smth = canWin(choices[:i] + choices[i+1:], remainder - choices[i])
                if not smth:
                    memo[tup] = True
                    return memo[tup]
                
            memo[tup] = False
            return memo[tup]
                    
        return canWin(list(range(1, maxChoosableInteger + 1)), desiredTotal)
        