class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        queue = deque()
        for i in range(k):
            if not queue:
                queue.append(nums[i])
            elif nums[i] <= queue[-1]:
                queue.append(nums[i])
            else:
                while queue and nums[i] > queue[-1]:
                    queue.pop()
                queue.append(nums[i])

        res.append(queue[0])
        
        for i in range(k, len(nums)):
            if nums[i - k] == queue[0]:
                queue.popleft()
            if not queue:
                queue.append(nums[i])
            elif nums[i] <= queue[-1]:
                queue.append(nums[i])
            else:
                while queue and nums[i] > queue[-1]:
                    queue.pop()
                queue.append(nums[i])
            res.append(queue[0])
        
        return res
        
        
