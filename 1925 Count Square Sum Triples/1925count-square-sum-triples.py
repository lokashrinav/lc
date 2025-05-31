class Solution:
    def countTriples(self, n: int) -> int:

        count = 0
        for i in range(1, n + 1):
            for p in range(i + 1, n + 1):
                calc = ((i ** 2 + p ** 2) ** (1/2))
                if calc % 1 == 0 and calc <= n:
                    count += 2
        
        return count

        