import math

# finding the area of rectangle
length= int(input("enter the lenght of rectangle."))
# taking the input for tje length for the rectangle.

width= int(input("enter the width of rectangle. "))
# taking input for the width of the rectangle.

area= length*width
# Calculating the area of the rectangle.

print("the area of the rectangle with your input is", area)
# Printing the calculated area of the rectangle.


# finding the area of a circle
radius= float(input("input the radius of a circle. "))
# Taking input for the radius of the circle.

area= math.pi*(radius**2)
# Calculating the area of the circle (math.pi* r^2)

print("the area of the circle with radius. ",".%2f", area)
# Printing the area of the circle with 2 decimal precision.

# finding the surface area and volume of a cylinder
radius = float(input("Enter the radius of the cylinder: "))
# Taking input for the radius of the cylinder.

height = float(input("Enter the height of the cylinder: "))
# Taking input for the height of the cylinder.

volume = math.pi * radius **2 * height
# Calculating the volume of the cylinder (math.pi* r^2 *h )

surface_area = 2 * math.pi * radius * height + 2 * math.pi * radius **2
# Calculating the surface area of the cylinder.

print(f"The volume of the cylinder is: {volume:.2f}")
# Printing the volume of the cylinder with 2 decimal place.

print(f"The surface area of the cylinder is: {surface_area:.2f}")
# Printing the surface area of the cylinder with 2 decimals place.

# finding the period of pendulum
g= 9.8
# force of gravity.

L = float(input("Enter the lenght of the pendulum (in meters):"))
# Taking input for the length of the pendulum

P = 2 * math.pi* math.sqrt(L/g)
# Calculating the period of the pendulum.

print(f"Time period of the pendulum:{P:.2f} seconds")
# Printing the time period of the pendulum with 2 decimal place.
