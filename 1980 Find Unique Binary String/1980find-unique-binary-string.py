class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        num_set = set(nums)
        saved = [None]

        def dfs(curr):
            if len(curr) == len(nums[0]):
                if ''.join(curr) not in num_set:
                    saved[0] = curr
                    return True
                return False
            
            curr.append("1")
            if dfs(curr):
                return True
            curr.pop()

            curr.append("0")
            if dfs(curr):
                return True
            curr.pop()

            return False
        
        dfs([])
        
        return ''.join(saved[0])
