class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        hmap = defaultdict(int)
        hmap[0] = 1
        total = 0
        curr = 0
        
        for i in range(len(nums)):
            #print(hmap)
            curr += nums[i]
            if curr - goal in hmap:
                total += hmap[curr - goal]
                
            hmap[curr] += 1
            
        return total

        