class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:

        res = []
        for num in nums:
            for elem in str(num):
                res.append(int(elem))
        
        return res
        