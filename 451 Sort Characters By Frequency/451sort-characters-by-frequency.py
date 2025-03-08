class Solution:
    def frequencySort(self, s: str) -> str:
        hmap = defaultdict(int)

        for char in s:
            hmap[char] += 1
        
        final = ""
        for elem, val in sorted(hmap.items(), key=lambda x: x[1]):
            final += elem * val
        
        return final[::-1]