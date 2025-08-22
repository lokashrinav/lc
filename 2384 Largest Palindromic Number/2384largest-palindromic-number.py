class Solution:
    def largestPalindromic(self, num: str) -> str:
        '''
        '''

        nums = [0] * 10
        for elem in num:
            nums[int(elem)] += 1

        stack  = []
        mid = ''
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0:
                continue
            stack.append(nums[i] // 2 * str(i))
            if mid == '' and nums[i] % 2:
                mid = i

        curr = ''.join(str(s) for s in stack) + str(mid) + ''.join(str(s) for s in stack[::-1])

        queue = deque(list(curr))

        while len(queue) >= 2 and queue[0] == '0':
            queue.popleft()
            queue.pop()

        if not queue:
            return '0'

        return ''.join(list(queue))
            
        