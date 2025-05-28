class Solution:
    def trimMean(self, arr: List[int]) -> float:

        heapify(arr)

        count = og = len(arr) // 20

        while count:
            out = heappop(arr)
            count -= 1
        
        for i in range(len(arr)):
            arr[i] = -arr[i]
        
        heapify(arr)

        count = og

        while count:
            out = heappop(arr)
            count -= 1
        
        for i in range(len(arr)):
            arr[i] = -arr[i]
                
        return sum(arr) / len(arr)

        