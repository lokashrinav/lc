class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        b, w = 0, 0

        minCount = float('inf')
        for i in range(k):
            if blocks[i] == 'B':
                b += 1
            else:
                w += 1
        minCount = min(minCount, w)
        
        for i in range(k, len(blocks)):
            if blocks[i] == 'B':
                b += 1
            else:
                w += 1
            
            if blocks[i - k] == 'B':
                b -= 1
            else:
                w -= 1

            minCount = min(minCount, w)
        
        return minCount
