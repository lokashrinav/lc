class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        memo = {}

        def dfs(ind, M, flag):
            if ind >= len(piles):
                return 0
            
            if (ind, M, flag) in memo:
                return memo[(ind, M, flag)]
            
            curr = 0
            maxNum = 0 if flag else float('inf')

            #print(ind, M, flag)

            for i in range(ind, min(len(piles), ind + 2 * M)):
                curr += piles[i]

                if flag:
                    maxNum = max(maxNum, curr + dfs(i + 1, max(M, i - ind + 1), False))
                else:
                    maxNum = min(maxNum, dfs(i + 1, max(M, i - ind + 1), True))
            
            #print(ind, M, flag, maxNum)

            memo[(ind, M, flag)] = maxNum
            
            return maxNum

        return dfs(0, 1, True)



