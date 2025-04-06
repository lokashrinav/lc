class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        memo = {}
        def dfs(day, ind):
            if day in memo:
                return memo[day]
                
            if day > days[-1]:
                return 0
            
            while ind < len(days) and day > days[ind]:
                ind += 1
            
            if ind >= len(days):
                return 0

            minNum = float('inf')
            if day == days[ind]:
                minNum = min(minNum, costs[0] + dfs(day + 1, ind))
            
            if day + 7 >= days[ind]:
                minNum = min(minNum, costs[1] + dfs(day + 7, ind))

            if day + 30 >= days[ind]:
                minNum = min(minNum, costs[2] + dfs(day + 30, ind))
            
            if day < days[ind]:
                minNum = min(minNum, dfs(days[ind], ind))

            memo[day] = minNum

            return minNum

        return dfs(0, 0)
        