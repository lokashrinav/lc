class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp = [0] * (amount + 1)
        for i in range(1,amount + 1):
            minList = []
            for p in range(len(coins)):
                if i - coins[p] >= 0 and dp[i - coins[p]] != -1:
                    minList.append(dp[i - coins[p]] + 1)
            if not minList:
                dp[i] = -1
            else:
                dp[i] = min(minList)
        print(dp)
        return dp[-1]
        



                
                    

