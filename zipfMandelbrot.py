import re
from operator import itemgetter
import matplotlib.pyplot as plt
from scipy import special
import numpy as np

#Get our corpus of medical words
frequency = {}
def frequencyCount(fileDir, n):
  output = {}
  for line in fileDir:
    line = line.strip().split('-')
    for i in range(len(line)-n+1):
      g = ' '.join(line[i:i+n])
      frequency.setdefault(g, 0)
      frequency[g] += 1

#build dict of words based on frequency

fileDir = open("/Users/aleesha/Documents/FIT/semester 2/AI/Assignment/nGramProject/corpus.txt")
frequencyCount(fileDir, 1)

#limit words to 1000
# n = 1000
# frequency = {key:value for key,value in frequency.items()[0:n]}

#convert value of frequency to numpy array
myList = []
# s = frequency.values()
for value in frequency.values():
    myList.append(value)
s = np.array(myList)

#Calculate zipf and plot the data
# a = 2. #  distribution parameter
# count, bins, ignored = plt.hist(s[s<50], 50, normed=True)
# x = np.arange(1., 50.)
# y = x**(-a) / special.zetac(a)
# plt.plot(x, y/max(y), linewidth=2, color='r')
# plt.show()


a = 2. # parameter
s = np.random.zipf(a, 1000)
#Truncate s values at 50 so plot is interesting
count, bins, ignored = plt.hist(s[s<50], 50, normed=True)
x = np.arange(1., 50.)
y = x**(-a)/special.zetac(a)
plt.plot(x, y/max(y), linewidth=2, color='r')
plt.show()