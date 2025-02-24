class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        
        adj = defaultdict(list)
        for y, x in edges:
            adj[y].append(x)
            adj[x].append(y)

        visited = set()
        visited.add(bob)
        
        def dfs(num):
            if num == 0:
                return True

            for a in adj[num]:
                if a not in visited:
                    visited.add(a)
                    if dfs(a):
                        return True
                    visited.remove(a)
            
            return False
        
        dfs(bob)

        queue = deque([(0, 0), (0, bob)])
        maxNum = float('-inf')

        dum1 = set()
        dum2 = set()

        while queue:
            cost1, out1 = queue.popleft()
            cost2, out2 = queue.popleft()

            if out1 in dum2 and out2 in dum1:
                pass
            elif out1 in dum2:
                cost2 += amount[out2]
            elif out1 == out2:
                cost1 += amount[out1] / 2
                cost2 +=  amount[out2] / 2
            elif out2 in dum1:
                cost1 += amount[out1]
            else:
                cost1 += amount[out1]
                cost2 += amount[out2]
                
            dum1.add(out1)
            dum2.add(out2)
            
            if len(adj[out1]) == 1 and out1 != 0:
                maxNum = max(maxNum, cost1)
                continue
            
            saved = (cost2, out2)
            for a in adj[out2]:
                if a in visited and a not in dum2:
                    saved = (cost2, a)
            
            for a in adj[out1]:
                if a not in dum1:
                    queue.append((cost1, a))
                    queue.append(saved)
        
        return int(maxNum)
