import operator

def conditionalProbability(fileDir, given):
    output = {}
    given = given.strip().split("-")
    for line in fileDir:
        line = line.strip().split('-')
        for i in range (len(line)):
            startIndex = i
            stopIndex = i + len(given)
            if(stopIndex < len(line) and line[startIndex : stopIndex] == given):
                nextWord = line[stopIndex]
                output.setdefault(nextWord, 0)
                output[nextWord] += 1
    return output

fileDir = open("/Users/aleesha/Documents/FIT/semester 2/AI/Assignment/nGramProject/corpus.txt")
condition = input("Enter the condition: ")
output = conditionalProbability(fileDir, condition)
sorted_x = sorted(output.items(), key=operator.itemgetter(1), reverse=True)

count = 0;
fileDir = open("/Users/aleesha/Documents/FIT/semester 2/AI/Assignment/nGramProject/corpus.txt")
for line in fileDir:
    line = line.strip().split('-')
    if condition in line:
        count += 1
#print(sorted_x)
for x in sorted_x:
    print(x, "Conditional Probability: \t", x[1]/count)