class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:

        
        p_arr = [0, 0, 0]

        arr = [arr1, arr2, arr3]

        res = []

        for i in range(len(arr1) + len(arr2) + len(arr3)):
            minNum = float('inf')

            for p in range(3):
                if p_arr[p] >= len(arr[p]):
                    return res
                minNum = min(minNum, arr[p][p_arr[p]])

            flag = True
            for p in range(3):
                if arr[p][p_arr[p]] != minNum:
                    flag = False
            
            if flag:
                res.append(minNum)
            
            for p in range(3):
                if arr[p][p_arr[p]] == minNum:
                    p_arr[p] += 1
        
        return res
                    
                
                

                
        