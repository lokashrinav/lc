class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:

        sum1 = 0
        for i in range(len(nums)):
            flag = False
            if i + k < len(nums):
                if nums[i] <= nums[i + k]:
                    flag = True
            
            if i - k >= 0:
                if nums[i] <= nums[i - k]:
                    flag = True    

            if not flag:
                sum1 += nums[i]

        return sum1
                