class Solution:
    def countLetters(self, s: str) -> int:

        count = 0
        curr = None
        l = 0

        for i in range(len(s)):
            if not curr:
                curr = s[i]
            
            if curr != s[i]:
                #count += i - l + 1
                curr = s[i]
                l = i
        
            count += (i - l + 1)

            #print(count)
        
        return count
    