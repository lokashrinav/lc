class Solution:
    def totalReplacements(self, ranks: List[int]) -> int:

        curr = ranks[0]
        count = 0

        for i in range(1, len(ranks)):
            if ranks[i] < curr:
                curr = ranks[i]
                count += 1
                
        return count
        