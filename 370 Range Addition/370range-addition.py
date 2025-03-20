class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        

        arr = [0] * (length + 1)

        for i in range(len(updates)):
            start, end, val = updates[i]
            arr[start] += val
            arr[end + 1] -= val
        
        for i in range(1, len(arr)):
            arr[i] += arr[i - 1]

        arr.pop()
        
        return arr