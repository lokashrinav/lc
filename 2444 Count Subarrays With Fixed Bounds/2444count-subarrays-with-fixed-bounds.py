from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], min_k: int, max_k: int) -> int:
        # Initialize pointers for tracking the positions of min_k, max_k, and out-of-range elements
        last_min_k = last_max_k = last_out_of_range = -1
      
        # Initialize the counter for the valid subarrays
        valid_subarrays_count = 0
      
        # Iterate through the list, checking each number against min_k and max_k
        for index, value in enumerate(nums):
            # Invalidate the subarray if the value is out of the specified range
            if value < min_k or value > max_k:
                last_out_of_range = index

            # Update the last seen index for min_k, if found
            if value == min_k:
                last_min_k = index

            # Update the last seen index for max_k, if found
            if value == max_k:
                last_max_k = index
          
            # Add to the count the number of valid subarrays ending with the current element
            # which is determined by the smallest index among last_min_k and last_max_k after the 
            # last out-of-range element
            valid_subarrays_count += max(0, min(last_min_k, last_max_k) - last_out_of_range)
      
        # Return the total count of valid subarrays
        return valid_subarrays_count