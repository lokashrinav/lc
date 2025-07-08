from bisect import bisect_left
from typing import List

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # First, we sort the events based on their ending time.
        events.sort(key=lambda event: event[1])

        # The number of events
        num_events = len(events)

        # Prepare a DP table with dimensions (number of events + 1) x (k + 1)
        dp_table = [[0] * (k + 1) for _ in range(num_events + 1)]

        # Iterate through each event, starting with index 1 for convenience
        for i, (start_time, _, value) in enumerate(events, 1):
            # Find the index of the last event that does not overlap with the current event
            previous_index = bisect_left(events, start_time, hi=i - 1, key=lambda event: event[1])

            # Update DP table for each of the k attendances
            for j in range(1, k + 1):
                # The value is the max between not attending this event and attending it
                dp_table[i][j] = max(
                    dp_table[i - 1][j],           # Not picking current event
                    dp_table[previous_index][j - 1] + value  # Picking current event
                )

        # The maximum value for attending at most k events is stored at dp_table[num_events][k]
        return dp_table[num_events][k]