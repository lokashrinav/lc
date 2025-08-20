class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        '''
        
        2, 3, 6, 8
        2, 3, 6, 7, 10

        '''
        
        def merge(arr1, arr2):
            res = []
            if arr1 is None:
                return arr2
            if arr2 is None:
                return arr1
            
            l = r = 0
            while l < len(arr1) and r < len(arr2):
                if arr1[l] == arr2[r]:
                    res.append(arr1[l])
                    l += 1
                    r += 1
                elif arr1[l] < arr2[r]:
                    l += 1
                else:
                    r += 1
            
            return res
        
        while len(arrays) > 1:
            out1 = arrays.pop()
            if arrays:
                out2 = arrays.pop()
            else:
                out2 = None

            out3 = merge(out1, out2)

            arrays.append(out3)
        
        return arrays[0]
