class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        queue = deque()
        for i in range(3):
            queue.append(nums[i])
        
        total = 0
        if float(queue[0]) + queue[-1] == queue[1] / 2:
            total += 1
        
        for i in range(3, len(nums)):
            queue.popleft()
            queue.append(nums[i])
            if float(queue[0]) + queue[-1] == queue[1] / 2:
                total += 1

        return total