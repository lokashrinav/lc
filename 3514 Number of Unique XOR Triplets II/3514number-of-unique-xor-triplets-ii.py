class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        xor_pairs = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                xor_pairs.add(nums[i] ^ nums[j])
                

        result = set(nums)
        
        for x in xor_pairs:
            for num in nums:
                result.add(x ^ num)

        return len(result)
