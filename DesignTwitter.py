class Twitter:
    def __init__(self):
        self.tweets = defaultdict(list)
        self.follow = defaultdict(set)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        answer = []
        minHeap = []

        self.follow[userId].add(userId)

        for followerId in self.follow[userId]:
            if followerId in self.tweets:
                retrieveTweet = self.tweets[followerId]
                ind = len(retrieveTweet) - 1
                newestTweet = retrieveTweet[ind]
                # Store count, tweetId, userId, index
                store = [newestTweet[0], newestTweet[1], followerId, ind]
                heapq.heappush(minHeap, store)

        while minHeap and len(answer)<10:
            # newestTweet =  [count, tweetId, userId, index]
            newestTweet = heapq.heappop(minHeap)
            answer.append(newestTweet[1])

            if newestTweet[3] >= 0:
                retrieveTweet = self.tweets[newestTweet[2]][newestTweet[3]]
                store = [retrieveTweet[0], retrieveTweet[1], newestTweet[2], newestTweet[3]-1]
                heapq.heappush(minHeap, store)
        return answer

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow[followerId]:
            self.follow[followerId].remove(followeeId)
'''
    def getNewsFeed(self, userId: int) -> List[int]:
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res
'''
# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)