class Twitter:

    def __init__(self):
        self.followers = defaultdict(set)
        self.tweets = defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]: 
        self.followers[userId].add(userId)
        heap = []
        res = []
        for foll in self.followers[userId]:
            if foll in self.tweets:
                count, tweetID = self.tweets[foll][len(self.tweets[foll]) - 1]
                currID = foll
                heapq.heappush(heap, [count, tweetID, currID, len(self.tweets[foll]) - 2])
        while heap and len(res) < 10:
            count, tweetID, currID, index = heapq.heappop(heap)
            res.append(tweetID)
            if index >= 0:
                count, tweetId = self.tweets[currID][index]
                heapq.heappush(heap, [count, tweetId, currID, index - 1])
        return res
        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers and followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)