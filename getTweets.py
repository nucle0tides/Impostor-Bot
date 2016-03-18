import twitter
from keys import *

# Authenticate via OAuth
api = twitter.Api(
    consumer_key,
    consumer_secret,
    token_key,
    token_secret
)

def getAllTweets(screen_name):
    new = []
    all_tweets = []
    new = api.GetUserTimeline(screen_name = screen_name, count = 200)
    all_tweets.extend(new)
    oldest = all_tweets[-1].id - 1

    while(len(new) > 0):
        new = api.GetUserTimeline(screen_name = screen_name, count = 200, max_id = oldest)
        all_tweets.extend(new)
        oldest = all_tweets[-1].id - 1

    out = [tweet.text.encode('utf-8') for tweet in all_tweets]
    f = open('static/tweets/' + screen_name + '_tweets.txt', 'w')
    for i in out:
        f.write("%s\n" % i)
