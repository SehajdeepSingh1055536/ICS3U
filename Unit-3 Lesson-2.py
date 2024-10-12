items = ["Apples", "Bananas", "Cherries", "Dosa"]
print(items) # Predict A - Does this really print anything?
# Prediction A- This code just print the names of the items.

print("The number of items is %d." % len(items)) # Predict B
# Prediction B- This code print how many items are there.

for i in items: # Predict C
    print(i)
# Prediction C- This code print the items in line.

for c in range(len(items)): # Prediction D
    print(c, items[c])
# Prediction D- This code print the items in line with numbers of items.


# Modify
# Initialize an empty list to store items
items = []

# Ask the user how many items they want to input
num_items = int(input("How many items are you entering?"))

# Prompt the user to enter each item
print("Enter your items now:")
for i in range(num_items):
    item = input(f"Next item: ")
    items.append(item)

# Output the size of the list and the items entered
print(f"\nYou have entered {len(items)} items.")
for item in items:
    print(item)
