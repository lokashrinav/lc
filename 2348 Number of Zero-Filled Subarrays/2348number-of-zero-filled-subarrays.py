class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        total = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                total += (count + 1) * count // 2
                count = 0

        if count:   
            total += (count + 1) * count // 2

        return total