class Solution:
    def findLHS(self, nums: List[int]) -> int:

        hmap2 = defaultdict(int)

        for i in range(len(nums)):
            hmap2[nums[i]] += 1

        maxDiff = 0
        for key, val in hmap2.items():
            if (key + 1) in hmap2 and hmap2[key + 1]:
                maxDiff = max(maxDiff, val + hmap2[key + 1])
        
        return maxDiff
            

         
        






        