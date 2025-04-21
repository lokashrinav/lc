class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        

        stack = []
        for i in range(len(arr)):
            if arr[i] != 0:
                stack.append(arr[i])
            else:
                stack.append(0)
                stack.append(0)
        
        for i in range(len(arr)):
            arr[i] = stack[i]
        
        


        


        