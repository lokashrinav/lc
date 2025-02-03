class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxNum = 0
        curr = 0

        # [(0, 2), (1, 4)]
        for i in range(len(heights)):
            if not stack:
                stack.append((i, heights[i]))
            else:
                ind = i
                while stack and stack[-1][1] > heights[i]:
                    ind, num = stack.pop()
                    curr = (i - ind) * num
                    maxNum = max(maxNum, curr)
                stack.append((ind, heights[i]))

        while stack:
            ind, num = stack.pop()
            curr = (len(heights) - ind) * num
            maxNum = max(maxNum, curr)

        return maxNum
