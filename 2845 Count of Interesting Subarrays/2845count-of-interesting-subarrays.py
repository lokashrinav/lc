class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        
        # 1, 4, ..., len(nums)

        total = 0
        hmap = defaultdict(int)
        hmap[k] = 1
        count = 0
        for i in range(len(nums)):
            if nums[i] % modulo == k:
                curr = 1
            else:
                curr = 0

            count += curr
            total += hmap[count % modulo]
            hmap[((count % modulo) + k) % modulo] += 1
        
        '''
        1, 0, 0
        1, 1, 1
        count = 1 + 
        '''
        
        return total

        '''
        3, 1, 9, 6
        1, 0, 1, 1
        1, 1, 2, 3
        '''

        '''hmap = defaultdict(int)
        hmap[k] = 1
        count = 0
        for i in range(len(nums)):
            if nums[i] % modulo == k:
                curr = 1
            else:
                curr = 0

            count += curr
            if count % modulo == k:
                total += hmap[a bscount % modulo]
            hmap[abs(count % modulo) - k] += 1
            print(total)
        
        
        1, 0, 1, 1
        1, 1, 2, 3
        
        0: 1
        1: 2

        1, 0, 0
        1, 1, 1

        0, 1, 1, 1

        0: 1
        1: 2
        total = 1

        1 + 1 + 1
        '''
                
        return total + (1 if k == 0 else 0)






