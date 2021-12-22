a_str = 'Hi Bob'
print(f"Initial string value is: {a_str}")

try:
    new_int = int(a_str)
    print("It worked on the try block.")
except:
    new_int = -1
    print("Try block didn't work. Executed except block instead.")

print('Value of new_int:', new_int)

# Let's try again
a_str = '123'
print(f"Initial string value is: {a_str}")

try:
    new_int = int(a_str)
    print("It worked on the try block.")
except:
    new_int = -1
    print("Try block didn't work. Executed except block instead.")

print('Value of new_int:', new_int)
