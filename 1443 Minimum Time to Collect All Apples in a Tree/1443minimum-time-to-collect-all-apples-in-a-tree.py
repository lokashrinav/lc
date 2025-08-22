class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:

        paths = defaultdict(list)

        for y, x in edges:
            paths[y].append(x)
            paths[x].append(y)

        total = 0
        visited = set()
        visited.add(0)
        def dfs(num, so):
            nonlocal total
            count = 1 if hasApple[num] else 0
            for elem in paths[num]:
                if elem in visited:
                    continue
                visited.add(elem)
                calc = dfs(elem, so + 1)
                count += calc

            if count and num != 0:
                total += 1
            print(num, total)
            
            return count

        dfs(0, 0)

        return total * 2
        