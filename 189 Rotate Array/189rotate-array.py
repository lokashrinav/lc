class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


        k = k % len(nums)

        if not k:
            return nums
            
        for i in range(len(nums)):
            ind = i

            if type(nums[ind]) is int:
                saved = nums[len(nums) + (ind - k)]

            while type(nums[ind]) is int:
                idk = nums[ind]
                nums[ind] = (saved, None)
                saved = idk
                ind = (ind + k) % len(nums)
        
        for i in range(len(nums)):
            nums[i] = nums[i][0]

        return nums
                    



        
        