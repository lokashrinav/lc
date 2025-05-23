class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        '''

        1, 8, 9, 10

        1, 2, 5, 6
        
        '''
        arr2.sort()
        total = 0
        for i in range(len(arr1)):
            closest = None
            l, r = 0, len(arr2) - 1
            while l <= r:
                m = (l + r) // 2
                if arr2[m] > arr1[i]:
                    if closest:
                        closest = arr2[m] if abs(arr2[m] - arr1[i]) < abs(closest - arr1[i]) else closest
                    else:
                        closest = arr2[m]
                    r = m - 1
                else:
                    if closest:
                        closest = arr2[m] if abs(arr2[m] - arr1[i]) < abs(closest - arr1[i]) else closest
                    else:
                        closest = arr2[m]
                    l = m + 1
            
            if abs(closest - arr1[i]) <= d:
                total += 1
            
        return len(arr1) - total