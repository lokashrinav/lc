class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            p1 = i + 1
            p2 = len(nums) - 1
            while p1 < p2:
                if p2 + 1 < len(nums) and nums[p2] == nums[p2 + 1]:
                    p2 -= 1
                elif p1 - 1 > i and nums[p1] == nums[p1 - 1]:
                    p1 += 1
                elif nums[p1] + nums[p2] == -nums[i]:
                    res.append([nums[p1], nums[p2], nums[i]])
                    p2 -= 1
                    p1 += 1
                elif nums[p1] + nums[p2] > -nums[i]:
                    p2 -= 1
                else:
                    p1 += 1
        
        return res