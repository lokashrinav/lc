class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)  # Get the length of the colors list
        ans = 0  # Initialize the answer to 0, which will count valid alternating groups
        cnt = 0  # Initialize the count of consecutive alternating colors

        # Iterate over the list twice to account for circular nature
        for i in range(n * 2):
            # If the current color is the same as the previous, reset count
            if i > 0 and colors[i % n] == colors[(i - 1) % n]:
                cnt = 1
            else:
                # Increment the count for consecutive alternating colors
                cnt += 1

            # Check if in the second half of the iteration and count is at least k
            # Increase the answer if conditions are met
            if i >= n and cnt >= k:
                ans += 1

        return ans  # Return the total number of valid alternating groups        