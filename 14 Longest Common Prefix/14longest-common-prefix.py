class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        new_str = ""
        minNum = float('inf')
        for i in range(len(strs)):
            minNum = min(minNum, len(strs[i]))

        for p in range(minNum):
            for i in range(len(strs)):
                if strs[i][p] != strs[0][p]:
                    return new_str
            new_str += strs[0][p]
        
        return new_str
                
            