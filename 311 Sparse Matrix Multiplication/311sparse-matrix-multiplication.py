class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m = len(mat1)
        n = len(mat1[0])
        k = len(mat2[0])

        hmap = defaultdict(list)
        for i in range(m):
            for p in range(n):
                if mat1[i][p] != 0:
                    hmap[i].append(p)
        
        hmap2 = defaultdict(list)
        for i in range(n):
            for p in range(k):
                if mat2[i][p] != 0:
                    hmap2[p].append(i)

        new_mat = [[0 for i in range(k)] for p in range(m)]

        def dop(arr1, arr2, i, p):
            total = 0
            print(i, p, hmap, hmap2)
            for key in hmap[i]:
                if key in hmap2[p]:
                    total += arr1[key] * arr2[key]
                
            return total
                
        for i in range(m):
            for p in range(k):
                new_mat[i][p] = dop(mat1[i], [mat2[z][p] for z in range(n)], i, p)
        
        return new_mat





