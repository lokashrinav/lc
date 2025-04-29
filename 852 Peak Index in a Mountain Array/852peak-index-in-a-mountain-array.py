class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        

        l, r = 1, len(arr)

        arr.insert(0, 0)
        arr.append(0)

        saved = 0
        ind = 0
        while l <= r:
            m = (l + r) // 2
            if arr[m] > arr[m + 1]:
                if arr[m] > saved:
                    saved = max(saved, arr[m])
                    ind = m - 1
                r = m - 1
            else:
                l = m + 1
        
        return ind