class FileSharing:

    def __init__(self, m: int):
        self.hmap = {}
        self.hmap2 = defaultdict(SortedSet)
        self.minHeap = []
        self.count = 1
        
    def join(self, ownedChunks: List[int]) -> int:
        main = None
        if self.minHeap:
            out = heappop(self.minHeap)
            self.hmap[out] = ownedChunks
            main = out
        else:
            self.hmap[self.count] = ownedChunks
            main = self.count
            self.count += 1
        
        for elem in ownedChunks:
            self.hmap2[elem].add(main)
        
        return main

    def leave(self, userID: int) -> None:
        idk = self.hmap[userID]
        for elem in idk:
            if userID in self.hmap2[elem]:
                self.hmap2[elem].remove(userID)

        del self.hmap[userID]

        heappush(self.minHeap, userID)

    def request(self, userID: int, chunkID: int) -> List[int]:
        prev = list(self.hmap2[chunkID])

        if prev:
            self.hmap[userID].append(chunkID)
            self.hmap2[chunkID].add(userID)
            
        return prev
        


# Your FileSharing object will be instantiated and called as such:
# obj = FileSharing(m)
# param_1 = obj.join(ownedChunks)
# obj.leave(userID)
# param_3 = obj.request(userID,chunkID)