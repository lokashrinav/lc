class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        count = 0
        p1, p2 = 0, 0
        minDist = float('inf')
        while True:
            while count < target:
                if p2 == len(nums):
                    return minDist if minDist != float('inf') else 0
                count += nums[p2]
                p2 += 1

            minDist = min(p2 - p1, minDist)

            print(minDist)

            while count >= target:
                if p1 == p2:
                    return minDist if minDist != float('inf') else 0
                count -= nums[p1]
                p1 += 1
                if count >= target:
                    minDist = min(p2 - p1, minDist)
                    print(minDist)
            print("")

        return minDist if minDist != float('inf') else 0

