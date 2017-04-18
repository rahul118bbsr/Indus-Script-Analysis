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
print("Count: ", count)
for x in sorted_x:
    print(x, "\t", x[0], "\t\tConditional Probability: \t", x[1]/count)