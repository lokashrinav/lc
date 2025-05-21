class Solution:
    def missingNumber(self, arr: List[int]) -> int:

        if len(set(arr)) == 1:
            return arr[0]

        dist = None
        flag = False
        for i in range(1, len(arr)):
            if dist is None:
                dist = arr[i] - arr[i - 1]
                flag = (i, i - 1)
            elif abs(dist) > abs(arr[i] - arr[i - 1]):
                return (arr[flag[0]] + arr[flag[1]]) // 2            
            elif abs(dist) < abs(arr[i] - arr[i - 1]):
                return (arr[i] + arr[i - 1]) // 2
        


                
            
            

        