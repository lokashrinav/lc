class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        n = len(seats)
        l = None
        maxCount = 0
        curr = 0

        for i in range(n):
            if seats[i] == 1:
                if l is None:
                    maxCount = max(maxCount, i)
                else:
                    maxCount = max(maxCount, ((i - l) // 2))
                l = i

        maxCount = max(maxCount, i - l)

        return maxCount
            
            


