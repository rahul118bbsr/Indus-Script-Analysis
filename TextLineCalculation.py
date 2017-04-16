import operator

def calculateTextLength(fileDir):
    output = {}
    for line in fileDir:
        textLength = len(line.strip().split('-'))
        output.setdefault(textLength, 0)
        output[textLength] += 1
    return output
    
fileDir = open("/Users/aleesha/Documents/FIT/semester 2/AI/Assignment/nGramProject/corpus.txt")
output = calculateTextLength(fileDir)
sorted_x = sorted(output.items(), key=operator.itemgetter(1), reverse=True)
#print(sorted_x)
for x in sorted_x:
    print(x)