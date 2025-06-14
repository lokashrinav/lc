class Solution:
    def expand(self, s: str) -> List[str]:

        final = []
        def dfs(ind, curr):
            if ind >= len(s):
                final.append(curr)
                return

            if s[ind] == "{":
                res = []
                while s[ind] != "}":
                    if s[ind].isalpha():
                        res.append(s[ind])
                    ind += 1
                res.sort()

                for elem in res:
                    dfs(ind + 1, curr + elem)
            else:
                dfs(ind + 1, curr + s[ind])

        dfs(0, "")

        return final

        