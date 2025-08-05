class Solution:
    def getSmallestString(self, n: int, k: int) -> str:

        curr = [1] * n
        total = n

        for i in range(n - 1, -1, -1):
            if k - total <= 25:
                curr[i] += k - total
                break
            else:
                curr[i] += 25
                total += 25

        for i in range(len(curr)):
            curr[i] = chr(curr[i] + 96)
        
        return ''.join(curr)
        