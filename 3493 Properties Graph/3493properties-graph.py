class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:

        def intersect(i, p):
            count = 0
            hset = set()
            for elem in properties[i]:
                hset.add(elem)

            hset2 = set()
            for elem in properties[p]:
                if elem in hset and elem not in hset2:
                    count += 1
                hset2.add(elem)

            return count
            
        adj = defaultdict(list)

        for i in range(len(properties)):
            for p in range(i + 1, len(properties)):
                if intersect(i, p) >= k:
                    adj[i].append(p)
                    adj[p].append(i)

        def dfs(num):
            if num in visited:
                return
            visited.add(num)
            for elem in adj[num]:
                dfs(elem)

        visited = set()
        total = 0
        
        for i in range(len(properties)):
            if i not in visited:
                dfs(i)
                total += 1

        return total