class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        

        arr = [0] * 1440

        for elem in timePoints:
            hour, minute = elem.split(":")
            arr[int(hour) * 60 + int(minute)] += 1
        
        for num in arr:
            if num > 1:
                return 0
        
        prev = None
        first = None
        minDiff = float('inf')
        for i in range(len(arr)):
            if arr[i] and prev is not None:
                item = min(i - prev, 1440 - prev + i)
                print(arr[i], prev, item)
                minDiff = min(minDiff, item)
                prev = i
            elif arr[i]:
                prev = i
                first = i
            
        
        item = min(prev - first, 1440 - (prev - first))
        minDiff = min(minDiff, item)

        return minDiff
        

        


                