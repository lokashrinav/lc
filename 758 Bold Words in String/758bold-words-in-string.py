class Solution:
    def boldWords(self, words: List[str], s: str) -> str:

        s2 = s
        s = list(s)
        curr = [0] * len(s)

        for i in range(len(s)):
            flag = 0
            for p in range(len(words)):
                #print(s[i:i+len(words[p])], words[p])
                if s2[i:i+len(words[p])] == words[p]:
                    flag = max(flag, len(words[p]))

            if flag:
                for p in range(i, i + flag):
                    curr[p] = 1
        
                
        res = []
        for i in range(len(s)):
            if curr[i] == 1 and (i == 0 or curr[i - 1] == 0):
                res.append("<b>")
            res.append(s[i])
            if curr[i] == 1 and (i == len(s) - 1 or curr[i + 1] == 0):
                res.append("</b>")
        
        return ''.join(res)

        