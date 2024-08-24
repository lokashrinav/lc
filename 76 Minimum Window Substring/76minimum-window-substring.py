class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hmap = {}
        hmap2 = {}
        for let in t:
            if let not in hmap2:
                hmap2[let] = 0
            hmap2[let] += 1
        
        for let in t:
            hmap[let] = 0

        l, r = 0, 0
        solved = 0
        needed = len(hmap.keys())
        saved_left = 0
        saved_right = 0
        saved_length = float('inf')
        while r < len(s):
            if s[r] in hmap:
                hmap[s[r]] += 1
                if hmap[s[r]] == hmap2[s[r]]:
                    solved += 1
                if solved == needed:
                    while solved == needed:
                        if s[l] in hmap:
                            hmap[s[l]] -= 1
                            if hmap[s[l]] < hmap2[s[l]]:
                                if r - l + 1 < saved_length:
                                    saved_left = l
                                    saved_right = r + 1
                                    saved_length = r - l + 1
                                solved -= 1
                        l += 1
            r += 1
                    
        return s[saved_left:saved_right]



        
        
            


        