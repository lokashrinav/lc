class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        if len(s) > 12:
            return []

        def works(curr):
            if not curr:
                return False
            if curr[0] == '0' and len(curr) != 1:
                return False
            if len(curr) > 3:
                return False
            if 0 <= int(''.join(curr)) <= 255:
                return True
            return False
        
        res = []
        
        def dfs(ind, final):
            if ind == len(s) and final and len(final) == 4 and works(final[-1]):
                res.append('.'.join(''.join(fun) for fun in final))
                return
            elif ind == len(s):
                return 

            if not final:
                final.append([])
            
            final[-1].append(s[ind])

            if works(final[-1]):
                final.append([])
                dfs(ind + 1, final)
                final.pop()

            dfs(ind + 1, final)

            final[-1].pop()

        dfs(0, [])

        return res

        