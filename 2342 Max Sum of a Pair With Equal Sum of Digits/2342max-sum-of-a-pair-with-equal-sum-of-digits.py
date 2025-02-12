class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def sum_digit(digit):
            return sum(int(char) for char in str(digit))
        
        hmap = defaultdict(int)

        maxNum = -1

        for i in range(len(nums)):
            sum_of = sum_digit(nums[i])
            if sum_of in hmap:
                maxNum = max(maxNum, hmap[sum_of] + nums[i])
                hmap[sum_of] = max(hmap[sum_of], nums[i])
            else:
                hmap[sum_of] = nums[i]
            
        return maxNum
                
