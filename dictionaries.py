# pylint: disable=invalid-name, missing-docstring, line-too-long, unspecified-encoding

# purse = dict()
# purse['money'] = 40.00
# purse['candies'] = 4
# purse['earphones'] = 1
# print(purse)

# The Histogram Problem
# ccc = dict()
# ccc['csev'] = 1
# ccc['cwen'] = 1
# print(ccc)
# ccc['cwen'] += 1
# print(ccc)
# print('smith' in ccc)

counts = dict()
names = ['smith', 'jones', 'garcia', 'miller', 'shoemaker', 'smith', 'miller']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)

# Using the get method
hero_counts = dict()
hero_list = ['Batman', 'Superman', 'Spiderman',
             'Batman', 'Batman', 'Batgirl', 'Superman']
for alias in hero_list:
    hero_counts[alias] = hero_counts.get(alias, 0) + 1
print(hero_counts)
# Definite Loop to print each key with its value
for i in hero_counts:
    print(i, hero_counts[i])
# Print just keys
print(hero_counts.keys())
# Print just values
print(hero_counts.values())
# Print each key-value pair using two iteration variables at once
for k, v in hero_counts.items():
    print(k, v)
