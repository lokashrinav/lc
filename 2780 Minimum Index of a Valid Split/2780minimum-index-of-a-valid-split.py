class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        '''
        (3, 2)

        1, None, 2, 2 - 2, 2, 2, 2

        [2,1,3,1,1,1,7,1,2,1]

        2, None, None, 1, 1, 1, 1, 1, 1, 1

        1, None, 1, None, 1, 1, 1, 1, 1

        '''

        res1 = []
        res2 = []

        maj = None
        count = 0
        hmap = defaultdict(int)
        for i in range(len(nums)):
            if count == 0:
                maj, count = nums[i], 1
            elif maj == nums[i]:
                count += 1
            else:
                count -= 1

            hmap[nums[i]] += 1

            res1.append(maj if hmap[maj] > ((i + 1) // 2) else None)

        maj = None
        count = 0
        hmap = defaultdict(int)
        idk = 0
        for i in range(len(nums) - 1, -1, -1):
            idk += 1
            if count == 0:
                maj, count = nums[i], 1
            elif maj == nums[i]:
                count += 1
            else:
                count -= 1

            hmap[nums[i]] += 1

            res2.append(maj if hmap[maj] > ((idk) // 2) else None)
        
        res2.reverse()

        for i in range(len(res1) - 1):
            if res1[i] is not None and res2[i + 1] is not None and res1[i] == res2[i + 1]:
                return i
        
        return -1





            


        