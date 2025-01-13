class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            #print(l, r, nums[l], nums[m], nums[r])
            if nums[m] == target:
                return True
            elif nums[m] == nums[r] == nums[l]:
                r -= 1
                l += 1
            elif nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return False
            
        