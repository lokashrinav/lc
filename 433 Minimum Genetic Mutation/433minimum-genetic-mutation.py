class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        queue = deque([startGene])
        count = 0
        res = ['A', 'C', 'G', 'T']

        hmap = defaultdict(list)

        for i in range(len(bank)):
            for p in range(len(bank[i])):
                for v in range(4):
                    new_str = bank[i][:p] + res[v] + bank[i][p+1:]
                    hmap[new_str].append(bank[i])
        
        visited = set()
        while queue:
            for i in range(len(queue)):
                out = queue.popleft()
                if out in visited:
                    continue
                
                visited.add(out)
                
                if out == endGene:
                    return count
                
                for elem in hmap[out]:
                    queue.append(elem)

            count += 1

        return -1

