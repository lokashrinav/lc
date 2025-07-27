class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        '''

        

        '''

        hmap = Counter(nums)
        total = {}

        for key in hmap:
            total[key] = hmap[key] * key

        fun = list(total.keys())
        fun.sort()
        dp = [0] * len(fun)

        for i in range(len(dp)):
            if i - 1 >= 0 and fun[i] - fun[i - 1] > 1:
                saved2 = dp[i - 1]
                saved1 = dp[i - 1]
            elif i - 1 < 0:
                saved1 = 0
                saved2 = 0
            else:
                saved1 = dp[i - 1]
                saved2 = dp[i - 2] if i - 2 >= 0 else 0

            dp[i] = max(total[fun[i]] + saved2, saved1)
        
        print(dp)

        '''
        1, 3
        '''
        
        return max(dp)