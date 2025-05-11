class Solution:
    def minDeletion(self, s: str, k: int) -> int:

        hmap = Counter(s)

        minHeap = []

        for key, val in hmap.items():
            minHeap.append((val, key))

        if k > len(minHeap):
            return 0

        heapify(minHeap)
        total = 0
        num = len(minHeap) - k

        while minHeap and num:
            out, val = heappop(minHeap)
            total += out
            num -= 1

        return total
        