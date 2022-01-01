import re

# handle = open('mbox-short.txt')
# for line in handle:
#     line = line.rstrip()
#     if re.search('^From:.+@', line):
#         print(line)


handle = open('mbox-short.txt')
for line in handle:
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
    if len(x) > 0:
        print(x)
