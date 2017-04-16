# NGramCounter builds a dictionary relating ngrams (as tuples) to the number
# of times that ngram occurs in a text (as integers)
class NGramCounter(object):

  # parameter n is the 'order' (length) of the desired n-gram
  def __init__(self, n):
    self.n = n
    self.ngrams = dict()
    self.beginnings = []

  # feed method calls tokenize to break the given string up into units
  def tokenize(self, text):
    return text.split("-")

  # feed method takes text, tokenizes it, and visits every group of n tokens
  # in turn, adding the group to self.ngrams or incrementing count in same
  # def feed(self, text):

  #   tokens = self.tokenize(text)

  #   # e.g., for a list of length 10, and n of 4, 10 - 4 + 1 = 7;
  #   # tokens[7:11] will give last three elements of list
  #   for i in range(len(tokens) - self.n + 1):
  #     gram = tuple(tokens[i:i+self.n])
  #     if gram in self.ngrams:
  #       self.ngrams[gram] += 1
  #     else:
  #       self.ngrams[gram] = 1

  def get_ngrams(self):
    return self.ngrams

  def feed(self, text):

    tokens = self.tokenize(text)

    # discard this line if it's too short
    if len(tokens) < self.n:
      return

    # store the first ngram of this line
    beginning = tuple(tokens[:self.n])
    self.beginnings.append(beginning)

    for i in range(len(tokens) - self.n):

      gram = tuple(tokens[i:i+self.n])
      next = tokens[i+self.n] # get the element after the gram

      # if we've already seen this ngram, append; otherwise, set the
      # value for this key as a new list
      if gram in self.ngrams:
        self.ngrams[gram].append(next)
      else:
        self.ngrams[gram] = [next]

  # generate a text from the information in self.ngrams
  def generate(self, num):

    from random import choice

    # get a random line beginning; convert to a list. 
    current = choice(self.beginnings)
    output = list(current)
    output_str = ""
    for i in range(num):
      if current in self.ngrams:
        possible_next = self.ngrams[current]
        next = choice(possible_next)
        output.append(next)
        # get the last N entries of the output; we'll use this to look up
        # an ngram in the next iteration of the loop
        current = tuple(output[-self.n:])
      else:
        break

    # output_str = output_str + output
    return output

#if __name__ == '__main__':
# create an NGramCounter object and feed data to it
ngram_counter = NGramCounter(2)
fileDir = open("/Users/aleesha/Documents/FIT/semester 2/AI/Assignment/nGramProject/corpus.txt")
for line in fileDir:
  line = line.strip()
  ngram_counter.feed(line)

# get ngrams from ngram counter; iterate over keys, printing out keys with
# a count greater than one
output = "<html><body><table>"
ngrams = ngram_counter.get_ngrams()
for ngram in ngrams.keys():
  count = ngrams[ngram]
  if count > 1:
    output += "<tr><td>%s</td><td>%s</td></tr>" % (ngram, str(count))
    print (' '.join(ngram) + ": " + str(count))
output += "</table></body></html>"

f = open('/Users/aleesha/Documents/FIT/semester 2/AI/Assignment/nGramProject/output/output.html', 'w')
f.write(output)
f.close()
# print(output)
# print("Generate Text: ")
# print(ngram_counter.generate(10))