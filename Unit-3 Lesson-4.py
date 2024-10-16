import math

ar2 = [[3, 4, 1, 2, 6],
      [9, 2, 3, 7, 5],
      [4, 2, 1, 0, 3]]
for i in range(len(ar2)):
  ar3 = ar2[i]
  for j in range(len(ar3)):
      print(ar3[j], end=" ")
  print() # PREDICT A

print(ar2) # PREDICT B  


# Prediction A:

34126
92375
42103

# Prediction B:
[[3, 4, 1, 2, 6], [9, 2, 3, 7, 5], [4, 2, 1, 0, 3]]

# Modify


arr2 = [[3, 4, 1, 2, 6],
        [9, 2, 3, 7, 5],
        [4, 2, 1, 0, 3]]

sums = []

for i in range(len(arr2)):
    row_sum = sum(arr2[i])
    sums.append(row_sum)

print(sums)
