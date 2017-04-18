import operator

def ngrams(fileDir, header, n):
  output = {}
  for line in fileDir:
    line = line.strip().split('-')
    if(line[0] == header):
        nFollowingSymbols = tuple(line[1 : 1 + n ])
        output.setdefault(nFollowingSymbols, 0)
        output[nFollowingSymbols] += 1
  return output
  
fileDir = open("/Users/aleesha/Documents/FIT/semester 2/AI/Assignment/nGramProject/corpus.txt")
output = ngrams(fileDir, input("Enter the header symbol: "), 3)
sorted_x = sorted(output.items(), key=operator.itemgetter(1), reverse=True)
#print(sorted_x)
for x in sorted_x:
    print(x)