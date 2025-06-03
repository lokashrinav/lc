class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        s = list(s)

        res = []

        def dfs(ind):
            if ind == len(s):
                return
                        
            if s[ind].isdigit():
                dfs(ind + 1)
            else:
                saved = s[ind]
                #res.append(''.join(s))
                dfs(ind + 1)
                s[ind] = s[ind].upper() if s[ind].lower() == s[ind] else s[ind].lower()
                res.append(''.join(s))
                dfs(ind + 1)
                s[ind] = saved
        
        res.append(''.join(s))

        dfs(0)

        

        return res

        
        