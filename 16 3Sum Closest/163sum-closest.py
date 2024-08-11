class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        hmap = {}
        curr = 0
        diff = float('inf')
        saved_vals = [0, 0, 0]
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum1 = nums[i] + nums[l] + nums[r] 
                if sum1 == target:
                    return sum1
                elif sum1 > target:
                    if abs(sum1 - target) < diff:
                        saved = [nums[i], nums[l], nums[r] ]
                        curr = sum1
                        diff = abs(sum1 - target)
                    r -= 1
                else:
                    if abs(sum1 - target) < diff:
                        saved = [nums[i], nums[l], nums[r] ]
                        curr = sum1
                        diff = abs(sum1 - target)
                    l += 1 
        print(saved)
        return curr
                    



        