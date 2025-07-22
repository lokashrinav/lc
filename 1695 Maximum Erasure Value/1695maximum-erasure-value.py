class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        hmap = defaultdict(int)
        sum1 = 0
        maxSum = 0
        l = 0
        for i in range(len(nums)):
            hmap[nums[i]] += 1
            sum1 += nums[i]
            while hmap[nums[i]] >= 2:
                hmap[nums[l]] -= 1
                sum1 -= nums[l]
                l += 1

            maxSum = max(sum1, maxSum)

        maxSum = max(sum1, maxSum)
        return maxSum
            
