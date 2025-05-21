class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:

        prefix = nums[::]
        suffix = nums[::]

        for i in range(1, len(prefix)):
            prefix[i] += prefix[i - 1]

        for i in range(len(suffix) - 2, -1, -1):
            suffix[i] += suffix[i + 1]

        res = []
        for i in range(len(prefix)):
            res.append(abs(prefix[i] - suffix[i]))
        
        return res

        