from math import ceil
from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int, y: int) -> int:
        # Helper function to check if the operation can be completed with 't' operations.
        def is_possible_with_t_operations(t: int) -> bool:
            # Initialize count of operations.
            operations = 0
            # Iterate through each number in the list.
            for value in nums:
                # If the value is greater than 't' times 'y', operations are needed.
                if value > t * y:
                    # Calculate the number of operations needed for the current value, and add to the total.
                    operations += ceil((value - t * y) / (x - y))
            # Return True if the counted operations are less than or equal to 't', else return False.
            return operations <= t

        # Initialize left and right pointers for the binary search.
        left, right = 0, max(nums)
        # Perform binary search to find the minimum number of operations required.
        while left < right:
            # Get the middle value between left and right.
            mid = (left + right) >> 1  # Using bitwise shift to divide by 2.
            # If the operation is possible with 'mid' operations, move the right boundary to 'mid'.
            if is_possible_with_t_operations(mid):
                right = mid
            # Otherwise, move the left boundary past 'mid'.
            else:
                left = mid + 1
        # The left pointer will now point to the minimum number of operations needed.
        return left
