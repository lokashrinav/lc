class Solution:
    def robotWithString(self, s: str) -> str:

        stack = []
        res = []

        i = 0
        last_ind = 0

        while i < len(s):
            print(i)

            minChar = s[i]
            for p in range(i, len(s)):
                minChar = min(s[p], minChar)

            for p in range(i, len(s)):
                if s[p] == minChar:
                    last_ind = p
            
            for p in range(i, last_ind+1):
                if s[p] == minChar:
                    res.append(minChar)
                else:
                    stack.append(s[p])
            
            if last_ind + 1 < len(s):
                new = s[last_ind+1]
                for p in range(last_ind+1, len(s)):
                    new = min(new, s[p])

                while stack and stack[-1] <= new:
                    res.append(stack.pop())
            
            i = last_ind + 1
        
        return ''.join(res) + ''.join(stack[::-1])
            



        