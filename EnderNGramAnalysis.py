import operator

def ngrams(fileDir, ender, n):
  output = {}
  for line in fileDir:
    line = line.strip().split('-')
    if(line[-1] == ender):
        nFollowingSymbols = tuple(line[-1 - n : -1])
        output.setdefault(nFollowingSymbols, 0)
        output[nFollowingSymbols] += 1
  return output
  
fileDir = open("/Users/aleesha/Documents/FIT/semester 2/AI/Assignment/nGramProject/corpus.txt")
output = ngrams(fileDir, input("Enter the ender symbol: "), 2)
sorted_x = sorted(output.items(), key=operator.itemgetter(1), reverse=True)
#print(sorted_x)
for x in sorted_x:
    print(x)