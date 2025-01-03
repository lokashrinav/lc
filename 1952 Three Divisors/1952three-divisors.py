class Solution:
    def isThree(self, n: int) -> bool:
        count = 0
        for i in range(1, (n // 2) + 1):
            if n % i == 0 and i * i == n:
                count += 1
            elif n % i == 0:
                count += 2
        print(count)
        return count == 3
        