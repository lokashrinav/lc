class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:

        count = 0
        for i in range(min(len(nums), k)):
            if nums[i] == key:
                count += 1
            
        res = []
        for i in range(len(nums)):           
            if i + k < len(nums) and nums[i + k] == key:
                count += 1
            
            if i - k - 1 >= 0 and nums[i - k - 1] == key:
                count -= 1

            print(count)

            if count:
                res.append(i)
        
        return res
                

            
