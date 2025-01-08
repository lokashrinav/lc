class Solution:
    def countHomogenous(self, s: str) -> int:
        total = 0
        count = 0
        prev = None
        for i in range(len(s)):
            if prev is not None:
                if s[i] == prev:
                    total += 1
                else:
                    count += (total * (total + 1)) / 2
                    total = 1
                prev = s[i]
            else:
                prev = s[i]
                total = 1

        if total:
            count += (total * (total + 1)) / 2
            total = 0

        return int(count) % (10 ** 9 + 7)

        