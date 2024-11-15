class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def binarySearch(num, stack):
            l, r = 0, len(stack) - 1
            while l < r:
                m = (l + r) // 2
                if(stack[m] >= num):
                    if m > 0 and stack[m - 1] < num:
                        return m
                    elif m == 0:
                        return m
                    else:
                        r = m - 1
                else:
                    l = m + 1
            return (l + r) // 2

        stack = []
        for i in range(len(nums)):
            if not stack:
                stack.append(nums[i])
            else:
                if stack[-1] < nums[i]:
                    stack.append(nums[i])
                else:
                    replaceIndex = binarySearch(nums[i], stack)
                    stack[replaceIndex] = nums[i]

        return len(stack)






        