# 1
count = 9
while (count != 0):
    print(count)
    count -= 1

# 2
count = 9
while (count != 0):
    count -= 1
    print(count)

# the answers of these two come diiferent the 1 one start from 9 and end at 1. The 2 one start from 8 and end at 0.

# Part - B

# functions to calculate triangular numbers 
def triangular_number(n):
  return n*(n+1)//2
 
# Loop to print the first 6 triangular numbers  
for i in range(1,7):
  suffix = "th"
  if i ==1:
    suffix ="st"
  elif i==2:
    suffix = "nd"
  elif i==3:
    suffix = "rd"
    
  print(f"The {i}{suffix} triangular number is {triangular_number(i)}")
