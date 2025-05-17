class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:

        last = None
        while arr != last:
            last = arr
            prev = arr.copy()
            for i in range(1, len(arr) - 1):
                if arr[i + 1] > arr[i] and arr[i - 1] > arr[i]:
                    prev[i] += 1
                elif arr[i + 1] < arr[i] and arr[i - 1] < arr[i]:
                    prev[i] -= 1
            arr = prev

        return arr
        