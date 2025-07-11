class Solution:
    def printVertically(self, s: str) -> List[str]:

        s = s.split(" ")
        maxLen = max(len(elem) for elem in s)

        res = []
        for p in range(maxLen):
            curr = []
            for i in range(len(s)):
                curr.append(s[i][p] if p < len(s[i]) else " ")
                
            while curr and curr[-1] == " ":
                curr.pop()

            res.append(''.join(curr))
        
        return res




        