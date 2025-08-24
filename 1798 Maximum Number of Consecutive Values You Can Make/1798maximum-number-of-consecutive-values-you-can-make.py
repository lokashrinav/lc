class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        reach = 0
        for c in sorted(coins):
            if c > reach + 1:
                return reach + 1
            reach += c
        return reach + 1
