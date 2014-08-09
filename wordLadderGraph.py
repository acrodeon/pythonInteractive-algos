##################################################################################
#                         Word Ladder Graph                                      #
# huge number of buckets, each of them with a four-letter word on the outside,   #
# except that one of the letters in the label has been replaced by an underscore #               
##################################################################################

from graph import Graph

def buildGraph(wordFileName):
    """creating a vertex for each word in the graph and edges between all the vertices we find for words found under the same key in the dictionary"""
    d = {}
    g = Graph()
    wfile = open(wordFileName,'r')
    # create buckets of words that differ by one letter
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1,word2)
    wfile.close()
    return g
