class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        
        arr.sort()

        hmap = Counter(arr)
        count = 0

        '''
        -8, -4, -2, -1, 0, 0, 1, 2, 4, 8
        '''
        arr1 = []
        arr2 = []

        for i in range(len(arr)):
            if arr[i] >= 0:
                arr1.append(arr[i])
            else:
                arr2.append(arr[i])
        
        arr2.reverse()

        for i in range(len(arr1)):
            print(count)
            if arr1[i] % 2 == 0 and int(arr1[i] / 2) in hmap:
                if arr1[i] == 0 and hmap[0] == 1:
                    continue

                count += 1
                hmap[int(arr1[i] / 2)] -= 1
                if hmap[int(arr1[i] / 2)] == 0:
                    del hmap[int(arr1[i] / 2)]
                hmap[arr1[i]] -= 1
                if hmap[arr1[i]] == 0:
                    del hmap[arr1[i]]

        for i in range(len(arr2)):
            print(count)
            if arr2[i] % 2 == 0 and int(arr2[i] / 2) in hmap:
                if arr2[i] == 0 and hmap[0] == 1:
                    continue

                count += 1
                hmap[int(arr2[i] / 2)] -= 1
                if hmap[int(arr2[i] / 2)] == 0:
                    del hmap[int(arr2[i] / 2)]
                hmap[arr2[i]] -= 1
                if hmap[arr2[i]] == 0:
                    del hmap[arr2[i]]

        return count == len(arr) // 2