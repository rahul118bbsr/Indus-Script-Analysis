import operator

def conditionalProbability(fileDir, given):
    output = {}
    given = given.strip().split("-")
    for line in fileDir:
        line = line.strip().split('-')
        for i in range (len(line)):
            startIndex = i
            stopIndex = i + len(given)
            if(stopIndex <= len(line) and line[startIndex : stopIndex] == given and startIndex - 1 >= 0):
                previousWord = line[startIndex - 1]
                output.setdefault(previousWord, 0)
                output[previousWord] += 1
    return output

fileDir = open("/Users/aleesha/Documents/FIT/semester 2/AI/Assignment/nGramProject/corpus.txt")
output = conditionalProbability(fileDir, input("Enter the condition: "))
sorted_x = sorted(output.items(), key=operator.itemgetter(1), reverse=True)
#print(sorted_x)
for x in sorted_x:
    print(x, "Conditional Probability: ", x[1]/636)