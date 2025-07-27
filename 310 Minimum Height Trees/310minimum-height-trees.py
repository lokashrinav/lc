class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        paths = defaultdict(set)
        for y, x in edges:
            paths[y].add(x)
            paths[x].add(y)

        queue = deque()
        visited = set()

        # Find initial leaves (keep your approach)
        for elem in paths:
            if len(paths[elem]) == 1:
                visited.add(elem)
                queue.append(elem)
        
        # Keep your while loop structure
        while queue:
            if len(visited) == n:
                return list(queue)

            next_queue = deque()
            
            # Keep your for loop structure  
            for i in range(len(queue)):
                out = queue.popleft()
                
                # Fix: actually remove the leaf
                for elem in list(paths[out]):
                    paths[elem].remove(out)
                    if elem not in visited and len(paths[elem]) == 1:
                        visited.add(elem)
                        next_queue.append(elem)
                
                # Remove the processed leaf
                del paths[out]
            
            queue = next_queue
        
        return []