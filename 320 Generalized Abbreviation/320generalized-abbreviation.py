class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        
        res = []
        def dfs(ind, abb, current):
            if ind == len(word):
                if abb > 0:
                    current += str(abb)
                res.append(current)
                return
            
            dfs(ind + 1, abb + 1, current)

            if abb > 0:
                current += str(abb)
            
            dfs(ind + 1, 0, current + word[ind])
        
        dfs(0, 0, "")
        return res

        
        
