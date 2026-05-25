class Twitter:

    def __init__(self):
        from collections import defaultdict
        self.users = defaultdict(list)
        self.follows = defaultdict(list)
        self.tweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.users[userId].append(tweetId)
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        news = [t for u, t in self.tweets if u in self.follows[userId] or u == userId]
        # print(news)
        return news[-1:-11:-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.follows[followerId]:
            self.follows[followerId].append(followeeId)
            # print(followerId,'follows',followeeId)
            # print(self.follows[followerId])
            return
        # print(followerId,'already followed', followeeId)
        # print(self.follows[followerId])

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].pop(self.follows[followerId].index(followeeId))
            # print(followerId,'UNfollow',self.follows[followerId].pop(self.follows[followerId].index(followeeId)))
            # print(self.follows[followerId])
            return
        # print(followerId,'Not follow',followeeId)
        # print(self.follows[followerId])
