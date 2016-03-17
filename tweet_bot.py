import twitter
import json
import random
import re
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
    f = open(screen_name + '_tweets.txt', 'w')
    for i in out:
        f.write("%s\n" % i)

#who knows if this is a good way to do this. I sure don't know.
def makeNodes(person):
    node_dict = {}
    f = open(person + '_tweets.txt', 'r')
    for lines in f:
        for word in lines.split(' '):
            node_dict[word.lower()] = []
    f.close()
    return node_dict

def createEdges(graph, person):
    f = open(person + '_tweets.txt', 'r')
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
    f.close()
    return graph

def getGraph(person):
    f = open(person + "_tweet_graph.json", 'r')
    graph = json.loads(f.read())
    f.close()
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

def removeLinks(sentence):
    #since I was too lazy to remove the links when constructing the graph *shrug*
    sentence = re.sub(r"http\S+", "", sentence)
    return sentence

def batchGenerateTweets(numTweets, person):
    random_tweets = []
    graph = getGraph(person)
    for i in range(numTweets):
        try:
            beginning = pickBeginning(graph)
            sentence = removeLinks(constructSentence(beginning, graph))
            if(sentence):
                random_tweets.append(sentence.encode('utf-8'))
        except Exception:
            pass
    f = open(person + '_random_tweets.txt', 'w')
    for i in random_tweets:
        f.write("%s\n" % i)
    f.close()

def makeJson(graph, person):
    graph = json.dumps(graph)
    graph_json = open(person + '_tweet_graph.json', 'w')
    graph_json.write(graph)

if __name__ == '__main__':
    person = 'nucle0tides'
    # getAllTweets(person)
    # graph = makeNodes(person)
    # graph = createEdges(graph, person)
    # makeJson(graph, person)
    batchGenerateTweets(1000, person)
