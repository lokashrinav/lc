class Solution:
    def finalString(self, s: str) -> str:
        
        curr = []
        for i in range(len(s)):
            if s[i] != 'i':
                curr.append(s[i])
            else:
                curr.reverse()
        
        return ''.join(curr)

        