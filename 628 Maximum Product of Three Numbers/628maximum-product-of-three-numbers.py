class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        maxNum1 = float('-inf')
        maxNum2 = float('-inf')
        maxNum3 = float('-inf')

        minNum1 = float('inf')
        minNum2 = float('inf')

        for i in range(len(nums)):
            if nums[i] >= maxNum1:
                maxNum3 = maxNum2
                maxNum2 = maxNum1
                maxNum1 = nums[i]
            elif nums[i] >= maxNum2:
                maxNum3 = maxNum2
                maxNum2 = nums[i]
            elif nums[i] > maxNum3:
                maxNum3 = nums[i]
        
        for i in range(len(nums)):
            if nums[i] <= minNum1:
                minNum2 = minNum1
                minNum1 = nums[i]
            elif nums[i] <= minNum2:
                minNum2 = nums[i]

        BiggestNum1 = maxNum1 * maxNum2 * maxNum3
        BiggestNum2 = max(nums) * minNum2 * minNum1
        return max(BiggestNum1, BiggestNum2)

        