class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        
        count = 0
        for i in range(len(arr)):
            if arr[i] > 5:
                count += 1
        
        if count >= 2:
            calc = 1
        else:
            calc = 2

        maxHour = -1
        for i in range(len(arr)):
            if arr[i] <= calc:
                maxHour = max(maxHour, arr[i])
            
        if maxHour == -1:
            return ""
        
        arr.remove(maxHour)

        maxHour2 = -1
        calc = 3 if maxHour == 2 else 9

        for i in range(len(arr)):
            if arr[i] <= calc:
                maxHour2 = max(maxHour2, arr[i])
        
        if maxHour2 == -1:
            return ""
        
        arr.remove(maxHour2)

        maxMinute = -1
        for i in range(len(arr)):
            if arr[i] <= 5:
                maxMinute = max(maxMinute, arr[i])
        
        if maxMinute == -1:
            return ""     

        arr.remove(maxMinute)    
            
        maxMinute2 = arr[0]

        arr.remove(maxMinute2)

        return ''.join([str(maxHour), str(maxHour2)]) + ":" + ''.join([str(maxMinute), str(maxMinute2)])
        

        

