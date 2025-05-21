class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        '''
        [1, 0], [3, 2]

        [1, 2, 0, 3]



        '''

        ind = None
        res = []
        total = 0
        for i in range(len(arr)):
            if arr[i] == i:
                if ind is None:
                    total += 1
                continue

            if ind:
                ind = max(ind, arr[i])

            if i == ind:
                res.append(ind)
                ind = None
            else:
                if ind is None:
                    if arr[i] >= i:
                        ind = arr[i]                        
            
            print(ind)
        
        return len(res) + total
                