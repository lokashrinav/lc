class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:

        #return 0.5

        '''

        2.5

        0.4 0.6 0.4 0.6

        0.24, 0.24, 0.16, 0.24, 0.24, 0.36

        0.5 

        0.4, 0.6, 0.4, 0.6

        4
        1

        '''


        cache = {}

        def dfs(ind, count):
            if ind == len(prob):
                if count == target:
                    return 1
                return 0
            if count > target:
                return 0
            
            if (ind, count) in cache:
                return cache[(ind, count)]
            
            calc1 = prob[ind] * dfs(ind + 1, count + 1)

            calc2 = (1 - prob[ind]) * dfs(ind + 1, count)
            
            cache[(ind, count)] = calc1 + calc2

            return calc1 + calc2
        
        return dfs(0, 0)
                


        '''

        1

        0.4 * 0.4 * 0.6 * 0.4

        0.6 * 0.6 * 0.6 * 0.4

        0.6 * 0.4 * 0.4 * 0.4

        0.6 * 0.4 * 0.6 * 0.6




        

        '''
        
        