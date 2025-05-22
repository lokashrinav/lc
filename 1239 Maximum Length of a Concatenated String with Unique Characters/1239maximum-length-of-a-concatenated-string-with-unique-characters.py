class Solution:
    def maxLength(self, arr: List[str]) -> int:

        '''

        '''

        cache = {}
        hset = set()

        def calc(ind):
            print(hset)
            if ind == len(arr):
                return 0
            
            if (ind, tuple(sorted(hset))) in cache:
                return cache[(ind, tuple(sorted(hset)))]
                        
            maxNum = calc(ind + 1)

            flag = True
            for i in range(len(arr[ind])):
                if arr[ind][i] in hset:
                    flag = False

            if flag and len(set(list(arr[ind]))) == len(arr[ind]):
                hset.update(set(list(arr[ind])))
                maxNum = max(maxNum, len(arr[ind]) + calc(ind + 1))
            
                for elem in arr[ind]:
                    if elem in hset:
                        hset.remove(elem)

            cache[ind, tuple(sorted(hset))] = maxNum

            return maxNum

        return calc(0)
        
            





        