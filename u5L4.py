
import math


def swap(B, p, q):
    temp = B[p]
    B[p] = B[q]
    B[q] = temp


def iSort(A):
    for i in range(1, len(A)):
        for j in range(i - 1, -1, -1):
            if A[j + 1] < A[j]:
                swap(A, j + 1, j)
            else:
                break


def trim(w):
    return w.strip() 

# Function to print the sorted array with 10 words per line
def printIt(A):
    for i in range(0, len(A), 10):
        print(" ".join(A[i:i+10]))

# Main execution flow
try:
    # Open the file
    with open("words40.dat", "r") as file:
        words = []

        # Read each word, trim it, and add it to the list
        for line in file:
            words.append(trim(line))

    # Sort the words alphabetically
    iSort(words)

    # Print the sorted words
    printIt(words)

except FileNotFoundError:
    print("Error: The file 'words40.dat' was not found. Please make sure it exists in the same directory as this script.")
except Exception as e:
    print(f"An error occurred: {e}")
