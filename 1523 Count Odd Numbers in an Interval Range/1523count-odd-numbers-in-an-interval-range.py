class Solution:
    def countOdds(self, low: int, high: int) -> int:

        return ((high + 1 - low) + (1 if low % 2 else 0)) // 2
        