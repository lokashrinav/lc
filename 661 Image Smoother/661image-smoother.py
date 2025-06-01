class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:

        dirs = [[0, 1], [1, 0], [1, 1], [0, 0], [-1, 1], [1, -1], [-1, -1], [-1, 0], [0, -1]]

        matrix = [[0] * len(img[0]) for i in range(len(img))]
        for i in range(len(img)):
            for p in range(len(img[0])):
                count = 0
                num = 0
                for y, x in dirs:
                    ny, nx = i + y, x + p
                    if len(img) > ny >= 0 and len(img[0]) > nx >= 0:
                        num += img[ny][nx]
                        count += 1

                matrix[i][p] = num // count
        
        return matrix

                

        