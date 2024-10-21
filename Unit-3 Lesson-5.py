def add(a, b):
  return a + b

print(add(7, 2))
# prediction - by adding the "7" and "2" the output would be 9. By replacing the the "7" and "2" with strings of any value the function will still work. But we mix data types the code will be crash.

# modify 1 
def add(a, b):
    return a + b

# Getting user input
input1 = input("Enter the first number: ")
input2 = input("Enter the second number: ")

# Checking if both inputs are numerical
try:
    # Try to convert inputs to float
    num1 = float(input1)
    num2 = float(input2)
    
    # Calling the function and multiplying the result by 2
    result = add(num1, num2) * 2
    print("The result is:", result)
    
except ValueError:
    # If conversion fails, inform the user
    print("Please enter valid numerical values (int or float).")
    
#modify - 2 

def add(a, b):
    return a + b

def myPow(m, n):
    return m ** n  # Raising m to the power of n

# Getting user input
input1 = input("Enter the first number (base): ")
input2 = input("Enter the second number (exponent): ")

# Checking if both inputs are numerical
try:
    # Try to convert inputs to float
    base = float(input1)
    exponent = float(input2)
    
    # Using the add function and multiplying the result by 2
    addition_result = add(base, exponent) * 2
    print("The result of addition multiplied by 2 is:", addition_result)
    
    # Using the myPow function
    my_pow_result = myPow(base, exponent)
    print("The result of myPow is:", my_pow_result)
    
    # Checking against math.pow()
   math_pow_result = math.pow(base, exponent)
    print("The result of math.pow is:", math_pow_result)
    
    # Verifying if both results match
    if my_pow_result == math_pow_result:
        print("myPow() matches math.pow().")
    else:
        print("myPow() does not match math.pow().")
    
except ValueError:
    # If conversion fails, inform the user
    print("Please enter valid numerical values (int or float).")
