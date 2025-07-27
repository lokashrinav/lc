class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        '''
        dp[i] = max(power[i] + dp[i + 1], dp[i + 3])

        1, 3, 6, 7

        [11, 10, 7, 7]

        '''

        hmap = Counter(power)
        total = {}
        for key in hmap:
            total[key] = hmap[key] * key

        power = list(hmap.keys())

        power.sort()

        dp = [0] * len(power)
        for i in range(len(power) - 1, -1, -1):
            saved = saved2 = None
            for p in range(i, min(i + 4, len(power))):
                if abs(power[i] - power[p]) >= 3:
                    saved = p
                    break

            if i + 1 < len(power):
                saved2 = i + 1

            #print(len(dp), saved2)
            calc1 = dp[saved2] if saved2 is not None else 0
            calc2 = dp[saved] if saved is not None else 0
            #print(i, power[i], total[power[i]], calc2, calc1)
            dp[i] = max(total[power[i]] + calc2, calc1)
        
        print(dp)

        return max(dp)


        

        

