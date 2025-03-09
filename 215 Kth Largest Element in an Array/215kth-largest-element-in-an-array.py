from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Convert kth largest to kth smallest index.
        k = len(nums) - k

        def quick(l: int, r: int) -> int:
            # Choose a pivot. Here we take the rightmost element.
            pivot = nums[r]
            # Initialize pointers for three partitions:
            # [l, low-1] < pivot, [low, mid-1] == pivot, [mid, high] are unknown, [high+1, r] > pivot.
            low, mid, high = l, l, r

            while mid <= high:
                if nums[mid] < pivot:
                    nums[low], nums[mid] = nums[mid], nums[low]
                    low += 1
                    mid += 1
                elif nums[mid] > pivot:
                    nums[mid], nums[high] = nums[high], nums[mid]
                    high -= 1
                else:  # nums[mid] == pivot
                    mid += 1

            # Now:
            # - indices l to low-1 are less than pivot
            # - indices low to high are equal to pivot
            # - indices high+1 to r are greater than pivot

            # Decide in which segment k lies.
            if k < low:
                return quick(l, low - 1)
            elif k > high:
                return quick(high + 1, r)
            else:
                # k falls in the segment equal to pivot.
                return nums[k]

        return quick(0, len(nums) - 1)
