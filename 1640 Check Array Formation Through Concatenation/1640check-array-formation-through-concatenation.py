class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:

        '''

        15, 88

        91, 4, 64, 78
    
        '''
        hmap = {}
        for i in range(len(pieces)):
            for p in range(len(pieces[i])):
                hmap[pieces[i][p]] = i

        res = []

        ind = 0

        while ind != len(arr):
            if ind == len(res):
                if arr[ind] not in hmap:
                    print("A")
                    return False

                res += pieces[hmap[arr[ind]]]
            
            if res[ind] != arr[ind]:
                
                print("B")
                return False
            
            ind += 1
        
        return True



        