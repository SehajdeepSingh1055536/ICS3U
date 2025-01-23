def validate(N):
    digits = [int(d) for d in str(N)][::-1]  # Convert to list of digits and reverse
    
    total = 0
    for i, digit in enumerate(digits):
        if i % 2 == 1:  # Double every second digit
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit
    
    return total % 10 == 0

# User Input
num = input("Validate a number with the Luhn Algorithm!\nEnter any number: ")
if validate(num):
    print(f"{num} is a valid number.")
else:
    print(f"{num} is not a valid number.")
