class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def check(node1, node2):
            y, x = node1
            if not (x >= 0 and x < length and y < width and y >= 0):
                return False
            y2, x2 = node2
            if heights[y2][x2] > heights[y][x]:
                return False
            return True
        
        length = len(heights[0])
        width = len(heights)
        queue = deque()
        visited_pacific = set()
        visited_atlantic = set()

        # y, x
        for ind in range(length):
            queue.append((0, ind))

        for ind in range(width):
            queue.append((ind, 0))

        while queue:
            for i in range(len(queue)):
                y, x = queue.popleft()
                if (y, x) in visited_pacific:
                    continue
                visited_pacific.add((y, x))
                if check((y, x + 1), (y, x)):
                    queue.append((y, x + 1))                  
                if check((y, x - 1), (y, x)):
                    queue.append((y, x - 1))
                if check((y + 1, x), (y, x)):
                    queue.append((y + 1, x),)
                if check((y - 1, x), (y, x)):
                    queue.append((y - 1, x))

        for ind in range(length):
            queue.append((width - 1, ind))

        for ind in range(width):
            queue.append((ind, length - 1))

        while queue:
            for i in range(len(queue)):
                y, x = queue.popleft()
                if (y, x) in visited_atlantic:
                    continue
                visited_atlantic.add((y, x))
                if check((y, x + 1), (y, x)):
                    queue.append((y, x + 1))                  
                if check((y, x - 1), (y, x)):
                    queue.append((y, x - 1))
                if check((y + 1, x), (y, x)):
                    queue.append((y + 1, x),)
                if check((y - 1, x), (y, x)):
                    queue.append((y - 1, x))
        
        combined = []
        for i in visited_atlantic:
            if i in visited_pacific:
                combined.append(i)
        
        return combined




        

        