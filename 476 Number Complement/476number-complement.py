class Solution:
    def findComplement(self, num: int) -> int:
        bit = num.bit_length()
        mask = (1 << bit) - 1
        return num ^ mask
        