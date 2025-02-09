class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visited = set()
        def dfs(num):
            if num in visited:
                return 
            visited.add(num)
            for num2 in rooms[num]:
                dfs(num2)
            
        dfs(0)

        return len(visited) == len(rooms)
        