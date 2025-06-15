class Solution:
    def generateTag(self, caption: str) -> str:

        s = caption.split(" ")
        final = "#"
        count = 0
        
        for i in range(len(s)):
            if not s[i]:
                continue
    
            s[i] = list(s[i])
            curr = ""
            if count == 0:
                for p in range(len(s[i])):
                    elem = s[i][p]
                    if elem.isalpha():
                        curr += elem.lower()
            else:
                for p in range(len(s[i])):
                    elem = s[i][p]
                    if elem.isalpha() and p != 0:
                        curr += elem.lower()
                    elif elem.isalpha() and p == 0:
                        curr += elem.upper()
                        
            final += curr
            count += 1
                        
        return final[:100]
            
        
            
        