import random

def shuffle(A):
    for i in range(len(A)):
        j = random.randint(0, len(A) - 1)
        A[i], A[j] = A[j], A[i]
    return A

size = 6
B = list(range(1, size + 1))  # Creates [1, 2, 3, 4, 5, 6]
print("Original array:", B)
print("Shuffled array:", shuffle(B))
