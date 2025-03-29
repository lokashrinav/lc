class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        
        visited = set()

        def dfs(ind, count, other):
            if ind in curr:

                if (abs(nums[ind]) % len(nums)) == 0:
                    return False
                elif other - curr[ind][1] == abs(count - curr[ind][0]):
                    return True
                else:
                    return False

            if ind in visited:
                return False
            
            visited.add(ind)
            curr[ind] = (count, other)
            
            new_ind = ind + nums[ind]

            if new_ind < 0:
                diff = abs(new_ind) % len(nums)
                new_ind = len(nums) - diff
            
            if new_ind >= len(nums):
                new_ind = new_ind % len(nums)

            if nums[ind] > 0:
                count += 1
            else:
                count -= 1
                
            return dfs(new_ind, count, other + 1)
        
        for i in range(len(nums)):
            curr = {}
            if i not in visited:
                if dfs(i, 0, 0):
                    return True
        
        return False

        '''
        0 -> 3
        1 -> 2
        2 -> 1
        3 -> 1
        4 -> 2
        '''
        