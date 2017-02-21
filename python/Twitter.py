"""
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the 10 most recent tweets in the user's news feed. Your design should support the following methods:

postTweet(userId, tweetId): Compose a new tweet.
getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
follow(followerId, followeeId): Follower follows a followee.
unfollow(followerId, followeeId): Follower unfollows a followee.
Example:

Twitter twitter = new Twitter();

// User 1 posts a new tweet (id = 5).
twitter.postTweet(1, 5);

// User 1's news feed should return a list with 1 tweet id -> [5].
twitter.getNewsFeed(1);

// User 1 follows user 2.
twitter.follow(1, 2);

// User 2 posts a new tweet (id = 6).
twitter.postTweet(2, 6);

// User 1's news feed should return a list with 2 tweet ids -> [6, 5].
// Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.getNewsFeed(1);

// User 1 unfollows user 2.
twitter.unfollow(1, 2);

// User 1's news feed should return a list with 1 tweet id -> [5],
// since user 1 is no longer following user 2.
twitter.getNewsFeed(1);
"""


import collections

class Tweet(object):
    def __init__(self, id, time):
        self.id = id
        self.time = time
        self.next = None

class User(object):
    def __init__(self, id):
        self.id = id
        self.followee = set()
        self.tweets = list()

    def follow(self, id):
        self.followee.add(id)

    def unfollow(self, id):
        self.followee.discard(id)

    def post(self, id, time):
        tweet = Tweet(id, time)
        self.tweets.append(tweet)

    def getTweets(self):
        return self.tweets

class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.users = collections.defaultdict()
        self.time = 0

    def register(self, userId):
        self.users[userId] = User(userId)

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        if userId not in self.users:
            self.register(userId)
        self.users[userId].post(tweetId, self.time)
        self.time += 1

    def getNewsFeed(self, userId, n=10):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        if userId not in self.users:
            return list()
        users = map(lambda x: self.users[x], (self.users[userId].followee | {userId}) )
        news = list()
        for user in users:
            news += user.getTweets()
        news.sort(key = lambda x: x.time, reverse = True)
        return map(lambda tweet: tweet.id, news[:10])

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId not in self.users:
            self.register(followerId)
        if followeeId not in self.users:
            self.register(followeeId)
        self.users[followerId].follow(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId in self.users:
            self.users[followerId].unfollow(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
