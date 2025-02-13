class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        heapq.heapify(nums)
        count = 0

        for num in nums:
            if num >= k:
                count += 1

        total = 0
        while count != len(nums):
            out1 = heapq.heappop(nums)
            out2 = heapq.heappop(nums)
            if out2 >= k:
                count -= 1
            
            added = min(out1, out2) * 2 + max(out1, out2)
            if added >= k:
                count += 1

            heapq.heappush(nums, added)
            total += 1
        
        return total

