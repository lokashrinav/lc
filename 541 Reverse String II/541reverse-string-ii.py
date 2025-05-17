class Solution:
    def reverseStr(self, s: str, k: int) -> str:

        idk = 0
        res = []
        curr = ""
        res2 = []
        for i in range(len(s)):
            #print(idk)
            if idk < k:
                res.append(s[i])
                idk += 1
            elif idk == 2 * k - 1:
                res2.append(s[i])
                curr += ''.join(res[::-1]) + ''.join(res2)
                res, res2 = [], []
                idk = 0
            else:
                res2.append(s[i])
                idk += 1
        
        if res:
            curr += ''.join(res[::-1]) 
        if res2:
            curr += ''.join(res2)
        
        return curr

        