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

