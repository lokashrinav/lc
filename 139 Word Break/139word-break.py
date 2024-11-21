class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        res = [False] * (len(s) + 1)
        res[0] = True

        for i in range(len(s)):
            if res[i] == True:
                for word in wordDict:
                    length = len(word)
                    print()
                    if word == s[i:i+length]:
                        res[i+length] = True
        print(res)
        return res[-1]                    


            
            


        