class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        

        # 5 + 1
        # 

        minNum = min(nums)

        x = nums.index(minNum)

        maxNum = max(nums)
        saved = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == maxNum:
                saved = i
                break
        
        count = x

        if x > saved:
            count -= 1

        count += len(nums) - saved - 1

        return count
            