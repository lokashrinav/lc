class Solution:
    def punishmentNumber(self, n: int) -> int:
        # Helper function to check if a square number can be split into two numbers that add up to the original number.
        def can_split_to_original(num_str: str, start_index: int, target_sum: int) -> bool:
            num_length = len(num_str)
            # If the starting index is beyond the string's length and target sum is zero, this is valid.
            if start_index >= num_length:
                return target_sum == 0
          
            current_num = 0
            # Consider different splits by incrementally including more digits.
            for j in range(start_index, num_length):
                current_num = current_num * 10 + int(num_str[j])
                # If the current number exceeds the target, there's no point in continuing.
                if current_num > target_sum:
                    break
                # Recursively check if the remaining string can fulfill the condition.
                if can_split_to_original(num_str, j + 1, target_sum - current_num):
                    return True
            return False

        # This variable holds the total sum of all square numbers fulfilling the condition.
        total_sum = 0
        # Iterate over the range 1 through n, inclusive.
        for i in range(1, n + 1):
            square_num = i * i  # Calculate the square of the number.
            # If the squared number can be split as desired, add to total sum.
            if can_split_to_original(str(square_num), 0, i):
                total_sum += square_num
      
        # Return the total sum of all such square numbers.
        return total_sum