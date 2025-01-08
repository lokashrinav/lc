class Solution:
    def numSub(self, s: str) -> int:
        
        total = 0
        count = 0
        for i in range(len(s)):
            if s[i] == '1':
                total += 1
            else:
                count += (total * (total + 1)) / 2
                total = 0

        if total:
            count += (total * (total + 1)) / 2
            total = 0

        return int(count) % (10 ** 9 + 7)


        