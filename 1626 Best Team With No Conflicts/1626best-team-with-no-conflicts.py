class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        final = [0] * len(ages)
        for i in range(len(ages)):
            final[i] = [ages[i], scores[i]]
        
        final.sort()

        fun = [final[i][0] for i in range(len(final))]
        fun2 = [final[i][1] for i in range(len(final))]

        indices = [0] * len(final)
        indices2 = [0] * len(final)

        for i in range(len(indices)):
            ind = bisect_right(fun, fun[i])
            indices[i] = ind

        for i in range(len(indices)):
            ind = bisect_left(fun, fun[i])
            indices2[i] = ind

        cache = {}

        print(final)
        
        def dfs(i, lowest):

            if i >= len(ages):
                return 0

            if (i, lowest) in cache:
                return cache[(i, lowest)]

            maxNum = dfs(i + 1, lowest)

            if lowest is None or final[i][1] >= lowest:
                new = lowest
                if not (i + 1 < len(ages) and final[i + 1][0] == final[i][0]):
                    if lowest is None:
                        new = final[i][1]
                    new = max(new, final[i][1])
                    maxNum = max(maxNum, final[i][1] + dfs(i + 1, new))
                else:   
                    if lowest is None:
                        new = final[i][1]
                    
                    for p in range(i + 1, indices[i]+1):
                        maxNum = max(maxNum, sum(fun2[i:p]) + dfs(indices[i], max(new, max(fun2[i:p]))))                    
                    
            cache[(i, lowest)] = maxNum

            #print(i, lowest, maxNum)

            return maxNum

        calc = dfs(0, None)

        #print(cache)

        return calc

