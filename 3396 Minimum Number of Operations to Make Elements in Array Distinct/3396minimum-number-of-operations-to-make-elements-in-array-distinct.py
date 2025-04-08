class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        queue = deque(nums)
        hmap = Counter(nums)

        above = 0
        for elem, val in hmap.items():
            if val > 1:
                above += 1
        
        if above == 0:
            return 0

        count = 0
        while queue:
            count += 1
            for i in range(min(3, len(queue))):
                out = queue.popleft()
                hmap[out] -= 1
                if hmap[out] == 1:
                    above -= 1
            if above == 0:
                return count            
        
        return count



        