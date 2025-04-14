class Solution:
    def parseTernary(self, expression: str) -> str:

        exp = expression
        def dfs(ind):
            if ind == len(expression) - 1 or exp[ind].isdigit() or exp[ind + 1] == ':':
                return (exp[ind], ind)
            
            idk = expression[ind:].split("?", 1)

            if idk[0] == 'T':
                val, new_ind = dfs(ind + 2)
                yo, final_ind = dfs(new_ind + 2)
                return (val, final_ind)
            else:
                val, new_ind = dfs(ind + 2)
                yo, final_ind = dfs(new_ind + 2)
                return (yo, final_ind)

        return dfs(0)[0]