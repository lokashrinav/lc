class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        # 3 1 2

        # 3 9 18 19

        minVal, maxVal = min(nums), max(nums)

        size = max(1, (maxVal - minVal) // (len(nums) - 1))
        hmap = defaultdict(list)

        for i in range(len(nums)):
            key = (nums[i] - minVal) // size
            if not hmap[key]:
                hmap[key] = [nums[i], nums[i]]
            else:
                hmap[key] = [max(hmap[key][0], nums[i]), min(hmap[key][1], nums[i])]
        
        ans = 0
        prevKey = -1

        for key in sorted(hmap.keys()):
            if prevKey != -1:
                ans = max(ans, hmap[key][1] - hmap[prevKey][0])
            prevKey = key
        
        return ans










        
