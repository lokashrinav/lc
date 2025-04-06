class Solution:
    def findBlackPixel(self, picture: List[List[str]], target: int) -> int:
        rows = [0] * len(picture)
        cols = [0] * len(picture[0])
        hmap = defaultdict(int)
        for y in range(len(picture)):
            row = picture[y]
            flag = False
            for x in range(len(picture[0])):
                if picture[y][x] == 'B':
                    rows[y] += 1
                    cols[x] += 1
                    flag = True
            
            if flag:
                hmap[tuple(row)] += 1
        
        count = 0
        for y in range(len(picture)):
            row = picture[y]
            for x in range(len(picture[0])):
                if picture[y][x] == 'B':
                    if rows[y] == target and cols[x] == target and hmap[tuple(row)] == target:
                        count += 1

        return count