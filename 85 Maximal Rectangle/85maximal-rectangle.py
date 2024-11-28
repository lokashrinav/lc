class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        def largest(arr):
            stack = []
            maxArea = 0
            for i in range(len(matrix[0])):
                start = i
                while stack and stack[-1][1] > arr[i]:
                    ind, elem = stack.pop()
                    maxArea = max(maxArea, elem * (i - ind))
                    start = ind
                stack.append((start, arr[i]))

            for i, h in stack:
                maxArea = max(maxArea, h * (len(arr) - i))
            
            return maxArea

        maxNum = float('-inf')
        arr = [0] * len(matrix[0])
        
        for i in range(len(matrix)):
            for p in range(len(arr)):
                if matrix[i][p] == "0":
                    arr[p] = 0
                else:
                    arr[p] = arr[p] + 1
            maxNum = max(largest(arr), maxNum)

        return maxNum

