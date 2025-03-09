class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        hmap = defaultdict(int)

        for char in s:
            hmap[char] += 1
        
        count = 0
        maxOne = 0
        for key in hmap:
            if hmap[key] % 2 == 0:
                count += hmap[key]
            else:
                count += (hmap[key] - 1) 
                maxOne = 1
        
        total = count + maxOne

        return total
            