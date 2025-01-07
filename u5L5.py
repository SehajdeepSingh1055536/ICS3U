def getNum(prompt):
    """
    This function prompts the user to enter a positive integer.
    It will keep asking until a valid positive integer is provided.
    """
    while True:
        try:
            num = int(input(prompt))
            if num > 0:
                return num
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def fib(n):
    """
    Recursive function to compute the nth Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# Main Program
print("Program for printing the Fibonacci sequence!")
num_terms = getNum("Please input a whole number: ")

# Generate and print Fibonacci sequence
sequence = []
for i in range(1, num_terms + 1):
    sequence.append(fib(i))

print(" ".join(map(str, sequence)))
