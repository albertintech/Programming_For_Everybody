"""Assignment for 'Using Python to Access Web Data'"""
# pylint: disable=unspecified-encoding
import re

handle = open('42.txt', encoding='UTF-8')

x = list()

for line in handle:
    line = line.rstrip()
    x = int(re.findall('[0-9]+', line))
    if len(x) > 0:
        print(x)
