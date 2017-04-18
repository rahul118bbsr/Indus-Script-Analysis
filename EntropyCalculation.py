import math

def entropy(stringlength, output, base = 2.0):
    H = 0.0
    for key in output:
        probability = output[key] / stringlength
        H -= probability * math.log2(probability)
    return H

# Counts frequency as per given n
def ngrams(fileDir, n, count = 0):
    output = {}
    for line in fileDir:
        line = line.strip().split('-')
        for i in range(len(line)-n+1):
            g = ' '.join(line[i:i+n])
            output.setdefault(g, 0)
            count += 1
            output[g] += 1
    print("Count for ", n , " gram: ", count)
    return entropy(count, output)

def calculateEntropy(fileDir, n):
    return ngrams(fileDir, n)

fileDir = open("/Users/aleesha/Documents/FIT/semester 2/AI/Assignment/nGramProject/corpus.txt")
print(calculateEntropy(fileDir, 1))
fileDir = open("/Users/aleesha/Documents/FIT/semester 2/AI/Assignment/nGramProject/corpus.txt")
print(calculateEntropy(fileDir, 2))
fileDir = open("/Users/aleesha/Documents/FIT/semester 2/AI/Assignment/nGramProject/corpus.txt")
print(calculateEntropy(fileDir, 3))
fileDir = open("/Users/aleesha/Documents/FIT/semester 2/AI/Assignment/nGramProject/corpus.txt")
print(calculateEntropy(fileDir, 4))

# Calculate Mutual Information:
# uniGramEntropy