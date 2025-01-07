class Solution:
    def maxPower(self, s: str) -> int:

        count = 0
        maxCount = 0
        prev = None
        for i in range(len(s)):
            if not prev:
                count = 1
                maxCount = max(count, maxCount)
                prev = s[i]
            else:
                if prev == s[i]:
                    count += 1
                    maxCount = max(count, maxCount)
                    prev = s[i]
                else:
                    count = 1
                    prev = s[i]

        return maxCount



        