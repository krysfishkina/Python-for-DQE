# 1. create a list of random number of dicts (from 2 to 10)

import random  # library for generating counts and size of dictionaries
import string  # library for generating keys of dictionaries

list_of_dicts = []
random_dict = {}
new_dict = {}

for i in range(random.randint(2, 10)):  # loop for random count of dictionaries
    for j in range(random.randint(1, 20)):  # loop for random count of key:value inside each dictionary
        random_dict[random.choice(string.ascii_lowercase)] = random.randint(0, 100)  # random key and value
    new_dict = random_dict.copy()
    list_of_dicts.append(new_dict)
    random_dict.clear()

print("""The list of random number of dicts (from 2 to 10) where numbers of keys is letter: 
""", list_of_dicts)

# 2. get previously generated list of dicts and create one common dict

final_dict = {}  # variable for final dictionary
common_dict = {}  # variable for dictionary without renaming
key_entry = {}  # variable for saving entries for each key

for index, each_dict in enumerate(list_of_dicts):  # read each dictionary
    for key in each_dict.keys():  # read the keys of each dictionary
        if key not in common_dict:  # check key existing
            common_dict[key] = each_dict[key]
            key_entry[key] = 1
        elif common_dict[key] < each_dict[key]:
            key_entry[key] = index + 1
            common_dict[key] = each_dict[key]

print("""The dict with max values:
""", common_dict)
for i in common_dict:  # a loop to change keys that appeared more than 1 time:
    if key_entry.get(i) > 1:
        final_dict[str(i) + '_' + str(key_entry.get(i))] = common_dict.get(i)
    else:
        final_dict[i] = common_dict.get(i)
print("""The final dict:
""", final_dict)
