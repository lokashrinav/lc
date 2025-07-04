class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:


        nums.sort()

        count = 0

        p1, p2 = 0, len(nums) - 1

        while p1 < p2:
            if nums[p1] + nums[p2] > k:
                p2 -= 1
            elif nums[p1] + nums[p2] < k:
                p1 += 1
            else:
                p2 -= 1
                p1 += 1
                count += 1
        
        return count
                
