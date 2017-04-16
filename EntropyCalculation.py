import math

def entropy(stringlength, output, base = 2.0):
    H = 0.0
    for key in output:
        probability = output[key] / stringlength
        H -= probability * math.log2(probability)
    return H

# Counts frequency as per given n
def ngrams(fileDir, n):
    output = {}
    for line in fileDir:
        line = line.strip().split('-')
        for i in range(len(line)-n+1):
            g = ' '.join(line[i:i+n])
            output.setdefault(g, 0)
            output[g] += 1
    return output

fileDir = open("/Users/aleesha/Documents/FIT/semester 2/AI/Assignment/nGramProject/corpus.txt")
output = ngrams(fileDir, 1)
fileDir = open("/Users/aleesha/Documents/FIT/semester 2/AI/Assignment/nGramProject/corpus.txt")
textLength = 0
for line in fileDir:
    line = line.strip().split('-')
    textLength += len(line)
    
print(entropy(textLength, output))