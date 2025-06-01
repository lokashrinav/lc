class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:

        s = text.split(" ")
        res = []

        for i in range(2, len(s)):
            if s[i - 2] == first and s[i - 1] == second:
                res.append(s[i]) 
        
        return res
        