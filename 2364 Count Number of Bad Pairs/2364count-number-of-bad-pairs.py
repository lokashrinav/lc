class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # 2, 1

        # nums[i] - i != nums[j] - j

        total = (len(nums) * (len(nums) - 1)) // 2
        count = 0
        hmap = defaultdict(int)
        # 4, 1, 3
        # 4, 0, 0
        
        for i in range(len(nums)):
            count += hmap[nums[i] - i]
            hmap[nums[i] - i] += 1

        return total - count

                
        