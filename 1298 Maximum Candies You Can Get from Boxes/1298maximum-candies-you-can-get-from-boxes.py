from collections import deque
from typing import List

class Solution:
    def maxCandies(
        self,
        statuses: List[int],  # statuses of boxes (0 for locked, 1 for open)
        candies: List[int],  # number of candies in each box
        keys: List[List[int]],  # list of keys for each box
        containedBoxes: List[List[int]],  # list of boxes contained within each box
        initialBoxes: List[int],  # list of boxes you start with
    ) -> int:
        # Queue with all the open boxes we can go through
        queue = deque([box for box in initialBoxes if statuses[box] == 1])
        # Calculate initial number of candies from open boxes
        total_candies = sum(candies[box] for box in initialBoxes if statuses[box] == 1)
        # Keep track of all boxes in hand whether they are locked or not
        boxes_in_hand = set(initialBoxes)
        # Keep a set of boxes from which candies have been taken
        boxes_accessed = {box for box in initialBoxes if statuses[box] == 1}

        # Keep iterating while there are boxes in the queue
        while queue:
            current_box = queue.popleft()  # Take the first box from the queue
            # Iterate over the keys contained in the current box
            for key in keys[current_box]:
                statuses[key] = 1  # Use the key to open the box with the matching number
                # Check if the now-opened box is in hand and hasn't been accessed yet
                if key in boxes_in_hand and key not in boxes_accessed:
                    total_candies += candies[key]  # Add the candies from the box
                    boxes_accessed.add(key)  # Mark the box as accessed
                    queue.append(key)  # Add the box to the queue to process further

            # Iterate over the boxes contained within the current box
            for box_id in containedBoxes[current_box]:
                boxes_in_hand.add(box_id)  # Add the contained box to boxes in hand
                # Check if the box is open and hasn't been accessed yet
                if statuses[box_id] and box_id not in boxes_accessed:
                    total_candies += candies[box_id]  # Add candies from the contained box
                    boxes_accessed.add(box_id)  # Mark the contained box as accessed
                    queue.append(box_id)  # Add the contained box to the queue for further processing

        # Return the total number of candies collected
        return total_candies