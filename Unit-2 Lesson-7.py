import math

# Print the header
print(f"{'N':>3}|{'SQR':>5}|{'Cubes':>7}|{'Roots':>5}")
print("-" * 20)

# Loop through values of N from 10 to 200, in steps of 15
for N in range(10, 201, 15):
    SQR = N ** 2
    Cubes = N ** 3
    Roots = round(math.sqrt(N), 2)
    
    # Print each row with proper formatting
    print(f"{N:>3}|{SQR:>5}|{Cubes:>7}|{Roots:>5.2f}")
