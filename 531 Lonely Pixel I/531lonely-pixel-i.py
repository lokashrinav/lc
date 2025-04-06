class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        rows = [0] * len(picture)
        cols = [0] * len(picture[0])
        for y in range(len(picture)):
            for x in range(len(picture[0])):
                if picture[y][x] == 'B':
                    rows[y] += 1
                    cols[x] += 1
        
        count = 0
        for y in range(len(picture)):
            for x in range(len(picture[0])):
                if picture[y][x] == 'B':
                    if rows[y] == 1 and cols[x] == 1:
                        count += 1

        return count

                    
        

        

        