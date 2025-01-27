class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
            
        if x < 0 or x % 10 == 0:
            return False

        idk = 0

        while idk < x:
            idk = idk * 10 + (x % 10)
            x = x // 10
        
        print(idk, x)

        return idk == x or x == idk // 10 
        