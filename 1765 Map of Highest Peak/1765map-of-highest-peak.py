class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        def surround(i, p, count, queue):
            if i + 1 < len(isWater):
                queue.append((i + 1, p, count))
            if i - 1 >= 0:
                queue.append((i - 1, p, count))
            if p - 1 >= 0:
                queue.append((i, p - 1, count))
            if p + 1 < len(isWater[0]):
                queue.append((i, p + 1, count))

        m = len(isWater)
        n = len(isWater[0])

        queue = deque()
        for i in range(m):
            for p in range(n):
                if isWater[i][p] == 1:
                    queue.append((i, p, 0))
        
        visited = set()
        while queue:
            out = queue.popleft()
            i, p, count = out
            if (i, p) in visited:
                continue
            visited.add((i, p))
            isWater[i][p] = count
            surround(i, p, count + 1, queue)
        
        return isWater






        


        
        