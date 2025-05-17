class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        
        minHeap = mat[0].copy()

        hmap = {elem: 1 for elem in mat[0]}

        for i in range(1, len(mat)):
            for p in range(len(mat[0])):
                if mat[i][p] in hmap:
                    hmap[mat[i][p]] += 1
            
            while minHeap and hmap[minHeap[0]] < i + 1:
                heappop(minHeap)
            
            if not minHeap:
                return -1
        
        return minHeap[0]

