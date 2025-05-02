class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        count1 = count2 = 0
        flag = None
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1] and (flag is False or flag is None):
                count1 += 1
                flag = True
            elif nums[i - 1] > nums[i] and (flag is True or flag is None):
                count1 += 1
                flag = False
                
        return count1 + 1
