class Solution:
    def clearStars(self, s: str) -> str:

        arr = [[] for i in range(26)]

        for i in range(len(s)):
            if s[i] != "*":
                arr[ord(s[i]) - 97].append(i)
            else:
                for i in range(26):
                    if arr[i]:
                        arr[i].pop()
                        break
        
        final = [""] * len(s)

        for i in range(len(arr)):
            for p in range(len(arr[i])):
                final[arr[i][p]] = s[arr[i][p]]

        return ''.join(final)

        
        