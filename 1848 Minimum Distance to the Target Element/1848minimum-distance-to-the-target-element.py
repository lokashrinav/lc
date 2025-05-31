class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:

        minNum = None
        for i in range(len(nums)):
            if nums[i] == target:
                if minNum is None:
                    minNum = abs(i - start)
                else:
                    if minNum > abs(i - start):
                        minNum = abs(i - start)
        
        return minNum

        