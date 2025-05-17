class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        '''
        2, -2
        '''

        def find():
            for i in range(len(nums)):
                if nums[abs(nums[i]) - 1] < 0:
                    return abs(nums[i])
                
                nums[abs(nums[i]) - 1] *= -1
            
        calc = abs(find())

        for i in range(len(nums)):
            nums[i] = abs(nums[i])

        idk = (sum(i for i in range(1, len(nums) + 1)))
        print(idk)
        print(sum(nums), calc)
        return [calc, idk - (sum(nums) - calc)]
