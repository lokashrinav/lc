class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        even_count = 0
        for elem in nums:
            if elem % 2 == 0:
                even_count += 1

        ind = 0
        while ind < even_count:
            nums[ind] = 0
            ind += 1

        while ind < len(nums):
            nums[ind] = 1
            ind += 1

        return nums

        

        