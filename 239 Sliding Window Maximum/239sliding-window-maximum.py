class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        queue = deque()
        res = []

        for i in range(k):
            while queue and nums[i] >= nums[queue[-1]]:
                out = queue.pop()
            queue.append(i)
    
        res.append(nums[queue[0]])

        print(queue)
        
        for i in range(k, len(nums)):
            if i - k == queue[0]:
                queue.popleft()
            while queue and nums[i] >= nums[queue[-1]]:
                out = queue.pop()
            queue.append(i)
            res.append(nums[queue[0]])
        
        return res