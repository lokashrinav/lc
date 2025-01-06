class Solution:
    def countEven(self, num: int) -> int:
        if sum([int(i) for i in str(num)]) % 2 == 0:
            return num // 2
        else:
            return (num-1) // 2