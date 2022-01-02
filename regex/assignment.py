
"""Assignment: Finding Numbers in a Haystack"""

# pylint: disable=unspecified-encoding

# input: string type
# output: integer type
# requirements: find every number and their sum total
# Algo:
# open file
# Find integers
# Convert string ints to interger type
# Add all ints and find sum

import re
handle = open('97.txt', encoding='UTF-8')
lst = list()
for line in handle:
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    if len(x) > 0:
        lst += x
int_lst = list()
int_lst = [int(i) for i in lst]
print(sum(int_lst))
