class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        cols = [0] * len(matrix[0])
        rows = [0] * len(matrix)
        answers = [[0] * len(matrix[0]) for i in range(len(matrix))]
        minHeap = []
        hmap = defaultdict(list)

        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if matrix[y][x] not in hmap:
                    heappush(minHeap, (matrix[y][x]))
                hmap[matrix[y][x]].append((y, x))
    
        class UnionFind:
            def __init__(self, positions):
                self.parent = {pos: pos for pos in positions}
                self.rank = {pos: 0 for pos in positions}
            
            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]
            
            def union(self, x, y):
                px, py = self.find(x), self.find(y)
                if px == py:
                    return
                if self.rank[px] < self.rank[py]:
                    px, py = py, px
                self.parent[py] = px
                if self.rank[px] == self.rank[py]:
                    self.rank[px] += 1
        
        while minHeap:
            num = heappop(minHeap)
            positions = hmap[num]
            
            # Union-Find on positions directly
            uf = UnionFind(positions)
            
            # Group by rows and columns
            rows_dict = defaultdict(list)
            cols_dict = defaultdict(list)
            for pos in positions:
                y, x = pos
                rows_dict[y].append(pos)
                cols_dict[x].append(pos)
            
            # Union within same rows and columns
            for pos_list in rows_dict.values():
                for i in range(len(pos_list) - 1):
                    uf.union(pos_list[i], pos_list[i + 1])
            
            for pos_list in cols_dict.values():
                for i in range(len(pos_list) - 1):
                    uf.union(pos_list[i], pos_list[i + 1])
            
            # ADD THIS: Group positions by connected components
            components = defaultdict(list)
            for pos in positions:
                root = uf.find(pos)
                components[root].append(pos)
            
            # ADD THIS: Assign ranks to each component
            for component in components.values():
                # Find max rank needed for this component
                max_rank_needed = 0
                for y, x in component:
                    max_rank_needed = max(max_rank_needed, max(rows[y], cols[x]) + 1)
                
                # Assign rank to all positions in component
                for y, x in component:
                    answers[y][x] = max_rank_needed
                    rows[y] = max(rows[y], max_rank_needed)
                    cols[x] = max(cols[x], max_rank_needed)

        return answers