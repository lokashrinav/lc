class Solution:
    def findMaximums(self, nums: List[int]) -> List[int]:
        arr = nums
        n = len(arr)
        prev_smaller = [-1] * n
        next_smaller = [n] * n

        # Previous smaller: strict smaller to the left
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            prev_smaller[i] = stack[-1] if stack else -1
            stack.append(i)

        # Next smaller: smaller or equal to the right
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            next_smaller[i] = stack[-1] if stack else n
            stack.append(i)

        # ans_len[L] stores the best value for window length L
        ans_len = [0] * (n + 1)
        for i in range(n):
            L = next_smaller[i] - prev_smaller[i] - 1
            ans_len[L] = max(ans_len[L], arr[i])

        # Fill blanks by carrying from larger windows
        for L in range(n - 1, 0, -1):
            ans_len[L] = max(ans_len[L], ans_len[L + 1])

        return ans_len[1:]