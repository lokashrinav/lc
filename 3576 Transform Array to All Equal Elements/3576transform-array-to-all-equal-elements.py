class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        '''
        
        '''
        nums1 = nums[::]

        count = 0
        for i in range(len(nums) - 1):
            if nums1[i] == 1:
                nums1[i] *= -1
                nums1[i + 1] *= -1
                count += 1

        flag = True
        for i in range(len(nums1)):
            if nums1[i] != -1:
                flag = False

        if flag and count <= k:
            return True

        count = 0
        for i in range(len(nums) - 1):
            if nums[i] != 1:
                nums[i] *= -1
                nums[i + 1] *= -1
                count += 1    

        flag = True
        for i in range(len(nums1)):
            if nums[i] != 1:
                flag = False

        if flag and count <= k:
            return True

        return False
        

        
        