class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        
        hmap = Counter(s)

        count = 0
        for key, val in hmap.items():
            if val % 2:
                count += 1
            if count >= 2:
                return False
        
        return True
        