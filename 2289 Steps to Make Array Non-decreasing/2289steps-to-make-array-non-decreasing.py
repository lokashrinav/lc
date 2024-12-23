class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        stack = []
        maxCount = 0
        for i in range(len(nums) - 1, -1, -1):
            count = 0
            while stack and stack[-1][0] < nums[i]:
                final1, final2 = stack.pop()
                maxCount = max(maxCount, final2)
                count += 1
            maxCount = max(maxCount, count)
            stack.append((nums[i], count))
        
        return max(max([i[1] for i in stack]), maxCount)


        