# This is the code block for creation and comparison of the two type dicitonaries

import csv
deck = []
journal = {}
dupe = {}

# Iterating through the list of creatures to find duplicate types
for creature in deck:
    for type in creature:
        if type not in journal:
            journal[type] = creature
        else:
            if type not in dupe:
                dupe[type] = []
            dupe[type].append(journal[type])
            journal[type] = creature

# Appending final creatures (if any) to dupe, then output as csv
if len(dupe) == 0:
    print("Congrats, you are a true Volo master with no duplicates!")
else:
    for type in dupe:
        dupe[type].append(journal[type])
    with open('types_with_duplicates.csv', 'w', newline = '') as f:
        writer = csv.writer(f)
        writer.writerow(dupe.keys())
        for type in range(len(dupe.keys())):
            writer.writerow([val[type] for val in dupe.values()])