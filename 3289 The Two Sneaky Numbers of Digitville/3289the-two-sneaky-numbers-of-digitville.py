class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        
        visited = set()
        res = []
        for i in range(len(nums)):
            if nums[i] in visited:
                res.append(nums[i])
            visited.add(nums[i])
        
        return res

        


        
        