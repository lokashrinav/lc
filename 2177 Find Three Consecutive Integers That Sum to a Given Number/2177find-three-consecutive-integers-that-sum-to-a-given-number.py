class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        # n * (n + 1) / 2 - (n - 3) * (n - 2) / 2 = num
        # 6 * 13 - 9 * 4
        # 78 - 45 = 33

        if num % 3 != 0:
            return []
        
        x = int((num + 3) / 3)

        return [x - 2, x - 1, x]
    