class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        
        res = []

        curr = ""

        for i in range(len(s)):
            curr += s[i]
            if (i + 1) % k == 0:
                res.append(curr)
                curr = ""

        if curr:   
            while len(curr) < k:
                curr += fill
            
            res.append(curr)
        
        return res
        