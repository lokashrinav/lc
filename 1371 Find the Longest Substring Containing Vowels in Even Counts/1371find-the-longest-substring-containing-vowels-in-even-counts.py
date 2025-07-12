class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        
        arr = ['a', 'e', 'i', 'o', 'u']
        count = {elem:0 for elem in arr}
        maxNum = 0
        hmap = {}
        hmap[(0, 0, 0, 0, 0)] = -1

        for i in range(len(s)):
            if s[i] in arr:
                count[s[i]] += 1

            res = []
            for key, val in sorted(count.items()):
                res.append(val % 2)

            #print(res)
            if tuple(res) in hmap:
                maxNum = max(maxNum, i - hmap[tuple(res)])
            else:
                hmap[tuple(res)] = i
        
        return maxNum
            

       