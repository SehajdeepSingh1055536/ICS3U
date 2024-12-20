#Author - Sehajdeep
#Due date - 8 Nov, 2024
#Program - School Yearbook Assignment
#Description - This program helps determine the optimal layout
#(dimensions and minimum perimeter) for arranging a specified
#number of photographs in a rectangular grid. The program finds
#the layout with the smallest perimeter to conserve space.

#Variable Dictionary
#find_minimum_perimeter function
#n (int): The total number of photographs to arrange in the rectangle.
#min_perimeter (float): The current smallest perimeter found for possible layouts; initialized to infinity.
#best_x (int): The width of the rectangle layout yielding the minimum perimeter found so far.
#best_y (int): The height of the rectangle layout yielding the minimum perimeter found so far.
#max_factor (int): The largest factor of n we need to check,set to the floor of the square root of n for efficiency.
#x (int): The current factor of n in the iteration.
#y (int): The corresponding factor of n such that y = n // x.
#perimeter (int): The perimeter of the rectangle calculated with the dimensions x and y.
#main function
#user_input (str): The user’s input, which should be a positive integer or the keyword "done" to end the program.
#num_photos (int): The validated integer number of photographs, converted from user_input.



import math

def find_minimum_perimeter(n):
    # Initialize the minimum perimeter to a large number
    min_perimeter = float('inf')
    best_x, best_y = 1, n
    
    # We only need to iterate up to the square root of n to find factors
    max_factor = math.floor(math.sqrt(n))
    
    for x in range(1, max_factor + 1):
        if n % x == 0:
            y = n // x  # Find the corresponding y for the factor x
            perimeter = 2 * (x + y)  # Calculate the perimeter for this rectangle
            if perimeter < min_perimeter:
                min_perimeter = perimeter
                best_x, best_y = x, y

    return min_perimeter, best_x, best_y

def main():
    print("Welcome to the school yearbook program!")
    
    while True:
        user_input = input("Please input your number of photographs.")
        
        # Check for 'done' to end the program
        if user_input.lower() == "done":
            print("Goodbye!")
            break

        # Check if input is a positive integer
        try:
            num_photos = int(user_input)
            if num_photos <= 0:
                print(f"{num_photos} is not a valid number of photos. Please enter a positive number.")
                continue
        except ValueError:
            print("Invalid input. Please enter a positive integer or 'done' to exit.")
            continue
        
        # Find the minimum perimeter and dimensions
        min_perimeter, x, y = find_minimum_perimeter(num_photos)
        print(f"Minimum perimeter is {min_perimeter} with dimensions: {x} x {y}.")

# Run the program
main()
