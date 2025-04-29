from collections import defaultdict
from typing import List

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, n, k = len(mat1), len(mat1[0]), len(mat2[0])
        
        # Store nonzero elements of mat1
        hmap = defaultdict(list)
        for i in range(m):
            for j in range(n):
                if mat1[i][j] != 0:
                    hmap[i].append((j, mat1[i][j]))  # Store index and value
        
        # Store nonzero elements of transposed mat2
        hmap2 = defaultdict(list)
        for j in range(n):
            for p in range(k):
                if mat2[j][p] != 0:
                    hmap2[p].append((j, mat2[j][p]))  # Store index and value
        
        # Result matrix
        new_mat = [[0] * k for _ in range(m)]
        
        # Compute product
        for i in range(m):
            for p in range(k):
                sum_val = 0
                nonzero_1 = hmap[i]
                nonzero_2 = {j: val for j, val in hmap2[p]}  # Convert list to dictionary for O(1) lookup
                
                for j, v1 in nonzero_1:
                    if j in nonzero_2:
                        sum_val += v1 * nonzero_2[j]

                new_mat[i][p] = sum_val
        
        return new_mat
