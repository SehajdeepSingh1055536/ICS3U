import math

# Input validation for x
x = int(input("Please input a whole number between 1 and 20: "))
if x < 1 or x > 20:
    print("x is outside of range. cannot continue.")
else:
    # Input validation for y
    y = int(input("please input another whole number between 1 and 20: "))
    if y < 1 or y > 20:
        print("y is outside of range. connot continue.")
    elif y != 0:
        # Check if y is factor of x
        rem = x % y
        if rem == 0:
            print("Yes!", y, "is afactor of" ,x)
        else:
            print("No!", y, "is not a factor of", x)
    else:
        # Handle division by zero case
        print("Error: You cannot divide by zero!")
