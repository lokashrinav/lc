class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        count = len(piles) // 3
        total = 0
        print(piles)
        for i in range(1, len(piles) - count, 2):
            total += piles[i]

        return total


                



        