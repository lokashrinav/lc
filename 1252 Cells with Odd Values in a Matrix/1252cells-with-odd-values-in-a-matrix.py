class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        
        idk = [0] * m
        idk2 = [0] * n

        for y, x in indices:
            idk[y] += 1
            idk2[x] += 1
        
        total = 0
        for y in range(m):
            for x in range(n):
                if (idk[y] + idk2[x]) % 2 != 0:
                    total += 1
        
        return total