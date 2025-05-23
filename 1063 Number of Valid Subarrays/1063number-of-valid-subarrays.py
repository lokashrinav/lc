class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        '''

        None, 2, None, 4, None

        [(0, 1), (1, 4)]

        total = 0

        [(0, 1), (2, 2)]

        total += 2 - 1 = 1

        [(0, 1), (2, 2), (3, 5)]

        [(0, 1), (2, 2), (3, 5)]

        total += 1

        [(0, 1), (2, 2), (4, 3)]

        total += 5 + 3 + 1

        '''

        stack = []
        total = 0
        for i in range(len(nums)):
            if not stack:
                stack.append((i, nums[i]))
            else:
                while stack and nums[i] < stack[-1][1]:
                    ind, num = stack.pop()
                    total += i - ind
                stack.append((i, nums[i]))
            #print(stack, total)

        while stack:
            ind, num = stack.pop()
            total += len(nums) - ind
        
        return total
