from math import comb

class Solution:
    def distributeCandies(self, candies: int, limit: int) -> int:
        # Check if the total number of candies is too large to distribute within the limit
        if candies > 3 * limit:
            # If so, return 0 as the distribution is not possible
            return 0
      
        # Calculate the possible distributions without any constraints
        # This is done by choosing 2 from 'candies + 2', which represents
        # distributing candies into 3 slots with restrictions (the Partitions of n)
        possible_distributions = comb(candies + 2, 2)
      
        # Now we need to subtract the invalid distributions
        # where one child would get more than the limit
        if candies > limit:
            # Subtract the combinations where any one child gets more than the limit
            possible_distributions -= 3 * comb(candies - limit + 1, 2)
      
        # Further adjust the count if one child gets more than double the limit
        if candies - 2 >= 2 * limit:
            # Add back the combinations that we subtracted 
            # twice due to overlap in our previous calculation
            possible_distributions += 3 * comb(candies - 2 * limit, 2)
      
        # Return the final number of possible distributions
        return possible_distributions