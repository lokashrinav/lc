class Solution:
    def longestCycle(self, edges: List[int]) -> int:

        visited = {}
        back = set()
        def dfs(num, count):
            if num == -1:
                return -1

            if num in visited:
                return count - visited[num]
            
            if num in back:
                return -1

            visited[num] = count
            back.add(num)
            
            return max(dfs(edges[num], count + 1), -1)            
            
        maxNum = -1
        for i in range(len(edges)):
            visited = {}
            maxNum = max(dfs(i, 0), maxNum)
        
        return maxNum 

        