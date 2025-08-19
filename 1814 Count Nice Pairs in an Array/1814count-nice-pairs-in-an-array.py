class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        # 18 = x - rev(x)
        # x = 42, 24
        # 42 + 23 = 41 + 24

        total = 0
        hmap = defaultdict(int)
        for i in range(len(nums)):
            num = nums[i]
            diff = num - int(str(num)[::-1])
            total += hmap[diff]
            hmap[diff] += 1
        
        return total % (10 ** 9 + 7)
