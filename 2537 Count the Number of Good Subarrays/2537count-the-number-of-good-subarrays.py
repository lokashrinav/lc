class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        
        l = 0
        hmap = defaultdict(int)
        total = 0
        count = 0
        i = 0
        while i < len(nums):
            count += hmap[nums[i]]
            hmap[nums[i]] += 1

            while count >= k:
                total += (len(nums) - i)
                hmap[nums[l]] -= 1
                count -= hmap[nums[l]]
                l += 1

            i += 1
        
        return total
            

            

