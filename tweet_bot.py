import twitter
import json
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
    f = open('my_tweets.txt', 'w')
    for i in out:
        f.write("%s\n" % i)

#who knows if this is a good way to do this. I sure don't know. 
def makeNodes():
    node_dict = {}
    f = open('my_tweets.txt', 'r')
    for lines in f:
        for word in lines.split(' '):
            if 'http' not in word and '@' not in word and word not in tweet_graph:
                node_dict[word] = []
    return node_dict

def createEdges(nodes):
    f = open('my_tweets.txt', 'r')
    for lines in f:
        for word in lines.split('')
            pass


if __name__ == '__main__':
    #getAllTweets("nucle0tides")
    graph = makeTweetGraph()
    print(graph)
