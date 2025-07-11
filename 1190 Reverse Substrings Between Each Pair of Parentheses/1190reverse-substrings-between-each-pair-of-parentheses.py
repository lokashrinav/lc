class Solution:
    def reverseParentheses(self, s: str) -> str:

        '''



        '''

        def dfs(ind):
            i = ind
            curr = ""
            while i < len(s):
                if s[i] == "(":
                    str1, i = dfs(i + 1)
                    str1 = str1[::-1]
                    curr += str1
                elif s[i] == ")":
                    return (curr, i + 1)
                else:
                    curr += s[i]
                    i += 1
            
            return (curr, ind + 1)

        str1, ind = dfs(0)

        return str1