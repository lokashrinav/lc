class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        '''
            51, 51, 11, 11
            X, 94, 11, 11
            X, X, 11, 11
            X, X, X, 56
        '''

        '''minNum = None
        curr = 0
        total = 0
        res = []
        prefix = [0]
        
        for i in range(len(arr)):
            if minNum is None:
                minNum = arr[i]
                total += minNum
                curr += minNum
                prefix.append(curr)
                res.append(curr)
            else:
                ind = bisect_left(res, arr[i])
                minNum = arr[i]
                if ind == len(prefix) - 1:
                    curr += arr[i]
                else:
                    curr = prefix[ind] + arr[i] * (i + 1 - ind)
                


                prefix.append(curr)
                total += curr'''
            
        
        '''
        bit ops
        dp

        prefix/hmap

        3, 1, 1, 1
        X, 1, 1, 1
        X, X, 2, 2
        X, X, X, 4



        3, 5, 1, 2, 4

        3, 3, 3, 1, 1
        X, 5, 5, 1, 1
        X, X, 7, 1, 1
        X, X, X, 2, 2
        X, X, X, X, 4

        3, 5, 1, 2, 4

        11, 81, 94, 43, 3

        11, 11, 11, 11, 3
        X, 81, 81, 43, 3
        X, X, 94, 43, 3
        X, X, X, 43, 3
        X, X, X, X, 3   
        '''

        res = deque()
        indices = deque()
        minNum = None
        curr = 0
        total = 0
        prefix = [0]
        
        for i in range(len(arr)):
            if minNum is None:
                minNum = arr[i]
                total += minNum
                curr += minNum
                prefix.append(curr)
                res.append(arr[i])
                indices.append(i)
            else:
                ind = None
                if arr[i] < res[-1]:
                    x = None
                    while res and arr[i] < res[-1]:
                        x = indices.pop()
                        res.pop()
                    indices.append(x)
                    res.append(arr[i])
                    ind = x
                else:
                    res.append(arr[i])
                    indices.append(i)
                    ind = i
                
                if index == len(res):
                    curr += arr[i]
                else:
                    curr = prefix[ind] + arr[i] * (i + 1 - ind)


                prefix.append(curr)
                total = ((total + curr) % (10 ** 9 + 7))
            
            #print(total, curr, "H")
#
        #print(prefix, total)

        '''
        51, 51, 11, 11
        X, 94, 11, 11
        X, X, 11, 11
        X, X, X, 56

        51 * 3 + 11 * 6 + 56
        '''
        
        return total


