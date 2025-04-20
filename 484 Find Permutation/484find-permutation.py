class Solution:
    def findPermutation(self, s: str) -> List[int]:
        
        stack = []
        res = []
        for i in range(len(s) + 1):
            stack.append(i + 1)

            if i == len(s) or s[i] == 'I':
                while stack:
                    res.append(stack.pop())
        
        return res

