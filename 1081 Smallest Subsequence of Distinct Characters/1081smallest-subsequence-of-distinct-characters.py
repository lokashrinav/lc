class Solution:
    def smallestSubsequence(self, s: str) -> str:
        '''
        
        bcabc
        cab

        '''

        stack = []
        visited = set()
        for i in range(len(s)):
            hset = set()
            if s[i] in visited:
                continue
            visited.add(s[i])
            for p in range(i + 1, len(s)):
                hset.add(s[p])
            while stack and s[i] < stack[-1] and stack[-1] in hset:
                out = stack.pop()
                visited.remove(out)
            stack.append(s[i])
        
        return ''.join(stack)
            
        