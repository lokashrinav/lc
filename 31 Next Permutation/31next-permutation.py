class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        savedInd = None
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                savedInd = i

        if savedInd is None:
            nums[:] = nums[::-1]
            return nums

        smallestNum = float('inf')
        smallestInd = None
        for p in range(savedInd + 1, len(nums)):
            if nums[p] <= smallestNum and nums[p] > nums[savedInd]:
                smallestNum = nums[p]
                smallestInd = p

        print(smallestInd)
        nums[smallestInd], nums[savedInd] = nums[savedInd], nums[smallestInd]

        nums[savedInd+1:] = nums[savedInd+1:][::-1]

        return nums

        
            


        