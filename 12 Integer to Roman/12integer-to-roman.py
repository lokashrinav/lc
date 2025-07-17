class Solution:
    def intToRoman(self, num: int) -> str:
        arr = [(1, "I"), (4, "IV"), (5, "V"), (9, "IX"), (10, "X"), (40, "XL"), (50, "L"), (90, "XC"), (100, "C"), (400, "CD"), (500, "D"), (900, "CM"), (1000, "M")]

        p1 = len(arr) - 1
        res = ""

        while p1 >= 0:
            if num >= arr[p1][0]:
                count = num // arr[p1][0]
                num = num % arr[p1][0]
                res += arr[p1][1] * count
                p1 -= 1
            else:
                p1 -= 1
        
        return res