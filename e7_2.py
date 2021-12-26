# pylint: disable=invalid-name, missing-docstring
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname, encoding="utf-8")
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count += 1
    col_pos = line.find(":")
    raw_number = line[col_pos + 1:]
    number_str = raw_number.strip()
    number = float(number_str)
    total += number
avg = total / count
print('Average spam confidence:', avg)
