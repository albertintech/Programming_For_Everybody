# for i in [5, 4, 3, 2, 1]:
#     print(i)
# print("Blastoff!")

# friends = ['Batman', 'Catwoman', 'Batgirl']
# for i in friends:
#     print("Hi " + i)

num_list = [3, 41, 12, 9, 74, 15]
largest_num = -1
for i in num_list:
    if i > largest_num:
        largest_num = i
    print(f"The largest number so far is {largest_num}")
print(f"{largest_num} is the largest number in the list.")

num_list = [1003, 99, 12, 9, 2, 1, -42]
smallest_num = max(num_list) + 1
for i in num_list:
    if i < smallest_num:
        smallest_num = i
    print(f"The smallest number so far is {smallest_num}")
print(f"{smallest_num} is the smallest number in the list.")

num_list = [1003, 99, 12, 9, 2, 1, -42]
smallest_num = None
for i in num_list:
    if smallest_num is None:
        smallest_num = i
    elif i < smallest_num:
        smallest_num = i
    print(f"The smallest number so far is {smallest_num}")
print(f"{smallest_num} is the smallest number in the list.")
