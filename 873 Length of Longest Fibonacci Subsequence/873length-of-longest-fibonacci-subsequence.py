class Solution:
    def lenLongestFibSubseq(self, arr):
        # Create a hash map to store value to index mappings for quick access
        value_to_index = {value: index for index, value in enumerate(arr)}
        n = len(arr)
      
        # Initialize a 2D array for dynamic programming, setting initial subsequence sizes to 2
        dp = [[2 for _ in range(n)] for _ in range(n)]
      
        # This variable will keep track of the longest fib sequence found
        longest_fib_sequence = 0
      
        # Iterate over pairs of numbers in the array to build up sequences
        for i in range(n):
            for j in range(i):
                # Find the previous number in the potential Fibonacci sequence
                difference = arr[i] - arr[j]
                # Check if the number exists in our array and precedes the second number (j)
                if difference in value_to_index and value_to_index[difference] < j:
                    # The k index refers to the position of the previous number
                    prev_index = value_to_index[difference]
                    # Update the DP table by extending the sequence found from prev_index and j
                    dp[j][i] = max(dp[j][i], dp[prev_index][j] + 1)
                    # Update the answer if a longer sequence is found
                    longest_fib_sequence = max(longest_fib_sequence, dp[j][i])
      
        return longest_fib_sequence