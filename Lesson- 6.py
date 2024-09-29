def calculate_result():
    # Ask user for their year of birth and age
    year_of_birth = int(input("Enter your year of birth:"))
    age = int(input("Enter your age: "))

    # Step 1: Double the birth year and add 5
    result = (year_of_birth * 2) + 5

    # Step 2: Multiply by 50 and add age
    result = (result * 50) + age

    # Step 3: Subtract 250
    result -= 250

    # Step 4: Divide by 100
    final_result = result / 100

    # Print the final result and interpretation
    print(f"The final result is: {final_result}")
    print(f"Interpretation: This number is an encoded version of your birth year and age, representing a unique identifier.")

# Call the function
calculate_result()
