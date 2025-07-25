class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:

        even = 0
        for i in range(len(position)):
            if position[i] % 2 == 0:
                even += 1
        
        return min(even, len(position) - even)
        