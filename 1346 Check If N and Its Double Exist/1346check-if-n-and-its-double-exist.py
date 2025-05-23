class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hmap = Counter(arr)

        for i in range(len(arr)):
            if arr[i] == 0:
                if hmap[0] >= 2:
                    return True
            else:
                if arr[i] * 2 in hmap:
                    return True
        
        return False


        