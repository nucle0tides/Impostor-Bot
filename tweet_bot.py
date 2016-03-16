import twitter
import json
import random
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
            node_dict[word.lower()] = []
    return node_dict

def createEdges(graph):
    f = open('my_tweets.txt', 'r')
    current_word = ''
    next_word = ''
    for lines in f:
        line = lines.split()
        print(line)
        for i in range(len(line)):
            current_word = line[i]
            if(i < len(line) - 1):
                next_word = line[i + 1]
                graph[current_word.lower()].append(next_word.lower())

    return graph

def getGraph(filename):
    f = open(filename, 'r')
    graph = json.loads(f.read())
    return graph

def pickBeginning(graph):
    beginning = []
    while len(beginning) < 1:
        beginning = graph[random.choice(graph.keys())]
    return beginning[0]

def constructSentence(previousState, graph):
    hasNextState = True
    sentence = previousState
    current_word = ''
    while hasNextState:
        if graph.has_key(previousState):
            current_word = random.choice(graph[previousState])
            sentence += " " + current_word
            previousState = current_word
            hasNextState = True
        else:
            hasNextState = False
    return sentence

if __name__ == '__main__':
    #getAllTweets("nucle0tides")
    # graph = makeNodes()
    # print(graph)
    # graph = createEdges(graph)
    # print(graph)
    # json = json.dumps(graph)
    # graph_json = open('tweet_graph.json', 'w')
    # graph_json.write(json)
    graph = getGraph('tweet_graph.json')
    beginning = pickBeginning(graph)
    sentence = constructSentence(beginning, graph)
    print(sentence.encode('utf-8'))
