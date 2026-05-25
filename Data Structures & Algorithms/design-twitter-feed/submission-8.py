class Twitter:

    def __init__(self):
        from collections import defaultdict, deque
        self.u_t = defaultdict(list)
        self.follows = defaultdict(set)
        self.t = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.t += 1
        self.u_t[userId].append((self.t, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        import heapq

        users = self.follows[userId] | {userId}

        streams = [self.u_t[u][:-11:-1] for u in users if self.u_t[u]]
        merged = heapq.merge(*streams, key=lambda x: -x[0])
        a = []
        for t, tweet in merged:
            a.append(tweet)
            if len(a) == 10:
                break
        return a

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
