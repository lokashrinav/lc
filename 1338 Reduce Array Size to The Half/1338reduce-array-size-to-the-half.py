class Solution:
    def minSetSize(self, arr: List[int]) -> int:

        hmap = Counter(arr)

        maxHeap = [(-val, key) for key, val in hmap.items()]

        heapify(maxHeap)
        total = 0
        count = 0

        while True:
            if total >= len(arr) / 2:
                break
            val, key = heappop(maxHeap)
            val = -val
            count += 1
            total += val
        
        return count
        