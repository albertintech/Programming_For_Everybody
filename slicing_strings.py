# pylint: disable=invalid-name, missing-docstring

# s = "Monty Python"
# print(s[:5])
# print(s[6:])
# print(s[-6:])
# print(s[::-1])
# print()

text = "X-DSPAM-Confidence:    0.8475"
col_pos = text.find(":")
raw_number = text[col_pos + 1:]
number_str = raw_number.strip()
print(number_str)
print(type(number_str))
print()
number = float(number_str)
print(number)
print(type(number))
