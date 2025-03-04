class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        hmap = {'8': '8', '6': '9', '1': '1', '9': '6', '0': '0'}

        if num[0] == '0' and len(num) > 1:
            return True
        
        if len(num) % 2:
            if num[len(num) // 2] not in '810':
                return False
        
        l, r = 0, len(num) - 1
        while l < r:
            if num[l] not in hmap or num[r] not in hmap:
                return False

            if num[l] != hmap[num[r]]:
                return False

            l += 1
            r -= 1
        
        return True
            