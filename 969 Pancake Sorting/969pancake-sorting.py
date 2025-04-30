class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        '''
        1, 4, 2, 3
        '''
        res = []

        '''
        3, 2, 4, 1

        '''

        for i in range(len(arr), 0, -1):
            #print(arr)
            x = arr.index(i)
            res.append(x+1)
            arr[:x+1] = arr[:x+1][::-1]
            res.append(i)
            arr[:i] = arr[:i][::-1]

        return res




        