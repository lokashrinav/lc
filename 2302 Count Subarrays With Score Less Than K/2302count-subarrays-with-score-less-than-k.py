from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # Initialize answer, current sum, and start index of the window
        answer = current_sum = start_index = 0
      
        # Iterate through the array with index and value
        for end_index, value in enumerate(nums):
            # Add the current number to the current sum
            current_sum += value
          
            # While the product of the sum of the current subarray
            # and the length of the subarray is at least k,
            # shrink the window from the left (increase start_index)
            while current_sum * (end_index - start_index + 1) >= k:
                current_sum -= nums[start_index]
                start_index += 1
          
            # The number of subarrays ending with the current number
            # is the length of the current window (end_index - start_index + 1)
            answer += end_index - start_index + 1
      
        # Return the total number of subarrays found
        return answer
