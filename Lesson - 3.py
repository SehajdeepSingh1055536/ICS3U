# task 1 
print("Welcome to Sanjay's Koala Party!")
print("It's possible Sanjay can distribute", 12)
print("cookies for each bowl.")

# task 2
print("Sanjay has 6 bowls for 144 cookies.")

#task 3 
amount = 7 * 4
print("The number of cookies per bowl is",amount)

# tutorial

# This will get you by for now:
print("There are ", 28, " people in this room.");
print("Your total money spent is: ", (2.75+9.32+11.91))

# Using print is far more flexible. It uses 
# a format specifier %d to tell it to place an integer 
# there, but you also have to indicate the actual variable 
# after your quote:

# %d is a format specifier for type int
print("There are %d people in this room." % 28)
# %f is a format specifier for type double
print("Pi is equal to %f" % 3.1416)
# %s is for string
print("%s's final score is %d" % ("Joe", 215))

# Return the result of a calculation:
# %.2f restricts to two decimals.
print("Total money spent is: %.2f" % (2.75+9.32+11.91))
# %f is a format specifier for type double
print("The area of a circle of radius %d is %f" % (4, 3.1416*4*4))
