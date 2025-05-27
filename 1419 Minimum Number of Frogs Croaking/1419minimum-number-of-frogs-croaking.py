class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        idk = "croak"
        hmap = {}

        for i in range(len(idk)):
            hmap[idk[i]] = i

        arr = [1, 0, 0, 0, 0]

        maxNum = 1

        for i in range(len(croakOfFrogs)):
            if hmap[croakOfFrogs[i]] != 0:
                arr[hmap[croakOfFrogs[i]]] -= 1

            for elem in arr:
                if elem < 0:
                    return -1
                        
            if hmap[croakOfFrogs[i]] + 1 < len(arr):
                arr[hmap[croakOfFrogs[i]] + 1] += 1

            #print(arr, sum(arr) - 1)
            maxNum = max(sum(arr) - 1, maxNum)
        
        for i in range(1, len(arr)):
            if arr[i] > 0:
                return -1
        return maxNum
        
        