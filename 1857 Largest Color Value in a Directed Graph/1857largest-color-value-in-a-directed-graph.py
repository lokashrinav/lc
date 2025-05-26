class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:

        paths = defaultdict(list)
        for y, x in edges:
            paths[y].append(x)
        
        def check(num, time):   

            for elem in paths[num]:   
                if elem in curr:
                    return True

                if elem in visited:
                    continue
                
                curr.add(elem)

                if check(elem, time + 1):
                    return True
            
                curr.remove(elem)
                visited.add(elem)
            
            return False
        
        visited = set()
        n = len(colors)

        for i in range(n):
            curr = set()
            curr.add(i)
            if i not in visited:
                if check(i, 0):
                    return -1
        
        visited = {}

        def dfs(num):
            if num in visited:
                return visited[num]

            new = [0] * 26

            for elem in paths[num]:
                arr_copy = dfs(elem)
                for i in range(len(arr_copy)):
                    new[i] = max(arr_copy[i], new[i])
            
            new[ord(colors[num]) - 97] += 1
            
            visited[num] = new.copy()
            
            return new

        maxNum = 1
        for i in range(len(colors)):
            if i not in visited:
                arr = dfs(i)
                maxNum = max(maxNum, max(arr))
        
        return maxNum