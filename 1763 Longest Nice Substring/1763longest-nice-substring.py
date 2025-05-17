class Solution:
    def longestNiceSubstring(self, s: str) -> str:

        fun = [0] * len(s)
        hmap = Counter(s)
        for i in range(len(s)):
            if not (s[i].lower() in hmap and s[i].upper() in hmap):
                fun[i] = 1
        
        fun2 = [None] * len(s)

        hmap = {}
        for i in range(len(s)):
            if fun[i] == 0:
                if s[i].upper() == s[i]:
                    if s[i].lower() in hmap:
                        fun2[i] = hmap[s[i].lower()] 
                elif s[i].lower() == s[i]:
                    if s[i].upper() in hmap:
                        fun2[i] = hmap[s[i].upper()] 

                hmap[s[i]] = i

        fun3 = [None] * len(s)

        hmap2 = {}
        for i in range(len(s) - 1, -1, -1):
            if fun[i] == 0:
                if s[i].upper() == s[i]:
                    if s[i].lower() in hmap2:
                        fun3[i] = hmap2[s[i].lower()] 
                elif s[i].lower() == s[i]:
                    if s[i].upper() in hmap:
                        fun2[i] = hmap[s[i].upper()] 

                hmap2[s[i]] = i
                
        #print(fun, fun2, fun3)

        prev = -1
        for i in range(len(fun)):
            if fun[i] == 0:
                fun[i] = (prev, None)
            else:
                prev = i
        
        prev = len(fun)
        for i in range(len(fun) - 1, -1, -1):
            if fun[i] != 1:
                fun[i] = (fun[i][0], prev)
            else:
                prev = i
        
        print(fun, fun2, fun3)

        maxStr = ""
        str1 = ""
        for i in range(len(fun)):
            if (fun2[i] is not None and fun[i][0] <= fun2[i] <= fun[i][1]) or (fun3[i] is not None and fun[i][0] <= fun3[i] <= fun[i][1]):
                str1 += s[i]
            else:
                str1 = ""
            maxStr = str1 if len(str1) > len(maxStr) else maxStr
        
        return maxStr
            

        '''for i in range(len(s)):
            if fun[i] == 1:
                str1 = ""'''


                

        