class Solution:
    def minimumLength(self, s: str) -> int:
        hmap = {}

        for char in s:
            hmap[char] = hmap.get(char, 0) + 1
        
        count = 0
        for key, val in hmap.items():
            if val > 2 and val % 2:
                count += 1
            elif val > 2 and val % 2 == 0:
                count += 2
            else:
                count += val
        
        return count