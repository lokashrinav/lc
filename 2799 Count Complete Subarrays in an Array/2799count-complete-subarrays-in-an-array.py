class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        hset = set(nums)

        '''
        1, 3, 1, 2 -> 2
        3, 1, 2 -> 2
        1, 2, 2 -> 0
        ''' 

        hmap = defaultdict(int)
        total = 0
        l = 0
        for i in range(len(nums)):
            hmap[nums[i]] += 1
            
            while len(hmap.keys()) == len(hset):
                total += len(nums) - i
                hmap[nums[l]] -= 1
                if hmap[nums[l]] == 0:
                    del hmap[nums[l]]
                l += 1
        
        return total



        