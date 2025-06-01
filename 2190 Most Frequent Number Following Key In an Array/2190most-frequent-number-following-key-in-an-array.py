class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        
        hmap = defaultdict(int)
        for i in range(1, len(nums)):
            if nums[i - 1] == key:
                hmap[nums[i]] += 1
        
        saved = 0
        maxCount = 0

        for key, val in hmap.items():
            if val > maxCount:
                saved = key
                maxCount = val

        return saved
