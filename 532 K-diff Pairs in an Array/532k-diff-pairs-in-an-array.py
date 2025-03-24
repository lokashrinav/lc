class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        hmap = defaultdict(int)
        total = 0
        hset = set()

        for i in range(len(nums)):
            # print(hmap, total)
            if nums[i] + k in hmap:
                if (nums[i], nums[i] + k) in hset or (nums[i] + k, nums[i]) in hset:
                    continue
                total += 1
                hset.add((nums[i], nums[i] + k))
            if nums[i] - k in hmap:
                if (nums[i], nums[i] - k) in hset or (nums[i] - k, nums[i]) in hset:
                    continue
                total += 1
                hset.add((nums[i], nums[i] - k))

            hmap[nums[i]] += 1

        return total

