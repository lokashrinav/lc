class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:

        if len(nums) == 2:
            return 2
        if len(nums) == 1:
            return 1

        '''

        01
        10
        11

        1, 2, 3, 4

        
        000 -> 0, 1, 2, 3, 4, 5, 6, 7

        4 xor 2 

    
        '''

        length = max(nums).bit_length()

        return 2 ** (length)