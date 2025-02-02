class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        currNum = None
        count = 0
        for i in range(len(nums)):
            if currNum is None:
                currNum = nums[i]
                count += 1
            elif currNum == nums[i]:
                count += 1
            else:
                count -= 1
                if count < 0:
                    currNum = nums[i]
                    count += 1

        return currNum
            

        