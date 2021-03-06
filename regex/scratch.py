"""Just a scratch file to work with regex"""

# pylint: disable=invalid-name, anomalous-backslash-in-string

import re

x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)  # => ['From: Using the :']

a = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
b = re.findall('\S+?@\S+', a)
print(b)  # => ['stephen.marquard@uct.ac.za']
