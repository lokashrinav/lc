class Solution:
    def pushDominoes(self, dominoes: str) -> str:

        dom = list(dominoes)

        hmap = {}

        queue = deque()
        for i in range(len(dominoes)):
            if dom[i] in 'LR':
                queue.append((i, 0, dom[i]))
        
        visited = {}

        while queue:
            # print(queue, visited)
            out, val, og = queue.popleft()
            if out not in visited:
                visited[out] = (og, val)
            elif visited[out][1] == val and visited[out][0] != og:
                visited[out] = ('.', val)
            elif visited[out][1] > val:
                visited[out] = (og, val)
            else:
                continue

            if og == 'L' and out - 1 >= 0 and dom[out - 1] == '.':
                queue.append((out - 1, val + 1, og))

            if og == 'R' and out + 1 < len(dom) and dom[out + 1] == '.':
                queue.append((out + 1, val + 1, og))
            
        str1 = ""
        for i in range(len(dom)):
            if i not in visited:
                str1 += '.'
            else:
                str1 += visited[i][0]
        
        return str1

        