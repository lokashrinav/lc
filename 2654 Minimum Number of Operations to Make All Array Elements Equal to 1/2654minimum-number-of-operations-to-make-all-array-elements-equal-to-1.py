class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        
        if 1 in nums:
            return n - nums.count(1)
        
        min_subarray_length = float('inf')
        for i in range(n):
            current_gcd = nums[i]
            for j in range(i, n):
                current_gcd = gcd(current_gcd, nums[j])
                if current_gcd == 1:
                    min_subarray_length = min(min_subarray_length, j - i + 1)
                    break
        
        if min_subarray_length == float('inf'):
            return -1
        
        return (min_subarray_length - 1) + (n - 1)