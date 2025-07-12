class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:

        hmap = {}
        for key, val in knowledge:
            hmap[key] = val

        i = 0
        res = []
        while i < len(s):
            if s[i] == "(":
                curr = ""
                while s[i + 1] != ")":
                    i += 1
                    curr += s[i]
                res.append(hmap[curr] if curr in hmap else "?")
            elif s[i] != ")":
                res.append(s[i])
            i += 1
        
        return ''.join(res)


        