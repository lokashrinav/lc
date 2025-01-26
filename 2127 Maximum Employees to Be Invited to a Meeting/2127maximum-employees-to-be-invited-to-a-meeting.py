class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        visited = [False] * len(favorite)

        longest_cycle = 0
        long2 = []
        for i in range(len(favorite)):
            if visited[i]:
                continue
            
            start = curr = i
            curr_set = set()
            while not visited[curr]:
                visited[curr] = True
                curr_set.add(curr)
                curr = favorite[curr]
            
            if curr in curr_set:
                length = len(curr_set)
                while start != curr:
                    start = favorite[start]
                    length -= 1
                longest_cycle = max(longest_cycle, length)
                if length == 2:
                    long2.append((curr, favorite[curr]))
            
        hmap = defaultdict(list)
        for src, dst in enumerate(favorite):
            hmap[dst].append(src)
        
        def bfs(src, dst):
            q = deque([(src, 0)])
            max_length = 0

            while q:
                node, length = q.popleft()
                if node == dst:
                    continue
                max_length = max(max_length, length)
                for nei in hmap[node]:
                    q.append((nei, length + 1))

            return max_length

        chain_sum = 0
        for n1, n2 in long2:
            chain_sum += bfs(n1, n2) + bfs(n2, n1) + 2
        
        return max(chain_sum, longest_cycle)




        