from bisect import bisect_left
from typing import List

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        # Helper function to check if it is possible to have 'diff' as the maximum difference
        # of at least 'p' pairs after removing some pairs from 'nums'.
        def is_possible(diff: int) -> bool:
            pairs_count = 0  # Count of valid pairs
            i = 0  # Index to iterate through 'nums'
          
            # Loop through the numbers and determine if we can form enough pairs
            while i < len(nums) - 1:
                # If the difference between the current pair is less than or equal to 'diff'
                if nums[i + 1] - nums[i] <= diff:
                    pairs_count += 1  # Acceptable pair, increment the count
                    i += 2  # Skip the next element as it has been paired up
                else:
                    i += 1  # Move to the next element to find a pair
                  
            # Return True if we have enough pairs, otherwise False
            return pairs_count >= p

        # Sort the input array before running the binary search algorithm
        nums.sort()
    
        # Use binary search to find the minimum possible 'diff' such that at least 'p' pairs
        # have a difference of 'diff' or less. The search range is from 0 to the maximum
        # difference in the sorted array.
        min_possible_diff = bisect_left(range(nums[-1] - nums[0] + 1), True, key=is_possible)

        return min_possible_diff