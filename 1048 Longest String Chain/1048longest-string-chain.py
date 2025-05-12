class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        maxChain = 0

        hmap = {}

        for elem in words:
            hmap[elem] = 0

        minHeap = [(-len(word), word) for word in words]

        heapify(minHeap)

        while minHeap:
            length, word = heappop(minHeap)
            for i in range(len(word)):
                calc = word[:i] + word[i+1:]
                if calc in hmap:
                    hmap[calc] = max(hmap[calc], 1 + hmap[word])

        calc2 = max(hmap.values())
        return calc2 + 1                
