class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:

        if len(original) != m * n:
            return []
        
        i = 0
        final = [([0] * n) for p in range(m)]

        print(final)

        while i < len(original):
            print(i, i // 2, i % n)
            final[i // n][i % n] = original[i]
            i += 1
        
        return final
        