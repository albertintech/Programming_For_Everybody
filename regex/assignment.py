"""Assignment for 'Using Python to Access Web Data'"""
# pylint: disable=unspecified-encoding
import re

# handle = open('42.txt')
fname = input("Enter file name: ")
handle = open(fname, encoding='UTF-8')

for line in handle:
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    if len(x) > 0:
        print(x)
