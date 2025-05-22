class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:

        '''


        '''
        
        def minDist(queen1, queen2):
            nx, ny = queen1
            dx, dy = queen2

            dist1 = abs(king[0] - nx) + abs(king[1] - ny)
            dist2 = abs(king[0] - dx) + abs(king[1] - dy)

            return queen1 if dist1 < dist2 else queen2
        
        def slope(first, second):
            nx, ny = first
            dx, dy = second

            if nx - dx == 0:
                return None

            return (ny - dy) / (nx - dx)

        arr = [None] * 8

        ind = 0
        for x, y in queens:
            if y == king[1]:
                if x < king[0]:
                    if arr[0] is None:
                        arr[0] = (x, y)
                    else:
                        arr[0] = minDist(arr[0], (x, y))
                else:
                    if arr[1] is None:
                        arr[1] = (x, y)
                    else:
                        arr[1] = minDist(arr[1], (x, y))
            elif x == king[0]:
                if y < king[1]:
                    if arr[2] is None:
                        arr[2] = (x, y)
                    else:
                        arr[2] = minDist(arr[2], (x, y))
                else:
                    if arr[3] is None:
                        arr[3] = (x, y)
                    else:
                        arr[3] = minDist(arr[3], (x, y))
            elif slope((x, y), king) == 1:
                if y > king[1]:
                    if arr[4] is None:
                        arr[4] = (x, y)
                    else:
                        arr[4] = minDist(arr[4], (x, y))
                else:
                    if arr[5] is None:
                        arr[5] = (x, y)
                    else:
                        arr[5] = minDist(arr[5], (x, y))
            elif slope((x, y), king) == -1:
                print((x, y), slope((x, y), king))
                if y > king[1]:
                    if arr[6] is None:
                        arr[6] = (x, y)
                    else:
                        arr[6] = minDist(arr[6], (x, y))
                else:
                    if arr[7] is None:
                        arr[7] = (x, y)
                    else:
                        arr[7] = minDist(arr[7], (x, y))
            ind += 1
            print(arr)
            '''
            5 - 4
            3 - 0
            '''

        res = [] 
        for elem in arr:
            if elem:
                res.append(elem)
        
        return res


            