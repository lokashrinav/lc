class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        

        res = []
        for elem in s:
            if elem != '-':
                res.append(elem)
        
        res2 = []
        curr = ""
        for i in range(len(res) - 1, -1, -1):
            if len(curr) == k:
                curr = curr[::-1]
                res2.append(curr)
                curr = ""
            
            curr += res[i].upper() if res[i].isalpha() else res[i]

        if curr:
            curr = curr[::-1]
            res2.append(curr)

        print(res2)
        
        return '-'.join(res2[::-1])
        
