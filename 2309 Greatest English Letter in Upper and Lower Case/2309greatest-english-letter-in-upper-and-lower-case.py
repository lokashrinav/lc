class Solution:
    def greatestLetter(self, s: str) -> str:

        hset = set(list(s))

        maxL = ""
        for elem in s:
            if elem.lower() in hset and elem.upper() in hset:
                maxL = max(elem.upper(), maxL)
        
        return maxL

        