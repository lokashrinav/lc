class Solution:
    def canWinNim(self, n: int) -> bool:
        # 1 -> Player 1
        # 2 -> Player 1 - Make it 1
        # 3 -> Player 1 - Make it 1
        # 4 -> Player 2
        # 5 -> Player 1
        # 6 -> 4 -> Player 1
        # 7 -> 4 -> Player 1
        # 8 -> Player 2
        # 9-11 -> 
        # 12
        if n % 4 == 0:
            return False
        return True
