import operator

def ngrams(fileDir, n):
  output = {}
  for line in fileDir:
    ender = line.strip().split('-')[-1]
    output.setdefault(ender, 0)
    output[ender] += 1
  return output

fileDir = open("/Users/aleesha/Documents/FIT/semester 2/AI/Assignment/nGramProject/corpus.txt")
output = ngrams(fileDir, 1)

sorted_x = sorted(output.items(), key=operator.itemgetter(1), reverse=True)
#print(sorted_x)
for x in sorted_x:
  print(x)