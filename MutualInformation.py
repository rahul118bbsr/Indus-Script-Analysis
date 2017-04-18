import math
import itertools

def entropyPart(p):
    if not p:
        return 0

    return -p * math.log(p)

def entropy(X, Y):
    pairs = zip(X, Y)
    lengthOfEachPair = 2
    probs = []
    for pair in itertools.product(X,Y):
        probs.append(1.0 * sum([p == pair for p in pairs]) / lengthOfEachPair)

    return sum([entropyPart(p) for p in probs])

def ngrams(fileDir, n):
    output = {}
    for line in fileDir:
        line = line.strip().split('-')
        for i in range(len(line)-n+1):
            g = ' '.join(line[i:i+n])
            output.setdefault(g, 0)
            output[g] += 1
    return output.values()

fileDir = open("/Users/aleesha/Documents/FIT/semester 2/AI/Assignment/nGramProject/corpus.txt")
X = ngrams(fileDir, 1)
fileDir = open("/Users/aleesha/Documents/FIT/semester 2/AI/Assignment/nGramProject/corpus.txt")
Y = ngrams(fileDir, 2)
print(entropy(X, Y))