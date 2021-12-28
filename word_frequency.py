"""This program can be used to generate a word frequency list from a given text file source."""

fname = input("Enter file name: ")
fh = open(fname, encoding='UTF-8')

counts = dict()
for line in fh:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
for k, v in counts.items():
    print(k + ":", v)
