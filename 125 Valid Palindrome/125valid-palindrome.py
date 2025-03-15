class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        p1, p2 = 0, len(s) - 1

        while p1 < p2:
            if s[p1].isalnum() and s[p2].isalnum():
                if s[p1].lower() == s[p2].lower():
                    p1 += 1
                    p2 -= 1
                else:
                    return False
            elif s[p1].isalnum():
                p2 -= 1
            elif s[p2].isalnum():
                p1 += 1
            else:
                p2 -= 1
                p1 += 1
        
        return True
              