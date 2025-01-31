class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        p1, p2 = 0, len(s) - 1

        while p1 < p2:
            if s[p1] != s[p2]:
                if s[p1+1:p2+1] == s[p1+1:p2+1][::-1] or s[p1:p2] == s[p1:p2][::-1]:
                    return True
                else:
                    return False
            else:
                p1 += 1
                p2 -= 1
        
        return True

