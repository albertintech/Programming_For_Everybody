# pylint: disable=invalid-name, missing-docstring, line-too-long, unspecified-encoding

# 8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method.
# The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list.
# When the program completes, sort and print the resulting words in alphabetical order.

fname = input("Enter file name: ")
fh = open(fname)

lst = list()
no_dups = list()
for line in fh:
    lst += line.split()
no_dups = list(dict.fromkeys(lst))
no_dups.sort()
print(no_dups)

# lst = list()
# no_dups = list()
# count = 0
# for line in fh:
#     lst += line.split()
#     for word in lst:
#         if word != lst[count]:
#             no_dups.append(word)
#             count += 1
# no_dups.sort()
# print(no_dups)
