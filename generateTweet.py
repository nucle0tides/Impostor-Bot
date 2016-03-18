import json
import random
import re
#who knows if this is a good way to do this. I sure don't know.
def makeNodes(person):
    node_dict = {}
    f = open('static/tweets/' + person + '_tweets.txt', 'r')
    for lines in f:
        for word in lines.split(' '):
            node_dict[word.lower()] = []
    f.close()
    return node_dict

def createEdges(graph, person):
    f = open('static/tweets/' + person + '_tweets.txt', 'r')
    current_word = ''
    next_word = ''
    for lines in f:
        line = lines.split()
        for i in range(len(line)):
            current_word = line[i]
            if(i < len(line) - 1):
                next_word = line[i + 1]
                graph[current_word.lower()].append(next_word.lower())
    f.close()
    return graph

def getGraph(person):
    f = open('static/tweets/' + person + "_tweet_graph.json", 'r')
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

def makeJson(graph, person):
    graph = json.dumps(graph)
    graph_json = open('static/tweets/' + person + '_tweet_graph.json', 'w')
    graph_json.write(graph)

def getGraph(person):
    f = open('static/tweets/' + person + "_tweet_graph.json", 'r')
    graph = json.loads(f.read())
    f.close()
    return graph

def createOneTweet(person):
    graph = getGraph(person)
    sentence = ''
    try:
        while len(sentence) < 2:
            beginning = pickBeginning(graph)
            sentence = removeLinks(constructSentence(beginning, graph))
    except Exception as excep:
        print type(excep)#good one
        print excep
    return sentence.encode('utf-8')[:140]
