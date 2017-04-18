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
f = open('/Users/aleesha/Documents/FIT/semester 2/AI/Assignment/nGramProject/output/ender_frequency.txt', 'w')

#print(sorted_x)
f.write("Header Symbol" + "\t\t\t" + "Frequency\n")
f.write("-----------------------------\n")
for x in sorted_x:
  f.write(str(x[0]) + "\t\t\t" + str(x[1]) + "\n")

f.close()