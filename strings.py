# pylint: disable=invalid-name, missing-docstring

# letter = fruit[1]
# print(letter)

# x = 3
# w = fruit[x - 1]
# print(w)

# print(len(fruit))

# using an indefinite loop
fruit = "banana"
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index += 1
print()

# using a definite loop
fruit = "banana"
index = 0
for letter in fruit:
    print(index, letter)
    index += 1
