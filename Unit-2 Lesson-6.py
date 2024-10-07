import math
# 1
S = "--8<--"
print(S*10)

# 2
# Example 1: range(lo, hi, step)
for i in range(0, 5, 1):
    print(i)  # Output: 0, 1, 2, 3, 4

# Example 2: range(x)
for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4

# Example 3: range(x, y)
for i in range(1, 5):
    print(i)  # Output: 1, 2, 3, 4

# Example 4: range(1, 5)
for i in range(1, 5):
    print(i)  # Output: 1, 2, 3, 4

# Example 5: range(x, y, s) with positive step
for i in range(1, 10, 2):
    print(i)  # Output: 1, 3, 5, 7, 9

# Example 6: range(x, y, s) with large step
for i in range(1, 100, 23):
    print(i)  # Output: 1, 24, 47, 70, 93

# Example 7: range(5, 101, 23)
for i in range(5, 101, 23):
    print(i)  # Output: 5, 28, 51, 74, 97

# Example 8: range(10, 1, -1)
for i in range(10, 1, -1):
    print(i)  # Output: 10, 9, 8, 7, 6, 5, 4, 3, 2

# Example 9: range(10, 1, -2)
for i in range(10, 1, -2):
    print(i)  # Output: 10, 8, 6, 4, 2


   
# 3    
rows = 5

# Create the top half (increasing pattern)
for i in range(1, rows + 1):
    spaces = ' ' * (rows - i)
    hashes = '#' * (2 * i - 1)
    print(spaces + hashes)


# 4
# Number of rows for the top pyramid part
rows = 5

# Create the top half (increasing pattern)
for i in range(1, rows + 1):
    spaces = ' ' * (rows - i)
    hashes = '#' * (2 * i - 1)
    print(spaces + hashes)

# Create the bottom half (decreasing pattern)
for i in range(rows - 1, 0, -1):
    spaces = ' ' * (rows - i)
    hashes = '#' * (2 * i - 1)
    print(spaces + hashes)

# 5 
S = "#"
for i in range(10,0,-1):
    print(S * i)
