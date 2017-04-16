import operator

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
output = ngrams(fileDir, 2)

sorted_x = sorted(output.items(), key=operator.itemgetter(1), reverse=True)
f = open('/Users/aleesha/Documents/FIT/semester 2/AI/Assignment/nGramProject/output/frequency_trigram.txt', 'w')

#print(sorted_x)
f.write("Symbol" + "\t\t\t" + "Frequency\n")
f.write("-----------------------------\n")
for x in sorted_x:
  f.write(str(x[0]) + "\t\t\t" + str(x[1]) + "\n")

f.close()
