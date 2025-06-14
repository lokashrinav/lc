class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:

        '''

        [101,56,69,48,30]

        30, 48, 56, 69, 101

        8, 24, 69, 85, 85

        [73,106,100,71,112,60,110]

        [6, 6, 15, 26, 30, 35, 39, 46, 60, 71, 73, 100, 106, 110, 112]
        [6, 6, 15, 26, 30, 35, 39, 46, 60, 71, 73, 100, 106, 110, 112]

        [71,35]
        [35, 71]

        '''

        #print(sorted(ages))

        hmap = Counter(ages)
        l = 0

        list1 = sorted(hmap.keys())

        sum1 = 0
        total = 0

        for i in range(len(list1)):
            while i > 0 and l < i and (list1[i] * 0.5 + 7) >= list1[l]:
                sum1 -= hmap[list1[l]]
                l += 1
            
            if (list1[i] * 0.5 + 7) < list1[i]:
                total += (sum1 * hmap[list1[i]]) + (hmap[list1[i]] - 1) * hmap[list1[i]]
            else:
                total += (sum1 * hmap[list1[i]])

            # 1 * 2 -> 
            # 2 + 2 + 2
            # 4 -> 3 + 3 + 3 + 3
            
            sum1 += hmap[list1[i]]
        
        return total
            

        