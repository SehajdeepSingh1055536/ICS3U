print("Make a choice from the following menu: ")
print("A: apples")
print("B: bananas")
print("C: cherries")

ch = input("Your choice: ")

if (ch == "A"):
    print("I prefer apples")
elif (ch == "B"):
    print("I prefer bananas")
else:
    print("I prefer cherries")

# When we enter other letter than A,B,C (including numbers and symbol) it always come "I prefer cherries"

# Modify 1 
print("Make a choice from the following menu: ")
print("A: apples")
print("B: bananas")
print("C: cherries")
print("D: erroneous")

ch = input("Your choice: ")

if (ch == "A"):
    print("I prefer apples")
elif (ch == "B"):
    print("I prefer bananas")

elif ( ch =="C"):
    print("I prefer cherries")
else :
    print("I prefer erroneous")
    
# Modify 2 

grade = int(input("Enter a number between 1 and 100"))

if grade >= 80 and grade <=100:
  print("A")
elif grade >=70 and grade <=79:
  print("B")
elif grade >=60 and grade <=69:
  print("C")
elif grade >=50 and grade <=59:
  print("D")
elif grade >=1 and grade <=49:
  print("F")
else:
  print("Not a valid number")
