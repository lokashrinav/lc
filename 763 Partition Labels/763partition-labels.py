class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hmap = defaultdict(list)
        # 0, 8 - a
        # 1, 5 - b
        # 4, 7 - c
        # 9, 14 - d
        # 10, 15 - e
        # 11, 11 - f
        # 13, 13 - g
        # 16, 19 - h
        # 17, 22  - i
        # 18, 23 - j
        # 24, 24 - k
        # 25, 25 - l
        for i in range(len(s)):
            hmap[s[i]] = i
        
        count = 1
        res = []
        end = None
        for i in range(len(s)):
            if not end:
                end = hmap[s[i]]
            else:
                end = max(end, hmap[s[i]])
            if i == end:
                res.append(count)
                count = 0
            count += 1
        return res


        

        