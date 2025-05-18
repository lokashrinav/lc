class Solution:
    def minSwaps(self, nums: List[int]) -> int:

        res = []
        for i in range(len(nums)):
            elem = str(nums[i])
            total = 0
            for s in elem:
                total += int(s)
                
            res.append((total, nums[i]))

        #print(res)

        hmap = {}
        for ind, elem in enumerate(res):
            hmap[elem] = ind

        minHeap = sorted(res)

        total = 0
        for i in range(len(res)):
            if res[i] == minHeap[i]:
                 continue
            else:
                ind = hmap[minHeap[i]]
                hmap[res[i]] = ind
                hmap[res[ind]] = i
                res[i], res[ind] = res[ind], res[i] 
                total += 1
            #print(res)

        return total
            
            
            
            

        '''
        
        
        10, 1

        1, 10

        9, 7, 7, 7

        7, 7, 7, 9
        '''
            
        