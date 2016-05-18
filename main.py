from getTweets import *
from generateTweet import *
import os.path

def do(person):
    if os.path.isfile('static/tweets/' + person + '_tweet_graph.json'):
        sentence = createOneTweet(person)
        while len(sentence) < 1:
            sentence = createOneTweet(person)
        return sentence
    else:
        try:
            getAllTweets(person)
        except Exception as e:
            return "Sorry, that user does not exist!"
        graph = makeNodes(person)
        graph = createEdges(graph, person)
        makeJson(graph, person)
        sentence = createOneTweet(person)
        while len(sentence) < 1:
            sentence = createOneTweet(person)
        return sentence

def doPic(person): 
    return getTwitterPicture(person)