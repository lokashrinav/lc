class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        
        res = []
        for i in range(len(index)):
            res.insert(index[i], nums[i])
        
        return res
            
        
        
        