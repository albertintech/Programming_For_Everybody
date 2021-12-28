"""This program can be used to generate a word frequency list from a given text file source."""

fname = input("Enter file name: ")
fh = open(fname, encoding='UTF-8')

counts = dict()
for line in fh:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
tmp = list()
for k, v in counts.items():
    tmp.append((v, k))
# print(tmp)
tmp = sorted(tmp, reverse=True)
print(tmp)
print("Word\t\tCount")
for k, v in tmp[:10]:
    print(f"{v}:\t\t{k}")
