class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        '''

        1, 2, 3, 3, 4, 5, 6, 

        '''

        res = [0]

        for i in range(len(nums)):
            curr = 0
            for p in range(i, len(nums)):
                curr += nums[p]
                res.append(curr)
        
        res.sort()

        for i in range(1, len(res)):
            res[i] += res[i - 1]
        
        '''
        
        '''
        
        return (res[right] - res[left - 1]) % (10 ** 9 + 7)

        