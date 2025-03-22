class Solution:
    def minSteps(self, n: int) -> int:
        
        memo = {}
        saved = [float('inf')]
        def dfs(pad, screen):
            if screen > n:
                return 1000
            if screen == n:
                return 0    

            if (pad, screen) in memo:
                return memo[(pad, screen)]
            
            minNum = float('inf')
            if screen and pad != screen:
                minNum = min(minNum, 1 + dfs(screen, screen))

            if pad:
                minNum = min(minNum, 1 + dfs(pad, screen + pad))

            memo[(pad, screen)] = minNum

            return minNum

        return dfs(0, 1)