class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:

        s1 = Counter(s1.split(" "))
        s2 = Counter(s2.split(" "))

        res = []
        for elem in s1:
            if elem not in s2 and s1[elem] == 1:
                res.append(elem)

        for elem in s2:
            if elem not in s1 and s2[elem] == 1:
                res.append(elem)
        
        return res

        
        