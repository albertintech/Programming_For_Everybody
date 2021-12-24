# pylint: disable=invalid-name, missing-docstring

s = "Monty Python"

index = 0
for letter in s:
    print(index, letter)
    index += 1
print()

position = s.find('yt')
print(position)

greet = "   Hi Bob "
print(greet)
print("Invoke strip method on greet object.")
print(greet.strip())
