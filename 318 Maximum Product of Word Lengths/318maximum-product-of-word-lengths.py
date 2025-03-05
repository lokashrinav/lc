class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        bitmasks = [0] * n
        lengths = [0] * n

        for i in range(len(words)):
            mask = 0
            for ch in words[i]:
                mask |= 1 << ord(ch) - ord('a')
            bitmasks[i] = mask
            lengths[i] = len(words[i])
        
        max_prod = 0
        for i in range(n):
            for p in range(i + 1, n):
                if bitmasks[i] & bitmasks[p] == 0:
                    max_prod = max(max_prod, lengths[i] * lengths[p])
        
        return max_prod

        