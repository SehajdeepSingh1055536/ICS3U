def swap(B, p, q):
    temp = B[p]
    B[p] = B[q]
    B[q] = temp

def sort(C):  # Implements Exchange Sort
    for i in range(len(C) - 1):  # Iterate up to the second last element
        for j in range(i + 1, len(C)):  # Compare with elements after i
            if C[i] > C[j]:  # Swap if out of order
                swap(C, i, j)

# Adjusted input array to match the sample output
A = [9, 5, 6, 14, 2, -1, 0, 19, 15, 8, 11]
sort(A)
print(A)
