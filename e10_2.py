"""
10.2
Write a program to read through the mbox-short.txt.
Isolate the following line types:
"From stephen.marquard@uct.ac.za Sat Jan  5 09: 14: 16 2008"
Then, figure out the distribution of emails by hour of the day.
Print out the counts, sorted by ascending hour as shown below.

Desired Output
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
"""

fname = input("Enter file name: ")
fh = open(fname, encoding='UTF-8')

times = list()
hours = list()
hour = list()
counts = dict()

for line in fh:
    if line.startswith("From ") and not line.startswith("From:"):
        lst = line.split()
        times.append(lst[5])
# print(times)  # the list of each hh:mm:ss
for time in times:
    hours = time.split(":")
    hour.append(hours[0])
# print(hour)  # the list of each hh
for number in hour:
    counts[number] = counts.get(number, 0) + 1
# print(counts)
tmp = list()
for k, v in counts.items():
    tmp.append((k, v))
# print(tmp)
tmp = sorted(tmp)
# print(tmp)
for k, v in tmp:
    print(f"{k} {v}")
