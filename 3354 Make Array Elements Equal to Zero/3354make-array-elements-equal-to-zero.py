class Solution:
    def countValidSelections(self, nums: List[int]) -> int:

        def dfs(ind, mov, og):

            while ind >= 0 and ind < len(og):
                if og[ind] == 0:
                    ind += mov
                elif nums[ind] > 0:
                    og[ind] -= 1
                    mov *= -1
                    ind += mov

            for i in range(len(og)):
                if og[i] != 0:
                    return 0
        
            return 1
        
        total = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                og = nums[::]
                total += dfs(i, 1, og)
                og = nums[::]
                total += dfs(i, -1, og)
        
        return total


        