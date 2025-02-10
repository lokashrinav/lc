class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        prefix_sum = 0
        min_heap = []
        operations = 0

        for num in nums:
            prefix_sum += num
            heapq.heappush(min_heap, num)

            if prefix_sum < 0:
                smallest = heapq.heappop(min_heap)  # Remove smallest element
                prefix_sum -= smallest  # Adjust sum after removing it
                operations += 1

        return operations