class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        hmap = {}
        for i in range(len(s)):
            hmap[s[i]] = i
        
        stack = []
        seen = set()
        for i, char in enumerate(s):
            if char in seen:
                continue
            
            while stack and char < stack[-1] and i < hmap[stack[-1]]:
                out = stack.pop()
                seen.remove(out)
            
            stack.append(char)
            seen.add(char)
        
        return ''.join(stack)