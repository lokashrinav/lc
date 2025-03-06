class Solution:
    def decodeString(self, s: str) -> str:

        stack = []

        final = ""
        num = 0
        curr = ""
        for i in range(len(s)):
            print(stack, num, s[i], curr)
            if s[i] == "]":
                dum, str1 = stack.pop()
                curr *= dum
                curr = str1 + curr
            elif s[i] == "[":
                stack.append((num, curr))
                curr = ""
                num = 0
            elif s[i].isalpha():
                curr += s[i]
            else:
                num = num * 10 + int(s[i])
        
        return curr
            
                
                