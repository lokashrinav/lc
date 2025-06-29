from bisect import bisect_right

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        # Constant for modulo operation
        mod = 10**9 + 7
        # Sort the input list to make use of binary search later
        nums.sort()
        n = len(nums)
      
        # Initialize power_of_two array which stores 2^i values modulo mod
        power_of_two = [1] * (n + 1)
        for i in range(1, n + 1):
            # Efficiently precompute powers of 2 mod mod
            power_of_two[i] = power_of_two[i - 1] * 2 % mod
      
        # Initialize the answer to 0
        ans = 0
        # Loop through the list
        for i, num in enumerate(nums):
            # Stop if the smallest number in a subsequence is too big
            if num * 2 > target:
                break
            # Find the largest number that can be paired with nums[i]
            # such that their sum does not exceed target.
            j = bisect_right(nums, target - num, i + 1) - 1
          
            # Add the count of valid subsequences starting with nums[i]
            # The count is the number of different ways to form subsequences 
            # from i+1 to j (inclusive), which is simply 2 raised to the power
            # of the number of elements between i and j, modulo mod.
            # This relies on the fact that for every element between i and j,
            # we can choose to either include it or not in our subsequence.
            ans = (ans + power_of_two[j - i]) % mod
      
        # Return the total count of valid subsequences modulo mod
        return ans