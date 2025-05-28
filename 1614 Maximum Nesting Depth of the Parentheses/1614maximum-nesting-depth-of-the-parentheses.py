class Solution:
    def maxDepth(self, s: str) -> int:

        first = maxNum = 0
        for elem in s:
            if elem == "(":
                first += 1
            elif elem == ")":
                first -= 1
            
            maxNum = max(maxNum, first)
        
        return maxNum
        