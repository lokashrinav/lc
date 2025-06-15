class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        '''
        
        [1,3,-5,5,6,-4]
        
        '''
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            if stack:
                stack.append(max(nums[i], stack[-1]))
            else:
                stack.append(nums[i])

        minStack = []
        for i in range(len(nums) - 1, -1, -1):
            if minStack:
                minStack.append(min(nums[i], minStack[-1]))
            else:
                minStack.append(nums[i])

        maxNum = float('-inf')

        stack = stack[::-1]
        minStack = minStack[::-1]

        for i in range(len(nums) - m + 1):
            maxNum = max(nums[i] * stack[i + m - 1], maxNum)
            maxNum = max(nums[i] * minStack[i + m - 1], maxNum)
        
        return maxNum

        