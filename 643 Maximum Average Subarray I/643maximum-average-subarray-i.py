class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        calc = sum(nums[:k])
        p1, p2 = 0, k

        maxCalc = calc
        while p2 < len(nums):
            calc -= nums[p1]
            calc += nums[p2]
            maxCalc = max(calc, maxCalc)
            p2 += 1
            p1 += 1
        return maxCalc / k
        
        
