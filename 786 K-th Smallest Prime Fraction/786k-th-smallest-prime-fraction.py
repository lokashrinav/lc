class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:

        minHeap = []

        for i in range(1, len(arr)):
            heappush(minHeap, (arr[0] / arr[i], 0, i))
        
        out = None
        i, j = None, None
        while minHeap and k:
            out, i, j = heappop(minHeap)
            if i + 1 < j:
                heappush(minHeap, (arr[i + 1] / arr[j], i + 1, j))
            k -= 1
        
        return [arr[i], arr[j]]

