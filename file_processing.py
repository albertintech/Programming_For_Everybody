"""Notes taken while watching the File Processing lecture. This file is not meant to be run!"""

# pylint: disable=invalid-name

# pattern
xfile = open('mbox.text')
for i in xfile:
    print(i)

# counting
fhand = open('mbox.text')
count = 0
for line in fhand:
    count += 1
print("Line count:", count)

# $ python open.py
# >>> Line Count: 132045

# reading a whole file and put into a single string
fhand = open('mbox.text')
inp = fhand.read()
print(len(inp))  # >>> 94626

file_name = input("Enter the file name: ")
try:
    fhand = open(file_name)
except:
    print("File cannot be opened:", file_name)
    quit()
count = 0
for line in fhand:
    if line.startswith("Subject:"):
        count += 1
print("There were", count, "subject lines in", file_name)
