class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        
        hmap = defaultdict(int)
        count = 0
        for i in range(len(nums)):
            for p in range(i + 1, len(nums)):
                product = nums[i] * nums[p]
                count += hmap[product]
                hmap[product] += 1

        return count * 8
        

                

        