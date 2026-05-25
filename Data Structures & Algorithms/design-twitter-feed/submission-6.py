class Twitter:

    def __init__(self):
        from collections import defaultdict, deque
        self.u_t = defaultdict(lambda: deque(maxlen = 10))
        self.follows = defaultdict(set)
        self.t = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.t += 1
        self.u_t[userId].append((self.t, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        import heapq
        a = []
        h = []
        users = self.follows[userId] | {userId}

        for u in users:
            if self.u_t[u]:
                i = len(self.u_t[u])-1
                t, tweet = self.u_t[u][i]
                heapq.heappush(h, (-t, tweet, u, i))
        while h and len(a) < 10:
            t, tweet, u, i = heapq.heappop(h)
            a.append(tweet)
            if i > 0:
                i -= 1
                t, tweet = self.u_t[u][i]
                heapq.heappush(h, (-t, tweet, u, i))
        return a

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
