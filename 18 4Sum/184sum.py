class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates
            for p in range(i + 1, len(nums) - 1):
                if p > i + 1 and nums[p] == nums[p - 1]:
                    continue  # Skip duplicates
                l, r = p + 1, len(nums) - 1
                while l < r:
                    sum1 = nums[i] + nums[p] + nums[l] + nums[r]
                    if sum1 == target:
                        res.append([nums[i], nums[p], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1 
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif sum1 > target:
                        r -= 1
                    else:
                        l += 1
        
        return res

        