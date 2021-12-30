# Python Regular Expression Quick Guide

# must use "import re"

# ^        Matches the beginning of a line
# $        Matches the end of the line
# .        Matches any character
# \s       Matches whitespace
# \S       Matches any non-whitespace character
# *        Repeats a character zero or more times
# *?       Repeats a character zero or more times (non-greedy)
# +        Repeats a character one or more times
# +?       Repeats a character one or more times (non-greedy)
# [aeiou]  Matches a single character in the listed set
# [^ XYZ]  Matches a single character not in the listed set
# [a-z0-9] The set of characters can include a range
# (        Indicates where string extraction is to start
#  )       Indicates where string extraction is to end

import re

x = 'My favorite 2 numbers are 9 and 42'
y = re.findall('[0-9]', x)
print(y)
# => ['2', '9', '4', '2']
z = re.findall('[0-4][0-3]', x)
print(z)
# => ['42']
