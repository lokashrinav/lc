class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:

        '''
        [10,13,17,21,15,15,9,17,22,22,13]

        



        '''


        res = deque()
        indices = deque()
        for i in range(len(arr) - 1, -1, -1):
            if not res:
                res.append(arr[i])
                indices.append(i)
            elif arr[i] <= res[-1]:
                res.append(arr[i])
                indices.append(i)
            else:
                break
        
        res.reverse()
        indices.reverse()

        print(res)

        maxNum = len(arr) - len(res)
        count = 0
        for i in range(len(arr)):
            if i >= 1 and arr[i] < arr[i - 1]:
                break

            if indices[0] == i:
                break
            ind = bisect_left(res, arr[i])
            #print(ind, "H")
            maxNum = min(len(arr) - (i + 1 + (len(res) - ind)), maxNum)
            #print(len(arr) - (i + 1 + (len(res) - ind)))
        
        return maxNum


        