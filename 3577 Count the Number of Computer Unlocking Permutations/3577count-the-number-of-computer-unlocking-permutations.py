class Solution:
    def countPermutations(self, complexity: List[int]) -> int:

        first = complexity[0]
        for i in range(1, len(complexity)):
            if complexity[i] <= first:
                return 0

        return math.factorial(len(complexity) - 1) % (10 ** 9 + 7)

        
        
        
        