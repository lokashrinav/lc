class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:

        pairs.sort(key=lambda x: (x[1], x[0]))

        maxNum = 1
        curr = 1

        prev = pairs[0]
        for i in range(1, len(pairs)):
            if prev[1] < pairs[i][0]:
                curr += 1
                prev = pairs[i]
        
        return curr
        