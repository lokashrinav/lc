class Solution:
    def addDigits(self, num: int) -> int:
        # 39 % 42 - 1
        # 11 - 1 % k + 1 = 2
        # (11 + 1) % k - 1 
        # k would be either a 13

        # (11 - 1) % k == (39 - 1) % k
        # 10 % k == 2 and 38 % k == 2
        x = (num - 1) % 9 + 1 
        if num == 0:
            return 0
        return x 