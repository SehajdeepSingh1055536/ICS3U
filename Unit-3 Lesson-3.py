items = ["Apples", "Bananas", "Cherries", "Dosa"]
sizes = []
for i in range(len(items)): # Predict A: State the purpose,
                            # data types, and any output
    sizeI = len(items[i])
    sizes.append(sizeI)

for i in range(len(sizes)): # Predict B: State the output
    print("%d %s" % (sizes[i], items[i]))

#prediction A- The first loop calculates the length of each string in the items list.
# data types - items is a list of strings(str).
# purpose - This part of the code is meant to determine the lengthof each string in the items list and store the length in sizes.

# prediction B- The second loop print the sizes (length) of each items along with the corresponding item name.

# Modify

items = ["Apples", "Bananas", "Cherries", "Dosa"]
sizes = []

# Loop to calculate the length of each item and store in sizes list
for i in range(len(items)):
    sizeI = len(items[i])
    sizes.append(sizeI)

# Loop to print the size and corresponding item
for i in range(len(sizes)):
    print("%d %s" % (sizes[i], items[i]))

# New loop to check if sizes[i] matches the length of items[i] and print True/False
for i in range(len(items)):
    print(sizes[i] == len(items[i]))
