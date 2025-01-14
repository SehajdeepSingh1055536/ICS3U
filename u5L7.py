fib_sequence = []


def fib(n):
    # Base case: n = 1
    if n == 1:
        fib_sequence.append(1)
        return fib_sequence
    
    # Base case: n = 2
    elif n == 2:
        fib(1)  # Ensure the first base case has run
        fib_sequence.append(1)
        return fib_sequence
    
    # Recursive case: n > 2
    else:
        fib(n - 1)  # Build up the sequence to n - 1
        
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

# Generate the first 45 terms of the Fibonacci sequence
fib(45)

# Print the resulting array
print(fib_sequence)
