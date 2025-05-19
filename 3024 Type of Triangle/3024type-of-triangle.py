class Solution:
    def triangleType(self, nums: List[int]) -> str:
        
        if min(nums) + sorted(nums)[1] <= max(nums):
            return "none"


        '''

        1, 1, 100

        

        '''

        if len(set(nums)) == 1:
            return "equilateral"
        elif len(set(nums)) == 2:
            return "isosceles"
        else:
            return "scalene"
        