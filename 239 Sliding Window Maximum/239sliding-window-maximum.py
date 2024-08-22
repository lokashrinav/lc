class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        for i in range(k):
            while q and q[-1] < nums[i]:
                q.pop()
            q.append(nums[i])
        res.append(q[0])

        for i in range(len(nums) - k):
            while q and q[-1] < nums[i + k]:
                q.pop()
            q.append(nums[i + k])
            if nums[i] == q[0]:
                q.popleft()
            res.append(q[0])
        return res
        
        


            
        